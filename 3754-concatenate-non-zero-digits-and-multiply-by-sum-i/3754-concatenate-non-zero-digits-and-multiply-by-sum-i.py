class Solution:
    def sumAndMultiply(self, n: int) -> int:
        str_n = str(n)
        digit_sum = sum(int(d) for d in str_n)
        non_zero_digits = "".join(d for d in str_n if d != '0')
        concat_num = int(non_zero_digits) if non_zero_digits else 0
        return concat_num * digit_sum