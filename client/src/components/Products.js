import React, { useState ,useEffect} from "react";
import NewProductForm from './NewProducts';
import './Products.css';
import axios from 'axios';

function ProductList() {
  const [products, setProducts] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5555/products')
    .then(res => res.json())
    .then(data => setProducts(data))
    .catch(err => console.log(err))
  },[])

  function addProduct(product) {
    fetch('http://127.0.0.1:5555/products', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(product)
    })
    .then(res => res.json())
    .then(data => setProducts([...products, data]))
    .catch(err => console.log(err));
  }


  return (
    <div>
      <NewProductForm addProduct={addProduct} />
      <div className="product-list">
        <h2>Product List</h2>
        {products.length === 0 ? (
          <p>No products added yet.</p>
        ) : (
            <table className="product-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Product Name</th>
                        <th>Description</th>
                        <th>Price</th>
                        <th>Stock Quantity</th>
                        <th>In stock</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map((product, index) =>(
                        <tr key={product.id || index}>
                            <td>{product.id}</td>
                            <td>{product.product_name}</td>
                            <td>{product.description}</td>
                            <td>{product.price.toFixed(2)} USD</td>
                            <td>{product.stock_qty}</td>
                            <td>{product.in_stock? 'Yes': 'No'}</td>
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

export default ProductList;