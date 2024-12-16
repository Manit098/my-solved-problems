// Problem 1: Create a Class
class Dog {
    String name;
    int age;
}

// Problem 2: Constructor Overloading
class Rectangle {
    int length;
    int width;

    Rectangle(int l, int w) {
        length = l;
        width = w;
    }

    Rectangle(int side) {
        length = side;
        width = side;
    }
}

// Problem 3: Method Overloading
class MathOperations {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
}

// Problem 4: Inheritance
class Animal {
    void sound() {
        System.out.println("Animal makes sound");
    }
}

class Cat extends Animal {
    void sound() {
        System.out.println("Cat meows");
    }
}

// Problem 5: Method Overriding
class Vehicle {
    void start() {
        System.out.println("Vehicle starts");
    }
}

class Car extends Vehicle {
    void start() {
        System.out.println("Car starts");
    }
}

// Problem 6: Abstract Class
abstract class Shape {
    abstract void draw();
}

class Circle extends Shape {
    void draw() {
        System.out.println("Drawing Circle");
    }
}

// Problem 7: Interface
interface Animal {
    void eat();
}

class Dog implements Animal {
    public void eat() {
        System.out.println("Dog eats");
    }
}

// Problem 8: Multiple Inheritance (via Interfaces)
interface CanRun {
    void run();
}

interface CanBark {
    void bark();
}

class Dog implements CanRun, CanBark {
    public void run() {
        System.out.println("Dog runs");
    }

    public void bark() {
        System.out.println("Dog barks");
    }
}

// Problem 9: Static Methods
class Utility {
    static void printMessage() {
        System.out.println("Hello from Utility");
    }
}

// Problem 10: Static Variables
class Counter {
    static int count = 0;

    Counter() {
        count++;
    }
}

// Problem 11: Final Keyword
final class FinalClass {
    // This class cannot be inherited
}

// Problem 12: Final Method
class Base {
    final void display() {
        System.out.println("Final method");
    }
}

// Problem 13: Encapsulation
class Person {
    private String name;

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

// Problem 14: Composition
class Engine {
    void start() {
        System.out.println("Engine starts");
    }
}

class Car {
    Engine engine = new Engine();

    void start() {
        engine.start();
    }
}

// Problem 15: Aggregation
class Department {
    String name;

    Department(String name) {
        this.name = name;
    }
}

class Employee {
    Department department;

    Employee(Department department) {
        this.department = department;
    }
}

// Problem 16: Polymorphism
class Animal {
    void sound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
    void sound() {
        System.out.println("Bark");
    }
}

// Problem 17: Constructor Chaining
class A {
    A() {
        this(5);
    }

    A(int x) {
        System.out.println("Value: " + x);
    }
}

// Problem 18: Inner Class
class Outer {
    class Inner {
        void display() {
            System.out.println("Inner class");
        }
    }
}

// Problem 19: Anonymous Inner Class
abstract class AbstractClass {
    abstract void display();
}

class Test {
    AbstractClass obj = new AbstractClass() {
        void display() {
            System.out.println("Anonymous Inner Class");
        }
    };
}

// Problem 20: Singleton Pattern
class Singleton {
    private static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}

// Problem 21: Exception Handling
class ExceptionExample {
    void divide(int a, int b) {
        try {
            System.out.println(a / b);
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero");
        }
    }
}

// Problem 22: Custom Exception
class MyException extends Exception {
    MyException(String message) {
        super(message);
    }
}

// Problem 23: Java Collections - ArrayList
import java.util.ArrayList;

class CollectionExample {
    ArrayList<String> list = new ArrayList<>();
}

// Problem 24: Java Collections - HashMap
import java.util.HashMap;

class MapExample {
    HashMap<String, Integer> map = new HashMap<>();

    void addEntry(String key, Integer value) {
        map.put(key, value);
    }

    Integer getValue(String key) {
        return map.get(key);
    }
}

// Problem 25: Java Collections - HashSet
import java.util.HashSet;

class SetExample {
    HashSet<String> set = new HashSet<>();

    void addElement(String element) {
        set.add(element);
    }

    boolean containsElement(String element) {
        return set.contains(element);
    }
}

// Problem 26: Java Collections - LinkedList
import java.util.LinkedList;

class LinkedListExample {
    LinkedList<String> list = new LinkedList<>();

    void addElement(String element) {
        list.add(element);
    }

    String getFirstElement() {
        return list.getFirst();
    }
}

// Problem 27: Java Collections - Stack
import java.util.Stack;

class StackExample {
    Stack<Integer> stack = new Stack<>();

    void push(int value) {
        stack.push(value);
    }

    int pop() {
        return stack.pop();
    }
}

// Problem 28: Java Collections - Queue
import java.util.LinkedList;
import java.util.Queue;

class QueueExample {
    Queue<String> queue = new LinkedList<>();

    void enqueue(String element) {
        queue.add(element);
    }

