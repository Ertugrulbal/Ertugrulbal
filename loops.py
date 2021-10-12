# numbers = [1,3,5,7,9,12,19,21]
# toplam=0
# for num in numbers:
#     toplam += num  
# print(toplam)
# for num in numbers:
#     if num%2==1:
#         square= num**2
#         print(square)
# *********************
# cities=['kocaeli','istanbul','ankara','izmir','rize']

# # for i in cities:
# #     if len(i)<=5:
# #         print(i)
# products= [
#     {'name':'samsung s6', 'price':'3000'},
#     {'name':'samsung s7', 'price':'4000'},
#     {'name':'samsung s8', 'price':'5000'},
#     {'name':'samsung s9', 'price':'6000'},
#     {'name':'samsung s10', 'price':'7000'}
# ]
# # toplam = 0
# # for urun in products:
# #     toplam += int(urun['price'])
# # print(toplam)
# for urun in products:
#     if int(urun['price'])<=5000:
#         print(urun['name'],urun['price'])
  
# *********************************
#         SAMPLES

# sayilar = [1,3,5,7,9,12,19,21]

# i=0

# while i<(len(sayilar)):
#     print(sayilar[i])
#     i+=1
    
# ***************************************
# begin= int(input('Bir başlangıç değeri giriniz: '))
# end= int(input('bir bitiş değeri giriniz: '))


# while end>begin:
#         begin+=1
#         print(begin)
# ********************************
# i=100

# while i>0:
#     print(i)
#     i -= 1
# *****************************
# num1= int(input("1. sayıyı giriniz: "))
# num2= int(input("2. sayıyı giriniz: "))
# num3= int(input("3. sayıyı giriniz: "))
# num4= int(input("4. sayıyı giriniz: "))
# num5= int(input("5. sayıyı giriniz: "))
# numbers= []
# i=0
# while i<5:
#     sayı= int(input("Lütfen bir sayı giriniz!: "))
#     numbers.append(sayı)
#     i+=1
# # list.sort()
# numbers.sort()
# print(numbers)
# *****************Benim Yaptığım*************
# urunsayısı= int(input("kaç adet ürün olacak: "))

# ürünListe= []

# i=0
# while i<urunsayısı:
#      urunler=input('product: '),input('price: ')
#      ürünListe.append({
#          urunler
#          })
#      i+= 1
# **************Hocanın Yaptığı***************
# urunler= []
# urunadeti= int(input("Kaç adet ürün girmek istiyorsunuz: "))
# i=0

# while i<urunadeti:
#     name= input("Lütfen bir ürün adı giriniz: ")
#     price= input("Lütfen ürün fiyatını giriniz: ")
#     urunler.append({
#         'name': name,
#         'price': price
#     })
#     i+=1
# for urun in urunler:
#     print(f"urun adı: {urun['name']}, ürün fiyatı: {urun['price']}")
# **********************************BREAK AND CONTINUE**************
# summation= 0
# x=1

# while x<=100:
#     x+=1
#     if x%2==1:
#         continue
#     summation+=x
# print(summation)
# **********************************************************
# for item in range(0,10,1):
#     print(item)
# ***********************************

# Greetings= 'Hello'

# for index,item in enumerate(Greetings):
#     print(f"The index number: {index} and item: {item}")
    # *************************************
# zip
# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# list3 =[10,20,30,40,50]

# # print(list(zip(list1,list2,list3)))
# for a,b,c in zip(list1,list2,list3):
#     print(a,c)