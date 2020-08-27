from heapq import heappop, heappush
from random import randrange
from math import inf

# ------------------
# SORTING ALGORITHMS
# ------------------

# BUBBLE SORT
	# 1) for i = 0 to len(array)
	# 2) for j = 0 to len(array) - i - i
	# 3) comparission (> or <)
	# 4) swap if ^^^
def bubble_sort(items):
	for i in range(len(items)):
		for j in range(len(items) - i - 1):
			if items[j] > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j]

# SELECTION SORT
def selection_sort(items):
	for i in range(len(items)):
		min_idx = i
		min_val = items[min_idx]
		for j in range(i+1, len(items)):
			if items[j] < min_val:
				min_idx = j
				min_val = items[j]
		items[i], items[min_idx] = items[min_idx], items[i]

# INSERTION SORT
def insertion_sort(items):
	for i in range(1, len(items)):
		item = items[i]
		j = i 
		while j > 0 and item < items[j-1]:
			items[j], items[j-1] = items[j-1],items[j]
			j-= 1

# MERGE SORT
	# 1) base case: len(array) <= 1
	# 2) middle idx
	# 3) left/ right split
	# 4) recursive call with ^^^
	# 5) merge both sorted lists
def merge_sort(items):
	if len(items) <= 1:
		return items

	middle = len(items)//2

	left_split = items[:middle]
	right_split = items[middle:]

	left_sorted = merge_sort(left_split)
	right_sorted = merge_sort(right_split)

	return merge(left_sorted, right_sorted)

def merge(left, right):
	result = []

	while left and right:
		if left[0] < right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))

	if left:
		result += left
	if right:
		result += right

	return result

# QUICKSORT
	# base case: start >= end
	# random pivot idx and item
	# swap pivot element with last element
	# pointer = start
	# for i = start to end
	# comparission with pivot
	# if ^^^ swap item with pointer
	# pointer ++
	# swap pointer with last element (pivot)
	# recursive call with left/ right pivot
def quicksort(items, start, end):
	if start >= end:
		return

	pivot_idx = randrange(start, end + 1)
	pivot_item = items[pivot_idx]

	items[pivot_idx], items[end] = items[end], items[pivot_idx]

	pointer = start

	for i in range(start, end):
		if items[i] < pivot_item:
			items[i], items[pointer] = items[pointer], items[i]
			pointer += 1

	items[pointer], items[end] = items[end], items[pointer]

	quicksort(items, start, pointer - 1)
	quicksort(items, pointer + 1, end)

# RADIX SORT
	# max element in array
	# 
def radix_sort(items):
	max_number = max(items)
	loops = len(str(max_number))

	for loop in range(loops):
		digits = [[] for i in range(10)]
		idx = -(loop + 1) 

		for item in items:

			str_item = str(item)

			try:
				digit = int(str_item[idx])
			except IndexError:
				digit = 0

			digits[digit].append(item)

		items.clear()
		for numeral in digits:
			items.extend(numeral)

# --------------------
# SEARCHING ALGORITHMS
# --------------------

# LINEAR SEARCH
def linear_search(items, target):
	for i in range(len(items)):
		if items[i] == target:
			return i
	return -1

# BINARY SEARCH
def binary_search(items, target):
	start = 0
	end = len(items) - 1

	while start <= end:
		middle_idx = (start + end) // 2
		middle_item = items[middle_idx]

		if middle_item == target:
			return middle_idx
		elif middle_item > target:
			end = middle_idx - 1
		elif middle_item < target:
			start = middle_idx + 1

	return -1
	

# -----------------
# GRAPHS ALGORITHMS
# -----------------

# DEPTH FIRST SEARCH (DFS)
def dfs(graph, current_vertex, target, visited=None):
	if not visited:
		visited = []

	visited.append(current_vertex)

	if current_vertex == target:
		return visited

	for neighbor in graph[current_vertex]:
		if neighbor not in visited:
			path = dfs(graph, neighbor, target, visited)

			if path:
				return path

# BREDTH FIRST SEARCH (BFS)
def bfs(graph, start, target):
	path = [start]
	vertex_and_path = [start, path]
	queue = [vertex_and_path]
	visited = set()

	while queue:
		current_vertex, path = queue.pop(0)
		visited.add(current_vertex)

		for neighbor in graph[current_vertex]:
			if neighbor not in visited:
				if neighbor == target:
					return path + [neighbor]
				else:
					queue.append([neighbor, path + [neighbor]])

# DIJKSTRA'S
def dijkstras(graph, start):
	distances = {}

	for vertex in graph:
		distances[vertex] = inf

	distances[start] = 0
	vertices_and_distances = [(start, 0)]

	while vertices_and_distances:
		current_vertex, current_distance = heappop(vertices_and_distances)

		for neighbor, edge_weight in graph[current_vertex]:
			new_distance = current_distance + edge_weight

			if new_distance < distances[neighbor]:
				distances[neighbor] = new_distance
				heappush(vertices_and_distances, (neighbor, new_distance))

	return distances

# A*
def a_star(graph, start, target):
	paths_and_distances = {}
	
	for vertex in graph:
		paths_and_distances[vertex] = [inf, [start.name]]
  
	paths_and_distances[start][0] = 0
	vertices_to_explore = [(0, start)]

	while vertices_to_explore:
		current_distance, current_vertex = heappop(vertices_to_explore)
    	
		for neighbor, edge_weight in graph[current_vertex]:
			new_distance = current_distance + edge_weight + manhattan_heuristic(neighbor, target)
			new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      
		if new_distance < paths_and_distances[neighbor][0]:
			paths_and_distances[neighbor][0] = new_distance
			paths_and_distances[neighbor][1] = new_path
			heappush(vertices_to_explore, (new_distance, neighbor))
  
	return paths_and_distances[target][1]

def manhattan_heuristic(start, target):
	x_distance = abs(start.x - target.x)
	y_distance = abs(start.y - target.y)
	return x_distance + y_distance

def euclidean_heuristic(start, target):
	x_distance = abs(start.x - target.x)
	y_distance = abs(start.y - target.y)
	return sqrt(x_distance**2, y_distance**2)


# -------------
# AI ALGORITHMS
# -------------

def minimax():
	pass

# ---------
# TEST AREA
# ---------












