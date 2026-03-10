import sys

def tham_lam_sap_xep(n, adj):
    # [HÀM ĐẶC BIỆT 1]: Thuật toán Welsh-Powell (Tham lam + Sắp xếp)
    # Tính bậc (degree) của từng đỉnh, sau đó sắp xếp các đỉnh theo bậc giảm dần.
    # Việc ưu tiên tô các đỉnh có bậc cao (nhiều ràng buộc) trước giúp tối ưu số màu dùng hơn so với tham lam thuần.
    
    degrees = [(len(adj[u]), u) for u in range(1, n + 1)]
    degrees.sort(reverse=True, key=lambda x: x[0])
    sorted_vertices = [u for deg, u in degrees]
    
    colors = {}
    for u in sorted_vertices:
        used_colors = {colors[v] for v in adj[u] if v in colors}
        c = 1
        while c in used_colors:
            c += 1
        colors[u] = c
        
    return colors

def to_mau_toi_uu(n, adj):
    # [HÀM ĐẶC BIỆT 2]: Tô màu tối ưu (Quay lui / Backtracking)
    # Thử giới hạn số màu m tăng dần từ 1 đến N. 
    # Mức m đầu tiên mà hàm đệ quy Try() tô thành công toàn bộ đồ thị chính là sắc số tối ưu.
    
    def is_safe(u, color, c):
        for v in adj[u]:
            if color.get(v) == c:
                return False
        return True

    def Try(u, m, color):
        if u > n:  # Đã tô xong tất cả n đỉnh
            return True
            
        for c in range(1, m + 1):
            if is_safe(u, color, c):
                color[u] = c
                if Try(u + 1, m, color):
                    return True
                color[u] = 0  # Backtrack
        return False

    # Thử lần lượt số màu từ 1 đến n
    for m in range(1, n + 1):
        color = {i: 0 for i in range(1, n + 1)}
        if Try(1, m, color):
            return color
            
    return {}

def in_ket_qua(ten_phuong_phap, colors):
    if not colors:
        return
    color_groups = {}
    for u, c in colors.items():
        if c not in color_groups:
            color_groups[c] = []
        color_groups[c].append(u)
        
    k = max(color_groups.keys())
    print(f"\n--- {ten_phuong_phap} ---")
    print(f"Số màu cần dùng: {k}")
    for c in range(1, k + 1):
        if c in color_groups:
            print(f"Màu {c}: " + " ".join(map(str, sorted(color_groups[c]))))

def main():
    # Đọc dữ liệu (N đỉnh, M cạnh)
    input_data = sys.stdin.read().split()
    if len(input_data) < 2: return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = {i: [] for i in range(1, n + 1)}
    idx = 2
    for _ in range(m):
        if idx + 1 < len(input_data):
            u, v = int(input_data[idx]), int(input_data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
            
    # Chạy và so sánh 2 phương pháp
    kq_tham_lam = tham_lam_sap_xep(n, adj)
    in_ket_qua("THUẬT TOÁN THAM LAM + SẮP XẾP", kq_tham_lam)
    
    kq_toi_uu = to_mau_toi_uu(n, adj)
    in_ket_qua("THUẬT TOÁN TÔ MÀU TỐI ƯU (QUAY LUI)", kq_toi_uu)

if __name__ == "__main__":
    main()