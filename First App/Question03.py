from calendar import c
import re
from unittest import result


course = "Python kursu questions'lari"
website = "http://www.sadikturan.com"

# 1. ' Hello World ' karakter dizisinin bas ve sondaki bosluk karakterlerini silin
result = 'Hello World'.split()
result = ' Hello World '.rsplit()
result = website.lstrip('/:pyh')
print(result)
# 2. 'www.sadikturan.com' icindeki sadikturan bilgisi haricindeki her karakteri silin
result1 = 'www.sadikturan.com'.strip('w.moc')
print(result1)

#3. 'course' karakter dizisinin tum karakterlerini kucuk harf yazin 
result2 =course.lower()
result3 =course.upper()
result4 =course.title()

#4. 'website' icinde kac tame a karakteri vardir 
result5= website.count('a')
result5= website.count('www')
result5= website.count('www',0,10)
print(result5)

#5. 'website ' "www" ile baslayip com ile bitiyor mu ?
result6= website.startswith('www')
result7= website.endswith('com')

#6. 'website' icinde '.com' ifadesi var mi?
result8=website.find('com') # index numarasini dondurur
result9=website.find('com',0,10)
result10=course.find('Python')  
result10=course.rfind('Python')  #r sagdan aramaya baslamasini saglar 

result11= website.index('com')
result12= website.rindex('com')

#7.'course' icindeki karakterlerin hepsi alfabetik mi?(isalpha, isdigit)
result13= course.isalpha()
result14='Hello'.isalpha()
result15=course.isdigit()
result16='123'.isdigit()

#8.'Contents' ifadesini satirda 50 karakter icine yerkestirip sag ve soluna * ekleyiniz 
result17='Contents'.center(50,'*')
result18='Contents'.ljust(50,'*') # sola yaslayip geri kalan kisma yildiz ekler 
result19='Contents'.rjust(50,'*') # saga yaslayip geri kalan kisma yildiz ekler 

#9. 'course' karaket dizisindeki tum bosluk karakterlerini '-' ile degistirin 
result20=course.replace(' ','-') 
result21=course.replace(' ','-',5) # 3. sayi sinir belirler 
result22=course.replace(' ','') 

#10. 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak degistirin 
result23='Hello World'.replace('World','There')

#11. 'course' karakter dizisini bosluk karakterlerinden ayirin
result24=course.split(' ')

