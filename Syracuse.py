import plotext as pltxt

def syracuse(n):
    y = []

    number = n
    y.append(int(number))

    while number>1:
        # Syracuse sequence calculation
        if number%2==1: #if number is odd
            number=number*3+1
        elif number%2==0: #if number is even
            number=number/2

        y.append(int(number))

    print(' ')
    print('Array with Syracuse sequence terms : ',y)
    print(' ')


    pltxt.plot(y)
    pltxt.title('Line Graph visualize Syracuse sequence')
    pltxt.show()

def main():
    n = eval(input('Please enter a positive integer ='))
    syracuse(n)

main()