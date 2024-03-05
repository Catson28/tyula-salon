import http from "../../http-common";
import ISubcategoryData from "../types/subcategory.type"

class SubcategoryDataService {
  getAll() {
    return http.get<Array<ISubcategoryData>>("/subcategories");
  }

  get(id: string) {
    return http.get<ISubcategoryData>(`/subcategories/${id}`);
  }

  create(data: ISubcategoryData) {
    return http.post<ISubcategoryData>("/subcategories", data);
  }

  update(data: ISubcategoryData, id: any) {
    return http.put<any>(`/subcategories/${id}`, data);
  }

  delete(id: any) {
    return http.delete<any>(`/subcategories/${id}`);
  }

  deleteAll() {
    return http.delete<any>(`/subcategories`);
  }

  findByTitle(title: string) {
    return http.get<Array<ISubcategoryData>>(`/subcategories?title=${title}`);
  }
}

export default new SubcategoryDataService();