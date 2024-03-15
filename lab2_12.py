input_string = input("Введите произвольную строку: ")
words = []
i=0
temp = ''
while i < len(input_string.strip()):
    #print('Итерация: ', i)
    str = input_string[i]
    #print(str)
    if str != ' ':
        temp += str
    else:
        words.append(temp)
        temp=''
    i+=1
    if i==len(input_string.strip()):
        if temp != '':
            words.append(temp)
words_ending_with_u = [word for word in words if word.endswith('u')]
print(f"Слова, оканчивающиеся на 'u': {words_ending_with_u}")