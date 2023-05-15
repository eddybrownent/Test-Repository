def fibonacci_range(start, end):
    fib_sequence = [0, 1]  # Initial Fibonacci sequence
    while fib_sequence[-1] <= end:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    for num in fib_sequence:
        if num >= start and num <= end:
            print(num)

# Example usage: Fibonacci series from the 5th number to the 10th number
fibonacci_range(2, 7)
