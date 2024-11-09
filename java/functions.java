package problem;

public class Func {
    
    // Function to find the maximum of two numbers
    public static void maxim(int a, int b) {
        int m = Math.max(a, b);
        System.out.println("Maximum of " + a + " and " + b + " is: " + m);
    }

    // Function to find the minimum of two numbers
    public static void minim(int a, int b) {
        int mn = Math.min(a, b);
        System.out.println("Minimum of " + a + " and " + b + " is: " + mn);
    }

    // Function to calculate the square of a number
    public static void square(int a) {
        int squ = a * a;
        System.out.println("Square of " + a + " is: " + squ);
    }

    // Function to add two numbers
    public static void additionFunction(int a, int b) {
        int sum = a + b;
        System.out.println("Sum of " + a + " and " + b + " is: " + sum);
    }

    // Function to print a hello message
    public static void hello() {
        System.out.println("Hello From Function");
    }

    // Function to calculate the factorial of a number
    public static void factorial(int n) {
        int fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        System.out.println("Factorial of " + n + " is: " + fact);
    }

    // Function to check if a number is even or odd
    public static void evenOrOdd(int n) {
        if (n % 2 == 0) {
            System.out.println(n + " is Even");
        } else {
            System.out.println(n + " is Odd");
        }
    }

    // Function to check if a number is prime
    public static void isPrime(int n) {
        boolean prime = true;
        if (n <= 1) {
            prime = false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                prime = false;
                break;
            }
        }
        if (prime) {
            System.out.println(n + " is Prime");
        } else {
            System.out.println(n + " is not Prime");
        }
    }

    // Function to find the sum of digits of a number
    public static void sumOfDigits(int n) {
        int sum = 0;
        while (n != 0) {
            sum += n % 10;
            n /= 10;
        }
        System.out.println("Sum of digits is: " + sum);
    }

    // Function to check if a number is a palindrome
    public static void isPalindrome(int n) {
        int original = n;
        int reversed = 0;
        while (n != 0) {
            int digit = n % 10;
            reversed = reversed * 10 + digit;
            n /= 10;
        }
        if (original == reversed) {
            System.out.println(original + " is a Palindrome");
        } else {
            System.out.println(original + " is not a Palindrome");
        }
    }

    // Function to calculate the sum of first N natural numbers
    public static void sumOfNaturalNumbers(int n) {
        int sum = (n * (n + 1)) / 2;
        System.out.println("Sum of first " + n + " natural numbers is: " + sum);
    }

    // Function to generate Fibonacci series up to N terms
    public static void fibonacci(int n) {
        int a = 0, b = 1;
        System.out.print("Fibonacci Series: ");
        for (int i = 1; i <= n; i++) {
            System.out.print(a + " ");
            int nextTerm = a + b;
            a = b;
            b = nextTerm;
        }
        System.out.println();
    }

    // Function to calculate the power of a number (x^y)
    public static void power(int x, int y) {
        int result = 1;
        for (int i = 1; i <= y; i++) {
            result *= x;
        }
        System.out.println(x + " raised to the power " + y + " is: " + result);
    }

    public static void main(String[] args) {
        hello();
        additionFunction(2, 4);
        square(4);
        maxim(10, 20);
        minim(10, 20);
        
        // Additional function calls
        factorial(5); // Factorial of 5
        evenOrOdd(7);  // Check if 7 is even or odd
        isPrime(11);   // Check if 11 is prime
        sumOfDigits(123);  // Sum of digits of 123
        isPalindrome(121); // Check if 121 is a palindrome
        sumOfNaturalNumbers(10); // Sum of first 10 natural numbers
        fibonacci(5); // Generate Fibonacci series up to 5 terms
        power(2, 3); // Calculate 2 raised to the power 3
    }
}
