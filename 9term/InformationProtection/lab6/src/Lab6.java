package lab6.src;

import lab4.src.RSA;

import java.io.IOException;


public class Lab6 {
    public static void main(String[] args) {
        boolean signatureVerified = false;
        DigitalSignature digitalSignature = new DigitalSignature();
        RSA rsa = new RSA();
        rsa.generateKeys();
        try {
            digitalSignature.sign(args[0], rsa);
            signatureVerified = digitalSignature.verifySignature(args[0] + DigitalSignature.signedPostfix, rsa);
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.printf("Signature verified %s", signatureVerified ? "true" : "false");
    }
}
