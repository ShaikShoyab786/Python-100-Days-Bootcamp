import random

rand_num = random.randint(1,10)
print(rand_num)

if rand_num <=5:
    print("Heads")
elif rand_num >5 and rand_num <=10:
    print("Tails")
else:
    print("Oops Something is fishy")

