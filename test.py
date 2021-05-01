# # Import module
# from tkinter import *
  
# # Create object
# root = Tk()
  
# # Adjust size
# root.geometry( "200x200" )
  
# # Change the label text
# def show():
#     label.config( text = clicked.get() )
  
# # Dropdown menu options
# options = [
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday",
#     "Sunday"
# ]
  
# # datatype of menu text
# clicked = StringVar()
  
# # initial menu text
# clicked.set( "Monday" )
  
# # Create Dropdown menu
# drop = OptionMenu( root , clicked , *options )
# drop.pack()
  
# # Create button, it will change label text
# button = Button( root , text = "click Me" , command = show ).pack()
  
# # Create Label
# label = Label( root , text = " " )
# label.pack()
  
# # Execute tkinter
# root.mainloop()



from tkinter import *
 
# importing the choosecolor package
from tkinter import colorchooser
 
# Function that will be invoked when the
# button will be clicked in the main window
def choose_color():
 
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title ="Choose color")
    
 
root = Tk()
button = Button(root, text = "Select color",
                   command = choose_color)
button.pack()
root.geometry("300x300")
root.mainloop()