import React from 'react';
import { useState } from 'react';
import axios from 'axios';

const SuggestRecipe = () => {
    const [inputValue, setInputValue] = useState('');
    const [response, setResponse] = useState('');
    const [loading, setLoading] = useState(false);

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
      };
    
    const handleButtonClick = async () => {
        try {
          setLoading(true);
          const serverResponse = await callServer(inputValue);
          setResponse(serverResponse.data);
        } catch (error) {
          console.error('Error calling server:', error);
        } finally {
          setLoading(false);
        }
    };
    
    const callServer = async (input) => {
        // Replace the URL with your actual server endpoint
        // const apiUrl = 'https://n8zgm9ipzf.execute-api.ap-southeast-2.amazonaws.com/Prod/recipe';
        const requestBody = { input };
    
        //return axios.get(apiUrl, requestBody);
        const config = {
            headers: {
              "Content-Type": "application/json"
            }
        };
        console.log('requestBody: ' + input);

        return axios.post("https://n8zgm9ipzf.execute-api.ap-southeast-2.amazonaws.com/Prod/recipe", 
        {data: requestBody }, config)
        // .then(response => {
        //   // axios.put(res.data, file, configBlop).then(res => console.log(res));
        //   //setLines(response.data);
        //   console.log("recipe suggested " + response.data);
        // });
    };

    return (

        <div className="container">
            <h2>Look up Recipe:</h2>
            <input
                type="text"
                value={inputValue}
                onChange={handleInputChange}
                placeholder="Type here"
            /> 
            <button onClick={handleButtonClick} disabled={loading}>
            {loading ? 'Calling Server...' : 'Call Server'}
            </button>
            <div>
                <strong>Server Response:</strong> {response}
            </div>    

        </div>
      );
    };
    
    export default SuggestRecipe;