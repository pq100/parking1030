
from typing import Optional

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from schema.payment import PaymentBase, Payment, PaymentList
from service.database import get_db
from service.payment import register, paymentlist, paymentone

router = APIRouter()

@router.post('/payment')
async def new_payment(payment: PaymentBase, db: Session = Depends(get_db)):
    print(payment)
    return register(db, payment)

@router.get('/paycheck', response_model=list[PaymentList])
async def paycheck(db: Session = Depends(get_db)):
    paycheck = paymentlist(db)
    return [PaymentList.model_validate(p) for p in paycheck]

@router.get('/payment/{pno}', response_model=Optional[Payment])
async def payment_one(pno: int, db: Session = Depends(get_db)):
    payment = paymentone(db, pno)
    if payment is None:
        raise HTTPException(404, 'Payment not found!')
    return Payment.model_validate(payment)
