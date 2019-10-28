#This program accept the total number of entries of string you want to make
#When the word 'exit' is typed, the loops breaks, and the total number of entry made is shown
print('Number of input you\'ll like to enter: ')
num= int(input())
serialNumber = 1
while serialNumber <= num:
    print('Your name please: ')
    name=input()
    if(name == 'exit'):
        print('You have made ' + str(serialNumber-1) + ' entries')
        break
    print(str(serialNumber) + ' ' + name)
    serialNumber +=1
