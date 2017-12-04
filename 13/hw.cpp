#include <iostream>

int caught_speeding(int speed, bool is_birthday) {
  int ans = 0;
  if (!is_birthday) {
    if (speed >= 61) {
      ans++;
    }
    if (speed > 80) {
      ans++;
    }
  }
    else {
      if (speed >= 66) {
        ans++;
      }
      if (speed > 86) {
        ans++;
      }
    }
  return ans;
}

bool cigar_party(int cigars, bool is_weekend) {
    bool ans = true;
    if ((!is_weekend and cigars > 60) or cigars <= 40) {
      ans = false;
    }
    return ans;
}

int lone_sum(int a, int b, int c) {
  int ans = 0;
  if (a != b and b != c) {
    ans += b;
  }
  if (c != a and c != b) {
    ans += c;
  }
  if (a != b and a != c) {
    ans += a;
  }
  return ans;
}


int main() {
  std::cout << caught_speeding(61, true);
  std::cout << caught_speeding(61, false);
  std::cout << caught_speeding(67, false);
  std::cout << caught_speeding(81, false);
  std::cout << caught_speeding(81, true);
  std::cout << "\n";

  std::cout << cigar_party(30, false);
  std::cout << cigar_party(50, false);
  std::cout << cigar_party(70, false);
  std::cout << cigar_party(70, true);
  std::cout << "\n";

  std::cout << lone_sum(1, 2, 3);
  std::cout << lone_sum(3, 2, 3);
  std::cout << lone_sum(3, 3, 3);
  std::cout << "\n";
}
