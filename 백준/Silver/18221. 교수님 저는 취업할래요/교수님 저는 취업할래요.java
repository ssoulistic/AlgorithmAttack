import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine().toString());
        int[][] graph = new int[N][N];
        int[] professor = new int[2];
        int[] seongkyu = new int[2];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 5) {
                    professor[0] = i;
                    professor[1] = j;
                } else if (graph[i][j] == 2) {
                    seongkyu[0] = i;
                    seongkyu[1] = j;
                }
            }
        }
        int students = 0;
        int startRow, startCol, endRow, endCol;
        startRow = Math.min(professor[0], seongkyu[0]);
        startCol = Math.min(professor[1], seongkyu[1]);
        endRow = Math.max(professor[0], seongkyu[0]);
        endCol = Math.max(professor[1], seongkyu[1]);

        for (int i = startRow; i < endRow + 1; i++) {
            for (int j = startCol; j < endCol + 1; j++) {
                if (graph[i][j] == 1) {
                    students += 1;
                }
            }
        }
        if (students >= 3 & (Math.pow(professor[0]-seongkyu[0],2)+Math.pow(professor[1]-seongkyu[1],2)>=25)) {
            bw.write("1");
            bw.flush();
        } else {
            bw.write("0");
            bw.flush();
        }


    }
}
