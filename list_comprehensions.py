def run():
    # squares = []
    # for i in range(1,101):
    #     if i%3!=0:            
    #         squares.append(i**2)

    # print(squares)
    
    challenge = [i for i in range(1,1000) if i%36==0]
    print(challenge)

if __name__ == '__main__':
    run()