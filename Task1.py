#creating a list
my_list=[1,2,3,4,5]

#Adding an element to the list
my_list.append(6)
my_list.append(12)

#Removing an element from the list
my_list.remove(2)
my_list.remove(3)

#Modifying an element in the list
my_list[3]=11
my_list[2]=10

print("updated list-:" ,my_list)

#creating a dictionary
my_dict={'Name':'Divyanshu','age':25,'city':'Rampur'}

#Adding 
my_dict['gender']='male'
my_dict['course']='BCA'

#Removing
del my_dict['age']


#modifying
my_dict['city']='Moradabad'

print("updated Dictionary:",my_dict)

#creating a set
my_set={1,2,3,4,5}

#adding
my_set.add(6)
my_set.add(7)

#removing
my_set.remove(2)
my_set.remove(3)

#modifying
my_set.discard(1)
my_set.add(11)

print("updated set:",my_set)


