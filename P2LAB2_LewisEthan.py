# Ethan Lewis
 # 4/10/2024
 # P2LAB2
 # Assignment tests student's knowledge of how to write code that uses a dictionary to store user input and displays output to the user


 


Car_dict = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

print('The keys in this dictionary are:')
print(Car_dict.keys())

print('Enter a vehicle to see it`s mpg:', end=' ')
carinput = input()

print('The', carinput, 'gets', Car_dict.get(carinput), 'mpg.')

print('How many miles will you drive the', carinput, '?', end=' ')
milesinput = float(input())

gasoutput = Car_dict.get(carinput) % milesinput

print(f'{gasoutput}gallons of gas are needed to drive the', carinput, milesinput,'miles.')
