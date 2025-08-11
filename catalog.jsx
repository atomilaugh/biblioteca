import './catalog.css'; 


export default function Catalog(props) {
  return (
    <div className="catalog-card">
      <img src={props.image} alt={props.title} />
      <h3>{props.title}</h3>
      <p>{props.description}</p>
      <p className="price">${props.price}</p>
      <button>Agregar al carrito</button>
    </div>
  );
}

