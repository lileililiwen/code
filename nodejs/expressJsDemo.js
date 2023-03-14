const express = require('express');
const app = express();
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

let posts = [
    { title: 'Post 1', content: 'Content 1' },
    { title: 'Post 2', content: 'Content 2' },
    { title: 'Post 3', content: 'Content 3' },
    { title: 'Post 4', content: 'Content 4' },
    { title: 'Post 5', content: 'Content 5' }
];

app.get('/', (req, res) => {
    const page = parseInt(req.query.page) || 1;
    const perPage = parseInt(req.query.perPage) || 5;
    const start = (page - 1) * perPage;
    const end = page * perPage;
    res.render('index', { posts: posts.slice(start, end) });
});

app.get('/create', (req, res) => {
    res.render('create');
});

app.post('/create', (req, res) => {
    const post = {
        title: req.body.title,
        content:req.body.content
    };
    posts.push(post);
    res.redirect('/');
});

app.get('/:id/update', (req, res) => {
    const id = parseInt(req.params.id);
    res.render('update', { post: posts[id] });
});

app.post('/:id/update',(req,res)=>{
   const id=parseInt(req.params.id);
   posts[id].title=req.body.title;
   posts[id].content=req.body.content;
   res.redirect('/');
});

app.get('/:id/delete',(req,res)=>{
   const id=parseInt(req.params.id);
   posts.splice(id,1);
   res.redirect('/');
});

app.listen(3000, () => console.log(`Example app listening on port ${3000}!`));