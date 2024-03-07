import React, { useState } from 'react';
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

  const handleEditCategory = (category: ICategoryData) => {
    if (category) {
      setCurrentCategory(category);
      // alert(JSON.stringify(currentCategory));
      // alert(JSON.stringify(setCurrentCategory(category)));
    }
    // setCurrentCategory(category);
    // alert(JSON.stringify(category));
  };

  const handleUpdateCategory = (updatedCategory: ICategoryData) => {
    // alert(JSON.stringify(currentCategory));
    CategoryDataService.update(updatedCategory, updatedCategory.id)
      .then((response: any) => {
        // Atualize a lista de categorias ou faça qualquer outra ação necessária
        // Aqui você pode definir o estado do currentCategory de volta para null
        setCurrentCategory(null);
      })
      .catch((e: Error) => {
        console.log(e);
      });
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
        </div>{/*
        {showCategoryForm && (
          <AddCategory onClose={handleCategoryClose} />
        )}
        {showCategoriesList && (
          <CategoriesList onClose={handleCategoryClose} />
        )}
         */}
        {showCategoryForm && (
          <AddCategory onClose={() => setShowCategoryForm(false)} />
        )}
        {showCategoriesList && (
          <CategoriesList onClose={() => setShowCategoriesList(false)} onEditCategory={handleEditCategory} />
        )}

        {currentCategory && (
          /*<Category id={currentCategory.id} onEdit={handleUpdateCategory} />*/
          <Category id={currentCategory.id} onEdit={handleUpdateCategory} />
        )}
      </div>
    </div>
  );
};

export default AllBeauty;
