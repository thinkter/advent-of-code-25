def q1_1():
    from collections import deque
    with open("input1.txt", "r", encoding="utf-8") as f:
        data = f.read()
        ins = data.splitlines()
        print(ins)
        # shit starts at 50 
        c = 0
        i = 50 
        d = deque(range(0, 100), maxlen=100)
        d.rotate(50) #shit gotta start at fitty
        #rotate( pos: right, neg: left)
        for line in ins:
            if line is not "":
                #print(line[0])
                dir = line[0]
                num = int(line[1:])

                if dir == "L":
                    d.rotate(-num)
                elif dir == "R":
                    d.rotate(num)
                if(d[0] == 0):
                    c = c+1
    print(d)
    print("\n\n")
    print(c) 


def q1_2():
    from collections import deque
    with open("input1.txt", "r", encoding="utf-8") as f:
        data = f.read()
        ins = data.splitlines()
        print(ins)
        # shit starts at 50 
        c = 0
        i = 50 
        d = deque(range(0, 100), maxlen=100)
        d.rotate(50) #shit gotta start at fitty
        #rotate( pos: right, neg: left)
        for line in ins:
            if line is not "":
                #print(line[0])
                dir = line[0]
                num = int(line[1:])
                if dir == "L":
                    for i in range(0 , num):
                        d.rotate(-1)
                        if(d[0] == 0):
                            c = c + 1
                elif dir == "R":
                    for i in range(0 , num):
                        d.rotate(1)
                        if(d[0] == 0):
                            c = c + 1
    print(d)
    print("\n\n")
    print(c) 


if __name__ == "__main__":
    #q1_1()
    q1_2()
