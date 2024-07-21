package internal

type Graph struct {
	visited []bool
	graph   [][]int
}

func newGraph(edges int, graph [][]int) *Graph {
	return &Graph{
		visited: make([]bool, edges),
		graph:   graph,
	}
}

func (g *Graph) dfs(curr int) {
	g.visited[curr] = true

	for _, key := range g.graph[curr] {
		if !g.visited[key] {
			g.dfs(key)
		}
	}
}

func CanVisitAllRooms(rooms [][]int) bool {
	g := newGraph(len(rooms), rooms)
	g.dfs(0)

	for _, j := range g.visited {
		if !j {
			return false
		}
	}
	return true
}
