entered_cost = 1
plateCostEntered = []
plateCostCalculate = []
plateValue = 0.0
plateValueTotal = 0.0

print('Please tell me the value of your dish, enter 0 when done.')

while entered_cost != 0:
    entered_cost = int(input('How much was the plate? '))
    plateCostEntered.append(entered_cost)

plateCostEntered.pop()
print('Here is the value of each plate with taxes and tips included...')

for x in plateCostEntered:
    plateValue = (x * 0.18) + (x * 0.07) + x
    print('The value of this plate', plateValue)
    plateCostCalculate.append(plateValue)
    plateValueTotal = plateValueTotal + plateValue

print('Total for all plates value after all taxes and tips included is', plateValueTotal)
