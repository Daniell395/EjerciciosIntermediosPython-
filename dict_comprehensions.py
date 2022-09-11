from calendar import c


def run():
    # cube = {}
    # for i in range(1,101):
    #     if i%3!=0:
    #         cube[i] = i**3
    # print(cube)        

    challenge={i:round(i**0.5,2) for i in range(1,1000)}
    print(challenge)

if __name__== '__main__':
    run()