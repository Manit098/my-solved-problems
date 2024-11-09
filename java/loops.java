package problem;

import java.util.Scanner;

public class loops {
    public static void main(String[] args) {
        // 1. Print Numbers 1 to 10
        System.out.println("Printing Numbers 1 to 10:");
        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
        }

        // 2. Sum of First N Natural Numbers
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number N: ");
        int N = sc.nextInt();
        int sum = 0;
        for (int i = 1; i <= N; i++) {
            sum += i;
        }
        System.out.println("Sum of the first " + N + " natural numbers is: " + sum);

        // 3. Factorial of a Number
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        int factorial = 1;
        for (int i = 1; i <= num; i++) {
            factorial *= i;
        }
        System.out.println("Factorial of " + num + " is: " + factorial);

        // 4. Multiplication Table
        System.out.print("Enter a number to generate its multiplication table: ");
        int number = sc.nextInt();
        System.out.println("Multiplication Table for " + number + ":");
        for (int i = 1; i <= 10; i++) {
            System.out.println(number + " x " + i + " = " + (number * i));
        }

        // 5. Fibonacci Series
        System.out.print("Enter the number of terms in the Fibonacci series: ");
        int terms = sc.nextInt();
        int a = 0, b = 1;
        System.out.print("Fibonacci Series: ");
        for (int i = 1; i <= terms; i++) {
            System.out.print(a + " ");
            int nextTerm = a + b;
            a = b;
            b = nextTerm;
        }
        System.out.println();

        // 6. Sum of Digits
        System.out.print("Enter a number to calculate the sum of its digits: ");
        int number1 = sc.nextInt();
        int sumOfDigits = 0;
        while (number1 != 0) {
            sumOfDigits += number1 % 10;
            number1 /= 10;
        }
        System.out.println("Sum of digits: " + sumOfDigits);

        // 7. Reverse a Number
        System.out.print("Enter a number to reverse it: ");
        int numberToReverse = sc.nextInt();
        int reversedNumber = 0;
        while (numberToReverse != 0) {
            reversedNumber = reversedNumber * 10 + numberToReverse % 10;
            numberToReverse /= 10;
        }
        System.out.println("Reversed Number: " + reversedNumber);

        // 8. Palindrome Check
        System.out.print("Enter a number to check if it is a palindrome: ");
        int numToCheck = sc.nextInt();
        int originalNum = numToCheck;
        int reversed = 0;
        while (numToCheck != 0) {
            reversed = reversed * 10 + numToCheck % 10;
            numToCheck /= 10;
        }
        if (originalNum == reversed) {
            System.out.println(originalNum + " is a palindrome.");
        } else {
            System.out.println(originalNum + " is not a palindrome.");
        }

        // 9. Armstrong Number
        System.out.print("Enter a number to check if it is an Armstrong number: ");
        int armstrongNum = sc.nextInt();
        int originalArmstrongNum = armstrongNum;
        int numLength = String.valueOf(armstrongNum).length();
        int armstrongSum = 0;
        while (armstrongNum != 0) {
            int digit = armstrongNum % 10;
            armstrongSum += Math.pow(digit, numLength);
            armstrongNum /= 10;
        }
        if (originalArmstrongNum == armstrongSum) {
            System.out.println(originalArmstrongNum + " is an Armstrong number.");
        } else {
            System.out.println(originalArmstrongNum + " is not an Armstrong number.");
        }

        // 10. GCD of Two Numbers
        System.out.print("Enter the first number to find GCD: ");
        int num1ForGCD = sc.nextInt();
        System.out.print("Enter the second number to find GCD: ");
        int num2ForGCD = sc.nextInt();
        int gcd = 1;
        for (int i = 1; i <= num1ForGCD && i <= num2ForGCD; i++) {
            if (num1ForGCD % i == 0 && num2ForGCD % i == 0) {
                gcd = i;
            }
        }
        System.out.println("GCD of " + num1ForGCD + " and " + num2ForGCD + " is: " + gcd);

        
    }
}
