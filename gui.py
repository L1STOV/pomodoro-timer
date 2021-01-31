from tkinter import *

root = Tk()


def gui():

    root['bg'] = 'red'
    root.title('Pomodoro')
    root.iconbitmap('img/tomato_1.ico')
    root.wm_attributes('-alpha', 0.9)
    root.geometry('500x250')
    root.resizable(width=False, height=False)

    pomodoro_label = Label(root, text='Pomodoro timer', font=('Comic Sans MS', 25, 'bold'))
    pomodoro_label.pack()
    pomodoro_label.config(bd=20, bg='red')

    root.mainloop()


if __name__ == '__main__':
    gui()
