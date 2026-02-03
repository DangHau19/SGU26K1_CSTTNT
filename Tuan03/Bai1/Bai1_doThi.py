import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# --- 1. KHỞI TẠO DỮ LIỆU ---
adj_list = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'C', 'E', 'F'],
    'C': ['A', 'B', 'D', 'F'],
    'D': ['C', 'F'],
    'E': ['B', 'D', 'F'],
    'F': ['A', 'C', 'E']
}

# --- 2. TÍNH BẬC CỦA ĐỈNH ---
print("=== 1. THÔNG TIN BẬC CỦA CÁC ĐỈNH ===")
max_deg = -1
for node, neighbors in adj_list.items():
    deg = len(neighbors)
    print(f"- Đỉnh {node}: bậc {deg}")
    if deg > max_deg:
        max_deg = deg
print(f"-> Bậc cao nhất của đồ thị là: {max_deg}")
print("-" * 30)

# --- 3. TÌM ĐƯỜNG ĐI TỪ A ĐẾN D (THUẬT TOÁN BFS) ---
def bfs_find_path(graph, start, goal):
    queue = deque([[start]]) # Hàng đợi chứa các đường đi
    visited = {start}
    
    while queue:
        path = queue.popleft() # Lấy đường đi đầu tiên
        node = path[-1] # Lấy đỉnh hiện tại (cuối đường đi)
        
        if node == goal:
            return path # Trả về đường đi nếu tìm thấy đích
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

print("\n=== 2. TÌM ĐƯỜNG ĐI TỪ A -> D ===")
path = bfs_find_path(adj_list, 'A', 'D')
if path:
    print(f"Đường đi tìm được: {' -> '.join(path)}")
else:
    print("Không tìm thấy đường đi.")
print("-" * 30)

# --- 4. VẼ ĐỒ THỊ ---
print("\n=== 3. VẼ ĐỒ THỊ ===")
G = nx.Graph()
for node, neighbors in adj_list.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42) # Layout cố định để hình không bị nhảy
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='lightgreen')
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')
plt.title("Đồ thị Bài 1", fontsize=15)
plt.axis('off')
plt.show()