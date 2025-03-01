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
