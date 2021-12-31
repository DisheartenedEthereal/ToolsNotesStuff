#include <cstdio>
#include <iostream>
#include <chrono>
#include <ctime>
#include <string>
#include<unistd.h>
void Welcome_Message();
void Time_Setup();
void Shadowsocks();
int main()
{
  Welcome_Message();
  return 0;
}

void Welcome_Message(){

  time_t now = time(0);
  char* dt = ctime(&now);
	std::cout << "The local date and time is: " << dt << std::endl;
	const char *logoString = R""""( 
 __    __    ___  _        __   ___   ___ ___    ___
|  |__|  |  /  _]| |      /  ] /   \ |   |   |  /  _]
|  |  |  | /  [_ | |     /  / |     || _   _ | /  [_
|  |  |  ||    _]| |___ /  /  |  O  ||  \_/  ||    _]
|  `  '  ||   [_ |     /   \_ |     ||   |   ||   [_
 \      / |     ||     \     ||     ||   |   ||     |
  \_/\_/  |_____||_____|\____| \___/ |___|___||_____|
  --------------------------------------------------
	)"""";
  printf("%s\nHello, friend today is %s\nI\'m currently setting up your usuals.. \n",logoString,dt);
  Time_Setup();
  Shadowsocks();
}

void Time_Setup(){
  system("ntpd -qg > /home/dethereal/locallogs/ntpd");
  // return the current time string
  sleep(5);
  time_t now = time(0);
  char* dt = ctime(&now);
  printf("[+] Your time has been updated to: %s",dt);
}

void Shadowsocks(){
  printf("[+] Shortly, a tmux session with the name \'Shadowsocks\' will be created with your shadowsocks session in it");
  system("sudo -u dethereal tmux new-session -d -s Shadowsocks /home/dethereal/ss.Appimage");



}
