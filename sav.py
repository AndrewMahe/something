import time

line = [((0, 0), (3, 0))]
score = [25,0]

rp_lt = [line, score]


def save_writing(rp_lt,line, score):
    date = time.strftime("%d_%m-%H_%M_%S")
    monfichier = open((date)+'.txt', 'w')

    for x in rp_lt:
        x = str(x)
        monfichier.write(x)
        monfichier.write("\n")

    monfichier.close

    print("Data got success fully saved")


def save_reading():
    monfichier = open('save.txt', 'r')

    line = monfichier.readline()
    score = monfichier.readline()

    monfichier.close

    return line,score




nt = str(input("w or r"))

if nt=="w":
    save_writing(rp_lt,line, score)

if nt=="r":
    line, score = save_reading()
    print(line,score)

