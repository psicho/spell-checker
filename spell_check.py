import dict_rus

# string_test = "Пришло теплое лето. На лисной опушки распускаюца колоколчики, незабутки, шыповник. Белые ромашки " \
#               "пратягивают к сонцу свои нежные лепески. Вылитают из уютных гнёзд птинцы. У зверей взраслеет смена. " \
#               "Мидвежата старше всех."

bad_words = []

string_test = input("Введите текст: ")
string_test = string_test.split()

for i in range(len(string_test)):
    string_test[i] = string_test[i].strip(".,\"\'")

    if string_test[i].lower() not in dict_rus.russ:
        bad_words.append(string_test[i])

print(bad_words)
