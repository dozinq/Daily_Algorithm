import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Node {
	private int x;
	private int y;
	
	public Node(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	int getX() {
		return this.x;
	}
	
	int getY() {
		return this.y;
	}
	
}

public class Main {
	/*
	 * 각 좌표를 돌면서 그것이 그림(1)인지 확인한다. true라면, 그림의 개수를 1 증가시킨다.
	 * 그리고 BFS를 진행해서 해당 그림의 넓이를 측정한다. 가장 길다면, maxWidth를 갱신한다. 
	 * */
	
	int n;
	int m;
	int[][] arr;
	boolean[][] visited;
	int[][] delta = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
	
	
	int[] bfs() {
		int paintCount = 0;
		int maxWidth = 0;
		Queue<Node> q = new LinkedList<Node>();
		visited = new boolean[n][m];
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[i][j] == 1 && !visited[i][j]) {
					q.offer(new Node(i, j));
					paintCount += 1;
					int thisWidth = 1;
					visited[i][j] = true;
					while (!q.isEmpty()) {
						Node node = q.poll();
						int x = node.getX();
						int y = node.getY();
						
						for (int d = 0; d < 4; d++) {
							int nx = x + delta[d][0];
							int ny = y + delta[d][1];
							if (0 <= nx && nx < n && 0 <= ny && ny < m) {
								if (arr[nx][ny] == 1 && !visited[nx][ny]) {
									thisWidth += 1;
									visited[nx][ny] = true;
									q.offer(new Node(nx, ny));
								}
							}
						}
					}
					if (maxWidth < thisWidth) maxWidth = thisWidth;
				}
			}
		}
		
		int[] ret = {paintCount, maxWidth}; 
		return ret;
	}
	
	void main() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		// n, m : 세로, 가로
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		// 배열 저장
		arr = new int[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int[] ans;
		ans = bfs();
		System.out.println(ans[0]);
		System.out.println(ans[1]);
		
	}
	
	public static void main(String[] args) throws IOException {
		new Main().main();
	}
}
