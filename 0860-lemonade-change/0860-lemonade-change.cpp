class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int fives = 0, tens = 0;
        int n = bills.size();
        for(int i=0; i<n; i++){
            if(bills[i]==5){
                fives++;
            }
            else if(bills[i]==10){
                fives--;
                tens++;
            }
            else{
                if(tens>0){
                    tens--; fives--;
                }
                else{
                    fives -= 3;
                }
            }
            if(fives<0){return false;}
        }
        return true;
    }
};