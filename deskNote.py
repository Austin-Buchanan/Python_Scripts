# Script that accepts command line input and adds a note with a timestamped name to a Windows desktop.

import time
import shutil
import getpass
import os

def main():
    # Get input from console
    note = input('Enter note: ')

    # Set up timestamp for filename
    currentTime = time.localtime()
    filename = time.strftime('%a_%d_%b_%Y_%H-%M-%S', currentTime) + '.txt'

    # Write to file
    with open(filename, 'w') as f:
        f.write(note)

    # Detect username and current path
    username = getpass.getuser()
    currentPath = os.getcwd() + '/' + filename
    print(currentPath)

    # Move file to desktop
    targetPath = 'C:/Users/' + username + '/Desktop/' + filename
    shutil.move(currentPath, targetPath)

    # Clean up and user communication
    f.close()
    print('Saved note to ' + targetPath)
    input('Press any key to continue...')

if __name__ == "__main__":  
    main()