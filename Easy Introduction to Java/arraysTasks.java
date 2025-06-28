

import java.util.Scanner;





// Question 3
/*
class MySolution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] stringArray = input.nextLine().split(" ");
        int[] intArray = new int[stringArray.length];
        intArray[0] = Integer.parseInt(stringArray[0]);
        intArray[intArray.length - 1] = Integer.parseInt(stringArray[intArray.length - 1]);
        int barier;
        if (intArray.length % 2 == 0) {
            barier = intArray.length - 2;
        }
        else {
            barier = intArray.length - 3;
            intArray[intArray.length - 2] = Integer.parseInt(stringArray[intArray.length - 2]);
        }
        for (int i = 1; i < barier; i+=2) {
            int temp = Integer.parseInt(stringArray[i]);
            intArray[i] = Integer.parseInt(stringArray[i + 1]);
            intArray[i + 1] = temp;
        }

        for (int i: intArray) {
            System.out.print(i + " ");
        }
    }
}
*/


// Question 4
/*
class MySolution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] myString = input.nextLine().split(" ");
        int myLength = Integer.MAX_VALUE, element = 0;
        for (int i = 0; i < myString.length; i++) {
            if (myString[i].length() < myLength) {
                myLength = myString[i].length();
                element = i + 1;
            }
        }
        System.out.println(element);
    }
}
*/

// Question 5
/*
class MySolution {
    public static void main(String[] agrs) {
        Scanner input = new Scanner(System.in);
        String[] stringArray = input.nextLine().split(" ");
        int summ = Integer.MAX_VALUE;
        for (int i = 0; i < stringArray.length - 2; i++) {
            if (Integer.parseInt(stringArray[i]) + Integer.parseInt(stringArray[i + 2]) < summ) {
                summ = Integer.parseInt(stringArray[i]) + Integer.parseInt(stringArray[i + 2]);
            }
        }
        if (summ == Integer.MAX_VALUE) {
            summ = 0;
        }

        System.out.println(summ);
    }
}
*/