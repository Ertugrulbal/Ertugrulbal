import random

randomNumber= random.randint(0,100)

hak= int(input("Hak sayısını giriniz: "))
soruPuanı=100//hak
print(randomNumber)

while hak > 0:

    tahmin= int(input("Lütfpuan= hak*soruPuanıen bir tahmin giriniz: "))
    puan= hak*soruPuanı
    if randomNumber == tahmin:
        print("BULDUNUZ!")
        break
    elif (randomNumber < tahmin):
        print("asagı inin!")
    else:
        print("yukarı çıkın!")
        
    hak=hak-1
    if hak==0:
        print("kaybettin")