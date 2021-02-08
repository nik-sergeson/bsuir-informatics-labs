package numbers;

import java.nio.ByteBuffer;


public class IntHelper {
    public static final byte[] intToByteArray(int value) {
        return new byte[]{
                (byte) (value >>> 24),
                (byte) (value >>> 16),
                (byte) (value >>> 8),
                (byte) value};
    }

    public static int fromByteArray(byte[] bytes) {
        int num = 0;
        for (int i = bytes.length - 1; i >= 0; i--) {
            num = num | (bytes[i] << (bytes.length - i - 1));
        }
        return num;
    }
}
