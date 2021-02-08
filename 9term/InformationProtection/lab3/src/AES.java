package lab3.src;

import java.util.HashMap;


public class AES {
    public final int BLOCK_SIZE = 128, STATE_COL_COUNT = BLOCK_SIZE / 32, KEY_SIZE = 128, KEY_COL_COUNT = KEY_SIZE / 32, ROW_COUNT = 4;
    private int roundCount;
    private int[][] sBox, rCon, invSBox;
    private static int[][] dirMixMatrix = {
            {2, 3, 1, 1},
            {1, 2, 3, 1},
            {1, 1, 2, 3},
            {3, 1, 1, 2}},
            invDirMixMatrix = {
                    {14, 11, 13, 9},
                    {9, 14, 11, 13},
                    {13, 9, 14, 11},
                    {11, 13, 9, 14}
            };

    public AES(int[][] sBox, int[][] rCon, int[][] invSBox, HashMap<Integer, HashMap<Integer, Integer>> roundCount) {
        this.sBox = sBox;
        this.rCon = rCon;
        this.invSBox = invSBox;
        this.roundCount = roundCount.get(KEY_COL_COUNT).get(STATE_COL_COUNT);
    }

    public byte[] encrypt(byte[] data, byte[] key) {
        final int BYTE_MASK = 255;
        int currentBlock = 0, currentEncryptedBlock = 0, stateSize = STATE_COL_COUNT * ROW_COUNT, encryptedLength = ((data.length / stateSize + (data.length % stateSize == 0 ? 0 : 1)) * stateSize);
        int[][] state, splitKey = new int[ROW_COUNT][KEY_COL_COUNT];
        byte[] encryptedData = new byte[encryptedLength];
        for (int i = 0; i < KEY_COL_COUNT; i++) {
            for (int j = 0; j < ROW_COUNT; j++) {
                if (i * KEY_COL_COUNT + j < key.length)
                    splitKey[j][i] = key[i * KEY_COL_COUNT + j];
                else
                    splitKey[j][i] = 1;
            }
        }
        int[][] expandedKey = expandKey(splitKey);
        while (currentBlock < data.length) {
            state = new int[ROW_COUNT][STATE_COL_COUNT];
            for (int i = 0; i < STATE_COL_COUNT; i++) {
                for (int j = 0; j < ROW_COUNT; j++) {
                    if (currentBlock < data.length)
                        state[j][i] = data[currentBlock];
                    else
                        state[j][i] = 0;
                    ++currentBlock;
                }
            }
            int[][] encryptedState = encryptState(state, expandedKey);
            for (int i = 0; i < STATE_COL_COUNT; i++) {
                for (int j = 0; j < ROW_COUNT; j++) {
                    encryptedData[currentEncryptedBlock] = (byte) encryptedState[j][i];
                    ++currentEncryptedBlock;
                }
            }
        }
        return encryptedData;
    }

    public int[][] encryptState(int[][] state, int[][] expandedKey) {
        int[][] encryptedState = state.clone();
        addRoundKey(encryptedState, getKeyForRound(expandedKey, 0));
        for (int i = 1; i < roundCount; i++) {
            round(encryptedState, getKeyForRound(expandedKey, i));
        }
        finalRound(encryptedState, getKeyForRound(expandedKey, roundCount));
        return encryptedState;
    }

    public void round(int[][] state, int[][] roundKey) {
        substituteBytes(state);
        shiftRows(state);
        mixColumns(state);
        addRoundKey(state, roundKey);
    }

    public void finalRound(int[][] state, int[][] roundKeys) {
        substituteBytes(state);
        shiftRows(state);
        addRoundKey(state, roundKeys);
    }

    public void substituteBytes(int[][] state) {
        int stateCell;
        final int FOUR_BIT_MASK = 15;
        for (int i = 0; i < STATE_COL_COUNT; i++) {
            for (int j = 0; j < ROW_COUNT; j++) {
                stateCell = state[j][i];
                state[j][i] = sBox[stateCell >> (Byte.SIZE / 2)][stateCell & FOUR_BIT_MASK];
            }
        }
    }

    public void shiftRows(int[][] state) {
        int[] tempRow = new int[STATE_COL_COUNT];
        for (int i = 1; i < ROW_COUNT; i++) {
            for (int j = 0; j < STATE_COL_COUNT; j++) {
                tempRow[(j - i + STATE_COL_COUNT) % STATE_COL_COUNT] = state[i][j];
            }
            for (int j = 0; j < STATE_COL_COUNT; j++) {
                state[i][j] = tempRow[j];
            }
        }

    }