    String dequeue() {
        return queue.poll();
    }
}

// Problem 29: Comparable Interface
class Person implements Comparable<Person> {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public int compareTo(Person other) {
        return this.age - other.age;
    }
}

// Problem 30: Comparator Interface
import java.util.Comparator;

class PersonComparator implements Comparator<Person> {
    public int compare(Person p1, Person p2) {
        return p1.name.compareTo(p2.name);
    }
}

// Problem 31: Serialization
import java.io.*;

class Employee implements Serializable {
    String name;
    int age;

    Employee(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

// Problem 32: Deserialization
class DeserializeExample {
    Employee deserializeEmployee(String filename) throws IOException, ClassNotFoundException {
        FileInputStream fileIn = new FileInputStream(filename);
        ObjectInputStream in = new ObjectInputStream(fileIn);
        Employee emp = (Employee) in.readObject();
        in.close();
        fileIn.close();
        return emp;
    }
}

// Problem 33: Thread Creation - Extending Thread
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running");
    }
}

// Problem 34: Thread Creation - Implementing Runnable
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Runnable is running");
    }
}

// Problem 35: Synchronization
class Counter {
    private int count = 0;

    synchronized void increment() {
        count++;
    }

    int getCount() {
        return count;
    }
}

// Problem 36: Deadlock
class Resource {
    synchronized void methodA(Resource resource) {
        System.out.println("Thread 1: Holding resource 1...");
        try { Thread.sleep(100); } catch (InterruptedException e) {}
        System.out.println("Thread 1: Waiting for resource 2...");
        resource.methodB();
    }

    synchronized void methodB() {
        System.out.println("Resource 2");
    }
}

// Problem 37: Java Streams - Filtering
import java.util.List;
import java.util.stream.Collectors;

class StreamExample {
    List<String> filterNames(List<String> names) {
        return names.stream().filter(name -> name.startsWith("A")).collect(Collectors.toList());
    }
}

// Problem 38: Java Streams - Mapping
import java.util.List;
import java.util.stream.Collectors;

class MapExample {
    List<Integer> getLengths(List<String> names) {
        return names.stream().map(String::length).collect(Collectors.toList());
    }
}

// Problem 39: Lambda Expressions
interface Greeting {
    void greet(String name);
}

class LambdaExample {
    void sayHello() {
        Greeting greeting = name -> System.out.println("Hello, " + name);
        greeting.greet("World");
    }
}

// Problem 40: Functional Interface
@FunctionalInterface
interface Calculator {
    int calculate(int a, int b);
}
// Problem 41: Java Enums
enum Day {
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
}

// Problem 42: Enum with Methods
enum Season {
    WINTER, SPRING, SUMMER, FALL;

    public String getDescription() {
        switch (this) {
            case WINTER: return "Cold and snowy";
            case SPRING: return "Flowers bloom";
            case SUMMER: return "Hot and sunny";
            case FALL: return "Leaves fall";
            default: return "Unknown";
        }
    }
}

// Problem 43: Java Annotations
@interface MyAnnotation {
    String value();
}

@MyAnnotation(value = "Example Annotation")
class AnnotatedClass {}

// Problem 44: Custom Annotation Processing
import java.lang.reflect.Method;

class AnnotationProcessor {
    void processAnnotations(Class<?> clazz) {
        for (Method method : clazz.getDeclaredMethods()) {
            if (method.isAnnotationPresent(MyAnnotation.class)) {
                MyAnnotation annotation = method.getAnnotation(MyAnnotation.class);
                System.out.println("Method: " + method.getName() + ", Annotation Value: " + annotation.value());
            }
        }
    }
}

// Problem 45: Java Reflection
import java.lang.reflect.Field;

class ReflectionExample {
    void printFields(Class<?> clazz) {
        Field[] fields = clazz.getDeclaredFields();
        for (Field field : fields) {
            System.out.println("Field: " + field.getName());
        }
    }
}

// Problem 46: Method References
import java.util.Arrays;
import java.util.List;

class MethodReferenceExample {
    void printList() {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
        names.forEach(System.out::println);
    }
}

// Problem 47: Optional Class
import java.util.Optional;

class OptionalExample {
    Optional<String> getName(boolean isPresent) {
        return isPresent ? Optional.of("John Doe") : Optional.empty();
    }
}

// Problem 48: Stream Reduce
import java.util.Arrays;
import java.util.List;

class ReduceExample {
    int sum(List<Integer> numbers) {
        return numbers.stream().reduce(0, Integer::sum);
    }
}

// Problem 49: CompletableFuture
import java.util.concurrent.CompletableFuture;

class CompletableFutureExample {
    void runAsyncTask() {
        CompletableFuture.runAsync(() -> {
            System.out.println("Asynchronous task running");
        });
    }
}

// Problem 50: Java Module System
module my.module {
    exports com.example;
}
