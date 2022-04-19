"1.Ввести произвольную строку в консоль."
str1=str(input())
new_line = str()

"2. Циклом пройтись по всем символам этой строки"
for s in str1:
    print(s, end='')
print()

"3. Пропустить 3-й символ"
for s in range(len(str1)):
    if s == 2:
        continue
    new_line += str1[s]
print(new_line)     

"4. Если есть символ 'c', вывести сообщение об этом."
if 'c' in str1:
    print(True)
else:
    print(False)

"5. Не выводить последний символ в строке."
print(str1[:len(str1)-1])