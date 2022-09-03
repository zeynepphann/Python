# value types => string, number 

x= 5 
y= 25

# burda bir nevi konteynir islemi uyguluyoruz 
x=y

y = 10

#print(x,y)

#referens types
a= ["apple","banana"]
b= ["apple","banana"]

a=b

b[0]= "grape"

print(a,b)


x,y,z = 5,10,20
x,y = y,x
x+=5 # x = x + 5
x-=5 # x = x - 5
x*=5 # x = x * 5
x/=5 # x = x / 5
x%=5 # x = x % 5
x//=5 # x = x // 5  kalani kusuratsiz alir 
x**=5 # x = x ** 5 5 kere x carpip sonuc verir

values = 1,2,3

print(values)
print(type(values))

x, y, z= values

print(x,y,z)











