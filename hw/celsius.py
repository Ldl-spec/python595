# 10 pts
# Please implement the following.
# 5 pts for code, 5 pts for style.

import sys

def parse_command_line(rawinput):

    # Determine if the user input is wrong
    if len(rawinput) > 2:
        print("The input is incorrect")
        sys.exit()

    # The string is converted to florating
    rawinput = float(rawinput[1])

    # Convert the temperature
    tmp = (rawinput - 32) / 1.8

    # Format the output
    print("{}F is {}C".format(int(rawinput), int(tmp)))

    return tmp

def calculate_celsius(degree_fahrenheit):
    '''
    Print conversion after parse.
    '''
    print("{:.1f}C".format(degree_fahrenheit))

if __name__ == "__main__":
    command_line_inputs = sys.argv
    user_fahrenheit = parse_command_line(command_line_inputs)
    calculate_celsius(user_fahrenheit)
