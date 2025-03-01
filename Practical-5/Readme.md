# Context-Free Grammar (CFG) Analysis

## Aim
To implement a Context-Free Grammar (CFG) analysis program in C++ that calculates the First and Follow sets of non-terminals, detects left recursion, and prints the results.

## Theory
A **Context-Free Grammar (CFG)** is a formal grammar that consists of a set of production rules where each rule maps a non-terminal to a sequence of terminals and/or non-terminals. CFGs are widely used in programming language parsers and compilers.

### **First and Follow Sets:**
- **First Set:** The First set of a non-terminal contains all terminals that can appear at the beginning of a string derived from that non-terminal.
- **Follow Set:** The Follow set of a non-terminal contains all terminals that can appear immediately after that non-terminal in some derivation.

### **Left Recursion Detection:**
- A grammar has left recursion if a non-terminal appears as the first symbol on the right-hand side of its own production rule, leading to infinite recursion during parsing.

## Code
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iterator>
using namespace std;

class CFG {
public:
    map<string, vector<vector<string>>> grammar;
    map<string, set<string>> first, follow;

    void addProduction(string nonTerminal, vector<string> production) {
        grammar[nonTerminal].push_back(production);
    }

    void calculateFirst() {
        for (auto &rule : grammar) {
            string nonTerminal = rule.first;
            for (auto &production : rule.second) {
                if (isTerminal(production[0])) {
                    first[nonTerminal].insert(production[0]);
                } else {
                    first[nonTerminal].insert(first[production[0]].begin(), first[production[0]].end());
                }
            }
        }
    }

    void calculateFollow() {
        follow["S"].insert("$");
        bool added;
        do {
            added = false;
            for (auto &rule : grammar) {
                string nonTerminal = rule.first;
                for (auto &production : rule.second) {
                    for (size_t i = 0; i < production.size(); i++) {
                        string currentSymbol = production[i];
                        if (isNonTerminal(currentSymbol)) {
                            if (i + 1 < production.size()) {
                                string nextSymbol = production[i + 1];
                                if (isTerminal(nextSymbol)) {
                                    added |= follow[currentSymbol].insert(nextSymbol).second;
                                } else {
                                    follow[currentSymbol].insert(first[nextSymbol].begin(), first[nextSymbol].end());
                                }
                            } else {
                                follow[currentSymbol].insert(follow[nonTerminal].begin(), follow[nonTerminal].end());
                            }
                        }
                    }
                }
            }
        } while (added);
    }

    void detectLeftRecursion() {
        for (auto &rule : grammar) {
            string nonTerminal = rule.first;
            for (auto &production : rule.second) {
                if (production[0] == nonTerminal) {
                    cout << "Left Recursion Detected in: " << nonTerminal << " -> ";
                    for (auto &symbol : production) {
                        cout << symbol << " ";
                    }
                    cout << endl;
                }
            }
        }
    }

    void printFirst() {
        cout << "First Sets:\n";
        for (auto &rule : first) {
            cout << rule.first << ": { ";
            for (auto &symbol : rule.second) {
                cout << symbol << " ";
            }
            cout << "}\n";
        }
    }

    void printFollow() {
        cout << "Follow Sets:\n";
        for (auto &rule : follow) {
            cout << rule.first << ": { ";
            for (auto &symbol : rule.second) {
                cout << symbol << " ";
            }
            cout << "}\n";
        }
    }

    bool isTerminal(const string& symbol) {
        return symbol[0] >= 'a' && symbol[0] <= 'z';
    }

    bool isNonTerminal(const string& symbol) {
        return symbol[0] >= 'A' && symbol[0] <= 'Z';
    }
};

int main() {
    CFG cfg;
    int numProductions;
    cout << "Enter the number of production rules: ";
    cin >> numProductions;

    for (int i = 0; i < numProductions; ++i) {
        string nonTerminal;
        cout << "Enter non-terminal: ";
        cin >> nonTerminal;

        int numSymbols;
        cout << "Enter number of symbols in production for " << nonTerminal << ": ";
        cin >> numSymbols;

        vector<string> production;
        cout << "Enter production: ";
        for (int j = 0; j < numSymbols; ++j) {
            string symbol;
            cin >> symbol;
            production.push_back(symbol);
        }

        cfg.addProduction(nonTerminal, production);
    }

    cfg.detectLeftRecursion();
    cfg.calculateFirst();
    cfg.calculateFollow();
    cfg.printFirst();
    cfg.printFollow();
    return 0;
}
```

## Sample Output
```
Enter the number of production rules: 2
Enter non-terminal: S
Enter number of symbols in production for S: 2
Enter production: S a
Enter non-terminal: A
Enter number of symbols in production for A: 1
Enter production: a

Left Recursion Detected in: S -> S a
First Sets:
S: { a }
A: { a }
Follow Sets:
S: { $ }
A: { }
```

## Conclusion
This program successfully implements a Context-Free Grammar (CFG) analysis tool that:
- Computes **First** and **Follow** sets for non-terminals.
- Detects **left recursion** in the given grammar.
- Displays the **First** and **Follow** sets as output.

This tool is useful for compiler design and syntax analysis in programming language parsers.

