// sublimestring.cpp
// Author: Morgan Strong
// Date: 4 September 2013
//
// Two strings are "sublime" when all the characters in the first string appear in the same order in the second string. For example, "rat" and "rather" are sublime, "mat" and "moat" are sublime, but "can" and "cat" are not. We want to determine whether pairs of strings are sublime or not.
// The first line of the input will be an integer N (1 <= N <= 100).
// Each of the following N lines represents a single test case, containing a space-separated pair of strings A, B, each of which consists of only letters (no special characters).
// For each test case, print 'sublime' if A is sublime to B, or 'unsublime' if not. No blank line between test cases.
// 
// Taken from hackermeter.com

#include <iostream>
#include <string>

using namespace std;

int main() {
  int cases;
  string str1, str2;
  
  // Iterate Over Cases
  cin >> cases;
  getline(cin, str1); // Clear '\n' after number of cases.
  while (cases--) {
    
    // Initialize
    getline(cin, str1, ' ');
    getline(cin, str2);
    string::iterator it1 = str1.begin();
    
    // Iterate through second string.
    for(string::iterator it2 = str2.begin(); it2 != str2.end(); it2++){
      // Check for Match and Increment.
      if(*it1 == *it2)
        it1++;
      
      // Check for Completion
      if(it1 == str1.end()){
        cout << "sublime" << endl;
        break;
      }
    }

    if(it1 != str1.end())
      cout << "unsublime" << endl;
  }
}