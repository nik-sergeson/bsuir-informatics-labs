package lab2.src;

import java.util.Arrays;
import java.util.Map;


public class DES {
    private int[] initialPermutation, rightBlockEnlarger, keyPC1, keyPC2, funcPermutation, keyShifts, inverseInitPermutation;
    private Map<Integer, byte[][]> sBoxes;
    public final int ROUND_COUNT = 16;

    public DES(int[] initialPermutation, int[] rightBlockEnlarger, int[] keyPC1, int[] keyPC2, int[] funcPermutation, int[] keyShifts, Map<Integer, byte[][]> sBoxes) {
        assert initialPermutation.length == Long.SIZE;
        assert rightBlockEnlarger.length == 48;
        assert funcPermutation.length == Integer.SIZE;
        assert sBoxes.size() == 8;
        assert keyPC1.length == 56;
        assert keyPC2.length == 48;
        assert keyShifts.length == ROUND_COUNT;
        this.initialPermutation = initialPermutation;
        this.rightBlockEnlarger = rightBlockEnlarger;
        this.keyPC1 = keyPC1;
        this.keyPC2 = keyPC2;
        this.funcPermutation = funcPermutation;
        this.keyShifts = keyShifts;
        this.sBoxes = sBoxes;
        inverseInitPermutation = getInversePermutation(initialPermutation);
    }

    public byte[] encrypt(byte[] source, long key) {
        final int subBlockCount = Long.SIZE / Byte.SIZE;
        int blockCount = source.length / subBlockCount + (source.length % subBlockCount != 0 ? 1 : 0), currentSubBlock = 0, currentEncryptedBlock = 0;
        long block = 0, subBlock = 0;
        final long BYTE_MASK = 255;
        byte[] encryptedSource = new byte[blockCount * subBlockCount];
        Arrays.fill(encryptedSource, (byte) 0);
        long[] roundKeys = generateRoundKeys(key);
        for (int i = 0; i < blockCount; i++) {
            block = 0;
            for (int j = 0; j < subBlockCount; j++) {
                if (currentSubBlock < source.length) {
                    subBlock = source[currentSubBlock];
                    block = (block << Byte.SIZE) | (subBlock & BYTE_MASK);
                } else
                    block = block << Byte.SIZE;
                ++currentSubBlock;
            }
            long encryptedBlock = encryptBlock(block, roundKeys);
            for (int j = subBlockCount - 1; j >= 0; j--) {
                encryptedSource[currentEncryptedBlock] = (byte) (encryptedBlock >> (Byte.SIZE * j));
                ++currentEncryptedBlock;
            }
        }
        return encryptedSource;
    }

    public long encryptBlock(long block, long[] roundKeys) {
        long permutatedBlock = 0, subBlock = 0;
        final long INT_MASK = 4294967295L, BIT_MASK = 1;
        int[] leftRight = new int[2];
        for (int i = 0; i < Long.SIZE; i++) {
            long bit = (block >> (initialPermutation[i] - 1)) & BIT_MASK;
            permutatedBlock = (permutatedBlock << 1) | bit;
        }
        leftRight[0] = (int) (permutatedBlock >> Integer.SIZE);
        leftRight[1] = (int) (permutatedBlock);
        for (int i = 0; i < ROUND_COUNT; i++) {
            leftRight = peformRoundEcnrypt(leftRight[0], leftRight[1], roundKeys[i]);
        }
        subBlock = leftRight[1];
        block = subBlock & INT_MASK;
        block <<= Integer.SIZE;
        subBlock = leftRight[0];
        block |= subBlock & INT_MASK;
        permutatedBlock = 0;
        for (int i = 0; i < Long.SIZE; i++) {
            long bit = (block >> (inverseInitPermutation[i] - 1)) & BIT_MASK;
            permutatedBlock = (permutatedBlock << 1) | bit;
        }
        return permutatedBlock;
    }

    public int[] peformRoundEcnrypt(int leftBlock, int rightBlock, long key) {
        int[] leftRight = new int[2];
        leftRight[0] = rightBlock;
        leftRight[1] = leftBlock ^ (func(rightBlock, key));
        return leftRight;
    }

