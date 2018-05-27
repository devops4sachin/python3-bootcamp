from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    if color not in valid_colors:
        color = "magenta"
    ascii_text = figlet_format(text)
    colored_ascii = colored(ascii_text, color=color)
    print(colored_ascii)

text = input("What would you like to print ?")
color = input("What color you want ?")

print_art(text, color)