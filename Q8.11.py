# Store the number of ways to make change for a given amount and denomination

def coins (amount, denominations,  curr_denom, memory):
    if (memory[amount][curr_denom] > 0):
        return memory[amount][curr_denom]

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
        ways += coins(amount - i * denom, denominations, curr_denom + 1, memory)
        i += 1
    
    memory[amount][curr_denom] = ways
    return ways

def get_change(n):
    memory = [[0 for x in range(4)] for y in range(n + 1)]
    return coins(n, [25, 10, 5, 1], 0, memory)

print(get_change(10))