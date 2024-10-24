import React, { useState } from "react";
import './NewCustomers.css';

function NewCustomerForm({addProduct}) {
  const [customer, setCustomer] = useState("");
  const [contact, setContact] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  //const [image, setImage ] = useState("");
  

  function handleFormSubmit (e) {
    e.preventDefault();
    console.log(customer, contact,email,phone);
    addProduct({
      customer,
      contact,
      email,
      phone,
    })
    setCustomer("");
    setContact("");
    setEmail("");
    setPhone("");

  }

  return (
    <div className="new-customer-form">
      <h2>New Customer</h2>
      <form onSubmit={e=> handleFormSubmit(e)}>
        <input 
        type="text" 
        name="model" 
        placeholder="Customer Name" 
        value={customer} onChange={e => setCustomer(e.target.value)}/>
        <input 
        type="text" 
        name="image" 
        placeholder="Contact person" 
        value={contact} onChange={e => setContact(e.target.value)}/>
        <input 
        type="text" 
        name="description" 
        placeholder="Customer email" 
        value={email} onChange={e => setEmail(e.target.value)}/>
        {/* <select  
        name="type" 
        value={type} 
        onChange={e => setType(e.target.value)}
        style={{padding: '8px', marging: '8px 0', width: '100%'}}>
        <option value=""> Select Type</option>
        <option value="zoom-module">Zoom Module</option>
        <option value="board-camera">Board Camera</option>
        <option value="interface-board">Interface Board</option>
        <option value="miniature-camera">Miniature Camera</option> */}
        {/* </select> */}
        <button type="submit">Add Product</button>
      </form>
    </div>
  );
}

export default NewCustomerForm;