"Задача 1"

def zad1(array):
    count=0
    for a in range(1,len(array)-1):
        if array[a]>array[a-1] and array[a]>array[a+1]:
            count+=1
    return count
"Задача 2, если смотреть со стороны какого ты стоишь в строю, то там быть 0 человека не может, поэтому делаем +1"
def zad2(array,x):
    count = array.count(x)
    array.append(x)
    array.sort(reverse=True)
    if count==0:
        return array.index(x)+1
    else:
        return array.index(x)+count+1
"3 задача"
def zad3():
    x = list()
    y = list()
    flag="NO"
    for i in range(8):
        _x, _y = [int(s) for s in input().split()]
        x.append(_x)
        y.append(_y)

    for i in range(8):
        for j in range(i+1,8):
            if x[i]==x[j] or y[i]==y[j] or abs(x[i]-x[j]) == abs(y[i]-y[j]):
                flag = 'YES'
    return flag

"4 задача"
def zad4(x1,y1,x2,y2):
    return (((x1-x2)**2)+((y1-y2)**2))**0.5

"5 задача"
def zad5(a,n):
    if n==0:
        return 1
    else:
        return a*zad5(a,n-1)

def zad6(*args):
    new_dict = dict()
    for i in args:
        client, thing, value = i.split()
        if not new_dict.get(client):
            new_dict[client] = dict()
        if not new_dict[client].get(thing):
            new_dict[client][thing]=int(value)
        else:
            new_dict[client][thing]+=int(value)
    return new_dict

def zad7():
    n = int(input())
    language = list()
    for i in range(n):
        k = int(input())
        safe = set()
        for j in range(k):
            safe.add(input())
        language.append(safe)
    
    unical_language = set.union(*language)
    total = set.intersection(*language)
    return len(total), sorted(total), len(unical_language), sorted(unical_language)

if __name__ == "__main__":
    #print(zad1([1,4,2,1,4,3,5,2,7]))
    #print(zad2([171,178,170,170,170,198,157],170))
    #print(zad3())
    #print(zad4(2,-5,-4,3))
    #print(zad5(2,4))
    #print(zad6("Ivanov paper 10","Petrov pens 5","Ivanov marker 3","Ivanov paper 7","Petrov envelope 20","Ivanov envelope 5"))
    print(zad7())