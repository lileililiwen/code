import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [news, setNews] = useState([]);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  useEffect(() => {
    axios.get('/api/news')
      .then(response => {
        setNews(response.data);
      });
  }, []);

  const handleSubmit = e => {
    e.preventDefault();
    axios.post('/api/news', { title, content })
      .then(response => {
        setNews([...news, response.data]);
        setTitle('');
        setContent('');
      });
  };

  const handleDelete = id => {
    axios.delete(`/api/news/${id}`)
      .then(() => {
        setNews(news.filter(n => n._id.$oid !== id));
      });
  };

  return (
    <div>
      <h1>News</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Title:
          <input type="text" value={title} onChange={e => setTitle(e.target.value)} />
        </label>
        <br />
        <label>
          Content:
          <textarea value={content} onChange={e => setContent(e.target.value)}></textarea>
        </label>
        <br />
        <button type="submit">Add News</button>
      </form>
      <ul>
        {news.map(n => (
          <li key={n._id.$oid}>
            <h2>{n.title}</h2>
            <p>{n.content}</p>
            <button onClick={() => handleDelete(n._id.$oid)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
