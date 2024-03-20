import React, { Component, ChangeEvent } from "react";
import ServiceDataService from "../../../services/net/ServiceDataService";
import IServiceData from '../../../services/types/service.type';

type Props = {
  onClose: () => void;
  onEditService: (service: IServiceData) => void; // Adding property to handle service edit in the parent
};

type State = {
  services: Array<IServiceData>,
  currentService: IServiceData | null,
  currentIndex: number,
  searchName: string
};

export default class ServicesList extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.onChangeSearchName = this.onChangeSearchName.bind(this);
    this.retrieveServices = this.retrieveServices.bind(this);
    this.refreshList = this.refreshList.bind(this);
    this.setActiveService = this.setActiveService.bind(this);
    this.removeAllServices = this.removeAllServices.bind(this);
    this.searchName = this.searchName.bind(this);

    this.state = {
      services: [],
      currentService: null,
      currentIndex: -1,
      searchName: ""
    };
  }

  componentDidMount() {
    this.retrieveServices();
  }

  onChangeSearchName(e: ChangeEvent<HTMLInputElement>) {
    const searchName = e.target.value;

    this.setState({
      searchName: searchName
    });
  }

  retrieveServices() {
    ServiceDataService.getAll()
      .then((response: any) => {
        this.setState({
          services: response.data
        });
        console.log(response.data);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  }

  refreshList() {
    this.retrieveServices();
    this.setState({
      currentService: null,
      currentIndex: -1
    });
  }

  setActiveService(service: IServiceData, index: number) {
    this.setState({
      currentService: service,
      currentIndex: index
    });
  }

  removeAllServices() {
    ServiceDataService.deleteAll()
      .then((response: any) => {
        console.log(response.data);
        this.refreshList();
      })
      .catch((e: Error) => {
        console.log(e);
      });
  }

  searchName() {
    this.setState({
      currentService: null,
      currentIndex: -1
    });

    ServiceDataService.findByName(this.state.searchName)
      .then((response: any) => {
        this.setState({
          services: response.data
        });
        console.log(response.data);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  }

  render() {
    const { searchName, services, currentService, currentIndex } = this.state;

    return (
      <div className="list row">
        <div className="col-md-8">
          <div className="input-group mb-3">
            <input
              type="text"
              className="form-control"
              placeholder="Search by name"
              value={searchName}
              onChange={this.onChangeSearchName}
            />
            <div className="input-group-append">
              <button
                className="btn btn-outline-secondary"
                type="button"
                onClick={this.searchName}
              >
                Search
              </button>
            </div>
          </div>
        </div>
        <div className="col-md-6">
          <h4>Lista de Servicos</h4>

          <ul className="list-group">
            {services &&
              services.map((service: IServiceData, index: number) => (
                <li
                  className={
                    "list-group-item " +
                    (index === currentIndex ? "active" : "")
                  }
                  onClick={() => this.setActiveService(service, index)}
                  key={index}
                >
                  {service.name}
                </li>
              ))}
          </ul>

          <button
            className="m-3 btn btn-sm btn-danger"
            onClick={this.removeAllServices}
          >
            Remove All
          </button>
        </div>
        <div className="col-md-6">
          {currentService ? (
            <div>
              <h4>Service</h4>
              <div>
                <label>
                  <strong>Name:</strong>
                </label>{" "}
                {currentService.name}
              </div>
              <div>
                <label>
                  <strong>Description:</strong>
                </label>{" "}
                {currentService.description}
              </div>
              <div>
                <label>
                  <strong>Price:</strong>
                </label>{" "}
                {currentService.price}
              </div>
                  {/* Button to edit the service */}
                  <button
                    className="btn btn-sm badge badge-warning btn-warning ml-2"
                    onClick={() => this.props.onEditService(currentService)}
                  >
                    Edit
                  </button>

            </div>
          ) : (
            <div>
              <br />
              <p>(List) --- Please click on a Service...</p>
            </div>
          )}
        </div>
      </div>
    );
  }
}
