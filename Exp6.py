# Write the python program for Vacuum Cleaner problem 
import random
room = [[random.randint(0,1) for _ in range(4)] for _ in range(4)]
print("All the rooms are dirty (1 = dirty, 0 = clean)")
print(room)
print("\nBefore cleaning the room, I detect all of these random dirts")
print(room)
total_cells = 16
cleaned = 0
x, y = 0, 0
for i in range(4):
    for j in range(4):
        x, y = i, j
        print(f"\nVacuum in this location now, {x} {y}")
        if room[x][y] == 1:
            room[x][y] = 0
            cleaned += 1
            print(f"Cleaned {x} {y}")
        else:
            print("Already clean")
print("\nRoom is clean now, Thanks for using : A.SAFARJI CLEANER")
print(room)
percentage = (cleaned / total_cells) * 100
print(f"Cleaning Efficiency: {percentage:.2f} %")