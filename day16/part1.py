lines = open("data.txt").read().splitlines()

line = [i for i in lines[0]]

new_line = []

for l in line:
    res = "{0:04b}".format(int(l, 16))
    new_line.append(str(res))
    
binary_line = ''.join(new_line)

def to_hex(n):
    num = int(n, 2)
    hex_num = format(num, 'x')
    return(hex_num)


print(binary_line)

packet_version = to_hex(binary_line[0:3])

packet_type_id = to_hex(binary_line[3:6])

print(f"Packet version: {packet_version}")
print(f"Packet type ID: {packet_type_id}")

for x in range(0, len(binary_line[6:]), 5):
    print(binary_line[6+x:6+5+x])