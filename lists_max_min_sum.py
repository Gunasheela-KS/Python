# # nested_list [[5,7,3], [12,7,19], [2,31,5]]
#return a list containing second largest nums from each list inside the nested_list
# [5,12,5]

nested_list=[[5,7,3], [12,7,19], [2,31,5]]

new_list=[]
for lst in nested_list:
    new_list.append(sorted(lst)[-2])
print(new_list)


# Find the maximum element in a list without using max function

num_list=[5,6,9,10,0]

max_num=num_list[0]
for element in num_list:
    if element > max_num:
        max_num=element
print(max_num)

# Find the second maximum number in the list

second_max=-666666666666
for element in num_list:
    if element > second_max and element < max_num:
        second_max=element
print(second_max)

# Minimum and maximum sum of four numbers in a list of length 5

given_list=[1,2,3,4,5]
min_sum=sum(given_list)-max(given_list)
max_sum=sum(given_list)-min(given_list)

print(max_sum)
print(min_sum)