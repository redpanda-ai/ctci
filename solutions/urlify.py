class Solution:
    def solver(self, in_s, string_length):
        in_string = list(in_s)
        i = string_length  # runner
        j = len(in_string) - 1  # placer

        while i > 0:
            c = in_string[i]
            if c == ' ':
                in_string[j] = '0'
                in_string[j - 1] = '2'
                in_string[j - 2] = '%'
                j -= 3
            else:
                in_string[j] = in_string[i]
                j -= 1
            i -= 1

        return "".join(in_string)



s = Solution()
my_solution = s.solver("Mr. John Smith    ", 13)
print(f"My solution: {my_solution}")