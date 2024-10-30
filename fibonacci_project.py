def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def get_fibonacci_sequence():
    try:
        n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return

        fib_gen = fibonacci_generator()  # Initialize the generator
        sequence = [next(fib_gen) for _ in range(n)]  # Get the first 'n' Fibonacci numbers

        print(f"The first {n} Fibonacci numbers are:", sequence)
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Run the program
get_fibonacci_sequence()

