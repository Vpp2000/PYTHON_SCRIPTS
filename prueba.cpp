#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int i,j;
    
    for (i=6 ; i>=0 ; i--){

        for (j=-6 ; j<=6 ; j++){
            if (abs(i)+abs(j) <= 6){
                cout << "*" ;
            }
        }
        cout << "\n";
    }
 return 0;
}

