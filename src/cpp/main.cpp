#include <iostream>
#include <optional>

int main()
{
    std::optional<int> x = 42;
    std::cout << "C++17 works: " << x.value() << '\n';
    return 0;
}