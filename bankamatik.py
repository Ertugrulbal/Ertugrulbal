ertugrulHesap= {
    'ad':'Ertugrul',
    'hesapNo':'1234334',
    'bakiye': 3000,
    'ekHesap': 2000
}
nihatHesap= {
    'ad':'Nihat',
    'hesapNo':'12354421',
    'bakiye': 4000,
    'ekHesap': 3000,
}

def paracekme(hesap, Miktar):
    if hesap['bakiye'] >= Miktar:
        print(f"{hesap['hesapNo']} nolu hesabınızdan para çekebilirsiniz.")
        hesap['bakiye']-= Miktar
        print(bakiyeSorgulama(nihatHesap))

        # print(f"{hesap['hesapNo']} nolu hesabınızda kalan miktar {hesap['bakiye']} TL kadardır.")
    else:
        toplam= hesap['bakiye']+hesap['ekHesap']

        if toplam>= Miktar:           
            devam_mı= input("Devam etmek istiyor musunuz? (e/h)")
            if devam_mı=='e':
                kalan_miktar= Miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-= kalan_miktar 
                # print(f"{hesap['hesapNo']} nolu hesabınızda kalan ek hesap tutarınız {hesap['ekHesap']} TL kadardır.")
                print(bakiyeSorgulama(nihatHesap))
            else:
                print("İyi günler dileriz...")
        else:
            print("Bakiyeniz yetersizdir.")    
def bakiyeSorgulama(hesap):
    print(f"{hesap['hesapNo']} hesap No'lu hesabın bakiyesi {hesap['bakiye']} TL kadardır. Ayrıca Ek Hesapta da {hesap['ekHesap']} TL kadar bulunmaktadır.")



paracekme(nihatHesap, 4000)


print('*****************')

paracekme(nihatHesap, 1000)