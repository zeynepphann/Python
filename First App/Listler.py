from email import message_from_bytes
import numbers
from re import A
import re


message = 'Hello There. My name is Zeynep Han'.split()
print(message) # suan index ile kelimelere ulasilabilir
print(message[0])

my_list = [1,2,3]
my_list1 = ['bir',2,True,5.6]
print(my_list)
print(my_list1)

list1= ['one','two','three']
list2= ['four','five','six']

numbers=list1+list2
print(numbers)
print(len(numbers)) # listede kac eleman oldugunu yazdirir


userA = ['Zeynep', 23]
userB = ['Zendaya', 25]

users=[userA, userB]

print(userA)
print(userB)
print(users)
print(users[1])

a=users[1] #liste seklinde olan users icerisinden sadece zendaya'ya ulasmak icin 
print(a[0])
#or
print(users[1][0])




#1. 'BMW, Mercedes, Opel, Mazda' elemanlarina sahip bir liste olusturunuz 
arabalar=['BMW', 'Mercedes', 'Opel', 'Mazda']

#2. Liste kac elemanlidir?
result = len(arabalar)
print(result)

#3. listenin ilk ve son elemanini nedir
result1= arabalar[0]
result2= arabalar[3]
result3= arabalar[-1] #ayni zamanda son eleman index -1 dir 

#4. Mazda degerini Toyota ile degistirin 
arabalar[-1]= 'Toyota'
result4 = arabalar

#5. Mercedes listenin bir elemani midir 
result5= 'Mersedes' in arabalar #boolean sonuc dondurur

#6. Listenin -2 indexsindeki deger nedir
result6= arabalar[-2]

#7. Listenin ilk 3 elemanini alin 
result7= arabalar[0:3]
result8= arabalar[:3]
result9= arabalar[-2:]

#8. Listenin son 2 elemani yerine "Toyota" ve "Renault" degerlerini ekleyin
arabalar[-2:]=['Toyota','Renault']
print(arabalar)

#9. listenin uzerine "Audi" ve "Nissan" degerlerini ekleyin
result10 =arabalar + ['Audi','Nissan']

#10. Listenin son elemanini silin
del arabalar[-1]
result11=arabalar
print(arabalar)

#11. Liste elemanlarini tersten yazdiriniz
result12=arabalar[::-1]
print(result12)

#12. Asagidaki verileri bir liste icinde saklayiniz 

    #studentA: Yigit Bilgi 2010, (70,60,70)
    #studentB: Sena Turan 1999, (80,80,70)
    #studentC: Ahmet Turan  1998, (80,70,90)

studentA=['Yigit', 'Bigi',2010,[70,60,70]]
studentB=['sena', 'turan',1999,[80,80,70]]
studentC=['ahmet', 'turan',1998,[80,70,90]]

result13=studentA[0]
result14=studentB[1]
result15=studentC[3][1]

result16= f"{studentA[0]}{studentA[1]} {2022-studentA[2]} yasinda ve not ortalamasi {studentA[3][0] + studentA[3][1]+studentA[3][2]/3}"
print(result16)
