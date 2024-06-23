import random

def three_digit_fibonacci():
    """
    Generates a list of three-digit Fibonacci numbers less than 1000.

    Returns:
        list: A list of three-digit Fibonacci numbers.
    """
    fibs = []
    a, b = 0, 1
    while b < 100:
        if b >= 10:
            fibs.append(b)
        a, b = b, a + b
    return fibs

def generate_fibonacci_resources():
    """
    Generates a list of numbers consisting of three random Fibonacci numbers and four random numbers between 100 and 999.
    
    Returns:
        list: A list of numbers.
    """
  
    fibonacci_numbers = three_digit_fibonacci()
    
    selected_fibonacci = random.sample(fibonacci_numbers, 3)
    
   
    # random_numbers = [random.randint(10, 100) for _ in range(4)]
    
   
    # result = selected_fibonacci + random_numbers
    # random.shuffle(result)
    
    return selected_fibonacci
    return result



fibonacci_resources = generate_fibonacci_resources()
print(fibonacci_resources)
