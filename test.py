tempList = [1 for i in range(0,21)]

for i in range(1,21):

    for i in range(1,21):

        tempList[i] = tempList[i] + tempList[i - 1]

print(tempList[-1])
