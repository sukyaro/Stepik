

import java.util.ArrayList;
import java.util.Scanner;

/*
class MySolution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String key = input.nextLine();
        String[] list = input.nextLine().split(" ");
        String found = "Неверный ввод";

        for (int i = 0; i < list.length; i++) {
            if (i == Integer.parseInt(key)) {
                found = list[i];
            }
        }

        System.out.println(found);

    }
}
*/

/*
class MySolution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] list = input.nextLine().split(" ");

        for (int i = 0; i < list.length; i++) {
            int counter = 0;
            String key = list[i];
            for (int j = 0; j < list.length; j++) {
                if (key.equals(list[j])) {
                    counter++;
                }
            }
            if (counter == 1) {
                System.out.print(key + " ");
            }
        }

    }
}
*/

/*
class MySolution {
    public static void main(String[] args) {
        ArrayList<String[]> mainArray = new ArrayList<>();
        Scanner input = new Scanner(System.in);

        while (input.hasNext()) {
            String[] line = input.nextLine().split(" ");
            mainArray.add(line);
        }

        int rows = mainArray.size() - 1;
        int columns = mainArray.get(0).length - 1;

        String[][] updatedArray = new String[columns + 1][rows + 1];

        for (int i = columns; i != -1; i--) {
            for (int j = 0; j <= rows; j++) {
                updatedArray[columns - i][j] = mainArray.get(j)[i];
            }
        }

        for (int i = 0; i <= columns; i++) {
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
*/

class MySolution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String[] matrixSize = input.nextLine().split(" ");
        int rows = Integer.parseInt(matrixSize[0]);
        int columns = Integer.parseInt(matrixSize[1]);
        int[][] field = new int[rows + 2][columns + 2];
        
        int bombs = input.nextInt();
        if (bombs > 0) {input.nextLine();}

        
        for (int i = 0; i < bombs; i++) {
            String[] bombCoordinates = input.nextLine().split(" ");
            int x = Integer.parseInt(bombCoordinates[0]);
            int y = Integer.parseInt(bombCoordinates[1]);
            field[x][y] = rows * columns;

            for (int j = x - 1; j <= x + 1; j++) {
                for (int k = y - 1; k <= y + 1; k++) {
                    field[j][k]++;
                }
            }
        }
        
        
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= columns; j++) {
                if (field[i][j] >= rows * columns) {
                    System.out.print("m");
                }
                else {
                System.out.print(field[i][j]);
                }
                if (j != columns) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
        
    }
}