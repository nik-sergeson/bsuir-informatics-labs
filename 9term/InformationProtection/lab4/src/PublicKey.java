package lab4.src;

import java.math.BigInteger;


public class PublicKey{
    private BigInteger e;
    private BigInteger n;

    public BigInteger getE() {
        return e;
    }

    public BigInteger getN() {
        return n;
    }

    public PublicKey(BigInteger e, BigInteger n) {
        this.e = e;
        this.n = n;
    }
}