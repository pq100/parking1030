from pydantic import BaseModel


class PaymentBase(BaseModel):
    payid: str
    desc: str
    payment: int

class Payment(PaymentBase):
    payid: int
    regdate: str

    # ORM 맵핑을 위한 설정
    # 데이터베이스 테이블 각 행 <-> pydantic
    class Config:
        from_attribute=True



class PaymentList(BaseModel):
    payid: int
    payment: int
    regdate: str

    class Config:
        from_attributes=True