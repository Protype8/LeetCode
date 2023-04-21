class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        string_length = len(s)
        length_list = []
        already_found = set([s[0]])
        current_end = s.rindex(s[0])
        print(current_end)
        counter = 1
        for i in range(string_length):
            if (s[i] not in already_found):
                i_end = s.rindex(s[i])
                if (i_end > current_end):
                    current_end = i_end
                    already_found.add(s[i])
            if (i == current_end):
                length_list.append(counter)
                counter = 0
            counter += 1
        return length_list
