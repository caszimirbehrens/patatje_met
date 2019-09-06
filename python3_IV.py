def palindrome(woord):
    stringA = ""
    stringB = ""
    for letter in woord:
        stringA = letter
        stringA += stringB
        stringB = stringA
    if stringB == woord:
        return(True)
    else:
        return(False)
        

woordje = input("geef woord ")
print(palindrome(woordje))