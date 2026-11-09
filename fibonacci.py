def generate_fibonacci_list(n):
    """
    Returns a list containing the Fibonacci series up to n terms.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_value = fib_series[-1] + fib_series[-2]
        fib_series.append(next_value)
        
    return fib_series

# --- Example Usage ---
if __name__ == "__main__":
    try:
        n_terms = int(input("Enter the number of terms: "))
        result = generate_fibonacci_list(n_terms)
        print(f"Fibonacci Series: {result}")
    except ValueError:
        print("Please enter a valid integer.")
