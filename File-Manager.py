from colorama import Fore, init, Style
from os import system

############################## READ FILE ##############################

############################## WRITE FILE ##############################

############################## CREATE FILE ##############################

def CreateFile():
    
    system('cls')

    newFile = input(Fore.GREEN + " Enter File's Name : " + Style.RESET_ALL)

    newFile = newFile + '.txt'

    myfile = open(newFile, "w") # create a new file if it doesn't exist

    print(Fore.LIGHTGREEN_EX + " Created file successfully." + Style.RESET_ALL)

    print(
        Fore.RED + ' [1] ' + Fore.WHITE + ' Write current file\n' +
        Fore.RED + ' [2] ' + Fore.WHITE + ' back to main\n'+
        Fore.LIGHTBLACK_EX + " Press any key to exit..."
    )

    answer = input(Fore.GREEN + " >> " + Style.RESET_ALL)

    if answer == '1':
        pass
    elif answer == '2':
        pass
    else:
        pass

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
        CreateFile()
    elif answer == '4':
        pass
    else:
        pass

############################## BODY ##############################

main()