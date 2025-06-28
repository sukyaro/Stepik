import java.util.Scanner;


/*
class MyClass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(sc.nextLine());
    }
}
*/


/*
class Test {
    public static void main(String[] args) {
        Scanner number = new Scanner(System.in);
        System.out.println(number.nextInt());
    }
}
*/

/*
class MySolution {
    public static void main(String[] args) {
        Scanner name = new Scanner(System.in);
        System.out.println("Hello, " + name.nextLine());
    }
}
*/

/*
public class Stepik {
    public static void main(String[] args) {
        System.out.println("What's 10 + 5? ");
        Scanner answer = new Scanner(System.in);
        if (answer.nextInt() == 15) {
            System.out.println("That is right");
        } else {
            System.err.println("Unfortunately it is not right");
        }
    }
}
*/

/*
class MySolution {
    public static void main(String[] args) {
        Scanner string = new Scanner(System.in);
        String output = string.nextLine();
        System.out.println(output + " " + output);
        System.out.println(output);
        System.out.println(output);       
    }
}
*/

/*
class MySolution {
    public static void main(String[] args) {
        Scanner temperature = new Scanner(System.in);
        System.out.println("Температура воздуха сегодня: " + temperature.nextInt() + " градусов.");      
    }
}
*/

/*
class MySolution {
    public static void main(String[] args) {
        Scanner name = new Scanner(System.in);
        String year_1 = name.next(), month_1 = name.next(), day_1 = name.next();
        System.out.println(day_1 + ":" + month_1 + ":" + year_1);    
    }
}
*/

/*
class MySolution {
    public static void main(String[] args) {
        Scanner name = new Scanner(System.in);
        String name_me = name.nextLine(), name_them = name.nextLine(), number = name.nextLine();
        System.out.println("Привет, " + name_me + ", это твой помощник " + name_them + ".");
        System.out.println("У тебя " + number + " новых писем.");
    }
}
*/

/*
class MyNumber {
    public static void main(String[] args) {
        Scanner number = new Scanner(System.in);
        int number_1 = number.nextInt(), number_2 = number.nextInt();
        int new_number = number_1 + number_2;
        System.out.println(new_number);
   }
}
*/

/*
class MyNumber {
    public static void main(String[] args) {
        Scanner number = new Scanner(System.in);
        Double length = number.nextDouble(), width = number.nextDouble();
        Double perimetr = length * 2 + width * 2;
        Double area = length * width;
        System.out.println(area);
        System.out.println(perimetr);

   }
}
*/

/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Double x = input.nextDouble();
        Double y = 5 * Math.pow(x, 2) + 2 * x + 11;
        System.out.println(y);
   }
}
*/

/*
class MyNumber {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        int number = num.nextInt();
        System.out.println(number + " " + number * number + " " + number * number * number);
    }
}
*/

/*
class MyNumber {
    public static void main(String[] args) {
        Scanner number = new Scanner(System.in);
        Double num_1 = number.nextDouble(), num_2 = number.nextDouble(), num_3 = number.nextDouble();
        Double median = (num_1 + num_2 + num_3) / 3;
        System.out.println(median);
    }
}
*/

/*
class MyNumber {
    public static void main(String[] args) {
        Scanner number = new Scanner(System.in);
        int last_dg = Math.abs(number.nextInt());
        System.out.println(last_dg % 10);
    }
}
*/

/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int all_money = input.nextInt(), salary_each = input.nextInt();
        System.out.println(all_money / salary_each + " " + all_money % salary_each);
   }
}
*/

/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int whole_time = input.nextInt();
        int hours = (whole_time % (24*60*60)) / (60*60), temp_mins = whole_time % (60*60);
        int mins = temp_mins / 60, seconds = temp_mins % 60;
        System.out.format("%02d"+":"+"%02d"+":"+"%02d", hours, mins, seconds);
    }
}
*/

/*
class MyNumber {
    public static void main(String[] args) {
        int x = 1, y = 5, z = 0;
        --y;
        System.out.println(y);
        x = 4 + y++;
        System.out.println(x);
        z += x--;
        System.out.println(z);
        x = y + z;      
        System.out.print(++x);
   }
}
*/

