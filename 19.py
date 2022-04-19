"1.Ввести произвольную строку в консоль."
str1=str(input())
print('-'*10)
print(str1)

print('-'*10)

"2. Циклом пройтись по всем символам этой строки"
for s in str1:
    print(s, end='')

print()
print('-'*10)

"3. Пропустить 3-й символ"
for s in str1:
    if str1.index(s) == 2:
        continue
    else:
        print(s, end='')
print()
print('-'*10)
"4. Если есть символ 'c', вывести сообщение об этом."
if 'c' in str1:
    print(True)
else:
    print(False)
    
print('-'*10)

"5. Не выводить последний символ в строке."
print(str1[:len(str1)-1])