import React, { useState, useEffect, ChangeEvent } from "react";
import { useNavigate } from 'react-router-dom';

import CategoryDataService from "../../../services/net/category.service";
import ICategoryData from "../../../services/types/category.type";

interface Props {
  id: string; // Adicione a propriedade id ao tipo Props
  onEdit: (updatedCategory: ICategoryData) => void;
  onDelete: (categoryId: string) => void; // Adicione a propriedade onDelete ao tipo Props
};

const Category: React.FC<Props> = ({ id, onEdit, onDelete }) => {
  const navigate = useNavigate();
  const [currentCategory, setCurrentCategory] = useState<ICategoryData>({
    id: "",
    name: "",
    description: "",
  });
  const [message, setMessage] = useState<string>("");

  useEffect(() => {
    if (id) {
      getCategory(id);
    }
  }, [id]);

  const onChangeName = (e: ChangeEvent<HTMLInputElement>) => {
    const name = e.target.value;
    setCurrentCategory(prevState => ({
      ...prevState,
      name: name,
    }));
  };

  const onChangeDescription = (e: ChangeEvent<HTMLInputElement>) => {
    const description = e.target.value;
    setCurrentCategory(prevState => ({
      ...prevState,
      description: description,
    }));
  };

  const getCategory = (id: string) => {
    CategoryDataService.get(id)
      .then((response: any) => {
        setCurrentCategory(response.data);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };
  
  const updateCategory = () => {
    CategoryDataService.update(
      currentCategory,
      currentCategory.id
    )
      .then((response: any) => {
        setMessage("The category was updated successfully!");
        onEdit(currentCategory);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };

  const deleteCategory = () => {
    CategoryDataService.delete(currentCategory.id)
      .then((response: any) => {
        setMessage("The category was deleted successfully!");
        onDelete(currentCategory.id); // Chama a função onDelete com o ID da categoria
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };
  
  return (
    <div>
      {id && currentCategory ? (
        <div className="edit-form">
          <h4>Category</h4>
          <form>
            <div className="form-group">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                className="form-control"
                id="name"
                value={currentCategory.name}
                onChange={onChangeName}
              />
            </div>
            <div className="form-group">
              <label htmlFor="description">Description</label>
              <input
                type="text"
                className="form-control"
                id="description"
                value={currentCategory.description}
                onChange={onChangeDescription}
              />
            </div>
          </form>
          <button
            className="badge badge-danger mr-2"
            onClick={deleteCategory}
          >
            Delete
          </button>
          <button
            type="button"
            className="badge badge-success"
            onClick={updateCategory}
          >
            Update
          </button>
          <p>{message}</p>
        </div>
      ) : (
        <div>
          <br />
          <p>({JSON.stringify(currentCategory)}) --- Please click on a Category...</p>
        </div>
      )}
    </div>
  );
};

export default Category;
