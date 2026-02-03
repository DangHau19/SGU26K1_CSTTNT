import collections

def solve_8_puzzle(start_state, goal_state):
    """
    Giải bài toán 8-Puzzle bằng thuật toán BFS.
    Input: Tuple chứa 9 số nguyên (0 đại diện cho ô trống)
    Output: Danh sách các bước đi để đến đích
    """
    start = tuple(start_state)
    goal = tuple(goal_state)
    
    # Hàng đợi lưu (trạng_thái_hiện_tại, đường_đi_đến_đó)
    queue = collections.deque([(start, [])])
    visited = set([start])
    
    # Các nước đi cho ô trống (index 0): Lên(-3), Xuống(+3), Trái(-1), Phải(+1)
    # Cần kiểm tra biên để tránh đi ra ngoài bảng 3x3
    
    while queue:
        current_state, path = queue.popleft()
        
        # Nếu tìm thấy đích
        if current_state == goal:
            return path + [current_state]
        
        # Tìm vị trí ô trống (số 0)
        zero_idx = current_state.index(0)
        row, col = divmod(zero_idx, 3) # Lấy dòng, cột
        
        # Xác định các nước đi hợp lệ
        moves = []
        if row > 0: moves.append(-3) # Lên
        if row < 2: moves.append(3)  # Xuống
        if col > 0: moves.append(-1) # Trái
        if col < 2: moves.append(1)  # Phải
        
        for move in moves:
            new_zero_idx = zero_idx + move
            
            # Tạo trạng thái mới bằng cách đổi chỗ
            new_state_list = list(current_state)
            new_state_list[zero_idx], new_state_list[new_zero_idx] = \
                new_state_list[new_zero_idx], new_state_list[zero_idx]
            new_state = tuple(new_state_list)
            
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [current_state]))
    return None

def print_board(state):
    """In trạng thái ra dạng bảng 3x3 đẹp mắt"""
    print(f"+---+---+---+")
    print(f"| {state[0]} | {state[1]} | {state[2]} |")
    print(f"+---+---+---+")
    print(f"| {state[3]} | {state[4]} | {state[5]} |")
    print(f"+---+---+---+")
    print(f"| {state[6]} | {state[7]} | {state[8]} |")
    print(f"+---+---+---+")

# --- CẤU HÌNH BÀI TOÁN THEO ĐỀ ---
# 0 là ô trống
START = [4, 8, 1, 6, 3, 0, 2, 7, 5] 
GOAL  = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# --- CHẠY THUẬT TOÁN ---
solution = solve_8_puzzle(START, GOAL)

if solution:
    steps = len(solution) - 1
    print(f"Đã tìm thấy lời giải tối ưu trong {steps} bước di chuyển!")
    print("="*30)
    
    # In 3 bước đầu và 3 bước cuối để báo cáo (hoặc in hết nếu muốn)
    for i, state in enumerate(solution):
        print(f"BƯỚC {i}:")
        print_board(state)
        print("      |")
        print("      V")
else:
    print("Không tìm thấy đường đi.")