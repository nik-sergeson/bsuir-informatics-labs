package numbers;

import java.math.BigInteger;
import java.util.Random;


public class BigIntHelper {
    protected static Random RANDOM = new Random();

    public static BigInteger sqrt(BigInteger n) {
        BigInteger a = BigInteger.ONE;
        BigInteger b = n.shiftRight(5).add(BigInteger.valueOf(8));
        while (b.compareTo(a) >= 0) {
            BigInteger mid = a.add(b).shiftRight(1);
            if (mid.multiply(mid).compareTo(n) > 0) {
                b = mid.subtract(BigInteger.ONE);
            } else {
                a = mid.add(BigInteger.ONE);
            }
        }
        return a.subtract(BigInteger.ONE);
    }

    public static BigInteger getRandomBigInt(BigInteger min, BigInteger max) {
        if (max.compareTo(min) < 0) {
            BigInteger tmp = min;
            min = max;
            max = tmp;
        } else if (max.compareTo(min) == 0) {
            return min;
        }
        max = max.add(BigInteger.ONE);
        BigInteger range = max.subtract(min);
        int length = range.bitLength();
        BigInteger result = new BigInteger(length, RANDOM);
        while (result.compareTo(range) >= 0) {
            result = new BigInteger(length, RANDOM);
        }
        result = result.add(min);
        return result;
    }

    public static BigInteger[] exctendedgcd(BigInteger a, BigInteger b) {
        BigInteger[] result = new BigInteger[2], factor;
        if (a.equals(BigInteger.ZERO)) {
            result[0] = BigInteger.ZERO;
            result[1] = BigInteger.ONE;
            return result;
        }
        factor = exctendedgcd(b.mod(a), a);
        result[0] = factor[1].subtract(b.divide(a).multiply(factor[0]));
        result[1] = factor[0];
        return result;
    }

    public static BigInteger modInverse(BigInteger num, BigInteger module) {
        return exctendedgcd(num, module)[0];
    }

    public static int byteSize(BigInteger num) {
        return num.toByteArray().length;
    }

}
