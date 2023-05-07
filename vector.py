import os 
import time 
import math

def style_gpt(text):
    for i in text:
        print(i, end="") 
        time.sleep(0.1)

def clean_cmd():
    return os.system("cls||clear")

class OneVector: 

    def __init__(self, x, y):
        self.verify_coord(x)
        self.verify_coord(y)

        self.x = x
        self.y = y

        self.vector = (self.x, self.y)

    @classmethod 
    def verify_coord(cls, coord):
        if not isinstance(coord, int):
            try:
                raise TypeError(style_gpt("Координаты должны быть типа 'int'."))
            except:
                clean_cmd()
                exit()

    def line_vector(self):
        return style_gpt(f"Длина вектора {self.vector} : {round(math.sqrt((self.x ** self.x) + (self.y ** self.y)), 2)}")
    
    def operator_vector(self, num):
        new_vec = (self.x * num, self.y * num)
        style_gpt("Заменить текущий вектор на новый? (+ / -): ")

        q = input()
        clean_cmd()

        if q == "-":
            return style_gpt(f"Вектор {self.vector} умноженный на число {num}: {new_vec}")
        else:
            style_gpt(f"Вектор {self.vector} умноженный на число {num}: {new_vec}")
            self._vector = new_vec

    def div_vec(self, num):
        new_vec = (self.x / num, self.y / num)
        style_gpt("Заменить текущий вектор на новый? (+ / -): ")

        q = input()
        clean_cmd()
        if q == "-":
            return style_gpt(f"Вектор {self.vector} разделенный на число {num}: {new_vec}")
        else:
            style_gpt(f"Вектор {self.vector} разделенный на число {num}: {new_vec}")
            self._vector = new_vec

    @property 
    def change_vec(self):
        style_gpt(f"Текущий вектор: {self.vector}") 
    
    @change_vec.setter 
    def change_vec(self, new):
        self._vector = new

class TwoVector(OneVector):

    def __init__(self, part1, part2):

        OneVector.verify_coord(part1[0])
        OneVector.verify_coord(part1[1])
        OneVector.verify_coord(part2[0])
        OneVector.verify_coord(part2[1])

        self._part1 = part1 
        self._part2 = part2 

    def line_vector(self, vec):
        if vec == self._part1:
            return style_gpt(f"Длина вектора: {round(math.sqrt(self._part1[0] ** self._part1[0] + self._part1[1] ** self._part1[1]), 2)}")
        else:
            return style_gpt(f"Длина вектора: {round(math.sqrt(self._part2[0] ** self._part2[0] + self._part2[1] ** self._part2[1]), 2)}")

    def operator_vector(self, vec, num):
        if vec == self._part1:
            new_vec = (self._part1[0] * num, self._part1[1] * num)
            style_gpt("Заменить текущий вектор на новый? (+ / -): ")

            q = input()
            clean_cmd()

            if q == "-":
                return style_gpt(f"Вектор {self._part1} умноженный на число {num}: {new_vec}")
            else:
                style_gpt(f"Вектор {self._part1} умноженный на число {num}: {new_vec}")
                self._part1 = new_vec
        else:
            new_vec = (self._part2[0] * num, self._part2[1] * num)
            style_gpt("Заменить текущий вектор на новый? (+ / -): ")

            q = input()
            clean_cmd()

            if q == "-":
                return style_gpt(f"Вектор {self._part2} умноженный на число {num}: {new_vec}")
            else:
                style_gpt(f"Вектор {self._part2} умноженный на число {num}: {new_vec}")
                self._part2 = new_vec
    
    def div_vec(self, vec, num):
        if vec == self._part1:
            new_vec = (self._part1[0] / num, self._part1[1] / num)
            style_gpt("Заменить текущий вектор на новый? (+ / -): ")

            q = input()
            clean_cmd()

            if q == "-":
                return style_gpt(f"Вектор {self._part1} разделенный на число {num}: {new_vec}")
            else:
                style_gpt(f"Вектор {self._part1} разделенный на число {num}: {new_vec}")
                self._part1 = new_vec
        else:
            new_vec = (self._part2[0] / num, self._part2[1] / num)
            style_gpt("Заменить текущий вектор на новый? (+ / -): ")

            q = input()
            clean_cmd()

            if q == "-":
                return style_gpt(f"Вектор {self._part2} разделенный на число {num}: {new_vec}")
            else:
                style_gpt(f"Вектор {self._part2} разделенный на число {num}: {new_vec}")
                self._part2 = new_vec

    def summa_vec(self):
        return style_gpt(f"Сумма векторов: {self._part1[0] + self._part2[0], self._part1[1] + self._part2[1]}")    
    
    def sk_vec(self):
        return style_gpt(f"Скалярный множитель векторов: {self._part1[0] * self._part2[0] + self._part1[1] * self._part2[1]}")    

    def coliner_vec(self):
        if self._part1[0] / self._part2[0] == self._part1[1] / self._part2[1]:
            return style_gpt("Вектора коллинеарны.")
        else:
            return style_gpt("Вектора не коллинеарны.")

    def all_stats(self):
        style_gpt(f"Общий результат для векторов ({self._part1}, {self._part2})\n")
        for i in [self.summa_vec, self.sk_vec, self.coliner_vec]:
            yield i

    @property 
    def change_vec1(self):
        style_gpt(f"Текущий вектор: {self._part1}") 
    
    @change_vec1.setter 
    def change_vec1(self, new):
        self._part1 = new

    @property 
    def change_vec2(self):
        style_gpt(f"Текущий вектор: {self._part2}") 
    
    @change_vec2.setter 
    def change_vec2(self, new):
        self._part2 = new

