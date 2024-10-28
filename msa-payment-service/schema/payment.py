from pydantic import BaseModel
from typing import Optional

class PaymentBase(BaseModel):
    payment: str
    paydate: str
    parkingtime: str
    carnum: str

    class Config:
        orm_mode = True  # SQLAlchemy 모델과 연동 시 필요

class PaymentCreate(PaymentBase):
    pass  # 새로운 결제 생성 시 필요한 필드를 상속

class Payment(PaymentBase):
    payid: int

class PaymentList(BaseModel):
    payid: int
    payment: str
    paydate: str
    parkingtime: str
    carnum: str

    class Config:
        orm_mode = True
