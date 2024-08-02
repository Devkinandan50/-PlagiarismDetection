import Form from 'react-bootstrap/Form';
import React, { useState } from 'react';
import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
const baseUrl = process.env.REACT_APP_BASE_URL;

function FileUpload() {
  const [file1, setFile1] = useState(null);
  const [file2, setFile2] = useState(null);
  const [loader, setloader] = useState(false);
  const [data, setdata] = useState(null);
  const [color, setcolor] = useState("Black");


  const handleFile1Change = (event) => {
    const selectedFile = event.target.files[0];
    setFile1(selectedFile);
  };

  const handleFile2Change = (event) => {
    const selectedFile = event.target.files[0];
    setFile2(selectedFile);
  };

  const runOnRender = async() => {
    const formData = new FormData();
    const response = await fetch(baseUrl + "/upload", {
      method: 'POST',
      body: formData,
    });
    const data = await response.json();
  };

  useEffect(() => {
    runOnRender();
  }, []); 



  const handleSubmit = async (event) => {
    setdata(null)
    event.preventDefault();

    if (file1 === null || !(file1.type === 'application/pdf')) {
      // toast.success("Password are not same", {
      //   position: "top-center"
      // });
      toast.error(`Please select Proper file as PDF.`, {
        position: "top-center"
      });
      return;
    }
    if (file2 === null || !(file2.type === 'application/pdf')) {
      toast.error(`Please select Proper file as PDF.`, {
        position: "top-center"
      });
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
        if ((data['jaccard Score'] * 100) > 70) {
          setcolor("red")
        }
        else {
          setcolor("green")
        }
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
      <ToastContainer />
      <div class="row mt-5">
        <div className="box1 col-lg-5" style={{
          height: 640, borderRight: `4px double ${color}`, ...(window.innerWidth >= 576 && window.innerWidth <= 950
            ? {
                height: 440,
                borderRight: '4px double white'
              }
            : {})
        }}>
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




        <div class="col-lg-7 mb-lg-0 mb-4" >
          <h4 className='text-center'>Plagiarism Result</h4>
          <hr class="my-2"></hr>

          {data ? (
            <div>
              {/* <p><strong>Cosine Score:</strong> {data['Cosine Score']}</p> */}
              {/* <p><strong>Jaccard Score:</strong> {data['jaccard Score']}</p> */}
              <div class="row m-3">
                <div class="col-sm-4">
                  <div style={{ width: 100 }}>
                    <CircularProgressbar value={(data['jaccard Score'] * 100).toFixed(1)} text={`${(data['jaccard Score'] * 100).toFixed(1)}%`} />
                  </div>
                </div>
                <div class="col-sm-8">
                  {(data['jaccard Score'] * 100) > 70 ? (
                    <>
                      <div class="alert alert-danger" role="alert">
                        <p><strong>Plagiarism Detected!!!</strong></p>
                        The text in both files exhibits a striking similarity, with a match percentage of {(data['jaccard Score'] * 100).toFixed(1)} %.
                      </div>
                    </>
                  ) : (
                    <>
                      <div class="alert alert-success" role="alert">
                        <p><strong>Originality Confirmed!!! </strong> </p>
                        The textual content in both files is dissimilar.
                      </div>
                    </>
                  )}

                </div>
              </div>



              {/* <h3>Common Words:</h3>
            <ul>
              {Object.entries(data['common words']).map(([word, weight]) => (
                <li key={word}>{word}: {weight}</li>
              ))}
            </ul> */}

              <table class="table table-bordered table-hover table-dark m-3 text-center">
                <thead class="thead-dark">
                  <tr>
                    <th scope="col">Parameter</th>
                    <th scope="col">{file1.name}</th>
                    <th scope="col">{file2.name}</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="table-light">
                    <td>File Size</td>
                    <td>{(file1.size / 1024).toFixed(1)} KB</td>
                    <td>{(file2.size / 1024).toFixed(1)} KB</td>
                  </tr>
                  {data['data'].map((item, index) => (
                    // <tr class={item.val3 ? ("table-danger"): ("table-success")} key={index}>
                    <tr class="table-light" key={index}>
                      <td>{item.name}</td>
                      <td>{item.val1 ? (item.val1) : ("-")}</td>
                      <td>{item.val2 ? (item.val2) : ("-")}</td>
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
                <div class="d-flex justify-content-center m-5">

                  <p>upload pdf to see result</p>
                </div>
              )}
            </>
          )}
        </div>
      </div>


    </>
  );
}

export default FileUpload;


