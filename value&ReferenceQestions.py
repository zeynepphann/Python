from unittest import result


x, y, z=2, 5, 10

numbers=1,5,7,10,6

#1. kullanicidan aldiginiz 2 sayinin carpimi ile x,y,z toplaminin farki nedir 

   #a = int(input('1. sayi: '))
   #b = int(input('2. sayi: '))
   #result=(a*b)-(x+y+z)


#2. y'nin x'e kalansiz bolumunu hesaplayiniz 
    #result= y // x

#3.(x,y,z) toplaminin mood 3'u nedir? 
   #toplam = (x+y+z)
   #result=toplam % 3


#4. y'nin x. kuvvetini hesaplayiniz
   #result = y**x


#5. x, *y,z= numbers islemine gore z'nin kupu kactir?
   #numbers = 1, 5, 7, 10, 6
   #x, *y ,z = numbers
   #result = z ** 3




#6. x, *y,z= numbers islemine gore y'nin degerleri toplami kactir? 
numbers = 1, 5, 7, 10, 6
x, *y ,z = numbers
result=y[0] + y[1] + y[2]

print(result)