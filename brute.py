import itertools
import time

def brute_force_hello_world():
    target_string = "Hello World"
    possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

    start_time = time.time()

    for combination in itertools.product(possible_characters, repeat=len(target_string)):
        brute_force_attempt = ''.join(combination)
        if brute_force_attempt == target_string:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return brute_force_attempt, elapsed_time

    return "Brute force unsuccessful"

result, elapsed_time = brute_force_hello_world()
print(f"Result: {result}")
print(f"Elapsed Time: {elapsed_time} seconds")
