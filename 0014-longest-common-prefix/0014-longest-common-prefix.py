class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        ref = strs[0]

        for ch_idx in range(len(ref)):
            cur_ch = ref[ch_idx]
            for word in strs[1:]:
                if ch_idx == len(word) or word[ch_idx] != cur_ch:
                    return ref[:ch_idx]
        return ref
