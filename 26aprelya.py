from ast import Return
from operator import is_
from re import A


def arr1():
    s=input()
    list1 = s.split(',')
    list2=[]
    for i in range(len(list1)):
        list2.append(input())
    
    d = dict(zip(list1, list2))
    return d

def sorddict(a):
    return sorted(a, key=a.get, reverse=True)[:3] 

def is_year_leap(a):
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    #print(arr1())
    #print(sorddict({'a': 500, 'b': 5874, 'c': 560,'d': 400, 'e': 5874, 'f': 20}))
    print(is_year_leap(1764))
    print(is_year_leap(1700))