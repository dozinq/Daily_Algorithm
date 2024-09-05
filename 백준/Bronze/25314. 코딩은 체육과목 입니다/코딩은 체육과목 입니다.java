import java.io.*;

public class Main {
	
	void main() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		for (int i = 4; i <= N; i += 4) {
			sb.append("long ");
		}
		sb.append("int");
		System.out.println(sb);
	}
	
	public static void main(String[] args) throws IOException {
		new Main().main();
	}
}