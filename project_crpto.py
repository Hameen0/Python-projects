# create a function to put everything together
def enigma():
    #import string to download all numbers and digits
    import string
    key= string.ascii_letters+string.digits
    #to flip the key to get value
    value= key[::-1]
    #create dictionaries for all the characters
    dict_e= dict(zip(key,value))
    dict_d= {value:key for key, value in dict_e.items()}
    mode=input('Enter mode, e for encode and d for decode: ')
    msg=input('Enter message: ')
    if mode.lower( )=='e':
        result= ''.join([dict_e[letter] for letter in msg.lower()])
        
    else :
        result=''.join([dict_d[letter] for letter in msg.lower()])
    
    return result.capitalize()
print(enigma())
