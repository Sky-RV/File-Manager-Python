from ast import For
from asyncio.windows_events import NULL
from tarfile import NUL
from colorama import Fore, init, Style
import os
from os import system

############################## END ##############################

def END(text):
    
    if text != NULL:
        print(Fore.LIGHTGREEN_EX + "\n {} in file successfully.\n".format(text) + Style.RESET_ALL)

    print(
        Fore.RED + ' [1] ' + Fore.WHITE + ' Back to main\n\n'+
        Fore.LIGHTBLACK_EX + " Press any key to exit..."
    )

    answer = input(Fore.GREEN + " >> " + Style.RESET_ALL)

    if answer == '1':
        main()
    else:
        pass

############################## READ FILE ##############################

def ReadFile():

    system('cls')

    readFile = input(Fore.GREEN + " Enter File's Name : " + Style.RESET_ALL)

    readFile = readFile + ".txt"

    myfile = open(readFile, "r") 

    print()

    print(Fore.GREEN + " Your Text : ")
    print(Fore.WHITE + myfile.read())

    myfile.close()

    END('Read')

############################## WRITE FILE ##############################

def WriteFile(n):

    system('cls')

    if n == NULL:
        writeFile = input(Fore.GREEN + " Enter File's Name : " + Style.RESET_ALL)
        writeFile = writeFile + '.txt'
    else:
        writeFile = n

    myfile = open(writeFile, "a") # append to the end of the file

    myText = input(Fore.GREEN + "\n Enter your text : " + Style.RESET_ALL + " ")

    myText = myText + "\n"

    myfile.write(myText)

    myfile.close()

    END('Writed')

############################## CREATE FILE ##############################

def CreateFile():
    
    system('cls')

    newFile = input(Fore.GREEN + " Enter File's Name : " + Style.RESET_ALL)

    newFile = newFile + '.txt'

    myfile = open(newFile, "w") # create a new file if it doesn't exist

    print(Fore.LIGHTGREEN_EX + "\n Created file successfully.\n" + Style.RESET_ALL)

    myfile.close()

    print(
        Fore.RED + ' [1] ' + Fore.WHITE + ' Write current file\n' +
        Fore.RED + ' [2] ' + Fore.WHITE + ' Back to main\n\n'+
        Fore.LIGHTBLACK_EX + " Press any key to exit..."
    )

    answer = input(Fore.GREEN + " >> " + Style.RESET_ALL)

    if answer == '1':
        WriteFile(newFile)
    elif answer == '2':
        main()
    else:
        pass

############################## DELETE FILE ##############################

def DeleteFile():

    system('cls')

    deleteFile = input(Fore.GREEN + " Enter File's Name : " + Style.RESET_ALL)

    deleteFile = deleteFile + ".txt"

    if os.path.exists(deleteFile):
        os.remove(deleteFile)
        print(Fore.LIGHTGREEN_EX + "\n Deleted file successfully.\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + " The File doesn't exist.")

    END(text=NULL)

############################## RENAME FILE ##############################

def RenameFile():

    system('cls')

    oldFile = input(Fore.GREEN + " Enter Old File's Name : " + Style.RESET_ALL)
    
    newFile = input(Fore.GREEN + "\n Enter New File's Name : " + Style.RESET_ALL)

    oldFile = oldFile + '.txt'
    newFile = newFile + '.txt'

    if os.path.exists(oldFile) and not(os.path.exists(newFile)):
        os.rename(oldFile, newFile)
        print(Fore.LIGHTGREEN_EX + "\n Renamed file successfully.\n" + Style.RESET_ALL)

    elif not(os.path.exists(oldFile)):
        print(Fore.RED + " The {} doesn't exist.".format(oldFile))
    
    elif not(os.path.exists(newFile)):
        print(Fore.RED + " The {} doesn't exist.".format(newFile))
    
    else:
        print(Fore.RED + " The {} doesn't exist or there is another {}.".format(oldFile, newFile))
    
    END(text=NULL)

############################## COPY FILE ##############################

def CopyFile():

    system('cls')

    oldFile = input(Fore.GREEN + " Enter Old File's Name : " + Style.RESET_ALL)

    newFile = input(Fore.GREEN + "\n Enter New File's Name : " + Style.RESET_ALL)

    oldFile = oldFile + '.txt'
    newFile = newFile + '.txt'

    with open(oldFile) as old:
        with open(newFile, "a") as new:
            for line in old:
                new.write(line)

    END("Copied")

############################## MOVE FILE ##############################

def MoveFile():

    system('cls')

    oldFile = input(Fore.GREEN + " Enter Old File's Name : " + Style.RESET_ALL)

    newFile = input(Fore.GREEN + "\n Enter New File's Name : " + Style.RESET_ALL)

    oldFile = oldFile + '.txt'
    newFile = newFile + '.txt'

    with open(oldFile) as old:
        with open(newFile, "w") as new:
            for line in old:
                new.write(line)

    END("Moved")

############################## MAIN ##############################

def main():

    system('cls')

    print(
        Fore.RED + ' [1] ' + Fore.WHITE + "Read File\n" +
        Fore.RED + ' [2] ' + Fore.WHITE + "Write File\n" +
        Fore.RED + ' [3] ' + Fore.WHITE + "Create File\n" +
        Fore.RED + ' [4] ' + Fore.WHITE + "Delete File\n" +
        Fore.RED + ' [5] ' + Fore.WHITE + "Rename File\n" +
        Fore.RED + ' [6] ' + Fore.WHITE + "Copy File\n" +
        Fore.RED + ' [7] ' + Fore.WHITE + "Move File\n\n" +
        Fore.LIGHTBLACK_EX + " Press any key to exit..."
    )

    answer = input(Fore.GREEN + " >> " + Style.RESET_ALL)

    if answer == '1':
        ReadFile()
    elif answer == '2':
        WriteFile(n=NULL)
    elif answer == '3':
        CreateFile()
    elif answer == '4':
        DeleteFile()
    elif answer == '5':
        RenameFile()
    elif answer == '6':
        CopyFile()
    elif answer == '7':
        MoveFile()
    else:
        pass

############################## BODY ##############################

main()