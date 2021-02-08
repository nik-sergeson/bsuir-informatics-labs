package lab4.src;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.Random;

import static numbers.BigIntHelper.byteSize;
import static numbers.BigIntHelper.getRandomBigInt;
import static numbers.BigIntHelper.modInverse;


public class RSA {
    protected static Random RANDOM = new Random();
    protected final int PRIME_SIZE = 1024;
    private PrivateKey currentPrivateKey;
    private PublicKey currentPublicKey;

    public PrivateKey getCurrentPrivateKey() {
        return currentPrivateKey;
    }

    public PublicKey getCurrentPublicKey() {
        return currentPublicKey;
    }

    public void generateKeys() {
        BigInteger p = BigInteger.probablePrime(PRIME_SIZE, RANDOM), q = p.nextProbablePrime(), n = p.multiply(q),
                euler_func = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE)),
                e = getRandomBigInt(BigInteger.ONE, euler_func);
        while (!e.gcd(euler_func).equals(BigInteger.ONE))
            e = getRandomBigInt(BigInteger.ONE, euler_func);
        BigInteger d = e.modInverse(euler_func);
        currentPrivateKey = new PrivateKey(d, n);
        currentPublicKey = new PublicKey(e, n);
    }

    public byte[] encrypt(byte[] source, PublicKey publicKey) {
        int moduleSize=byteSize(publicKey.getN()), sourceBlockLength = moduleSize-2, encBlockLength = moduleSize, sourceIterator = 0, encryptedIterator = 0;
        byte[] block = new byte[sourceBlockLength], encryptedBlock, encryptedSource = new byte[(source.length / sourceBlockLength + (source.length % sourceBlockLength == 0 ? 0 : 1)) * encBlockLength];
        BigInteger currentBlock;
        while (sourceIterator < source.length) {
            if(sourceIterator+sourceBlockLength-1<source.length) {
                System.arraycopy(source, sourceIterator, block, 0, sourceBlockLength);
                sourceIterator += sourceBlockLength;
            }
            else{
                Arrays.fill(block, (byte) 0);
                System.arraycopy(source, sourceIterator, block, sourceBlockLength-(source.length-sourceIterator), source.length-sourceIterator);
                sourceIterator += source.length-sourceIterator;
            }
            currentBlock = new BigInteger(1, block);
            encryptedBlock = currentBlock.modPow(publicKey.getE(), publicKey.getN()).toByteArray();
            System.arraycopy(encryptedBlock, 0, encryptedSource, encryptedIterator+(encBlockLength-encryptedBlock.length), encryptedBlock.length);
            encryptedIterator += encBlockLength;
        }
        return encryptedSource;
    }

    public byte[] decrypt(byte[] source, PrivateKey privateKey) {
        int sourceBlockLength = byteSize(privateKey.getN()), sourceIterator = 0, decryptedIterator = 0;
        byte[] block = new byte[sourceBlockLength], decryptedBlock, decryptedSource = new byte[source.length];
        BigInteger currentBlock;
        while (sourceIterator < source.length) {
            System.arraycopy(source, sourceIterator, block, 0, sourceBlockLength);
            sourceIterator+=sourceBlockLength;
            currentBlock = new BigInteger(1, block);
            decryptedBlock = currentBlock.modPow(privateKey.getD(), privateKey.getN()).toByteArray();
            System.arraycopy(decryptedBlock, 0, decryptedSource, decryptedIterator, decryptedBlock.length);
            decryptedIterator+=decryptedBlock.length;
        }
        return decryptedSource;
    }
}
