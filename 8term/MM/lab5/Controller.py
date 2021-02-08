import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from TwoDimRandomValue import *
import yaml
class Controller(QWidget):

    def __init__(self, row_count, col_count, prob_values, A_values, B_values, uniform_generator):
        QWidget.__init__(self)
        layout = QGridLayout(self)
        self.uniform_generator=uniform_generator
        self.row_count_input=QLineEdit(str(row_count),self)
        self.col_count_input=QLineEdit(str(col_count),self)
        A_size_label=QLabel("A size",self)
        B_size_label=QLabel("B size", self)
        self.implementation_size=QLineEdit(str(100), self)
        implementation_size_label=QLabel("Implementation size", self)
        self.size_button = QPushButton('Resize', self)
        self.size_button.clicked.connect(self.resize_button_clicked)
        self.generate_button=QPushButton("Generate", self)
        self.generate_button.clicked.connect(self.generate_button_clicked)
        self.result_output=QPlainTextEdit()
        self.inp_probability_table = QTableWidget()
        self.inp_probability_table.setRowCount(row_count)
        self.inp_probability_table.setColumnCount(col_count)
        for i in range(row_count):
            for j in range(col_count):
                self.inp_probability_table.setItem(i, j, QTableWidgetItem(str(prob_values[i][j])))
        self.A_table = QTableWidget()
        self.A_table.setRowCount(1)
        self.A_table.setColumnCount(row_count)
        for i in range(row_count):
            self.A_table.setItem(0, i, QTableWidgetItem(str(A_values[i])))
        self.B_table = QTableWidget()
        self.B_table.setRowCount(1)
        self.B_table.setColumnCount(col_count)
        for i in range(col_count):
            self.B_table.setItem(0, i, QTableWidgetItem(str(B_values[i])))
        self.gen_probability_table=QTableWidget()
        self.gen_probability_table.setRowCount(row_count)
        self.gen_probability_table.setColumnCount(col_count)
        self.A_hist=MyMplCanvas(self)
        self.B_hist=MyMplCanvas(self)
        layout.addWidget(A_size_label, 0,0,1,1)
        layout.addWidget(self.row_count_input, 0, 1, 1, 1)
        layout.addWidget(B_size_label, 0,2,1,1)
        layout.addWidget(self.col_count_input, 0, 3, 1, 1)
        layout.addWidget(self.size_button, 0, 4, 1, 1)
        layout.addWidget(implementation_size_label, 0,5,1,1)
        layout.addWidget(self.implementation_size, 0,6,1,1)
        layout.addWidget(self.generate_button, 0,7, 1,1)
        self.A_table.setMaximumHeight(60)
        self.B_table.setMaximumHeight(60)
        layout.addWidget(self.A_table, 1, 0, 1, 4)
        layout.addWidget(self.B_table, 1, 4, 1, 4)
        layout.addWidget(self.inp_probability_table, 2, 0, 2, 4)
        layout.addWidget(self.gen_probability_table, 4,0, 2,4)
        layout.addWidget(self.A_hist, 2, 4, 2, 4)
        layout.addWidget(self.B_hist, 4, 4, 2, 4)
        layout.addWidget(self.result_output, 6, 0, 2, 8)

    def resize_button_clicked(self):
        row_count=int(self.row_count_input.text())
        col_count=int(self.col_count_input.text())
        self.A_table.setColumnCount(row_count)
        self.B_table.setColumnCount(col_count)
        self.inp_probability_table.setColumnCount(col_count)
        self.inp_probability_table.setRowCount(row_count)
        self.gen_probability_table.setColumnCount(col_count)
        self.gen_probability_table.setRowCount(row_count)

    def generate_button_clicked(self):
        eps=0.01
        implement_size=int(self.implementation_size.text())
        probabilities=[]
        for i in xrange(self.inp_probability_table.rowCount()):
            prob_row=[]
            for j in xrange(self.inp_probability_table.columnCount()):
                prob_row.append(yaml.load(str(self.inp_probability_table.item(i,j).text())))
            probabilities.append(prob_row)
        x_values=[]
        for i in xrange(self.A_table.columnCount()):
            x_values.append(yaml.load(str(self.A_table.item(0, i).text())))
        y_values=[]
        for i in xrange(self.B_table.columnCount()):
            y_values.append(yaml.load(str(self.B_table.item(0,i).text())))
        x_distrib_series=get_x_distribution_series(x_values, probabilities)
        x_distrib_func=get_x_distribution_function(x_distrib_series)
        y_distrib_series=get_conditional_distribution_series(probabilities, x_values, y_values, x_distrib_series)
        y_distrib_func=get_y_distribution_function(x_values, y_values, y_distrib_series)
        two_dim_generator=two_dim_value_generator(x_values, y_values, x_distrib_func, y_distrib_func, self.uniform_generator)
        two_dim_values=[two_dim_generator.next() for i in xrange(implement_size)]
        two_dim_values_unzip=zip(*two_dim_values)
        gen_x_values=list(two_dim_values_unzip[0])
        gen_y_values=list(two_dim_values_unzip[1])
        bar_chart_x=get_bar_chart(20, min(gen_x_values)-eps, max(gen_x_values)+eps)(gen_x_values)
        bar_chart_y=get_bar_chart(20, min(gen_y_values)-eps, max(gen_y_values)+eps)(gen_y_values)
        self.A_hist.compute_figure(bar_chart_x, "X bar chart")
        self.B_hist.compute_figure(bar_chart_y, "Y bar chart")
        cond_distrib=get_conditional_distribution(x_values, y_values, two_dim_values)
        for i in xrange(len(cond_distrib)):
            for j in xrange(len(cond_distrib[i])):
                if self.gen_probability_table.item(i,j) is not None:
                    self.gen_probability_table.item(i,j).setText(str(cond_distrib[i][j]))
                else:
                    self.gen_probability_table.setItem(i,j, QTableWidgetItem(str(cond_distrib[i][j])))
        exp_value_x=get_expected_value_x(cond_distrib, x_values)
        exp_value_y=get_expected_value_y(cond_distrib, y_values)
        disper_x=get_dispersion_x(cond_distrib, x_values, exp_value_x)
        disper_y=get_dispersion_y(cond_distrib, y_values, exp_value_y)
        correl=get_correlation_coefficient(cond_distrib, x_values, y_values)
        self.result_output.document().setPlainText("M[x]={}\nM[y]={}\nD[x]={}\nD[y]={}\nr={}\n{}".format(exp_value_x, exp_value_y,
                                                                                             disper_x, disper_y, correl,str(two_dim_values)))




class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.hold(False)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_figure(self, bar_chart, title):
        left=[]
        height=[]
        for a, b, f in bar_chart:
            left.append(a)
            height.append(f)
        self.axes.bar(left, height, width=bar_chart[0][1]-bar_chart[0][0])
        self.axes.axis([bar_chart[0][0], bar_chart[-1][1], 0, 1])
        self.axes.set_xlabel('X')
        self.axes.set_ylabel('Density')
        self.axes.set_title(title)
        self.draw()
