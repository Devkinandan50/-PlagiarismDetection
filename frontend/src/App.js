import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import Navbar from './components/Navbar';
import { Home } from './Pages/Home';
import Main from './Pages/Main';


function App() {
  return (
    <>
      
          <Router>
            <Navbar />
            <div className="container">
              <Switch>
                <Route exact path="/">
                  <Home />
                </Route>
                <Route exact path="/main">
                  <Main />
                </Route>
              </Switch>
            </div>
          </Router>
        
    </>
  );
}

export default App;