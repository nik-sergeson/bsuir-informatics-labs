package lab4.src;

import java.math.BigInteger;


public class PrivateKey {
    private BigInteger d;
    private BigInteger n;

    public BigInteger getD() {
        return d;
    }

    public BigInteger getN() {
        return n;
    }

    public PrivateKey(BigInteger d, BigInteger n) {
        this.d = d;
        this.n = n;
    }
}
