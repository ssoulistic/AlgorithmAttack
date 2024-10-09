import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        ArrayList<Integer> arr = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            arr.add(Integer.parseInt(st.nextToken()));
        }
        int[][] buses = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                buses[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int answer=0;
        int first=arr.get(0)-1;
        for (int i = 1; i < M; i++) {
            int second = arr.get(i)-1;
            answer+=buses[first][second];
            first = second;
        }
        bw.write(answer+"\n");
        bw.flush();

    }
}
