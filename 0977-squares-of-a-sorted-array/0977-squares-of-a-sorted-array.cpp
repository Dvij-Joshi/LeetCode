class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> nums1;
        int i,j=0;
        for(i=0;i<nums.size();i++){
            if(nums[i]<0){
                j++;
            }
            nums[i]=nums[i]*nums[i];
           
        }
        j=j-1;
        i=j+1;
        
        for(int k=0;k<nums.size();k++){
            if(j<0){
                // nums1[i]=nums[i];
                nums1.push_back(nums[i]);
                i++;
            }
            else if(i==nums.size()){
                nums1.push_back(nums[j]);
                j--;
            }
            else if(nums[i]<nums[j]){
                nums1.push_back(nums[i]);
                i++;
            }
            else{
                nums1.push_back(nums[j]);
                j--;
            }

        }
        
        
        return nums1;
    }
};