# создал простой класс для работы с двумя числами

class Operation:
    """Класс для работы с числами, умеет складывать, вычитать, делить, умножать и находить остаток 
        от деления двух чисел"""
    # иницилизируем два числа
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    # функция для сложения двух чисел
    def addition(self):
        return self.x + self.y

    # функция для вычитания одного числа из другого
    def subtraction(self):
        return self.x - self.y
    
    # функция для деления одного числа на дрогое
    def division(self):
        return self.x / self.y
    
    # функция для умножения двух чисел
    def multiplication(self):
        return self.x * self.y
    
    # функция для нахождения остатка от деления
    def reminder(self):
        return self.x % self.y
    