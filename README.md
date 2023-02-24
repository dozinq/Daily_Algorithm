# : 🙂 Growth Process
> I solved algorithm problems every day and recorded them here.

</br>

---

</br>

#### 알고리즘 문제 풀이를 통해 깨달은 점 혹은 잊기 쉬운 점에 대한 개인적인 정리.



> - Unicode value return - BOJ15829
>
>   - ord()는 숫자에 대응하는 유니코드 숫자를 반환한다. 사용할 때마다 print()로 출력 후 확인하여 사용할 수 있도록 하자.
>
>     ```python
>     ord('a') == 97
>     ord('z') == 122
>     ```



> - Dictionary - BOJ1620
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



> - 백 트래킹
>   - 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법. 최적화 문제와 결정 문제를 푸는 방법이다. (ex. 순열과 조합에 대한 구현)
> - 순열과 조합에 관한 수학적인 정리 - BOJ9095, BOJ2407
>   - 관련한 사이트 링크 : *https://coding-factory.tistory.com/606*



> - Binary Search - BOJ2805
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



> - Copy, Deepcopy
>   - 리스트를 '슬라이싱[:]' 하거나 'copy()' 메소드를 사용하여 1차원 배열을 복제할 수 있다.
>   - copy 라이브러리를 import하고 'deepcopy()' 메소드를 사용하여 2차원 배열을 복제할 수 있다.



> - Dijkstra - BOJ1916
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