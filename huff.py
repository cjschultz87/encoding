import sys

sierra = sys.argv[1]

alpha = []
skip = []

i = 0
i_a = 0
while i < len(sierra):
    if len(skip) > 0:
        bravo = True
        
        while bravo == True:
            bravo_1 = True
            
            for s in skip:
                if i == s[0]:
                    i += s[1]
                    bravo_1 = False
            if bravo_1 == True:
                bravo = False
    
    if i == len(sierra):
        break
    
    alpha.append([sierra[i],0])
    
    i_s_1 = i + 1
    
    while i_s_1 < len(sierra):
        if sierra[i_s_1] == alpha[i_a][0]:
            alpha[i_a][1] += 1
            skip.append([i_s_1,1])
        i_s_1 += 1
    if len(skip) > 1:
        i_s_1 = i_a + 1
        while i_s_1 < len(skip):
            if skip[i_s_1][0] == skip[i_s_1 - 1][0]:
                skip[i_s_1 - 1][1] += skip[i_s_1][1]
                skip.pop(i_s_1)
            else:
                i_s_1 += 1
    i_a += 1
    i += 1    

def sort_a(alpha,index):
    if len(alpha) > 1 and type(alpha) == type([]):
        for a in alpha:
            if type(a) != type([]) or len(a) != 2:
                return []
            else:
                pass
                
    i = 0
    
    while i < len(alpha) - 1:
        i_1 = i + 1
        a = alpha[i]
        while i_1 < len(alpha):
            if a[index] > alpha[i_1][index]:
                alpha[i] = alpha[i_1]
                alpha[i_1] = a
                a = alpha[i]
            i_1 += 1
        i += 1
        
    return alpha
    
alpha_prime = []

for a in alpha:
    alpha_prime.append(a)
    
alpha_prime = sort_a(alpha_prime,1)
    
while len(alpha_prime) > 1:
    a_prime = [[alpha_prime[0],alpha_prime[1]],0]
    a_prime[1] = alpha_prime[0][1] + alpha_prime[1][1]
    
    alpha_prime.insert(0,a_prime)
    
    alpha_prime.pop(1)
    alpha_prime.pop(1)
    
    alpha_prime = sort_a(alpha_prime,1)
    
alpha_prime = alpha_prime[0]

alpha = sort_a(alpha,1)[::-1]

node = ["[0]","[1]"]

i = 0

while i < len(alpha):

    n = 0
    
    branch = "alpha_prime" + node[n]
    
    encoding = ""
    
    i_b = 0
    
    while type(eval(branch)) != type(alpha[0][0]):
        boole = True
        
        if i > 0:
            lima = len(alpha[i-1][1])
            
            
        
            if not (type(eval(branch)[1]) == type(5)) and len(encoding) + 1 == lima:
                n = (int(alpha[i-1][1][lima - 1]) + 1) % 2
                
            elif type(eval(branch)[1]) == type(5):
                boole = False
                n = 0
                
            elif type(eval(branch)[0]) == type(alpha[0][0]):
                n = 0
            
            elif i_b < len(alpha[i-1][1]):
                n = int(alpha[i-1][1][i_b])
                
            else:
                n = 1
                
                
        else:
            if type(eval(branch)[0]) == type(alpha[i][0]):
                n = 0
                boole = False
                
            elif type(eval(branch)[0][0]) == type(alpha[i][0]):
                n = 0
                
            else:
                n = 1
        
        branch += node[n]
        
        if boole == True:
            encoding += str(n)
            
            i_b += 1
        
        boole = True
    
    encoding = encoding[0:len(encoding)]
    
    alpha[i][1] = encoding
    
    i += 1
    
print(alpha)

sierra_enc = ""

for s in sierra:
    for a in alpha:
        if s == a[0]:
            sierra_enc += a[1]
            break

print(sierra)
print(sierra_enc)