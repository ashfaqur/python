import termcolor
from termcolor import colored
import colorama

colorama.init()


text = colored("Hi There", color='yellow', on_color='on_cyan')

print(text)
