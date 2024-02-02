import React from 'react';
import Camera from 'react-html5-camera-photo';
import 'react-html5-camera-photo/build/css/index.css';
import { useCallback } from "react"; // import useCallback
import axios from 'axios';

const FileUpload = () => {
        const b64toBlob = function(b64Data, contentType, sliceSize) {
            contentType = contentType || '';
            sliceSize = sliceSize || 512;

            console.log('b64toBlob');
            //console.log(b64Data);
            //var byteCharacters = atob(b64Data);
            var byteCharacters = b64Data;
            var byteArrays = [];

            for (var offset = 0; offset < byteCharacters.length; offset += sliceSize) {
                var slice = byteCharacters.slice(offset, offset + sliceSize);

                var byteNumbers = new Array(slice.length);
                for (var i = 0; i < slice.length; i++) {
                    byteNumbers[i] = slice.charCodeAt(i);
                }

                var byteArray = new Uint8Array(byteNumbers);

                byteArrays.push(byteArray);
            }

        var blob = new Blob(byteArrays, {type: contentType});
        return blob;
    }

    const blobToFile = (theBlob, fileName) => {
        theBlob.lastModifiedDate = new Date();
        theBlob.name = fileName;
        return theBlob;
      };

    // create a capture function
    const handleTakePhoto = useCallback((dataUri) => {
        // Do stuff with the photo...
        console.log('takePhoto');
        //console.log(dataUri);
        const config = {
            headers: {
              "Content-Type": "application/json"
            }
        };
      
        const configBlop = {
            headers: {
              "Content-Type": "multipart/form-data"
            }
        };
      
        const blob = b64toBlob(dataUri, "image/png");
        const fileName = "beauftragung-unterschrift.png";
        const file = blobToFile(blob, fileName);
        axios.post("https://n8zgm9ipzf.execute-api.ap-southeast-2.amazonaws.com/Prod/upload", 
            {fileName: fileName, fileType: "image/png", data: dataUri }, config)
            .then(res => {
              // axios.put(res.data, file, configBlop).then(res => console.log(res));
              console.log("image uploaded");
        });
    });

    return (
      <div className="container">
        <Camera
            onTakePhoto = { (dataUri) => { handleTakePhoto(dataUri); } }
        />
      </div>
    );
  };
  
  export default FileUpload;