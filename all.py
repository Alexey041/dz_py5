#1
#Напишите программу, удаляющую из текста все слова, содержащие ""абв""

with open ('file.txt', 'r', encoding='utf-8') as file:
    some_str = file.readline()

some_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not \
    in i, some_str.split()))

print(some_list)

#2
#Создайте программу для игры в ""Крестики-нолики""

def input_user_x(line1, line2, line3, x):
    count_x = 0
    while count_x == 0:
        for i in range(3):
            if line1[i] == x:
                line1[i] = 'x'
                count_x = 1
        for j in range(3):
            if line2[j] == x:
                line2[j] = 'x'
                count_x = 1
        for k in range(3):
            if line3[k] == x:
                line3[k] = 'x'
                count_x = 1

        if count_x == 0:
            print('Сюда поставить нельзя!')
            print(line1)
            print(line2)
            print(line3)
            x = int(input('Поставьте X '))
        
    return line1, line2, line3

def input_user_o(line1, line2, line3, o):
    count_o = 0
    while count_o == 0:
        for i in range(3):
            if line1[i] == o:
                line1[i] = 'o'
                count_o = 1
        for j in range(3):
            if line2[j] == o:
                line2[j] = 'o'
                count_o = 1
        for k in range(3):
            if line3[k] == o:
                line3[k] = 'o'
                count_o = 1

        if count_o == 0:
            print('Сюда поставить нельзя!')
            print(line1)
            print(line2)
            print(line3)
            o = int(input('Поставьте O '))
        
    return line1, line2, line3

def winner(line1, line2, line3):
    winner_ind = 0  #1-X, 2-O, 0-ничья
    if line1 == ['x', 'x', 'x'] or line2 == ['x', 'x', 'x'] or line3 == ['x', 'x', 'x']:
        winner_ind = 1
    if line1 == ['o', 'o', 'o'] or line2 == ['o', 'o', 'o'] or line3 == ['o', 'o', 'o']:
        winner_ind = 2
    if line1[0] == 'x' and line2[0] == 'x' and line3[0] == 'x':
        winner_ind = 1
    if line1[0] == 'o' and line2[0] == 'o' and line3[0] == 'o':
        winner_ind = 2
    if line1[1] == 'x' and line2[1] == 'x' and line3[1] == 'x':
        winner_ind = 1
    if line1[1] == 'o' and line2[1] == 'o' and line3[1] == 'o':
        winner_ind = 2
    if line1[2] == 'x' and line2[2] == 'x' and line3[2] == 'x':
        winner_ind = 1
    if line1[2] == 'o' and line2[2] == 'o' and line3[2] == 'o':
        winner_ind = 2
    if line1[0] == 'x' and line2[1] == 'x' and line3[2] == 'x':
        winner_ind = 1
    if line1[2] == 'x' and line2[1] == 'x' and line3[0] == 'x':
        winner_ind = 1    
    if line1[0] == 'o' and line2[1] == 'o' and line3[2] == 'o':
        winner_ind = 1
    if line1[2] == 'o' and line2[1] == 'o' and line3[0] == 'o':
        winner_ind = 1
    return winner_ind

line1 = [1, 2, 3]
line2 = [4, 5, 6]
line3 = [7, 8, 9]

print(line1)
print(line2)
print(line3)

count = 0
while winner(line1, line2, line3) == 0:
    x = int(input('Поставьте Х '))
    input_user_x(line1, line2, line3, x)
    print(line1)
    print(line2)
    print(line3)
    winner(line1, line2, line3)
    count += 1
    if winner(line1, line2, line3) != 0:
        break

    o = int(input('Поставьте O '))
    input_user_o(line1, line2, line3, o)
    print(line1)
    print(line2)
    print(line3)
    winner(line1, line2, line3)
    count += 1
    if winner(line1, line2, line3) != 0:
        break
        
    if count == 8:
        break

if winner(line1, line2, line3) == 1:
    print('Победили крестики')
if winner(line1, line2, line3) == 2:
    print('Победили нолики')
if winner(line1, line2, line3) == 0:
    print('Победила дружба')

#3
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах. 
 
def compression(some_list): 
    count = 1 
    result_list = [] 
    for i in range(len(some_list) - 1): 
        if some_list[i] == some_list[i + 1]: 
            count += 1 
        if some_list[i] != some_list[i + 1]: 
            result_list.append(f'{count}{some_list[i]}') 
            count = 1 
 
    i += 1 
    if some_list[i] == some_list[i - 1]: 
        result_list.append(f'{count}{some_list[i]}') 
    else: 
        count = 1 
        result_list.append(f'{count}{some_list[i]}') 
 
    return result_list 
 
def decompression(some_list): 
    count_list = [] 
    value_list = [] 
    res_list = [] 
    for i in range(0, len(some_list), 2): 
        count_list.append(some_list[i]) 
        count_list_int = list(map(int, count_list)) 
    for j in range(1, len(some_list), 2): 
        value_list.append(some_list[j]) 
    for k in range(len(count_list_int)): 
        res_list.append(value_list[k] * count_list_int[k]) 
    return res_list 
 
def list_to_str(some_list): 
    result_str = ''.join(some_list) 
    return result_str 
 
 
with open('input.txt', 'r', encoding='utf-8') as file: 
    b = file.readline() 
    some_list = list(b.strip()) 
    compression_str = ''.join(str(x) for x in compression(some_list)) 
 
with open('output.txt', 'r+', encoding='utf-8') as file1: 
    file1.write(compression_str) 
 
with open('output.txt', 'r+', encoding='utf-8') as file1:
    b1 = file1.readline() 
    some_list2 = list(b1.strip()) 
 
with open('input.txt', 'r+', encoding='utf-8') as file: 
    file.write(list_to_str(decompression(some_list2))) 