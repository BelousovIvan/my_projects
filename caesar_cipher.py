# test
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

# функция считает длину слова без учета символов
def lenght(text):
    total = 0
    for i in text:
        if "a" <= i <= "z" or "A" <= i <= "Z":
            total += 1
    return total

vvod = input().split()
[cesars_shifr_eng_right(vvod[i], lenght(vvod[i])) for i in range(len(vvod))]