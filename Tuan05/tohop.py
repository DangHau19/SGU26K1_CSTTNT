def sinh_to_hop(k, n, elements):
    # [HÀM ĐẶC BIỆT]: Thuật toán Quay lui (Backtracking) cốt lõi
    # Thay vì duyệt 2 lần (1 lần đếm, 1 lần in), ta lưu tất cả vào mảng results.
    results = []
    current_indices = [-1] * k

    def Try(i, start_idx):
        # Điều kiện dừng (Base case): Khi đã chọn đủ k phần tử
        if i == k:
            # Map các chỉ số (index) đã chọn sang giá trị thực tế của tập hợp A
            combo = [elements[idx] for idx in current_indices]
            results.append(combo)
            return
        
        # Nhánh đệ quy: Thử chọn các phần tử tiếp theo (từ start_idx đến n-1)
        for j in range(start_idx, n):
            current_indices[i] = j  # Ghi nhận quyết định chọn phần tử ở vị trí j
            Try(i + 1, j + 1)       # Đi sâu vào nhánh tiếp theo, chỉ được chọn từ j+1 trở đi

    Try(0, 0)
    return results

def main():
    # Nhập N và K từ bàn phím
    n, k = map(int, input().split())
    
    # Nhập N phần tử của tập hợp
    elements = []
    for _ in range(n):
        elements.append(input().strip())

    # Gọi hàm xử lý
    tap_hop_ket_qua = sinh_to_hop(k, n, elements)

    # In ra dòng đầu tiên: Số lượng tổ hợp (M)
    print(len(tap_hop_ket_qua))
    
    # In ra các dòng tiếp theo: Từng tổ hợp
    for combo in tap_hop_ket_qua:
        print(" ".join(combo))

if __name__ == "__main__":
    main()