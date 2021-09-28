# === Example Solution ===
# Note: There are many ways to do this!

# Just some arbitrary prices
prices = [20.4, 16.4, 13.2, 15.71, 12.0, 13.56, 14.67, 18.24, 20.89, 21.24, 23.55, 26.00]

# Get price at first index
initial_price = prices[0]
# Get price at last index (-1 means last item)
final_price = prices[-1]

# Calculate profit
profit = (final_price - initial_price)*10

# Print out profit
print('Profit: $' + str(profit))
# Done!

# === Look further for more fun tips and the bonus solution! ===

# Secret! f-strings (format strings) can be used to print things prettier
# Here we had a float rounding error, but we can specify the format
# to .2f to limit it to 2 decimal places.
# Link to more info on string formatting: https://realpython.com/python-f-strings/
print(f'Profit: ${profit:.2f}')


# === Bonus solution ===
num_stocks = int(input('How many stocks are you buying and holding? '))
profit = (final_price - initial_price)*num_stocks
print(f'You made ${profit:.2f}!')