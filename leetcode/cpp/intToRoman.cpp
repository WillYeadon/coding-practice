#include <string>
#include <vector>
#include <iostream>

std::string intToRoman(int num) {
    std::vector<std::pair<int, std::string>> valueSymbols = {
        {1000, "M"},
        {900, "CM"},
        {500, "D"},
        {400, "CD"},
        {100, "C"},
        {90, "XC"},
        {50, "L"},
        {40, "XL"},
        {10, "X"},
        {9, "IX"},
        {5, "V"},
        {4, "IV"},
        {1, "I"}
    };

    std::string roman = "";

    for (const auto& pair : valueSymbols) {
        int value = pair.first;
        const std::string& symbol = pair.second;

        while (num >= value) {
            num -= value;
            roman += symbol;
        }
    }

    return roman;
}

int main() {
    int num = 123;
    std::string roman = intToRoman(num);
    std::cout << "Roman numeral representation: " << roman << std::endl;
    return 0;
}
