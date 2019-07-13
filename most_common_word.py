"""
819. Most Common Word
Easy

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.



Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.



Note:

    1 <= paragraph.length <= 1000.
    0 <= banned.length <= 100.
    1 <= banned[i].length <= 10.
    The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
    paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
    There are no hyphens or hyphenated words.
    Words only consist of letters, never apostrophes or other punctuation symbols.

"""
from typing import List
import re


class Solution:
    """ Questions:
        Does length refers to characters or words?
        Here I assume it refers to words. """

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        forbidden_list = ['!', '?', ',', ';', '.'] + banned
        paragraph = paragraph.lower()
        print(type(paragraph))

        for forb_item in forbidden_list:
            if forb_item in paragraph:
                paragraph = paragraph.replace(forb_item, '')

        paragraph = re.sub(r'\s{2,}', ' ', paragraph)
        paragraph = paragraph.rsplit(' ')

        if len(paragraph) > 1:
            rank: dict = {}
            for i in range(len(paragraph)):
                if paragraph.count(paragraph[i]) > len(paragraph) // 2:
                    return paragraph[i]
                elif paragraph.count(paragraph[i]) > 1:
                    rank[paragraph.count(paragraph[i])] = paragraph[i]

            if len(rank) > 0:
                return print(rank.get(max(rank.keys())))


common = Solution()
common.mostCommonWord('Hit the road Jack. Hit now', ['the', 'road'])
common.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit'])














