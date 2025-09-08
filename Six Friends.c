#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int x, y;
        cin >> x >> y;
        int s = x * 3;
        int z = y * 2;
        cout << min(s, z) << endl;
    }
    return 0;
}

