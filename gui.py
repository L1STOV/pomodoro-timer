from tkinter import *


def gui():
    root = Tk()

    root['bg'] = 'red'
    root.title('Pomodoro')
    root.wm_attributes('-alpha', 0.7)
    root.geometry('500x250')

    root.resizable(width=False, height=False)

    root.mainloop()


if __name__ == '__main__':
    gui()
