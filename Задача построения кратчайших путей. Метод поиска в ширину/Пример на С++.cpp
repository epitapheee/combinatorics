#include <iostream>
#include <queue>
#include <unordered_set>
#include <vector>

using namespace std;

void bfs(vector<vector<int>> &graph, int start) {
	unordered_set<int> visited;
	queue<int> q;

	visited.insert(start);
	q.push(start);

	while (!q.empty()) {
		int vertex = q.front();
		cout << vertex << " ";
		q.pop();

		for (int neighbor : graph[vertex]) {
			if (visited.find(neighbor) == visited.end()) {
				visited.insert(neighbor);
				q.push(neighbor);
			}
		}
	}
}

int main() {
	vector<vector<int>> graph = {{1, 2}, {0, 3}, {0, 3}, {}, {}, {}};
	bfs(graph, 0);
	return 0;
}