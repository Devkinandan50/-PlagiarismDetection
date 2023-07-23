import Form from 'react-bootstrap/Form';
import React, { useState } from 'react';
import Result from '../components/Result';
const baseUrl = process.env.REACT_APP_BASE_URL;

function FileUpload() {
  const [file1, setFile1] = useState(null);
  const [file2, setFile2] = useState(null);
  const [loader, setloader] = useState(false);
  const [data, setdata] = useState(null);


  const handleFile1Change = (event) => {
    const selectedFile = event.target.files[0];
    setFile1(selectedFile);
  };

  const handleFile2Change = (event) => {
    const selectedFile = event.target.files[0];
    setFile2(selectedFile);
  };


  const handleSubmit = async (event) => {
    setdata(null)
    event.preventDefault();
    
    if (file1 === null || !(file1.type === 'application/pdf')) {
      alert('Please select two PDF files1.');
      return;
    }
    if (file2 === null || !(file2.type === 'application/pdf')) {
      alert('Please select two PDF files2.');
      return;
    }
    
    setloader(true);
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
        setdata(data)
      } else {
        console.log('An error occurred while uploading the files.');
      }
    } catch (error) {
      console.log('An error occurred:', error);
    }
    setloader(false);
  };

  return (
    <>

      <div class="row mt-5">
        <div class="col-lg-5" style={{ height: 600, borderRight: "2px double green" }}>
          <h4 className='text-center'> Upload Your PDF Here</h4>
          <hr class="my-2"></hr>
          <div className='mt-5 p-4'>

            <div class="card">
              <div class="card-body">
                <form onSubmit={handleSubmit}>
                  <Form.Group controlId="formFile" className="mb-3">
                    <Form.Label>file input </Form.Label>
                    <Form.Control type="file" id="file1" accept=".pdf" onChange={handleFile1Change} />
                  </Form.Group>

                  <Form.Group controlId="formFile" className="mb-3">
                    <Form.Label>file input </Form.Label>
                    <Form.Control type="file" id="file2" accept=".pdf" onChange={handleFile2Change} />
                  </Form.Group>


                  <div className="col-auto my-1 text-center">
                    <button type="submit" class="btn btn-primary">Upload Files</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>




        <div class="col-lg-7 mb-lg-0 mb-4">
          <h4 className='text-center'> Result</h4>
          <hr class="my-2"></hr>

          {data ? (
            <div>
              <h2>Plagiarism Result:</h2>
              <p><strong>Cosine Score:</strong> {data['Cosine Score']}</p>
              <p><strong>Jaccard Score:</strong> {data['jaccard Score']}</p>

              {/* <h3>Common Words:</h3>
            <ul>
              {Object.entries(data['common words']).map(([word, weight]) => (
                <li key={word}>{word}: {weight}</li>
              ))}
            </ul> */}

              <h3>Data:</h3>
              <table>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Value1</th>
                    <th>Value2</th>
                    <th>Value3</th>
                  </tr>
                </thead>
                <tbody>
                  {data['data'].map((item, index) => (
                    <tr key={index}>
                      <td>{item.name}</td>
                      <td>{item.val1}</td>
                      <td>{item.val2}</td>
                      <td>{item.val3.toString()}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <>
              {loader ? (
                <div class="d-flex justify-content-center m-5">
                  <div class="spinner-border" role="status">

                  </div>
                </div>
              ) : (
                <p>upload pdf to see result</p>
              )}
            </>
          )}
        </div>

      </div>

    </>
  );
}

export default FileUpload;


