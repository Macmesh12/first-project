import numpy as np
import math
import tkinter as tk
num1 = int(input("The first number: "))
num2 = int(input("The second number: "))

def find_first_common_multiple(num1, num2):
    multiples_num1 = set(range(num1, num1*num2+1, num1))
    multiples_num2 = set(range(num2, num1*num2+1, num2))
    
    common_multiples = multiples_num1.intersection(multiples_num2)
    
    if common_multiples:
        first_common_multiple = min(common_multiples)
        print("The lowest common multiple of", num1, "and", num2, "is:", first_common_multiple)
    else:
        print("There are no common multiples between", num1, "and", num2)



find_first_common_multiple(num1, num2)


# Create the GUI window
root = tk.Tk()
root.title("Lowest common Multiple")
root.heigh

# Input fields
label1 = tk.Label(root, text="Enter Number 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter Number 2:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Button to find common multiple
find_button = tk.Button(root, text="Find Common Multiple", command=find_first_common_multiple)
find_button.pack()

# Display result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()




