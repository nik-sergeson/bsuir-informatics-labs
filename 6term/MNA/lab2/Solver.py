__author__ = 'nik-u'
import math
import random
import sys
from sympy import Matrix, eye, Symbol,zeros


class Solver:
    def __init__(self, precision, epsilon, relaxation_q=0.01):
        self.precision = precision
        self.epsilon=epsilon
        self.relaxation_q=relaxation_q
        self.relaxation_l=1000
        self.relaxation_omega=sorted([random.uniform(0, 2) for i in xrange(100)])

    def matrix_norm_1(self, matrix):
        row_count, col_count=matrix.shape
        row_amounts=[]
        for i in xrange(row_count):
            current_sum=0
            for j in xrange(col_count):
                current_sum+=abs(matrix[i, j])
            row_amounts.append(current_sum)
        return max(row_amounts)

    def matrix_norm_2(self, matrix):
        row_count, col_count=matrix.shape
        row_amounts=[]
        for i in xrange(col_count):
            current_sum=0
            for j in xrange(row_count):
                current_sum+=abs(matrix[j, i])
            row_amounts.append(current_sum)
        return max(row_amounts)

    def matrix_norm_3(self, matrix):
        row_count, col_count=matrix.shape
        current_sum=0
        for i in xrange(row_count):
            for j in xrange(col_count):
                current_sum+=matrix[i,j]*matrix[i,j]
        return math.sqrt(current_sum)

    def vector_norm_1(self, vector):
        row_count, col_count=vector.shape
        max_elem=abs(vector[0,0])
        for i in xrange(1, row_count):
            max_elem=max(max_elem, abs(vector[i]))
        return max_elem

    def vector_norm_2(self, vector):
        row_count, col_count=vector.shape
        row_sum=abs(vector[0,0])
        for i in xrange(1, row_count):
            row_sum+=abs(vector[i,0])
        return row_sum

    def vector_norm_3(self, vector):
        row_count, col_count=vector.shape
        row_sum=0
        for i in xrange(row_count):
            row_sum+=vector[i, 0]*vector[i, 0]
        return math.sqrt(row_sum)

    def jacobi_transformation(self, matrix_A, matrix_f):
        row_count, col_count=matrix_A.shape
        for i in xrange(row_count):
            if matrix_A[i ,i] == 0:
                raise ValueError("Null diagonal element")
        matrix_B=zeros(row_count, col_count)
        matrix_c=zeros(row_count, 1)
        for i in xrange(row_count):
            for j in xrange(col_count):
                if i!=j:
                    matrix_B[i, j]= -1.0*matrix_A[i, j]/matrix_A[i, i]
            matrix_c[i, 0]=1.0*matrix_f[i, 0]/matrix_A[i, i]
        return (matrix_B, matrix_c)

    def add_x_matrix_transformation(self, matrix_A, matrix_f):
        row_count, col_count=matrix_A.shape
        matrix_B=eye(row_count)-matrix_A
        matrix_c=matrix_f.copy()
        return (matrix_B, matrix_c)

    def get_tau_parametr_transformation(self,a, b, n):
        def tau_parametr_transformation(matrix_A, matrix_f):
            tau_list=sorted([random.uniform(a, b) for i in xrange(n)])
            row_count, col_count=matrix_A.shape
            matrix_dict={}
            for tau in tau_list:
                matrix_B=eye(row_count)-tau*matrix_A
                matrix_c=tau*matrix_f
                matrix_dict[tau]=(matrix_B,matrix_c)
            return matrix_dict
        return tau_parametr_transformation

    def solution_found(self, matrix_norm, vector_norm, x_i_next, x_i, matrix_B_norm, iteration_quantity, max_iteration_quantity):
        if matrix_norm is None:
            if vector_norm(x_i_next-x_i)<self.epsilon or iteration_quantity>=max_iteration_quantity:
                return True
        else:
            if matrix_B_norm*(1-matrix_B_norm)*vector_norm(x_i_next-x_i)<self.epsilon:
                return True
        return False

    def iterative_method(self, transformation_method, matrix_A, matrix_f):
        matrix_norm=None
        row_count, col_count=matrix_A.shape
        vector_norm=self.vector_norm_1
        relaxation_method_enabled=False
        iteration_quantity=0
        relaxation_method_matrices_i={}
        solutions={}
        solution_found=False
        solution_diff=sys.maxint
        solution_omega_index=0
        solution_tau_index=0
        matrix_B_norm=None
        if self.matrix_norm_1(matrix_A)<1:
            matrix_norm=self.matrix_norm_1
            vector_norm=self.vector_norm_1
        elif self.matrix_norm_2(matrix_A)<1:
            matrix_norm=self.matrix_norm_2
            vector_norm=self.vector_norm_2
        elif self.matrix_norm_3(matrix_A)<1:
            matrix_norm=self.matrix_norm_3
            vector_norm=self.vector_norm_3
        else:
            max_iteration_quantity=100
        matrices=transformation_method(matrix_A, matrix_f)
        if isinstance(matrices, tuple):
            matrix_B, matrix_c=matrices
            print(matrix_B)
            x_i=matrix_c.copy()
            if matrix_norm is not None:
                matrix_B_norm=matrix_norm(matrix_B)
            while True:
                iteration_quantity+=1
                if not relaxation_method_enabled:
                    x_i_next=matrix_B*x_i+matrix_c
                    if (matrix_norm is not None and 1-matrix_B_norm<self.relaxation_q) or (matrix_norm is None and iteration_quantity>self.relaxation_l):
                        if self.solution_found(matrix_norm, vector_norm,x_i_next,x_i, matrix_B_norm,iteration_quantity,max_iteration_quantity):
                            solutions['vector_x']=x_i_next
                            solutions['iteration_quantity']=iteration_quantity
                            break
                        relaxation_method_enabled=True
                        for omega in self.relaxation_omega:
                            relaxation_method_matrices_i[omega]=x_i_next.copy()
                    else:
                        if self.solution_found(matrix_norm, vector_norm,x_i_next,x_i, matrix_B_norm,iteration_quantity,max_iteration_quantity):
                                solutions['vector_x']=x_i_next
                                solutions['iteration_quantity']=iteration_quantity
                                break
                    x_i=x_i_next
                else:
                    for omega in self.relaxation_omega:
                        x_i=relaxation_method_matrices_i[omega].copy()
                        for i in xrange(col_count):
                            relaxation_method_matrices_i[omega][i, 0]=omega*(matrix_B[i, 0:]*x_i+matrix_c[i, 0])+(1-omega)*x_i[i, 0]
                        if self.solution_found(matrix_norm, vector_norm, relaxation_method_matrices_i[omega], x_i,
                                                               matrix_B_norm, iteration_quantity, max_iteration_quantity):
                            if not solution_found:
                                solution_found=True
                                solution_diff=vector_norm(relaxation_method_matrices_i[omega]-x_i)
                                solution_omega_index=omega
                            elif vector_norm(relaxation_method_matrices_i[omega]-x_i)<solution_diff:
                                solution_omega_index=omega
                                solution_diff=vector_norm(relaxation_method_matrices_i[omega]-x_i)
                    if solution_found:
                        solutions['vector_x']=relaxation_method_matrices_i[omega]
                        solutions['iteration_quantity']=iteration_quantity
                        solutions['omega']=solution_omega_index
                        break
        else:
            matrix_B_norm={}
            for tau in matrices:
                matrix_B, matrix_c=matrices[tau]
                if matrix_norm is not None:
                    matrix_B_norm[tau]=matrix_norm(matrix_B)
                matrices[tau].append(matrix_c.copy())
            solution_omega_index=0
            solution_tau_index=0
            while True:
                iteration_quantity+=1
                for tau in matrices:
                    matrix_B, matrix_c, x_i=matrices[tau]
                    if not relaxation_method_enabled:
                        x_i_next=matrix_B*x_i+matrix_c
                        if self.solution_found(matrix_norm, vector_norm,x_i_next,x_i, matrix_B_norm[tau],iteration_quantity,max_iteration_quantity):
                            if not solution_found:
                                solution_diff=vector_norm(x_i_next-x_i)
                                solution_found=True
                                solution_tau_index=tau
                            elif vector_norm(x_i_next-x_i)<solution_diff:
                                solution_tau_index=tau
                                solution_diff=vector_norm(x_i_next-x_i)
                        matrices[tau][2]=x_i_next
                    else:
                        for omega in self.relaxation_omega:
                            x_i=relaxation_method_matrices_i[tau][omega].copy()
                            for i in xrange(col_count):
                                relaxation_method_matrices_i[tau][omega][i, 0]=omega*(matrix_B[i, 0:]*x_i+matrix_c[i, 0])+(1-omega)*x_i[i, 0]
                            if self.solution_found(matrix_norm, vector_norm, relaxation_method_matrices_i[tau][omega], x_i,
                                                                   matrix_B_norm, iteration_quantity, max_iteration_quantity):
                                if not solution_found:
                                    solution_diff=vector_norm(relaxation_method_matrices_i[tau][omega]-x_i)
                                    solution_found=True
                                    solution_omega_index=omega
                                    solution_tau_index=tau
                                elif vector_norm(relaxation_method_matrices_i[tau][omega]-x_i)<solution_diff:
                                    solution_diff=vector_norm(relaxation_method_matrices_i[tau][omega]-x_i)
                                    solution_omega_index=omega
                                    solution_tau_index=tau
                if not relaxation_method_enabled:
                    if solution_found:
                        solutions['vector_x']=matrices[solution_tau_index][2]
                        solutions['iteration_quantity']=iteration_quantity
                        solutions['tau']=solution_tau_index
                        print("---------------Solutions after {0} iterations--------------".format(iteration_quantity))
                        for tau in matrices:
                            print "tau={0}".format(tau)
                            print(matrices[tau][2])
                        break
                    else:
                        for tau in matrices:
                            if (matrix_norm is not None and 1-matrix_B_norm[tau]<self.relaxation_q) or (matrix_norm is None and iteration_quantity>self.relaxation_l):
                                relaxation_method_enabled=True
                                break
                        if relaxation_method_enabled:
                            for tau in matrices:
                                relaxation_method_matrices_i[tau]={}
                                for omega in self.relaxation_omega:
                                    relaxation_method_matrices_i[tau][omega]=matrices[tau][2].copy()
                else:
                    if solution_found:
                        solutions['vector_x']=relaxation_method_matrices_i[solution_tau_index][solution_omega_index]
                        solutions['iteration_quantity']=iteration_quantity
                        solutions['tau']=solution_tau_index
                        solutions['omega']=solution_omega_index
                        print("---------------Solutions after {0} iterations--------------".format(iteration_quantity))
                        for omega in relaxation_method_matrices_i:
                            print "tau={0}, omega={1}".format(solution_tau_index, omega)
                            print(relaxation_method_matrices_i[solution_tau_index][omega])
                        break
        return solutions

    def seidel_method(self, transformation_method, matrix_A, matrix_f):
        matrix_norm=None
        row_count, col_count=matrix_A.shape
        vector_norm=self.vector_norm_1
        relaxation_method_enabled=False
        iteration_quantity=0
        matrix_B_norm=None
        relaxation_method_matrices_i={}
        solutions={}
        solution_found=False
        solution_omega_index=0
        solution_tau_index=0
        if self.matrix_norm_1(matrix_A)<1:
            matrix_norm=self.matrix_norm_1
            vector_norm=self.vector_norm_1
        elif self.matrix_norm_2(matrix_A)<2:
            matrix_norm=self.matrix_norm_2
            vector_norm=self.vector_norm_2
        elif self.matrix_norm_3(matrix_A)<1:
            matrix_norm=self.matrix_norm_3
            vector_norm=self.vector_norm_3
        else:
            max_iteration_quantity=100
        matrices=transformation_method(matrix_A, matrix_f)
        if isinstance(matrices, tuple):
            matrix_B, matrix_c=matrices
            x_i=matrix_c.copy()
            if matrix_norm is not None:
                matrix_B_norm=matrix_norm(matrix_B)
            matrix_L=matrix_B.copy()
            for i in xrange(row_count):
                for j in xrange(0, i+1):
                    matrix_L[i, j]=0
            matrix_U=matrix_B-matrix_L
            x_i_next=zeros(col_count, 1)
            while True:
                iteration_quantity+=1
                if not relaxation_method_enabled:
                    for i in xrange(col_count):
                        x_i_next[i, 0]=matrix_L[i, 0:]*x_i_next+matrix_U[i, 0:]*x_i+matrix_c[i,0]
                    if (matrix_norm is not None and 1-matrix_B_norm<self.relaxation_q) or (matrix_norm is None and iteration_quantity>self.relaxation_l):
                        if self.solution_found(matrix_norm, vector_norm,x_i_next,x_i, matrix_B_norm,iteration_quntity,max_iteration_quantity):
                            solutions['vector_x']=x_i_next
                            solutions['iteration_quantity']=iteration_quantity
                            break
                        relaxation_method_enabled=True
                        for omega in self.relaxation_omega:
                            relaxation_method_matrices_i[omega]=x_i_next.copy()
                    else:
                        if self.solution_found(matrix_norm, vector_norm,x_i_next,x_i, matrix_B_norm,iteration_quntity,max_iteration_quantity):
                                solutions['vector_x']=x_i_next
                                solutions['iteration_quantity']=iteration_quantity
                                break
                    x_i=x_i_next
                else:
                    solution_omega_index=0
                    solution_diff=0
                    for omega in self.relaxation_omega:
                        x_i=relaxation_method_matrices_i[omega].copy()
                        for i in xrange(col_count):
                            relaxation_method_matrices_i[omega][i, 0]=omega*(matrix_L[i, 0:]*relaxation_method_matrices_i[omega]+matrix_U[i, 0:]*x_i+matrix_c[i,0])+(1-omega)*x_i[i, 0]
                    if self.solution_found(matrix_norm, vector_norm, relaxation_method_matrices_i[omega], x_i,
                                                               matrix_B_norm, iteration_quantity, max_iteration_quantity):
                            if not solution_found:
                                solution_found=True
                                solution_diff=vector_norm(relaxation_method_matrices_i[omega]-x_i)
                                solution_omega_index=omega
                            elif vector_norm(relaxation_method_matrices_i[omega]-x_i)<solution_diff:
                                solution_omega_index=omega
                                solution_diff=vector_norm(relaxation_method_matrices_i[omega]-x_i)
                    if solution_found:
                        solutions['vector_x']=relaxation_method_matrices_i[omega]
                        solutions['iteration_quantity']=iteration_quantity
                        solutions['omega']=solution_omega_index
                        break
        else:
            matrix_B_norm={}
            matrix_L={}
            matrix_U={}
            for tau in matrices:
                matrix_B, matrix_c=matrices[tau]
                if matrix_norm is not None:
                    matrix_B_norm[tau]=matrix_norm(matrix_B)
                matrix_L[tau]=matrix_B.copy()
                for i in xrange(row_count):
                    for j in xrange(0, i+1):
                        matrix_L[tau][i, j]=0
                matrix_U[tau]=matrix_B-matrix_L[tau]
            solution_omega_index=0
            solution_tau_index=0
            while True:
                iteration_quantity+=1
                for tau in matrices:
                    if not relaxation_method_enabled:
                        matrix_B, matrix_c, x_i=matrices[tau]
                        x_i_next=zeros(col_count, 1)
                        for j in xrange(col_count):
                            x_i_next[j, 0]=matrix_L[tau][j, 0:]*x_i_next+matrix_U[tau][j, 0:]*x_i+matrix_c[j, 0]
                        if self.solution_found(matrix_norm, vector_norm,x_i_next,x_i, matrix_B_norm[tau],iteration_quantity,max_iteration_quantity):
                            if not solution_found:
                                solution_diff=vector_norm(x_i_next-x_i)
                                solution_found=True
                                solution_tau_index=tau
                            elif vector_norm(x_i_next-x_i)<solution_diff:
                                solution_tau_index=tau
                                solution_diff=vector_norm(x_i_next-x_i)
                        matrices[tau][2]=x_i_next
                    else:
                        for omega in self.relaxation_omega:
                            x_i=relaxation_method_matrices_i[tau][omega].copy()
                            for i in xrange(col_count):
                                relaxation_method_matrices_i[tau][omega][i, 0]=omega*(matrix_L[tau][i, 0:]*relaxation_method_matrices_i[tau][omega]+
                                                                                      matrix_U[tau][j, 0:]*x_i+matrix_c[j, 0])+(1-omega)*x_i[i, 0]
                            if self.solution_found(matrix_norm, vector_norm, relaxation_method_matrices_i[tau][omega], x_i,
                                                           matrix_B_norm, iteration_quantity, max_iteration_quantity):
                                if not solution_found:
                                    solution_diff=vector_norm(relaxation_method_matrices_i[tau][omega]-x_i)
                                    solution_found=True
                                    solution_omega_index=omega
                                    solution_tau_index=tau
                                elif vector_norm(relaxation_method_matrices_i[tau][omega]-x_i)<solution_diff:
                                    solution_diff=vector_norm(relaxation_method_matrices_i[tau][omega]-x_i)
                                    solution_omega_index=omega
                                    solution_tau_index=tau
                if not relaxation_method_enabled:
                    if solution_found:
                        solutions['vector_x']=matrices[solution_tau_index][2]
                        solutions['iteration_quantity']=iteration_quantity
                        solutions['tau']=solution_tau_index
                        print("---------------Solutions after {0} iterations--------------".format(iteration_quantity))
                        for tau in matrices:
                            print "tau={0}".format(tau)
                            print(matrices[tau][2])
                        break
                    else:
                        for tau in matrices:
                            if (matrix_norm is not None and 1-matrix_B_norm[tau]<self.relaxation_q) or (matrix_norm is None and iteration_quantity>self.relaxation_l):
                                relaxation_method_enabled=True
                                break
                        if relaxation_method_enabled:
                            for tau in matrices:
                                relaxation_method_matrices_i[tau]={}
                                for omega in self.relaxation_omega:
                                    relaxation_method_matrices_i[tau][omega]=matrices[tau][2].copy()
                else:
                    if solution_found:
                        solutions['vector_x']=relaxation_method_matrices_i[solution_tau_index][solution_omega_index]
                        solutions['iteration_quantity']=iteration_quantity
                        solutions['tau']=solution_tau_index
                        solutions['omega']=solution_omega_index
                        print("---------------Solutions after {0} iterations--------------".format(iteration_quantity))
                        for omega in relaxation_method_matrices_i:
                            print "tau={0}, omega={1}".format(solution_tau_index, omega)
                            print(relaxation_method_matrices_i[solution_tau_index][omega])
                        break
            return solutions
