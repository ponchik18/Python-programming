import re

string = input("Введите строку последовательностьей цифр от 0 до 9: ")
string = re.sub(r'\D+', r'', string)
dictionary_of_number=dict()
for i in range(10):
    number_str=str(i)
    dictionary_of_number.update({i : string.count(number_str)})
print(dictionary_of_number)
