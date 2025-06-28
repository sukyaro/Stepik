

import java.util.Scanner;



/*
class MyNumber {
    public static void main(String[] args) {
        for (int i = 1; i < 6; i++) {
            System.out.println(i);
        }
    }
}
*/


// Question 5
/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String number = input.nextLine();

        for (int i = 9; i >= 0; i--) {
            if (number.contains(String.valueOf(i))) {
                System.out.println(i);
                break;
            }
        }
    }
}
*/


// Question 6
/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt(), b = input.nextInt();

        if (a > b) {
            a += b;
            b = a - b;
            a = a - b;
        }

        for (int i = a; i <= b; i++) {
            if (i % 2 != 0) {
                System.out.print(i + " ");
            }
        }
    }
}
*/


// Question 7
/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long number = input.nextLong();

        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                System.out.print(i + " ");
            }
        }

    }
}
*/


// Question 8
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long number = input.nextLong(), count = 0;

        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                count++;
            }
        }

        if (count == 2) {
            System.out.println("true");
        }
        else {
            System.out.println("false");
        }
    }
}