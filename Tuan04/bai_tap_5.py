import heapq
import pprint

# ============================================================================
# BÀI 1: BEST-FIRST SEARCH
# ============================================================================

# ============================================================================
# Phần 1: Biểu diễn đồ thị
# ============================================================================

# Biểu diễn bằng danh sách kề có trọng số
COST = {}
COST['A'] = {'C': 9, 'D': 7, 'E': 13, 'F': 20}
COST['B'] = {}
COST['C'] = {'H': 6}
COST['D'] = {'E': 4, 'H': 8}
COST['E'] = {'I': 3, 'K': 4}
COST['F'] = {'G': 4, 'I': 6}
COST['G'] = {}
COST['H'] = {'K': 5}
COST['I'] = {'B': 5, 'K': 9}
COST['K'] = {'B': 6}

print("=" * 80)
print("BIỂU DIỄN ĐỒ THỊ")
print("=" * 80)
print("\nDanh sách kề có trọng số:")
for vertex in sorted(COST.keys()):
    if COST[vertex]:
        print(f"{vertex}: {COST[vertex]}")
    else:
        print(f"{vertex}: []")

# MinHeap class
class MinHeap(object):
    def __init__(self):
        self.items = []
    
    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        heapq.heappush(self.items, item)
    
    def pop(self):
        item = heapq.heappop(self.items)
        return item
    
    def check(self, item):
        return item in self.items
    
    def update(self, item, new_item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items[i] = new_item
                heapq.heapify(self.items)

# Kiểm tra MinHeap
print("\n" + "=" * 80)
print("KIỂM TRA MINHEAP")
print("=" * 80)

items = [(10, "F"), (6, "B"), (8, "K"), (21, "A"), (9, "H")]
OPEN = MinHeap()

print("\nThứ tự thêm vào: ")
for item in items:
    OPEN.push(item)
    print(item, end=" ")

print("\n\nCập nhật (8, 'K') thành (1, 'K')")
OPEN.update((8, 'K'), (1, 'K'))

print("\nThứ tự lấy ra: ")
items_out = []
while OPEN.empty() == False:
    item = OPEN.pop()
    items_out.append(item)
    print(item, end=" ")
print()

# Hàm lấy danh sách kề
def LayKe(G, a):
    """
    Tìm danh sách đỉnh kề với a trong đồ thị G
    Return: None nếu a không tồn tại, [] nếu a không có đỉnh kề, [a1, a2, ...] nếu có
    """
    if G.get(a) is None:
        result = None
    else:
        result = []
        for b in G[a]:
            result.append(b)
    return result

# Kiểm tra
print("\n" + "=" * 80)
print("KIỂM TRA HÀM LAYKE")
print("=" * 80)
print(f"\nDanh sách kề của A: {LayKe(COST, 'A')}")
print(f"Danh sách kề của B: {LayKe(COST, 'B')}")
print(f"Danh sách kề của I: {LayKe(COST, 'I')}")
print(f"Danh sách kề của X (không tồn tại): {LayKe(COST, 'X')}")

# ============================================================================
# BestFirstSearch
# ============================================================================

def BestFirstSearch(G, start, goal):
    """
    Tìm đường đi ngắn nhất từ đỉnh start đến goal trong đồ thị G
    Input:
    + Đồ thị G biểu diễn dưới dạng danh sách kề trọng số
    + Đỉnh xuất phát start và tìm kiếm goal
    Return: (path, g) 
    + path[q]: đỉnh trước của q để đi tới q
    + g[q]: đường đi ngắn nhất từ start đến q
    """
    result = (None, None)
    
    if G.get(start) is None or G.get(goal) is None:
        return (None, None)
    
    path = {}  # path(q) = p: đỉnh p là đỉnh trước của q
    g = {}     # g(q): chi phí ngắn nhất từ start --> q
    OPEN = MinHeap()
    CLOSED = []
    
    # Khởi tạo
    OPEN.push((0, start))
    path[start] = None
    g[start] = 0
    
    # Vòng lặp chính
    while OPEN.empty() == False:
        (_, p) = OPEN.pop()  # lấy đỉnh p ra khỏi OPEN với g(p) min
        CLOSED.append(p)     # Đưa p vào CLOSED
        
        # Lấy danh sách kề với đỉnh p
        ds_ke = LayKe(G, p)
        if ds_ke is None:
            continue
            
        for q in ds_ke:  # Xét các đỉnh q kề với p
            if q in CLOSED:  # q thuộc CLOSED --> không làm gì
                pass
            elif OPEN.check((g.get(q), q)):  # Kiểm tra q nằm trong OPEN
                if g.get(q) is not None and g[q] > g[p] + G[p][q]:
                    g[q] = g[p] + G[p][q]
                    path[q] = p
                    OPEN.push((g[q], q))  # Cập nhật lại (g(q), q) trong OPEN
            else:  # Nếu q chưa xét
                g[q] = g[p] + G[p][q]  # Tính g(q)
                path[q] = p  # Tính path(q)
                OPEN.push((g[q], q))  # Đưa q vào OPEN
    
    return (path, g)

# Chạy BFS từ A đến B
print("\n" + "=" * 80)
print("BÀI 1: BEST-FIRST SEARCH - TÌM ĐƯỜNG ĐI TỪ A ĐẾN B")
print("=" * 80)

path_bfs, g_bfs = BestFirstSearch(COST, 'A', 'B')

print("\nMảng chi phí tối ưu g(p):")
print(pprint.pformat(g_bfs))

print("\nMảng truy hồi đường đi path(p):")
print(pprint.pformat(path_bfs))

print(f"\nChi phí từ A đến B: g(B) = {g_bfs.get('B', 'Không tìm được')}")

# ============================================================================
# Truy hồi đường đi
# ============================================================================

def find_path(path, start, goal):
    """
    Truy hồi đường đi từ path array
    Input: path (mảng truy hồi), start (đỉnh bắt đầu), goal (đỉnh đích)
    Return: Danh sách đỉnh từ start --> goal
    """
    result = []
    
    v = goal
    while path.get(v) is not None:
        result.append(v)
        v = path[v]
    
    result.append(v)
    result.reverse()
    
    return result

# Truy hồi đường đi BFS
path_result_bfs = find_path(path_bfs, 'A', 'B')
print("\n" + "=" * 80)
print("TRUY HỒI ĐƯỜNG ĐI - BFS")
print("=" * 80)
print(f"\nĐường đi từ A đến B: {path_result_bfs}")
print(f"Số bước: {len(path_result_bfs) - 1}")
print(f"Chi phí tổng cộng: {g_bfs['B']}")

# ============================================================================
# BÀI 2: THUẬT TOÁN A*
# ============================================================================

# Định nghĩa heuristic h(p) - ước lượng chi phí từ p --> B
h = {}
h['A'] = 18  # Ước lượng từ A --> B
h['B'] = 0   # Ở B rồi
h['C'] = 16  # Ước lượng từ C --> B
h['D'] = 15  # Ước lượng từ D --> B
h['E'] = 15  # Ước lượng từ E --> B
h['F'] = 20  # Ước lượng từ F --> B
h['G'] = 20  # Ước lượng từ G --> B
h['H'] = 10  # Ước lượng từ H --> B
h['I'] = 5   # Ước lượng từ I --> B
h['K'] = 6   # Ước lượng từ K --> B

print("\n" + "=" * 80)
print("BÀI 2: THUẬT TOÁN A* SEARCH - TÌM ĐƯỜNG ĐI TỪ A ĐẾN B")
print("=" * 80)

print("\nTri thức h(p) - Heuristic (ước lượng chi phí từ p --> B):")
print(pprint.pformat(h))

# ============================================================================
# A* Search Algorithm
# ============================================================================

def AStartSearch(G, start, goal, h={}):
    """
    Tìm đường đi ngắn nhất từ đỉnh start đến goal trong đồ thị G với tri thức h(p)
    Input:
    + Đồ thị G biểu diễn dưới dạng danh sách kề trọng số
    + Đỉnh xuất phát start và tìm kiếm goal
    + Tri thức h(p): ước lượng chi phí đi từ đỉnh p --> goal
    Return: (path, g)
    + path[q]: đỉnh trước của q để đi tới q
    + g[q]: đường đi ngắn nhất từ start đến q
    """
    result = (None, None)
    
    if G.get(start) is None or G.get(goal) is None:
        return (None, None)
    
    path = {}  # path(q) = p: đỉnh p là đỉnh trước của q
    g = {}     # g(q): chi phí ngắn nhất từ start --> q
    f = {}     # f(q) = g(q) + h(q): hàm đánh giá
    OPEN = MinHeap()
    CLOSED = []
    
    # Khởi tạo
    path[start] = None
    g[start] = 0
    f[start] = g[start] + h.get(start, 0)
    OPEN.push((f[start], start))
    
    # Vòng lặp chính
    while OPEN.empty() == False:
        (_, p) = OPEN.pop()  # lấy đỉnh p ra khỏi OPEN với f(p) min
        CLOSED.append(p)     # đưa p vào CLOSED
        
        # Lấy danh sách kề với đỉnh p
        ds_ke = LayKe(G, p)
        if ds_ke is None:
            continue
        
        for q in ds_ke:  # Xét các đỉnh q kề với p
            if q in CLOSED:  # q thuộc CLOSED
                if g.get(q) is not None and g[q] > g[p] + G[p][q]:
                    g[q] = g[p] + G[p][q]
                    f[q] = g[q] + h.get(q, 0)
                    path[q] = p
                    CLOSED.remove(q)  # di chuyển q vào lại OPEN
                    OPEN.push((f[q], q))
            elif OPEN.check((f.get(q), q)):  # q nằm trong OPEN
                if g.get(q) is not None and g[q] > g[p] + G[p][q]:
                    g[q] = g[p] + G[p][q]
                    f[q] = g[q] + h.get(q, 0)
                    path[q] = p
                    OPEN.push((f[q], q))  # cập nhật lại (f(q), q) trong OPEN
            else:  # Nếu q chưa xét
                g[q] = g[p] + G[p][q]
                f[q] = g[q] + h.get(q, 0)
                path[q] = p
                OPEN.push((f[q], q))  # Đưa q vào OPEN
    
    return (path, g)

# Chạy A*
path_astar, g_astar = AStartSearch(COST, 'A', 'B', h)

print("\nMảng chi phí tối ưu g(p):")
print(pprint.pformat(g_astar))

print("\nMảng truy hồi đường đi path(p):")
print(pprint.pformat(path_astar))

print(f"\nChi phí từ A đến B: g(B) = {g_astar.get('B', 'Không tìm được')}")

# Truy hồi đường đi A*
path_result_astar = find_path(path_astar, 'A', 'B')
print("\n" + "=" * 80)
print("TRUY HỒI ĐƯỜNG ĐI - A*")
print("=" * 80)
print(f"\nĐường đi từ A đến B: {path_result_astar}")
print(f"Số bước: {len(path_result_astar) - 1}")
print(f"Chi phí tổng cộng: {g_astar['B']}")

# So sánh BFS và A*
print("\n" + "=" * 80)
print("SO SÁNH BEST-FIRST SEARCH VÀ A*")
print("=" * 80)
print("\nBest-First Search:")
print(f"  Đường đi: {path_result_bfs}")
print(f"  Chi phí: {g_bfs['B']}")

print("\nA* Search:")
print(f"  Đường đi: {path_result_astar}")
print(f"  Chi phí: {g_astar['B']}")

print(f"\nKết luận: Cả hai thuật toán đều tìm được đường đi ngắn nhất = {g_astar['B']}")
print("\n✓ Hoàn thành toàn bộ bài tập!")
