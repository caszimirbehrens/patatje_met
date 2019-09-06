def palindrome(woord):
    stringA = ""
    stringB = ""
    for letter in woord:
        stringA = letter
        stringA += stringB
        stringB = stringA
    if stringB == woord:
        return(true)
        

woordje = input("geef woord ")
palindrome(woordje)