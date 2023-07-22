// import React, { useContext, useEffect, useState} from 'react'

// const Main = () => { 
//     const [pdfFile1, setPdfFile1] = useState(null);
//     const [pdfFile2, setPdfFile2] = useState(null);
//     const [validationError, setValidationError] = useState('');




//     const handleFile1Change = (event) => {
//         const file = event.target.files[0];
//         const fileReader = new FileReader();

//         fileReader.onload = (event) => {
//           const pdfData = event.target.result;
//           // const textContent = this.extractTextFromPDF(pdfData);
//           console.log(pdfData);
//         };

//         fileReader.readAsArrayBuffer(file);


//         if (file && file.type === 'application/pdf') {
//           setPdfFile1(file);
//           setValidationError('');
//         } else {
//           setPdfFile1(null);
//           setValidationError('Please select a PDF file for File 1.');
//         }
//       };

//       const handleFile2Change = (event) => {
//         const file = event.target.files[0];
//         if (file && file.type === 'application/pdf') {
//           setPdfFile2(file);
//           setValidationError('');
//         } else {
//           setPdfFile2(null);
//           setValidationError('Please select a PDF file for File 2.');
//         }
//       };

//       const handleSubmit = (event) => {
//         event.preventDefault();
//         if (pdfFile1 && pdfFile2) {
//           // Perform further processing with the PDF files
//           console.log('File 1:', pdfFile1);
//           console.log('File 2:', pdfFile2);
//           alert("pdf gone")
//         } else {
//           setValidationError('Please select both PDF files.');
//         }
//       };


//     return (
//         <div>
//       <form onSubmit={handleSubmit}>
//         <div>
//           <label htmlFor="file1">File 1:</label>
//           <input type="file" id="file1" accept="application/pdf" onChange={handleFile1Change} />
//         </div>
//         <div>
//           <label htmlFor="file2">File 2:</label>
//           <input type="file" id="file2" accept="application/pdf" onChange={handleFile2Change} />
//         </div>
//         <button type="submit">Submit</button>
//       </form>
//       {validationError && <p>{validationError}</p>}
//     </div>
//     )
// }

// export default Main



import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import React, { useState } from 'react';
const baseUrl = process.env.REACT_APP_BASE_URL;

function FileUpload() {
  const [file1, setFile1] = useState(null);
  const [file2, setFile2] = useState(null);

  const handleFile1Change = (event) => {
    const selectedFile = event.target.files[0];
    setFile1(selectedFile);
  };

  const handleFile2Change = (event) => {
    const selectedFile = event.target.files[0];
    setFile2(selectedFile);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (file1 === null || !(file1.type === 'application/pdf')) {
      alert('Please select two PDF files1.');
      return;
    }
    if (file2 === null || !(file2.type === 'application/pdf')) {
      alert('Please select two PDF files2.');
      return;
    }

    const formData = new FormData();
    formData.append('file1', file1);
    formData.append('file2', file2);

    try {
      const response = await fetch(baseUrl + "/upload", {
        method: 'POST',
        body: formData,
      });

      if (response) {
        const data = await response.json();
        console.log('Files uploaded successfully.');
        alert('Files uploaded successfully.');
        alert(data)
        console.log(data)
        // Handle the response as needed
      } else {
        console.log('An error occurred while uploading the files.');
      }
    } catch (error) {
      console.log('An error occurred:', error);
    }
  };

  return (
    <Container>
      <Row>
        <Col>
          <div>
            <form onSubmit={handleSubmit}>
              
              <Form.Group controlId="formFile" className="mb-3">
                <Form.Label>Default file input example</Form.Label>
                <Form.Control type="file" id="file1" accept=".pdf" onChange={handleFile1Change} />
              </Form.Group>

              <Form.Group controlId="formFile" className="mb-3">
                <Form.Label>Default file input example</Form.Label>
                <Form.Control type="file" id="file2" accept=".pdf" onChange={handleFile2Change} />
              </Form.Group>

              <button type="submit">Upload Files</button>
            </form>
          </div>
        </Col>
        <Col>2 of 2</Col>
      </Row>
    </Container>


  );
}

export default FileUpload;


