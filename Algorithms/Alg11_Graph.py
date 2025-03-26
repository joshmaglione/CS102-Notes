# An implementation of a graph via its adjacency list
class Graph:
	def __init__(self, A:list[list[int]]) -> None:
		self.adjacency_list = A
		self.n_vertices = len(A)

	def __repr__(self) -> str:
		return f"A graph with adjacency list:\n{self.adjacency_list}"
	
	def add_edge(self, i:int, j:int) -> None:
		if not j in self.adjacency_list[i]:
			self.adjacency_list[i].append(j)

	def remove_edge(self, i:int, j:int) -> None:
		if j in self.adjacency_list[i]:
			self.adjacency_list[i].remove(j)

	def has_edge(self, i:int, j:int) -> bool:
		return bool(j in self.adjacency_list[i])

	def out_edges(self, i:int) -> list[int]:
		return self.adjacency_list[i]

	def in_edges(self, j:int) -> list[int]:
		return [i for i, verts in enumerate(self.adjacency_list) if j in verts]


if __name__ == "__main__":
	G = Graph([
		[2, 4], 
		[2],
		[],
		[1, 2], 
		[]
	])
	print(f"{G}\n")

	# Test: add_edge
	print(f"We add the edge (4, 1).")
	G.add_edge(4, 1)
	print(f"{G}\n")

	# Test: remove_edge
	print(f"We remove the edge (0, 2).")
	G.remove_edge(0, 2)
	print(f"{G}\n")