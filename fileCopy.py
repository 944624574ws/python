def main():
    f1 = input("enter a source file: ").strip()
    f2 = input("enter a source file: ").strip()

    infile = open(f1, 'r')
    outfile = open(f2, 'w')

    countLines = countChars = 0
    for line in infile:
        countLines += 1
        countChars += len(line)
        outfile.write(line)
    print(countLines, "lines and", countChars, "chars copied")

    infile.close()
    outfile.close()

main()
