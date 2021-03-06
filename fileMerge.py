def main():
    ftele1 = open('TeleAddressBook.txt', 'rb')
    ftele2 = open('EmailAddressBook.txt', 'rb')

    ftele1.readline()
    ftele2.readline()

    list1_name = []
    list2_name = [];
    list1_tele = []
    list2_email = []

    for line in ftele1:
        elements = line.split()
        list1_name.append(str(elements[0].decode('gbk')))
        list1_tele.append(str(elements[1].decode('gbk')))

    for line in ftele2:
        elements = line.split()
        list2_name.append(str(elements[0].decode('gbk')))
        list2_email.append(str(elements[1].decode('gbk')))

    lines = []
    lines.append('姓名\t   电话\t  邮箱\n')

    for i in range(len(list1_name)):
        s = ''
        if list1_name[i] in list2_name:
            j = list2_name.index(list1_name[i])
            s = '\t'.join([list1_name[i], list1_tele[i], list2_email[j]])
            s += '\n'
        else:
            s = '\t'.join([list1_name[i], list1_tele[i], str(' ----- ')])
            s += '\n'
        lines.append(s)

    for i in range(len(list2_name)):
        s = ''
        if list2_name[i] not in list1_name:
            s = '\t'.join([list2_name[i], str(' ---- '), list2_email[i]])
            s += '\n'
        lines.append(s)
    ftele3 = open('AddressBook.txt', 'w')
    ftele3.writelines(lines)
    ftele3.close()
    ftele1.close()
    ftele2.close()

    print('The addressBooks are merged!')

if __name__=="__main__":
    main()
