package lab1_2.src;

import files.FileHelper;

import java.io.IOException;


public class Lab1_2 {
    public static void main(String[] args) throws IOException {
        EightBitManager bitManager = new EightBitManager();
        Scrambler scrambler = new Scrambler(bitManager.SIZE, 97, bitManager);
        String source = FileHelper.fileToString(args[0]);
        byte[] encrypted = scrambler.encrypt(source.getBytes());
        System.out.println(new String(encrypted));
        String decrypted = new String(scrambler.decrypt(encrypted));
        System.out.println(decrypted);
    }
}
