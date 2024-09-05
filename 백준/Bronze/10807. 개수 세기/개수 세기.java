import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	void main() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		// input data 확인 안 하고 설계하다보니, 수정사항 발생.
		// 맞긴 했지만, 난해하고 비효율적인 코드가 되어버렸다. 문제 요구대로 다시 설계해보자.
		int[] arr = new int[201];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			int tmp = Integer.parseInt(st.nextToken());
			arr[tmp + 100] += 1;
		}
		
		int v = Integer.parseInt(br.readLine());
		System.out.println(arr[v + 100]);
		
	}
	
	public static void main(String[] args) throws IOException {
		new Main().main();
	}

}