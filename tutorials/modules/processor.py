def process_numbers(l):
    if(not isinstance(l, list)):
        return []
    
    newlist = []

    for value in l:
        if (isinstance(value, int) or value.isnumeric()):
            newlist.append(int(value))
        
    newlist.sort()
    return newlist


def process_names(l):
    if(not isinstance(l, list)):
        return []
    
    newlist = []

    for value in l:
        if (isinstance(value, str) and value.isalpha()):
            newlist.append(value)
        
    newlist.sort()
    return newlist