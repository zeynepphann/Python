
fruits = {'orange', 'apple','banana'}

#print(fruits[0]) indexlenemez

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape']) #birden fazla ekleme icin 
fruits.add('cherry') # ayni eleman birden fazla eklenmeye calisirsa eklenmez 

print(fruits)

fruits.remove('mango')
fruits.discard('apple')
fruits.pop() # herhangi bir elemani siler 
fruits.clear() # hepsini siler

myList=[1,2,3,4,4,3,2]
print(set(myList)) # tekrarsiz list verir 

