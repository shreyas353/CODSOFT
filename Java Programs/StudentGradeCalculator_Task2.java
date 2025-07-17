import java.util.Scanner;
public class StudentGradeCalculator_Task2
{
    public static void main(String[] args) 
    {
        System.out.println("Student Grade Calculator");
        System.out.print("Enter the number of subjects: ");
        int numSubjects = new Scanner(System.in).nextInt();
        int[] marks = new int[numSubjects];
        int totalMarks = 0;
        for (int i = 0; i < numSubjects; i++) 
        {
            System.out.print("Enter marks for Subject " + (i + 1) + " (out of 100): ");
            marks[i] = new Scanner(System.in).nextInt();
            while (marks[i] < 0 || marks[i] > 100) 
            {
                System.out.print("Invalid mark! Enter again (0–100): ");
                marks[i] = new Scanner(System.in).nextInt();
            }
            totalMarks += marks[i];
        }
        double averagePercentage = (double) totalMarks / numSubjects;
        String grade;
        if (averagePercentage >= 90) 
        {
            grade = "A+";
        } 
        else if (averagePercentage >= 80) 
        {
            grade = "A";
        } 
        else if (averagePercentage >= 70) 
        {
            grade = "B";
        } 
        else if (averagePercentage >= 60) 
        {
            grade = "C";
        } 
        else if (averagePercentage >= 50) 
        {
            grade = "D";
        } 
        else 
        {
            grade = "F";
        }
        System.out.println("\n Result Summary:");
        System.out.println("Total Marks: " + totalMarks + " out of " + (numSubjects * 100));
        System.out.printf("Average Percentage: %.2f%%\n", averagePercentage);
        System.out.println("Grade: " + grade);
    }
}