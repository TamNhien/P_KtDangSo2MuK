n = int(input("Nhập số nguyên dương n : "))
is_power_of_2 = n > 0 and (n & (n - 1)) == 0
print(n, "là số dạng 2^k." if is_power_of_2 else "không phải là số dạng 2^k.")

