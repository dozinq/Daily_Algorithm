import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	int[] data;
	int fibRet = 0;
	
	int fib(int n) {
		if (n == 1 || n == 2) {
			fibRet++;
			return 1;
		}
		return (fib(n-1) + fib(n-2));
	}
	
	int fibonacci(int n) {
		data = new int[n+1];
		data[1] = 1;
		data[2] = 1;
		int ret = 0;
		for (int i = 3; i < n+1; i++) {
			data[i] = data[i-1] + data[i-2];
			ret++;
		}
		return ret;
	}
	
	void main() throws IOException {
		int n = Integer.parseInt(br.readLine());
		
		fib(n);
		System.out.println(fibRet + " " + fibonacci(n));
	}
	
	public static void main(String[] args) throws IOException {
		new Main().main();
	}

}
