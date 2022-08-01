ogrenciler={}

number =input("ogrenci no : ")

name=input('ogrenci adi :')
surname = input('ogrenci soyad: ')
phone = input('ogrenci telefon: ') 


# 3 tane ogrenci girmek icin 
ogrenciler[number] = {
    'ad':  name,
    'soyad': surname,
    'telefon': phone
}

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone
    }
})


number =input("ogrenci no : ")
name=input('ogrenci adi :')
surname = input('ogrenci soyad: ')
phone = input('ogrenci telefon: ') 


ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone
    }
})


number =input("ogrenci no : ")
name=input('ogrenci adi :')
surname = input('ogrenci soyad: ')
phone = input('ogrenci telefon: ') 


ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone
    }
})

print(ogrenciler)


