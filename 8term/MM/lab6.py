from __future__ import division
import sys
import scipy.stats as sts
from PyQt4.QtGui import *
from lab6.Controller import Controller
from lab6.QSchemeSimulator import *


def main(args):
    app = QApplication(args)
    source = Source(sts.expon(scale=1))
    phase1_storage = StorageWithRefuseWithStatistics(3)
    phase1 = Phase(phase1_storage, sts.triang, DistributionParams(["loc", "scale"], 1 / 2, loc=2, scale=3), 5)
    phase2_storage = StorageWithStatistics(3)
    phase2 = Phase(phase2_storage, sts.uniform, DistributionParams(["loc", "scale"], loc=3, scale=6), 3)
    phase3_storage = StorageWithStatistics(3)
    phase3 = Phase(phase3_storage, sts.norm, DistributionParams(["loc", "scale"], loc=5, scale=1), 4)
    phase4_storage = StorageWithStatistics(3)
    phase4 = Phase(phase4_storage, sts.triang, DistributionParams(["loc", "scale"], 1, loc=3, scale=4), 3)
    phase5_storage = StorageWithStatistics(3)
    phase5 = Phase(phase5_storage, sts.norm, DistributionParams(["loc", "scale"], loc=5, scale=1), 5)
    end_storage = EndStorage()
    qscheme = QSchemeSimulator(source, [phase1, phase2, phase3, phase4, phase5], end_storage)
    controller = Controller(qscheme, 5)
    controller.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
