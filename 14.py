class Solution:
    def longestCommonPrefix(self, strs) -> str:
        result = ''
        if strs:
            first_word = strs[0]

            if len(strs) == 1:
                return first_word

            for index, char in enumerate(first_word):
                for num, string in enumerate(strs[1:]):
                    print('index: ', index)
                    if index < len(string) and string[index] == first_word[index]:
                        if num == (len(strs)-2):
                            result += char
                    else:
                        return result
        return result


input1 = Solution()
input2 = Solution()
print('test1', input1.longestCommonPrefix(["flower", "flow", "flight"]))
print('test2', input2.longestCommonPrefix([["dog", "racecar", "car"]]))
