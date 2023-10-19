# : 🙂 Growth Process
> I solved algorithm problems every day and recorded them here.

</br>

---

</br>

#### 알고리즘 문제 풀이를 통해 깨달은 점 혹은 잊기 쉬운 점에 대한 개인적인 정리.

1. [Unicode value return](#idx-1)
2. [Dictionary](#idx-2)
3. [Backtracking](#idx-3)
4. [Binary Search](#idx-4)
5. [Copy, Deepcopy](#idx-5)
6. [Dijkstra's Algorithm](#idx-6)
7. [heapq](#idx-7)
8. [Kruskal's Algorithm](#idx-8)
9. [Union-Find](#idx-9)
10. [Topological Sort](#idx-10)



<br>

> - Unicode value return - BOJ15829 <a id="idx-1"></a>
>
>   - ord()는 숫자에 대응하는 유니코드 숫자를 반환한다. 사용할 때마다 print()로 출력 후 확인하여 사용할 수 있도록 하자.
>
>     ```python
>     ord('a') == 97
>     ord('z') == 122
>     ```

</br>

> - Dictionary - BOJ1620<a id="idx-2"></a>
>
>   - key를 이용해, value를 찾아낼 수 있다. 리스트와 마찬가지로 dict[key]를 입력한다면 value값을 반환하지만, value값이 존재하지 않을 경우를 대비해, dict.get(key)를 입력하여 오류를 방지하는 것이 낫다.
>
>   - value값을 이용하여 key를 찾으려고 한다면 효율적인 두가지 방법이 있다.
>
>     1. ```python
>        # dict라는 이름의 딕셔너리 객체가 존재한다면,
>        dict_reverse = {}
>                      
>        for idx in range(len(dict) + 1):
>            dict_reverse[dict.get(idx)] = idx
>        ```
>
>     2. ```python
>        # 애초에 dict를 입력받아 저장할 때, 같이 저장하는 방법
>        dict = {}
>        dict_reverse = {}
>        for idx in range(1, N+1):
>            tmp = sys.stdin.readline().strip()
>            dict[idx] = tmp
>            dict_reverse[tmp] = idx
>        ```

</br>

> - Backtracking<a id="idx-3"></a>
>   - 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법. 최적화 문제와 결정 문제를 푸는 방법이다. (ex. 순열과 조합에 대한 구현)
>   - 순열과 조합에 관한 수학적인 정리 - BOJ9095, BOJ2407
>     - 관련한 사이트 링크 : *https://coding-factory.tistory.com/606*

</br>

> - Binary Search - BOJ2805<a id="idx-4"></a>
>
>   - O(logN)
>
>     ```python
>     N, M = map(int, input().split())
>     data = list(map(int, input().split()))
>     start, end = 1, sum(data)
>             
>     while start <= end:
>         mid = (start + end) // 2
>         cnt = 0
>         for i in data:
>             if i > mid:
>                 cnt += i - mid
>         if cnt >= M:
>             start = mid + 1
>         else:
>             end = mid - 1
>             
>     print(end)
>     ```

</br>

> - Copy, Deepcopy<a id="idx-5"></a>
>   - 리스트를 '슬라이싱[:]' 하거나 'copy()' 메소드를 사용하여 1차원 배열을 복제할 수 있다.
>   - copy 라이브러리를 import하고 'deepcopy()' 메소드를 사용하여 2차원 배열을 복제할 수 있다.

</br>

> - Dijkstra's Algorithm - BOJ1916<a id="idx-6"></a>
>
>   - 최단 경로 탐색 알고리즘으로 음의 간선을 포함하지 않는다면 사용하기 적합하다.
>
>     1. 출발 노드를 설정한 후, 출발노드의 경로 배열을 최초 배열로 사용한다.
>
>     2. 그 후, 노드로부터 가장 비용이 적은 노드를 선택하여 방문하도록 한다.
>
>     3. 다음 노드부터는 최초 배열로 부터 저장된 정보와 비교하며 최소 비용을 갱신한다.
>
>     4. 최소 비용 노드 방문 후 정보 갱신을 반복하여, 모든 노드를 방문하도록 한다.
>
>   - heapq를 사용한 Python 코드
>
>     ```python
>     import heapq  # 우선순위 큐 구현을 위함
>             
>     # 입력
>     N = int(input())  # node 개수
>     M = int(input())  # edge 개수
>     graph = [[] for _ in range(N+1)]
>     for _ in range(M):
>         a, b, c = map(int, input().split())
>         graph[a].append((b, c))  # 도착지, 가중치
>     start, end = map(int, input().split())  # 출발지 목적지
>             
>     # 다익스트라 최적경로 탐색
>     def dijkstra(graph, start):
>         distances = [int(1e9)] * (N+1)  # 처음 초기값은 무한대
>         distances[start] = 0  # 시작 노드까지의 거리는 0
>         queue = []
>         heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작
>             
>         while queue:  # queue에 남아있는 노드가 없을 때까지 탐색
>             dist, node = heapq.heappop(queue)  # 탐색할 노드, 거리
>             
>             # 기존 최단거리보다 멀다면 무시
>             if distances[node] < dist:
>                 continue
>             
>             # 노드와 연결된 인접노드 탐색
>             for next_node, next_dist in graph[node]:
>                 distance = dist + next_dist  # 인접노드까지의 거리
>                 if distance < distances[next_node]:  # 기존 거리 보다 짧으면 갱신
>                     distances[next_node] = distance
>                     heapq.heappush(queue, [distance, next_node])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
>         return distances
>             
>     dist_start = dijkstra(graph, start)
>     print(dist_start[end])
>     ```

</br>

> - heapq<a id="idx-7"></a>
>
>   - Python의 heapq
>
>     - 0부터 K까지의 모든 원소가 항상 자식 원소들(2k+1, 2k+2)보다 작거나 같은 '최소 힙'의 형태로 정렬된다.
>
>     ```python
>     import heapq
>             
>     # 힙 생성.
>     heap = []
>     # 힙에 item 추가.
>     heapq.heappush(heap, 50)
>     # 힙에서 가장 작은 원소를 반환. (-> 비어있는 경우 IndexError)
>     tmp = heapq.heappop(heap)
>             
>     # 이미 생성된 리스트를 힙 자료형으로 변환.
>     mylst = [50, 10, 20]
>     heapq.heapify(mylst)
>             
>     # [10, 50, 20]의 최소힙 형태로 변환.
>     print(mylst)
>     ```
>
>     - 관련한 사이트 링크 : *https://littlefoxdiary.tistory.com/3*

</br>

> - Kruskal's Algorithm - BOJ1197<a id="idx-8"></a>
>
>   ```python
>   # 오름차순으로 정렬되어 있는 data 배열을 활용한다.
>   def kruskal(cnt):
>       ans = 0
>       for node_1, node_2, val in data:
>           if find(node_1) != find(node_2):
>               union(node_1, node_2)
>               ans += val
>               cnt -= 1
>           if cnt == 0:
>               return ans
>   ```
>
>   - 그리디 알고리즘의 일종으로, 그래프 간선들을 가중치의 오름차순으로 정렬하고, 사이클을 형성하지 않는 선에서 정렬된 순서대로 간선을 선택한다.
>   - 최소 신장  트리(Minimum Spanning Tree, MST)를 구하기 위한 알고리즘으로 그의 예시
>     - 여러 개의 네트워크 지점들이 있는데, 모든 지점들을 유선으로 연결화되 연결선의 총 길이가 최소가 되어야 하는 문제
>     - 도시들을 모두 연결하되, 연결하는 도로의 길이의 합이 최소가 되어야 하는 문제
>   - 관련한 사이트 링크 : *https://chanhuiseok.github.io/posts/algo-33/*

</br>

> - Union-Find - BOJ20040<a id="idx-9"></a>
>   
>   ```python
>   def find(x):
>       if parent[x] != x:
>           return find(parent[x])
>       return x
>   
>   def union(a, b):
>       a = find(a)
>       b = find(b)
>       if a < b:
>           parent[b] = a
>       else:
>           parent[a] = b
>   ```
>   
>   - Disjoint Set(서로소 집합)을 표현하는 자료구조
>   - 서로 다른 두 집합을 병합하는 Union 연산
>   - 집합 원소가 어떤 집합에 속해있는지 찾는 Find 연산
>   - 이를 이용한다면, 동일한 부모 노드를 가지고 있는 자식 노드끼리는 사이클을 형성하게 되므로 이을 수 없다는 것을 알 수 있다.
>   
>   - 관련한 사이트 링크 : *https://0x15.tistory.com/34*

</br>

> - Topological Sort - BOJ2252, BOJ1005<a id="idx-10"></a>
>
>   ```python
>   import sys
>   from collections import deque
>   
>   n, m = map(int, sys.stdin.readline().split())
>   
>   graph = [[] for _ in range(n+1)]
>   inDegree = [0 for _ in range(n+1)]
>   queue = deque()
>   ans = []
>   
>   for i in range(m):
>       a, b = map(int, sys.stdin.readline().split())
>       graph[a].append(b)
>       inDegree[b] += 1
>   
>   # 가장 위에 아무것도 없는 요소를 추가한다.
>   for i in range(1, n+1):
>       if inDegree[i] == 0:
>           queue.append(i)
>   
>   # 큐를 돌면서 그 다음 순위의 노드를 저장할 수 있도록 한다.
>   while queue:
>       tmp = queue.popleft()
>       ans.append(tmp)
>       for i in graph[tmp]:
>           inDegree[i] -= 1
>           if inDegree[i] == 0:
>               queue.append(i)
>   
>   print(*ans)
>   ```
>
>   - '위상 정렬'이라고 하며, 비순환 방향 그래프에서 정점을 선형으로 정렬하게 된다.
>   - 우선도를 체크할 수 있도록 하여, 결과적으로 순위의 순서대로 정렬할 수 있게 한다.