#!/usr/bin/env python3

# Place my_list below this comment (before the function definitions)

my_list = [1,2,3,4,5]

def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    ordered_list.append(len(ordered_list) + 1 )
    return

def remove_items_from_list(ordered_list, items_to_remove):
    
    
    for i in range(len(items_to_remove)):
        ordered_list.remove(items_to_remove[i])

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)