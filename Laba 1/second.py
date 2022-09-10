import re

string = str(input("Введите текст: "))
result_list = re.split(r'\W+', string)
for i in range(len(result_list)):
    if result_list[i] == '':
        result_list.remove('')

print("Количество введённых слов = ", len(result_list))

glas_list = ['а', 'о', 'у', 'и', 'ы', 'ё', 'я', 'ю', 'э', 'е']
string_copy = re.sub(r'\d+', r'', string)
result_list = re.split(r'\W+', string_copy)
count_of_glas = int(0)
count_of_coglas = int(0)

for index in range(len(result_list)):
    word = result_list[index]
    for index_of_letter in range(len(word)):
        if word[index_of_letter].lower() in glas_list:
            count_of_glas += 1
        else:
            count_of_coglas +=1


print("Количество согласных букв = ", count_of_coglas)
print("Количество гласных букв = ", count_of_glas)