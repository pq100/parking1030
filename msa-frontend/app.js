let createError = require('http-errors');
let express = require('express');
let path = require('path');
let request = require('request')
let port = 3000
var session = require('express-session')
// 환경변수 설정을 위해 템플릿 엔진 지정
const handlebars = require('express-handlebars')


let indexRouter = require('./public/index');

let app = express();

// handlebars 설정
// const hbs = handlebars.create({})
// app.engine('handlebars', hbs.engine);
// app.set('view engine', 'handlebars');
// app.set('views', path.join(__dirname, 'public/handlebars'));

// session 설정
// resave, save

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// 서버 시작
app.listen(port, () => {
  console.log(`frontend server on port ${port}`)
})

app.get('/auth/login', (req, res) => {
  // FastAPI 서버로 요청을 보냄
  request.get('http://localhost:8000/auth/login', (error, response, body) => {
    if (!error && response.statusCode == 200) {
      let data = JSON.parse(body);
      res.redirect(data.login_url);  // Naver 로그인 URL로 리다이렉트
    } else {
      res.status(500).send("Failed to get login URL from FastAPI server");
    }
  });
});





module.exports = app;



