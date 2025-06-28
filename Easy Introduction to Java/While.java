import java.util.Scanner;

// Question 5
/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int counter = input.nextInt(), i = 1;
        while (i <= counter) {
            System.out.println(i);
            i++;
        }
    }
}
*/

// Question 6
/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int number = input.nextInt(), i = 1;
        while ((i * i) < number) {
            System.out.print(i * i + " ");
            i++;
        }
    }
}
*/

// Question 7
/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        boolean flag = true;
        int sum = 0;
        while (flag == true) {
            int number = input.nextInt();
            if (number == 0) {
                flag = false;
            } else {
                sum += number;
            }
        }
        System.out.println(sum);
    }
}
*/

// Question 8
/*
class MyNumber {
    public static void main(String[] agrs) {
        Scanner input = new Scanner(System.in);
        int counter = 0;
        while (input.hasNext()) {
            String word = input.next();
            if (word.equalsIgnoreCase(" ")) {
                break;
            } else {
                counter += 1;
            }
        }
        System.out.println(counter);
    }
}
*/

// Question 13
/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int count = 0, div3 = 0;
        while (true) {
            int number = input.nextInt();
            if (number % 11 != 0) {
                break;
            } else {
                count += 1;
                if (number % 3 == 0) {
                    div3 += number;
                }
            }
        }
        System.out.println(count);
        System.out.println(div3);
    }
}
*/

// Question 14
/*
class MyNumber {
    public static void main(String[] agrs) {
        Scanner input = new Scanner(System.in);
        float count = 0, total = 0;
        while (true) {
            int number = input.nextInt();
            if (number > 10 || number < 0) {break;}
            else {count += 1; total += number;}
        }
        System.out.println(total / count);
    }
}
*/

// Question 15
/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long number = input.nextLong();
        while (number > 0) {
            System.out.print(number % 10);
            number = number / 10;
        }
    }
}
*/

// Question 16
/*
class MyProgram {
    public static void main(String[] agrs) {
        Scanner input = new Scanner(System.in);

        String letters = input.nextLine();
        char letter1 = letters.charAt(0);
        char letter2 = letters.charAt(2);

        while (input.hasNext()) {
            String word = input.next();
            if (word.charAt(0) >= letter1 && word.charAt(0) <= letter2) {
                System.out.println(word);
            }
        }
    }
}
*/
