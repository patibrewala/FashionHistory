import sys
from tkinter import *
from PIL import ImageTk,Image 


sys.path.append('../')
from my_module.functions import *
sys.path.append/my_module

# Create a tkinter window named root
root= Tk()
# Title of the window
root.title("Fashion History")
# Size of the window
root.geometry("600x800")

def decade_or_apparel():
    """
    Finds whether input from entry widget is a year or a clothing item,
    gets the history of input by calling respective functions 
    and inserts that history in the text widget.
    """

    # get the text enetered by user in the entry widget
    input_txt = entry_year_or_apparel.get()

    # check for invalid input
    if input_txt == '' or input_txt == ' ':
        output_info = "Invalid Input"

    # print decade history if input is a year
    elif input_txt.isdigit():
        output_info = print_decade_info(input_txt)
        
    # print apparel history if input is a valid string
    else:
        output_info = print_apparel_info(input_txt)

    # delete previous text in the text widegt
    output.delete(0.0, END)

    # insert the new information to the text widget
    output.insert(END, output_info)

def to_exit():
    """
    To close the tkinter window and end the program
    """

    # destroy the root window
    root.destroy()
    # exit out of the program
    exit()


intro_txt = """
Welcome! I am here to tell you the fashion history through decades from the 
1850s. I can also tell you the history of a particular article of clothing. 
Enter a year like 2005, 1994, or 1876 to find out the fashion history of that 
decade or enter a clothing item like crop top, jeans or sun dress to find out 
history of that peice.
""" 

# open an image and display it in the root window
intro_img = Image.open("Fashion.png")
resized0=intro_img.resize((400, 150), Image.ANTIALIAS)
new_img0 = ImageTk.PhotoImage(resized0)

intro_label_img = Label(root, image=new_img0)
intro_label_img.grid(row=0, column=0) 

# display the first introduction label in the root window
intro_label_txt = Label(root, text=intro_txt, font="none 12 bold")
intro_label_txt.grid(row=1, column=0) 

# create an entry widget to get input from user
entry_year_or_apparel = Entry (root) 
entry_year_or_apparel.grid(row=2, column=0)

# button widget to rpint fashion history
print_history_button = Button(root, text="Get Fashion History", 
    command=decade_or_apparel)
print_history_button.grid(row=3, column=0)

# buttton to quit of the program
exit_button = Button(root, text="Quit", bg='red', command=to_exit)
exit_button.grid(row=4, column=0)

# text widget to print the fashion history
output = Text(root)
output.grid(row=5, column=0, padx=10)
output.configure(font=("Comic Sans MS", 12))

root.mainloop() 