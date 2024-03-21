import React from "react";
import styled from "styled-components";

import { CustomImageData } from '../../../services/types/image.type';

type Props = {
    images: CustomImageData[]; // Array de objetos ServiceData
};

const GalleryContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 10px;
`;

const ServiceCard = styled.div`
  width: 100%;
  height: 120px;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const ServiceImage = styled.img`
  width: 100%;
  height: 100%;
  object-fit: cover;
`;

const ServiceImageGalleryComplex: React.FC<Props> = ({ images }) => {
  return (
    <GalleryContainer>
      {images.map((serviceData, index) => (
        <ServiceCard key={index}>
          <ServiceImage src={`http://localhost:8000${serviceData.image.Path}`} alt={`Service Image ${index + 1}`} />
        </ServiceCard>
      ))}
    </GalleryContainer>
  );
};

export default ServiceImageGalleryComplex;

// Declaração de export vazia para tratar o arquivo como um módulo
export {};
