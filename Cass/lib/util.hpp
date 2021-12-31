#include <iostream>
#include <string>
namespace util {
	class Time{
		private:
			std::string timeZone;
			std::string sysTime;
			std::string internetTime;
		public:
			std::string getCurrentTimezone();
			std::string getCurrentTime();
			std::string getInternetTime();
			
			std::string checkCurrentTimezone();
			std::string checkCurrentTime();
			std::string checkInternetTime();
	};
}
