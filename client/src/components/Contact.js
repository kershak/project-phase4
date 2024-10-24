import React, { useState } from 'react';
import './Contact.css'; // Import the CSS file for styling

function Contact() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  });

  function handleChange  (e)  {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  function handleSubmit  (e) {
    e.preventDefault();
    //console.log('Form submitted:', formData);
    fetch('http://localhost:6001/contacts', {
      method: 'POST',
      headers: {
        'Content-Type' : 'Application/json',
      },
      body: JSON.stringify(formData),
    })
    .then(res => res.json())
    .then(data =>{
      //console.log(data);
      setFormData({
        name:"",
        email:"",
        message:""
      });
    })
    .catch((error)=>{console.error(error);

    })
  };

  return (
    <div className="contact-page">
      <h1>Contact Us</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name</label>
        <input
          type="text"
          id="name"
          name="name"
          placeholder="Your Name"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <label htmlFor="email">Email</label>
        <input
          type="email"
          id="email"
          name="email"
          placeholder="Your Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <label htmlFor="message">Message</label>
        <textarea
          id="message"
          name="message"
          placeholder="Your Message"
          value={formData.message}
          onChange={handleChange}
          required
        ></textarea>
        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default Contact;