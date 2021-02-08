package lab1_2.src;

import lab1_2.src.ScramblerBitManager;

import java.nio.charset.StandardCharsets;


public class Scrambler {
    private int[] registers;
    private int key;
    private int size;
    private ScramblerBitManager bitManager;

    public Scrambler(int size, int key, ScramblerBitManager bitManager) {
        registers = new int[size];
        this.size = size;
        this.key = key;
        this.bitManager = bitManager;
    }

    private void resetState() {
        final int BIT_MASK = 1;
        int key = this.key;
        for (int i = size - 1; i >= 0; i--) {
            registers[i] = key & BIT_MASK;
            key >>= 1;
        }
    }

    public byte[] encrypt(byte[] data) {
        resetState();
        byte[] encryptedBytes = new byte[data.length];
        byte currentByte, encryptedByte;
        final byte BIT_MASK = 1;
        for (int i = 0; i < data.length; i++) {
            currentByte = data[i];
            encryptedByte = 0;
            for (int j = 0; j < Byte.SIZE; j++) {
                encryptedByte <<= 1;
                encryptedByte |= bitManager.getBit(registers, (currentByte >> (Byte.SIZE - j - 1)) & BIT_MASK);
            }
            encryptedBytes[i] = encryptedByte;
        }
        return encryptedBytes;
    }

    public byte[] decrypt(byte[] data) {
        resetState();
        byte[] decryptedBytes = new byte[data.length];
        byte currentByte, decrypedByte;
        final byte BIT_MASK = 1;
        for (int i = 0; i < data.length; i++) {
            currentByte = data[i];
            decrypedByte = 0;
            for (int j = 0; j < Byte.SIZE; j++) {
                decrypedByte <<= 1;
                decrypedByte |= bitManager.getBit(registers, (currentByte >> (Byte.SIZE - j - 1)) & BIT_MASK);
            }
            decryptedBytes[i] = decrypedByte;
        }
        return decryptedBytes;
    }
}
