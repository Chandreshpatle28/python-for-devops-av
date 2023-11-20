my_list = [1, 2, 3, 'DevOps', True] #list
print(my_list)
print(len(my_list)) #5

first_element = my_list[0]
last_element = my_list[-1]
print(first_element)
print(last_element)

my_list[2] = 'Automation'
print(my_list)

my_list.append('Python')
print(my_list)

my_list.remove(2)
print(my_list)

removed_element = my_list.pop(1)
print(my_list)

subset = my_list[0:3]
print(subset)

another_list =[ "hello", "Chandresh"] # new list created

new_list = [my_list , "   ", another_list] #Concatenated
print(new_list)