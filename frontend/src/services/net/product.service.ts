import http from "./base/http-common";
import IProductData from "../types/product.type";

class ProductDataService {
  getAll() {
    return http.get<Array<IProductData>>("api/products/list/");
  }

  get(id: string) {
    return http.get<IProductData>(`api/products/read/${id}/`);
  }

  create(data: IProductData) {
    return http.post<IProductData>("api/products/add/", data);
  }

  update(data: IProductData, id: any) {
    return http.put<any>(`api/products/update/${id}/`, data);
  }

  delete(id: any) {
    return http.delete<any>(`api/products/delete/${id}/`);
  }

  deleteAll() {
    return http.delete<any>(`api/products/deleteAll/`);
  }

  findByName(name: string) {
    return http.get<Array<IProductData>>(`api/products/search?name=${name}`);
  }
}

export default new ProductDataService();
