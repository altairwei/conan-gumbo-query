#include <iostream>
#include <string>
#include "gumbo-query/Document.h"
#include "gumbo-query/Node.h"

int main(int argc, char * argv[])
{
  std::string page("<h1><a>Hello World !</a></h1>");
  CDocument doc;
  doc.parse(page.c_str());

  CSelection c = doc.find("h1 a");
  std::cout << c.nodeAt(0).text() << std::endl;
  return 0;
}