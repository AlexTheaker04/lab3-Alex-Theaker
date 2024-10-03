#!/usr/bin/env python3

# Create the list called "my_list" here, not within any function defined below.
# That makes it a global object. We'll talk about that in another lab.


my_list = [100, 200, 300, 'six hundred']


def give_list():
    return my_list

def give_first_item():
    return str(my_list[0])

def give_first_and_last_item():
    #return str(my_list[0] , my_list[-1])
    new_list = []

    first1 = my_list[0]
    new_list.append(first1)
    new_list.append(my_list[-1])
    return new_list

def give_second_and_third_item():
    return my_list[1:3]

if __name__ == '__main__':   # This section also referred to as a "main block"
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())