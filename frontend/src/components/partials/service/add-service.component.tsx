import React, { Component, ChangeEvent } from "react";
import ServiceDataService from "../../../services/net/ServiceDataService";
import IServiceData from '../../../services/types/service.type';
import ICategoryData from '../../../services/types/category.type';
import CategoryDataService from "../../../services/net/CategoryDataService";
import ISubcategoryData from '../../../services/types/subcategory.type';
import SubcategoryDataService from "../../../services/net/SubcategoryDataService";

type Props = {
  onClose: () => void;
};

type State = IServiceData & {
  submitted: boolean;
  categories: Array<ICategoryData>;
  selectedCategory: string;
  subcategories: Array<ISubcategoryData>;
  selectedSubcategory: string;
};

export default class AddService extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.onChangeName = this.onChangeName.bind(this);
    this.onChangeDescription = this.onChangeDescription.bind(this);
    this.onChangeCategory = this.onChangeCategory.bind(this);
    this.onChangeSubcategory = this.onChangeSubcategory.bind(this);
    this.saveService = this.saveService.bind(this);
    this.newService = this.newService.bind(this);

    this.state = {
      id: null,
      name: "",
      description: "",
      price: 0,
      category: "",
      subcategory: "",
      categories: [],
      selectedCategory: "",
      subcategories: [],
      selectedSubcategory: "",
      images: [], // Add the images property here
      submitted: false,
    };
  }

  componentDidMount() {
    CategoryDataService.getAll()
      .then((response: any) => {
        this.setState({
          categories: response.data
        });
        console.log(response.data);
      })
      .catch((e: Error) => {
        console.log(e);
      });

      SubcategoryDataService.getAll()
      .then((response: any) => {
        this.setState({
          subcategories: response.data
        });
        console.log(response.data);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  }

  onChangeName(e: ChangeEvent<HTMLInputElement>) {
    this.setState({
      name: e.target.value
    });
  }

  onChangeDescription(e: ChangeEvent<HTMLInputElement>) {
    this.setState({
      description: e.target.value
    });
  }

  onChangeCategory(e: ChangeEvent<HTMLSelectElement>) {
    this.setState({
      selectedCategory: e.target.value
    });
  }

  onChangeSubcategory(e: ChangeEvent<HTMLSelectElement>) {
    this.setState({
      selectedSubcategory: e.target.value
    });
  }

  saveService() {
    const data: IServiceData = {
      name: this.state.name,
      description: this.state.description,
      price: this.state.price,
      category: this.state.selectedCategory,
      subcategory: this.state.selectedSubcategory,
      images: this.state.images // Assuming images is of type array
    };

    ServiceDataService.create(data)
      .then((response: any) => {
        this.setState({
          id: response.data.id,
          name: response.data.name,
          description: response.data.description,
          price: response.data.price,
          category: response.data.category,
          subcategory: response.data.subcategory,
          submitted: true
        });
        console.log(response.data);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  }

  /* 

  newService() {
    this.setState({
      id: null,
      name: "",
      description: "",
      price: 0,
      category: "", // Adjust if needed
      selectedCategory: "", // Reset selectedCategory if needed
      selectedSubcategory: "", // Reset selectedSubcategory
      submitted: false
    });
  }
  */
  newService() {
    this.setState({
      id: null,
      name: "",
      description: "",
      price: 0,
      category: "", // Adjust if needed
      subcategory: "", // Adjust if needed
      images: [], // Reset the images array
      submitted: false
    });
  } 
  


  render() {
    const { submitted, name, description, price, categories, selectedCategory, subcategories, selectedSubcategory } = this.state;

    return (
      <div className="submit-form">
        {submitted ? (
          <div>
            <h4>You submitted successfully!</h4>
            <button className="btn btn-success" onClick={this.newService}>
              Add
            </button>
          </div>
        ) : (
          <div>
            <div className="form-group">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                className="form-control"
                id="name"
                required
                value={name}
                onChange={this.onChangeName}
                name="name"
              />
            </div>

            <div className="form-group">
              <label htmlFor="description">Description</label>
              <input
                type="text"
                className="form-control"
                id="description"
                required
                value={description}
                onChange={this.onChangeDescription}
                name="description"
              />
            </div>

            <div className="form-group">
              <label htmlFor="price">Price</label>
              <input
                type="number"
                className="form-control"
                id="price"
                required
                value={price}
                onChange={(e) => this.setState({ price: parseInt(e.target.value) })}
                name="price"
              />
            </div>

            <div className="form-group">
              <label htmlFor="category">Category</label>
              <select
                className="form-control"
                id="category"
                required
                value={selectedCategory}
                onChange={this.onChangeCategory}
                name="category"
              >
                <option value="">Select a category</option>
                {categories.map((category: ICategoryData, index: number) => (
                  <option key={index} value={category.id}>{category.name}</option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="subcategory">Subcategory</label>
              <select
                className="form-control"
                id="subcategory"
                required
                value={selectedSubcategory}
                onChange={this.onChangeSubcategory}
                name="subcategory"
              >
                <option value="">Select a subcategory</option>
                {subcategories.map((subcategory: ISubcategoryData, index: number) => (
                  <option key={index} value={subcategory.id}>{subcategory.name}</option>
                ))}
              </select>
            </div>

            <button onClick={this.saveService} className="btn btn-success">
              Submit
            </button>
          </div>
        )}
      </div>
    );
  }
}
