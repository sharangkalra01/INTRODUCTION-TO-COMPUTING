''' NAME = SHARANG KALRA
SID= 21103012
BRANCH = COMPUTER SCIENCE AND ENGINEERING'''

# Assignment 1
# QUESTION =4

Marks = []
for i in range(5):
    print("Enter Marks", i + 1, ": ", end="")
    x = int(input())
    Marks.append(x)
    # Sorting the marks list
    Marks.sort()
print("Sorted Order Of Marks are as  : ", Marks)

