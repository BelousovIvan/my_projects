import random

def is_valid(digit):
    if digit.isdigit() and 1 <= int(digit) <= n:
        return True
    else:
        return False

n = int(input("Добро пожаловать в числовую угадайку, напишите целое число - правая граница чисел: "))
n1 = random.randint(1, n)
print(n1)
number = input("Угадайте целое число от 1 до " + str(n) + ", которое загадал компьютер: ")
total = 0

while True:
    if not is_valid(number):
        number = input("А может быть все-таки введем целое число от 1 до " + str(n) + "? ")
        continue
    total += 1
    if int(number) > n1:
        number = input("Слишком много, попробуйте еще раз: ")
        continue
    elif int(number) < n1:
        number = input("Слишком мало, попробуйте еще раз: ")
        continue
    else:
        print("Вы угадали с", total, "попытки, поздравляем!")
        question = input("y - новая игра, n - закончить игру: ")
        if question == "y":
            n = int(input("Ура! Продолжаем играть! Напишите целое число - правая граница чисел: "))
            n1 = random.randint(1, n)
            print(n1)
            number = input("Угадайте целое число от 1 до " + str(n) + ", которое загадал компьютер: ")
            total = 0
            continue
        elif question == "n":
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            break
