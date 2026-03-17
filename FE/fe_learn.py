def reverse_bits(n):
    res = 0
    for i in range(8):
        # resを左にずらしてnの最下位ビットを足す
        res = (res << 1) | (n & 1)
        # nを右にずらして次のビットへ
        n >>= 1
    return res

# テスト
input_val = 0b11001010  # 202
print(f"Result: {bin(reverse_bits(input_val))}")