    public int func(int rightBlock, long key) {
        final int KEY_SIZE = 48, B_BLOCK_COUNT = 8, B_BLOCK_SIZE = 6, BIT_MASK = 1, FOUR_BIT_MASK = 0b1111, SEQUENCE_BLOCK_SIZE = 4;
        final long SIX_BIT_MASK = 63;
        int outSequence = 0, permutatedBlock, bit = 0, row = 0, col = 0;
        long enlargedBlock = 0;
        byte[] bBlocks = new byte[B_BLOCK_COUNT];
        byte[][] currentSBox = null;
        byte currentBlock, SFuncValue = 0;
        for (int i = 0; i < KEY_SIZE; i++) {
            bit = (rightBlock >> (rightBlockEnlarger[i] - 1)) & BIT_MASK;
            enlargedBlock = (enlargedBlock << 1) | bit;
        }
        enlargedBlock = enlargedBlock ^ key;
        for (int i = B_BLOCK_COUNT - 1; i >= 0; i--) {
            bBlocks[i] = (byte) (enlargedBlock & SIX_BIT_MASK);
            enlargedBlock >>= B_BLOCK_SIZE;
        }
        for (int i = 0; i < B_BLOCK_COUNT; i++) {
            currentSBox = sBoxes.get(i + 1);
            currentBlock = bBlocks[i];
            row = (((currentBlock >> (B_BLOCK_SIZE - 1)) & BIT_MASK) << 1) | (currentBlock & BIT_MASK);
            col = (currentBlock >> 1) & FOUR_BIT_MASK;
            outSequence = (outSequence << SEQUENCE_BLOCK_SIZE) | (currentSBox[row][col] & FOUR_BIT_MASK);
        }
        permutatedBlock = 0;
        for (int i = 0; i < Integer.SIZE; i++) {
            bit = (outSequence >> (funcPermutation[i] - 1)) & BIT_MASK;
            permutatedBlock = (permutatedBlock << 1) | bit;
        }
        return permutatedBlock;
    }

    public long[] generateRoundKeys(long sourceKey) {
        final long SUBKEY_MASK = 0b1111111111111111111111111111;
        long roundKey = 0, subKey;
        long[] roundKeys = new long[ROUND_COUNT];
        final int SUBKEY_SIZE = 28, BIT_MASK = 1, ROUND_KEY_SIZE = 48;
        int leftSubKey = 0, rightSubKey = 0;
        Arrays.fill(roundKeys, 0);
        for (int i = 0; i < SUBKEY_SIZE; i++) {
            leftSubKey = (leftSubKey << 1) | (int) ((sourceKey >> (keyPC1[i] - 1)) & BIT_MASK);
            rightSubKey = (rightSubKey << 1) | (int) ((sourceKey >> (keyPC1[i + SUBKEY_SIZE] - 1)) & BIT_MASK);
        }
        for (int i = 0; i < ROUND_COUNT; i++) {
            leftSubKey = (int) (((leftSubKey << keyShifts[i]) | (leftSubKey >> (SUBKEY_SIZE - keyShifts[i]))) & SUBKEY_MASK);
            rightSubKey = (int) (((rightSubKey << keyShifts[i]) | (rightSubKey >> (SUBKEY_SIZE - keyShifts[i]))) & SUBKEY_MASK);
            subKey = leftSubKey;
            roundKey = subKey & SUBKEY_MASK;
            roundKey <<= SUBKEY_SIZE;
            subKey = rightSubKey;
            roundKey |= subKey & SUBKEY_MASK;
            for (int j = 0; j < ROUND_KEY_SIZE; j++) {
                roundKeys[i] = (roundKeys[i] << 1) | ((roundKey >> (keyPC2[j] - 1)) & BIT_MASK);
            }
        }
        return roundKeys;
    }

    public int[] getInversePermutation(int[] permutation) {
        int[] inversePermutation = new int[permutation.length];
        for (int i = 0; i < permutation.length; i++) {
            inversePermutation[permutation[i] - 1] = i + 1;
        }
        return inversePermutation;
    }

    public byte[] decrypt(byte[] source, long key) {
        final int subBlockCount = Long.SIZE / Byte.SIZE;
        int blockCount = source.length / subBlockCount + (source.length % subBlockCount != 0 ? 1 : 0), currentSubBlock = 0, currentDecryptedBlock = 0;
        long block = 0, subBlock = 0;
        final long BYTE_MASK = 255;
        byte[] decryptedSource = new byte[source.length];
        Arrays.fill(decryptedSource, (byte) 0);
        long[] roundKeys = generateRoundKeys(key);
        reverseArray(roundKeys);
        for (int i = 0; i < blockCount; i++) {
            block = 0;
            for (int j = 0; j < subBlockCount; j++) {
                subBlock = source[currentSubBlock];
                block = (block << Byte.SIZE) | (subBlock & BYTE_MASK);
                ++currentSubBlock;
            }
            long decryptedBlock = encryptBlock(block, roundKeys);
            for (int j = subBlockCount - 1; j >= 0; j--) {
                decryptedSource[currentDecryptedBlock] |= (byte) ((decryptedBlock >> (Byte.SIZE * j)) & BYTE_MASK);
                ++currentDecryptedBlock;
            }
        }
        return decryptedSource;
    }

    public void reverseArray(long[] array) {
        long temp;
        for (int i = 0; i < array.length / 2; i++) {
            temp = array[i];
            array[i] = array[array.length - i - 1];
            array[array.length - i - 1] = temp;
        }
    }
}
