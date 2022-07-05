import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("320x80")
        self.title('Tkinter OptionMenu Widget')

        # initialize data
        self.languages = ('Python', 'JavaScript', 'Java',
                        'Swift', 'GoLang', 'C#', 'C++', 'Scala')

        # set up variable
        self.option_var = tk.StringVar(self)

        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # option menu
        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.languages[0],
            *self.languages)

        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

        # output label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, sticky=tk.W, **paddings)


if __name__ == "__main__":
    app = App()
    app.mainloop()