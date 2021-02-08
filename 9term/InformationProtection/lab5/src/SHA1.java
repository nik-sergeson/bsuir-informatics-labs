package lab5.src;

import java.util.ArrayList;
import java.util.Arrays;

import static numbers.IntHelper.intToByteArray;


public class SHA1 {
    public static final int BLOCK_SIZE = 512, SIGNATURE_SIZE = 160;
    private int H0, H1, H2, H3, H4;

    public SHA1() {
        H0 = 0x67452301;
        H1 = 0xefcdab89;
        H2 = 0x98badcfe;
        H3 = 0x10325476;
        H4 = 0xc3d2e1f0;
    }

    public int func(int t, int x, int y, int z) {
        if (t <= 19)
            return (x & y) ^ ((~x) & z);
        else if (t <= 39)
            return x ^ y ^ z;
        else if (t <= 59)
            return (x & y) ^ (x & z) ^ (y ^ z);
        else
            return x ^ y ^ z;
    }

    public int getK_t(int t) {
        if (t <= 19)
            return 0x5a827999;
        else if (t <= 39)
            return 0x6ed9eba1;
        else if (t <= 59)
            return 0x8f1bbcdc;
        else
            return 0xca62c1d6;
    }

    private void addBlockHash(int[] block) {
        final int EXTENDED_BLOCK_LENGTH = 80;
        int[] extendedBlock = new int[EXTENDED_BLOCK_LENGTH];
        int a, b, c, d, e;
        Arrays.fill(extendedBlock, 0);
        a = H0;
        b = H1;
        c = H2;
        d = H3;
        e = H4;
        for (int j = 0; j < block.length; j++)
            extendedBlock[j] = block[j];
        for (int j = block.length; j < EXTENDED_BLOCK_LENGTH; j++) {
            int xorResult = extendedBlock[j - 3] ^ extendedBlock[j - 8] ^ extendedBlock[j - 14] ^ extendedBlock[j - 16];
            extendedBlock[j] = (xorResult << 1) | (xorResult >> (Integer.SIZE - 1));
        }
        for (int j = 0; j < EXTENDED_BLOCK_LENGTH; j++) {
            int temp = leftRotate(a, 5) + func(j, b, c, d) + e + extendedBlock[j] + getK_t(j);
            e = d;
            d = c;
            c = leftRotate(b, 30);
            b = a;
            a = temp;
        }
        H0 = H0 + a;
        H1 = H1 + b;
        H2 = H2 + c;
        H3 = H3 + d;
        H4 = H4 + e;
    }

    public byte[] getComputedHash() {
        byte[] hash = new byte[SIGNATURE_SIZE / Byte.SIZE];
        System.arraycopy(intToByteArray(H0), 0, hash, 0, Integer.BYTES);
        System.arraycopy(intToByteArray(H1), 0, hash, Integer.BYTES, Integer.BYTES);
        System.arraycopy(intToByteArray(H2), 0, hash, Integer.BYTES * 2, Integer.BYTES);
        System.arraycopy(intToByteArray(H3), 0, hash, Integer.BYTES * 3, Integer.BYTES);
        System.arraycopy(intToByteArray(H4), 0, hash, Integer.BYTES * 4, Integer.BYTES);
        return hash;
    }

    public void resetState() {
        H0 = 0x67452301;
        H1 = 0xefcdab89;
        H2 = 0x98badcfe;
        H3 = 0x10325476;
        H4 = 0xc3d2e1f0;
    }

    public void addHash(byte[] source) {
        ArrayList<int[]> blocks;
        final int BLOCK_LENGTH = BLOCK_SIZE / Byte.SIZE;
        for (int i = 0; i < source.length; i += BLOCK_LENGTH) {
            blocks = getBlock(source, i);
            for (int[] block : blocks) {
                addBlockHash(block);
            }
        }
    }

    public ArrayList<int[]> getBlock(byte[] source, int startByte) {
        final int BLOCK_LENGTH = BLOCK_SIZE / Integer.SIZE, BYTE_MASK = 255;
        int currentSourceBlock = startByte;
        int[] block = new int[BLOCK_LENGTH];
        ArrayList<int[]> result = new ArrayList<>();
        if (source.length - startByte > BLOCK_SIZE / Byte.SIZE) {
            for (int i = 0; i < BLOCK_LENGTH; i++) {
                for (int j = 0; j < Integer.BYTES; currentSourceBlock++, j++) {
                    block[i] = (block[i] << 1) | (source[currentSourceBlock] & BYTE_MASK);
                }
            }
            result.add(block);
        } else {
            int currentBlock = 0, initialByte = 128, lastByteIndex = 0, bytesLeft;
            for (; currentSourceBlock < source.length; currentBlock++) {
                lastByteIndex = 0;
                for (int j = 0; j < Integer.BYTES && currentSourceBlock < source.length; currentSourceBlock++, j++, lastByteIndex++) {
                    block[currentBlock] = (block[currentBlock] << 1) | (source[currentSourceBlock] & BYTE_MASK);
                }
                if(currentSourceBlock >= source.length)
                    break;
            }
            bytesLeft = Integer.BYTES - lastByteIndex + (BLOCK_LENGTH - currentBlock) * Integer.BYTES;
            if (bytesLeft >= Long.BYTES) {
                if (lastByteIndex == Integer.BYTES) {
                    ++currentBlock;
                    lastByteIndex = 0;
                }
                if (bytesLeft > Long.BYTES) {
                    block[currentBlock] = (block[currentBlock] << 1) | initialByte;
                    ++lastByteIndex;
                    for (; lastByteIndex < Integer.BYTES; ++lastByteIndex) {
                        block[currentBlock] <<= 1;
                    }
                    ++currentBlock;
                }
                long sourceLength = source.length * Byte.SIZE;
                block[BLOCK_LENGTH - 2] = (int) (sourceLength >> Long.SIZE / 2);
                block[BLOCK_LENGTH - 1] = (int) sourceLength;
                result.add(block);
            } else {
                if (bytesLeft > 0) {
                    if (lastByteIndex == Integer.BYTES) {
                        ++currentBlock;
                        lastByteIndex = 0;
                    }
                    block[currentBlock] = (block[currentBlock] << 1) | initialByte;
                    ++lastByteIndex;
                    for (; lastByteIndex < Integer.BYTES; ++lastByteIndex) {
                        block[currentBlock] <<= 1;
                    }
                    result.add(block);
                    block = new int[BLOCK_LENGTH];
                } else {
                    result.add(block);
                    block = new int[BLOCK_LENGTH];
                    lastByteIndex = 0;
                    block[currentBlock] = (block[currentBlock] << 1) | initialByte;
                    ++lastByteIndex;
                    for (; lastByteIndex < Integer.BYTES; ++lastByteIndex) {
                        block[currentBlock] <<= 1;
                    }
                    ++currentBlock;
                }
                long sourceLength = source.length * Byte.SIZE;
                block[BLOCK_LENGTH - 2] = (int) (sourceLength >> Long.SIZE / 2);
                block[BLOCK_LENGTH - 1] = (int) sourceLength;
                result.add(block);
            }

        }
        return result;
    }

    public int leftRotate(int value, int bitCount) {
        return (value << bitCount) | (value >> (Integer.SIZE - bitCount));
    }
}
