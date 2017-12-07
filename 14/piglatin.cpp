#include <iostream>
#include <string>
#include <locale>

using std::cout;
using std::endl;

bool is_vowel(char vowel) {
  if (vowel == 'a' || vowel == 'e' || vowel == 'i' || vowel == 'o' || vowel == 'u') {
    return true;
  }
  else {
    return false;
  }
}

std::string translate(std::string word) {
  std::string res = "";

  //Change to lowercase
  for (int i = 0; i < word.length(); i++) {
    word[i] = tolower(word[i]);
  }

  //Translate
  if (is_vowel(word[0])) {
    res = word + "ay";
  }
  else {
    res = word.substr(1, word.length()) + word[0] + "ay";
   }
   return res;
}

int main() {
  cout << translate("hello") << endl;
  cout << translate("apple") << endl;
  cout << translate("person") << endl;
  cout << translate("orange") << endl;
}
