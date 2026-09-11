class Solution:
    def fullJustify(self, words, maxWidth):
        ans = []
        i = 0

        while i < len(words):
            j = i
            total_length = 0

            while (j < len(words) and
                   total_length + len(words[j]) + (j - i) <= maxWidth):

                total_length += len(words[j])
                j += 1

            num_words = j - i

            spaces = maxWidth - total_length

        
            if j == len(words) or num_words == 1:

                line = " ".join(words[i:j])

                # Remaining spaces go at the end
                line += " " * (maxWidth - len(line))

            else:

                gaps = num_words - 1

                spaces_each = spaces // gaps

                extra_spaces = spaces % gaps

                line = ""

                for k in range(i, j):

                    line += words[k]

                    if k < j - 1:

                
                        gap_spaces = spaces_each

                        if k - i < extra_spaces:
                            gap_spaces += 1

                        line += " " * gap_spaces

            ans.append(line)

            i = j

        return ans