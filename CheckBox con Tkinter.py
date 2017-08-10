import tkinter as tk
from tkinter import ttk
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Checkbutton en tkinter")
        
        self.checkbox_value = tk.BooleanVar(self)
        self.checkbox = ttk.Checkbutton(self,
            text="Opción",
            variable=self.checkbox_value,
            command=self.checkbox_clicked)
        self.checkbox.place(x=40, y=70)
        
        self.place(width=300, height=200)
    
    def checkbox_clicked(self):
        print(self.checkbox_value.get())
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
