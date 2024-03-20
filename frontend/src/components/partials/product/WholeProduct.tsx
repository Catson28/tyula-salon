import React, { useEffect } from 'react';

import AddProduct from './add-product.component';
import ProductsList from './products-list.component'; // Importando o componente de listagem de produtos
import Product from './product.component'; // Importando o componente de exibição de produto
import { useProductState } from '../../../services/utils/productUtils'; // Importando o hook de estado para produtos

const WholeProduct: React.FC = () => {
  const {
    currentProduct,
    showProductForm,
    showProduct,
    showProductsList,
    deletedProductId,

    setShowProductForm, // Adicionando as funções de configuração ao objeto de retorno
    setShowProduct,
    setShowProductsList,
    handleProductsListClick,
    handleAddProductClick,
    handleEditProduct,
    handleDeleteProduct,
    handleUpdateProduct
  } = useProductState();

  useEffect(() => {
    if (!currentProduct && deletedProductId) {
      setShowProduct(false);
      setShowProductsList(false);
    }
  }, [currentProduct, deletedProductId]);

  const productsButtonViewText = showProduct || showProductsList ? "Fechar" : "Abrir";
  const productsButtonAddText = showProductForm ? "Fechar" : "Adicionar";

  return (
      <>
        <div className="btn-toolbar justify-content-between p-2" role="toolbar" aria-label="Toolbar with button groups">
          <h2 id="vertical-variation">Lista de Productos<a className="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="#" href="#vertical-variation"></a></h2>
          <button type="button" className="btn btn-primary" onClick={handleProductsListClick}>{productsButtonViewText}</button>
          <button type="button" className="btn btn-primary" onClick={handleAddProductClick}>{productsButtonAddText}</button>
        </div>
        {showProductForm && (
          <AddProduct onClose={() => setShowProductForm(false)} />
        )}
        {showProductsList && (
          <ProductsList onClose={() => setShowProductsList(false)} onEditProduct={handleEditProduct} />
        )}
        {showProduct && currentProduct && (
          <Product id={currentProduct.id} onEdit={handleUpdateProduct} onDelete={handleDeleteProduct} />
        )}
      </>
  );
};

export default WholeProduct;
