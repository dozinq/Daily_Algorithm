# : 🙂 Growth Process
> I solved algorithm problems every day and recorded them here.



---

#### 깨달은 점 혹은 잊기 쉬운 점에 대한 개인적인 정리.



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
>   - key를 이용해, value로 찾아낼 수 있다. 리스트와 마찬가지로 dict[key]를 입력한다면 value값을 반환하지만, value값이 존재하지 않을 경우를 대비해, dict.get(key)를 입력하여 오류를 방지하는 것이 낫다.
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





