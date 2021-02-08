from __future__ import division
import bisect
from lab1.BasisMatricesHelper import get_basis_matrix, get_basis_c_vector
from math import floor
from sympy.matrices import Matrix, zeros
from lab3.SimplexMethod import SimplexMethod
from ..DualSimplexMethod import DualSimplexMethod

class CuttingPlaneMethod(object):
    """
    :rtype A_matrix:MutableDenseMatrix
    """


    def __init__(self, A_matrix, b_matrix, c_matrix, condition_operators=None, eps=0.000001):
        self.A_matrix=A_matrix
        self.b_matrix=b_matrix
        self.c_matrix=c_matrix
        if condition_operators is None:
            self.condition_operators = ["="] * self.b_matrix.shape[0]
        else:
            self.condition_operators = condition_operators
        self.eps=eps
        self.var_quantity=self.A_matrix.shape[1]


    def solve(self, maximize):
        J_synt=[]
        J_synt_limitations={}
        solver=SimplexMethod(self.c_matrix, self.A_matrix, self.b_matrix, self.eps, self.condition_operators)
        plan, J_basis=solver.solve(maximize)
        while True:
            J_not_basis=sorted(set(range(plan.shape[0]))-set(J_basis))
            J_inter=sorted(set(J_basis).intersection(set(J_synt)))
            if J_inter:
                for j in J_inter:
                    b_j=self.b_matrix[J_synt_limitations[j], 0]
                    a_j=self.A_matrix[J_synt_limitations[j], :]
                    a_j/=-a_j[0,j]
                    b_j/=-a_j[0, j]
                    for i in xrange(self.A_matrix.shape[0]):
                        factor=self.A_matrix[i, j]
                        self.b_matrix[i, 0]+=factor*b_j
                        self.A_matrix[i, :]+=factor*a_j
                    J_basis.remove(j)
                    J_synt.remove(j)
                for j in reversed(J_inter):
                    self.A_matrix.col_del(j)
                    self.A_matrix.row_del(J_synt_limitations[j])
                    for j_synt in J_synt_limitations.iterkeys():
                        if J_synt_limitations[j_synt]>J_synt_limitations[j]:
                            J_synt_limitations[j_synt]-=1
                    self.b_matrix.row_del(J_synt_limitations[j])
                    self.condition_operators.pop(J_synt_limitations[j])
                    plan.row_del(j)
                    self.c_matrix.row_del(j)
                for i,j in enumerate(J_basis):
                    pos=bisect.bisect_left(J_inter, j)
                    J_basis[i]-=pos
                for i,j in enumerate(J_not_basis):
                    pos=bisect.bisect_left(J_inter, j)
                    J_not_basis[i]-=pos
                for i,j in enumerate(J_synt):
                    pos=bisect.bisect_left(J_inter, j)
                    if pos>0:
                        J_synt_limitations[j-pos]=J_synt_limitations[j]
                        del J_synt_limitations[j]
                        J_synt[i]-=pos
            j_0=-1
            for i in J_basis:
                if abs(plan[i, 0] - round(plan[i, 0])) > self.eps:
                    j_0 = i
                    break
            if j_0==-1:
                return plan[:self.var_quantity, :]
            k=J_basis.index(j_0)
            inverse_basis_matrix=get_basis_matrix(self.A_matrix, J_basis).inv()
            vector_a=zeros(self.A_matrix.shape[1], 1)
            for j in J_not_basis:
                a_j=(inverse_basis_matrix*self.A_matrix[:, j])[k, 0]
                vector_a[j, 0]=a_j-floor(a_j)
            beta=Matrix([plan[j_0, 0]-floor(plan[j_0, 0])])
            A_matrix=zeros(self.A_matrix.shape[0]+1, self.A_matrix.shape[1]+1)
            A_matrix[:-1, :-1]=self.A_matrix[:, :]
            A_matrix[-1, :-1]=vector_a.transpose()
            A_matrix[-1, -1]=-1
            self.A_matrix=A_matrix
            self.b_matrix=self.b_matrix.row_insert(self.b_matrix.shape[0], beta)
            self.c_matrix=self.c_matrix.row_insert(self.c_matrix.shape[0], zeros(1,1))
            self.condition_operators.append('=')
            new_var=self.A_matrix.shape[1]-1
            J_synt_limitations[new_var]=self.A_matrix.shape[0]-1
            bisect.insort_left(J_synt, new_var)
            bisect.insort_left(J_basis, new_var)
            inverse_basis_matrix=get_basis_matrix(self.A_matrix, J_basis).inv()
            solver = DualSimplexMethod(self.c_matrix, self.A_matrix, self.b_matrix, self.eps, self.condition_operators)
            plan, J_basis = solver.solve(maximize, J_basis)