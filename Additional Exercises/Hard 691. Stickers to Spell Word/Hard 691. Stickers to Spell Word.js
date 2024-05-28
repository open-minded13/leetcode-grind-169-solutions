// Date of Last Practice: Mar 26, 2024
// 
// Time Complexity: O(2^m * s * l * m), where m is the length of the target string,
//                  s is the number of stickers, and l is the average length of a sticker.
//
//                  There are 2^m possible states where m is the length of the target string.
//                  For each state, we iterate over all stickers. 
//                  For each sticker, we iterate over its characters. 
//                  For each character in the sticker, we iterate over the target string of length m.
// 
// Space Complexity: O(2^m), where m is the length of the target string.

var minStickers = function (stickers, target) {
    const targetLength = target.length
    const numOfStates = 1 << targetLength       // 2^targetLength possible states
    const dp = Array(numOfStates).fill(Infinity)
    dp[0] = 0                                   // Base case: 0 stickers needed for empty target

    for (let state = 0; state < numOfStates; state++) {
        if (dp[state] === Infinity) continue    // Skip unreachable states

        for (const sticker of stickers) {
            let now = state                     // Current state before applying the sticker
            for (const char of sticker) {       // Try applying each character of the sticker
                for (let i = 0; i < targetLength; i++) {
                    if (char === target[i] && ((now >> i) & 1) === 0) {
                        now |= 1 << i           // Update state to cover this character
                        break                   // Move to the next character in the sticker
                    }
                }
            }
            dp[now] = Math.min(dp[now], dp[state] + 1) // Update DP table
        }
    }

    return dp[numOfStates - 1] === Infinity ? -1 : dp[numOfStates - 1]
};

module.exports = minStickers