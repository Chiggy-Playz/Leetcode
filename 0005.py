def longestPalindrome(s: str) -> str:
            res = ""

            for j in range(len(s)-1, -1, -1):
                if s[j] not in s[:j]:
                    continue
                i = 0
                while i < j:
                    if s[i] != s[j]:
                        i += 1
                        continue
                    substr = s[i:j+1]
                    if substr == substr[::-1] and len(substr) > len(res):
                        res = substr
                        break
                    i+=1

            return res or s[0]
                

print(longestPalindrome("aacabdkacaa"))