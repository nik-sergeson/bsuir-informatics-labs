package lab1_2.src;


public class EightBitManager implements ScramblerBitManager {
    public final int SIZE = 8;

    @Override
    public byte getBit(int[] registers, int sourceBit) {
        int encBit = registers[SIZE - 1], firstBit = (registers[SIZE - 1] ^ registers[SIZE - 2]) ^ registers[0];
        byte cipherBit = (byte) (sourceBit ^ encBit);
        for (int i = registers.length - 1; i > 0; i--)
            registers[i] = registers[i - 1];
        registers[0] = firstBit;
        return cipherBit;
    }
}
