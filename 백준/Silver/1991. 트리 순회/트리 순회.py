import sys
input=sys.stdin.readline
N=int(input())
graph={}
# 전위 순회 root left right
# 중위 순회 left root right
# 후위 순회 left right root

for _ in range(N):
    root,left,right=input().split()
    graph[root]=[left,right]

r1,r2,r3=[],[],[]
def preorder(start):
    l,r=graph[start]
    
    r1.append(start)
    
    if l!=".":
        preorder(l)
    if r!=".":
        preorder(r)

def inorder(start):
    l,r=graph[start]

    if l!=".":
        inorder(l)
    r2.append(start)
    if r!=".":
        inorder(r)

def postorder(start):
    l,r=graph[start]
    if l!=".":
        postorder(l)
    if r!=".":
        postorder(r)
    r3.append(start)

preorder("A")
print("".join(r1))

inorder("A")
print("".join(r2))

postorder("A")
print("".join(r3))