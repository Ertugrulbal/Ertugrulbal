sayı = int(input("Bir sayı giriniz: "))
for i in range(2,sayı):
    if sayı%i==0:
        print(f"{sayı} is not asal number")
        break
if sayı%i!=0:
        print(f"{sayı} is a asal number")
      
            