prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
highest, spread = 0, 0

for i in reversed(range(len(prices))):
    if highest < prices[i]:
        highest = prices[i]
    else:
        spread = max(spread, highest - prices[i])

print(spread)