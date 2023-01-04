def tower_of_hanoi(n, source, dest, aux):
    if n == 1:
        print(f'Move disk {n - 1} from {source} to {dest}')
    else:
        tower_of_hanoi(n - 1, source, aux, dest)
        print(f'Move disk {n-1} from {source} to {dest}')
        tower_of_hanoi(n-1, aux, dest, source)

    return


tower_of_hanoi(4, "A", "B", "C")
