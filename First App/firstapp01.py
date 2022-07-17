maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli*vergi))
print(maasAhmet - (maasAhmet*vergi))

# Buyuk kucuk harf duyarliligi vardir
x, y, name, isStudent = (1, 2, "ali", False)
print(x, y, name, isStudent)

# Conversion 
#yorum yapmak istedigin sutunlari secip ctrl kc yaparsak hepsi yoruma alinir 
#yada satirlarin basladigi ve bittigi yere ''' tirnak atmak yeterli 
#ctrl ku ise yorumu kaldirir


# x = input('1.sayi :')
# y = input('2.sayi :')

# # toplam= x+y sayilari yan yana yazdirir

# print(type(x))
# print(type(y))

# toplam = int(x) + int(y)
# print(toplam)

x= 5
y= 2.5
name= 'zendaya'
isOnline= True

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

#int to float
x= float(x)
print(x)
print(type(x))

#float to int
 
y= int (y)
print(y)

print(type(y))

result = x+ y
print(result)

#bool to str
isOnline= str(isOnline)
print(isOnline)
print(type(isOnline))

#true'nin int'e cevrilmis hali 1 verir 
#false'un int'e cevrilmis hali 0 verir 