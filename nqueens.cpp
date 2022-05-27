//generate n queens method

#include<bits/stdc++.h>
using namespace std;

void display_board(vector<vector<int>>&board,int n){
    cout<<"--------------------"<<endl;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(board[i][j]==1){
                cout<<"Q "; 
            }else{
                cout<<"* "; 
            }
        }
        cout<<endl;
    }
    cout<<"--------------------"<<endl<<endl;

}

bool isSafe(vector<vector<int>>&board,int x, int y, int n){

    //checking the column

    for(int row=0;row<x;row++){
        if(board[row][y]==1){
            return false;
        }
    }

    //checking the north-west diagonal

    int row=x;
    int col=y;

    while(row>=0 && col>=0){
        if(board[row][col]==1){
            return false;
        }
        row--;
        col--;
    }

    //checking the north-east diagonal

    row=x;
    col=y;

    while(row>=0 && col<n){
        if(board[row][col]==1){
            return false;
        }
        row--;
        col++;
    }

    return true;

}

bool nQueen(vector<vector<int>>&board,int x, int n){
    
    if(x>=n){
        return true;
    }

    for(int col=0;col<n;col++){
        if(isSafe(board,x,col,n)){
            board[x][col]=1;
            display_board(board,n);

            if(nQueen(board,x+1,n)){
                return true;
            }

            board[x][col]=0;

        }
        else {
            cout << "Backtracking...\n";
        }
    }
    return false;

     


}

int main(){
    int n;
    cout<<"Enter the dimensions of the chess board ";
    cin>>n;

    vector<vector<int>>board(n,vector<int>(n,0)); 

    // display_board(board,n);
    if(nQueen(board,0,n));
    display_board(board,n);




}