#include <iostream>
using namespace std;

int main() {
    int m;
    cin >> m; 
    while (m--) {
        int n;
        cin >> n;
        if (n > 30)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}

