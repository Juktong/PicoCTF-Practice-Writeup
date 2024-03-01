from pwn import *

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

port = 51422

def getLSB(pl):
    r = remote("saturn.picoctf.net", port)
    r.recv()
    r.send(pl + "\n")
    rec = r.recv()
    rec = rec[16:-1]
    r.close()
    return int(rec)


def eliminate(guess, toEliminate, remaining_set):
    for b in toEliminate:
        if b ^ guess in remaining_set:
            remaining_set.remove(b ^ guess)


def guess_one_byte(byte_idx):
    baseload = "0" * 32
    base = getLSB(baseload)

    remaining_set_A = {i for i in range(256)}
    remaining_set_B = {i for i in range(256)}
    weighted = True

    for guess in range(16):
        inj = str(hex(guess))[2:]
        if len(inj) == 1:
            inj = "0" + inj

        payload = '0' * (32 - 2 - 2 * byte_idx) + inj + '0' * (2 * byte_idx)
        tmp = getLSB(payload)
        # print("LSB of this load:", tmp, "\nPayload: ", payload)
        if tmp < base:
            weighted = False
        if tmp == base:
            eliminate(guess, even_res_by_idx, remaining_set_A)
            eliminate(guess, odd_res_by_idx, remaining_set_B)
        else:
            eliminate(guess, odd_res_by_idx, remaining_set_A)
            eliminate(guess, even_res_by_idx, remaining_set_B)

    if not weighted:
        assert len(remaining_set_A) == 1
        return next(iter(remaining_set_A))
    else:
        assert len(remaining_set_B) == 1
        return next(iter(remaining_set_B))


res = ""
for i in range(16):
    toAppend = hex(guess_one_byte(i))[2:]
    if len(toAppend) == 1:
        toAppend = "0" + toAppend
    res = toAppend + res
print(res)
