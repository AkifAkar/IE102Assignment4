import numpy as np
import matplotlib.pyplot as plt

normalProfitPerDozen = 24
costOfDozen = 8
leftOverProfitPerDozen = 7
demandsAndProbabilities = [[6, 0.1], [8, 0.2], [10, 0.3], [12, 0.2], [14, 0.1], [16, 0.1]]


def CalculateExpectedProfit(preparedDozen, printVal):  # printVal is to determine whether to print calculations
    ExpectedProfit = 0
    for i in demandsAndProbabilities:
        unMetDemand = 0
        leftOver = 0
        profitFromDemand = -preparedDozen * costOfDozen  # cost of production
        if preparedDozen > i[0]:  # if we have more than demand
            profitFromDemand += i[0] * normalProfitPerDozen
            leftOver = preparedDozen - i[0]
            profitFromDemand += leftOver * leftOverProfitPerDozen
        elif preparedDozen == i[0]:  # if we have just many as demand
            profitFromDemand += i[0] * normalProfitPerDozen
        else:  # if we have less than demand
            profitFromDemand += preparedDozen * normalProfitPerDozen
            unMetDemand = i[0] - preparedDozen
        if printVal:
            print(
                f"Demand : {i[0]}, profit = {profitFromDemand}, leftover dozens  = {leftOver}, unmet demand = {unMetDemand}, Missed profit = {unMetDemand * 16}, probability = {i[1]}")
        ExpectedProfit += profitFromDemand * i[1]  # Adding the weigthed value of profit
    if printVal:
        print(f"Expected Total Profit is {ExpectedProfit}")
    return ExpectedProfit


CalculateExpectedProfit(9, True)
CalculateExpectedProfit(12, True)
CalculateExpectedProfit(15, True)

# Code to illustrate the distribution of expected total profit
nums = np.arange(1, 50)
values = np.array([])
for i in range(1, 50):
    values = np.append(values, CalculateExpectedProfit(i, False))
plt.plot(nums, values)
plt.show()
