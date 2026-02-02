# LineTrace Codebase Analysis

### File Structure Summary
- Total Files: 127
- Total Directories: 60
- File Extensions: .md: 14, .png: 71, .py: 38, .java: 1, .go: 2

### Directory Tree
```
  ├── LICENSE
  ├── Roadmap
   │  ├── LeetCode.md
   │  └── Roadmap.md
  ├── LeetCode
   │  ├── 15. 3Sum
   │  │  ├── 3Sum.png
   │  │  └── 3Sum.py
   │  ├── 169. Majority Element
   │  │  ├── majorityElement.py
   │  │  ├── majorityElement.png
   │  │  └── majorElement_2.py
   │  ├── 345. Reverse Vowels of a String
   │  │  ├── reverseVowels.png
   │  │  └── reverseVowels.py
   │  ├── 53. Maximum Subarray
   │  │  ├── maxSubArray.png
   │  │  ├── maxSubArray.py
   │  │  └── maxSubArray.java
   │  ├── 58. Length of Last Word
   │  │  ├── lengthOfLastWord.png
   │  │  ├── lengthOfLastWord.py
   │  │  └── lengthOfLastWord.go
   │  ├── 167. Two Sum II - Input Array Is Sorted
   │  │  ├── twoSum.png
   │  │  └── twoSum.py
   │  ├── 1. Two Sum
   │  │  ├── twoSum.png
   │  │  └── twoSum.py
   │  ├── 9. Palindrome Number
   │  │  ├── palindromeNumber.png
   │  │  └── palindromeNumber.py
   │  ├── 344. Reverse String
   │  │  ├── reverseString.py
   │  │  └── reverseString.png
   │  ├── 680. Valid Palindrome II
   │  │  ├── validPalindrome.py
   │  │  └── validPalindrome.png
   │  ├── 217. Contains Duplicate
   │  │  ├── containsDuplicate.png
   │  │  └── containsDuplicate.py
   │  ├── 605. Can Place Flowers
   │  │  ├── canPlaceFlowers.py
   │  │  └── canPlaceFlowers.png
   │  ├── 121. Best Time to Buy and Sell Stock
   │  │  ├── maxProfit.png
   │  │  └── maxProfit.py
   │  ├── 1768. Merge Strings Alternately
   │  │  ├── mergeAlternately.png
   │  │  └── mergeAlternately.py
   │  ├── 14. Longest Common Prefix
   │  │  ├── longestCommonPrefix.png
   │  │  ├── longestCommonPrefix.py
   │  │  └── longestCommonPrefix.go
   │  ├── 560. Subarray Sum Equals K
   │  │  ├── subarraySum.py
   │  │  └── subarraySum.png
   │  ├── 1071. Greatest Common Divisor of Strings
   │  │  ├── gcdOfStrings.py
   │  │  └── gcdOfStrings.png
   │  ├── 238. Product of Array Except Self
   │  │  ├── productExceptSelf.png
   │  │  └── productExceptSelf.py
   │  ├── 151. Reverse Words in a String
   │  │  ├── reverseWords.py
   │  │  └── reverseWords.png
   │  ├── 876. Middle of the Linked List
   │  │  ├── middleNode.py
   │  │  └── middleNode.png
   │  ├── 13. Roman to Integer
   │  │  ├── romanToInteger.py
   │  │  └── romanToInteger.png
   │  ├── 1431. Kids With the Greatest Number of Candies
   │  │  ├── kidsWithCandies.py
   │  │  └── kidsWithCandies.png
   │  └── 125. Valid Palindrome
   │    ├── validPalindrome.py
   │    └── validPalindrome.png
  ├── reCode
   │  ├── 169. Majority Element
   │  │  ├── majorityElement.py
   │  │  ├── majorityElement.png
   │  │  └── majorElement_2.py
   │  ├── 121. Best Time to Buy and Sell Stock
   │  │  ├── maxProfit.png
   │  │  └── maxProfit.py
   │  ├── 560. Subarray Sum Equals K
   │  │  ├── subarraySum.py
   │  │  └── subarraySum.png
   │  └── 1071. Greatest Common Divisor of Strings
   │    ├── gcdOfStrings.py
   │    └── gcdOfStrings.png
  ├── README.md
  ├── DesignPatterns
   │  ├── Creational
   │  │  ├── Singleton
   │  │  │  ├── Readme.md
   │  │  │  └── singleton.py
   │  │  └── Factory
   │  │    ├── factory.py
   │  │    └── Readme.md
   │  ├── Behavioral
   │  └── Structural
  ├── Arrays
   │  ├── 1. containsDuplicates
   │  │  ├── Contains Duplicate.png
   │  │  └── Contains Duplicate.py
   │  ├── 3. findDisappearNumbers
   │  │  ├── Find Disappear Numbers.py
   │  │  └── Find Disappear Numbers.png
   │  ├── 6. minTimeToVisitAllPoints
   │  │  ├── Min Time To Visit All Points.py
   │  │  └── Min Time To Visit All Points.png
   │  ├── 5. smallerNumbersThanCurrent
   │  │  ├── Smaller Numbers Than Current.png
   │  │  └── Smaller Numbers Than Current.py
   │  ├── 4. twoSum
   │  │  ├── Two Sum.png
   │  │  └── Two Sum.py
   │  ├── 7. spiralOrder
   │  │  ├── Spiral Matrix.py
   │  │  └── Spiral Matrix.png
   │  └── 2. missingNumber
   │    ├── Missing Number.png
   │    └── Missing Number.py
  ├── LineTrace.md
  ├── GEMINI.md
  ├── AGENTS.md
  ├── CLAUDE.md
  └── SystemDesign
     ├── systemDesignFlow.png
     ├── Breakdown
      │  ├── Uber
      │  │  └── designUber.md
      │  └── assets
      │    └── uber
      │       ├── Geohasing.png
      │       ├── QuadTrees.png
      │       ├── HighLevel.png
      │       └── uber.png
     ├── Data Modelling
      │  ├── dataModelling.md
      │  └── assets
      │    ├── Scaling and Sharding.png
      │    ├── Wide Column DB.png
      │    ├── Relational DB.png
      │    ├── Normalization vs Denormalization.png
      │    ├── Entities, Key & Relationships.png
      │    ├── Indexing.png
      │    ├── Graph DB.png
      │    ├── Wrapping up.png
      │    ├── Key Value.png
      │    └── Document DB.png
     ├── CAP Theorem
      │  └── CAP.md
     ├── Caching
      │  ├── Caching.md
      │  └── assets
      │    ├── Where to cache
      │     │  ├── External Caching.png
      │     │  ├── Client-side Caching.png
      │     │  ├── CDN.png
      │     │  └── In-Process Caching.png
      │    ├── Common Issues
      │     │  ├── 2. Cache Consistency.png
      │     │  ├── 3. Hot Keys.png
      │     │  └── 1. Cache Stampede (Thundering Herd).png
      │    ├── Cache Eviction Policies
      │     │  └── Cache Eviction Policies.png
      │    ├── Cache Architecture
      │     │  ├── 4. Read-through.png
      │     │  ├── 2. Write-through.png
      │     │  ├── 1. Cache-Aside.png
      │     │  └── 3. Write-behind.png
      │    ├── When to Bring Up Caching.png
      │    └── Caching.png
     └── API Design
        ├── apiDesign.md
        └── assets
           ├── HTTP Methods.png
           ├── Pagination.png
           ├── GraphQL.png
           ├── API.png
           ├── REST.png
           ├── RPC.png
           ├── Security.png
           └── Responses.png
```

