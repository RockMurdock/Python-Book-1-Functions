# Now do the reverse. Convert the dollar amount into the coins that make up that dollar amount. The final result is an object with the correct number of quarters, dimes, nickels, and pennies.

#That should produce the following output.
"""
>>> print(piggyBank)
{ 'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4 }
"""

dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here

piggyBank["quarters"] = int(dollarAmount * 4)

piggyBank["dimes"] = int((dollarAmount - piggyBank["quarters"] / 4) * 10)

piggyBank["nickels"] = int((dollarAmount - piggyBank["quarters"] / 4 - piggyBank["dimes"] / 10) * 20)

piggyBank["pennies"] = int((dollarAmount - piggyBank["quarters"] / 4 - piggyBank["dimes"] / 10 - piggyBank["nickels"] / 20) * 101)

print(piggyBank)