# программа способна шифровать и дешифровать текст в соответствии с алгоритмом "шифр Цезаря".
# Она должна запрашивать у пользователя следующие данные:
# - направление: шифрование или дешифрование;
# - язык алфавита: русский или английский;
# - шаг сдвига (со сдвигом вправо).

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# функция шифрует русский текст со сдвигом вправо
def cesars_shifr_rus_right(str1, n):
    for i in range(len(str1)):
        if (str1[i] in rus_lower_alphabet) and ord(str1[i])+n <= 1103:
            print(chr(ord(str1[i])+n), end="")
        elif (str1[i] in rus_upper_alphabet) and ord(str1[i])+n <= 1071:
            print(chr(ord(str1[i])+n), end="")
        elif (str1[i] in rus_lower_alphabet) and ord(str1[i])+n >= 1103:
            print(chr(ord(str1[i])+n-32), end="")
        elif (str1[i] in rus_upper_alphabet) and ord(str1[i])+n >= 1071:
            print(chr(ord(str1[i])+n-32), end="")
        else:
            print(str1[i], end="")

# функция дешифрует русский текст со сдвигом влево
def cesars_shifr_rus_left(str1, n):
    for i in range(len(str1)):
        if (str1[i] in rus_lower_alphabet) and ord(str1[i])-n >= 1072:
            print(chr(ord(str1[i])-n), end="")
        elif (str1[i] in rus_upper_alphabet) and ord(str1[i])-n >= 1040:
            print(chr(ord(str1[i])-n), end="")
        elif (str1[i] in rus_lower_alphabet) and ord(str1[i])-n <= 1072:
            print(chr(ord(str1[i])-n+32), end="")
        elif (str1[i] in rus_upper_alphabet) and ord(str1[i])-n <= 1040:
            print(chr(ord(str1[i])-n+32), end="")
        else:
            print(str1[i], end="")

# функция шифрует английский текст со сдвигом вправо
def cesars_shifr_eng_right(str1, n):
    for i in range(len(str1)):
        if (str1[i] in eng_lower_alphabet) and ord(str1[i])+n <= 122:
            print(chr(ord(str1[i])+n), end="")
        elif (str1[i] in eng_upper_alphabet) and ord(str1[i])+n <= 90:
            print(chr(ord(str1[i])+n), end="")
        elif (str1[i] in eng_lower_alphabet) and ord(str1[i])+n >= 122:
            print(chr(ord(str1[i])+n-26), end="")
        elif (str1[i] in eng_upper_alphabet) and ord(str1[i])+n >= 90:
            print(chr(ord(str1[i])+n-26), end="")
        else:
            print(str1[i], end="")

# функция дешифрует английский текст со сдвигом влево
def cesars_shifr_eng_left(str1, n):
    for i in range(len(str1)):
        if (str1[i] in eng_lower_alphabet) and ord(str1[i])-n >= 97:
            print(chr(ord(str1[i])-n), end="")
        elif (str1[i] in eng_upper_alphabet) and ord(str1[i])-n >= 65:
            print(chr(ord(str1[i])-n), end="")
        elif (str1[i] in eng_lower_alphabet) and ord(str1[i])-n <= 97:
            print(chr(ord(str1[i])-n+26), end="")
        elif (str1[i] in eng_upper_alphabet) and ord(str1[i])-n <= 65:
            print(chr(ord(str1[i])-n+26), end="")
        else:
            print(str1[i], end="")

print("Привет!", end=" ")
while True:
    k = int(input("Ты хочешь зашифровать послание или дешифровать? 1 - шифровать / 2 - дешифровать: "))
    l = int(input("Послание будет на русском или на английском языке? 1 - русский / 2 - английский: "))
    n = int(input("Какой будет шаг сдвига? "))
    str1 = input("Введи послание: ")
    if k == 1 and l == 1:
        print("Шифрование русского послания со сдвигом " + str(n) + ": ", end=" ")
        cesars_shifr_rus_right(str1, n)
    elif k == 2 and l == 1:
        print("Дешифрование русского послания со сдвигом " + str(n) + ": ", end=" ")
        cesars_shifr_rus_left(str1, n)
    elif k == 1 and l == 2:
        print("Шифрование английского послания со сдвигом " + str(n) + ": ", end=" ")
        cesars_shifr_eng_right(str1, n)
    elif k == 2 and l == 2:
        print("Дешифрование английского послания со сдвигом " + str(n) + ": ", end=" ")
        cesars_shifr_eng_left(str1, n)
    print()
    q = int(input("Требуется ли обработать ещё одно послание? 1 - да / 2 - нет: "))
    if q == 1:
        continue
    elif q == 2:
        print("Рад был помочь, пока!")
        break