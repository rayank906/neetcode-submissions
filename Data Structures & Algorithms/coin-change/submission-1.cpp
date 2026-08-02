class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        /*
            dp[i] = minimum number of coins needed to build i
            to find that, loop through every coin, check for amount - coin
            and find how many coins is needed to build i

            1. build memo of size n+1
            2. init dp[0] = 0
            3. for i = 1 and above, 
                a. loop through all coins
                b. find dp[i-c] that minimizes number of coins used to reach dp[i]
                c. return dp[i] if not int_max else return -1
        */
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0;

        for (int i = 1; i < dp.size(); i++){
            for (int c : coins) {
                if (i - c >= 0 && dp[i - c] < amount + 1) {
                    dp[i] = min(dp[i], dp[i - c] + 1);
                }
            }
        }

        if (dp[amount] == amount + 1) return -1;

        return dp[amount];
    }
};
