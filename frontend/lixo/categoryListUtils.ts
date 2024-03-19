// categoryListUtils.ts
import CategoryDataService from "../src/services/net/CategoryDataService";
import ICategoryData from "../src/services/types/category.type";

export function retrieveCategories() {
  return CategoryDataService.getAll()
    .then((response: any) => {
      return response.data;
    })
    .catch((e: Error) => {
      console.log(e);
      return [];
    });
}

export function removeAllCategories() {
  return CategoryDataService.deleteAll()
    .then((response: any) => {
      console.log(response.data);
      return true;
    })
    .catch((e: Error) => {
      console.log(e);
      return false;
    });
}

export function searchCategoryByName(name: string) {
  return CategoryDataService.findByName(name)
    .then((response: any) => {
      return response.data;
    })
    .catch((e: Error) => {
      console.log(e);
      return [];
    });
}
