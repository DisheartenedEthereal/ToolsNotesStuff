#include <iostream>
#include <thread>
#include <chrono>

int main() {
    std::string s = "Hello Friend, we are here";

    for (const auto c : s) {
        std::cout << c << std::flush;
        std::this_thread::sleep_for(std::chrono::milliseconds(250));
    }
    std::cout << std::endl;
}