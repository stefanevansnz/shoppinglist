import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MockList from "./component/list/MockList"
import FileUpload from "./component/file-upload/FileUpload";
import SuggestRecipe from "./component/suggest-recipe/SuggestRecipe"
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
      <MockList />
      <SuggestRecipe />      
      <header className="App-header">
          <h2>Shopping List v0.1</h2>
          <ul>
          {posts.map(post => (
            <li id={post.id} key={post.id}>{post.item}</li>
          ))}
          </ul>
      </header>
      <FileUpload />
    </div>
    
  );
}

export default App;
