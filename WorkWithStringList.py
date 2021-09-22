# check: all items in list need to have type str [<type: str>, <type: str>, <type: str>, <type: str>]
def check_one_type_items_in_list(list_, type_=str):
    type_list = list(map(type, list_))
    for t in type_list:
        if t != type_:
            raise TypeError('All items in the list must be type of str')

    return None

# get new list (['a', 'b', 'c'], 'c') -> new list -> ['a' ,'b' ,'c'] (without item 'c')
def get_new_list_without_item(old_list, item):

    check_one_type_items_in_list(old_list)

    if type(old_list) != list:
        raise TypeError

    new_list = old_list.copy()
    delete_item_in_list(new_list, item)
    return new_list


def delete_item_in_list(list, item):
    list.remove(item)

#   ['a', 'b', 'c'] -> to string -> a, b, c
def get_list_as_string(list, string_separator=', '):
    return string_separator.join(list)

#   (['a', 'b', 'c'], '-', '_', False) -> ['-a_', '-b_', '-c_']
#   (['a', 'b', 'c'], '-', '_', True) -> ['-a_', '-b_', '-c']
def get_new_list_with(old_list, item_in_start='', item_in_end='', do_not_end_the_itemInEnd=True):
    new_list = []
    for element in old_list:
        new_list.append(item_in_start + element + item_in_end)

    if(do_not_end_the_itemInEnd):
        new_list[-1] = new_list[-1][:-len(item_in_end)]

    return new_list

#   requirement: list1 length == list2 length
#   (['a', 'b', 'c'], ['d', 'e', 'f'], ' = ') -> new list -> ['a = d', 'b = e', 'c = f']
def glue_two_string_lists(list1, list2, concatenation_string=' = '):
    i = 0
    new_list = []
    for element in list1:
        new_list.append(list1[i] + concatenation_string + list2[i])
        i += 1

    return new_list
