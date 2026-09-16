class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int bestsum = nums[0]+nums[1]+nums[2];
        for(int i=0;i<nums.size()-2;i++){
            int left = i+1;
            int right = nums.size()-1;
            while(left<right){
                int currentsum = nums[i]+nums[left]+nums[right];
                if(std::abs(currentsum-target)<std::abs(bestsum-target)){
                    bestsum = currentsum;
                }
                // if(currentsum==bestsum){
                //     return bestsum;
                // }
                if(currentsum < target){
                    left ++;
                }
                else{
                    right--;
                }
            }
        }
        return bestsum;
    }
};