def sort_contacts(param):
    param = list(param.items())
    ordered_list_of_tuples = []
    for dictionaryItem in param:
        ordered_list_of_tuples.append((dictionaryItem[0], dictionaryItem[1][0], dictionaryItem[1][1]))
    ordered_list_of_tuples.sort()
    return ordered_list_of_tuples
