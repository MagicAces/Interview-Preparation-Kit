import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        // Scanner s = new Scanner(System.in);
        Scanner stdin = new Scanner(new BufferedInputStream(System.in));
        while (stdin.hasNext()) {
        String input = stdin.nextLine();
    
        String[] options = input.split(";");
        String output = "";
        
        if(options[0].equals("S")) {
            switch(options[1]) {
                case "M":
                case "V":
                    String value = options[2];
                    for(char i: value.toCharArray()) {
                        if(Character.isUpperCase(i))
                            output += " ";
                        output += Character.toLowerCase(i);
                    }
                    output = output.replace("()", "");
                    break;
                case "C":
                    String newStr = options[2].substring(0, 1).toUpperCase() + options[2].substring(1);
                    for(char i: newStr.toCharArray()) {
                        if(Character.isUpperCase(i))
                            output += " ";
                        output += Character.toLowerCase(i);
                    }
                    output = output.substring(1);
                    break;
            }
        } else if(options[0].equals("C")) {
            String[] words = options[2].split(" ");
            switch(options[1]) {
                case "M":
                    for(String word: words) {
                        output += word.substring(0, 1).toUpperCase() + word.substring(1);
                    } 
                    
                    output = output.substring(0, 1).toLowerCase() + output.substring(1) + "()";
                    break;
                case "V":
                    for(String word: words) {
                        output += word.substring(0, 1).toUpperCase() + word.substring(1);
                    } 
                    output = output.substring(0, 1).toLowerCase() + output.substring(1);
                    break; 
                case "C":
                    for(String word: words) {
                        output += word.substring(0, 1).toUpperCase() + word.substring(1);
                    }
                    break;
            }
            
        }
        
        System.out.println(output);
        }
    }
}


