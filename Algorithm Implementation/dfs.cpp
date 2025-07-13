#include <iostream>
#include <stack>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

vector<int> dfs(unordered_map<int, vector<int>>& graph, int start, int goal) {
    stack<vector<int>> paths;
    unordered_set<int> visited;

    paths.push({start});

    while (!paths.empty()) {
        vector<int> current_path = paths.top();
        paths.pop();
        int last_node = current_path.back();

        if (last_node == goal) {
            return current_path;
        }

        if (visited.find(last_node) == visited.end()) {
            visited.insert(last_node);
        
            for (auto it = graph[last_node].rbegin(); it != graph[last_node].rend(); ++it) {
                int neighbor = *it;
                if (visited.find(neighbor) == visited.end()) {
                    vector<int> new_path = current_path;
                    new_path.push_back(neighbor);
                    paths.push(new_path);
                }
            }
        }
    }

    return {}; 
}

void printGraph(const unordered_map<int, vector<int>>& graph) {
    cout << "\nGraph structure:\n";
    for (const auto& pair : graph) {
        cout << pair.first << ": ";
        for (int neighbor : pair.second) {
            cout << neighbor << " ";
        }
        cout << endl;
    }
}

int main() {
    unordered_map<int, vector<int>> graph;
    int nodes, edges;

    cout << "Enter number of nodes: ";
    cin >> nodes;

    cout << "Enter number of edges: ";
    cin >> edges;

    cout << "Is the graph undirected? (1 for Yes, 0 for No): ";
    bool undirected;
    cin >> undirected;

    cout << "Enter edges (format: from to):\n";
    for (int i = 0; i < edges; i++) {
        int from, to;
        cin >> from >> to;
        graph[from].push_back(to);
        if (undirected) {
            graph[to].push_back(from);
        }
    }

    int start, goal;
    cout << "Enter start node: ";
    cin >> start;
    cout << "Enter goal node: ";
    cin >> goal;

    if (graph.find(start) == graph.end() || graph.find(goal) == graph.end()) {
        cout << "Error: Start or goal node not present in the graph!" << endl;
        return 1;
    }

    printGraph(graph); 

    vector<int> path = dfs(graph, start, goal);

    if (path.empty()) {
        cout << "No path found from " << start << " to " << goal << "." << endl;
    } else {
        cout << "DFS Path from " << start << " to " << goal << ": ";
        for (int node : path) {
            cout << node << " ";
        }
        cout << endl;
    }

    return 0;
}
