#include <bits/stdc++.h>
using namespace std;

int main() {

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        if (n < 3) {
            cout << "LIGHT\n";
        } else if (n < 7) {
            cout << "MODERATE\n";
        } else {
            cout << "HEAVY\n";
        }
    }
    return 0;
}

