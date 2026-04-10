# Imports
import time
import random

# :3
while True:
    x = random.randint(0, 2)

    match x:
        case 0: print("meow")
        case 1: print("mrrrp")
        case 2: print("mrraow")

    time.sleep(0.5)
