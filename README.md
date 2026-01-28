# ⚡️ The Engineering Blueprint

<div align="center">

![Language](https://img.shields.io/badge/Language-Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Language](https://img.shields.io/badge/Language-Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Problems Solved](https://img.shields.io/badge/Solved-20-green?style=for-the-badge)
![Patterns](https://img.shields.io/badge/Patterns-2-blueviolet?style=for-the-badge)
![Systems](https://img.shields.io/badge/Systems-2-ff69b4?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

**A comprehensive repository mastering Data Structures, Algorithms, System Design, and Design Patterns.**

[Algorithms](#-algorithms--leetcode) • [System Design](#-system-design) • [Design Patterns](#-design-patterns) • [Getting Started](#-getting-started)

</div>

---

## 📖 About

This repository serves as a personal knowledge base and professional portfolio, documenting a journey through the core pillars of Software Engineering. It is strictly maintained with a focus on **clean code**, **scalability**, and **performance**.

**Key Focus Areas:**
- 🧠 **Algorithms:** High-performance solutions for LeetCode problems with Time/Space complexity analysis.
- 🏗️ **System Design:** Deep dives into real-world distributed systems and architectural breakdowns.
- 🎨 **Design Patterns:** Idiomatic implementations of GoF patterns in Python and Go.

---

## 📂 Repository Architecture

The codebase is organized into three primary modules, ensuring intuitive navigation and separation of concerns.

```text
/
├── LeetCode/                  # 🧩 Algorithms & Data Structures
│   ├── 1. Two Sum/            # Optimized Solutions
│   ├── 15. 3Sum/
│   └── ...
├── SystemDesign/              # ☁️ Distributed Systems Architecture
│   ├── CAP Theorem/           # Fundamental Concepts: CAP Theorem
│   └── Breakdown/
│       └── Uber/              # Case Study: Design Uber
├── DesignPatterns/            # 📐 Object-Oriented Design Patterns
│   ├── Creational/            # Factory, Singleton, etc.
│   ├── Behavioral/
│   └── Structural/
└── README.md
```

---

## 🧩 Algorithms & LeetCode

A collection of strictly typed, efficient solutions.

|  #  | Problem Title | Difficulty | Solution | Topic Tags |
| :--: | :--- | :---: | :---: | :--- |
| 0001 | **Two Sum** | 🟢 Easy | [Python](./LeetCode/1.%20Two%20Sum/twoSum.py) | Array, Hash Table |
| 0009 | **Palindrome Number** | 🟢 Easy | [Python](./LeetCode/9.%20Palindrome%20Number/palindromeNumber.py) | Math |
| 0013 | **Roman to Integer** | 🟢 Easy | [Python](./LeetCode/13.%20Roman%20to%20Integer/romanToInteger.py) | Hash Table, Math |
| 0014 | **Longest Common Prefix** | 🟢 Easy | [Python](./LeetCode/14.%20Longest%20Common%20Prefix/longestCommonPrefix.py), [Go](./LeetCode/14.%20Longest%20Common%20Prefix/longestCommonPrefix.go) | String |
| 0015 | **3Sum** | 🟡 Medium | [Python](./LeetCode/15.%203Sum/3Sum.py) | Array, Two Pointers |
| 0053 | **Maximum Subarray** | 🟡 Medium | [Python](./LeetCode/53.%20Maximum%20Subarray/maxSubArray.py), [Java](./LeetCode/53.%20Maximum%20Subarray/maxSubArray.java) | Array, Dynamic Programming, Divide and Conquer |
| 0058 | **Length of Last Word** | 🟢 Easy | [Python](./LeetCode/58.%20Length%20of%20Last%20Word/lengthOfLastWord.py), [Go](./LeetCode/58.%20Length%20of%20Last%20Word/lengthOfLastWord.go) | String |
| 0125 | **Valid Palindrome** | 🟢 Easy | [Python](./LeetCode/125.%20Valid%20Palindrome/validPalindrome.py) | Two Pointers, String |
| 0151 | **Reverse Words in a String** | 🟡 Medium | [Python](./LeetCode/151.%20Reverse%20Words%20in%20a%20String/reverseWords.py) | String, Two Pointers |
| 0167 | **Two Sum II - Input Array Is Sorted** | 🟡 Medium | [Python](./LeetCode/167.%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted/twoSum.py) | Array, Two Pointers |
| 0217 | **Contains Duplicate** | 🟢 Easy | [Python](./LeetCode/217.%20Contains%20Duplicate/containsDuplicate.py) | Array, Hash Table |
| 0238 | **Product of Array Except Self** | 🟡 Medium | [Python](./LeetCode/238.%20Product%20of%20Array%20Except%20Self/productExceptSelf.py) | Array, Prefix Sum |
| 0344 | **Reverse String** | 🟢 Easy | [Python](./LeetCode/344.%20Reverse%20String/reverseString.py) | Two Pointers, String |
| 0345 | **Reverse Vowels of a String** | 🟢 Easy | [Python](./LeetCode/345.%20Reverse%20Vowels%20of%20a%20String/reverseVowels.py) | Two Pointers, String |
| 0560 | **Subarray Sum Equals K** | 🟡 Medium | [Python](./LeetCode/560.%20Subarray%20Sum%20Equals%20K/subarraySum.py) | Array, Hash Table, Prefix Sum |
| 0605 | **Can Place Flowers** | 🟢 Easy | [Python](./LeetCode/605.%20Can%20Place%20Flowers/canPlaceFlowers.py) | Array, Greedy |
| 0680 | **Valid Palindrome II** | 🟢 Easy | [Python](./LeetCode/680.%20Valid%20Palindrome%20II/validPalindrome.py) | String, Two Pointers |
| 0876 | **Middle of the Linked List** | 🟢 Easy | [Python](./LeetCode/876.%20Middle%20of%20the%20Linked%20List/middleNode.py) | Linked List, Two Pointers |
| 1071 | **Greatest Common Divisor of Strings** | 🟢 Easy | [Python](./LeetCode/1071.%20Greatest%20Common%20Divisor%20of%20Strings/gcdOfStrings.py) | Math, String |
| 1431 | **Kids With the Greatest Number of Candies** | 🟢 Easy | [Python](./LeetCode/1431.%20Kids%20With%20the%20Greatest%20Number%20of%20Candies/kidsWithCandies.py) | Array |
| 1768 | **Merge Strings Alternately** | 🟢 Easy | [Python](./LeetCode/1768.%20Merge%20Strings%20Alternately/mergeAlternately.py) | Two Pointers, String |

---

## ☁️ System Design

Architectural breakdowns of complex distributed systems, focusing on scalability, reliability, and maintainability.

### 📜 **[CAP Theorem](./SystemDesign/%20CAP%20Theorem/CAP.md)**
Analysis of the fundamental trade-offs in distributed systems.
- **Core Concepts:** Consistency, Availability, and Partition Tolerance.
- **Trade-offs:** Exploring CA, AP, and CP configurations.
- **Real-world Examples:** Insights into DynamoDB and Google Spanner.

### 🔌 **[API Design](./SystemDesign/API%20Design/apiDesign.md)**
Principles of building effective APIs.
- **Styles:** REST, GraphQL, RPC.
- **Key Concepts:** Pagination, Rate Limiting, Security, Versioning.

### 💾 **[Data Modelling](./SystemDesign/Data%20Modelling/dataModelling.md)**
Techniques for efficient data storage and retrieval.
- **Models:** Relational vs. NoSQL (Document, Graph, Key-Value).
- **Optimization:** Indexing, Normalization vs. Denormalization.

### 🚗 **[Design Uber](./SystemDesign/Breakdown/Uber/designUber.md)**
A comprehensive analysis of a ride-sharing platform.
- **Core Requirement:** Real-time driver matching & location tracking.
- **Key Constraints:** Low latency, high consistency, heavy write throughput.
- **Diagrams:** High-level architecture, database schema, and component interactions.

---

## 📐 Design Patterns

Implementation of standard GoF design patterns to solve common software design problems.

### **Creational Patterns**
Mechanisms for object creation that increase flexibility and reuse of existing code.

- **[Factory Method](./DesignPatterns/Creational/Factory/Readme.md):**  Defines an interface for creating an object, but lets subclasses alter the type of objects that will be created.
- **[Singleton](./DesignPatterns/Creational/Singleton/Readme.md):** Ensures a class has only one instance and provides a global point of access to it.

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.8+**
- **Go 1.20+** (Optional)
- **Java 11+** (Optional)

### Running a Solution
Navigate to the specific directory and execute the script.

```bash
# Run a Python solution
cd "LeetCode/1. Two Sum"
python3 twoSum.py

# Run a Go solution
cd "LeetCode/14. Longest Common Prefix"
go run longestCommonPrefix.go

# Run a Java solution
cd "LeetCode/53. Maximum Subarray"
javac maxSubArray.java && java Solution
```

---

## 🤝 Contributing

Contributions are strictly regulated to maintain quality.

1. **Fork** the repository.
2. Create a **Feature Branch** (`git checkout -b feature/NewSystemDesign`).
3. **Commit** your changes with meaningful messages.
4. **Push** and Open a **Pull Request**.

---

<div align="center">
  <p><b>Crafted with ❤️ by Kushal Banda</b></p>
  <p><i>Building the future, one line of code at a time.</i></p>
</div>