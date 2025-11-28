class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check_text = []
        dict_symbol = {")": "(", "}": "{", "]": "["}
        if len(s)<=1:
            return False
        for i in s:
            if i in dict_symbol:
                if not check_text or dict_symbol[i] != check_text.pop():
                    return False
            else:
                check_text.append(i)
        return not check_text    