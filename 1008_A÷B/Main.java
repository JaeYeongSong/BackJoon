import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String[] number = scan.nextLine().split(" ");
        System.out.println(Double.parseDouble(number[0]) / Double.parseDouble(number[1]));
    }
}