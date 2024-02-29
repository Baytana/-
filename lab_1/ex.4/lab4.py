#4. Уникальные слова. Напишите программу, которая открывает заданный текстовый файл и затем показывает список 
# всех уникальных слов в файле. (Подсказка: храните слова в качестве элементов множества.)

file_name = "file_text.txt"
ans_set = []
with open(file_name, "r") as file:
    words = file.read().split()
for i in words:
    if i not in ans_set:
        ans_set.append(i)
       
print(' '.join(ans_set))