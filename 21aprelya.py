from ctypes.wintypes import PINT
from hashlib import new
import re


def calc(a,b,operation):
    if operation == '+':
        return a+b
    elif operation == '-':
        return a-b
    elif operation == '*':
        return a*b
    elif operation == '/':
        return a/b
    else:
        return 'Неизвестная операция'


def polindrom(a):
    a = str(a).lower()
    if a == a[::-1]:
        return 'Слово - полиндром'
    else:
        return 'Слово не является полиндромом'

def spisok(a):
    new_list = []
    for i in a:
        if i>5:
            new_list.append(i)
    return new_list

def bottle(n):
    a={0:'бутылок', 1:'бутылка', 2: 'бутылки', 3:'бутылки', 4:'бутылки',5:'бутылок', 6: 'бутылок', 7: 'бутылок', 8: 'бутылок', 9: 'бутылок'}
    while n!=0:
        b = n%10
        c = (n-1)%10
        if n==15:
            c = 0
        if n==11 or n==12 or n==13 or n==14:
            b = 0
            c = 0
        print('На столе стояло',n,a[b], '1 бутылка упала', n - 1,a[c], 'осталось на столе')
        n-=1

if __name__ == "__main__":
    print(calc(1,1,'+'))
    print(calc(2,1,'-'))
    print(calc(16,2,'/'))
    print(calc(3,3,'*'))
    print(calc(1,1,':'))
    print(polindrom("ШаЛаш"))
    print(polindrom("Корова"))
    print(spisok([0, 4, 78, 2, 1, 1, 13, 21, 34, 55, 89, 167]))
    print(bottle(100))