woorden = {"microsoft": "billgates", "apple": "Steve Jobs", "google": "Larry Page en Sergey Brin"}

def woordindictonairy(woord):
    if woord in woorden:
        return(True)
    else:
        return(False)

woordje = input("geef woord ")
print(woordindictonairy(woordje))