#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int X, Y;
        cin >> X >> Y;

        int sum = (X / 10) * Y;
        cout << sum << endl;
    }

    return 0;
}
