# Chapter 4 List and tuple exercise
spam = ['apples', 'banana', 'tofu', 'cats']

# def listToString(fromList):
#     finalStr = ''
#     for s in fromList:
#        finalStr += s + ', '
#     return finalStr
    
def listToString(fromList):
    finalStr = ''
    length = len(fromList)
    for i in range(0, length):
        if i == length - 1:
            finalStr = finalStr + ' and ' + fromList[i] 
        else:
            finalStr +=  fromList[i] + ', '
    return finalStr
output = listToString(spam)
print(output)