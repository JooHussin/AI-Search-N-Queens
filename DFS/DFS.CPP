#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N = 5;
vector<int> board(5, -1);

// Make sure the place is safe by bool isSafe Function
bool isSafe(int row, int col) {
    for (int i = 0; i < row; i++) {
        // same Column or same diameter
        if (board[i] == col ||
            abs(board[i] - col) == abs(i - row)) {
            return false;
        }
    }
    return true;
}

// DFS + Backtracking
bool dfs(int row) {
    if (row == N) {
        return true; 
    }

    for (int col = 0; col < N; col++) {
        if (isSafe(row, col)) {
            board[row] = col;     // نحط الملكة

            if (dfs(row + 1)) {   // نكمل
                return true;
            }

            board[row] = -1;      // Backtrack
        }
    }
    return false;
}

int main() {
    cout << "Solving 5-Queens using DFS : \n\n";

    if (dfs(0)) {
        cout << "Solution Found:\n\n";
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i] == j)
                    cout << "Q ";
                else
                    cout << ". ";
            }
            cout << endl;
        }
    } else {
        cout << "No solution found \n";
    }

    cin.get(); 
    return 0; 
}
