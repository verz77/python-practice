import os 

def save_tasks(tasks):
    with open("todo.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    tasks = []
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                tasks.append(line)
    return tasks

#меню/ввод 1 
def show_tasks(tasks):
    if len(tasks) == 0:
        print("Дел нет")
    else:
        number = 0
        for task in tasks:
            number = number + 1 
            print(f"{number}. {task}")

def add_task(tasks):
    text = input("Что добавить: ")
    text = text.strip()
    if text != "":
        tasks.append(text)
        print("Добавлено")
    else:
        print("Пустое дело не добавлено")

def remove_task(tasks):
    if len(tasks) == 0:
        print("Удалять нечего")
    else:
        show_tasks(tasks)
        text = input("Номер для удаления: ").strip()
        if text.isdigit():
            number = int(text)
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Удалено")
            else:
                print("Нет такого номера")
        else:
            print("Нет такого номера")

tasks = load_tasks()
while True:
    print("\n=== Список дел ===")
    print("1 - Показать дела")
    print("2 - Добавить дело")
    print("3 - Удалить дело")
    print("0 - выход")
    choice = input("Выбор: ")

    if choice == "0":
        break
    elif choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
        save_tasks(tasks)
    elif choice == "3":
        remove_task(tasks)
        save_tasks(tasks)
    else:   
        print("Неверный выбор")

print("Пока!")
