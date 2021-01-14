import pandas

# Reading data
df = pandas.read_csv('aria.csv', sep=';', parse_dates=['Date'])

# Stores the highest Low value
highestLowValue = None
# Count of the current high streak
highStreak = 0
# Can be buy, hold, sell
action = None
# Indicates if a buy has been executed.
buy = False
# Stores the lowest Low value
lowestLowValue = None
# Cound of the current low streak
lowStreak = 0
# List of actions
actions = []

for index, row in df.iterrows():
    curLowValue = row['Low']

    # First row will be handled differently
    # Setting highest Low value
    if not highestLowValue:
        highestLowValue = curLowValue
    # Setting highest Low value and counting the streak
    elif curLowValue >= highestLowValue:
        highestLowValue = curLowValue
        highStreak += 1
    else:
        # Resetting streak
        highStreak = 0

    # First row will be handled differently
    # Setting lowest Low value
    if not lowestLowValue:
        lowestLowValue = curLowValue
    # Setting lowest Low value and counting the streak
    elif curLowValue < lowestLowValue:
        lowestLowValue = curLowValue
        lowStreak += 1
    else:
        # Resetting streak
        lowStreak = 0

    # Setting action depending on action and buy execution
    if (action is None or action != 'buy') and not buy and highStreak == 2:
        action = "buy"
        buy = True
    elif buy and lowStreak == 2:
        action = "sell"
        buy = False
    else:
        action = "hold"

    actions.append(action)

# Appending column
df['Action'] = actions

pandas.set_option('display.max_rows', None)
print(df)

df.to_csv('aria-out.csv', sep=';', encoding='utf-8')
