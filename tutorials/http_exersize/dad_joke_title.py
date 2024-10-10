from random import choice

import colorama
from pyfiglet import figlet_format
import termcolor

PROGRAM_NAME = "DAD JOKE 3000"


def show():
    """
    Displays the program title in ASCII with random color
    :return: None
    """
    colorama.init()
    title = figlet_format(PROGRAM_NAME)

    colors = list(termcolor.COLORS.keys())
    random_color = choice(colors)

    colored_title = termcolor.colored(title, color=random_color)
    print(colored_title)
