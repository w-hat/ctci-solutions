#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>

using namespace std;

extern "C" char* lastklines(char* filename, int k_lines) {
  string lines[k_lines];
  int index = 0;
  ifstream infile(filename);
  if (infile.is_open()) {
    string line;
    while (getline(infile, line)) {
      lines[index] = line + "\n";
      index = (index + 1) % k_lines;
    }
    infile.close();
  }
  string lastlines = "";
  for (int i = 0; i < k_lines; i++) {
    lastlines.append(lines[i]);
  }
  char* ret = (char*)malloc(sizeof(char) * (lastlines.length() + 1));
  strcpy(ret, lastlines.c_str());
  return ret;
}

