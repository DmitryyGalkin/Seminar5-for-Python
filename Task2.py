"""2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

my_list = ["Когда-то нас было много \n", "потом стало двое \n", "теперь "
                                                                "один \n"]
with open("text_2.txt", "w") as f_obj:
    f_obj.writelines(my_list)
with open("text_2.txt", "r") as f_obj:
    lines = 0
    words = 0
    for line in f_obj:
        lines += line.count("\n")
        words += line.count(" ")
        print(f"В строке {words} слов(-ва)")
    print(f"В файле {lines} строк и {words} слов")
