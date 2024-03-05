import http from "../../http-common";
import ICategoryData from "../types/category.type"

class CategoryDataService {
  getAll() {
    return http.get<Array<ICategoryData>>("api/categories/list/");
  }

  get(id: string) {
    return http.get<ICategoryData>(`api/categories/${id}`);
  }

  create(data: ICategoryData) {
    return http.post<ICategoryData>("api/categories/add/", data);
  }

  update(data: ICategoryData, id: any) {
    return http.put<any>(`api/categories/${id}`, data);
  }

  delete(id: any) {
    return http.delete<any>(`api/categories/delete/${id}`);
  }

  deleteAll() {
    return http.delete<any>(`api/categories`);
  }

  findByName(name: string) {
    return http.get<Array<ICategoryData>>(`api/categories?name=${name}`);
  }
}

export default new CategoryDataService();