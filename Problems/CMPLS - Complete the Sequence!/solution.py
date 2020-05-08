# method of differences for sequence evaluation

testcase = int(input())
testcases = dict()

for i in range(testcase):
    testcases[str(i)] = {
        'SC' : list(map(int, input().split(" "))),
        'seq' : list(map(int , input().split(" ")))
    }    
    
for i in range(testcase):
    S, C = list(map(int , testcases[str(i)]['SC']))
    
    polynomial = []
    polynomial.append(list(map(int , testcases[str(i)]['seq'])))
    
    if(S == 1):
        polynomial[0] = polynomial[0]*2
        S += 1
    
    poly = polynomial[0]
    D = 0
    while(True):
        diff = [poly[i] - poly[i - 1] for i in range(1, len(poly))]
        poly = diff
        polynomial.append(poly)
        D += 1
        
        if(all(i == diff[0] for i in poly)):
            break
    
    polynomial[D] += list(map(int , (str(polynomial[D][0])*C)))

    for i in range(D-1 , -1, -1):
        start = len(polynomial[i])-1
        for j in range(start , start+C):
            polynomial[i].append(polynomial[i][j] + polynomial[i+1][j])
            
    print(*polynomial[0][-C:])
