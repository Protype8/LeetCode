import math
class Solution:
  def minWindow(self, s: str, t: str) -> str:
    current_length = math.inf
    minimum = []
    current = []
    needed = [w for w in t]
    word_dict = {w:0 for w in t}
    original_count = {w:t.count(w) for w in t}
    left_pointer = 0
    right_pointer = 0
    while left_pointer < len(s):
      if(right_pointer < len(s)):
        current.append(s[right_pointer])
        try:
          word_dict[s[right_pointer]] += 1
          needed.remove(s[right_pointer])
        except:
          pass
      if (needed == []):
        deleted = ""
        while left_pointer < len(s):
          deleted = current.pop(0)
          left_pointer += 1
          if(deleted in t):
            word_dict[deleted] -= 1
            if(word_dict[deleted] == original_count[deleted]-1):
              break
        if (len(current) + 1 < current_length and len(current)+1 >= len(t)):
          minimum = [deleted] + current.copy()
          current_length = len(current)+1
        needed.append(deleted)
      elif(right_pointer >= len(s)):
        break
