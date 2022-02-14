from colorama import Fore, init, Style
from os import system

############################## READ FILE ##############################

############################## WRITE FILE ##############################

############################## CREATE FILE ##############################

############################## DELETE FILE ##############################

############################## MAIN ##############################

def main():

    system('cls')

    print(
        Fore.RED + ' [1] ' + Fore.WHITE + "Read File\n" +
        Fore.RED + ' [2] ' + Fore.WHITE + "Write File\n" +
        Fore.RED + ' [3] ' + Fore.WHITE + "Create File\n" +
        Fore.RED + ' [4] ' + Fore.WHITE + "Delete File\n" +
        Fore.LIGHTBLACK_EX + " Press any key to exit..."
    )

    answer = input(Fore.GREEN + " >> " + Style.RESET_ALL)

    if answer == '1':
        pass
    elif answer == '2':
        pass
    elif answer == '3':
        pass
    elif answer == '4':
        pass
    else:
        pass

############################## BODY ##############################

main()