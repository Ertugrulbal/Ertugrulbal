import datetime
bugün = datetime.datetime.today()
tarih= input("aracınızın trafige cikis tarihini giriniz(2021/09/28): ")
tarih= tarih.split('/')
trafigeCikis= datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
day= bugün - trafigeCikis
fark= day.days
if (fark<365):
    print('1. servis gelmiştir!')
elif (fark > 365) and (fark < 365*2):
    print('2. servis gelmiştir!')
elif (fark > 365*2) and (fark < 365*3):
    print('3. servis gelmiştir!')
else:
    print('hatalı tarih girdiniz!')