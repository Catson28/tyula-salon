import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import AddTutorial from './../../partials/tutorial/add-tutorial.component';
import TutorialsList from './../../partials/tutorial/tutorials-list.component';

import AddCategory from './../../partials/category/add-category.component';
import CategoriesList from './../../partials/category/categories-list.component';
import Category from './../../partials/category/category.component';
import CategoryDataService from "../../../services/net/category.service";
import ICategoryData from "../../../services/types/category.type";

const AllBeauty: React.FC = () => {
  const [showTutorialForm, setShowTutorialForm] = useState<boolean>(false);
  const [showTutorialsList, setShowTutorialsList] = useState<boolean>(false);
  const [currentCategory, setCurrentCategory] = useState<ICategoryData | null>(null);


  const [showCategoryForm, setShowCategoryForm] = useState<boolean>(false);
  const [showCategoriesList, setShowCategoriesList] = useState<boolean>(false);
  const categoriesButtonViewText = showCategoriesList ? "Fechar" : "Abrir";
  const categoriesButtonAddText = showCategoryForm ? "Fechar" : "Adicionar";


  const handleTutorialClose = () => {
    setShowTutorialForm(false);
    setShowTutorialsList(false);
  };

  const handleTutorialsListClick = () => {
    handleTutorialClose();
    setShowTutorialsList(true);
  };
  
  const handleAddTutorialClick = () => {
    handleTutorialClose();
    setShowTutorialForm(true);
  };

  const handleCategoryClose = () => {
    setShowCategoryForm(false);
    setShowCategoriesList(false);
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
    }
  };

  const handleUpdateCategory = (updatedCategory: ICategoryData) => {
    CategoryDataService.update(updatedCategory, updatedCategory.id)
      .then((response: any) => {
        // setCurrentCategory(currentCategory);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };

  useEffect(() => {
    if (!currentCategory) {
      // Aqui você pode realizar ações com base na categoria atual, como fazer uma solicitação de API
      console.log("Categoria atualizada:", currentCategory);
      JSON.stringify(currentCategory)
      setCurrentCategory(currentCategory);
    }
  }, [currentCategory]);
  

  return (
    <div className="container-fluid">
      <div className="container">
        <div className="btn-toolbar justify-content-between p-2" role="toolbar" aria-label="Toolbar with button groups">
          <h2 id="vertical-variation">Lista de tutoriais<a className="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="#" href="#vertical-variation"></a></h2>
          <button type="button" className="btn btn-primary" onClick={handleTutorialsListClick}>Abrir</button>
          <button type="button" className="btn btn-primary" onClick={handleAddTutorialClick}>Adicionar</button>
        </div>
        {showTutorialForm && (
          <AddTutorial onClose={handleTutorialClose} />
        )}
        {showTutorialsList && (
          <TutorialsList onClose={handleTutorialClose} />
        )}
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

        {currentCategory && (
          <Category id={currentCategory.id} onEdit={handleUpdateCategory} />
        )}
      </div>
    </div>
  );
};

export default AllBeauty;
