import random
i = 0

def word_mixer():
    global i
    word = input("what word would you like to mix ==>")
    list_word,mixer = [],[];
    for char in word:
        list_word.append(char)
        mixer.append(char)
    random.shuffle(mixer)
    print(mixer)
    print(list_word)
    while mixer != list_word:
        i = i + 1
        print(mixer)
        print(i)
        random.shuffle(mixer)

    print("took "+str(i)+" tries to match")

def number_sorter():
    global i
    num_list = []
    lenght = int(input("how many numbers would you like to sort ==>"))
    for i in range(1,lenght):
        num = int(input("==>"))
        num_list.append(num)
    sortedd = sorted(num_list)
    while num_list != sortedd:
        print(num_list)
        print("try number {}".format(i))
        random.shuffle(num_list)
        i = i + 1
    print("took "+str(i)+" tries to match")
    print(num_list)

print("1--word mixer\n2--number sorter")
choose = int(input("==>"))
if choose == 1:
    word_mixer()
elif choose == 2:
    number_sorter()
else:
    print("just 1 or 2 :|")
bogo()