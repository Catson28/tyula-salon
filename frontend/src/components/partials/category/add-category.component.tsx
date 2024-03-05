import React, { Component, ChangeEvent } from "react";
import CategoryDataService from "../../../services/net/category.service";
import ICategoryData from '../../../services/types/category.type';

type Props = {
  onClose: () => void;
};

type State = ICategoryData & {
  submitted: boolean
};

export default class AddCategory extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.onChangeName = this.onChangeName.bind(this);
    this.onChangeDescription = this.onChangeDescription.bind(this);
    this.saveCategory = this.saveCategory.bind(this);
    this.newCategory = this.newCategory.bind(this);

    this.state = {
      id: null,
      name: "",
      description: "",
      submitted: false
    };
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

  saveCategory() {
    const data: ICategoryData = {
      name: this.state.name,
      description: this.state.description
    };

    CategoryDataService.create(data)
      .then((response: any) => {
        this.setState({
          id: response.data.id,
          name: response.data.name,
          description: response.data.description,
          submitted: true
        });
        console.log(response.data);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  }

  newCategory() {
    this.setState({
      id: null,
      name: "",
      description: "",
      submitted: false
    });
  }

  render() {
    const { submitted, name, description } = this.state;

    return (
      <div className="submit-form">
        {submitted ? (
          <div>
            <h4>You submitted successfully!</h4>
            <button className="btn btn-success" onClick={this.newCategory}>
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

            <button onClick={this.saveCategory} className="btn btn-success">
              Submit
            </button>
            <button className="btn btn-primary" onClick={this.props.onClose}>Fechar</button>
          </div>
        )}
      </div>
    );
  }
}
