def to_cycles(perm):
    # pi = dict([i + 1, perm[i]] for i, _ in enumerate(perm))
    pi = {i + 1: perm[i] for i, _ in enumerate(perm)}
    cycles = []
    while pi:
        elem = next(iter(pi))
        this_elem = pi[elem]
        next_item = pi[this_elem]
        cycle = []
        while True:
            cycle.append(this_elem)
            del pi[this_elem]
            this_elem = next_item
            if next_item in pi:
                next_item = pi[next_item]
            else:
                break
        cycles.append(cycle)
    return cycles