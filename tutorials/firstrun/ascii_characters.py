import pyfiglet
import termcolor
import colorama

colorama.init()

input_msg = input("What do you like to print out: " )
input_color = input("What color: ")

ascii_art = pyfiglet.figlet_format(input_msg)
colored_ascii = termcolor.colored(ascii_art, input_color)
print(colored_ascii)

