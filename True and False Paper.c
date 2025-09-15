#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int k, n;
        cin >> k >> n;
        cout << abs(k - n) << endl;
    }
    return 0;
}
