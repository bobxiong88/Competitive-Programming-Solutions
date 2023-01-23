n = int(input())

for sets in range(n):
    ns = int(input())
    nv = int(input())
    no = int(input())
    subjects = []
    verbs = []
    objects = []
    for i in range(ns):
        subjects.append(input())
    for i in range(nv):
        verbs.append(input())
    for i in range(no):
        objects.append(input())

    for s in range(ns):
        for v in range(nv):
            for o in range(no):
                print(subjects[s],verbs[v],objects[o]+".")