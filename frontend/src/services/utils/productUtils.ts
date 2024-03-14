import { useState } from 'react';
import ProductDataService from "./../net/product.service";
import IProductData from "./../types/product.type";

export const useProductState = () => {
  const [currentProduct, setCurrentProduct] = useState<IProductData | null>(null);
  const [showProductForm, setShowProductForm] = useState<boolean>(false);
  const [showProduct, setShowProduct] = useState<boolean>(false);
  const [showProductsList, setShowProductsList] = useState<boolean>(false);
  const [deletedProductId, setDeletedProductId] = useState<string | null>(null);

  const handleProductClose = () => {
    setShowProductForm(false);
    setShowProductsList(false);
    setShowProduct(false);
  };

  const handleProductsListClick = () => {
    if (showProductsList) {
      handleProductClose();
    } else {
      handleProductClose();
      setShowProductsList(true);
    }
  };

  const handleAddProductClick = () => {
    if (showProductForm) {
      handleProductClose();
    } else {
      handleProductClose();
      setShowProductForm(true);
    }
  };

  const handleEditProduct = (product: IProductData) => {
    if (product) {
      setCurrentProduct(product);
      handleProductClose();
      setShowProduct(true);
    }
  };

  const handleDeleteProduct = (productId: string) => {
    ProductDataService.delete(productId)
      .then((response: any) => {
        handleProductClose();
        setDeletedProductId(productId);
        setCurrentProduct(null);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };

  const handleUpdateProduct = (updatedProduct: IProductData) => {
    ProductDataService.update(updatedProduct, updatedProduct.id)
      .then((response: any) => {
        // setCurrentProduct(currentProduct);
        handleProductClose();
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };

  return {
    currentProduct,
    showProductForm,
    showProduct,
    showProductsList,
    deletedProductId,
    setShowProductForm,
    setShowProduct,
    setShowProductsList,
    handleProductsListClick,
    handleAddProductClick,
    handleEditProduct,
    handleDeleteProduct,
    handleUpdateProduct
  };
};
