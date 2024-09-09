import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

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
	
	int N;
	char[][] arr;
	boolean[][] visited;
	int[][] delta = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
	
	// 적록색약이 아닌 사람 기준 BFS
	int bfs() {
		int areaCount = 0;
		Queue<Node> q = new LinkedList<Node>();
		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					visited[i][j] = true;
					q.offer(new Node(i, j));
					areaCount += 1;
					while (!q.isEmpty()) {
						Node node = q.poll();
						int x = node.getX();
						int y = node.getY();
						for (int d = 0; d < 4; d++) {
							int nx = x + delta[d][0];
							int ny = y + delta[d][1];
							if (0 <= nx && nx < N && 0 <= ny && ny < N) {
								if (arr[x][y] == arr[nx][ny] && !visited[nx][ny]) {
									visited[nx][ny] = true;
									q.offer(new Node(nx, ny));		
								}
							}
						}
					}
				}
			}
		}
		return areaCount;
	}
	
	// 적록색약인 사람 기준 BFS
	int bfsV2() {
		int areaCount = 0;
		Queue<Node> q = new LinkedList<Node>();
		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					visited[i][j] = true;
					q.offer(new Node(i, j));
					areaCount += 1;
					while (!q.isEmpty()) {
						Node node = q.poll();
						int x = node.getX();
						int y = node.getY();
						for (int d = 0; d < 4; d++) {
							int nx = x + delta[d][0];
							int ny = y + delta[d][1];
							if (0 <= nx && nx < N && 0 <= ny && ny < N) {
								if (arr[x][y] == 'B') {
									if (arr[nx][ny] == 'B' && !visited[nx][ny]) {
										visited[nx][ny] = true;
										q.offer(new Node(nx, ny));
									}
								}
								else if (arr[nx][ny] != 'B' && !visited[nx][ny]) {
									visited[nx][ny] = true;
									q.offer(new Node(nx, ny));		
								}
							}
						}
					}
				}
			}
		}
		return areaCount;
	}
	
	void main() throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new char[N][N];
		for(int i = 0; i < N; i++) {
			String tmpStr = br.readLine();
			for (int j = 0; j < N; j++) {
				char tmpChar = tmpStr.charAt(j);
				arr[i][j] = tmpChar;
			}
		}
		System.out.println(bfs() + " " + bfsV2());
	}
	
	public static void main(String[] args) throws IOException {
		new Main().main();
	}

}
