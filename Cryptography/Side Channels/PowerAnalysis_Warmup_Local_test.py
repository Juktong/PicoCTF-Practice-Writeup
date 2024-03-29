import random, sys, time

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)
odd_res_by_idx = {0, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 18, 19, 21, 22, 24, 27, 32, 33, 34, 37, 38, 41, 42, 43, 44, 46,
                  47, 49, 50, 51, 54, 56, 60, 61, 63, 64, 65, 68, 73, 75, 76, 77, 78, 80, 81, 83, 86, 87, 89, 91, 95,
                  97, 99, 100, 101, 102, 103, 104, 105, 107, 110, 112, 113, 115, 117, 119, 123, 125, 126, 128, 130, 132,
                  133, 135, 137, 139, 141, 142, 143, 145, 146, 158, 159, 164, 169, 172, 173, 175, 176, 178, 179, 180,
                  181, 183, 188, 194, 201, 203, 204, 205, 206, 210, 213, 216, 217, 218, 219, 221, 222, 224, 227, 228,
                  229, 232, 234, 235, 237, 239, 241, 242, 243, 244, 248, 249, 250, 251, 254}
even_res_by_idx = {1, 4, 8, 12, 15, 16, 17, 20, 23, 25, 26, 28, 29, 30, 31, 35, 36, 39, 40, 45, 48, 52, 53, 55, 57, 58,
                   59, 62, 66, 67, 69, 70, 71, 72, 74, 79, 82, 84, 85, 88, 90, 92, 93, 94, 96, 98, 106, 108, 109, 111,
                   114, 116, 118, 120, 121, 122, 124, 127, 129, 131, 134, 136, 138, 140, 144, 147, 148, 149, 150, 151,
                   152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 165, 166, 167, 168, 170, 171, 174, 177, 182, 184,
                   185, 186, 187, 189, 190, 191, 192, 193, 195, 196, 197, 198, 199, 200, 202, 207, 208, 209, 211, 212,
                   214, 215, 220, 223, 225, 226, 230, 231, 233, 236, 238, 240, 245, 246, 247, 252, 253, 255}

secret = bytes.fromhex("37cb5c4775a6094abebf6d3bbd7abbb2")


def getLSB(pl):
    plaintext = bytes.fromhex(pl)
    leak_buf = []
    for i in range(16):
        print("Testing:", plaintext[i],secret[i])
        out = Sbox[plaintext[i] ^ secret[i]]
        leak_buf.append(out & 0x01)
    print("Leak Buffer: ",leak_buf)
    time.sleep(0.01)
    return leak_buf.count(1)


def eliminate(guess, toEliminate, remaining_set):
    for b in toEliminate:
        if b ^ guess in remaining_set:
            remaining_set.remove(b ^ guess)


def guess_one_byte(byte_idx):
    baseload = "0" * 32
    base = getLSB(baseload)
    print(base)

    remaining_set_A = {i for i in range(256)}
    remaining_set_B = {i for i in range(256)}
    isA = True

    for guess in range(256):
        inj = str(hex(guess))[2:]
        # print(inj)
        if len(inj) == 1:
            inj = "0" + inj

        payload = '0' * (32 - 2 - 2 * byte_idx) + inj + '0' * (2 * byte_idx)
        print(payload)
        tmp = getLSB(payload)
        print("LSB of this load:", tmp)
        if tmp < base:
            isA = False
        if tmp == base:
            eliminate(guess, even_res_by_idx, remaining_set_A)
            eliminate(guess, odd_res_by_idx, remaining_set_B)
        else:
            eliminate(guess, odd_res_by_idx, remaining_set_A)
            eliminate(guess, even_res_by_idx, remaining_set_B)
        print(remaining_set_A)
        print(remaining_set_B)
        print()

    if not isA:
        # assert len(remaining_set_A) == 1
        return next(iter(remaining_set_A))  # get ele
    else:
        # assert len(remaining_set_B) == 1
        return next(iter(remaining_set_B))  # get ele


res = []
for i in range(16):
    toAppend=hex(guess_one_byte(i))[2:]
    if len(toAppend)==1:
        toAppend="0"+toAppend
    res.append(toAppend)
    print(res)
