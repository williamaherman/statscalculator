import random

# 1. Generate a random number without a seed between a range of two numbers - Both Integer and Decimal

# 2.Generate a random number with a seed between a range of two numbers - Both Integer and Decimal

#Random integer from 20 to 100
num1 = random.randint(20, 100)
print("Random integer between 20 & 100: ", num1)

# Random decimal float from 10 to 999.9
int_num = random.choice(range(100, 10000))
float_num = int_num/100
print("Random decimal number between 10 & 1000:", float_num)

# 3. Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal

# Integer
randomFloatList = []
# Set a length of the list to 10
for i in range(0, 10):
    xint = round(random.uniform(50.50, 500.50), 0)
    randomFloatList.append(xint)

print("List of 10 random integer numbers")
print(randomFloatList)


#Decimal
randomFloatList = []
# Set a length of the list to 10
for i in range(0, 10):
    xdec = round(random.uniform(50.50, 500.50), 5)
    randomFloatList.append(xdec)

print("List of 10 random decimal numbers")
print(randomFloatList)


# 4. Select a random item from a list

a_list = ['RandomItem1', 'RandomItem2', 'RandomItem3', 'RandomItem4', 'RandomItem5']

an_item = random.choice(a_list)
print ("Randomly selected item from list:", an_item)

# 5. Set a seed and randomly select the same value from a list

aList = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampled_list = random.sample(aList, 2)
print("Choosing 2 random items from a list using random.sample() function:", sampled_list)

# 6. Select N number of items from a list without a seed



# 7. Select N number of items from a list with a seed