<h1>Algorithm</h1>
<h3>목차</h3>
<ol>
	<li>
		<a href="#bruteforce">완전탐색</a>
	</li>
</ol>

	💥개인적으로 공부하며, 개념을 정리하는 페이지입니다.

	📍Focus point : 
		1. 알고리즘이 동작할 때 쓰이는 자원은 무엇일까?
		2. 알고리즘을 언제 활용해야 할까?
		3. 시간복잡도의 계산은 어떻게 할까?
	
<h2 id="bruteforce">완전 탐색</h2>
<h4>영문명 : brute force search, exhaustive search</h4>
<h4> 모든 경우의 수를 계산해보고 해를 찾는 방법</h4>

- 보통 반복문을 사용하거나, 재귀적인 <i>dfs</i> 같은 방법으로 모든 경우의 수를 계산한다.

1. 알고리즘이 동작할 때 쓰이는 자원은 무엇일까?
	- 재귀 vs 반복문에따라 달라진다. 
		- 재귀는 함수를 반복해서 호출해오는 방법이기 때문에 메모리 `Call Stack`에 스택이 쌓인다.
		- 반복문의 경우에는 사용하는 변수에 따라 달라진다. 동적할당이 반복문 안에서 일어날 경우 할당된 메모리는 힙 영역에 저장된다. 또, 선언된 지역변수들은 스택에 저장된다. 
2. 알고리즘을 언제 활용해야 할까?
	- 효율이 안좋은 편이기 때문에 다른 알고리즘을 적용하기 어려워 <b><i>모든 경우의 수를 찾아봐야할 때</i></b>라고 생각한다.
3. 시간복잡도의 계산은 어떻게 할까?
	- 반복문은 반복문의 중첩 수 $x$에 따라.. $O(N^x)$가 되기도 하고, 재귀의 경우에는 한 함수에서 얼마나 호출하느냐에 따라 $O(x^N)$ 가 되기도 한다. $(x=1,2...)$

### Backtracking
### Dynamic Programming
### Greedy Algorithm
### conquer and divide
	복잡한 문제를 작은 문제로 쪼개서 푸는 방법
 
### sorting algorithm
	정렬 알고리즘
1. Bubble Sort
O($N^2$)
2. Merge Sort
## Data Structure
### stack, queue
시간 복잡도 : 쓰기 O(1), 읽기 O(N)
자료구조 FILO / FIFO

### Priority Queue

### Prefix Sum
	누적합

## Tree
### Union Find(Disjoint set)
### Minimum Spanning Tree
### Trie
### Topological Sort
### Segment Tree

## Graph Search
### BFS
### DFS

## Search Techinque
### Two Pointer
### binary search
	탐색시 반으로 잘라 범위를 줄여나가는 방법
시간복잡도 : O($logN$)

## Shortest Distance
### Dijkstra
### Floyd-warshall
### Bellman-Ford


