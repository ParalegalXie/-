# 正向
for i in range(0,10):
    for j in range(1,i+1):
        print(str(i) + "*" + str(j) + "=" + str(i*j), end = "  ")
    print() 

# 一正一逆
for i in range(9,0,-1):
    for j in range(1,i+1):
        print(str(i) + "*" + str(j) + "=" + str(i*j), end = "  ")
    print() 

# 双逆向
for i in range(9,0,-1):
    for j in range(i,0,-1):
        print(str(i) + "*" + str(j) + "=" + str(i*j), end = "  ")
    print() 
