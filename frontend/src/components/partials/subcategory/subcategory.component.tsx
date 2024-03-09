import React, { useState, useEffect, ChangeEvent } from "react";
import { useNavigate } from 'react-router-dom';

import SubcategoryDataService from "../../../services/net/subcategory.service";
import ISubcategoryData from "../../../services/types/subcategory.type";

interface Props {
  id: string;
  onEdit: (updatedSubcategory: ISubcategoryData) => void;
  onDelete: (subcategoryId: string) => void;
};

const Subcategory: React.FC<Props> = ({ id, onEdit, onDelete }) => {
  const navigate = useNavigate();
  const [currentSubcategory, setCurrentSubcategory] = useState<ISubcategoryData>({
    id: "",
    name: "",
    description: "",
    category: "",
  });
  const [message, setMessage] = useState<string>("");

  useEffect(() => {
    if (id) {
      getSubcategory(id);
    }
  }, [id]);

  const onChangeName = (e: ChangeEvent<HTMLInputElement>) => {
    const name = e.target.value;
    setCurrentSubcategory(prevState => ({
      ...prevState,
      name: name,
    }));
  };

  const onChangeDescription = (e: ChangeEvent<HTMLInputElement>) => {
    const description = e.target.value;
    setCurrentSubcategory(prevState => ({
      ...prevState,
      description: description,
    }));
  };

  const getSubcategory = (id: string) => {
    SubcategoryDataService.get(id)
      .then((response: any) => {
        setCurrentSubcategory(response.data);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };
  
  const updateSubcategory = () => {
    SubcategoryDataService.update(
      currentSubcategory,
      currentSubcategory.id
    )
      .then((response: any) => {
        setMessage("The subcategory was updated successfully!");
        onEdit(currentSubcategory);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };

  const deleteSubcategory = () => {
    SubcategoryDataService.delete(currentSubcategory.id)
      .then((response: any) => {
        setMessage("The subcategory was deleted successfully!");
        onDelete(currentSubcategory.id);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };
  
  return (
    <div>
      {id && currentSubcategory ? (
        <div className="edit-form">
          <h4>Subcategory</h4>
          <form>
            <div className="form-group">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                className="form-control"
                id="name"
                value={currentSubcategory.name}
                onChange={onChangeName}
              />
            </div>
            <div className="form-group">
              <label htmlFor="description">Description</label>
              <input
                type="text"
                className="form-control"
                id="description"
                value={currentSubcategory.description}
                onChange={onChangeDescription}
              />
            </div>
          </form>
          <button
            className="badge badge-danger mr-2"
            onClick={deleteSubcategory}
          >
            Delete
          </button>
          <button
            type="button"
            className="badge badge-success"
            onClick={updateSubcategory}
          >
            Update
          </button>
          <p>{message}</p>
        </div>
      ) : (
        <div>
          <br />
          <p>({JSON.stringify(currentSubcategory)}) --- Please click on a Subcategory...</p>
        </div>
      )}
    </div>
  );
};

export default Subcategory;
