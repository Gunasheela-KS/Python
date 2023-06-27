def two_sum(num_list,target):
    occurences_list=[]
    for i,num in enumerate(num_list):
        complement=target-num
        if complement in num_list:
            occurences_list.append(i,num_list.index(complement))

    unique_occurences=[]
    for item in occurences_list:
        if item[::-1] not in unique_occurences:
            unique_occurences.append(item)

    return unique_occurences

### Time and space complexity O(n^2) ###

def two_sum(num_list,target):
    unique_occurences=[]
    num_dict={}

    for i,num in enumerate(num_list):
        comp=target-num
        if comp in num_dict:
            unique_occurences.append([i,num_dict[comp]])
        num_dict[num]=i
    return unique_occurences

### Time and space complexity O(n) ###
