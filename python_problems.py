#problem 1
#write a method with take key, value from the user and add that value in the list.. 
#if key is already filled should return message to user to chose another key. length of list will be 10
def key_values(my_list):
    """write a method with take key, value from the user and add that value in the list.. 
    if key is already filled should return message to user to chose another key. length of list will be 10"""
    index = int(input("Enter the index where you want to add the value (0-9): "))
    value = input("Enter the value that you want to add: ")
    
    if index < len(my_list):
        if my_list[index] is None:
            my_list[index] = value
            print("Value '" + value + "' added to list at index " + str(index))
        else:
            print("Index " + str(index) + " is already filled. Please choose another index.")
    else:
        print("Index " + str(index) + " is out of range. Please choose an index between 0 and " + str(len(my_list) - 1) + ".")

    if None not in my_list:
        print("List is now full.")
        
        
        
# Initialize an empty list with 10 None values
my_list = [None] * 10

# Add values to the list using user input
while None in my_list:
    key_values(my_list)

# Print the resulting list
my_list=[int(i) for i in my_list]
print(my_list)


#***************************************************************************************************************************
#problem 2
#write a method with fixed length of list 5. 
#if user enter more then 5th value in the list bottom value should be removed and new value should be added at the top of list
    
def add_to_list(my_list):
    """add element to a list using Lifo"""
    # Enter value from the user
    value=int(input("Enter value: "))
    #insert value at the top of list
    my_list.insert(0,value)
    while len(my_list)>5:
            my_list.pop()
    return my_list

my_list=add_to_list(my_list)
print(my_list)
 
# *************************************************************************************************************************************

#problem 3
#write a method with list of random numbers, when user add new value methode will check if the value already exist in 
#list return message "value already in the list other wise add the value in the list and display back the list till that value
def add_number():
    random = []
    while len(random) < 10:
        value = int(input())
        random.append(value)

    #num = int(input("Enter a number"))
    new_value = int(input("Enter a new value: "))
    if new_value in random:
        print("Value already in the list.")
        index = random.index(new_value)
        print(random[:index+1])
    else:
        random.append(new_value)
        index = random.index(new_value)
        print(random[:index+1])

add_number()
#******************************************************************************************************************************

#problem 4
#write a method which can create a multi die-mention array by getting number of values 
#of first list and number of values for the associative list, display the list as value in table formate
# Define the size of the multi-dimensional array

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create an empty multi-dimensional array with the specified size
multi_array = [[None] * cols for i in range(rows)]

# Loop through each element in the multi-dimensional array and get the value from the user

for i in range(rows):
    for j in range(cols):
        multi_array[i][j] = input("Enter the value for element at row " + str(i) + " and column " + str(j) + ": ")

# Print the multi-dimensional array
print("Multi-dimensional array:")

for i in range(rows):
    for j in range(cols):
        print(multi_array[i][j], end="\t")

    print()