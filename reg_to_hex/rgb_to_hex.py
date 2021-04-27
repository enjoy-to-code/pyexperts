def rgb_to_hex(r, g, b):
  return ('{:02X}' * 3).format(r, g, b)

print(rgb_to_hex(255, 3, 10)) 
# result: 'FF030A'

  