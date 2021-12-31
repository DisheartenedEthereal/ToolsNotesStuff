.PHONY : clearscr compile link
all : | clearscr compile link
compile:
	g++ -c lib/util.cpp -o lib.o
	g++ -c lib/network.cpp -o network.o
	g++ -c run.cpp -o run.o
link:
	g++ -o runfile lib.o network.o run.o
	rm lib.o network.o run.o
clearscr:
	clear