/*
class MyNumber {
    public static void main(String[] args) {
        int x = 10;
        System.out.println(++x);
        System.out.println(++x);
        System.out.println(++x);
    }
}
*/

/*
class MyNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();
        System.out.println(--number + " " + ++number + " " + ++number);
    }
}
*/

/*
class MyNumber {
    public static void main(String[] args) {
        Scanner inputs = new Scanner(System.in);
        int x = inputs.nextInt(), y = inputs.nextInt();
        int first_part = (x += 1) / (y -= 1);
        int second_part = (y += 2) / (x -= 2);
        System.out.println(first_part + second_part);
   }
}
*/

/*
class MyProgram {
   public static void main(String[] args) {
       Scanner string = new Scanner(System.in);
       String str = string.nextLine();
       System.out.println(str.length());
   }
}
*/

/*
class MyProgram {
   public static void main(String[] args) {
       Scanner input = new Scanner(System.in);
       String string = input.nextLine();
       System.out.println(string.charAt(0) + " " + string.charAt(string.length() - 1));
   }
}
*/

/*
class MyProgram {
   public static void main(String[] args) {
       Scanner input = new Scanner(System.in);
       String str_1 = input.nextLine(), str_2 = input.nextLine();
       System.out.println(str_1.contains(str_2));
   }
}
*/

/*
class MyProgram {
   public static void main(String[] args) {
       Scanner input = new Scanner(System.in);
       String string = input.nextLine();
       System.out.println(string.toLowerCase());
       System.out.println(string.toUpperCase());
   }
}
*/

/*
class MyProgram {
   public static void main(String[] args) {
       Scanner input = new Scanner(System.in);
       String str = input.nextLine();
       int index = input.nextInt();
       System.out.println(str.charAt(index - 1));
   }
}
*/

/*
class MyProgram {
   public static void main(String[] args) {
       Scanner input = new Scanner(System.in);
       String str_1 = input.nextLine(), str_2 = input.nextLine();
       System.out.println(str_1.equals(str_2));
   }
}
*/

/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String str_1 = input.nextLine(), str_2 = input.nextLine();
        String str_3 = str_1 + " " + str_2;
        System.out.println(str_3);
        System.out.println(str_3.length());
    }
}
*/

/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int number_1 = input.nextInt(), number_2 = input.nextInt();
        System.out.println(number_1 + number_2);
        String num_1 = Integer.toString(number_1), num_2 = Integer.toString(number_2);
        System.out.println(num_1 + num_2);
    }
}
*/

/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String word_1 = input.nextLine(), word_2 = input.nextLine();
        System.out.println(word_1.charAt(0) < word_2.charAt(0));
    }
}
*/


// 2.8 Test
// Question 1
/*
class MyNumber {
   public static void main(String[] args) {
       int x = 4, 
           y = 7;
       int sumNum = x + y;
       System.out.print(sumNum);
   }
}
*/


// Question 3
/*
class MyString {
   public static void main(String[] args) {
    String name;
    name = "Максим";
    System.out.println(name);
   }
}
*/


// Question 4
/*
class MyProgram {
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int days = input.nextInt(), output = days * 60 * 60 * 24;
        System.out.println(output);
	}
}
*/


// Question 7
/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        float a = input.nextInt(), b = input.nextInt(), c = input.nextInt();
        double discriminant = Math.sqrt(Math.pow(b, 2) - (4 * a * c));
        double x1 = ((-b) + discriminant) / (2 * a), x2 = ((-b) - discriminant) / (2 * a);
        double sum = x1 + x2, product = x1 * x2;
        System.out.println(String.format("%.1f", sum) + " " + String.format("%.1f", product));
    }
}
*/


// Question 8
/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int year = input.nextInt();
        int numberOfYears = (year / 4) + (year / 400) - (year / 100);
        System.out.println(numberOfYears);
    }
}
*/


