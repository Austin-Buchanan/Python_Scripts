def main():
    inputFile = open("rawText.txt", "r")
    outputFile = open("newText.txt", "w")
    rawLines = []

    lines = inputFile.readlines()
    for line in lines:
        line = "\'" + line.replace('\n', '') + "\',\n"
        rawLines.append(line)
    
    rawLines[-1] = rawLines[-1].replace(',', '')
    outputFile.writelines(rawLines)

    inputFile.close()
    outputFile.close()

if __name__== "__main__":
    main()
