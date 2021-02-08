package lab7.src;

import files.FileHelper;

import java.io.IOException;
import java.math.BigInteger;


public class Lab7 {
    public static void main(String[] args) throws IOException {
        BigInteger p = new BigInteger("785963102379428822376694789446897396207498568951"),
                a = new BigInteger("317689081251325503476317476413827693272746955927"),
                b = new BigInteger("790528966078787587181205720257185354321100651934");
        EllipticCurvePoint basePoint = new EllipticCurvePoint(new BigInteger("771507216262649826170648268565579889907769254176"), new BigInteger("390157510246556628525279459266514995562533196655"));
        EllipticCurve curve = new EllipticCurve(a, b, p);
        PrivateKey user1PrivateKey = PrivateKey.generateKey(curve.orderLowerBound()), user2PrivateKey = PrivateKey.generateKey(curve.orderLowerBound());
        PublicKey user1PublicKey = new PublicKey(basePoint, curve, user1PrivateKey), user2PublicKey = new PublicKey(basePoint, curve, user2PrivateKey);
        String source = FileHelper.fileToString(args[0]);
        EllipticCurveCipher cipher = new EllipticCurveCipher(curve, basePoint);
        byte[] encrypted = cipher.encrypt(source.getBytes(), user1PrivateKey, user2PublicKey);
        System.out.println(new String(encrypted));
        byte[] decrypted = cipher.decrypt(encrypted, user2PrivateKey, user1PublicKey);
        System.out.println(new String(decrypted));
    }
}
