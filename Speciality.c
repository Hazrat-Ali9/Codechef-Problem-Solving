#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int x, y, z;
        cin >> x >> y >> z;
        int m = max(x, max(y, z));
        
        if (m == x)
            cout << "Setter" << endl;
        else if (m == z)
            cout << "Editorialist" << endl;
        else
            cout << "Tester" << endl;
    }
    return 0;
}

