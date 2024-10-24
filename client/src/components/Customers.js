import React, { useState ,useEffect} from "react";
import NewCustomerForm from './NewCustomers';
import './Customers.css';
import axios from 'axios';

function CustomerList() {
  const [customers, setCustomer] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5555/customers')
    .then(res => res.json())
    .then(data => setCustomer(data))
    .catch(err => console.log(err))
  },[])

  function addCustomer(customer) {
    fetch('http://127.0.0.1:5555/customers', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(customer)
    })
    .then(res => res.json())
    .then(data => setCustomer([...customers, data]))
    .catch(err => console.log(err));
  }


  return (
    <div>
      <NewCustomerForm addCustomer={addCustomer} />
      <div className="customer-list">
        <h2>Customer List</h2>
        {customers.length === 0 ? (
          <p>No products added yet.</p>
        ) : (
            <table className="customer-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Customer Name</th>
                        <th>Contact</th>
                        <th>Email</th>
                        <th>Phone</th>
                        
                    </tr>
                </thead>
                <tbody>
                    {customers.map((customer, index) =>(
                        <tr key={customer.id || index}>
                            <td>{customer.id}</td>
                            <td>{customer.cust_name}</td>
                            <td>{customer.contact}</td>
                            
                            <td>{customer.email}</td>
                            <td>{customer.phone}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        //   
        )}
      </div>
    </div>
  );
}

export default CustomerList;