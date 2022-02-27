import random

row = int(input("Enter row of the Chess: "))
column = int(input("Enter column of the Chess: "))

rW = int(input("Enter Row position of white knight: "))
cW = int(input("Enter Column position of white knight: "))

rB = int(input("Enter Row position of black knight: "))
cB = int(input("Enter Column position black knight: "))

steps = int(input("Enter number of steps to meet knights on the same position: "))

xodW = [rW, cW]
xodB = [rB, cB]
print(xodW)
print(xodB)

if xodW == xodB:
    print("Ikalasi bita joyda")
else:
    counter = 0
    while steps > counter:

        counter += 1

        if counter % 2 != 0:

            # Oq yuradi
            xod_1w = [rW - 2, cW + 1]
            xod_2w = [rW - 2, cW - 1]
            xod_3w = [rW + 1, cW - 2]
            xod_4w = [rW - 1, cW - 2]
            xod_5w = [rW + 2, cW + 1]
            xod_6w = [rW + 2, cW - 1]
            xod_7w = [rW + 1, cW + 2]
            xod_8w = [rW - 1, cW + 2]

            print("Oq yuradi...")
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

            rW = xodW[0]
            cW = xodW[1]

            if xodW == xodB:
                print("CHEER")
                break

        else:
            # qora yuradi

            xod_1b = [rB - 2, cB + 1]
            xod_2b = [rB - 2, cB - 1]
            xod_3b = [rB + 1, cB - 2]
            xod_4b = [rB - 1, cB - 2]
            xod_5b = [rB + 2, cB + 1]
            xod_6b = [rB + 2, cB - 1]
            xod_7b = [rB + 1, cB + 2]
            xod_8b = [rB - 1, cB + 2]

            print("Qora yuradi...")
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

            rB = xodB[0]
            cB = xodB[1]

            if xodW == xodB:
                print("CHEER")
                break

    else:
        print(-1)
        print(f"{counter} moves.")
