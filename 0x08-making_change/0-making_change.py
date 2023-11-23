#!/usr/bin/python3
"""
No modules to be imported at this time
"""


def makeChange(coins, total):
    """
    A function to determine total number of coins neede to make
    the total value
    Args:
        coins: List containing int values
        total: total value to be met
    """
    # Initialize a list to store the minimum number of coins needed for each total
    dp = [float('inf')] * (total + 1)
    
    # Zero coins needed for a total of zero
    dp[0] = 0
    
    # Iterate through each coin value
    for coin in coins:
        # Update the dp array with minimum coins needed for each total value
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return the fewest number of coins needed for the total amount
    return dp[total] if dp[total] != float('inf') else -1
