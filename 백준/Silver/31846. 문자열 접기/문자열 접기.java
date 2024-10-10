import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        String sb = br.readLine();
        int Q = Integer.parseInt(br.readLine());
        for (int i = 0; i < Q; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            char[] subString = new char[end-start+1];
            sb.getChars(start - 1, end, subString, 0);
            int countMax = 0;
            for (int j = 0; j<subString.length;j++) {
                int count = 0;
                for (int k = 0; k <= j; k++) {
                    if (2*j+1-k<end-start+1 && subString[k] == subString[2*j+1-k]) {
                        count++;
                    }
                }
                if (count > countMax) {
                    countMax = count;
                }
            }
            bw.write(String.valueOf(countMax));
            bw.newLine();
        }
    bw.flush();
    }
}
