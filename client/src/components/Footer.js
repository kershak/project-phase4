import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css'; 

const Footer = () => (
  <footer className="footer">
    <div className="footer-content">
      <div className="footer-logo">
        <img src="/ascentlogo.png" alt="Ascent Imaging Logo" />
      </div>
      <div className="footer-links">
        <ul>
          <li><Link to ="/">Home </Link></li>
          <li><Link to ="/products">Products</Link></li>
          <li><Link to="/about">About</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </div>
      <div className="footer-contact">
        <p>Contact Us: <a href="mailto:info@ascent-imaging.com">info@ascent-imaging.com</a></p>
        <p>Phone: (123) 456-7890</p>
      </div>
      <div className="footer-social">
        <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">Facebook</a>
        <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">Twitter</a>
        <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer">LinkedIn</a>
      </div>
    </div>
    <div className="footer-bottom">
      <p>&copy; 2024 Ascent Imaging. All rights reserved.</p>
    </div>
  </footer>
);

export default Footer;