woorden = {1: 1}

for i in range(2, 10):
    key2 = i*i
    woorden[i] = key2
for key in woorden:
    print(str(key) + ", " + str(woorden[key]))

    