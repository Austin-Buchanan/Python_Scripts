# Script that accepts command line input and adds a note with a timestamped name to a Windows desktop.

import time
import shutil

def main():
    # Get input from console
    note = input('Enter note: ')

    # Set up timestamp for filename
    currentTime = time.localtime()
    filename = time.strftime('%a_%d_%b_%Y_%H-%M-%S', currentTime) + '.txt'

    # Write to file, move to desktop
    with open(filename, 'w') as f:
        f.write(note)
    shutil.move('./' + filename, 'C:/Users/austi/Desktop/' + filename)

    # Clean up and user communication
    f.close()
    print(filename + ' saved to the desktop.')

if __name__ == "__main__":
    main()