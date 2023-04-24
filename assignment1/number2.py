list1 = ['S001', 'S002', 'S003', 'S004']
list2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list3 = [85, 98, 89, 92]

# defininf a dictionary and looping through the lists to create the values
my_nested_dictionary = {}

for index in range(len(list1)):
    my_nested_dictionary[list1[index]] = {
        list2[index]:list3[index]
    }

print('This is my nested dictionary with the first list as the keys ', my_nested_dictionary)

# Creating the list with the nested dicts as the value

my_list = [my_nested_dictionary]
print(my_list)
