import java.util.Scanner;
public class CapitalizeWords {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] w = sc.nextLine().split(" ");
        for(String s : w)
            System.out.print(Character.toUpperCase(s.charAt(0)) + s.substring(1) + " ");
    }
}
