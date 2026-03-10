import random

def quay_lui(n):
    # [HÀM ĐẶC BIỆT 1]: Đệ quy quay lui (Backtracking)
    # Duyệt từng hàng, thử đặt hậu vào các cột an toàn.
    # Kỹ thuật: Dùng 3 mảng đánh dấu (cột, chéo chính, chéo phụ) để kiểm tra an toàn O(1).
    if n == 2 or n == 3:
        return None

    board = [[0] * n for _ in range(n)]
    cot = [False] * n
    cheo_chinh = [False] * (2 * n - 1)
    cheo_phu = [False] * (2 * n - 1)

    def Try(hang):
        # Base case: Đã xếp thành công N con hậu
        if hang == n:
            return True
        for c in range(n):
            # Kiểm tra ô (hang, c) có bị khống chế không
            if not cot[c] and not cheo_chinh[hang - c + n - 1] and not cheo_phu[hang + c]:
                board[hang][c] = 1
                cot[c] = cheo_chinh[hang - c + n - 1] = cheo_phu[hang + c] = True
                
                # Đi sâu vào nhánh tiếp theo, nếu tìm được 1 nghiệm thì return True ngay lập tức
                if Try(hang + 1):
                    return True
                
                # Backtrack: Phục hồi trạng thái nếu nhánh này sai
                board[hang][c] = 0
                cot[c] = cheo_chinh[hang - c + n - 1] = cheo_phu[hang + c] = False
        return False

    if Try(0):
        return board
    return None

def tham_lam_tung_phan(n):
    # [HÀM ĐẶC BIỆT 2]: Tham lam từng phần (Min-Conflicts Heuristic)
    # Khởi tạo ngẫu nhiên, sau đó dời các con hậu đang bị tấn công đến ô ít bị tấn công nhất.
    # Thường dùng cho N rất lớn (ví dụ N = 1000) khi quay lui bị quá thời gian.
    if n == 2 or n == 3: 
        return None
        
    queens = [i for i in range(n)]
    random.shuffle(queens) 
    
    def count_conflicts(r, c):
        conflicts = 0
        for i in range(n):
            if i == r: continue
            if queens[i] == c or abs(i - r) == abs(queens[i] - c):
                conflicts += 1
        return conflicts

    max_steps = 1000 
    for _ in range(max_steps):
        conflicted_queens = [r for r in range(n) if count_conflicts(r, queens[r]) > 0]
        
        if not conflicted_queens:
            board = [[0] * n for _ in range(n)]
            for r in range(n):
                board[r][queens[r]] = 1
            return board
            
        r = random.choice(conflicted_queens)
        min_c = queens[r]
        min_conflicts = count_conflicts(r, queens[r])
        
        for c in range(n):
            if c == queens[r]: continue
            c_conflicts = count_conflicts(r, c)
            if c_conflicts < min_conflicts:
                min_conflicts = c_conflicts
                min_c = c
        
        queens[r] = min_c
        
    return None 

def main():
    try:
        n = int(input().strip())
    except EOFError:
        return
        
    # Gọi hàm thuật toán (Mặc định dùng quay lui để ra kết quả ổn định và khớp test case)
    ket_qua = quay_lui(n)
    # ket_qua = tham_lam_tung_phan(n) # Mở comment dòng này nếu muốn dùng cách Tham lam

    if ket_qua is None:
        print(0)
    else:
        print(1)
        for row in ket_qua:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()