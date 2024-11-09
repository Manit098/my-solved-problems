package problem;

import java.util.Scanner;

public class array {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. Find the largest element in an array
        System.out.print("Enter the size of the array: ");
        int size = sc.nextInt();
        int[] arr = new int[size];

        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < size; i++) {
            arr[i] = sc.nextInt();
        }

        int largest = arr[0];
        for (int i = 1; i < size; i++) {
            if (arr[i] > largest) {
                largest = arr[i];
            }
        }
        System.out.println("The largest element in the array is: " + largest);

        // 2. Find the sum of all elements in an array
        int sum = 0;
        for (int i = 0; i < size; i++) {
            sum += arr[i];
        }
        System.out.println("Sum of all elements in the array is: " + sum);

        // 3. Reverse an array
        System.out.print("Reversed array: ");
        for (int i = size - 1; i >= 0; i--) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        // 4. Check if an array is sorted in ascending order
        boolean isSorted = true;
        for (int i = 1; i < size; i++) {
            if (arr[i] < arr[i - 1]) {
                isSorted = false;
                break;
            }
        }
        if (isSorted) {
            System.out.println("The array is sorted in ascending order.");
        } else {
            System.out.println("The array is not sorted in ascending order.");
        }

        // 5. Count the frequency of a specific element in the array
        System.out.print("Enter the element to count its frequency: ");
        int element = sc.nextInt();
        int frequency = 0;
        for (int i = 0; i < size; i++) {
            if (arr[i] == element) {
                frequency++;
            }
        }
        System.out.println("The frequency of " + element + " in the array is: " + frequency);

        // 6. Find the smallest element in the array
        int smallest = arr[0];
        for (int i = 1; i < size; i++) {
            if (arr[i] < smallest) {
                smallest = arr[i];
            }
        }
        System.out.println("The smallest element in the array is: " + smallest);

        // 7. Check if an array contains a specific element
        System.out.print("Enter the element to check if it exists in the array: ");
        int checkElement = sc.nextInt();
        boolean contains = false;
        for (int i = 0; i < size; i++) {
            if (arr[i] == checkElement) {
                contains = true;
                break;
            }
        }
        if (contains) {
            System.out.println("The array contains the element " + checkElement);
        } else {
            System.out.println("The array does not contain the element " + checkElement);
        }

        // 8. Find the second largest element in an array
        if (size > 1) {
            int firstLargest = Integer.MIN_VALUE;
            int secondLargest = Integer.MIN_VALUE;
            for (int i = 0; i < size; i++) {
                if (arr[i] > firstLargest) {
                    secondLargest = firstLargest;
                    firstLargest = arr[i];
                } else if (arr[i] > secondLargest && arr[i] != firstLargest) {
                    secondLargest = arr[i];
                }
            }
            System.out.println("The second largest element in the array is: " + secondLargest);
        } else {
            System.out.println("Array does not have a second largest element.");
        }

        // 9. Merge two arrays
        System.out.print("Enter the size of the second array: ");
        int size2 = sc.nextInt();
        int[] arr2 = new int[size2];

        System.out.println("Enter the elements of the second array:");
        for (int i = 0; i < size2; i++) {
            arr2[i] = sc.nextInt();
        }

        int[] mergedArray = new int[size + size2];
        for (int i = 0; i < size; i++) {
            mergedArray[i] = arr[i];
        }
        for (int i = 0; i < size2; i++) {
            mergedArray[size + i] = arr2[i];
        }

        System.out.print("Merged Array: ");
        for (int i = 0; i < mergedArray.length; i++) {
            System.out.print(mergedArray[i] + " ");
        }
        System.out.println();

    }
}