// Question 9
/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num1 = input.nextInt(), num2 = input.nextInt();
        System.out.println("Сложение: " + num1 + " + " + num2 + " = " + (num1 + num2));
        System.out.println("Вычитание: " + num1 + " - " + num2 + " = " + (num1 - num2));
    }
}
*/



// Conditional constructions
// Question 4
/*
class MyProg {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        int inp1 = input.nextInt(), inp2 = input.nextInt();
        if (inp1 > inp2) {
            System.out.println("Махатма");
        } else {
            System.out.println("Джавахарлал");
        }
	}
}
*/


// Question 5
/*
class MyProg {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        String str1 = input.nextLine(), str2 = input.nextLine();
        if (str1.length() > str2.length()) {
            System.out.println("Махатма");
        } else {
            System.out.println("Джавахарлал");
        }
	}
}
*/


// Question 6
/*
class MyProg {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        String inp1 = input.nextLine(), inp2 = input.nextLine();
        if (inp1.equals(inp2)) {
            System.out.println("Access is granted");
        } else {
            System.out.println("Access is denied");
        }
	}
}
*/


// Question 7
/*
class MyProg {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt(), b = input.nextInt(), c = input.nextInt();
        if (a > b) {
            if (a > c) {
                System.out.println(a);
            } else {
                System.out.println(c);
            }
        } else if (b > c) {
            System.out.println(b);
        } else {
            System.out.println(c);
        }
    }
}
*/


// Question 8
/*
class MyProg {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        float x1 = input.nextFloat(), x2 = input.nextFloat();
        System.out.println((x1 < x2) ? "Бой продолжается!" : "Холифилд - чемпион!");
	}
}
*/


// Question 9
/*
class MyProg {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        String num = input.nextLine();
        System.out.println((num.matches("^[3-5]")) ? "YES" : "NO");
	}
}
*/


// Question 10
/*
class MyProg {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        System.out.println((num % 7 == 0) ? "YES" : "NO");
	}
}
*/

/*
// Question 11
class MyProg {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        System.out.println((num % 7 == 0 && num % 5 != 0) ? "YES" : "NO");
	}
}
*/

// Logical constructions
// Question 8
/*
class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String originalString = input.nextLine();
        String singleChar = input.nextLine();
        if (originalString.contains(singleChar) || originalString.length() > 20) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
*/

// Question 10
/*
class MyProgram {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        int num1 = input.nextInt(), num2 = input.nextInt();
        if (((num1 + num2) % 2 == 0) && ((num1 * num2) % 2 != 0)) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
	}
}
*/

// Question 11
/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num1 = input.nextInt(), num2 = input.nextInt(), num3 = input.nextInt();
        if (((num1 % 2 == 0) && (num2 % 2 == 0) && !(num3 % 2 == 0)) ||
            ((num1 % 2 == 0) && (num3 % 2 == 0) && !(num2 % 2 == 0)) ||
            (!(num1 % 2 == 0) && (num2 % 2 == 0) && (num3 % 2 == 0))) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}
*/

// Question 12
/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int day = input.nextInt(), month = input.nextInt(), year = input.nextInt();
        boolean flag = true;
        if (year < 0) {
            flag = false;
        } else if ((month < 1) || (month > 12)) {
            flag = false;
        } else {
            boolean isLeap = false;
            if ((year % 400 == 0) || (year % 4 == 0) && (year % 100 != 0)) {
                isLeap = true;
            }
            if ((month == 1) || (month == 3) || (month == 5) || (month == 7) || (month == 8) || (month == 10) || (month == 12)) {
                if ((day < 1) || (day > 31)) {
                    flag = false;
                }
            } else if ((month == 4) || (month == 6) || (month == 9) || (month == 11)) {
                if ((day < 1) || (day > 30)) {
                    flag = false;
                }
            } else {
                if (isLeap) {
                    if ((day < 1) || (day > 29)) {
                        flag = false;
                    }
                } else {
                    if ((day < 1) || (day > 28)) {
                        flag = false;
                    }
                }
            }
        }

        System.out.println(flag);
    }
}
*/


