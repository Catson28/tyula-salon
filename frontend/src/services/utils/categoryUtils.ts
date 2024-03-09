import { useState } from 'react';
import CategoryDataService from "./..//net/category.service";
import ICategoryData from "./../types/category.type";

export const useCategoryState = () => {
  const [currentCategory, setCurrentCategory] = useState<ICategoryData | null>(null);
  const [showCategoryForm, setShowCategoryForm] = useState<boolean>(false);
  const [showCategory, setShowCategory] = useState<boolean>(false);
  const [showCategoriesList, setShowCategoriesList] = useState<boolean>(false);
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

  return {
    currentCategory,
    showCategoryForm,
    showCategory,
    showCategoriesList,
    deletedCategoryId,
    setShowCategoryForm,
    setShowCategory,
    setShowCategoriesList,
    handleCategoriesListClick,
    handleAddCategoryClick,
    handleEditCategory,
    handleDeleteCategory,
    handleUpdateCategory
  };
};
