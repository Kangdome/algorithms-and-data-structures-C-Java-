


N = 3

def f(N):   
    if N == 1:       
        return 1
        print ("returned one")
    else:       
        return f(N-1) *  N
        print ("returned Else")
#f(N)
print (f(N))


