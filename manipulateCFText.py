from itertools import islice

with open("rank.txt") as f:
    for line in f:
        if "Jim Foley" in line:
            print(''.join(islice(f,47)))
