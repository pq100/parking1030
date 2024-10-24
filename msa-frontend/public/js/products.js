// 페이지 로드시 자동으로 실행
window.addEventListener('load', async () => {
    try {
        const products = await getProductList()
        //테스트용 const products = null;
        displayProductList(products);
    } catch (e) {
        console.log(e);
        alert('상품 목록 조회 실패!');
    }
});

// 회원 데이터 가져오기
const getProductList = async () => {
    let url = `${sessionStorage.getItem('productsrvURL')}/products`; // FastAPI 서버 URL
    const res = await fetch(url);
    if (res.ok) {
        const data = await res.json();
        return data;
    } else {
        throw new Error('상품 목록 fetch 실패!!');
    }
};

const displayProductList = (products) => {
    // 테스트용 products = [{'name: 테스트','','','','',''}]

    const productlist = document.querySelector('#product-list');  // 변수명 수정
    console.log(products);
    let html = '<ul>';
    for (const p of products) {
        html += `<li>
            상품명 : <a href="/product/${p.pno}">${p.name}</a>, 
            상품가격 : ${p.price}, 
            상품 등록일: ${p.regdate}
        </li>`;
    }
    html += '</ul>';  // HTML 닫는 태그 수정

    productlist.innerHTML = html;
};
