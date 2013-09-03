// palindrome.cpp
// Author: Morgan Strong
// Date: 3 September 2013
//
// This is a trivial palindrome checker that outputs "Y" or "N" if the string
// received via cin is a palindrome.  Written as a quick C++ refresher exercise
// from hackermeter.com.

#include <iostream>
#include <string>

using namespace std;

int main() {
    int cases, i, j;
    string str;
    bool done;

    // First line of input is the number of test cases.
    cin >> cases;
    getline(cin,str); // Get rid of newline char after number of cases.

    while(cases--) {
        // Get Input
        getline(cin, str);
        i = 0;
        j = str.size() - 1;
        done = false;

        // Iterate characters and check that they match.
        while(i < j){
            if(str[i] != str[j]){
                cout << 'N' << endl;
                done = true;
                break;
            }

            i++;
            j--;
        }

        if(done)
            continue;
        
        // Only Reach This point if all characters match.
        cout << 'Y' << endl;
    }

    return 0;
}