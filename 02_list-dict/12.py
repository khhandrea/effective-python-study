# Stride: arr[::d]
# Slice: arr[a:b]

a = [i for i in range(10)]

even = a[::2]
even_limited = even[1:-1]
print(f"even_limited: {even_limited}")