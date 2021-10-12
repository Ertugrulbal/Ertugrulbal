ogrenciler = {}

number= input('öğrenci no: ')
name= input ('ad soyad: ')
surname= input('soyad: ')
telefon = input('telefon no: ')

ogrenciler.update({
    number:{
       'ad': name,
       'soyad': surname,
       'telefon': telefon
    }
})
number= input('öğrenci no: ')
name= input ('ad soyad: ')
surname= input('soyad: ')
telefon = input('telefon no: ')

ogrenciler.update({
    number:{
       'ad': name,
       'soyad': surname,
       'telefon': telefon
    }
})
number= input('öğrenci no: ')
name= input ('ad soyad: ')
surname= input('soyad: ')
telefon = input('telefon no: ')

ogrenciler.update({
    number:{
       'ad': name,
       'soyad': surname,
       'telefon': telefon
    }
})


print('*'*50)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(f"aradığınız {ogrNo} nolu öğrenciniz {ogrenci['ad']} {ogrenci['soyad']}'dir ve telefon numarası {ogrenci['telefon']}'dur")