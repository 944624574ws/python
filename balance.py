def addInterest(balance, rate):
    for i in range(len(balance)):
        balance[i] = balance[i] * (1 + rate)

def main():
    amouts = [100, 200, 300, 400]
    rate = 0.1
    addInterest(amouts, rate)
    print(amouts)

main()


    
