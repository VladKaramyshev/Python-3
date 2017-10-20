"""3. Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
    и возвращающую True,если оно простое, и False - иначе."""
import math

def is_prime(x):
    if x == 0:
    	return False	
    for i in range(2, round(math.sqrt(x))):
    	if x % i == 0:
    		return False	
  	return True