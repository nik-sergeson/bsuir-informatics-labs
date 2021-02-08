from __future__ import division
from lab1.RandomGenerator import multiplicative_congruental_method
from lab2.EventSimulators import *
import sys

def main(args):
    tests_quantity=100
    m = 2 ** 31 - 1
    k = 48271
    mult_cong = multiplicative_congruental_method(17856391, m, k)
    simple_probability=0.7
    simple_simulator=random_event_simulator(mult_cong, simple_probability)
    event_happened=0
    print("Testing simple event with probability={}".format(simple_probability))
    for i in xrange(tests_quantity):
        if simple_simulator.next():
            event_happened+=1
    print("Event happened {} times in {} tests".format(event_happened, tests_quantity))
    print("\n\n")
    mult_cong = multiplicative_congruental_method(17856391, m, k)
    AB_happened=0
    A_nB_happened=0
    nA_B_happened=0
    nA_nB_happened=0
    A_probability=0.4
    B_probability=0.5
    complex_simulator=complex_event_simulator(mult_cong, A_probability, B_probability)
    print("Testing complex event with probability Pa={} Pb={}".format(A_probability, B_probability))
    for i in xrange(tests_quantity):
        A_evnt, B_evnt=complex_simulator.next()
        if A_evnt and B_evnt:
            AB_happened+=1
        elif A_evnt and  not B_evnt:
            A_nB_happened+=1
        elif not A_evnt and B_evnt:
            nA_B_happened+=1
        else:
            nA_nB_happened+=1
    print("AB happened {}\nAnB happened {}\nnAB happened {}\nnAnB happened {} times in {} tests".format(AB_happened, A_nB_happened,
                                                                                                        nA_B_happened, nA_nB_happened,
                                                                                                        tests_quantity))
    print("\n\n")
    mult_cong = multiplicative_congruental_method(17856391, m, k)
    AB_happened=0
    A_nB_happened=0
    nA_B_happened=0
    nA_nB_happened=0
    A_probability=0.4
    B_probability=0.5
    Pb_a=0.4
    complex_simulator=complex_dependent_event_simulator(mult_cong, A_probability, B_probability, Pb_a)
    Pb_not_a = B_probability - Pb_a * A_probability
    Pb_not_a /= 1 - A_probability
    print("Testing complex event consisting of dependent events with probability Pa={} Pb_!a={} Pb_a={}".format(A_probability, Pb_not_a, Pb_a))
    for i in xrange(tests_quantity):
        A_evnt, B_evnt=complex_simulator.next()
        if A_evnt and B_evnt:
            AB_happened+=1
        elif A_evnt and  not B_evnt:
            A_nB_happened+=1
        elif not A_evnt and B_evnt:
            nA_B_happened+=1
        else:
            nA_nB_happened+=1
    print("AB happened {}\nAnB happened {}\nnAB happened {}\nnAnB happened {} times in {} tests".format(AB_happened, A_nB_happened,
                                                                                                        nA_B_happened, nA_nB_happened,
                                                                                                        tests_quantity))
    print("\n\n")
    mult_cong = multiplicative_congruental_method(17856391, m, k)
    probabilities=[0.3, 0.2, 0.1, 0.4]
    event_happened={n:0 for n in xrange(1, len(probabilities)+1)}
    complex_simulator=full_group_event_simulator(mult_cong, probabilities)
    print("Testing full group events with probabilities P={}".format(probabilities))
    for i in xrange(tests_quantity):
        i=complex_simulator.next()
        event_happened[i]+=1
    for i, quant in event_happened.items():
        print("Event {} happened {} times".format(i, quant))

if __name__ == "__main__":
    main(sys.argv)
