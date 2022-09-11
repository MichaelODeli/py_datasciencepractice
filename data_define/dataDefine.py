import re
def dataDefine(inputData, addData):
    if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", inputData):
        if addData == False:
            return('email')
        if addData == True:
            return([inputData, 'email'])
    elif re.match(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", inputData):
        if addData == False:
            return('phone')
        if addData == True:
            return([inputData, 'phone'])
    else:
        return(None)
