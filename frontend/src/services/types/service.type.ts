// types/service.type.ts
import { CustomImageData } from './image.type';
import IProductData from './product.type';

type IServiceData = {
  id: number;
  name: string;
  description: string;
  price?: string; // Adicione o campo price opcional, caso necessário
  subcategory: number | string; // Altere para number se for o tipo correto
  cover?: {
    ImageID: number;
    Path: string;
    object_id: number;
    content_type: number;
  } | null;
  images: CustomImageData[]; // Adicione a propriedade images ao tipo ICategoryData
  products: IProductData[]; // Adicione a propriedade products ao tipo ICategoryData
};

export default IServiceData;
