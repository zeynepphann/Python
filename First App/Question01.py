'''1. Question
Daire Alani: πr2
Daire Cevresi: 2πr

*Yari capi verilen bir dairenin 
alan ve cevresini hesaplayiniz (r: 3.14)
'''

from turtle import st
from unicodedata import name


# pi=3.14
# r=float(input("yari cap: ")) 

# alan= pi*(r**2)
# cevre= 2*pi*r

# print("alan",alan)
# print("yariCap",cevre)


# bir str da ilk karakteri yazdiriniz 

# str="python"

# print(str.len)
# print("ilk karakter; "+str[0])

# # str'in kac karakterli oldugunu yazdiriniz
# length=len(str)
# print("strin uzunlugu "+ len(str))

# # #str'in son karakterini yazdiriniz 
# print("str;in son karakteri "+ str[length-1])

# print(str[3:5])
# print(str[3:5:2]) # sonraki 2 karakterlerin alinis sayisidir iki karakterden bir karakter alir 


#-----------------------------------------------------------------------#
name = 'Zendaya'
surname = 'Han'

print('my name is {0} {1}' .format(name,surname))
print('my name is {1} {0}' .format(name,surname))
print('my name is {s} {n}' .format(n=name,s=surname))
print('my name is {} {} and im {} years old.' .format(name,surname,'36'))


result= 200/50
print('the result is {} '.format(result))
print('the result is {r:5:3} '.format(result))

#5=bosluk birakmak icin 
#3=virgulden sonraki basamak sayisini belirtir


