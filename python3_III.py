def reverse_string(woord):
    stringA = ""
    stringB = ""
    for letter in woord:
        stringA = letter
        stringA += stringB
        stringB = stringA
    return stringB
        

woordje = input("geef woord ")
print(reverse_string(woordje))

