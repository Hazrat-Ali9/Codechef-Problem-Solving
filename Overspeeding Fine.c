#include <bits/stdc++.h>
using namespace std;

int main() {
    
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        if (n <= 70) {
            cout << 0 << "\n";
        } 
        else if (n <= 100) {
            cout << 500 << "\n";
        } 
        else {
            cout << 2000 << "\n";
        }
    }
    return 0;
}


