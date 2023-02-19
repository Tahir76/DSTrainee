def add_list_sort():
    
    '''Sorts a list of integers and adds a number to the sorted list.'''
    
    num_list=[]
    for num in input("Enter a list of integers separated by spaces: ").split():
        num_list.append(int(num))
        num_list.sort()
    
    print("Sorted List: ",num_list)
    number = int(input("Enter a number to add to the list: "))
    index =0
    while index < len(num_list) and  number>num_list[index]:
        index+=1
    num_list.insert(index,number)
    print('Add num in list at sorted postion: ',num_list)

add_list_sort()