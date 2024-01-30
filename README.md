# FindRepo

Позволяет находить файлы по фрагменту кода, используя API github и gitlab.

# Пример работы:

Файл tic_tac_toe.py содержит: 
```
def func():
    print("hello")

func()
```

Запрос:
```
python3 main.py -file "/tic_tac_toe.py" -max_count 5
```

Ответ:
```
github result: https://github.com/preetu391/master-in-python-with-dsa/blob/c96e40d490a7954223e3ad002819cb66654dba55/exceptionHandling.py
gitlab result: https://gitlab.com/andres-kaldo/tic_tac_toe https://gitlab.com/ours1/tictactoe https://gitlab.com/intz1/tictactoe https://gitlab.com/viljar2/TicTacToe https://gitlab.com/sda-learn-anton/tictactoe
```
