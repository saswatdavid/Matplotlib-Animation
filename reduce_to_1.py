import math
import pandas as pd
import matplotlib.pyplot as plt

def solution(n):
    # Your code here
    n = int(n)
    count = 0
    while n!= 1:
        if n%2!=0:
            if (math.log((n+1),2))%1==0:
                n = n+1
                count += 1
            else:
                n = n-1
                count += 1
        else:
            n = n/2
            count += 1
    return count

def solution_2(n):
    n = int(n)
    count = 0
    while n > 1:
        if n % 2 == 0:
           n = n/2
        else:
            if (n == 3 or n % 4 == 1):
                n = (n - 1)
            else: 
                n = (n + 1)
        count += 1
    return count

rows=[]
for i in range(1,20):
    rows.append([i, solution(i)])

df = pd.DataFrame(rows, columns=["A", "B"])

df.plot(x="A", y="B")
plt.show()