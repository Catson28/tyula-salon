import React, { useEffect } from 'react';

import AddCategory from './add-category.component';
import CategoriesList from './categories-list.component';
import Category from './category.component';
import { useCategoryState } from '../../../services/utils/categoryUtils';

const AboutCategory: React.FC = () => {
  const {
    currentCategory,
    showCategoryForm,
    showCategory,
    showCategoriesList,
    deletedCategoryId,

    setShowCategoryForm, // Adicione as funções de configuração ao objeto de retorno
    setShowCategory,
    setShowCategoriesList,
    handleCategoriesListClick,
    handleAddCategoryClick,
    handleEditCategory,
    handleDeleteCategory,
    handleUpdateCategory
  } = useCategoryState();

  useEffect(() => {
    if (!currentCategory && deletedCategoryId) {
      setShowCategory(false);
      setShowCategoriesList(false);
    }
  }, [currentCategory, deletedCategoryId]);

  const categoriesButtonViewText = showCategory || showCategoriesList ? "Fechar" : "Abrir";
  const categoriesButtonAddText = showCategoryForm ? "Fechar" : "Adicionar";

  return (
      <>
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
      </>
  );
};

export default AboutCategory;
