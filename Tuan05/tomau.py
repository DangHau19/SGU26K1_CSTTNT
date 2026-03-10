import sys

def to_mau_do_thi(n, edges):
    # [HÀM ĐẶC BIỆT]: Thuật toán Tham lam (Greedy) tô màu đồ thị
    # Nguyên lý: Lần lượt xét từng đỉnh từ 1 đến n, tô đỉnh đó bằng màu (số) nhỏ nhất
    # mà CHƯA bị sử dụng bởi bất kỳ đỉnh nào kề với nó.
    
    # Khởi tạo danh sách kề
    adj = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    colors = {} # Dictionary lưu màu của từng đỉnh {đỉnh: màu}
    
    for u in range(1, n + 1):
        # Lấy danh sách các màu đã bị các đỉnh kề "chiếm dụng"
        used_colors = {colors[v] for v in adj[u] if v in colors}
        
        # Tìm màu (bắt đầu từ 1) nhỏ nhất chưa bị chiếm
        c = 1
        while c in used_colors:
            c += 1
            
        colors[u] = c
        
    # Gom nhóm các đỉnh lại theo màu để dễ in ra
    color_groups = {}
    for u, c in colors.items():
        if c not in color_groups:
            color_groups[c] = []
        color_groups[c].append(u)
        
    return color_groups

def main():
    # Đọc toàn bộ dữ liệu từ bàn phím một lần
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Trích xuất M cạnh (mỗi cạnh 2 đỉnh u, v)
    edges = []
    idx = 2
    for _ in range(m):
        if idx + 1 < len(input_data):
            edges.append((int(input_data[idx]), int(input_data[idx+1])))
            idx += 2
            
    # Gọi thuật toán
    color_groups = to_mau_do_thi(n, edges)
    
    # Số lượng màu cần dùng chính là màu lớn nhất đã được tô
    k = max(color_groups.keys()) if color_groups else 0
    
    # In ra dòng đầu: Số màu k
    print(k)
    
    # In ra k dòng tiếp theo: Các đỉnh có cùng màu (đã sắp xếp tăng dần)
    for c in range(1, k + 1):
        if c in color_groups:
            print(" ".join(map(str, sorted(color_groups[c]))))

if __name__ == "__main__":
    main()