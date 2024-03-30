import React, { useState } from "react";
import styled from 'styled-components';
import NavbarComponent from '../../partials/NavbarComponent'

const GridContainer = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  height: 100vh;
`;

const RightPane = styled.div`
  grid-column: 2 / 3;
  grid-row: 1 / 3;
  grid-template-rows: 1fr 1fr 1fr;
  background-color: lightblue;
`;

const TopLeftPane = styled.div`
  background-color: lightgreen;
`;

const BottomLeftPane = styled.div`
  background-color: lightcoral;
`;



// Estilos para o container principal
const FormControl = styled.div`
padding: 10px;
// display: flex;
// flex-direction: row;
align-items: center;
gap: 10px;
`;
const FormColumn = styled.div`
  width:100%;
  // display: flex;
  // flex-direction: row;
 flex: 1; /* Ocupa todo o espaço disponível */
`;

// Estilos para o container principal
const GroupRowItems = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content:space-between;
`;

// Estilos para o container principal
const GroupRowContent = styled.div`
  display: flex;
  flex-direction: row;
  grid-template-rows: 1fr 1fr;
  // align-items: center;
  // justify-content:space-between;
`;

// Estilos para o título ou label
const Titles = styled.h2`
  font-size: 18px;
`;



const Title = styled.div<{ selected: boolean }>`
  position: absolute;
  bottom: 5px;
  left: 5px;
  font-weight: bold;
  color: ${({ selected }) => (selected ? 'white' : 'black')};
`;

// Estilos para o select dropdown
const Select = styled.select`
  flex: 1; /* Ocupa todo o espaço disponível */
  padding: 8px;
  margin:5px;
  border-radius: 5px;
  border: 1px solid #ccc;
`;

// Estilos para o select dropdown
const InputField = styled.input`
  flex: 1; /* Ocupa todo o espaço disponível */
  padding: 4px;
  margin:5px;
  border-radius: 5px;
  border: 1px solid #ccc;
`;

// Estilos para o botão "Adicionar"
const Button = styled.button`
  padding: 8px 12px; /* Ajuste o padding conforme necessário */
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #0056b3;
  }
`;

const GridComponent = () => {



  const [selectedCard, setSelectedCard] = useState<number | null>(null);

  const handleCardClick = (index: number) => {
    setSelectedCard(index);
  };

  return (
    <NavbarComponent>
        <GridContainer>
          <RightPane>
            <FormControl>
              <GroupRowContent>
                <FormColumn>
                  <Titles>Servico:</Titles>
                  <InputField />
                </FormColumn>
                <FormColumn>
                  <Titles>Nota:</Titles>
                  <Select>
                    <option value="opcao1">selecione o valor</option>
                    <option value="opcao1">200</option>
                    <option value="opcao2">500</option>
                    <option value="opcao3">1000</option>
                    <option value="opcao3">2000</option>
                    <option value="opcao3">5000</option>
                  </Select>
                  <Button>Adicionar</Button>                
                </FormColumn>                
              </GroupRowContent>


            </FormControl>

            
            <FormControl>
              <GalleryContainer>
                <ServiceCard selected={selectedCard === 0} onClick={() => handleCardClick(0)}>
                  <Title selected={selectedCard === 0}>Atom</Title>
                  <Subtitle>11.99</Subtitle>
                  <ServiceImage src="http://localhost:8000/media/images/35652246.jpg" alt="Service Image" />
                </ServiceCard>
                <ServiceCard selected={selectedCard === 1} onClick={() => handleCardClick(1)}>
                  <Title selected={selectedCard === 1}>Limon</Title>
                  <Subtitle>110.99</Subtitle>
                  <ServiceImage src="http://localhost:8000/media/images/D_NQ_NP_773592-MLB71333730379_082023-O.webp" alt="Service Image" />
                </ServiceCard>
                <ServiceCard selected={selectedCard === 2} onClick={() => handleCardClick(2)}>
                  <Title selected={selectedCard === 2}>Limon</Title>
                  <Subtitle>110.99</Subtitle>
                  <ServiceImage src="http://localhost:8000/media/images/D_NQ_NP_773592-MLB71333730379_082023-O.webp" alt="Service Image" />
                </ServiceCard>
                <ServiceCard selected={selectedCard === 3} onClick={() => handleCardClick(3)}>
                  <Title selected={selectedCard === 3}>Limon</Title>
                  <Subtitle>110.99</Subtitle>
                  <ServiceImage src="http://localhost:8000/media/images/D_NQ_NP_773592-MLB71333730379_082023-O.webp" alt="Service Image" />
                </ServiceCard>
                <ServiceCard selected={selectedCard === 4} onClick={() => handleCardClick(4)}>
                  <Title selected={selectedCard === 4}>Limon</Title>
                  <Subtitle>110.99</Subtitle>
                  <ServiceImage src="http://localhost:8000/media/images/D_NQ_NP_773592-MLB71333730379_082023-O.webp" alt="Service Image" />
                </ServiceCard>
              </GalleryContainer>  
            </FormControl>




          </RightPane>
          <TopLeftPane>       




          <FormControl>
              <Titles>Selecione Cliente:</Titles>
              <GroupRowItems>
                <Select>
                  <option value="opcao1">Opção 1</option>
                  <option value="opcao2">Opção 2</option>
                  <option value="opcao3">Opção 3</option>
                </Select>
                <Button>Adicionar</Button>
              </GroupRowItems>
            </FormControl>



          </TopLeftPane>
          <BottomLeftPane>Bottom Left Pane</BottomLeftPane>
        </GridContainer>
    </NavbarComponent>

  );
};

export default GridComponent;


// Styled component for flex container
const FlexContainer = styled.div`
  display: flex;
  flex-wrap: wrap;
`;

const GalleryContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  gap: 10px;
`;

const ServiceCard = styled.div<{ selected: boolean }>`
  position: relative;
  width: 100%;
  height: 110px;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  border: 2px solid transparent;
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);

  &:hover {
    transform: scale(1.05);
  }

  ${({ selected }) =>
    selected &&
    `
    transform: scale(1.1);
    border-color: #0d6efd;
  `}
`;


const ServiceImage = styled.img`
  width: 100%;
  height: 100%;
  object-fit: cover;
`;

const Subtitle = styled.div`
  position: absolute;
  bottom: 5px;
  right: 5px;
  font-size: 12px;
`;
