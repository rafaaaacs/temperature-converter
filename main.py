import os
import random
import colorama
from colorama import Fore, Back, Style

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print(Fore.CYAN + """

                                ██████╗  █████╗ ███████╗ █████╗  ██████╗███████╗      
                                ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝      
                                ██████╔╝███████║█████╗  ███████║██║     ███████╗█████╗
                                ██╔══██╗██╔══██║██╔══╝  ██╔══██║██║     ╚════██║╚════╝
                                ██║  ██║██║  ██║██║     ██║  ██║╚██████╗███████║      
                                ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝      
                                                                              
    

     """)

choice = int(input("What do you want to convert? \n 1. Celsius to Fahrenheit \n 2. Fahrenheit to Celsius \nYour Choice: "))
print("\n")

def celsius():
    C = int(input("How many °C do you want to convert into Fahrenheit? \nYour Choice: "))
    F = (C * 9/5) + 32

    print(f"Result: {F}")


def fahrenheit():
    F = int(input("How many °F do you want to convert into Celsius? \nYour choice: "))
    C = 5/9 * (F - 32)

    print(f"Result: {C}")

if choice == 1:
    celsius()
elif choice == 2:
    fahrenheit()
else:
    print("Invalid Choice...")

print("\n")

input(Fore.RESET + "Press enter to exit...")
