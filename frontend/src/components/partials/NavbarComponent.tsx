import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { FaHome, FaAddressBook, FaBriefcase, FaCogs, FaChevronRight, FaShoppingCart, FaCubes, FaWrench, FaUsers, FaChartLine, FaBoxes  } from 'react-icons/fa';
import DynamicContent from './DynamicContent';
import { Link } from 'react-router-dom'; // Importe o Link do react-router-dom
import NavbarSkelet from './NavbarSkelety';


interface SidebarProps {
  collapsed: boolean;
}

const SkeletonLoader = styled.div`
  /* Estilos para o esqueleto de carregamento */
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f0f0;
`;

const Sidebar = styled.div<SidebarProps>`
  height: 100%;
  width: ${({ collapsed }) => (collapsed ? '80px' : '200px')};
  position: fixed;
  top: 0;
  left: 0;
  background-color: #333;
  overflow-x: hidden;
  transition: width 0.5s;
`;

const SidebarHeader = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80px;
  color: white;
`;

const SidebarNav = styled.div`
  padding-top: 20px;
`;

const Nav = styled.nav`
  width: 100%;
  display: flex;
  flex-direction: column;
`;


const NavLink = styled(Link)<{ active: boolean }>`
  display: block;
  align-items: center;
  padding: 10px 20px;
  color: ${({ active }) => (active ? 'red' : 'white')}; // Estilo para rota ativa
  text-decoration: none;
  transition: background-color 0.3s;

  &:hover {
    background-color: #555;
  }
`;

const NavSubLink = styled.a<{ active: boolean; visible: boolean }>`
  display: ${({ visible }) => (visible ? 'block' : 'none')};
  align-items: center;
  padding: 10px 20px;
  color: ${({ active }) => (active ? 'red' : 'white')}; // Estilo para rota ativa
  text-decoration: none;
  transition: background-color 0.3s;

  &:hover {
    background-color: #555;
  }
`;



const IconDiv = styled.div`
  margin-right: 10px;
`;

const TitleDiv = styled.div``;

const NavTitle = styled.span<{ collapsed: boolean }>`
  display: ${({ collapsed }) => (collapsed ? 'none' : 'inline')};
`;

const Navbar = styled.nav<{ sidebarWidth: string }>`

  margin-left: ${({ sidebarWidth }) => sidebarWidth};
  transition: margin-left 0.5s;
  background-color: #303;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
`;

const Logo = styled.div`
  font-size: 1.5rem;
`;

const Links = styled.div`
  display: flex;
  align-items: center;
`;

const NavbarLink = styled(Link)`
  color: white;
  text-decoration: none;
  margin-right: 20px;
`;

const AuthLinks = styled.div`
  display: flex;
  align-items: center;
`;

const AuthLink = styled.a`
  color: white;
  text-decoration: none;
  margin-left: 20px;
`;

const HideButton = styled.button`
  background-color: #007bff;
  color: #fff;
  padding: 5px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #0056b3;
  }
