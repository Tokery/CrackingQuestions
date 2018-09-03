def coins (amount, denominations,  curr_denom):
    # Only one way to make change with pennies
    if (curr_denom >= len(denominations) - 1):
        return 1
    
    denom = denominations[curr_denom]

    # Start with 0 quarters
    #   - 0 dimes
    #   - 1 dime
    #   - 2 dimes
    # 1 Quarter
    #   - 0 dimes
    # etc...
    i = 0
    ways = 0
    while (i * denom <= amount):
        ways += coins(amount - i * denom, denominations, curr_denom + 1)
        i += 1
    return ways

def get_change(n):
    return coins(n, [25, 10, 5, 1], 0)

print(get_change(10))