import React, { useState, useEffect } from 'react';
import styled, { keyframes, css } from 'styled-components';

// Definição de imagens e textos para cada grupo
const imagesAndTexts = [
  {
    image: 'http://localhost:8000/media/images/8515cd56b16ebe3b2f41af8091762ec3.JPEG',
    text: 'Texto 1'
  },
  {
    image: 'http://localhost:8000/media/images/277254782_5015332358560493_7370300353602031270_n_4hogsk4.jpg',
    text1: 'Texto 2-1',
    text2: 'Texto 2-2'
  },
  {
    backgroundImage: 'http://localhost:8000/media/images/8515cd56b16ebe3b2f41af8091762ec3.JPEG',
    text: 'Texto 3',
    smallImage: 'http://localhost:8000/media/images/1668952320921.JPEG'
  }
];

const CarouselContainer = styled.div`
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
`;

const fadeIn = keyframes`
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
`;

const fadeOut = keyframes`
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
`;

const Image = styled.div<{ src: string; backgroundImage?: boolean }>`
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: ${({ src }) => src && `url(${src})`};
  background-size: cover;
  background-position: center;
  animation: ${({ backgroundImage }) =>
    backgroundImage
      ? css`
          ${fadeIn} 1s ease-in-out forwards
        `
      : css`
          ${fadeOut} 1s ease-in-out forwards
        `};
`;

const Text = styled.div`
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 24px;
  font-weight: bold;
  animation: ${fadeIn} 1s ease-in-out forwards;
`;

const Carousel: React.FC = () => {
    const [index, setIndex] = useState(0);
  
    useEffect(() => {
      const interval = setInterval(() => {
        setIndex((prevIndex) => (prevIndex + 1) % imagesAndTexts.length);
      }, 4000); // Altere o intervalo conforme necessário
      return () => clearInterval(interval);
    }, []);
  
    const currentItem = imagesAndTexts[index];
  
    return (
      <CarouselContainer>
        {currentItem.image && (
          <Image src={currentItem.image} backgroundImage={!currentItem.text} />
        )}
        {currentItem.text && (
          <Text>{currentItem.text}</Text>
        )}
        {currentItem.text1 && (
          <Text>{currentItem.text1}</Text>
        )}
        {currentItem.text2 && (
          <Text>{currentItem.text2}</Text>
        )}
        {currentItem.smallImage && (
          <Image src={currentItem.smallImage} />
        )}
        {currentItem.backgroundImage && (
          <Image src={currentItem.backgroundImage} />
        )}
      </CarouselContainer>
    );
  };
  

export default Carousel;
