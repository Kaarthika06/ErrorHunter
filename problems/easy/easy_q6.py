# Print Numbers from 1 to N: Write a program to print numbers from 1 to a given number N using a while loop.
def print_numbers(n):
    i = 1
    while i <= n:
        print(i)
        i+= 1   
    return num
if __name__ == "__main__":
    num = int(input("Enter the Number "))
    result= print_numbers(num)
    print(result)
