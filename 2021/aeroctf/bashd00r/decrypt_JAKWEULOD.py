#!/usr/bin/python
def bf_char(n, p, res):
    selected = -1
    for i in range(0x10, 0x7f):
        if pow(i, n, p) == res:
            if selected == -1:
                selected = i
            else:
                print("Other candidate %d" % i)
    return selected

flag = bytearray(b"-"*65)

elts = [
    (0x7b7bc, 0x3fa, 0x6af18, 4),
    (0x3fbeb, 0x2a1, 0xd56d, 0xd),
    (0x3ddd3, 0x2d6, 0x2195e, 0x39),
    (0x564d9, 0xcf, 0x29ec3, 0x2b),
    (0x7d1f0, 0x1bc, 0x1f260, 0x16),
    (0x546b5, 0x365, 0x23d63, 8),
    (0x77329, 0x3ae, 0x50621, 0x30),
    (0x4b69f, 0x246, 0x2f40d, 0x1f),
    (0x27ded, 0x3a1, 0x27b0b, 0x2d),
    (0x6518c, 0x1bb, 0x60608, 0x37),
    (0x5463f, 0x291, 0x1e2f9, 3),
    (0x772bb, 0x9a, 0x26e81, 0xb),
    (0x5f804, 0x388, 0x4a4e1, 7),
    (0x65256, 0x307, 0x5416f, 0xd),
    (0x470cb, 0x27e, 0x2505, 0xa),
    (0x57d67, 0x18d, 0x268c7, 0x1a),
    (0x5f94d, 0x3a3, 0x52acc, 0x18),
    (0x74d7a, 0x226, 0x41573, 0x2f),
    (0x31825, 0x144, 0x1311a, 0xe),
    (0x435c4, 0x11a, 0x13bd9, 0xf),
    (0x333e6, 0x295, 0x89da, 0x11),
    (0x681f1, 0x255, 0x4abeb, 0xb),
    (0x40177, 0x12e, 0x591c, 0x37),
    (0x4cb93, 0x1fb, 0x3d9a5, 0x34),
    (0x42a4a, 0x388, 0x9025, 0x19),
    (0x46ba3, 0x16e, 0x1e71b, 0x11),
    (0x79f1a, 0x182, 0x685ab, 0x38),
    (0x2fb7a, 0x1f6, 0x218d7, 0x2d),
    (0x2fa50, 0x3f3, 0x120ab, 0x29),
    (0x59718, 0x386, 0x4269, 0x2a),
    (0x2df74, 0x357, 0xf661, 0x23),
    (0x74d5d, 0x22a, 0x5abad, 0xc),
    (0x50535, 0x338, 0x80f4, 0x28),
    (0x2cdc5, 0x2c9, 0x1a148, 0x2e),
    (0x2e0f8, 0x37b, 0x19b25, 0x2d),
    (0x35af6, 0x211, 0x9571, 0x33),
    (0x21a5d, 0x1cc, 0x6d5, 0x6),
    (0x7374a, 0x390, 0x2c649, 0x33),
    (0x60f5f, 0xec, 0x3d7da, 0x2c),
    (0x6e2a3, 0x246, 0x40052, 0x35),
    (0x2f086, 0x97, 0x1eb8, 0x3d),
    (0x353da, 0x3f6, 0x0d060, 0x24),
    (0x5c80a, 0x125, 0x2cc07, 0x3a),
    (0x65d3a, 0x2d7, 0x62ad0, 2),
    (0x3d396, 0x1c8, 0x3d255, 0x3b),
    (0x7b9cc, 0x1f8, 0xb94, 0x3e),
    (0x3c76e, 0x2f0, 0xda23, 0x23),
    (0x7efae, 0x3e3, 0x14d86, 0x1b),
    (0x47de5, 0x2b5, 0x514f, 0xd),
    (0x2207d, 0x1bb, 0xc5d0, 0x1d),
    (0x41b9c, 0x19d, 0x167fd, 0x38),
    (0x55c61, 0x3f6, 0x131bc, 0x1),
    (0x667bb, 0x255, 0x301da, 0x1),
    (0x5fc85, 0x169, 0x592db, 0x5),
    (0x48BD4, 0x389, 0x29820, 0x3c),
    (0x3c46a, 0x211, 0x21fba, 0x3f),
    (0x53490, 0x306, 0x90e1, 0x1e),
    (0x352D2, 0xad, 0x1c697, 0x13),
    (0x695e1, 0x2b2, 0x3425f, 0x12),
    (0x7b843, 0x3f9, 0x26e87, 0),
    (0x44a4b, 0x382, 0x32227, 0x27),
    (0x5c3bb, 0x19e, 0x522f, 0x20),
    (0x271aa, 0x238, 0xcc6a, 0x14),
    (0x6530f, 0x2a7, 0x4833a, 0x36),
    (0x40dd0, 0x23b, 0xa669, 0x22),
    (0x597e8, 0x361, 0x4993b, 0x21),
    (0x270ae, 0x304, 0x1f23c, 0x32),
    (0x4a46e, 0x318, 0x1ab8a, 0x25),
    (0x603f1, 0x3a7, 0x42da2, 0x15),
    (0x6e0ae, 0x3b0, 0x52a86, 0x26),
    (0x20dc2, 0xfe, 0x19d86, 0x17),
    (0x66026, 0x250, 0x1de94, 0x31),
    (0x28ebc, 0x3cd, 0x513b, 0x1c),
    (0x2241a, 0x153, 0x71a3, 0x9),
    (0x3dbca, 0x377, 0x5de6, 0x10)

]

for e in elts:
    c = bf_char(e[1], e[0], e[2])
    #print(hex(e[3]))
    flag[e[3]] = c

print(len(elts))
print(flag)
pos = [hex(i) for i in range(len(flag)) if flag[i] == ord("-")]
print(pos)