// Question 13
/*
class MyProgram  {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] words = input.nextLine().split(" ");
        char w1 = words[0].charAt(0), w2 = words[1].charAt(0), w3 = words[2].charAt(0);
        if ((w1 < w2) && (w1 < w3) && (w2 < w3)) {System.out.println(words[0] + "\n" + words[1] + "\n" + words[2]);}
        if ((w2 < w1) && (w1 < w3) && (w2 < w3)) {System.out.println(words[1] + "\n" + words[0] + "\n" + words[2]);}
        if ((w3 < w1) && (w1 < w2) && (w3 < w2)) {System.out.println(words[2] + "\n" + words[0] + "\n" + words[1]);}
        if ((w1 < w2) && (w1 < w3) && (w3 < w2)) {System.out.println(words[0] + "\n" + words[2] + "\n" + words[1]);}
        if ((w2 < w3) && (w2 < w1) && (w3 < w1)) {System.out.println(words[1] + "\n" + words[2] + "\n" + words[0]);}
        if ((w3 < w2) && (w3 < w1) && (w2 < w1)) {System.out.println(words[2] + "\n" + words[1] + "\n" + words[0]);}
        }
}
*/


// Nested conditional constructions
// Question 2
/*
class Example {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num1 = input.nextInt(), num2 = input.nextInt(), num3 = input.nextInt();
        System.out.println(num1 + num2 + num3 - Math.max(num1, Math.max(num2, num3)) - Math.min(num1, Math.min(num2, num3)));
    }
}
*/

// Question 3 
/*
class Example {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] sals = input.nextLine().split(" ");
        int[] sals1 = new int[3];
        int diff = input.nextInt();
        boolean flag = false;

        for (int i = 0; i < 3; i++) {
            sals1[i] = Integer.parseInt(sals[i]);
        }

        if (Math.max(sals1[0], Math.max(sals1[1], sals1[2])) - Math.min(sals1[0], Math.min(sals1[1], sals1[2])) >= diff) {
            flag = true;
        }

        if (flag == true) {
            System.out.println("Ура, бастуем!");
        } else {
            System.out.println("За работу, Солнце ещё высоко");
        }
    }   
}
*/

// Question 4
/*
class Exercise {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] coo1 = input.nextLine().split(" "), coo2 = input.nextLine().split(" ");
        int[] coords1 = new int[2], coords2 = new int[2];
        
        for (int i = 0; i < 2; i++) {
            coords1[i] = Integer.parseInt(coo1[i]);
            coords2[i] = Integer.parseInt(coo2[i]);
        }

        if (coords1[0] - coords2[1] == 0) {
            System.out.println(coords1[0]);
        } else if (coords2[0] - coords1[1] == 0) {
            System.out.println(coords2[0]);
        } else if (coords1[0] >= coords2[0] && coords1[1] <= coords2[1]) {
            System.out.println(coords1[0] + " " + coords1[1]);
        } else if (coords2[0] >= coords1[0] && coords2[1] <= coords1[1]) {
            System.out.println(coords2[0] + " " + coords2[1]);
        } else if (coords1[0] < coords2[0] && coords2[0] < coords1[1] && coords1[1] < coords2[1]) {
            System.out.println(coords2[0] + " " + coords1[1]);
        } else if (coords2[0] < coords1[0] && coords1[0] < coords2[1] && coords2[1] < coords1[1]) {
            System.out.println(coords1[0] + " " + coords2[1]);
        } else {
            System.out.println("Пересечения нет");
        }
    }
}
*/

