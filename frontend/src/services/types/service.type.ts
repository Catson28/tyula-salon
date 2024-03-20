export default interface IServiceData {
    id?: any | null;
    name: string;
    description: string;
    price: number;
    category: string; // Suponho que o campo "category" seja uma referência ao ID da categoria
    subcategory: string; // Suponho que o campo "subcategory" seja uma referência ao ID da subcategoria
  }
  