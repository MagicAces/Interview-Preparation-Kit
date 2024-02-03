import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'timeConversion' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    
     public static String timeConversion(String s) {
    // Write your code here
        String result = "";
        String hour = s.substring(0, 2);
        String minute = s.substring(3, 5);
        String second = s.substring(6, 8);
        String[] terms = s.split(":");
        
        if(s.toUpperCase().contains("AM")) {
            if(hour.equals("12")) {
                result = "00:" + minute + ":" + second;
            } else {
                result = hour + ":" + minute + ":" + second;
            }
        } else {
            if(hour.equals("12")) {
                result = hour + ":" + minute +  ":" + second;
            } else {
                 result = Integer.toString((
                            Integer.parseInt(hour) + 12)) 
                            + ":" + minute + ":" + second;
            }   
        }
        return result;
        
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        String result = Result.timeConversion(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
