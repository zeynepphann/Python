from cgitb import reset
from re import S
import re
from unittest import result


names = ['Ali','Yagmur','Hakan','Deniz']
years = [1998,2000,1998,1987]

# 1. "Cenk" ismini listenin sonuna ekleyiniz 
names.append('Cenk')
print(names)

# 2. "Sena" degerini listenin basina ekleyiniz 
names.insert(0, 'Sena')
print(names)


# 3. "Deniz" ismini listeden siliniz.
names.remove('Deniz') #or name.pop('Deniz') pop listenin sonundaki elemani siler 
print(names) 

# 4. "Deniz" isminin indexi nedir? 
index = names.index('Deniz')
print(index)

# 5. "Ali" listenin bir elemani midir? 
result= 'Ali' in names 
result = names.index('Ali')
print(result)

# 6. Listenin elemanlarini ters ceviriniz 
names.reverse()
print(names)

# 7. Liste elemanlarini alfabetik olarak siralayiniz 
names.sort()

# 8. years listesini rakamsal buyukluge gore siralayiniz 
years.sort()

# 9. str= "Chevrolet, Dacia" karakter dizisini listeye cevriniz 
str= "Chevrolet,Dacia"
result=str.split(',')
print(result)

#10. years dizisinin en buyuk ve en kucuk elemani nedir?
min = min(years)
max = max(years)

#11. years dizisinde kac tane 1998 degeri vardir ?
result = years.count(1998)

#12. years dizisinin tum elemanlarini siliniz 
years.clear()

#13. Kullanicidan alacaginiz  3 tane marka bilgisini bir listeye saklayiniz 
markalar= []
marka= input("marka: ")
markalar.append(marka)