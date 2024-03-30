from collections import deque
def solution(begin, target, words):
    visited={}
    for w in words:
        visited[w]=0
    visited[target]=0
    visited[begin]=1

    def bfs(start):
        que=deque()
        que.append(start)
        while que:
            word=que.popleft()
            for next_word in words:
                if visited[next_word]==0 or visited[next_word]>visited[word]+1:
                    diff=0
                    for i in range(len(next_word)):
                        if word[i]!=next_word[i]:
                            diff+=1
                    if diff==1:
                        if visited[next_word]>visited[word]+1:
                            visited[next_word]=visited[word]+1
                            que.append(next_word)
                        elif visited[next_word]==0:
                            visited[next_word]=visited[word]+1
                            que.append(next_word)
        return
    
    bfs(begin)
    
    if visited[target]:
        return visited[target]-1
    else:
        return 0