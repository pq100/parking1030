from itertools import product
from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from service.database import get_db
from service.payment import register, paymentlist, paymentone

router = APIRouter()

@router.post('/payment')
async def new_product(product: ProductBase, db:Session=Depends(get_db)):
    print(product)

    return register(db, product)

@router.get('/payments', response_model=list[PaymentList])
async def list_products(db:Session=Depends(get_db)):
    products = productlist(db)

    # 테이블 조회환 결과 객체를
    # UserList 형식의 배열로 재생성
    return [PaymentList.model_validate(p) for p in products]


@router.get('/payment/{pno}', response_model=Optional[Payment])
async def product_one(pno: int, db:Session=Depends(get_db)):
    payment = paymentone(db, pno)

    # 상품이 조회되지 않을 경우 응답코드 404를 프론트엔드로 전달
    if product is None:

        raise HTTPException(404, 'Payment not found!')

    return Payment.model_validate(product)







