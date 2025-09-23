#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        double x, y;
        cin >> x >> y;
        double ans = x + (x / 10.0) - (x - y);
        cout << (int)ans << endl;
    }
    return 0;
}

