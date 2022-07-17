from operator import le, rshift
import re
from tkinter import W


course="Python kursu questions'lari"
website="http://www.sadikturan.com"
#1.'course' karakter dizisinde kac karakter bulunmaktadir?
result=len(course)
print(result)
lengt=len(website)

#2.'website' icinden www karakterlerini alin.
result=website[7:10]
print(result)

#3.'website' icinde com karakterlerini alin
result=website[21:24]
print(result)
result=website[lengt-3:lengt]

#4. 'course' icinden ilk 15 ve son 15 karakterlerini alin 
result = course[0:15]
print(result)
result = course[:15]
print(result)
result = course[-15:-1]
print(result)

