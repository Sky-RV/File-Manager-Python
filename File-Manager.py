import sys
from colorama import Fore, init, Style
from os import system

############################## READ FILE ##############################

############################## WRITE FILE ##############################

def WriteFile():
    system('cls')

    writeFile = input(Fore.GREEN + " Enter File's Name : " + Style.RESET_ALL)

    writeFile = writeFile + '.txt'

    myfile = open(writeFile, "a") # append to the end of the file

    myText = input(Fore.GREEN + "\n Enter your text : " + Style.RESET_ALL + " ")

    myText = myText + "\n"

    myfile.write(myText)

    myfile.close()

    print(Fore.LIGHTGREEN_EX + "\n Writed in file successfully.\n" + Style.RESET_ALL)

    print(
        Fore.RED + ' [1] ' + Fore.WHITE + ' Back to main\n'+
        Fore.LIGHTBLACK_EX + " Press any key to exit..."
    )

    answer = input(Fore.GREEN + " >> " + Style.RESET_ALL)

    if answer == '1':
        main()
    else:
        pass

############################## CREATE FILE ##############################

def CreateFile():
    
    system('cls')

    newFile = input(Fore.GREEN + " Enter File's Name : " + Style.RESET_ALL)

    newFile = newFile + '.txt'

    myfile = open(newFile, "w") # create a new file if it doesn't exist

    print(Fore.LIGHTGREEN_EX + "\n Created file successfully.\n" + Style.RESET_ALL)

    print(
        Fore.RED + ' [1] ' + Fore.WHITE + ' Write current file\n' +
        Fore.RED + ' [2] ' + Fore.WHITE + ' Back to main\n'+
        Fore.LIGHTBLACK_EX + " Press any key to exit..."
    )

    answer = input(Fore.GREEN + " >> " + Style.RESET_ALL)

    if answer == '1':
        pass
    elif answer == '2':
        main()
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
        Fore.RED + ' [4] ' + Fore.WHITE + "Delete File\n\n" +
        Fore.LIGHTBLACK_EX + " Press any key to exit..."
    )

    answer = input(Fore.GREEN + " >> " + Style.RESET_ALL)

    if answer == '1':
        pass
    elif answer == '2':
        WriteFile()
    elif answer == '3':
        CreateFile()
    elif answer == '4':
        pass
    else:
        pass

############################## BODY ##############################

main()