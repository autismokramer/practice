girls = [] # creates and empty list

while True:
    print('List all your dream girls' + ('press enter when finished'))
    dream = input()
    if dream == '':
        break;
    girls = girls + [dream]
print(girls)
