import random
import time


eng_words = ['Hi','Bye','Task', 'Programm']
in_words = ['Halo','Sampai jumpa','Tugas', 'Program']
score = 0

mode = input("Pilih mode: 0 - tambahkan kata baru, 1 - pelatihan: \n")
while ((mode != '0') and (mode != '1')):
    mode = input("Simbol tidak valid! Pilih antara 0 atau 1. (0 menambahkan kata baru, sedangkan 1 mengaktifkan pelatihan) \n")

if mode == "1":
    print("Terjemahkan kata sebanyak mungkin! Kamu punya 10 kesempatan!")
    for i in range(10):
        number = random.randint(0, len(eng_words)-1)
        print("Bagaimana seharusnya kita menerjemahkan: " + eng_words[number])
        if input() == in_words[number]:
            print("Hebat!!!")
            score += 1
        else:
            print("Tidak, tidak mendekati... Kata yang benar adalah - " + in_words[number])
        print ("Score kamu", score)
else:
    word = input("Ketik kata bahasa Inggris: ")
    translate = input("Ketik terjemahan kata ini: ")
    if len(word) > 0 and len(translate) > 0:
        eng_words.append(word)
        in_words.append(translate)
        print("Kata berhasil ditambahkan!")
        

