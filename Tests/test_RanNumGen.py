import random
from datetime import datetime

# 1. Generate a random number without a seed between a range of two numbers - Both Integer and Decimal

#Random integer from 20 to 100
num1 = random.randint(20, 100)
print("Random integer between 20 & 100 w/o seed: ", num1)

# Random decimal float from 10 to 999.9
dec_num = random.choice(range(100, 10000))
float_num = dec_num/100
print("Random decimal between 10 & 100 w/o seed:", float_num)

# 2.Generate a random number with a seed between a range of two numbers - Both Integer and Decimal

#Random integer from 20 to 100
random.seed(datetime)
num1 = random.randint(20, 100)
print("Random integer between 20 & 100 with seed: ", num1)

# Random decimal float from 10 to 100
random.seed(datetime)
dec_num = random.choice(range(100, 10000))
float_num = dec_num/100
print("Random decimal between 10 & 100 with seed:", float_num)

# 3. Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal

# Integer
randomIntList = []
# Set a length of the list to 10 and range from 1 to 100
for i in range(0, 10):
    random.seed(datetime)
    xint = random.randint(1,100)
    randomIntList.append(xint)

print("List of 10 random integers from 1 to 100 with seed:")
print(randomIntList)


#Decimal
randomDecList = []
# Set a length of the list to 10
for i in range(0, 10):
    xdec = round(random.uniform(10, 100), 2)
    randomDecList.append(xdec)

print("List of 10 random decimals from 10 to 100 with seed:")
print(randomDecList)


# 4. Select a random item from a list

a_list = ['RandomItem1', 'RandomItem2', 'RandomItem3', 'RandomItem4', 'RandomItem5']

an_item = random.choice(a_list)
print ("Randomly selected item from list:", an_item)

# 5. Set a seed and randomly select the same value from a list

random.seed(2)
aList = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampled_list = random.sample(aList, 2)
print("2 values from a list of 2 using seed : ", sampled_list)

# 6. Select N number of items from a list without a seed

aList = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampled_list = random.sample(aList, 2)
print("2 values from a list with out seed: ", sampled_list)

# 7. Select N number of items from a list with a seed

random.seed(3)
aList = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampled_list = random.sample(aList, 2)
print("2 values from a list using seed of 3: ", sampled_list)