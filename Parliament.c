#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, x;
        cin >> n >> x;
        if (x * 2 >= n)  
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}

