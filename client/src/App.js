import React from "react";
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Route,Switch} from "react-router-dom";
import Home from './components/Home';
import Footer from './components/Footer';
import About from "./components/About";
import Contact from "./components/Contact";
import ProductList from "./components/Products";
import CustomerList from "./components/Customers";

function App() {
//   return <h1>Project Client</h1>;
// }

  return (
    <Router>
      <div className="app">
      <Navbar /> 
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/about" component={About} />
        <Route path="/contact" component={Contact} />
        <Route path="/products" component={ProductList}/>
        <Route path="/customers" component={CustomerList}/>
        <Route path="*" component= {() => <div className= "page-not-found">404 Not Found</div>} />
      </Switch>
      <Footer />
      </div>
    </Router>
  );
}


export default App;
