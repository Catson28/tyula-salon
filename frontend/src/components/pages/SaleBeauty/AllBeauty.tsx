import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import AddTutorial from './../../partials/tutorial/add-tutorial.component';
import TutorialsList from './../../partials/tutorial/tutorials-list.component';

import AddCategory from './../../partials/category/add-category.component';
import CategoriesList from './../../partials/category/categories-list.component';

const AllBeauty: React.FC = () => {
  const [showTutorialForm, setShowTutorialForm] = useState<boolean>(false);
  const [showTutorialsList, setShowTutorialsList] = useState<boolean>(false);


  const [showCategoryForm, setShowCategoryForm] = useState<boolean>(false);
  const [showCategoriesList, setShowCategoriesList] = useState<boolean>(false);


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

  const handleFormTutorialSubmit = () => {
    setShowTutorialForm(false);
  };


  const handleCategoryClose = () => {
    setShowCategoryForm(false);
    setShowCategoriesList(false);
  };

  const handleCategoriesListClick = () => {
    handleCategoryClose();
    setShowCategoriesList(true);
  };
  
  const handleAddCategoryClick = () => {
    handleCategoryClose();
    setShowCategoryForm(true);
  };

  const handleFormCategorySubmit = () => {
    setShowCategoryForm(false);
  };

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
          <button type="button" className="btn btn-primary" onClick={handleCategoriesListClick}>Abrir</button>
          <button type="button" className="btn btn-primary" onClick={handleAddCategoryClick}>Adicionar</button>
        </div>
        {showCategoryForm && (
          <AddCategory onClose={handleCategoryClose} />
        )}
        {showCategoriesList && (
          <CategoriesList onClose={handleCategoryClose} />
        )}
      </div>
    </div>
  );
};

export default AllBeauty;
