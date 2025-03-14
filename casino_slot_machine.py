import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1
def deposit():
    while True:
        amount = input("Enter the amount to deposit. $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        else:
            print("Please enter a valid amount")
    return amount

def get_num_of_lines():
    while True:
        lines = input("Enter the no of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 0 <= lines <= 3:
                break
            else:
                print("Please enter valid number of lines.")
        else:
            print("Please enter a valid lines")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid amount")
    return amount

rows=3
cols=3
symbols={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winnings_lines=[]
    for line in range(lines):
        symbol =columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winnings_lines.append(line+1)

    return winnings,winnings_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range (cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range (rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range (len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(column)-1:
                print(column[row],end=" | ")
            else:
                print(column[row], end="")
        print()

def spin(balance):
    lines=get_num_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet > balance:
            print(f"You do not have enogh to bet that amount, your current balace is ${balance}")
        else:
            break
    print(f"You are betttint ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(rows,cols,symbols)
    print_slot_machine(slots)
    winnings, winnings_lines=check_winnings(slots,lines,bet,symbol_values)
    print(f"You won ${winnings}")
    print(f"You won on line : ",*winnings_lines)
    return winnings - total_bet

def main():  
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}")
        ans = input("Press enter to spin again (q to quit).")
        if ans == "q":
            break
        balance += spin(balance)

    print(f"You have left with ${balance}")
    
main()
