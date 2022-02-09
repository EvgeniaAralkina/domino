# класс 1ой доминошки
# a - левое число
# b - правое
# status - поменяли или нет ( + - не менли, - меняли)
class Node:

    def __init__(self, a, b, status):
        """Constructor"""
        self.a = a
        self.b = b
        self.status = status

# функция для переворота доминошки, меняются числа и статус
    def change_status(self):
        c = self.a
        self.a = self.b
        self.b = c
        self.status = '-' if self.status=='+' else '+'


# функция которя все делает
# answ - массив с последовательностью доминошек которую уже выложили
# ost - массив с оставшимися доминошками
# return 0 - не удалось найти подходящую доминошку
# return answ - последовательность доминошек
def foo(answ, ost):
    # for k in answ: print(k.a, k.b)
    # print('-')
    #
    # for j in ost: print(j.a, j.b)
    # print(len(ost))
    # print('---')

# условие выхода - нет невыложенных доминошек
    if len(ost) == 0:
         return answ
# проходим по остатку и ищем доминошку которую можно добавить в начало или в хвост цепочки
    for i in range(len(ost)):
        # левое число первой доминошки совпадает с правым числом доминошки из остатка
        # (ставим в начало и не переворачиваем)
        if (answ[0].a == ost[i].b):
            answ.insert(0,ost[i]) # добавляем доминошку к последовательности
            ost.remove(ost[i]) # удаляем ее из остатка
            res = foo(answ,ost) # рекурсивно вызываем ту же функцию
            if res == 0: # если не нашли подходящей доминошки
                ost.insert(i, answ[0]) # возвращаем ту доминошку в остаток
                answ.remove(answ[0]) # и убираем ее из ответа
            else: return answ # все ок, прерываем дальнейшее выполнение и возвращем answ

        # правое число последней доминошки совпадает с левым числом доминошки из остатка
        # (ставим в конец и не переворачиваем)
        if (answ[-1].b == ost[i].a):
            answ.append(ost[i])
            ost.remove(ost[i])
            res = foo(answ, ost)
            if res == 0:
                ost.insert(i, answ[-1])
                answ.pop()
            else: return answ
        # левое число первой доминошки совпадает с левым числом доминошки из остатка
        # (ставим в начало и переворачиваем)
        if answ[0].a == ost[i].a:
            ost[i].change_status()
            answ.insert(0, ost[i])
            ost.remove(ost[i])
            res = foo(answ, ost)
            if res == 0:
                ost.insert(i, answ[0])
                answ.remove(answ[0])
            else: return answ
        # правое число последней доминошки совпадает с правым числом доминошки из остатка
        # (ставим в конец и переворачиваем)
        if answ[-1].b == ost[i].b:
            ost[i].change_status()
            answ.append(ost[i])
            ost.remove(ost[i])
            res = foo(answ, ost)
            if res == 0:
                ost.insert(i, answ[-1])
                answ.pop()
            else: return answ
    return 0


if __name__ == '__main__':
    ostatok = [] # остаток - невыложенные доминошки, после прочтения ввода тут будут все кроме первой
    answ = [] # answ - массив с выложенными, после прочтеия ввода тут будет только первая
    while True:
        t = input()
        if t:
            i = t.split()
            ostatok.append(Node(i[0],i[1],'+'))
        else:
            break
    answ.append(ostatok[0])
    ostatok.pop(0)
    
    res = foo(answ, ostatok)
    if res==0: print("Решения нет!")
    else:
        for i in res:
            print (i.a, i.b, i.status)