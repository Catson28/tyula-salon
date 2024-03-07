import { useState, useEffect, ChangeEvent } from "react";
import { useParams, useNavigate } from 'react-router-dom';

import CategoryDataService from "../../../services/net/category.service";
import ICategoryData from "../../../services/types/category.type";

interface RouterProps {
  id?: string;
}

type Props = {
  id: string; // Adicione a propriedade id ao tipo Props
  onEdit: (updatedCategory: ICategoryData) => void;
};


const Category: React.FC<Props> = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [currentCategory, setCurrentCategory] = useState<ICategoryData>({
    id: "",
    name: "",
    description: "",
  });
  const [message, setMessage] = useState<string>("");
  // alert(JSON.stringify("currentCategory"));

  // alert(JSON.stringify(currentCategory));
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
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };

  const deleteCategory = () => {
    CategoryDataService.delete(currentCategory.id)
      .then((response: any) => {
        navigate("/categories");
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };

  
  // alert(JSON.stringify(c cxdrefurrentCategory));
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
