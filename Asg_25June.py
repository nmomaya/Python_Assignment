def push(l1,data):
    l1.append(data)

def pop(l1):
    return l1.pop()

def IsEmpty(l1):
    return l1 == []

def IsFull(l1):
    return len(l1) == 10

def pop(l1):
    return l1[-1]

def main():
    rollno = []
    push(rollno,1)
    push(rollno,2)
    push(rollno,3)
    print(rollno)
    print(pop(rollno))

if __name__ == '__main__':
    main()
