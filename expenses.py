#ВВОД 1 
text = input('введите траты:')
expenses = []
for p in text.split():
    expenses.append(int(p))
#ПОДСЧЕТ 2
total = 0
for expense in expenses:
    total = total + expense

average = total / len(expenses)

biggest = expenses[0]
smallest = expenses[0]
days_above = 0 
for expense in expenses:
    if expense > biggest:
        biggest = expense 
    if smallest > expense:
        smallest = expense
    if expense > average:
        days_above = days_above + 1

biggest = expenses[0]
biggest_day = 1 
day = 0
for expense in expenses:
    day = day + 1 
    if expense > biggest:
        biggest = expense 
        biggest_day = day 
#ВЫВОД 3 
print("Недельные траты")
print(F"Общая сумма: {total}")
print(F"Средний расход в день: {average:.2f}")
print(F'Самая большая трата: {biggest}')
print(F'Самая маленькая трата: {smallest}')
print(F"Дней потрачено больше среднего: {days_above}")
if total > 5000:
    print("Бюджет превышен")
else:
    print("В Бюджете")
print(F"В какой день самая большая трата: {biggest_day}")
