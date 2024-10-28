const regProductBtn = document.querySelector('#regProductBtn');
const productfrm = document.productfrm;

// 비동기 처리 구현 - async, await
/* regProductBtn.addEventListener('click', async () => {
    const formData = new FormData(productfrm);

    // FormData를 JSON 형태로 변환
    let jsondata = {};
    formData.forEach((val, key) => {
        jsondata[key] = val;
    });

    console.log(JSON.stringify(jsondata)); // 변환된 jsondata를 출력

    try {
        // REST API 호출
        const res = await fetch('http://127.0.0.1:8050/product', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsondata) // 변환된 JSON 데이터를 전송
        });

        if (!res.ok) {
            throw new Error('상품 등록 실패!! 상태 코드: ' + res.status);
        }

        const resData = await res.json();
        alert('상품 등록 성공!!');
        // 서버에서 받은 데이터 출력
        console.log(resData); // 전체 응답 출력
        console.log('상품 번호:', resData.pno);  // 상품 번호 출력
        console.log('상품명:', resData.name);  // 상품명 출력
        console.log('등록일:', resData.regdate);  // 등록일 출력

    } catch (error) {
        alert('상품 등록 실패!!');
        console.error('Error:', error.message);
    }
}); */
