 # Ethan Lewis
 # 4/10/2024
 # P1HW2
 # For this assignment you will create a program that does some basic math on numbers that are entered



 
print('Enter your budget:', end=' ')
budget = float(input())

print('Enter your travel destination:', end=' ')
destination = input()

print('How much will you spend on gas?', end=' ')
gasmoney = float(input())

print('How much will you need for accomodations?', end=' ')
restmoney = float(input())

print('How much will you spend on food?', end=' ')
foodmoney = float(input())

print('---------Travel Expenses---------')

print('Location:', destination)
print('Initial budget: $', budget)

print('Fuel: $', gasmoney)
print('Hotels/etc: $', restmoney)
print('Food: $', foodmoney)

finalbalance = budget - gasmoney - restmoney - foodmoney

print('Remaining Balance: $', finalbalance)
