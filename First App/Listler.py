from email import message_from_bytes
import numbers
from re import A


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

#4. Mazda degerini Toyota ile degistirin 
#5. Mercedes listenin bir elemani midir 
#6. Listenin -2 indexsindeki deger nedir 
#7. Listenin ilk 3 elemanini alin 
#8. Listenin son 2 elemani yerine "Toyota" ve "Renault" degerlerini ekleyin
#9. listenin uzerine "Audi" ve "Nissan" degerlerini ekleyin
#10. Listenin son elemanini silin
#11. Liste elemanlarini tersten yazdiriniz
#12. Asagidaki verileri bir liste icinde saklayiniz 

    #studentA: Yigit Bilgi 2010, (70,60,70)
    #studentB: Sena Turan 1999, (80,80,70)
    #studentC: Ahmet Turan  1998, (80,70,90)


