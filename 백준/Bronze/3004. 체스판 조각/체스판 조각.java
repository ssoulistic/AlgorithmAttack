import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.valueOf(br.readLine());
        int answer;
        if (N % 2 ==0){
            answer=(N/2+1)*(N/2+1);
        }
        else{
            answer=(N/2+2)*(N/2+1);
        }
        bw.write(String.valueOf(answer));
        bw.flush();
    }
}
