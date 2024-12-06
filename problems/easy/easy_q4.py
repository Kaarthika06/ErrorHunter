# Positive, Negative, or Zero: Accept a number and check if it is positive, negative, or zero.
def check_number(num):
    if num > 0:
        print("Positive")  
    elif num < 0:
        print("Negative")  
    else:
        print("Number is ZERO")   
        
if __name__ == "__main__":
    num = int(input("Enter the Number : "))
    result= check_number(num)
    print(result)
    
    
    
