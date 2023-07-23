import random

id=(input('Enter your student id: '))

min_max=input('Minimum and Maximum value for the range of negative HP:')

min_max=min_max.split(' ')
low=int(min_max[0])
high=int(min_max[1])

total_turns=str(int(id[0])*2)
bullets=id[2]

print(f"1. Depth and Branches ratio is {total_turns}:{bullets}")


terminal=[]
bullets=int(bullets)
total_turns=int(total_turns)
n=(bullets)**(total_turns)

for i in range (n):
    a=random.randint(low,high)
    terminal.append(a)

print(f"2, Terminal States(Leaf Nodes) are {terminal}")

initial_hp=id[-2:]
initial_hp=initial_hp[::-1]
initial_hp=int(initial_hp)

count=0
leaf=0
def minimax(position, depth, alpha, beta, maximizingPlayer, count=0, leaf=0):
    if depth==0 and count==0:
        leaf+=1
        count+=1
        return (terminal[position],count,leaf)
    if depth==0 and count!=0:
        leaf+=1
        position=count
        count+=1
        return (terminal[position],count,leaf)
    if maximizingPlayer:

        maxEval=-10000

        for i in range (bullets):
            eval=minimax(i, depth-1,alpha, beta, False,count,leaf)
            leaf=eval[2]
            count=eval[1]
            eval=eval[0]
            maxEval=max(maxEval,eval)
            alpha= max(alpha, eval)
            if alpha>=beta:
                count=count+bullets-1
                break
        return (maxEval,count,leaf)

    else:
        minEval=+10000
        for i in range (bullets):
            eval=minimax(i,depth-1,alpha,beta,True,count,leaf)
            leaf = eval[2]
            count = eval[1]
            eval = eval[0]
            minEval=min(minEval,eval)
            beta=min(beta,eval)
            if alpha>=beta:
                count=count+bullets-1
                break
        return (minEval,count,leaf)


a=minimax(0,total_turns,-10000,+10000,True)

print(f"3. Left life(HP) of the defender after maximum damage caused by the attacker is {initial_hp-a[0]}")
print(f"4. After Alpha-Beta Pruning Leaf Node Comparisons {a[2]}")
