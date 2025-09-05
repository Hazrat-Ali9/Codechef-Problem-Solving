#include <iostream>
using namespace std;

int cost(int x) {
    if (x <= 300) {
        return 3000;
    } else {
        return x * 10;
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int x;
        cin >> x;
        cout << cost(x) << endl;
    }
    return 0;
}


