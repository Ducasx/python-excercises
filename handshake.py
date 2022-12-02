def print_handshakes(people):
    handshakes = 0

    people2 = []
    for person in people:
        people2.append(person)

    for person in people:
        for person2 in people2:
            if person != person2:
                handshakes += 1
                print(person + ' shakes hand with ' + person2)
        people2.pop(0)

    print('-=-=-=-=-=-=-')

    return handshakes

assert print_handshakes(['Alice', 'Bob']) == 1
assert print_handshakes(['Alice', 'Bob', 'Carol']) == 3
assert print_handshakes(['Alice', 'Bob', 'Carol', 'David']) == 6