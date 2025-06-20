import java.util.Scanner;
public class ReverseWords {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] w = sc.nextLine().split(" ");
        for(String s : w)
            System.out.print(new StringBuilder(s).reverse() + " ");
    }
}
