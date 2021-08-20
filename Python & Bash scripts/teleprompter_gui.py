import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import Button

#  default font size in text box
n = 45

#  function to open text files
def open_script():
    text_file = filedialog.askopenfilename(
        initialdir="~/home/pi/Desktop",
        title="Open",
        filetypes=(("Text Files", "*.txt"),)
        )
    text_file = open(text_file)
    file_cont = text_file.read()
    text_area.insert(tk.END, file_cont)
    
    text_file.close()
    text_area.focus()
  
# main tkinter window
win = tk.Tk()
win.title("Raspberry Pi Teleprompter")
  
# window title label
ttk.Label(win, 
          text = "Raspberry Pi Teleprompter",
          font = ("Times New Roman", 15), 
          foreground = "black").grid(column = 0,
                                     row = 0, pady = 20, padx = 10)

#  setup for text area
text_area = scrolledtext.ScrolledText(win, 
                                      wrap = tk.WORD, 
                                      width = 22, 
                                      height = 20, 
                                      font = ("Times New Roman",
                                              n))

#  grid for text area
text_area.grid(column = 0, pady = 10, padx = 10)

#  button to launch open text function
Button(win, text ="open",command=open_script).grid(column = 1, row = 0, pady = 20, padx = 10)

#  brings mouse into text area
text_area.focus()

#  make the window full screen
def full(event):
    win.attributes("-fullscreen", True)
#  make the window windowed
def minimize(event):
    win.attributes("-fullscreen", False)
#  bind escape key to minimize()
win.bind('<Escape>', minimize)
#  bind F1 to full screen
win.bind('<F1>', full)

#  default window to full screen
win.attributes("-fullscreen", True)

#  run program
win.mainloop()
