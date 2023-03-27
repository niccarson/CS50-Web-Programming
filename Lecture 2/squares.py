#importing from another sheet
from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")

# alternatively, can also just use "import functions"
# then the print statement would be print(f"The square of {i} is {functions.square(i)})