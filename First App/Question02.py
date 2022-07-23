

import re


course="Python kursu questions'lari"
website="http://www.sadikturan.com"
#1.'course' karakter dizisinde kac karakter bulunmaktadir?
result=len(course)
lengt=len(website)

#2.'website' icinden www karakterlerini alin.
result=website[7:10]

#3.'website' icinde com karakterlerini alin
result=website[21:24]
result=website[lengt-3:lengt]

#4. 'course' icinden ilk 15 ve son 15 karakterlerini alin 
result = course[0:15]
result = course[:15]
result = course[-15:]

result = course[-15:-1]
#5. 'course' ifadesindeki karakterleri tersten yazdirin.
result = course[::-1]

s= '12345' * 5
print(result)
print(s[::5])

name, surname, age, job='Bora', 'Yilmaz',"32" , 'muhendis'

#6. Yukarida verilen degiskenler ile ekrana asagidaki ifadeyi yazdirin
# Benim adim Bora Yilmaz, yasim 32 ve meslegim muhendis

result = "Benim adim "+ name + " " + surname + ",Yasim " + age+ " ve meslegim " + job 
print(result)

#7. 'Hello world' ifadesindeki w harfini "W" ile degistirin
s='Hello world' 
s =s[0:6]+ 'W'+ s[-4:]
print(s)
