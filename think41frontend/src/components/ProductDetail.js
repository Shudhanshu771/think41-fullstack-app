import { useParams, Link } from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';

function ProductDetail() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`http://localhost:5000/api/products/${id}`)
      .then(res => {
        setProduct(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <p>Loading...</p>;
  if (!product) return <p>Product not found.</p>;

  return (
    <div style={{ padding: '20px' }}>
      <Link to="/" style={{ marginBottom: '20px', display: 'inline-block' }}>← Back to Products</Link>

      <h2>{product.name}</h2>

      {/* Image using a placeholder */}
      <img
        src={`https://via.placeholder.com/300x300?text=${encodeURIComponent(product.brand || 'Product')}`}
        alt={product.sku}
        style={{ marginBottom: '20px', borderRadius: '8px' }}
      />

      <p><strong>Brand:</strong> {product.brand || 'N/A'}</p>
      <p><strong>Price (Cost):</strong> ₹{product.cost?.toFixed(2) || 'N/A'}</p>
      <p><strong>Retail Price:</strong> ₹{product.retail_price?.toFixed(2) || 'N/A'}</p>
      <p><strong>Category:</strong> {product.category || 'N/A'}</p>
      <p><strong>Department:</strong> {product.department || 'N/A'}</p>
    </div>
  );
}

export default ProductDetail;
