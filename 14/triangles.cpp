#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

std::string line(int l, std::string c) {
  std::string res = "";
  for (int i = 0; i < l; i += 1) {
    res += c;
  }
  res += "\n";
  return res;
}

std::string rect(int w, int h) {
  std::string res = "";
  for (int i = 0; i < h; i += 1) {
    res += line(w, "*");
  }
  return res;
}

/*
 *
 **
 ***
 ****
 */
std::string tri1(int h) {
  std::string res = "";
  for (int i = 1; i <= h; i += 1) {
    res += line(i, "*");
  }
  return res;
}


/*
   *
  ***
 *****
 */
std::string tri2(int h) {
  std::string res;
  res.reserve(((h*2-1) + 1) * h);
  int spaces = h;
  for (int i = 1; i <= h; i += 1) {
    std::fill_n(std::back_inserter(res), spaces - 1, ' ');
    std::fill_n(std::back_inserter(res), i * 2 - 1, '*');
    std::fill_n(std::back_inserter(res), spaces - 1, ' ');
    res.push_back('\n');
    --spaces;
  }
  return res;
}

/*
  *
 **
***
 */
std::string tri3(int h) {
  std::string res;
  res.reserve((h+1)*h);
  int spaces = h;
  for (int i = 1; i <= h; i += 1) {
    std::fill_n(std::back_inserter(res), spaces - 1, ' ');
    std::fill_n(std::back_inserter(res), i, '*');
    res.push_back('\n');
    --spaces;
  }
  return res;
}
int main(){
  string s="hello";
  cout<<s<<endl;
  cout << line(5, "a");
  cout << "\n";
  cout << rect(3, 4);
  cout << "\n";
  cout << tri1(3);
  cout << "\n";
  cout << tri2(3);
  cout << "\n";
  cout << tri3(3);
}
