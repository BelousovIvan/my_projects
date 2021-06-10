# программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля,
# а также на то, какие символы требуется в него включить, а какие исключить.

import random

def generate_password(length, chars):
    print(*[random.choice(chars) for _ in range(length)], sep="")

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""
n = int(input("Сколько паролей надо создать? "))
k = int(input("Длина каждого пароля? "))
d = int(input("Включать ли цифры? 1 - Да / 2 - Нет: "))
l = int(input("Включать ли прописные буквы? 1 - Да / 2 - Нет: "))
j = int(input("Включать ли строчные буквы? 1 - Да / 2 - Нет: "))
m = int(input("Включать ли символы? 1 - Да / 2 - Нет: "))
p = int(input("Исключать ли неоднозначные символы iIlL1oO0? 1 - Да / 2 - Нет: "))
if d == 1:
    chars = chars + digits
if l == 1:
    chars = chars + uppercase_letters
if j == 1:
    chars = chars + lowercase_letters
if m == 1:
    chars = chars + punctuation
if p == 1:
    chars = "".join([i for i in chars if i not in "iIlL1oO0"])

print("Пароли созданы:")
[generate_password(k, chars) for i in range(n)]
