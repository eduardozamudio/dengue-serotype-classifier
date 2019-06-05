def insert_separator(s, sep = ','):
    '''
    Insert the separator sep between every character in string s
    
    :param s:   string
    :type s:    str

    :param sep: separetor to insert between characters (default = ',')
    :type sep:  str
    
    :return:    string
    :rtype:     str

    
    :Example:

    s = 'abcde'
    insert_separator(s)
    
    output: 'a,b,c,d,e'
    
    '''
    if (s.__class__ is not str):
        return s
    
    res = None   
    lenght = len(s)
    
    if lenght <= 1:
        res = s
    else:
        half = lenght // 2
        res = insert_separator(s[:half]) + sep + insert_separator(s[half:])
    return res