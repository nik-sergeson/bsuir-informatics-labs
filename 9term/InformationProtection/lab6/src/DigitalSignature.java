package lab6.src;

import lab4.src.PrivateKey;
import lab4.src.PublicKey;
import lab4.src.RSA;
import lab5.src.SHA1;
import numbers.BigIntHelper;

import java.io.*;
import java.util.Arrays;


public class DigitalSignature {
    public static final String signedPostfix = "signed";
    public static final int BLOCK_SIZE = SHA1.BLOCK_SIZE * 2 * 1024 * 100;
    private SHA1 sha1;

    public DigitalSignature() {
        sha1 = new SHA1();
    }

    public void sign(String path, RSA rsa) throws IOException {
        File inFile = new File(path), outFile = new File(path + signedPostfix);
        FileInputStream source = new FileInputStream(inFile);
        FileOutputStream signed = new FileOutputStream(outFile);
        byte[] buffer = new byte[BLOCK_SIZE];
        int readBytes;
        sha1.resetState();
        while (true) {
            readBytes = source.read(buffer, 0, BLOCK_SIZE);
            if (readBytes < BLOCK_SIZE) {
                if (readBytes <= 0)
                    break;
                else {
                    byte[] tailBytes = new byte[readBytes];
                    System.arraycopy(buffer, 0, tailBytes, 0, readBytes);
                    sha1.addHash(tailBytes);
                    signed.write(tailBytes);
                }
            } else {
                sha1.addHash(buffer);
                signed.write(buffer);
            }
        }
        byte[] encryptedHash = rsa.encrypt(sha1.getComputedHash(), new PublicKey(rsa.getCurrentPrivateKey().getD(), rsa.getCurrentPrivateKey().getN()));
        signed.write(encryptedHash);
        source.close();
        signed.close();
    }

    public boolean verifySignature(String path, RSA rsa) throws IOException {
        File inFile = new File(path);
        FileInputStream signed = new FileInputStream(inFile);
        int readBytes, encHashLength=BigIntHelper.byteSize(rsa.getCurrentPublicKey().getN());
        byte[] buffer = new byte[BLOCK_SIZE], hash = new byte[encHashLength];
        long bytesToRead = inFile.length() - encHashLength;
        sha1.resetState();
        while (true) {
            if (bytesToRead >= BLOCK_SIZE)
                readBytes = signed.read(buffer, 0, BLOCK_SIZE);
            else
                readBytes = signed.read(buffer, 0, (int) bytesToRead);
            bytesToRead = bytesToRead - readBytes;
            if (readBytes < BLOCK_SIZE) {
                if (readBytes == 0)
                    break;
                else {
                    byte[] tailBytes = new byte[readBytes];
                    System.arraycopy(buffer, 0, tailBytes, 0, readBytes);
                    sha1.addHash(tailBytes);
                }
            } else {
                sha1.addHash(buffer);
            }
            if (bytesToRead == 0)
                break;
        }
        signed.read(hash, 0, encHashLength);
        hash = rsa.decrypt(hash, new PrivateKey(rsa.getCurrentPublicKey().getE(), rsa.getCurrentPublicKey().getN()));
        byte[] expectedHash = sha1.getComputedHash(), fileHash = new byte[expectedHash.length];
        System.arraycopy(hash, 0, fileHash, 0, expectedHash.length);
        return Arrays.equals(fileHash, expectedHash);
    }
}
