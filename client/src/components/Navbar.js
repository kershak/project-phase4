import React, { useState } from 'react';
import './Navbar.css';
import {Link} from 'react-router-dom';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(prevState => !prevState);
  };

  return (
    
    <nav className="navbar">
      <div className="logo">
        <img src="/ascentlogo.png" alt="Ascent Imaging Logo" />
      </div>
      <button className="menu-toggle" onClick={toggleMenu} aria-label="Toggle navigation">
        ☰
      </button>
      <ul className={`nav-links ${isOpen ? 'open' : ''}`}>
        <li><Link to ="/">Home </Link></li>
        <li><Link to = "/customers">Customers</Link></li>
        <li><Link to = "/orders">Orders</Link></li>
        <li><Link to = "/returns">Returns</Link></li>
        <li><Link to ="/products">Products</Link></li>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/contact">Contact</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;