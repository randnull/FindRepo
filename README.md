# FindRepo

Программное обеспечение для поиска источника по файлам.

![GitHub top language](https://img.shields.io/github/languages/top/randnull/FindRepo)

# Краткое описание

Для проверки на наличие в открытых источниках можно использовать как один файл, так и папку с файлами. По результатам проверки будет сгенерирован отчет, в котором будут указаны найденные файлы.  


# Глобальный поиск

Глобальный поиск происходит по внешним ресурсам, таким как Google и Github.

# Локальный поиск

Локальный поиск происходит по собственной базе данных. После поиска (если не было найдено похожего в базе) файлы можно также добавить в базу данных. Помимо этого, если требуется поиск только по своим запросам, возможно поднять собственный севрер с базой данных.


# Примеры запросов

Пример запроса на глобальный поиск:

```
make global file=Users/User/Files/File.py args="-save_path Users/User/results"
```

Пример отчета по глобальному поиску:

```
{
    "Report": {
        "path": "/Users/kirillgorunov/Documents/test",
        "search_type": "global",
        "status": "Founded",
        "result_1": {
            "link": "https://example.com/1",
            "match": 4
        },
        "result_2": {
            "link": "https://example2.com/2",
            "match": 3
        },
    }
}
```

Пример запроса на локальный поиск:

```
make local file=Users/User/Files/File.py args="-save_path Users/User/results -read_only -source example.com/example/example"
```

Пример отчета по локальному поиску:

```
{
    "Report": {
        "path": "/Users/kirillgorunov/Documents/test",
        "search_type": "local",
        "status": "Founded",
        "result_1": {
            "link": "/Users/kirillgorunov/Documents/test",
            "match": 1.0
        }
    }
}
```

