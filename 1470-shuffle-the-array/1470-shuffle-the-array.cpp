class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> ans(nums.size());
        int i=0,j=0,k=n;
        for(int i=0;i<k;i++){ //i = 0,i=1,2,
            ans[j]=nums[i]; //0 = 2,2=5,4=1,
            j++; // j=1,3,5,
            ans[j]=nums[n]; //1 = 3, 3=4,5=7
            n++; // n = 4,5
            j++; // j=2,4
               
        }
        return ans;// 2,3,5,4,1,7
    }
};