    public void mixColumns(int[][] state) {
        int[] column = new int[ROW_COUNT];
        int mulResult = 0;
        for (int i = 0; i < STATE_COL_COUNT; i++) {
            for (int j = 0; j < ROW_COUNT; j++)
                column[j] = state[j][i];
            for (int j = 0; j < ROW_COUNT; j++) {
                int result = 0;
                for (int k = 0; k < ROW_COUNT; k++) {
                    mulResult = multiplyPolynoms(dirMixMatrix[j][k], column[k]);
                    result ^= mulResult;
                }
                state[j][i] = result;
            }
        }
    }

    public int multiplyPolynoms(int x, int y) {
        int result = 0, bit;
        final int MOD_POLYNOM = 27, MAX_POWER = 8, BIT_MASK = 1, HIGH_BIT = 128, BYTE_MASK = 255;
        for (int i = 0; i < MAX_POWER; i++) {
            bit = y & BIT_MASK;
            if (bit != 0)
                result ^= x;
            bit = x & HIGH_BIT;
            x = (x << 1) & BYTE_MASK;
            if (bit != 0)
                x ^= MOD_POLYNOM;
            y >>= 1;
        }
        return result;
    }

    public void addRoundKey(int[][] state, int[][] roundKey) {
        for (int i = 0; i < STATE_COL_COUNT; i++) {
            for (int j = 0; j < ROW_COUNT; j++) {
                state[j][i] = state[j][i] ^ roundKey[j][i];
            }
        }
    }

    public int[][] expandKey(int[][] cipherKey) {
        int[][] expandedKey = new int[ROW_COUNT][STATE_COL_COUNT * (roundCount + 1)];
        if (KEY_COL_COUNT < 6) {
            for (int i = 0; i < KEY_COL_COUNT; i++) {
                for (int j = 0; j < ROW_COUNT; j++) {
                    expandedKey[j][i] = cipherKey[j][i];
                }
            }
            for (int i = KEY_COL_COUNT; i < STATE_COL_COUNT * (roundCount + 1); i += KEY_COL_COUNT) {
                int[] prevCol = substituteBytesColumn(shiftKeyCol(expandedKey, i - 1));
                for (int j = 0; j < ROW_COUNT; j++) {
                    expandedKey[j][i] = expandedKey[j][i - KEY_COL_COUNT] ^ prevCol[j] ^ rCon[j][i / KEY_COL_COUNT - 1];
                }
                for (int j = 1; j < KEY_COL_COUNT && i + j < STATE_COL_COUNT * (roundCount + 1); j++) {
                    for (int k = 0; k < ROW_COUNT; k++) {
                        expandedKey[k][i + j] = expandedKey[k][i + j - KEY_COL_COUNT] ^ expandedKey[k][i + j - 1];
                    }
                }
            }
        } else {
            for (int i = 0; i < KEY_COL_COUNT; i++) {
                for (int j = 0; j < ROW_COUNT; j++) {
                    expandedKey[j][i] = cipherKey[j][i];
                }
            }
            for (int i = KEY_COL_COUNT; i < STATE_COL_COUNT * (roundCount + 1); i += KEY_COL_COUNT) {
                int[] prevCol = substituteBytesColumn(shiftKeyCol(expandedKey, i - 1));
                for (int j = 0; j < ROW_COUNT; j++) {
                    expandedKey[j][i] = expandedKey[j][i - KEY_COL_COUNT] ^ prevCol[j] ^ rCon[j][i / KEY_COL_COUNT - 1];
                }
                for (int j = 0; j < 4; j++) {
                    for (int k = 0; k < ROW_COUNT; k++) {
                        expandedKey[k][i + j] = expandedKey[k][i + j - KEY_COL_COUNT] ^ expandedKey[k][i + j - 1];
                    }
                }
                for (int j = 0; j < ROW_COUNT; j++) {
                    prevCol[j] = expandedKey[j][i + 3];
                }
                prevCol = substituteBytesColumn(prevCol);
                for (int j = 0; j < ROW_COUNT; j++) {
                    expandedKey[j][i + 4] = expandedKey[j][i + 4 - KEY_COL_COUNT] ^ prevCol[j];
                }
                for (int j = 5; j < KEY_COL_COUNT; j++) {
                    for (int k = 0; k < ROW_COUNT; k++) {
                        expandedKey[k][i + j] = expandedKey[k][i + j - KEY_COL_COUNT] ^ expandedKey[k][i + j - 1];
                    }
                }
            }
        }
        return expandedKey;
    }

    public int[] substituteBytesColumn(int[] col) {
        int keyCell;
        int[] substCol = col.clone();
        final int FOUR_BIT_MASK = 15;
        for (int j = 0; j < ROW_COUNT; j++) {
            keyCell = substCol[j];
            substCol[j] = sBox[keyCell >> (Byte.SIZE / 2)][keyCell & FOUR_BIT_MASK];
        }
        return substCol;
    }

