import { useState, useEffect } from 'react';
import ICategoryData from "../types/category.type";

export const useCategoryState = () => {
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

  useEffect(() => {
    if (!currentCategory && deletedCategoryId) {
      setShowCategory(false);
      setShowCategoriesList(false);
    }
  }, [currentCategory, deletedCategoryId]);

  return {
    currentCategory,
    setCurrentCategory,
    showCategoryForm,
    setShowCategoryForm,
    showCategory,
    setShowCategory,
    showCategoriesList,
    setShowCategoriesList,
    categoriesButtonViewText,
    categoriesButtonAddText,
    deletedCategoryId,
    setDeletedCategoryId,
    handleCategoryClose,
    handleCategoriesListClick,
    handleAddCategoryClick,
    handleEditCategory
  };
};
