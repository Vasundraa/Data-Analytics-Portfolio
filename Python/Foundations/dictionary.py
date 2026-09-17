
#creating dictionary with constructor
details=dict(name='Vasu', age=22, degree='B.E.', stream='CSE',city='Coimbatore')
print('Details created:',details)

#printing keys
print(details.keys())

#printing values 
print(details.values())

#printing both keys and values
print(details.items())

#accesiing values using keys
print('accessing method 1:',details.get('name')) #does not show error when we try to access unavilable keyvalue using customizable msg: get('key name', 'msg')
#or
print('accessing method 2:',details['name'])

#add
details['dob']='13/07/2004'
print('added new key in details:',details)

#update
details.update({
    'city':'CBE',
    'DOB':'01.06.05'
})
#or
details['name']='Sri' #will not cause error becoz of add syntax instead it over writes it
print(details)

#delete
del details['name']
print(details)
#delete last inserted values
details.popitem()
print(details)

#traversing
#packed
for item in details.items():
    print(item, end="/")

print()
#unpacking
for key,value in details.items():
    print(f'{key} - {value}')

#copy
new=details.copy()
new['stream']='ECE'
print("details:",details)
print("new",new)

new = details
new['stream']='CSE'
print("details:",details)
print("new",new)