
def sven(woordje):
    A = 0
    for letter in woordje:
        A += 1
        print(letter*A)

woord = input("woord pls? ")
sven(woord)    