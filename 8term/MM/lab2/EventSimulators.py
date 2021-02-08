from __future__ import division


def random_event_simulator(random_generator, Pa):
    while True:
        x = random_generator.next()
        yield x <= Pa


def complex_event_simulator(random_generator, Pa, Pb):
    while True:
        x1 = random_generator.next()
        x2 = random_generator.next()
        yield x1 <= Pa, x2 <= Pb


def complex_dependent_event_simulator(random_generator, Pa, Pb, Pb_a):
    Pb_nota = (Pb - Pb_a * Pa) / (1 - Pa)
    while True:
        x1 = random_generator.next()
        x2 = random_generator.next()
        if x1 <= Pa and x2 <= Pb_a:
            yield True, True
        elif x1 > Pa and x2 <= Pb_nota:
            yield False, True
        elif x1 <= Pa and x2 > Pb_a:
            yield True, False
        elif x1 > Pa and x2 > Pb_a:
            yield False, False


def full_group_event_simulator(random_generator, group_probabilities):
    assert abs(sum(group_probabilities) - 1) < 0.01
    probabilities=[0]
    for prob in group_probabilities:
        probabilities.append(probabilities[-1]+prob)
    while True:
        x1 = random_generator.next()
        for i in range(1,len(probabilities)):
            if probabilities[i-1] <= x1 and x1 < probabilities[i]:
                yield i
                break
        else:
            yield len(probabilities)-1