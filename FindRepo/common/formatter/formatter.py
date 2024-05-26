from typing import List
import ast


class FormatterPerRequest:
    def __init__(self):
        pass


    @staticmethod
    def delete_forbidden_char(raw_object: str) -> str:
        '''Удаляет запрещенные для запроса символы'''
        github_forbidden_char: List = [".", ",", ":", ";", "/", "\\", "'",
                                    '"', "=", "*", "!", "?", "#", "$", "&"
                                    "+", "^", "|", "~", "<", ">", "(", ")",
                                    "{", "}", "[", "]", "@", '`', '-']

        for ch in github_forbidden_char:
            raw_object = raw_object.replace(ch, '')
        return raw_object


    def _delete_empty_lines(self, raw_object: str) -> str:
        '''Удаляет пустые строки'''

        lines: List = raw_object.split('\n')

        clear_lines: List = list()

        for line in lines:
            if line.strip():
                clear_lines.append(line)

        return '\n'.join(clear_lines)


    def format(self, raw_object: str) -> str:
        '''Стандартизирует объект'''

        new_object: str = self._delete_empty_lines(raw_object)

        return new_object


class FormatterPerHash(ast.NodeTransformer):
    def __init__(self):
        self._in_func = 0
        self._func_counter = 1
        self._func_names = {}
        self._import_names = []
        self._global_var_counter = 1
        self._global_var_names = {}
        self._func_var_counter = 1
        self._func_var_names = {}
        self._cur_func_globals = []

    def format(self, code):
        tree = ast.parse(code)
        formated_tree = self.visit(tree)
        self.fix_imports(formated_tree)
        return ast.unparse(formated_tree)

    def visit_Import(self, node):
        for n in node.names:
            self._import_names.append(n.name)
        return None

    def visit_Name(self, node):
        if type(node.ctx) is ast.Store:
            if self._in_func and node.id not in self._cur_func_globals:
                if node.id in self._func_var_names:
                    node.id = self._func_var_names[node.id]
                else:
                    self._func_var_names[node.id] = 'funcvar' + str(self._func_var_counter)
                    self._func_var_counter += 1
                    node.id = self._func_var_names[node.id]
            else:
                if node.id in self._global_var_names:
                    node.id = self._global_var_names[node.id]
                else:
                    self._global_var_names[node.id] = 'var' + str(self._global_var_counter)
                    self._global_var_counter += 1
                    node.id = self._global_var_names[node.id]
            return node

        if node.id in self._func_names:
            node.id = self._func_names[node.id]
        elif self._in_func and node.id not in self._cur_func_globals:
            if node.id in self._func_var_names:
                node.id = self._func_var_names[node.id]
        else:
            if node.id in self._global_var_names:
                node.id = self._global_var_names[node.id]
        return node

    def visit_AnnAssign(self, node):
        if isinstance(node.target, ast.AST):
            self.visit(node.target)
        new_node = ast.Assign(targets=[node.target], value=node.value)
        return ast.copy_location(new_node, node)

    def visit_Expr(self, node):
        if type(node.value) is ast.Constant and type(node.value.value) is str:
            return None
        elif type(node.value) is ast.Call:
            self.visit(node.value)
        return node

    def visit_BinOp(self, node):
        if type(node.left) is ast.Name:
            self.visit(node.left)

        if type(node.right) is ast.Name:
            self.visit(node.right)

        if type(node.left) is ast.Constant and type(node.right) is ast.Constant:
            if type(node.op) is ast.Add:
                new_value = node.left.value + node.right.value
            if type(node.op) is ast.Sub:
                new_value = node.left.value - node.right.value
            if type(node.op) is ast.Mult:
                new_value = node.left.value * node.right.value
            if type(node.op) is ast.Div:
                if node.right.value != 0:
                    new_value = node.left.value / node.right.value

            new_node = ast.Constant(value=new_value, kind=None)
            return ast.copy_location(new_node, node)
        return node

    def visit_FunctionDef(self, node):
        self._in_func = 1

        for arg in node.args.args:
            self._func_var_names[arg.arg] = 'funcvar' + str(self._func_var_counter)
            self._func_var_counter += 1
            arg.arg = self._func_var_names[arg.arg]

        new_body = node.body
        size = 0
        for n in new_body:
            size += 1
            if type(n) is ast.Global:
                self._cur_func_globals.extend(n.names)
                for i, name in enumerate(n.names):
                    n.names[i] = self._global_var_names[name]
                continue
            self.visit(n)
            if type(n) is ast.Return:
                break
        node.body = new_body[:size]
        new_name = 'func' + str(self._func_counter)

        self._func_names[node.name] = new_name
        node.name = new_name
        self._func_counter += 1

        self._cur_func_globals = []
        self._in_func = 0
        return node

    def visit_Call(self, node):
        if node.func.id in self._func_names:
            node.func.id = self._func_names[node.func.id]
        for arg in node.args:
            if isinstance(arg, ast.AST):
                self.visit(arg)
        return node

    def fix_imports(self, node):
        if self._import_names:
            names = []
            self._import_names.sort()
            for n in self._import_names:
                names.append(ast.alias(name=n, asname=None))
            import_node = ast.Import(names=names)
            node.body.insert(0, import_node)
