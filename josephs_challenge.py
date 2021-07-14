# Задача Иосифа Флавия.
# По кругу стоит n воинов, начиная с первого воина они убивают каждого k-го воина.
# Спрашивается, в каком месте нужно встать, чтобы остаться последним выжившим.
# Название задачи восходит к истории, случившейся с Иосифом Флавием во время Иудейской войны.


n = int(input())
k = int(input())
list = [i for i in range(1, n+1)]

while len(list) != 1:
    if k == 1:
        print(n)
        exit()
    elif k > len(list):
        list[(k - (k // len(list)) * len(list) - 1)] = 0
        list = list[(k - (k // len(list)) * len(list)):] + list[:(k - (k // len(list)) * len(list))]
    elif k <= len(list):
        for i in list:
            if (list.index(i)+1) % k == 0:
                list[(list.index(i))] = 0
        list = list[(len(list) // k) * k:] + list[:(len(list) // k) * k]
    while 0 in list:
        list.remove(0)

print(f"Нужно встать на {list[0]} месте")