package lab7.src;

import java.math.BigInteger;

import static numbers.BigIntHelper.getRandomBigInt;


public class PrivateKey {
    private BigInteger key;

    private PrivateKey(BigInteger key){
        this.key=key;
    }

    public BigInteger getKey() {
        return key;
    }

    public static PrivateKey generateKey(BigInteger curveOrder){
        return new PrivateKey(getRandomBigInt(curveOrder.subtract(curveOrder.divide(BigInteger.valueOf(10))), curveOrder));
    }
}
