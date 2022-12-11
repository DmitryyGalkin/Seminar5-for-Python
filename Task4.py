"""4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл."""

num = {"One": 1, "Two": 2, "Three": 3, "Four": 4}
num_translate = ["Один", "Два", "Три", "Четыре"]
result = []
count = 0
with open("text_task4.txt", "w") as file_obj:
    for number, digit in num.items():
        file_obj.writelines(f"{number} - {digit}\n")

with open("text_task4.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split('-')
        if tokens[0] in line:
            word = num_translate[count]
            result.append(f"{word} - {tokens[1]}")
            count += 1
    print(result)
with open("text_translate.txt", "w") as file_obj:
    file_obj.writelines(result)