`;


const NavbarComponent = ({  children }: React.PropsWithChildren) => {
  const [activeRoute, setActiveRoute] = useState('');

  const [collapsed, setCollapsed] = useState(false);
  // const [sublinkVisible, setSublinkVisible] = useState(false);
  const sidebarWidth = collapsed ? '80px' : '200px';
  const [sublinkVisible, setSublinkVisible] = useState({
    works: false,
    services: false,
  });
  const [loading, setLoading] = useState(true); // Estado para controlar o carregamento

  useEffect(() => {
    // Simulação de carregamento com um timer
    const timer = setTimeout(() => {
      setLoading(false); // Define o carregamento como concluído após o tempo especificado
    }, 2000); // Tempo de simulação em milissegundos

    return () => clearTimeout(timer); // Limpa o timer ao desmontar o componente
  }, []);

  const toggleSidebar = () => {
    setCollapsed(!collapsed);
  };


  const handleSublinkHover = (section: string, isVisible: boolean) => {
    setSublinkVisible((prevState) => ({
      ...prevState,
      [section]: isVisible,
    }));
    setActiveRoute(section); // Define a rota ativa ao entrar no sublink
  };

  const adicionealgo = () => {
    console.log('Carregamento completo! Faça algo aqui.');
    setLoading(false); // Define o carregamento como concluído
  };
  

  return (
    <>
      {loading ? (
        <SkeletonLoader>
            <h1>Loading...</h1>
        </SkeletonLoader>
      ) : (<>
            <Navbar sidebarWidth={sidebarWidth}>
              <HideButton onClick={toggleSidebar}>
                Hide
              </HideButton>
              <Links>
                <NavbarLink to="/">Home</NavbarLink>
                <NavbarLink to="/contacts">Contacts</NavbarLink>
                <NavbarLink to="/TestAllBeauty">All Functions</NavbarLink>
              </Links>
              <AuthLinks>
                <AuthLink href="#">Login / Signup</AuthLink>
                <AuthLink href="#">Logout</AuthLink>
              </AuthLinks>
            </Navbar>
            <Sidebar collapsed={collapsed}>
              <SidebarHeader>Logo</SidebarHeader>
              <SidebarNav>
                <Nav>
                  <NavLink to="/"
                    active={activeRoute === 'home'} // Passa a rota ativa para NavSubLink
                  >
                    <FaHome /> <NavTitle collapsed={collapsed}>Home</NavTitle>
                  </NavLink>

                  <NavLink to="/sale" active={activeRoute === 'sale'}>
                    <FaShoppingCart /> <NavTitle collapsed={collapsed}>Sale ou Vendas</NavTitle>
                  </NavLink>

                  <NavLink to="/products" active={activeRoute === 'products'}>
                    <FaCubes /> <NavTitle collapsed={collapsed}>Produtos</NavTitle>
                  </NavLink>

                  <NavLink to="/services" active={activeRoute === 'services'}>
                    <FaWrench /> <NavTitle collapsed={collapsed}>Serviços</NavTitle>
                  </NavLink>

                  <NavLink to="/employees" active={activeRoute === 'employees'}>
                    <FaUsers /> <NavTitle collapsed={collapsed}>Funcionários</NavTitle>
                  </NavLink>

                  <NavLink to="/sales-reports" active={activeRoute === 'sales-reports'}>
                    <FaChartLine /> <NavTitle collapsed={collapsed}>Relatórios de Vendas</NavTitle>
                  </NavLink>

                  <NavLink to="/inventory-control" active={activeRoute === 'inventory-control'}>
                    <FaBoxes /> <NavTitle collapsed={collapsed}>Controle de Estoque</NavTitle>
                  </NavLink>

                  <NavLink to="/contacts"
                    active={activeRoute === 'contacts'} // Passa a rota ativa para NavSubLink
                  >
                    <FaAddressBook /> <NavTitle collapsed={collapsed}>Contacts</NavTitle>
                  </NavLink>
                  <NavLink
                    to="/works"
                    onMouseEnter={() => handleSublinkHover('works',true)}
                    onMouseLeave={() => handleSublinkHover('works',false)}
                    active={activeRoute === 'work'} // Passa a rota ativa para NavSubLink
                  
                  >
                    <FaBriefcase /> <NavTitle collapsed={collapsed}>Works <FaChevronRight /></NavTitle>
                    {!collapsed && (
                      <Nav>
                        <NavSubLink visible={sublinkVisible.works} href="/works/sublink1"
                    active={activeRoute === 'sublink1'} // Passa a rota ativa para NavSubLink
                    >Sublink 1</NavSubLink>
                        <NavSubLink visible={sublinkVisible.works} href="/works/sublink2"
                    active={activeRoute === 'sublink2'} // Passa a rota ativa para NavSubLink
                    >Sublink 2</NavSubLink>
                        <NavSubLink visible={sublinkVisible.works} href="/works/sublink3"
                    active={activeRoute === 'sublink3'} // Passa a rota ativa para NavSubLink
                    >Sublink 3</NavSubLink>
                      </Nav>
                    )}
                  </NavLink>
                  <NavLink to="/allfuncs"
                    active={activeRoute === 'allfuncs'} // Passa a rota ativa para NavSubLink
                  
                  >
                    <FaCogs /> <NavTitle collapsed={collapsed}>All Functions</NavTitle>
                  </NavLink>
                  <NavLink
                    to="/TestAllBeauty"
                    onMouseEnter={() => handleSublinkHover('services',true)}
                    onMouseLeave={() => handleSublinkHover('services',false)}
                    active={activeRoute === '/TestAllBeauty'} // Passa a rota ativa para NavSubLink
                  
                  
                    >
                    <FaBriefcase /><NavTitle collapsed={collapsed}>Services <FaChevronRight /></NavTitle>
                    {!collapsed && (
                      <Nav>
                        <NavSubLink visible={sublinkVisible.services} href="/works/sublink1"
                    active={activeRoute === 'subtile1'} // Passa a rota ativa para NavSubLink
                    >Sublink 1</NavSubLink>
                        <NavSubLink visible={sublinkVisible.services} href="/works/sublink2"
                    active={activeRoute === 'subtile2'} // Passa a rota ativa para NavSubLink
                    >Sublink 2</NavSubLink>
                        <NavSubLink visible={sublinkVisible.services} href="/works/sublink3"
                    active={activeRoute === 'subtile3'} // Passa a rota ativa para NavSubLink
                    >Sublink 3</NavSubLink>
                      </Nav>
                    )}
                  </NavLink>
                </Nav>
              </SidebarNav>
            </Sidebar>

            <DynamicContent sidebarWidth={sidebarWidth} >
              {children} {/* Renderizando o conteúdo dinâmico aqui */}
            </DynamicContent>

            </>
            )}
    </>
  );
};

export default NavbarComponent;
