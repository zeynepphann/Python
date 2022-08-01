# Key - value 

# 41=> kocaeli 34 istanbul 

sehirler = ['kocaeli', 'istanbul']
plakalar =[41,34]

print(plakalar[sehirler.index('kocaeli')])
print(plakalar[sehirler.index('istanbul')])

#plakalar = { 'key' : 'value'}
plakalar = { 'kocaeli' : 41, 'istanbul' : 34}

plakalar['ankara'] = 6
plakalar['kocaeli'] = ' new value'

users = {
    'sadikturan' : { 
            'age': 36,
        'email ' : 'sadik@',
        'address' : 'kocaeli'
    },
    
    'cinarturan': {
      'age': 3,
        'email ' : 'cinar@',
        'address' : 'istanbul'
    }
}

print(users['cinarturan'])
print(users['cinarturan']['age'])
print(users['cinarturan']['email'])
print(users['cinarturan']['address'])


 



