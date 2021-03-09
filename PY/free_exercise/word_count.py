# [AWS]
# given a long string containing multiple words and delimeters (‘ ‘, ‘,’,’.’..), Count the words and find the word(s) with max counter


input_str = "given a long string containing multiple words and delimeters, Count the words and find the words with max counter." \
            "There delimeters include dot space and comma."

class Solution():
    def word_count(self, s): 
        sc = s.replace('. ', ' ')
        sc = sc.replace(', ', ' ')
        sc = sc.replace(',', ' ')
        sc = sc.replace('.', ' ')
        words = sc.split(' ')
        #print(words)

        wc = {}
        for w in words:
            if w in wc:
                wc[w] += 1
            else:
                wc[w] = 1

        print(wc)
        max_count = max([wc[k] for k in wc])
        max_words = [k for k in wc if wc[k]==max_count]
        return max_words



def test():
    S = Solution()
    ret = S.word_count(input_str)
    print(ret)


test()
