class soda():
    def __init__(self, ingredient):
        if isinstance(ingredient,str):
            self.ingredient = ingredient
        else:
            self.ingredient = None
    
    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print('Обычная газировка')  


class calcclass():
    def __init__(self, num1, num2, operation):
        self.num1 = num1
        self.num2= num2
        self.operation = operation
        
    def calc(self):    
        if self.operation == '+':
            return self.num1+self.num2
        elif self.operation == '-':
            return self.num1-self.num2
        elif self.operation == '*':
            return self.num1*self.num2
        elif self.operation == '/':
            return self.num1/self.num2
        else:
            return 'Неизвестная операция'

if __name__ == "__main__":
    #drink1 = soda('')
    #drink2 = soda('клубника')
    #drink1.show_my_drink()
    #drink2.show_my_drink()
    calc1=calcclass(1,2,'+')
    calc2=calcclass(5,5,'*')
    print(calc1.calc())
    print(calc2.calc())
