f = open("../tables/A000001", "r")


seq = []
while True:
    line = f.readline()
    if line == '':break
    a, b = line.split()
    seq.append(b)


def a000001(N):
    if N > len(seq) + 1:
        print("Requires knowledge of group theory to implement, instead is using the 2047 terms provided by OEIS.")
        print("Please ensure the input is below that value.")
    return seq[N+1]