def troj(riadok: int):
    for i in range(riadok):
        for a in range(riadok-i-1):
            print(" ", end='')
        for b in range(2*i+1):
            print("x", end='')
        for a in range(riadok-i-1):
            print(" ", end='')
        print('')


troj(5)