#Конец кода связаного с классами 

clean_cmd()
gpt_word = style_gpt("Кол-во векторв --> ")
work_vector = int(input())
clean_cmd()


if work_vector == 1:
    gpt_word = style_gpt("Введите координаты ('через пробел'): ")
    x, y = input().split()
    clean_cmd()
    v = OneVector(int(x), int(y))

    while True: 

        clean_cmd()
        gpt_word = style_gpt("Действия: \n1)Длина вектора\n2)Умножить вектор на число\n3)Разделить вектор на число\n4)Текущий вектор\n5)Выйти\nВыберите цыфру --> ")
        oper = int(input())
        clean_cmd()

        if oper == 5:
            break 
        elif oper == 1:
            v.line_vector()
            time.sleep(1)
        elif oper == 2:
            gpt_word = style_gpt("Введите число --> ")
            num = int(input())
            clean_cmd()
            v.operator_vector(num)
            time.sleep(1)
        elif oper == 3:
            gpt_word = style_gpt("Введите число --> ")
            num = int(input())
            clean_cmd()
            v.div_vec(num)
            time.sleep(1)
        elif oper == 4:
            v.change_vec
            time.sleep(1)
            clean_cmd()
        else:
            try:                
                raise TypeError(style_gpt("Выбранно неправильное действие!"))
            except:
                clean_cmd()
else:
    gpt_word = style_gpt("Введите координаты ('через пробел'): ")
    x1, y1, x2, y2 = input().split()
    part1 = (int(x1), int(y1))
    part2 = (int(x2), int(y2))
    v2 = TwoVector(part1, part2)
    clean_cmd()

    while True:
        style_gpt(f"С чем работаем?\n1)Вектор №1 {part1}\n2)Вектор №2 {part2}\n3)С двумя сразу\n4)Выйти\nВыберите цыфру --> ")
        res = int(input())
        clean_cmd()

        if res == 4:
            break
        elif res == 1:
            while True:

                clean_cmd()
                gpt_word = style_gpt("Действия: \n1)Длина вектора\n2)Умножить вектор на число\n3)Разделить вектор на число\n4)Текущий вектор\n5)Выйти\nВыберите цыфру --> ")
                oper = int(input())
                clean_cmd()
                if oper == 5:
                    break
                elif oper == 1:
                    v2.line_vector(part1)
                    time.sleep(1)
                elif oper == 2:
                    gpt_word = style_gpt("Введите число --> ")
                    num = int(input())
                    clean_cmd()
                    v2.operator_vector(part1, num)
                    part1 = v2._part1
                    time.sleep(1)
                elif oper == 3:
                    gpt_word = style_gpt("Введите число --> ")
                    num = int(input())
                    clean_cmd()
                    v2.div_vec(part1, num)
                    part1 = v2._part1
                    time.sleep(1)
                elif oper == 4:
                    v2.change_vec1
                    time.sleep(1)
                    clean_cmd()
                else:
                    try:                
                        raise TypeError(style_gpt("Выбранно неправильное действие!"))
                    except:
                        clean_cmd()
        elif res == 2:
            while True:

                clean_cmd()
                gpt_word = style_gpt("Действия: \n1)Длина вектора\n2)Умножить вектор на число\n3)Разделить вектор на число\n4)Текущий вектор\n5)Выйти\nВыберите цыфру --> ")
                oper = int(input())
                clean_cmd()
                if oper == 5:
                    break
                elif oper == 1:
                    v2.line_vector(part2)
                    time.sleep(1)
                elif oper == 2:
                    gpt_word = style_gpt("Введите число --> ")
                    num = int(input())
                    clean_cmd()
                    v2.operator_vector(part2, num)
                    part2 = v2._part2
                    time.sleep(1)
                elif oper == 3:
                    gpt_word = style_gpt("Введите число --> ")
                    num = int(input())
                    clean_cmd()
                    v2.div_vec(part2, num)
                    part2 = v2._part2
                    time.sleep(1)
                elif oper == 4:
                    v2.change_vec2
                    time.sleep(1)
                    clean_cmd()
                else:
                    try:                
                        raise TypeError(style_gpt("Выбранно неправильное действие!"))
                    except:
                        clean_cmd()
        elif res == 3:
            for i in v2.all_stats():
                i() 
                print()
            clean_cmd()
        else:
            try:                
                raise TypeError(style_gpt("Выбранно неправильное действие!"))
            except:
                clean_cmd()
