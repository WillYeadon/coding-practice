#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = i + 1; j < nums.size(); ++j) {
                if ((nums[i] + nums[j] == target) && (i != j)) {
                    return { i, j };
                }
            }
        }
        return {};
    }
};

int main()
{
    Solution sol;
    std::vector<int> nums = { 2, 7, 11, 15 };
    int target = 9;

    std::vector<int> result = sol.twoSum(nums, target);

    if (!result.empty()) {
        std::cout << "Indices: " << result[0] << ", " << result[1] << std::endl;
    }
    else {
        std::cout << "No solution found." << std::endl;
    }

    return 0;
}
