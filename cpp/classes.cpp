#include <iostream>
#include <string>
using namespace std;

class Book{
	public:
		string title;
		string author;
		int pages;
		Book(string aTitle, string aAuthor,int aPages){
			title = aTitle;
			author = aAuthor;
			pages = aPages;
		}
};

int main()
{
	string name = "Booba";
	int age = 18;
	double pi = 3.145;

	//Book book1;
	//book1.title = "Haha";
	//book1.pages = 550 ;
	//book1.author = "Mamdali mash ghorboon";
	Book book1("Gighoo the second","Master Gighoo jr",995);
	std::cout << book1.title << std::endl;
	return 0;
}
