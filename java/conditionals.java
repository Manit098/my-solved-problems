package problem;

import java.util.Scanner;

public class conditionals {
    public static void main(String[] args) {
        // Max Of Two Number
        int max = Math.max(2, 6);
        System.out.println("The Max Of Number Is " + max);
        //Min Of Two Number

        int min = Math.min(3,6);
        System.out.println("The Max Of Number Is " + min);
        // Positive, Negative, or Zero
        Scanner sc = new Scanner(System.in);
        System.out.println("Input The Number To Check It Is Negative Zero Or Positive :");
        int inp = sc.nextInt();
        if(inp > 0) {
            System.out.println("Positive Number");
        }
        else if(inp < 0 ) {
            System.out.println("Negative Number");
        }
        else{
            System.out.println("Number Is Zero Not Negative Or Positive");
        }
        // Grade Calculator
        Scanner sc2 = new Scanner(System.in);
        System.out.println("Enter Your Marks Out Of 100 : ");
        int grade = sc2.nextInt();
        if(grade < 50){
            System.out.println("Your Son Failed The Exam");
        }
        else if(grade <= 80){
            System.out.println("Your Son Is A Average Student");
        }
        else{
            System.out.println("Your Student Won Rat Race ");
        }
        // Leap Year Check
        Scanner sc3 = new Scanner(System.in);
        System.out.println("Enter Which Year It Is");
        int year = sc3.nextInt();
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            System.out.println(year + " is a leap year.");
        } else {
            System.out.println(year + " is not a leap year.");
        }

        // Vowel or Consonant
        Scanner sc4 = new Scanner(System.in);

        System.out.print("Enter a letter: ");
        char ch = sc.next().toLowerCase().charAt(0); // Convert input to lowercase for easy comparison

        // Check if the character is a vowel
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
            System.out.println(ch + " is a vowel.");
        } else if ((ch >= 'a' && ch <= 'z')) { // Check if it's a letter in the alphabet
            System.out.println(ch + " is a consonant.");
        } else {
            System.out.println("Invalid input. Please enter an alphabet letter.");
        }

        // Eligible to Vote
        Scanner sc5 = new Scanner(System.in);
        System.out.println("Enter Your Age : ");
        int age = sc5.nextInt();
        if(age < 18)
            System.out.println("You Can Vote");
        else
            System.out.println("You Cant Vote Kid ");

        // Divisibility Check
        Scanner sc6 = new Scanner(System.in);
        System.out.println("Enter The Number To See Divisibility By 5,11");
        int divisibility = sc6.nextInt();
        if(divisibility % 5 == 0 || divisibility % 11 == 0 )
            System.out.println("Divisible");
        else
            System.out.println("Not Divisible");
        // Even Numbers in Range
        Scanner sc7 = new Scanner(System.in);

        System.out.print("Enter the starting number of the range: ");
        int start = sc.nextInt();

        System.out.print("Enter the ending number of the range: ");
        int end = sc.nextInt();

        System.out.println("Even numbers in the range:");
        for (int i = start; i <= end; i++) {
            if (i % 2 == 0) {
                System.out.print(i + " ");
            }
        }
        // Odd Numbers in Range
        Scanner sc8 = new Scanner(System.in);

        System.out.print("Enter the starting number of the range: ");
        int start2 = sc.nextInt();

        System.out.print("Enter the ending number of the range: ");
        int end2 = sc.nextInt();

        System.out.println("Odd numbers in the range:");
        for (int i = start; i <= end; i++) {
            if (i % 2 != 0) {
                System.out.print(i + " ");
            }
        }
    }
}
