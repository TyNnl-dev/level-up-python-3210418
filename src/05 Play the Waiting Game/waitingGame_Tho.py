import time
import random

def waiting_game():
  number = random.randrange(2, 4) # will generate numbers from 2 to 4
  print(f"Your target time is {number} seconds")
  input("---Press Enter to Begin---")
  start_time = time.time()
  input(f"...Press Enter again after {number} seconds...")
  end_time = time.time()
  elapsed_time = round(end_time - start_time, 3)
  
  print(f"Elapsed time: {elapsed_time} seconds")
  if elapsed_time > number:
    tmp_time = round(elapsed_time - number, 3)
    print(f"{tmp_time} seconds too slow")
  elif elapsed_time < number:
    tmp_time = round(number - elapsed_time, 3)
    print(f"{tmp_time} seconds too fast")
  else:
    print("Wow you're a winner")

waiting_game()