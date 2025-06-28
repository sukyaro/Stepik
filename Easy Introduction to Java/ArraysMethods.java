

import java.util.Arrays;
import java.util.Scanner;


// Question 2
/*
class Example {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] myIntArray = new int[n];
        input.nextLine();
        String[] myStringArray = input.nextLine().split(" ");
        int element = input.nextInt();
        for (int i = 0; i < myStringArray.length; i++) {
            myIntArray[i] = Integer.parseInt(myStringArray[i]);
        }
        Arrays.sort(myIntArray);
        try {
            System.out.println(myIntArray[element - 1]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Ошибка ввода");
        }
    }
}
*/


// Question 3
/*
class Example {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] myStringArray = input.nextLine().split(" ");
        int[] myIntArray = new int[myStringArray.length];
        for (int i = 0; i < myIntArray.length; i++) {
            myIntArray[i] = Integer.parseInt(myStringArray[i]);
        }
        Arrays.sort(myIntArray);
        System.out.println(Arrays.toString(myIntArray));
    }
}
*/



