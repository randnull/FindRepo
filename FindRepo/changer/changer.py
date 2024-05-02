import ast
import astunparse


class ASTChanger(ast.NodeTransformer):
    def __init__(self):
        self._func_counter = 1
        self._import_names = []

    def visit_Import(self, node):
        for n in node.names:
            self._import_names.append(n.name)
        return None

    def visit_AnnAssign(self, node):
        new_node = ast.Assign(targets=[node.target], value=node.value)
        return ast.copy_location(new_node, node)

    def visit_Expr(self, node):
        if type(node.value) is ast.Constant and type(node.value.value) is str:
            return None
        return node

    def visit_BinOp(self, node):
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

    '''
    def visit_FunctionDef(self, node):
        self._functions_list.append(node.name)
        return None
        ...
    
    '''

    def visit_FunctionDef(self, node):
        node.name = 'func' + str(self._func_counter)
        self._func_counter += 1
        return node

    def fix_imports(self, node):
        if self._import_names:
            names = []
            self._import_names.sort()
            for n in self._import_names:
                names.append(ast.alias(name=n, asname=None))
            import_node = ast.Import(names=names)
            node.body.insert(0, import_node)


if __name__ == '__main__':
    i = open('input.txt', 'r')
    o = open('output.txt', 'w')
    tree = ast.parse(i.read())
    #print(astunparse.dump(tree))
    changer = ASTChanger()
    trans_tree = changer.visit(tree)
    changer.fix_imports(trans_tree)
    res = ast.unparse(trans_tree)
    o.write(res)
    i.close()
    o.close()
