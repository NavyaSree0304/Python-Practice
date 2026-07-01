import math
import random
import platform

print("Math Module")
print(math.sqrt(64))
print(math.factorial(5))
print(math.pi)
print(math.ceil(4.2))
print(math.floor(4.8))

print("\nRandom Module")
print(random.randint(1, 10))
print(random.choice(["Python", "AI", "ML"]))
print(random.randrange(1, 100))

print("\nPlatform Module")
print(platform.system())
print(platform.machine())
print(platform.processor())
print(platform.python_version())
