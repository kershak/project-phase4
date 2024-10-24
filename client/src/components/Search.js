import React from "react";

function Search({filterProducts, filter}) {

  return (
    <div className="searchbar">
      <label htmlFor="search">Search Products:</label>
      <input
        type="text"
        id="search"
        value = {filter}
        placeholder="Type a model to search..."
        onChange={(e) => filterProducts(e.target.value)}
      />
    </div>
  );
}
 
export default Search;