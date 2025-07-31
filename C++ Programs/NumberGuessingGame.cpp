#include <iostream>
#include <cstdlib>  // For rand(), srand()
#include <ctime>    // For time()

using namespace std;

int main() {
    srand(time(0));  // Seed for random number generation

    int secretNumber = rand() % 100 + 1;  // Random number between 1 and 100
    int guess;
    int maxChances = 7;  // You can change this to make it easier/harder
    int chancesLeft = maxChances;

    cout << "===============================" << endl;
    cout << "🎮 Welcome to Number Guessing Game!" << endl;
    cout << "I'm thinking of a number between 1 and 100." << endl;
    cout << "You have " << maxChances << " chances to guess it correctly." << endl;
    cout << "===============================" << endl;

    while (chancesLeft > 0) {
        cout << "\n⏳ Chance " << (maxChances - chancesLeft + 1)
             << " of " << maxChances << ". Enter your guess: ";
        cin >> guess;

        if (guess == secretNumber) {
            cout << "🎉 Correct! You guessed the number in "
                 << (maxChances - chancesLeft + 1) << " tries!" << endl;
            break;
        } else if (guess > secretNumber) {
            cout << "Too high! 🔼 Try a smaller number." << endl;
        } else {
            cout << "Too low! 🔽 Try a bigger number." << endl;
        }

        chancesLeft--;

        if (chancesLeft == 0) {
            cout << "\n💀 Game Over! You've used all your chances." << endl;
            cout << "The correct number was: " << secretNumber << endl;
        }
    }

    cout << "\nThanks for playing! 👋" << endl;
    return 0;
}
