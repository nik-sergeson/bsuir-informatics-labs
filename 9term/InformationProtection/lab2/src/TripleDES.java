package lab2.src;


public class TripleDES {
    private DES desCipher;

    public TripleDES(DES desCipher) {
        this.desCipher = desCipher;
    }

    public byte[] encrypt(long key1, long key2, long key3, byte[] source) {
        return desCipher.encrypt(desCipher.encrypt(desCipher.encrypt(source, key1), key2), key3);
    }

    public byte[] decrypt(long key1, long key2, long key3, byte[] source) {
        return desCipher.decrypt(desCipher.decrypt(desCipher.decrypt(source, key3), key2), key1);
    }
}
