ar_count = int(input().strip())
def simpleArraySum():
    ar = []
    for i in range(1,ar_count+1):
        ar.append(i)
    total = 0
    for i in ar:
        total += i
    return total
print(simpleArraySum())