import java.util.*;

public class BFSExample {
	public static void main(String[] args) {
		Map<String, List<String>> graph = new HashMap<>();
		graph.put("A", Arrays.asList("B", "C"));
		graph.put("B", Arrays.asList("D", "E"));
		graph.put("C", Collections.singletonList("F"));
		graph.put("D", Collections.emptyList());
		graph.put("E", Collections.singletonList("F"));
		graph.put("F", Collections.emptyList());
		bfs(graph, "A");
	}

	private static void bfs(Map<String, List<String>> graph, String start) {
		Set<String> visited = new HashSet<>();
		Queue<String> queue = new LinkedList<>();

		visited.add(start);
		queue.offer(start);
		while (!queue.isEmpty()) {
			String vertex = queue.poll();
			System.out.print(vertex + " ");

			for (String neighbor : graph.getOrDefault(vertex, Collections.emptyList())) {
				if (!visited.contains(neighbor)) {
					visited.add(neighbor);
					queue.offer(neighbor);
				}
			}
		}
	}
}