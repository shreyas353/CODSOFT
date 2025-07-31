#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

char board[3][3];
char player = 'X';
char ai = 'O';

void initializeBoard() {
    char num = '1';
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            board[i][j] = num++;
}

void displayBoard() {
    cout << "\n";
    for (int i = 0; i < 3; i++) {
        cout << " ";
        for (int j = 0; j < 3; j++) {
            cout << board[i][j];
            if (j < 2) cout << " | ";
        }
        cout << "\n";
        if (i < 2) cout << "---|---|---\n";
    }
    cout << "\n";
}

bool isMoveValid(int move) {
    int row = (move - 1) / 3;
    int col = (move - 1) % 3;
    return (move >= 1 && move <= 9 && board[row][col] != 'X' && board[row][col] != 'O');
}

void makeMove(char symbol, int move) {
    int row = (move - 1) / 3;
    int col = (move - 1) % 3;
    board[row][col] = symbol;
}

bool checkWin(char symbol) {
    for (int i = 0; i < 3; i++) {
        if ((board[i][0] == symbol && board[i][1] == symbol && board[i][2] == symbol) ||
            (board[0][i] == symbol && board[1][i] == symbol && board[2][i] == symbol))
            return true;
    }
    if ((board[0][0] == symbol && board[1][1] == symbol && board[2][2] == symbol) ||
        (board[0][2] == symbol && board[1][1] == symbol && board[2][0] == symbol))
        return true;

    return false;
}

bool checkDraw() {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[i][j] != 'X' && board[i][j] != 'O')
                return false;
    return true;
}

int getRandomMove() {
    int move;
    do {
        move = rand() % 9 + 1;
    } while (!isMoveValid(move));
    return move;
}

int main() {
    srand(time(0));
    char playAgain;

    do {
        initializeBoard();
        bool gameOver = false;

        while (!gameOver) {
            displayBoard();

            // Player move
            int move;
            cout << "Your turn (X). Enter move (1-9): ";
            cin >> move;

            if (!isMoveValid(move)) {
                cout << "Invalid move. Try again.\n";
                continue;
            }

            makeMove(player, move);

            if (checkWin(player)) {
                displayBoard();
                cout << "You win!\n";
                break;
            }

            if (checkDraw()) {
                displayBoard();
                cout << "It's a draw!\n";
                break;
            }

            // AI move
            int aiMove = getRandomMove();
            makeMove(ai, aiMove);
            cout << "AI played at position " << aiMove << "\n";

            if (checkWin(ai)) {
                displayBoard();
                cout << "AI wins! Better luck next time.\n";
                break;
            }

            if (checkDraw()) {
                displayBoard();
                cout << "It's a draw!\n";
                break;
            }
        }

        cout << "Play again? (y/n): ";
        cin >> playAgain;

    } while (playAgain == 'y' || playAgain == 'Y');

    cout << "Thanks for playing!\n";
    return 0;
}