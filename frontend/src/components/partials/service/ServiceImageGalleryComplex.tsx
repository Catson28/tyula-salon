import React, { useState } from "react";
import styled from "styled-components";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

import { CustomImageData } from '../../../services/types/image.type';

type Props = {
    images: CustomImageData[]; // Array de objetos ServiceData
};

const GalleryContainer = styled.div<{ showSlider: boolean }>`
  position: relative; /* Adicione position relative para GalleryContainer */
  ${props => props.showSlider ? 'width: 100vw; height: 100vh; position: fixed; top: 0; left: 0; z-index: 999; background-color: rgba(0, 0, 0, 0.5); display:block;' : 'display: grid; grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); gap: 10px; display:flex; '}
`;

const ServiceCard = styled.div`
  position: relative; /* Adicione position relative para ServiceCard */
  width: 100%;
  height: 120px;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer;
`;

const ToggleButton = styled.button`
  position: absolute; /* Adicione position absolute para o botão */
  top: 10px; /* Ajuste a posição conforme necessário */
  left: 10px; /* Ajuste a posição conforme necessário */
  z-index: 1000; /* Certifique-se de que o botão apareça sobre a imagem */
  background-color: red;
  color: white;
  border: none;
  font-size: 16px;
  cursor: pointer;
`;

const ServiceImage = styled.img<{ showSlider: boolean; comprimento?: number; altura?: number }>`
${props => props.showSlider ? `width: ${props.comprimento}vh; height: ${props.altura}vh; z-index: 500; object-fit: contain; object-position: center;`: 'width: 100%; height: 100%; object-fit: cover;'}


  ${props => props.showSlider && `
    transition: transform 0.3s ease;
    ${ServiceCard}:hover & {
      transform: scale(1.2); // Aumenta o tamanho da imagem em 20% ao passar o mouse
    }
  `}
`;



const CustomGrid = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 900;
`;

const ServiceImageGalleryComplex: React.FC<Props> = ({ images }) => {
  const [showSlider, setShowSlider] = useState(false);

  const toggleSlider = () => {
    setShowSlider(!showSlider);
  };

  const toggleCloseSlider = () => {
    setShowSlider(!showSlider);
  };

  const settings = {
    dots: true,
    arrows: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
  };

  return (
    <GalleryContainer showSlider={showSlider}>
      {!showSlider ? (
        <>
          {images.map((serviceData, index) => (
            <ServiceCard key={index} onClick={toggleSlider}>
              <ServiceImage src={`http://localhost:8000${serviceData.image.Path}`} alt={`Service Image ${index + 1}`} showSlider={showSlider} />
            </ServiceCard>
          ))}
        </>
      ) : (
        <Slider {...settings}>
          {images.map((serviceData, index) => (
            <div key={index}>
              <CustomGrid >
                <ToggleButton onClick={toggleCloseSlider}>X</ToggleButton> {/* Botão para fechar o slider */}
                <ServiceImage  comprimento={80} altura={80} src={`http://localhost:8000${serviceData.image.Path}`} alt={`Service Image ${index + 1}`} showSlider={showSlider} />
              </CustomGrid>
            </div>
          ))}
        </Slider>
      )}
    </GalleryContainer>
  );
};

export default ServiceImageGalleryComplex;
