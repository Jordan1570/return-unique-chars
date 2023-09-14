# Write a Python function that takes a list and returns a 
# new list with distinct elements from the first list.

num_list = [ 1, 2, 3, 3, 3, 3, 4, 5, 9, 5]

def new_unique_list(num_list):
    unique_list = []
    for num in num_list:
        if num not in unique_list:
            unique_list.append(num)
        else:
            unique_list = unique_list

    return unique_list

unique_list = new_unique_list(num_list)

print(f'Unique String = {unique_list}')