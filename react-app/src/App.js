import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get('https://n8zgm9ipzf.execute-api.ap-southeast-2.amazonaws.com/Prod/')
      .then(response => {
        setPosts(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
          Shopping List
          <ul>
          {posts.map(post => (
            <li key={post.id}>{post.item}</li>
          ))}
          </ul>
      </header>
    </div>
  );
}

export default App;
