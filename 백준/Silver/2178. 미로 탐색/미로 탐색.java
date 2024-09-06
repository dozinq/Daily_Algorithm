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
	
	public int getX() {
		return this.x;
	}
	
	public int getY() {
		return this.y;
	}
}

public class Main {
	
	void main() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		// 배열 생성
		int[][] arr = new int[N][M]; 
		for (int i = 0; i < N; i++) {
			String tmpStr = br.readLine();
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(tmpStr.substring(j, j+1));
			}
		}
		
		// BFS
		int[][] delta = { {0, -1}, {1, 0}, {0, 1}, {-1, 0} };
		int[][] visited = new int[N][M];
		Queue<Node> q = new LinkedList<Node>();
		q.offer(new Node(0, 0));
		visited[0][0] = 1;
		
		while(!q.isEmpty()) {
			Node node = q.poll();
			int x = node.getX();
			int y = node.getY();
			
			for (int d = 0; d < 4; d++) {
				int nx = x + delta[d][0];
				int ny = y + delta[d][1];
				
				if (!(0 <= nx && nx < N && 0 <= ny && ny < M)) {
					continue;
				}
				
				if (arr[nx][ny] == 1 && visited[nx][ny] == 0) {
					q.offer(new Node(nx, ny));
					visited[nx][ny] = visited[x][y] + 1;
				}
			}
		}
		System.out.println(visited[N-1][M-1]);
	}
	
	public static void main(String[] args) throws IOException {
		new Main().main();
	}
}
