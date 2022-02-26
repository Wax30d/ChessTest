import random

row = int(input("Enter row of the Chess: "))
column = int(input("Enter column of the Chess: "))

rW = int(input("Enter Row position of white knight: "))
cW = int(input("Enter Column position of white knight: "))

rB = int(input("Enter Row position of black knight: "))
cB = int(input("Enter Column position black knight: "))

xodW = [rW, cW]
xodB = [rB, cB]
print(xodW)
print(xodB)

if xodW == xodB:
    print("Ikalasi bita joyda")
else:
    counter = 0
    while xodW != xodB:

        counter += 1

        # Oq yuradi
        xod_1w = [rW - 2, cW + 1]
        xod_2w = [rW - 2, cW - 1]
        xod_3w = [cW - 2, rW + 1]
        xod_4w = [cW - 2, rW - 1]
        xod_5w = [rW + 2, cW + 1]
        xod_6w = [rW + 2, cW - 1]
        xod_7w = [cW + 2, rW + 1]
        xod_8w = [cW + 2, rW - 1]

        numberOfAllStepsW = [xod_1w, xod_2w, xod_3w, xod_4w, xod_5w, xod_6w, xod_7w, xod_8w]
        print(numberOfAllStepsW)

        # possible steps of white horse
        numberOfAllPossibleStepsW = []
        for i in range(8):
            if 0 < numberOfAllStepsW[i][0] <= row and 0 < numberOfAllStepsW[i][1] <= column:
                numberOfAllPossibleStepsW.append(numberOfAllStepsW[i])

        print(numberOfAllPossibleStepsW)

        xodW = random.choice(numberOfAllPossibleStepsW)
        print(xodW)

        if xodW == xodB:
            print(counter)
            break

        else:
            # qora yuradi
            counter += 1

            xod_1b = [rB - 2, cB + 1]
            xod_2b = [rB - 2, cB - 1]
            xod_3b = [cB - 2, rB + 1]
            xod_4b = [cB - 2, rB - 1]
            xod_5b = [rB + 2, cB + 1]
            xod_6b = [rB + 2, cB - 1]
            xod_7b = [cB + 2, rB + 1]
            xod_8b = [cB + 2, rB - 1]

            numberOfAllStepsB = [xod_1b, xod_2b, xod_3b, xod_4b, xod_5b, xod_6b, xod_7b, xod_8b]
            print(numberOfAllStepsB)

            # possible steps of white horse
            numberOfAllPossibleStepsB = []
            for i in range(8):
                if 0 < numberOfAllStepsB[i][0] <= row and 0 < numberOfAllStepsB[i][1] <= column:
                    numberOfAllPossibleStepsB.append(numberOfAllStepsB[i])

            print(numberOfAllPossibleStepsB)

            xodB = random.choice(numberOfAllPossibleStepsB)
            print(xodB)

            if xodW == xodB:
                print(counter)
                break
