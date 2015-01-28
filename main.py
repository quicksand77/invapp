__author__ = 'root'

from Tkinter import *

class InvForm:
    def __init__(self):

        # initialize the form
        self.root = Tk()
        self.root.title("Inventory Application Form")
        testbuttn1 = Radiobutton(self.root, text = "test button1", value = '12').grid(row=1, column = 1)
        testbuttn2 = Radiobutton(self.root, text = "test button2", value = '14').grid(row=1, column = 2)
        closeButton = Button(self.root, text = "Exit", command = self.close).grid(row=2, column = 1)

        self.root.mainloop()

    def close(self):
        print "Thank you for using the Inventory Application Form"
        self.root.destroy()


if __name__ == "__main__":
    print "please launch using blah blah"
    form = InvForm()
    form()