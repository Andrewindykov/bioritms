def is_isolate(t,i=0,j=0):
    if t[i][j]+t[i][j+1]+t[i+1][j]+t[i+1][j+1]<2:
        return True
    else:
        return False

def verify(t):
    # print(len(t))
    for i in range(len(t)-1):
        # print(t[i])
        for j in range(len(t[i])-1):
            # print(j)
            if not is_isolate(t,i,j):
                # print('returnfalse')
                return False
    # print('endoffunction verify')
    return True

t=[[0,0,0],
   [0,0,0],
   [0,1,0]]
print(verify(t))