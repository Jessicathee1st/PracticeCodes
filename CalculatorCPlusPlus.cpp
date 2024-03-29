#include <iostream>
using namespace std;
int main() {
    char operators;
    double a, b;
    //obtaining the type of operand from user
    cout << "Enter an operator (+, -, *, /): ";
    cin >> operators;
    //obtaining the input values for calculations
    cout << "Enter the first number: ";
    cin >> a;
    
    cout<<"Enter the second number: ";
    cin>> b;
    //Calculations
    if (operators == '+') {
        cout << "Sum Result: " << (a+b);
    } else if (operators == '-') {
        cout << "Difference Result: " << (a-b);
    } else if (operators == '*') {
        cout << "Multiplication Result: " << (a*b);
    } else if (operators == '/') {
        if (b != 0)
            cout << "Division Result: " << a/b;
        else
            cout << "Invalid! You cannot divide by zero";
    } else {
        cout << "Your operator is invalid!, enter only +,-,/ or * ";
    }



    return 0;
}

