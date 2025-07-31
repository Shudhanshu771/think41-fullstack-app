// src/components/ProductList.js
import { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/products')
      .then(res => setProducts(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Products</h2>
      <div style={{ display: 'flex', flexWrap: 'wrap' }}>
        {products.map(product => (
          <div
            key={product.id}
            style={{
              width: '180px',
              margin: '10px',
              border: '1px solid #ccc',
              padding: '10px',
              textAlign: 'center',
              borderRadius: '8px',
              boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
            }}
          >
            <h4 style={{ fontSize: '16px' }}>{product.title}</h4>
            <p style={{ margin: '5px 0' }}>₹ {product.price}</p>
            <p style={{ fontSize: '12px', color: '#888' }}>{product.brand}</p>
            <Link to={`/product/${product.id}`}>View Details</Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProductList;
