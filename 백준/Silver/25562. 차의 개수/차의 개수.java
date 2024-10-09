import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine().toString());
        StringBuilder sbmax = new StringBuilder("1");
        StringBuilder sbmin = new StringBuilder("1");
        int j=1;
        for (int i = 0; i < N-1; i++) {
            j+=Math.pow(2,i);
            sbmax.append(" "+j);
        }
        int k=1;
        for (int i = 1; i < N; i++) {
            k++;
            sbmin.append(" "+k);
        }
        bw.write(String.valueOf(N*(N-1)/2));
        bw.newLine();
        bw.write(sbmax.toString());
        bw.newLine();
        bw.write(String.valueOf(N-1));
        bw.newLine();
        bw.write(sbmin.toString());
        bw.newLine();
        bw.flush();
    }
}
