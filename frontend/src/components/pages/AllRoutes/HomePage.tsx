import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from "react-router-dom";
import Navbar from "../../partials/Navbar";
import NavbarComponent from "../../partials/NavbarComponent";
import Carousel from "../../partials/Carousel";

import TelaDoNavegador from '../../partials/HelperResposnve/TelaDoNavegador';

import styled from 'styled-components';

const ContainerFluid = styled.div`
  width: 100%;
`;

const Container = styled.div`
  margin-right: auto;
  margin-left: auto;
  padding-right: 15px;
  padding-left: 15px;
`;

const Row = styled.div`
  display: flex;
  flex-wrap: wrap;
  margin-right: -15px;
  margin-left: -15px;
`;

const Col = styled.div`
  flex: 0 0 100%;
  max-width: 100%;
  padding-right: 15px;
  padding-left: 15px;

  @media (min-width: 576px) {
    flex: 0 0 50%;
    max-width: 50%;
  }

  @media (min-width: 992px) {
    flex: 0 0 20%;
    max-width: 20%;
  }
`;

const LinkStyled = styled(Link)`
  display: block;
  padding: 1rem;
  border: 1px solid #dee2e6;
  background-color: #f8f9fa;
  color: #212529;
  text-decoration: none;
  text-align: center;
`;

const StyledDiv = styled.div`
  display: block;
  padding: 1rem;
  border: 1px solid #dee2e6;
  background-color: #f8f9fa;
  text-align: center;
`;

const HomePage: React.FC = () => {
  return (
    <>
      <NavbarComponent />
      <Carousel />
      <Navbar />

      <ContainerFluid>
        <Container>
          <Row>
            <Col>
              <LinkStyled to="/AllBeauty">CRUDS</LinkStyled>
            </Col>
            <Col>
              <LinkStyled to="/beauty">CARREGAR IMAGEM</LinkStyled>
            </Col>
            <Col>
              <LinkStyled to="/items">CRUDS CONTEXT API</LinkStyled>
            </Col>
            <Col>
              <LinkStyled to="/TestAllBeauty">CRUDS Test</LinkStyled>
            </Col>
            <Col>
              <LinkStyled to="/estilo">estilos</LinkStyled>
              <StyledDiv>Row column</StyledDiv>
            </Col>
            <Col>
              <LinkStyled to="/palavras">palavras</LinkStyled>
              <StyledDiv>Row column</StyledDiv>
            </Col>
            {/* Repita conforme necessário */}
          </Row>
        </Container>
      </ContainerFluid> 
      <TelaDoNavegador />

    </>

  );
};

export default HomePage;
