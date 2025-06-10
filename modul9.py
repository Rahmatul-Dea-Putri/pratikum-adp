from termcolor import colored, cprint
import os

os.system('cls')

print(" " * 10 + colored("TODAY IS A SPECIAL DAY!!!", "magenta"))
print()

print(" " * 18, end="")
print(colored("^","blue"),end=" ")
print(colored("^","blue"),end=" ")
print(colored("^","blue"))

cprint(" " * 18, end="")
cprint(" ", "white", "on_red", end=" ")
cprint(" ", "white", "on_white", end=" ")
cprint(" ", "white", "on_red")

cprint(" " * 16, end="")
cprint(" " * 9, "white", "on_yellow")

cprint(" " * 13, end="")
cprint("~" * 15, "magenta", "on_light_grey")

cprint(" " * 13, end="")
cprint(" " * 15, "white", "on_light_green")

cprint(" " * 10, end="")
cprint("    ITS YOUR DAY!   ", "blue", "on_light_grey")

cprint(" " * 8, end="")
cprint("=" * 24, "white", "on_light_blue")

cprint(" " * 8, end="")
cprint("\_/" *8, "white", "on_magenta")
print()

print(" " * 13 + colored("HAPPY BIRTHDAY!!!", "blue"))
