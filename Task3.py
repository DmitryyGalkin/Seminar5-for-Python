"""3) Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

workers = {"Ivanov": 25040, "Petrov": 14544, "Sidorov": 27300, "lionov": 21253,
           "Semshov": 45018, "Kudrin": 18230, "Lazarev": 15110, "Lui": 12000,
           "Diogen": 22000, "Evklid": 22078}


def medium_salary(a, b):
    return a / b


with open("text_task3.exe", "w") as file_obj:
    for worker, salary in workers.items():
        file_obj.writelines(f"{worker}:{salary}\n")

looser = []
sum_salary = 0
count = 0
with open("text_task3.exe", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) < 20000:
            looser.append(tokens[0])
        sum_salary += int(tokens[1])
        count += 1
print(f"Сотрудники, зарплата которых менее 20000 {looser}")
print(
    f"Средняя величина доходов сотрудников {medium_salary(sum_salary, count)}")
