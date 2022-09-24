# 1. girilen 2 sayidan hangisi buyuktur?

     #a = int(input('a: '))
     #b = int(input('b: '))

     #result = a > b
     #print(f'a:{a} b:{b} den buyuktur:{result}')

# 2. kullanicidan 2 vize(%60) ve final(%40) notunu alip ortalama hesaplayiniz?
# eger ortalama 50 ve ustundeyse gecti degilse kaldi yazdirin

   #vize1 = float(input('1.vize : '))
   #vize2 = float(input('2.vize : '))
   #final = float(input('final : '))
   #ortalama =((vize1+vize2) /2 * 0.6) + (final * 0.4)

   #print(f'not ortalamaniz : {ortalama} ve dersten gecme durumunuz : {ortalama>=50}')


# 3. Girilen bir sayinin tek mi cift mi oldugunu yazdirin

    #sayi = int(input('sayi:'))
    #tekcift = (sayi % 2== 0)
    #print (f'girilen sayi cift olma durumu : {tekcift}')


# 4. Girilen bir sayinin negatif mi pozitif mi oldugunu yazdirin
#sayi = int( input('sayi: '))
# pozitifmi=(sayi> 0)
# print(f'girilen sayinin pozitif olma durumu {pozitifmi}')


# 5. Parola ve email bilgisini isteyip dogrulugunu kontrol ediniz
#   (email zynphn@gmail.com  password: '12345' )
from unicodedata import is_normalized


email= 'zynphn@gmail.com'
password='12345'

girilenEmail =input ('email: ')
girilenPassword= input('parola: ')

isEmail=(email==girilenEmail.lower()) # lower girileni kucuk harfe cevirir
isPassword = (password==girilenPassword.strip()) # strip aradaki bosluklari hiclige cevirmek icin kullanilir

print(f'Email bilgisi dogrumu : {isEmail} ve parola dogru mu : {isPassword} ')


