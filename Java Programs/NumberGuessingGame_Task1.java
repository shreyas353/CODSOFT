import java.util.Random;
import java.util.Scanner;
public class NumberGuessingGame_Task1
{
    public static void main(String[] args) 
    {
        try (Scanner scanner = new Scanner(System.in)) {
            Random random = new Random();
            int rounds = 0;
            int score = 0;
            String playAgain;
            System.out.println("Welcome to the Number Guessing Game!");
            do 
            {
                int numberToGuess = random.nextInt(100) + 1; // number between 1 and 100
                int attemptsAllowed = 7;
                int attempts = 0;
                boolean guessedCorrectly = false; 
                rounds++;
                System.out.println("\nRound " + rounds + ": Guess a number between 1 and 100.");
                System.out.println("You have " + attemptsAllowed + " attempts.");
                while (attempts < attemptsAllowed)
                {
                    System.out.print("Attempt " + (attempts + 1) + ": Enter your guess: ");
                    int guess;
                    // Handle invalid inputs
                    if (scanner.hasNextInt())
                    {
                        guess = scanner.nextInt();
                        attempts++;
                    }
                    else
                    {
                        System.out.println("Please enter a valid number!");
                        scanner.next(); // discard invalid input
                        continue;
                    }
                    if (guess < numberToGuess)
                    {
                        System.out.println("Too low!");
                    }
                    else if (guess > numberToGuess)
                    {
                        System.out.println("Too high!");
                    }
                    else
                    {
                        System.out.println("Correct! You guessed it in " + attempts + " attempts.");
                        score++;
                        guessedCorrectly = true;
                        break;
                    }
                }
                if (!guessedCorrectly) 
                {
                    System.out.println("Out of attempts! The number was: " + numberToGuess);
                }
                System.out.print("\nDo you want to play another round? (yes/no): ");
                scanner.nextLine(); // consume leftover newline
                playAgain = scanner.nextLine().trim().toLowerCase();
            }
            while (playAgain.equals("yes"));
            System.out.println("\nGame Over!");
            System.out.println("You played " + rounds + " round(s) and won " + score + " round(s).");
            System.out.println("Thanks for playing!");
        }
    }
}