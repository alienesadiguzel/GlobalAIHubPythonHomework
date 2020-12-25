
name = input("Plz enter your name:")

word=input(" Welcome {}\n Plz enter a word: ".format(name))#Kullanıcıdan bir kelime istedim.
program=True #Programın akışını kontrol etmek için tanımladım.
wrongGuess=0 #Yanlış tahmin sayısını tanımladım.
charList=list(word) #List yapısına çevirip daha kolay kontrol sağlamayı amaçladım.
lenght=len(charList) #Uzunluğu program kontrolü için kullandım.

while program:
    for char in range (1,11):
        inputChar = input("Plz enter a char: ")
        if inputChar in charList:
            print("The word have this char!")
            lenght -=1 #burada her doğru cevapta bir harf eksilttim.
            if lenght == 0: #sıfır olduğunda tüm harfleri biliyor ve oyunu kazanıyor.
                print("You Won! The word is {}".format(word))
                program=False
        else:
            print("The word haven't this char!")
            wrongGuess+=1 #Yanlış tahmin sayısı artıyor
            if wrongGuess==10: #yanlış tahmin 10 olduğunda oyunu sonlandırdım.
                print("Game Over!")
                program = False










