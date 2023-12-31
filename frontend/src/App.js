import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import Navbar from './components/Navbar';
import { Home } from './Pages/Home';
import Main from './Pages/Main';

// import dotenv from 'dotenv';
// dotenv.config();

function App() {
  return (
    <>
      
          <Router>
            <Navbar />
            <div className="container">
              <Switch>
                <Route exact path="/">
                   <Main />
                </Route>
                <Route exact path="/main">
                   <Home />
                </Route>
              </Switch>
            </div>
          </Router>
        
    </>
  );
}

export default App;
