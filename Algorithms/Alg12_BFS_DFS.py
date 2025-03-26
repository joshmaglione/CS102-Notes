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

	def BFS(self, start:int=0) -> list[int]:
		"""
		Return the list of vertices traversed via a breadth-first search starting at vertex 0.
		"""
		vertices = []							# list to return
		queue = [start]							# the queue for searching		
		seen = [False]*(self.n_vertices)		# prevent duplicates
		seen[start] = True
		while len(queue) > 0:
			v = queue.pop(0)					# Pull from start
			vertices.append(v)
			for v_neighbor in self.adjacency_list[v]:
				if not seen[v_neighbor]:
					seen[v_neighbor] = True
					queue.append(v_neighbor)	# Add at end
		return vertices

if __name__ == "__main__":
	G = Graph([
		[1, 2, 3], 
		[4],
		[4, 5],
		[6, 7], 
		[8],
		[6], 
		[7],
		[],
		[]
	])
	print(f"{G}\n")

	print(G.BFS())