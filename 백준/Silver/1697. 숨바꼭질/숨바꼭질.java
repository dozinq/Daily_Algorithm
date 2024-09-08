import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	int N;
	int K;
	int[] visited = new int[100001];
	Queue<Integer> q = new LinkedList<Integer>();
	int ans;
	
	int bfs() {
		q.offer(N);
		while(!q.isEmpty()) {
			int x = q.poll();
			if (x == K) {
				ans = visited[x];
				break;
			}
			for (int i = 0; i < 3; i++) {
				int nx;
				if (i == 1) {
					nx = x - 1;
				}else if (i == 2) {
					nx = x + 1;
				}else {
					nx = 2 * x;
				}
				// 범위 체크 및 초기 N의 지점에 다시 가서는 안 됨.
				// 초기 N의 지점. 즉, visited[N] == 0이기에, 이를 이용해서 계산해주기 위해.
				if (0 <= nx && nx < 100001 && nx != N) {
					if (visited[nx] == 0) {
						visited[nx] = visited[x] + 1;
						q.offer(nx);
					}
				}
			}
		}
		return ans;
	}
	
	void main() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		System.out.println(bfs());
	}
	
	public static void main(String[] args) throws IOException {
		new Main().main();
	}
	
}