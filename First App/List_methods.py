from operator import le


numbers=[1,10,5,16,4,9,10]
letters=['a','f','g','h','a','y']

val= min(numbers)
val1= max(numbers)
val2= max(letters)
val3= min(letters)

val4=numbers[3:6]
val5=numbers[:3]
val6=numbers[4:] #4. indexten baslar son karaktere kadar yazdirir

numbers[4]= 40
print(numbers)

numbers.append('29')
numbers.insert(3,54) #3. indexten hemen once sag tarafta yazan sayiyi ekle
numbers.insert(-1,23) #son karakterden onceki indexe sag tarafta yazan sayiyi ekler 

numbers.pop(0) #icine yazilan indexteki karakteri siler 
numbers.remove(10) #icinde yazilan sayiyi siler


letters.sort() # alfabetik siralar 

print(numbers) 

numbers.reverse() #tam tersi siralar  
letters.reverse()

print(numbers) 
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10))



numbers.clear() #butun elemanlari siler 
print(numbers)
























