package lab7.src;


public class PublicKey {
    private EllipticCurvePoint key;

    public EllipticCurvePoint getKey() {
        return key;
    }

    public PublicKey(EllipticCurvePoint basePoint, EllipticCurve curve, PrivateKey privateKey){
        this.key=basePoint.multiplyScalar(privateKey.getKey(), curve);
    }
}
