export default interface IProductData {
    id?: any | null;
    name: string;
    description: string;
    category: string; // Suponho que o campo "category" seja uma referência ao ID da categoria
  }
  