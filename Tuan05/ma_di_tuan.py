import sys

# Tăng giới hạn đệ quy để tránh lỗi khi bàn cờ lớn
sys.setrecursionlimit(2000)

def giai_ma_di_tuan(n, start_x, start_y):
    # [TỐI ƯU TOÁN HỌC CỰC KỲ QUAN TRỌNG]: 
    # Đề yêu cầu hành trình khép kín (trở về điểm ban đầu) -> tổng số bước N*N phải là số chẵn.
    # Nếu N lẻ (VD: 3, 5, 7, 9), bàn cờ không có số lượng ô đen trắng bằng nhau cho một chu trình,
    # mã chắc chắn không thể quay về điểm xuất phát. Ta return None luôn để tiết kiệm thời gian chạy.
    if n % 2 != 0:
        return None

    board = [[0] * n for _ in range(n)]
    
    # 8 hướng di chuyển của quân mã
    dx = [-2, -2, -1, -1,  1, 1,  2, 2]
    dy = [-1,  1, -2,  2, -2, 2, -1, 1]

    def hop_le(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == 0

    def dem_loi_thoat(x, y):
        count = 0
        for i in range(8):
            if hop_le(x + dx[i], y + dy[i]):
                count += 1
        return count

    # [HÀM ĐẶC BIỆT]: Quay lui (Backtracking) + Heuristic Warnsdorff
    def Try(x, y, step):
        board[x][y] = step
        
        # Base case: Đã đi qua tất cả N*N ô
        if step == n * n:
            # Kiểm tra xem từ ô cuối có thể nhảy 1 bước về lại ô xuất phát không (Hành trình khép kín)
            for i in range(8):
                if x + dx[i] == start_x and y + dy[i] == start_y:
                    return True
            board[x][y] = 0
            return False

        # Thu thập các bước đi tiếp theo có thể
        next_moves = []
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if hop_le(nx, ny):
                loi_thoat = dem_loi_thoat(nx, ny)
                next_moves.append((loi_thoat, nx, ny))
        
        # Sắp xếp theo Warnsdorff: Ưu tiên đi vào những ô có ít lối thoát nhất trước
        # Điều này giúp quân mã vét cạn các ô ở rìa/góc bàn cờ, tránh bị kẹt không có đường ra
        next_moves.sort(key=lambda val: val[0])

        # Đi sâu vào nhánh đệ quy
        for _, nx, ny in next_moves:
            if Try(nx, ny, step + 1):
                return True
        
        # Backtracking: Phục hồi trạng thái nếu sai đường
        board[x][y] = 0
        return False

    if Try(start_x, start_y, 1):
        return board
    return None

def main():
    try:
        # Đọc dữ liệu từ bàn phím (N, x0, y0)
        inp = input().split()
        if not inp: return
        n = int(inp[0])
        
        # Tọa độ đề bài cho là 1-based, ta chuyển về 0-based để xử lý mảng
        x0 = int(inp[1]) - 1 
        y0 = int(inp[2]) - 1
    except EOFError:
        return

    ket_qua = giai_ma_di_tuan(n, x0, y0)

    if ket_qua is None:
        print(0)
    else:
        print(1)
        for row in ket_qua:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()