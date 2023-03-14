//const fetch = require('node-fetch');

const apiUrl = 'https://example.com/wp-json/wp/v2/posts'; // 替换成您的WordPress站点URL
const authToken = 'Bearer <YOUR_TOKEN>'; // 替换成您的WordPress REST API身份验证令牌

const posts = [
  {
    title: '文章标题1',
    content: '文章内容1',
    status: 'publish',
  },
  {
    title: '文章标题2',
    content: '文章内容2',
    status: 'publish',
  },
  // ... 添加更多文章
];

async function createPosts() {
  for (const post of posts) {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': authToken,
      },
      body: JSON.stringify(post),
    });
    
    const data = await response.json();
    
    console.log(`文章 "${data.title.rendered}" 已发布，ID: ${data.id}`);
  }
}

createPosts();