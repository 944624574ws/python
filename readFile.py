def main():
    infile = open('test.txt', 'r')
    data = infile.read()
    print(data)
    infile.close()
    
    infile = open('test.txt', 'r')
    for i in range(2):
        line = infile.readline()
        print(line[:-1])
    infile.close()
main()
