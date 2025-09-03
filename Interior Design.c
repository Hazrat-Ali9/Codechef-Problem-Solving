#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int sum1 = x1 + y1;
        int sum2 = x2 + y2;
        
        if(sum1 > sum2)
            cout << sum2 << endl;
        else
            cout << sum1 << endl;
    }
    return 0;
}
