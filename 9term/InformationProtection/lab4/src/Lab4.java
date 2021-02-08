package lab4.src;

import files.FileHelper;

import java.io.IOException;
import java.math.BigInteger;
import java.util.Arrays;


public class Lab4 {
    public static void main(String[] args) throws IOException {
        RSA rsa = new RSA();
        rsa.generateKeys();
        String source = FileHelper.fileToString(args[0]);
        byte[] encrypted = rsa.encrypt(source.getBytes(), rsa.getCurrentPublicKey());
        System.out.println(new String(encrypted));
        byte[] decrypted = rsa.decrypt(encrypted, rsa.getCurrentPrivateKey());
        System.out.println(new String(decrypted));
    }
}
