import React, { useContext, useEffect, useState} from 'react'

const Main = () => { 
    const [pdfFile1, setPdfFile1] = useState(null);
    const [pdfFile2, setPdfFile2] = useState(null);
    const [validationError, setValidationError] = useState('');

    const handleFile1Change = (event) => {
        const file = event.target.files[0];
        if (file && file.type === 'application/pdf') {
          setPdfFile1(file);
          setValidationError('');
        } else {
          setPdfFile1(null);
          setValidationError('Please select a PDF file for File 1.');
        }
      };
    
      const handleFile2Change = (event) => {
        const file = event.target.files[0];
        if (file && file.type === 'application/pdf') {
          setPdfFile2(file);
          setValidationError('');
        } else {
          setPdfFile2(null);
          setValidationError('Please select a PDF file for File 2.');
        }
      };
    
      const handleSubmit = (event) => {
        event.preventDefault();
        if (pdfFile1 && pdfFile2) {
          // Perform further processing with the PDF files
          console.log('File 1:', pdfFile1);
          console.log('File 2:', pdfFile2);
          alert("pdf gone")
        } else {
          setValidationError('Please select both PDF files.');
        }
      };


    return (
        <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="file1">File 1:</label>
          <input type="file" id="file1" accept="application/pdf" onChange={handleFile1Change} />
        </div>
        <div>
          <label htmlFor="file2">File 2:</label>
          <input type="file" id="file2" accept="application/pdf" onChange={handleFile2Change} />
        </div>
        <button type="submit">Submit</button>
      </form>
      {validationError && <p>{validationError}</p>}
    </div>
    )
}

export default Main