from lab1.RandomGenerator import square_middle_method, multiplicative_congruental_method, get_k_by_m, get_bar_chart
from lab1.PlotDrawer import PlotDrawer
from Tkinter import *


def quit_wrapper(mainwin):
    def quit():
        mainwin.destroy()
        sys.exit()

    return quit


def main(args):
    mainwin = Tk()
    mainwin.columnconfigure(0, weight=1)
    mainwin.rowconfigure(0, weight=1)
    plotdrawer = PlotDrawer(mainwin)
    square_middle = square_middle_method(8, 17856392)
    m = 2 ** 31 - 1
    k = 48271
    mult_cong = multiplicative_congruental_method(17856391, m, k)
    plotdrawer.draw(get_bar_chart(10, 0, 1), square_middle, mult_cong)
    mainwin.mainloop()


if __name__ == "__main__":
    main(sys.argv)
