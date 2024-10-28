from sqlalchemy.orm import Session

from models.payment import Payment
from schema.payment import PaymentBase

def register(db: Session, payment: PaymentBase):
    payment = Payment(**payment.model_dump())
    db.add(payment)
    db.commit()
    db.refresh(payment)
    print(payment)

    return payment

def paymentlist(db: Session):
    return db.query(Payment.payment, Payment.paydate,
                    Payment.regdate, Payment.carnum) \
        .order_by(Payment.carnum.desc()).all()


def paymentone(db: Session, pno: int):
    return db.query(Payment) \
        .filter(Payment.payid == carnum).first()
