# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random  

def write_random_numbers_to_file():  
  
    while True:  
        try:  
            num_of_randoms = int(input("Enter the number of random numbers to generate (up to 1000): "))  
            if 1 <= num_of_randoms <= 1000:  
                break  
            else:  
                print("Please enter a number between 1 and 1000.")  
        except ValueError:  
            print("Invalid input. Please enter an integer value.")  

    random_numbers = [random.randint(1, 500) for _ in range(num_of_randoms)]  

    filename = "random_numbers.txt"  

    with open(filename, 'w') as file:  
        for number in random_numbers:  
            file.write(f"{number}\n")  

    print(f"{num_of_randoms} random numbers have been written to {filename}.")  
  
if __name__ == '__main__':
    write_random_numbers_to_file()

#Jadon Anderstrom, 11/01/24, "Random Number File Writer".
