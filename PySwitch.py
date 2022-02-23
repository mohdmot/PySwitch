def case (value):
    '''
    Usage:
        myCase = case(ANY_VALUE,break=False)

        # Break Param Used To Break Commands After Eech Case

        myCase['value']
        # This Will Return The Value

        myCase['type']
        # This Will Return The Value Type , Ex :
        # 'str' or 'int' or 'float'
    '''
    return value

def default ():
    '''
    This Used in Switch Class
    '''
    return '__DEFAULT__'

class switch ():
    '''
    Usage:
        switch('any_thing',{
            case('any_thing') : lambda:print('Same Value'),
            case('not_any_thing1') : lambda:print('Wrong Value'),
            default() : lambda:print('Somthing Else')
        })
    '''
    def __init__ (self,variable,cases) :
        if not('dict' in str(type(cases))):
            raise SyntaxError('Switch Take \'dict\' Data in Second Param')
        for d in cases.items():
            if d[0] == '__DEFAULT__':
                d[1]()
                break
            else:
                if d[0] == variable:
                    d[1]()
                    break
'''
# Example of Use :

data='instagram'
switch(data,{
    case('twitter'):lambda:print('This is Twitter'),
    case('whatsapp'):lambda:print('This is Whatsapp'),
    case('instagram'):lambda:print('This is Instagram'),
    default():lambda:print('Somthing Else')
})

'''