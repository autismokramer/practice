girls = ['Diana' , 'Dyana', 'Tiffany' , 'Trini' , 'Jordan'] # creating a list

print('girl of my dreams to day is ' + girls[0])

print(girls[-1]) # this should print trini since negative start from last list item

print(girls[1:4])

print(len(girls[2]))

girls[1] = 'Isabella' # chaning a item on a list

print(girls)

places = ['New york' , 'Los Angeles' ,'Mexico', 'Korea']

dreams = girls + places # this combines to list into one

print(dreams)

del places[2] # using the del statement to delete an item from a list

print(places)

if 'Diana' in girls: # using the in operator to check if diana is in the girls list
    print('She is in there')
else:
    print('she is not in there want me to addher')

if 'Jadee' not in girls:
    girls = girls + ['Jadee'] # this is adding jadee to the list 
    print(girls)
else:
    print('She is already in here')

dogs = ['thin' , 'gold' , 'loud']

size,color,bark  = dogs # simple way to assign a variable to a list 

print(size)
    
