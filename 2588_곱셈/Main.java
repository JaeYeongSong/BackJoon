import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = Integer.parseInt(scan.nextLine());
        String b = scan.nextLine();

        System.out.println(a * getNumericValue(b, 2));
        System.out.println(a * getNumericValue(b, 1));
        System.out.println(a * getNumericValue(b, 0));
        System.out.println(a * Integer.parseInt(b));
    }

    private static int getNumericValue(String str, int index) {
        return Character.getNumericValue(str.charAt(index));
    }
}