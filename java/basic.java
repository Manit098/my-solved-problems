import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // 1. Print Hello World
        System.out.println("Hello World");

        // 2. Print Your Name
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Your Name: ");
        String username = sc.next();
        System.out.println("Hello " + username);

        // 3. Basic Maths
        int a = 3;
        int b = 5;
        int sum = a + b;
        int sub = a - b;
        int mul = a * b;
        int div = (b != 0) ? a / b : 0; // Avoid division by zero
        System.out.println("Sum = " + sum + ", Sub = " + sub + ", Mul = " + mul + ", Div = " + div);

        // 4. Even or Odd
        System.out.print("Enter a Number: ");
        int inp = sc.nextInt();
        if (inp % 2 == 0) {
            System.out.println("It's an Even Number");
        } else {
            System.out.println("It's an Odd Number");
        }

        // 5. Simple Calculator
        System.out.print("Enter an Operator (plus, minus, multiple, divide): ");
        String operator = sc.next();

        System.out.print("Enter First Number: ");
        int num1 = sc.nextInt();
        System.out.print("Enter Second Number: ");
        int num2 = sc.nextInt();

        if (operator.equals("plus")) {
            System.out.println("Result: " + (num1 + num2));
        } else if (operator.equals("minus")) {
            System.out.println("Result: " + (num1 - num2));
        } else if (operator.equals("multiple")) {
            System.out.println("Result: " + (num1 * num2));
        } else if (operator.equals("divide")) {
            if (num2 != 0) {
                System.out.println("Result: " + (num1 / num2));
            } else {
                System.out.println("Cannot divide by zero.");
            }
        } else {
            System.out.println("Invalid operator.");
        }

        // 6. Swap Numbers
        int swapnum1 = 2;
        int swapnum2 = 4;
        System.out.println("Before Swap: swapnum1 = " + swapnum1 + ", swapnum2 = " + swapnum2);

        // Swapping using a temporary variable
        int temp = swapnum1;
        swapnum1 = swapnum2;
        swapnum2 = temp;

        System.out.println("After Swap: swapnum1 = " + swapnum1 + ", swapnum2 = " + swapnum2);

        // Close the scanner
        sc.close();
        // Area Of Rectangle
        int length = 30;
        int breadth = 20;
        int area = length * breadth;
        System.out.println("Area Of Rectangle Is" + area +"cm2");
        // Area Of Circle
        double radius = 5;
        double circlearea = Math.PI * Math.pow(radius, 2);
        System.out.println("Area of Circle is " + circlearea + " square units");
       // Fahrenheit - Celcius
        Scanner scanner = new Scanner(System.in);


        System.out.print("Enter temperature in Fahrenheit: ");
        double fahrenheit = scanner.nextDouble();


        double celsius = (fahrenheit - 32) * 5 / 9;


        System.out.printf("Temperature in Celsius: %.2f°C%n", celsius);

        scanner.close();
       // Calculate Simple Interest
        Scanner scanner22 = new Scanner(System.in);

        System.out.print("Enter Principal amount: ");
        double principal = scanner22.nextDouble();

        System.out.print("Enter Rate of Interest (per year): ");
        double rate = scanner22.nextDouble();

        System.out.print("Enter Time (in years): ");
        double time = scanner22.nextDouble();

        
        double simpleInterest = (principal * rate * time) / 100;


        System.out.printf("Simple Interest: %.2f%n", simpleInterest);

        scanner.close();
    }
}