    public int[] shiftKeyCol(int[][] expandedKey, int col) {
        int[] keyCol = new int[ROW_COUNT];
        for (int i = 0; i < ROW_COUNT - 1; i++) {
            keyCol[i] = expandedKey[i + 1][col];
        }
        keyCol[ROW_COUNT - 1] = expandedKey[0][col];
        return keyCol;
    }

    public int[][] getKeyForRound(int[][] expandedKey, int round) {
        int[][] roundKey = new int[ROW_COUNT][STATE_COL_COUNT];
        for (int i = round * STATE_COL_COUNT; i < (round + 1) * STATE_COL_COUNT; i++) {
            for (int j = 0; j < ROW_COUNT; j++) {
                roundKey[j][i % STATE_COL_COUNT] = expandedKey[j][i];
            }
        }
        return roundKey;
    }

    public byte[] decrypt(byte[] data, byte[] key) {
        final int BYTE_MASK = 255;
        int currentBlock = 0, currentDecryptedBlock = 0;
        int[][] state, splitKey = new int[ROW_COUNT][KEY_COL_COUNT];
        byte[] decryptedData = new byte[data.length];
        for (int i = 0; i < KEY_COL_COUNT; i++) {
            for (int j = 0; j < ROW_COUNT; j++) {
                if (i * KEY_COL_COUNT + j < key.length)
                    splitKey[j][i] = key[i * KEY_COL_COUNT + j];
                else
                    splitKey[j][i] = 1;
            }
        }
        int[][] expandedKey = expandKey(splitKey);
        while (currentBlock < data.length) {
            state = new int[ROW_COUNT][STATE_COL_COUNT];
            for (int i = 0; i < STATE_COL_COUNT; i++) {
                for (int j = 0; j < ROW_COUNT; j++) {
                    state[j][i] = data[currentBlock] & BYTE_MASK;
                    ++currentBlock;
                }
            }
            int[][] decryptedState = decryptState(state, expandedKey);
            for (int i = 0; i < STATE_COL_COUNT; i++) {
                for (int j = 0; j < ROW_COUNT; j++) {
                    decryptedData[currentDecryptedBlock] = (byte) decryptedState[j][i];
                    ++currentDecryptedBlock;
                }
            }
        }
        return decryptedData;
    }

    public int[][] decryptState(int[][] state, int[][] expandedKey) {
        int[][] decryptedState = state.clone();
        addRoundKey(decryptedState, getKeyForRound(expandedKey, roundCount));
        for (int i = roundCount - 1; i > 0; i--) {
            invRound(decryptedState, getKeyForRound(expandedKey, i));
        }
        finalInvRound(decryptedState, getKeyForRound(expandedKey, 0));
        return decryptedState;
    }

    public void invRound(int[][] state, int[][] roundKey) {
        invShiftRows(state);
        invSubstituteBytes(state);
        addRoundKey(state, roundKey);
        invMixColumns(state);
    }

    public void finalInvRound(int[][] state, int[][] roundKeys) {
        invSubstituteBytes(state);
        invShiftRows(state);
        addRoundKey(state, roundKeys);
    }

    public void invSubstituteBytes(int[][] state) {
        int stateCell;
        final int FOUR_BIT_MASK = 15;
        for (int i = 0; i < STATE_COL_COUNT; i++) {
            for (int j = 0; j < ROW_COUNT; j++) {
                stateCell = state[j][i];
                state[j][i] = invSBox[stateCell >> (Byte.SIZE / 2)][stateCell & FOUR_BIT_MASK];
            }
        }
    }

    public void invShiftRows(int[][] state) {
        int[] tempRow = new int[STATE_COL_COUNT];
        for (int i = 1; i < ROW_COUNT; i++) {
            for (int j = 0; j < STATE_COL_COUNT; j++) {
                tempRow[(j + i) % STATE_COL_COUNT] = state[i][j];
            }
            for (int j = 0; j < STATE_COL_COUNT; j++) {
                state[i][j] = tempRow[j];
            }
        }

    }

    public void invMixColumns(int[][] state) {
        int[] column = new int[ROW_COUNT];
        int mulResult = 0;
        for (int i = 0; i < STATE_COL_COUNT; i++) {
            for (int j = 0; j < ROW_COUNT; j++)
                column[j] = state[j][i];
            for (int j = 0; j < ROW_COUNT; j++) {
                int result = 0;
                for (int k = 0; k < ROW_COUNT; k++) {
                    mulResult = multiplyPolynoms(invDirMixMatrix[j][k], column[k]);
                    result ^= mulResult;
                }
                state[j][i] = result;
            }
        }
    }
}
