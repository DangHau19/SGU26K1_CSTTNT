import collections
import matplotlib.pyplot as plt
import numpy as np

# --- 1. THUẬT TOÁN BFS ---
def solve_maze_thin_walls(rows, cols, walls, start, goal):
    queue = collections.deque([(start, [start])])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == goal: return path
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbor = (nr, nc)
                move_segment = tuple(sorted(((r, c), (nr, nc))))
                if move_segment not in walls and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
    return None

# 2. CẤU HÌNH MÊ CUNG 
ROWS = 6
COLS = 6
START = (0, 0)
GOAL = (5, 5)

# Danh sách vách ngăn
blocked_edges = [
    # --- Tường dọc (Ngăn cách Cột 1 và Cột 2) ---
    ((0, 1), (0, 2)),  # Hàng 0 (Sát biên trên)
    ((1, 1), (1, 2)),  # Hàng 1
    
    ((4, 1), (4, 2)),  # Hàng 4 (Dưới)
    ((5, 1), (5, 2)),  # Hàng 5 (Sát đáy)
    
    # --- Tường ngang (Ngăn cách Hàng 2 và Hàng 3) ---
    ((2, 4), (3, 4)),
    ((2, 5), (3, 5))
]

walls = set()
for u, v in blocked_edges:
    walls.add(tuple(sorted((u, v))))

# 3. CHẠY VÀ VẼ HÌNH
path = solve_maze_thin_walls(ROWS, COLS, walls, START, GOAL)

plt.figure(figsize=(6, 6))
ax = plt.gca()

# 1. Cài đặt trục chính (Major) để hiển thị SỐ (0, 1, 2...)
# Đặt tick tại vị trí 0, 1, 2, 3, 4, 5
ax.set_xticks(range(COLS))
ax.set_yticks(range(ROWS))

# 2. Cài đặt trục phụ (Minor) để vẽ LƯỚI (Grid)
# Đặt tick tại vị trí bán nguyên (-0.5, 0.5...) để lưới bao quanh ô
ax.set_xticks(np.arange(-0.5, COLS, 1), minor=True)
ax.set_yticks(np.arange(-0.5, ROWS, 1), minor=True)

# 3. Vẽ lưới dựa trên trục phụ (Minor)
ax.grid(which='minor', color='lightgray', linestyle='-', linewidth=1)

# 4. Tắt lưới ở trục chính (để không bị kẻ đè lên số) và tắt vạch tick thừa
ax.grid(which='major', visible=False) 
ax.tick_params(axis='both', which='both', length=0) # Tắt các vạch ngắn thò ra (tick marks)

# -------------------------------------------

# Vẽ tường
for (r1, c1), (r2, c2) in walls:
    if r1 == r2: # Tường dọc
        x = max(c1, c2) - 0.5
        plt.plot([x, x], [r1 - 0.5, r1 + 0.5], 'k-', linewidth=5)
    elif c1 == c2: # Tường ngang
        y = max(r1, r2) - 0.5
        plt.plot([c1 - 0.5, c1 + 0.5], [y, y], 'k-', linewidth=5)

# Vẽ đường đi
if path:
    print(f"Đã tìm thấy đường đi ({len(path)} bước).")
    py = [p[0] for p in path]
    px = [p[1] for p in path]
    plt.plot(px, py, 'r-o', linewidth=3, markersize=8, label='Đường đi')
else:
    print("Không tìm thấy đường đi!")

# Start / Goal
plt.text(START[1], START[0], 'S', color='green', fontweight='bold', ha='center', va='center', fontsize=14)
plt.text(GOAL[1], GOAL[0], 'G', color='blue', fontweight='bold', ha='center', va='center', fontsize=14)

plt.gca().invert_yaxis() # Đảo trục Y
plt.title("Đường đi của Kiến (Có trục số)", fontsize=14)
plt.show()