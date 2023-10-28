class Solution(object):
    def countVowelPermutation(self, n):
        MOD = 10**9 + 7
        
        # Initialize an array to store the count of valid strings for each vowel 'a', 'e', 'i', 'o', 'u'.
        dp = [1] * 5  # Initialize with 1 for each vowel of length 1
        
        # Define the rules for transitions between vowels.
        transitions = [
            [1],       # 'a' can be followed by 'e'
            [0, 2],    # 'e' can be followed by 'a' or 'i'
            [0, 1, 3, 4],  # 'i' can be followed by 'a', 'e', 'o', or 'u'
            [2, 4],    # 'o' can be followed by 'i' or 'u'
            [0]        # 'u' can be followed by 'a'
        ]
        
        # Perform dynamic programming to calculate the counts.
        for length in range(2, n + 1):
            new_dp = [0] * 5
            for current_vowel in range(5):
                for next_vowel in transitions[current_vowel]:
                    new_dp[current_vowel] = (new_dp[current_vowel] + dp[next_vowel]) % MOD
            dp = new_dp
        
        # Sum up the counts for all vowels of length 'n'.
        total_count = sum(dp) % MOD
        
        return total_count

# Example usage:
sol = Solution()
print(sol.countVowelPermutation(1))  # Output: 5
print(sol.countVowelPermutation(2))  # Output: 10
print(sol.countVowelPermutation(5))  # Output: 68
