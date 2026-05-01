li = [1, 4, 4, 4, 5, 3]
n = 6

def test(li):
    count = 0

    for i in li:
        if i not in ar:
            ar.append(i)
        count += 1
    print(ar)
    print(count)
test(li)