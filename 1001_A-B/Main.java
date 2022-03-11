import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String[] number = scan.nextLine().split(" ");
        System.out.println(Integer.parseInt(number[0]) - Integer.parseInt(number[1]));
    }
}