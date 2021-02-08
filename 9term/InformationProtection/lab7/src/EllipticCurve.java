package lab7.src;

import java.math.BigInteger;

import static numbers.BigIntHelper.sqrt;


public class EllipticCurve {
    private BigInteger a, b, module;

    public EllipticCurve(BigInteger a, BigInteger b, BigInteger module) {
        this.a = a;
        this.b = b;
        this.module = module;
    }

    public BigInteger getA() {
        return a;
    }

    public BigInteger getB() {
        return b;
    }

    public BigInteger getModule() {
        return module;
    }

    public BigInteger orderLowerBound() {
        return module.add(BigInteger.ONE).subtract(sqrt(module).multiply(BigInteger.valueOf(2)));
    }

    public BigInteger orderUpperBound() {
        return module.add(BigInteger.ONE).add(sqrt(module).multiply(BigInteger.valueOf(2)));
    }
}
