from __future__ import division
import sys
from PyQt4.QtGui import *
from lab5.Controller import Controller
from lab1.RandomGenerator import multiplicative_congruental_method


def main(args):
    app = QApplication(args)
    m = 2 ** 31 - 1
    k = 48271
    mult_cong = multiplicative_congruental_method(17856391, m, k)
    controller = Controller(2, 2, [[1 / 4, 1 / 4], [1 / 4, 1 / 4]], [1, 2], [3, 4], mult_cong)
    controller.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
