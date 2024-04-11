#Ethan Lewis

 #4/10/2024

 #P2HW2

 #Assignment assess student understanding of Lists


print('Enter your grade for Module 1.', end=' ')
module1 = float(input())

print('Enter your grade for Module 2.', end=' ')
module2 = float(input())

print('Enter your grade for Module 3.', end=' ')
module3 = float(input())

print('Enter your grade for Module 4.', end=' ')
module4 = float(input())

print('Enter your grade for Module 5.', end=' ')
module5 = float(input())

print('Enter your grade for Module 6.', end=' ')
module6 = float(input())

fullgradelist = [module1, module2, module3, module4, module5, module6]

average = sum(fullgradelist) / len(fullgradelist)

print('-------------Results-------------')
print('Lowest Grade:', min(fullgradelist))
print('Highest Grade:', max(fullgradelist))
print('Sum of Grades:', sum(fullgradelist))
print(f'Average: {average:.2f}') 
