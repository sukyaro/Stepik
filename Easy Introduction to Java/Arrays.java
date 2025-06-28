
import java.util.Scanner;




/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int arrayLength = input.nextInt();
        int[] myArray = new int[arrayLength];
        for (int i = 0; i < arrayLength; i++) {
            myArray[i] = input.nextInt();
        }
        System.out.println(myArray[arrayLength - 1]);
    }
}
*/


// Question 11
/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int arrayLength = input.nextInt();
        int[] myArray = new int[arrayLength];
        for (int i = 0; i < arrayLength; i++) {
            myArray[i] = input.nextInt();
        }
        int index = input.nextInt();
        System.out.println(myArray[index]);
    }
}
*/


// Question 12
/*
class Example {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int arrayLength = input.nextInt()/2, summ = 0;
        int[] myArray = new int[arrayLength];
        for (int i = 1; i <= arrayLength; i++) {
            myArray[i - 1] = i * 2;
            summ += myArray[i - 1];
            System.out.print(" " + myArray[i - 1]);
        }
        System.out.println("");
        System.out.println(summ); 
    }
}
*/


// Question 13
/*
class Example {
    public static void main(String[] agrs) {
        Scanner input = new Scanner(System.in);
        int arrayLength = input.nextInt();
        int[] myArray = new int[arrayLength];
        for (int i = 0; i < arrayLength; i++) {
            myArray[i] = input.nextInt();
        }
        for (int i = 1; i <= arrayLength - 1; i++) {
            if (myArray[i] > myArray[i - 1]) {
                System.out.println(myArray[i]);
            }
        }
    }
}
*/


// Question 14
/*
class Example {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String myString = input.nextLine();
        String[] myArray = myString.split(",");
        for (int i = 0; i < myArray.length; i++) {
            System.out.println(myArray[i]);
        }
    }
}
*/