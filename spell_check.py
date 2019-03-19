import spell_check

# string_test = "Пришло теплое лето. На лисной опушки распускаюца колоколчики, незабутки, шыповник. Белые ромашки пратягивают к сонцу свои нежные лепески. Вылитают из уютных гнёзд птинцы. У зверей взраслеет смена. Мидвежата старше всех."

bed_words = []

string_test = input("Введите строку: ")
string_test = string_test.split()
for i in range(len(string_test)):
    string_test[i] = string_test[i].strip(".,\"\'")
    # print(string_test[i])

    if string_test[i].lower() not in spell_check.russ:
        # print("no")
        bed_words.append(string_test[i])
        # print(string_test[i])

print(bed_words)