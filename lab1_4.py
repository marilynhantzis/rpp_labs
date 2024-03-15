input_sequence = input('Введите последовательность чисел: ')
i=0
sum_sequence = []
temp = ''
while i < len(input_sequence.strip()):
    #print('Итерация: ', i)
    str = input_sequence[i]
    #print(str)
    if str != ' ':
        temp += str
    else:
        sum_sequence.append(int(temp))
        temp=''
    i+=1
    if i==len(input_sequence.strip()):
        if temp != '':
            sum_sequence.append(int(temp))
sum_sequence_len = len(sum_sequence)
i2 = 0
final_sum = 0
final_count = 0
while i2 < sum_sequence_len:
    final_sum+=sum_sequence[i2]
    i2+=1
print('Сумма элементов:', final_sum)
print('Количество элементов:', i2)