// Question 5
/*
class Example {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num1 = input.nextInt(), num2 = input.nextInt(), num3 = input.nextInt();
        if (num1 % 2 == 0 && num2 % 2 == 0 && num3 % 2 == 0) {
            System.out.println(Math.max(num1, Math.max(num2, num3)));
        } else if (num1 % 2 == 0 && num2 % 2 == 0 && num3 % 2 != 0) {
            System.out.println((num1 > num2) ? num1 : num2);
        } else if (num1 % 2 == 0 && num2 % 2 != 0 && num3 % 2 == 0) {
            System.out.println((num1 > num3) ? num1 : num3);
        } else if (num1 % 2 != 0 && num2 % 2 == 0 && num3 % 2 == 0) {
            System.out.println((num2 > num3) ? num2 : num3);
        } else if (num1 % 2 == 0 && num2 % 2 != 0 && num3 % 2 != 0) {
            System.out.println(num1);
        } else if (num1 % 2 != 0 && num2 % 2 == 0 && num3 % 2 != 0) {
            System.out.println(num2);
        } else if (num1 % 2 != 0 && num2 % 2 != 0 && num3 % 2 == 0) {
            System.out.println(num3);
        } else {
            System.out.println("Чётных чисел нет");
        }
    }
}
*/


// Switch operation
// Question 5
/*
class MyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String newInput = input.nextLine();
        switch (newInput) {
            case "System.out.println()":
                System.out.println("Это команда вывода на печать");                
                break;
            
            case "if":
                System.out.println("Это условный оператор");
                break;
            
            case "else":
                System.out.println("Это альтернативная конструкция условного оператора");
                break;

            default:
                System.out.println("Раздел в разработке");
        }
    }
}
*/


// Test
// Question 2
/*
class MyTest {
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();
        if (number > 99 && number < 1000) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
*/

// Question 3
/*
class Example {
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String str1 = input.nextLine().toLowerCase(), str2 = input.nextLine().toLowerCase();
        if (str1.contains(str2) == true) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}
*/

// Question 4
/*
class Example {
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int number = Math.abs(input.nextInt()), figure = input.nextInt();
        if (number > 99 && number < 999) {
            if ((number / 10) % 10 == figure) {
                System.out.println("true");
            } else {
                System.out.println("false");
            }
        } else {
            System.out.println("error");
        }
    }
}
*/

// Question 5 
/*
class Example {
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double num1 = input.nextDouble(), num2 = input.nextDouble();
        System.out.println((num1 > num2) ? ">" : (num1 < num2) ? "<" : "=");
    }
}
*/

// Question 6
/*
class Example {
    public static void main(String[] agrs) {
        Scanner input = new Scanner(System.in);
        int month = input.nextInt();
        if (month == 1 || month == 2 || month == 12) {
            System.out.println("Зима");
        } else if (month == 3 || month == 4 || month == 5) {
            System.out.println("Весна");
        } else if (month == 6 || month == 7 || month == 8) {
            System.out.println("Лето");
        } else if (month == 9 || month == 10 || month == 11) {
            System.out.println("Осень");
        } else {
            System.out.println("ERROR");
        }
    }
}
*/

// Question 7
/*
class Example {
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double x = input.nextDouble(), y = input.nextDouble();
        if ((x >= -1.41421 && x <= 1.41421 && y <= 2 - Math.pow(x, 2) && y >= 0) ||
           (x <= 0 && y <= 0 && y > x && y <= 2 - Math.pow(x, 2))) {
            System.out.println("Yes");
           } else {
            System.out.println("No");
           }
    }
}
*/

// Question 8
/*
class Example {
    public static void main(String[] agrs) {
        Scanner input = new Scanner(System.in);
        String string = input.nextLine();
        if ((string.contains("Джефф Безос") == true) ||
            (string.contains("Илон Маск") == true) ||
            (string.contains("Марк Цукерберг") == true) ||
            (string.contains("Билл Гейтс") == true)){
            System.out.println("Добро пожаловать!");
        } else {
            System.out.println("Здесь никого нет, Вы ошиблись дверью");
        }
    }
}
*/

// Question 9
class Example {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String string = input.nextLine();
        switch (string.length()) {
            case (0):
                System.out.println("Ноль букв");
                break;
            case (1):
                System.out.println("Одна буква");
                break;
            case (2):
                System.out.println("Две буквы");
                break;
            case (3):
                System.out.println("Три буквы");
                break;
            case (4):
                System.out.println("Четыре буквы");
                break;
            case (5):
                System.out.println("Пять букв");
                break;
            default:
                System.out.println("Длинное слово");
        }
    }
}