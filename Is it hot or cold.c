#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        if (n > 20)
            cout << "HOT" << endl;
        else
            cout << "COLD" << endl;
    }
    return 0;
}

