import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int C = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int[][] picture = new int[R][C];
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                picture[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        boolean edible = Boolean.TRUE;
        for (int i = 0; i < C; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = R-1; j >= 0; j--) {
                if (picture[j][i] != Integer.parseInt(st.nextToken())){
                    edible=Boolean.FALSE;
                    break;
                }
            }
        }
        if (edible){
            bw.write("|>___/|        /}\n" +
                    "| O < |       / }\n" +
                    "(==0==)------/ }\n" +
                    "| ^  _____    |\n" +
                    "|_|_/     ||__|");
            bw.flush();
        }
        else{
            bw.write("|>___/|     /}\n| O O |    / }\n( =0= )\"\"\"\"  \\\n| ^  ____    |\n|_|_/    ||__|");
            bw.flush();
        }
    }
}
