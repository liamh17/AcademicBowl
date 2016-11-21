from tkinter import *
import math

"""
We'll need to use GPIO pins on the rasberry pi to
accomplish our goal of reading buttons.

    TODO:
    - add our pins and gpio ports
    - finish display
    - + 20, 10, or 5 pts if answer is CORRECT
    - - 20, 10, or 5 pts if answer is INCORRECT

    I DON'T NEED GPIO PORTS
    ALL I NEED IS BUTTONS TO CLICK
    EASY
"""

class AcademicBowlOperator(Frame):
    """ GUI: KEEPS AND DISPLAYS SCORES BASED ON BUTTON INPUT """
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # create all of our buttons, labels, etc.
        
        fj_score_txt = "Father Judge's score ->"
        lf_score_txt = "Little Flower's score ->"
        ar_score_txt = "Ryan's score ->"
        sh_score_txt = "St. Hubert's score ->"
        answer_disp_txt = "Is the answer correct or incorrect? Please click one."

        corr_button_txt = "Correct"
        incorr_button_txt = "Incorrect"
        
        self.fj_score = Label(self, text = fj_score_txt)
        self.lf_score = Label(self, text = lf_score_txt)
        self.ar_score = Label(self, text = ar_score_txt)
        self.sh_score = Label(self, text = sh_score_txt)
        self.answer_disp = Label(self, text = answer_disp_txt)

        self.fj_score.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.lf_score.grid(row = 1, column = 0, columnspan = 2, sticky = W)
        self.ar_score.grid(row = 2, column = 0, columnspan = 2, sticky = W)
        self.sh_score.grid(row = 3, column = 0, columnspan = 2, sticky = W)
        self.answer_disp.grid(row = 6, column = 0, columnspan = 2, sticky = W)

        self.corr_button = Button(self, text = corr_button_txt)
        self.incorr_button = Button(self, text = incorr_button_txt)

        self.corr_button.grid(row = 7, column = 0, sticky = W)
        self.incorr_button.grid(row = 8, column = 0, sticky = W)
        

    def quit(self):
        self.destroy()

root = Tk()
root.title("Score Calculator - Academic Bowl 2017")
root.geometry("500x200")
display = AcademicBowlOperator(root)

root.mainloop()
