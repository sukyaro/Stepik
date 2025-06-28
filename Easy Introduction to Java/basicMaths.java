import java.util.Scanner;



/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt(), y = input.nextInt();
        System.out.println(Math.pow(x, y));
    }
}
*/


// Question 3
/*
class MyProgram {
    public static void main(String[] args) {
        double number1 = Math.pow(Math.E, Math.PI), number2 = Math.pow(Math.PI, Math.E);
        if (number1 > number2) {
            System.out.println(">");
        }
        else if (number1 < number2) {
            System.out.println("<");
        }
        else {
            System.out.println("=");
        }
    }
}
*/


// Question 5
/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int angle = input.nextInt();
        System.out.println(Math.toRadians(angle));
    }
}
*/


// Question 6
/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int angle = input.nextInt();
        double newAngle = Math.toRadians(angle);
        double sin = Math.sin(newAngle), cos = Math.cos(newAngle);

        System.out.println(sin + cos);
        
    }
}
*/


// Question 7
/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int floating = input.nextInt();
        String newString = "%." + floating + "f";
        String formated = String.format(newString, Math.PI);
        System.out.println(formated);
    }
}
*/


// Question 8
/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt(), y = input.nextInt(), n = input.nextInt();


        double firstPart = Math.pow(x, y);
        double secondPart = Math.pow(firstPart, 1.0/n);
        String formated = String.format("%.5f", secondPart);
        double newNumber = Double.parseDouble(formated);
        

        System.out.println(newNumber);
    }
}
*/


// Question 9
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double a = input.nextDouble(), b = input.nextDouble();
        double c = Math.pow(Math.pow(a, 2) + Math.pow(b, 2), 0.5);

        double perimeter = Math.round(a + b + c);
        System.out.println(perimeter);
    }
}