pre_encoded = {}

def rite(c):
    with open('pre_encoded.txt', 'r') as f:
        con = eval(f.read())
    con[name] = data
    with open('pre_encoded.txt', 'w') as g:
        g.write(repr(con))

name = input()
data = []
while input() != 'bpm':
    unit = []
    for i in range(2):
        unit.append(int(input()))
    data.append(unit)
data.append(int(input()))
print(data)
if input() == 'Y':
    rite(data)

