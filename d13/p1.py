import sys

input = open(sys.argv[1]).read().rstrip()
pairs = input.split("\n\n")


def parse_packet(packet):
    parsed_packet = []
    i = 1
    while i < len(packet)-1:
        c = packet[i]
        if c == "[":
            j = packet.find("]", i)
            sublist = parse_packet(packet[i:j+1])
            parsed_packet.append(sublist)
            i = j + 1
            continue
        if c in [",", "]"]:
            i += 1
            continue
        parsed_packet.append(int(c))
        i += 1
    return parsed_packet


def check_order(packet1, packet2):
    i = 0
    while i < min(len(packet1), len(packet2)):
        if packet1 == packet2:
            i += 1
            continue
        if type(packet1[i]) is int and type(packet2[i]) is int:
            return packet1[i] < packet2[i]
        if type(packet1[i]) is list and type(packet2[i]) is list:
            result = check_order(packet1[i], packet2[i])
            if result:
                return result
        if type(packet1[i]) is int:
            new_packet = packet1[:]
            new_packet[i] = [packet1[i]]
            return check_order(new_packet, packet2)
        if type(packet2[i]) is int:
            new_packet = packet2[:]
            new_packet[i] = [packet2[i]]
            return check_order(packet1, new_packet)
        i += 1
    if len(packet1) == len(packet2):
        return None
    return len(packet1) < len(packet2)


ans = 0
for i, pair in enumerate(pairs):
    p1, p2 = pair.split("\n")
    packet1 = parse_packet(p1)
    packet2 = parse_packet(p2)
    print(packet1)
    print(packet2)
    print(check_order(packet1, packet2))
    print()
    if check_order(packet1, packet2):
        ans += (i + 1)
print(ans)
