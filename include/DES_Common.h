#define uint uint32_t
#define uchar unsigned char

#define MAP_8(dest, src, off_tab, off_dest) \
    dest[off_dest + 0x00] = src[off_tab + 0x00], dest[off_dest + 0x01] = src[off_tab + 0x01], dest[off_dest + 0x02] = src[off_tab + 0x02], dest[off_dest + 0x03] = src[off_tab + 0x03],\
    dest[off_dest + 0x04] = src[off_tab + 0x04], dest[off_dest + 0x05] = src[off_tab + 0x05], dest[off_dest + 0x06] = src[off_tab + 0x06], dest[off_dest + 0x07] = src[off_tab + 0x07];

#define MAP_16(dest, src, table, off_tab, off_dest) \
    dest[off_dest + 0x00] = src[table[off_tab + 0x00] - 1], dest[off_dest + 0x01] = src[table[off_tab + 0x01] - 1], dest[off_dest + 0x02] = src[table[off_tab + 0x02] - 1], dest[off_dest + 0x03] = src[table[off_tab + 0x03] - 1],\
    dest[off_dest + 0x04] = src[table[off_tab + 0x04] - 1], dest[off_dest + 0x05] = src[table[off_tab + 0x05] - 1], dest[off_dest + 0x06] = src[table[off_tab + 0x06] - 1], dest[off_dest + 0x07] = src[table[off_tab + 0x07] - 1],\
    dest[off_dest + 0x08] = src[table[off_tab + 0x08] - 1], dest[off_dest + 0x09] = src[table[off_tab + 0x09] - 1], dest[off_dest + 0x0a] = src[table[off_tab + 0x0a] - 1], dest[off_dest + 0x0b] = src[table[off_tab + 0x0b] - 1],\
    dest[off_dest + 0x0c] = src[table[off_tab + 0x0c] - 1], dest[off_dest + 0x0d] = src[table[off_tab + 0x0d] - 1], dest[off_dest + 0x0e] = src[table[off_tab + 0x0e] - 1], dest[off_dest + 0x0f] = src[table[off_tab + 0x0f] - 1];

#define XOR_32(dest, src1, src2) \
    dest[0x00] = src1[0x00] ^ src2[0x00], dest[0x01] = src1[0x01] ^ src2[0x01], dest[0x02] = src1[0x02] ^ src2[0x02], dest[0x03] = src1[0x03] ^ src2[0x03],\
    dest[0x04] = src1[0x04] ^ src2[0x04], dest[0x05] = src1[0x05] ^ src2[0x05], dest[0x06] = src1[0x06] ^ src2[0x06], dest[0x07] = src1[0x07] ^ src2[0x07],\
    dest[0x08] = src1[0x08] ^ src2[0x08], dest[0x09] = src1[0x09] ^ src2[0x09], dest[0x0a] = src1[0x0a] ^ src2[0x0a], dest[0x0b] = src1[0x0b] ^ src2[0x0b],\
    dest[0x0c] = src1[0x0c] ^ src2[0x0c], dest[0x0d] = src1[0x0d] ^ src2[0x0d], dest[0x0e] = src1[0x0e] ^ src2[0x0e], dest[0x0f] = src1[0x0f] ^ src2[0x0f],\
    dest[0x10] = src1[0x10] ^ src2[0x10], dest[0x11] = src1[0x11] ^ src2[0x11], dest[0x12] = src1[0x12] ^ src2[0x12], dest[0x13] = src1[0x13] ^ src2[0x13],\
    dest[0x14] = src1[0x14] ^ src2[0x14], dest[0x15] = src1[0x15] ^ src2[0x15], dest[0x16] = src1[0x16] ^ src2[0x16], dest[0x17] = src1[0x17] ^ src2[0x17],\
    dest[0x18] = src1[0x18] ^ src2[0x18], dest[0x19] = src1[0x19] ^ src2[0x19], dest[0x1a] = src1[0x1a] ^ src2[0x1a], dest[0x1b] = src1[0x1b] ^ src2[0x1b],\
    dest[0x1c] = src1[0x1c] ^ src2[0x1c], dest[0x1d] = src1[0x1d] ^ src2[0x1d], dest[0x1e] = src1[0x1e] ^ src2[0x1e], dest[0x1f] = src1[0x1f] ^ src2[0x1f];

#define S_BOX(j) \
    row = 0, col = 0;\
    col = (newr[j * 6] ^ key[i][j * 6]) << 1;\
    col += (newr[j * 6 + 5] ^ key[i][j * 6 + 5]);\
    row += (newr[j * 6 + 1] ^ key[i][j * 6 + 1]) << 3;\
    row += (newr[j * 6 + 2] ^ key[i][j * 6 + 2]) << 2;\
    row += (newr[j * 6 + 3] ^ key[i][j * 6 + 3]) << 1;\
    row += (newr[j * 6 + 4] ^ key[i][j * 6 + 4]);\
    int2bit = S[j * 64 + col * 16 + row];\
    afterp[j * 4 + 3] = (int2bit & 1);\
    afterp[j * 4 + 2] = (int2bit & 2) >> 1;\
    afterp[j * 4 + 1] = (int2bit & 4) >> 2;\
    afterp[j * 4] = (int2bit & 8) >> 3;

#define GET_BITS \
    char2bits(data[0], &init_data[0 * 8]);\
    char2bits(data[1], &init_data[1 * 8]);\
    char2bits(data[2], &init_data[2 * 8]);\
    char2bits(data[3], &init_data[3 * 8]);\
    char2bits(data[4], &init_data[4 * 8]);\
    char2bits(data[5], &init_data[5 * 8]);\
    char2bits(data[6], &init_data[6 * 8]);\
    char2bits(data[7], &init_data[7 * 8]);

