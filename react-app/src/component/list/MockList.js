import React from 'react';
import { useState } from 'react';
import axios from 'axios';

const MockList = () => {
    const [inputValue, setInputValue] = useState('');

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
      };
    return (

        <header className="App-header">
            <h2>Mock List v0.1</h2>
            <ul>
            </ul>
        </header>
      );
    };
export default MockList;