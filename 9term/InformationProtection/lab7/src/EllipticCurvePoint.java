package lab7.src;

import java.math.BigInteger;

import static numbers.BigIntHelper.modInverse;


public class EllipticCurvePoint {
    private BigInteger x, y;

    public EllipticCurvePoint(BigInteger x, BigInteger y) {
        this.x = x;
        this.y = y;
    }

    public EllipticCurvePoint(EllipticCurvePoint other) {
        this.x = new BigInteger(other.x.toByteArray());
        this.y = new BigInteger(other.y.toByteArray());
    }

    public BigInteger getX() {
        return x;
    }

    public BigInteger getY() {
        return y;
    }


    public boolean isZero() {
        return y == null;
    }

    public static EllipticCurvePoint zero(BigInteger x) {
        return new EllipticCurvePoint(x, null);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        EllipticCurvePoint point = (EllipticCurvePoint) o;
        if (point.isZero())
            return this.isZero();
        else if (this.isZero())
            return point.isZero();
        if (x != null ? !x.equals(point.x) : point.x != null) return false;
        return y != null ? y.equals(point.y) : point.y == null;

    }

    public EllipticCurvePoint inverse() {
        return new EllipticCurvePoint(x, y.negate());
    }

    public EllipticCurvePoint add(EllipticCurvePoint other, EllipticCurve curve) {
        if (this.isZero())
            return new EllipticCurvePoint(other);
        else if (other.isZero())
            return new EllipticCurvePoint(this);
        else if (this.equals(other)) {
            return this.doublePoint(curve);
        } else if (x.equals(other.getX()))
            return zero(new BigInteger(x.toByteArray()));
        else {
            BigInteger numerator = other.getY().subtract(y), denumerator = other.getX().subtract(x);
            if (denumerator.signum() < 0) {
                numerator = numerator.negate();
                denumerator = denumerator.negate();
            }
            BigInteger lambda = numerator.multiply(modInverse(denumerator, curve.getModule())).mod(curve.getModule());
            BigInteger newX = (lambda.pow(2).subtract(x).subtract(other.getX())).mod(curve.getModule());
            BigInteger newY = (lambda.multiply(x.subtract(newX)).subtract(y)).mod(curve.getModule());
            return new EllipticCurvePoint(newX, newY);
        }
    }

    public EllipticCurvePoint doublePoint(EllipticCurve curve) {
        BigInteger lambda = x.pow(2).multiply(BigInteger.valueOf(3)).add(curve.getA()).multiply(modInverse(y.multiply(BigInteger.valueOf(2)), curve.getModule())).mod(curve.getModule());
        BigInteger newX = lambda.pow(2).subtract(x.multiply(BigInteger.valueOf(2))).mod(curve.getModule());
        BigInteger newY = lambda.multiply(x.subtract(newX)).subtract(y).mod(curve.getModule());
        return new EllipticCurvePoint(newX, newY);
    }

    public EllipticCurvePoint multiplyScalar(BigInteger num, EllipticCurve curve) {
        EllipticCurvePoint current = this, result = zero(new BigInteger(x.toByteArray()));
        for (int i = 0; i < num.bitLength(); i++) {
            if (num.testBit(i)) {
                result = result.add(current, curve);
            }
            current = current.doublePoint(curve);
        }
        return result;
    }
}
