# A bare-bones implementation of a edge weighted graph via its adjacency list
class WeightedGraph:
	def __init__(self, A:list[list[tuple[int]]]) -> None:
		self.adjacency_list = A
		self.n_vertices = len(A)

	def __repr__(self) -> str:
		return f"An edge-weighted graph with adjacency list:\n{self.adjacency_list}"
	
	# An implementation of Dijkstra's algorithm
	def shortest_path(self, start:int, finish:int) -> list[int]:
		# Setup
		infinity = float("infinity")		# A float larger than all reals
		seen = [False]*(self.n_vertices)	# Same as BFS/DFS
		path = []							# We return this

		# Our table of weights
		weights = [infinity]*(self.n_vertices)
		weights[start] = 0					# Since we start at start

		# Initialize
		next_verts = [(start, 0)]

		# At each stage, move to cheapest vertex v.
		# If v is our target, we're done.
		# Otherwise, we make sure we don't come back, and we update weights.
		while len(next_verts) > 0:
			v, _ = min(next_verts, key=lambda tup: tup[1])
			path.append(v)
			if v == finish:		# If this is never true and we leave the loop
				return path		# then we know there is no path start -> finish!
			seen[v] = True
			next_verts = [t for t in self.adjacency_list[v] if not seen[t[0]]]
			for n_vert, n_weight in next_verts:
				weights[n_vert] = min(weights[v] + n_weight, weights[n_vert])
		print(f"No path from vertex {start} to {finish}!")


if __name__ == "__main__":
	G = WeightedGraph([
		[(1, 6), (2, 2)],
		[(3, 1)],
		[(1, 3), (3, 6)],
		[]
	])
	print(f"{G}\n")
	print(G.shortest_path(0, 3))

	print()
	H = WeightedGraph([
		[(1, 6), (2, 2)],
		[(3, 1), (4, 2)],
		[(1, 3), (3, 6)],
		[],
		[(3, 10)]
	])
	print(f"{H}\n")
	print(H.shortest_path(0, 3))