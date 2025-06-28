

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Arrays;


/*
class MyClass {
    public static void main(String[] args) {
        int[][] myNastedArray = {{1, 2}, {3, 4}, {5, 6}};
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 2; j++) {
                System.out.print(myNastedArray[i][j] + " ");
            }
            System.out.println("");
        }
    }
}
*/


// Question 3
/*
class MySolution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int rows = input.nextInt(), columns = input.nextInt();
        int[][] multTable = new int[rows][columns];
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= columns; j++) {
                multTable[i - 1][j - 1] = i * j;
                System.out.print(j == columns ? multTable[i - 1][j - 1]: multTable[i - 1][j - 1] + " ");
            }
            System.out.println("");
        }
    }
}
*/

// Question 5
/*
class MySolution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int rows = input.nextInt();
        input.nextLine();
        String[][] myDictionary = new String[rows][];
        for (int i = 0; i < rows; i++) {
            String[] newLine = input.nextLine().split(" ");
            myDictionary[i] = newLine;
            System.out.println(Arrays.toString(myDictionary[i]));
        }
    }
}
*/


// Question 7
/*
class MySolution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int rows = 0, columns = 0;
        while (input.hasNext()) {
            rows++;
            String[] newLine = input.nextLine().split(" ");
            columns = newLine.length;
        }
        System.out.println("Строк: " + rows);
        System.out.println("Столбцов: " + columns);
    }
}
*/


// Question 8
/*
class MySolution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int element = 0;
        while (input.hasNext()) {
            String[] newLine = input.nextLine().split(" ");
            System.out.print(newLine[element] + " ");
            if (element < newLine.length - 1) {
                element++;
            }
            else {
                break;
            }
        }
    }
}
*/


// Question 9
class MySolution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<String[]> mainArray = new ArrayList<>();
        
        while (input.hasNext()) {
            String[] singleLine = input.nextLine().split(" ");
            mainArray.add(singleLine);
        }

        int rows = mainArray.size() - 1;
        int columns = mainArray.get(0).length - 1; 
        String[][] updatedArray = new String[columns + 1][rows + 1];
        
        for (int i = 0; i <= rows; i++) {
            for (int j = 0; j <= columns; j++) {
                updatedArray[j][i] = mainArray.get(rows - i)[columns - j];
            }
        }

        for (int i = columns; i != -1; i--) {
            for (int j = 0; j <= rows; j++) {
                System.out.print(updatedArray[i][j]);
                if (j != rows) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}