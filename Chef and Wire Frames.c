#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int m, n, q;
        cin >> m >> n >> q;
        int sum = m * 2 + n * 2;
        cout << sum * q << endl;
    }
    return 0;
}

