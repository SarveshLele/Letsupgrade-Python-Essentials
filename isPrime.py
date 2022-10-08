def isPrime(numb):
    flag = -1
    if numb > 1:
        for x in range(2,numb):
            if numb%x == 0:
                flag = 1
    
    if flag == 1:
        print("Number is not prime")
    else:
        print("Number is Prime")

isPrime(5)