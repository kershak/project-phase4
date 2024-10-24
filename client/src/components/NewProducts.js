import React, { useState } from "react";
import './NewProducts.css';

function NewProductForm({addProduct}) {
  const [product_name, setProduct] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [stock_qty, setQty] = useState("");
  const [in_stock, setStock] = useState("");
  
  function handleFormSubmit (e) {
    e.preventDefault();
    console.log(product_name, description, price, stock_qty, in_stock);
    addProduct({
      product_name,
      description,
      price,
      stock_qty,
      in_stock,
    })
    setProduct ('');
    setDescription ('');
    setPrice("");
    setQty("");
    setStock('');
  }

  return (
    <div className="new-product-form">
      <h2>New Product</h2>
      <form onSubmit={e=> handleFormSubmit(e)}>
        <input 
        type="text" 
        name="model" 
        placeholder="Camera Model" 
        value={product_name} onChange={e => setProduct(e.target.value)}/>
        <input 
        type="text" 
        name="description" 
        placeholder="Camera description" 
        value={description} onChange={e => setDescription(e.target.value)}/>
        <input 
        type="text" 
        name="price" 
        placeholder="Camera price" 
        value={price} onChange={e => setPrice(e.target.value)}/>
        <input 
        type="text" 
        name="quantity" 
        placeholder="Camera quantity" 
        value={stock_qty} onChange={e => setQty(e.target.value)}/>
        <select  
        name="type" 
        onChange={e => setStock(e.target.value)}
        style={{padding: '8px', marging: '8px 0', width: '100%'}}>
        <option value=""> Select Type</option>
        <option value="in_stock">In stock</option>
        <option value="out_stock">Out of stock</option>
        {/* <option value="interface-board">Interface Board</option>
        <option value="miniature-camera">Miniature Camera</option> */}
        </select>
        <button type="submit">Add Product</button>
      </form>
    </div>
  );
}

export default NewProductForm;