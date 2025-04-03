def challenge(arg1):
    typeOfData = type(arg1)
    if typeOfData == str:
        arg1 = arg1 + "!"
    elif typeOfData == int:
        arg1 = arg1 + 5
    elif typeOfData == float:
        arg1 = arg1 + 2.71828
    elif typeOfData == bool:
        arg1 = arg1 + True
        arg1 = bool(arg1)
    return (arg1)


print(challenge("hi"))
print(challenge(10))
print(challenge(3.14159))
print(challenge(False))
