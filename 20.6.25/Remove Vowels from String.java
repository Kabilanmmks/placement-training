import java.util.Scanner;
public class RemoveVowels {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        s = s.replaceAll("[aeiouAEIOU]", "");
        System.out.println(s);
    }
}
