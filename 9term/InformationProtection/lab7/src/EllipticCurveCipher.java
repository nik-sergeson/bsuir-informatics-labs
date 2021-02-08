package lab7.src;

import numbers.BigIntHelper;

import java.math.BigInteger;

import static numbers.IntHelper.fromByteArray;


public class EllipticCurveCipher {
    private EllipticCurve curve;
    private EllipticCurvePoint basePoint;

    public EllipticCurveCipher(EllipticCurve curve, EllipticCurvePoint basePoint) {
        this.curve = curve;
        this.basePoint = basePoint;
    }

    public byte[] encrypt(byte[] source, PrivateKey senderKey, PublicKey receiverKey) {
        int currentByte = 0, currentEncryptedByte = 0, blockSize = BigIntHelper.byteSize(curve.getModule());
        byte[] encrtyptedSource = new byte[source.length * blockSize], encryptedBlock;
        EllipticCurvePoint key = receiverKey.getKey().multiplyScalar(senderKey.getKey(), curve);
        while (currentByte < source.length) {
            BigInteger c1 = BigInteger.valueOf(source[currentByte] - Byte.MIN_VALUE).multiply(key.getX()).mod(curve.getModule());
            encryptedBlock = c1.toByteArray();
            System.arraycopy(encryptedBlock, 0, encrtyptedSource, currentEncryptedByte + (blockSize - encryptedBlock.length), encryptedBlock.length);
            ++currentByte;
            currentEncryptedByte += blockSize;
            if (currentByte < source.length) {
                BigInteger c2 = BigInteger.valueOf(source[currentByte] - Byte.MIN_VALUE).multiply(key.getY()).mod(curve.getModule());
                encryptedBlock = c2.toByteArray();
                System.arraycopy(encryptedBlock, 0, encrtyptedSource, currentEncryptedByte + (blockSize - encryptedBlock.length), encryptedBlock.length);
                ++currentByte;
                currentEncryptedByte += blockSize;
            }
        }
        return encrtyptedSource;
    }

    public byte[] decrypt(byte[] source, PrivateKey receiverKey, PublicKey senderKey) {
        int currentByte = 0, currentDecryptedByte = 0, blockSize = BigIntHelper.byteSize(curve.getModule());
        byte[] decryptedSource = new byte[source.length / blockSize], block = new byte[blockSize];
        int m1, m2;
        EllipticCurvePoint key = senderKey.getKey().multiplyScalar(receiverKey.getKey(), curve);
        BigInteger xInverse = BigIntHelper.modInverse(key.getX(), curve.getModule()), yInverse = BigIntHelper.modInverse(key.getY(), curve.getModule());
        while (currentByte < source.length) {
            System.arraycopy(source, currentByte, block, 0, blockSize);
            m1 = fromByteArray((new BigInteger(block)).multiply(xInverse).mod(curve.getModule()).toByteArray());
            decryptedSource[currentDecryptedByte] = (byte) (m1 + Byte.MIN_VALUE);
            currentByte += blockSize;
            ++currentDecryptedByte;
            if (currentByte < source.length) {
                System.arraycopy(source, currentByte, block, 0, blockSize);
                m2 = fromByteArray((new BigInteger(block)).multiply(yInverse).mod(curve.getModule()).toByteArray());
                decryptedSource[currentDecryptedByte] = (byte) (m2 + Byte.MIN_VALUE);
                currentByte += blockSize;
                ++currentDecryptedByte;
            }
        }
        return decryptedSource;
    }
}
