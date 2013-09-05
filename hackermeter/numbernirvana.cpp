// numbernirvana.cpp
// Author: Morgan Strong
// Date: 4 September 2013
//
// A happy number is defined by the following process: 
// Given a number X, square each digit and sum the results. Repeat this procedure on the resulting sum until you either reach 1, or fall into a repeating cycle which does not include 1. When this process ends in 1, X is a happy number.
// The first line of the input will be an integer N (1 <= N <= 100).
// Each of the following N lines represents a single test case, containing an integer X (1 <= X <= 100000).
// For each test case, print 'Y' if X is a happy number, and 'N' if not. No blank line between test cases.
// 
// Taken from hackermeter.com


#include <iostream>
#include <set>

using namespace std;

int main() {
  int cases, num, sum, digit;
  set<int> seen = set<int>();
  
  cin >> cases;
  while (cases--) {
    
    // Initialize
    cin >> num;
    seen.clear();

    // Run until Completion
    while(true){
      
      // Generate Sum of Squared Digits
      sum = 0;
      while (num){
        digit = num % 10;
        sum += digit * digit;
        num = num / 10;
      }
      
      // Check for Completion
      if(sum == 1){
        cout << "Y" << endl;
        break;
      }
      else if(seen.find(sum) != seen.end()){
        cout << "N" << endl;
        break;
      }
      
      // Prepare for Next Iteration
      num = sum;
      seen.insert(num);
    }
  }
}