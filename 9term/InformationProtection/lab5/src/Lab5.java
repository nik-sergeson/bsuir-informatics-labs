package lab5.src;

import files.FileHelper;

import java.io.IOException;
import java.util.Arrays;


public class Lab5 {
    public static void main(String[] args) throws IOException {
        SHA1 sha1 = new SHA1();
        String source = FileHelper.fileToString(args[0]);
        sha1.addHash(source.getBytes());
        byte[] shaValue = sha1.getComputedHash();
        System.out.print(new String(shaValue));
        for (int i = 0; i < 255; i++) {
            sha1.resetState();
            sha1.addHash((source + (char)i).getBytes());
            if (Arrays.equals(sha1.getComputedHash(), shaValue))
                throw new AssertionError();
        }
    }
}