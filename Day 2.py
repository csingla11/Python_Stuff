#Lists

from time import process_time_ns


new_list=[1,2,3,4]
my_list=['sring',100,120.23]
print(len(my_list))


#indexing and slicing
my_list=['one','two','three']
print(my_list[0])
print(my_list[1:])

#concatenate list 

another_list=["four","five"]
print(my_list+another_list)

new_one=my_list+another_list
print(new_one)


#Lists are mutable means- can update values dynamically

new_one[0]= 1
print(new_one)


#append the list

new_one.append('seven')
print(new_one)

#pop off item from last in list
print(new_one.pop())
print(new_one)

#pop off from some particular location
print(new_one.pop(1))


#sort the list

new_list=['q','r','t','v','j']
num_list=['2','3','1','5','6']

print(new_list.sort()) #it will return none only and list will be sorted so print list now
print(num_list.sort()) #it will return none only and list will be sorted so print list now

print(new_list)
print(num_list)

sorted_list=new_list.sort()
print(type(sorted_list))

#reverse function to list
num_list.reverse()
print(num_list)