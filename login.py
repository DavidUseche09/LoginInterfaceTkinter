import tkinter as tk 
from tkinter import ttk, messagebox
 
class Login(tk.Tk):
    def __init__(self):
        super().__init__()
            #Main Window
        self.geometry('300x130')
        self.title('Login')
        self.resizable(0,0)
           #Grid Config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._componentsCreation()

    def _componentsCreation(self):
            #User
        userLabel = ttk.Label(self, text='User: ')
        userLabel.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.userEntry = ttk.Entry(self)
        self.userEntry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
            #Password
        passwordLabel = ttk.Label(self, text='Password: ')
        passwordLabel.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.passwordEntry = ttk.Entry(self, show="*")
        self.passwordEntry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
            #Login Button
        logginButton = ttk.Button(self, text='Login', command=self._login)
        logginButton.grid(row=3, column=0, columnspan=2)
    
            #Login function
    def _login(self):
        messagebox.showinfo('Login Data: ', f'User: {self.userEntry.get()} \n Password: {self.passwordEntry.get()}')

#Window Execution
if __name__ == '__main__':
    loginWindow = Login()
    loginWindow.mainloop()