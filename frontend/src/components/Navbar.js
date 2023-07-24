import React, { useContext, useEffect } from 'react'
import { Link, useLocation } from "react-router-dom";
import { useHistory } from 'react-router-dom';


const Navbar = () => {
    let location = useLocation();
    let history = useHistory();
    


    // without reload change data
    // useEffect(() => {
    //     set_checK_loginOr_not();
    // }, [])

    return (
        <>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <Link className="navbar-brand" to="/">FindPlaG</Link>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item">
                                <Link className={`nav-link ${location.pathname === "/" ? "active" : ""}`} aria-current="page" to="/">Home</Link>
                            </li>
                            {/* <li className="nav-item">
                                <Link className={`nav-link ${location.pathname === "/allprojects" ? "active" : ""}`} aria-current="page" to="/allprojects">All Projects</Link>
                            </li>
                            <li className="nav-item">
                                <Link className={`nav-link ${location.pathname === "/howitsworks" ? "active" : ""}`} to="/howitsworks">How its Works</Link>
                            </li> */}
                            <li className="nav-item">
                                <Link className={`nav-link ${location.pathname === "/main" ? "active" : ""}`} to="/main">Main</Link>
                            </li>

                        </ul>
                        <form className="d-flex">
                                    <Link className="btn btn-primary mx-1" to="/main" role="button">Get Started</Link>
                                    {/* <Link className="btn btn-primary mx-1" to="/signup" role="button">Signup</Link> */}
                        </form> 
                    </div>
                </div>
            </nav>
        </>
    )
}

export default Navbar
