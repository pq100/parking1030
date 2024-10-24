document.addEventListener('DOMContentLoaded', ()=>{
    const token = sessionStorage.getItem('token');
    if (!token) {
        alert('로그인 하세요!');
        location.href ='/';
    }
});

const lougoutbtn = document.querySelector('#logoutbtn');
lougoutbtn.addEventListener('click', () => {
    sessionStorage.removeItem('token');
    location.href = '/';
})


