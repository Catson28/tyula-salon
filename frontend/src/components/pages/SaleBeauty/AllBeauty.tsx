import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

import AddCategory from './../../partials/category/add-category.component';
import CategoriesList from './../../partials/category/categories-list.component';
import Category from './../../partials/category/category.component';
import CategoryDataService from "../../../services/net/category.service";
import ICategoryData from "../../../services/types/category.type";

const AllBeauty: React.FC = () => {
  const [currentCategory, setCurrentCategory] = useState<ICategoryData | null>(null);
  const [showCategoryForm, setShowCategoryForm] = useState<boolean>(false);
  const [showCategory, setShowCategory] = useState<boolean>(false);
  const [showCategoriesList, setShowCategoriesList] = useState<boolean>(false);
  const categoriesButtonViewText = showCategory || showCategoriesList ? "Fechar" : "Abrir";
  const categoriesButtonAddText = showCategoryForm ? "Fechar" : "Adicionar";
  const [deletedCategoryId, setDeletedCategoryId] = useState<string | null>(null);


  const handleCategoryClose = () => {
    setShowCategoryForm(false);
    setShowCategoriesList(false);
    setShowCategory(false);
  };

  const handleCategoriesListClick = () => {
    if (showCategoriesList) {
      handleCategoryClose();
    } else {
      handleCategoryClose();
      setShowCategoriesList(true);
    }
  };
  
  const handleAddCategoryClick = () => {
      if (showCategoryForm) {
        handleCategoryClose();
      } else {
        handleCategoryClose();
        setShowCategoryForm(true);
      }
  };

  const handleEditCategory = (category: ICategoryData) => {
    if (category) {
      setCurrentCategory(category);
      handleCategoryClose();
      setShowCategory(true);
    }
  };
  


  const handleDeleteCategory = (categoryId: string) => {
    CategoryDataService.delete(categoryId)
      .then((response: any) => {
        handleCategoryClose();
        setDeletedCategoryId(categoryId);
        setCurrentCategory(null);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };

  const handleUpdateCategory = (updatedCategory: ICategoryData) => {
    CategoryDataService.update(updatedCategory, updatedCategory.id)
      .then((response: any) => {
        // setCurrentCategory(currentCategory);
        handleCategoryClose();
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };

 
  useEffect(() => {
    if (!currentCategory && deletedCategoryId) {
      setShowCategory(false);
      setShowCategoriesList(false);
    }
  }, [currentCategory, deletedCategoryId]);

  return (
    <div className="container-fluid">
      <div className="container">

        <div className="btn-toolbar justify-content-between p-2" role="toolbar" aria-label="Toolbar with button groups">
          <h2 id="vertical-variation">Lista de Categorias<a className="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="#" href="#vertical-variation"></a></h2>
          <button type="button" className="btn btn-primary" onClick={handleCategoriesListClick}>{categoriesButtonViewText}</button>

          <button type="button" className="btn btn-primary" onClick={handleAddCategoryClick}>{categoriesButtonAddText}</button>
        </div>
        {showCategoryForm && (
          <AddCategory onClose={() => setShowCategoryForm(false)} />
        )}
        {showCategoriesList && (
          <CategoriesList onClose={() => setShowCategoriesList(false)} onEditCategory={handleEditCategory} />
        )}

        {showCategory && currentCategory && (
          <Category id={currentCategory.id} onEdit={handleUpdateCategory}  onDelete={handleDeleteCategory} />
        )}
      </div>
    </div>
  );
};

export default AllBeauty;
