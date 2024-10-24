from sqlalchemy.orm import Session

from models.payment import Payment
from schema.payment import PaymentBase

def register(db: Session, product: PaymentBase):
    product = Payment(**product.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    print(product)

    return product

def paymentlist(db: Session):
    return db.query(Payment.name, Payment.price,
                    Payment.regdate, Payment.pno) \
        .order_by(Payment.pno.desc()).all()


def paymentone(db: Session, pno: int):
    return db.query(Payment) \
        .filter(Payment.pno == pno).first()
