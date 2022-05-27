// Generate magic square using the north-east method
// doubts- what to do if n=1
// todo - write the constant and put proper spaces while displaying the matrix

/* VARIABLE AND FUNCTION REFERENCE
1)n - dimensions of the magic square


*/

#include <bits/stdc++.h>
using namespace std;

void display_board(vector<vector<int>> board, int n) {
    cout << "--------------------" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            // cout<<board[i][j]<<" ";
            printf("%-3d ", board[i][j]);
        }
        cout << endl;
    }
    cout << "--------------------" << endl << endl;
}

int main() {
    int n;
    while (true) {
        cout << "Enter the dimensions of the magic square: ";
        cin >> n;
        if (n % 2 == 0) {
            cout << "Please enter a odd number" << endl;
        } else {
            break;
        }
    }

    int m;
    m = n * ((pow(n, 2) + 1) / 2);
    cout << "The magic constant is " << m << endl;

    vector<vector<int>> board(n, vector<int>(n, 0));

    display_board(board, n);

    int row = 0;
    int col = n / 2;

    board[row][col] = 1;
    display_board(board, n);

    for (int i = 2; i <= pow(n, 2); i++) {
        row = row - 1;
        col = col + 1;

        if (row == -1 && col == n) {
            row = row + 2;
            col = col - 1;
        }

        if (row == -1) {
            row = n - 1;
        }

        if (col == n) {
            col = 0;
        }

        if (board[row][col] == 0) {
            board[row][col] = i;
        } else {
            row = row + 2;
            col = col - 1;
            board[row][col] = i;
        }

        display_board(board, n);
    }
}