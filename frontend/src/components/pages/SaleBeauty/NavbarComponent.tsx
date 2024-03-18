import React, { useState } from 'react';
import styled from 'styled-components';
import { FaHome, FaAddressBook, FaBriefcase, FaCogs, FaUser, FaSignOutAlt, FaChevronRight } from 'react-icons/fa';

interface SidebarProps {
  collapsed: boolean;
}

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

const NavLink = styled.a`
  display: block;
  align-items: center;
  padding: 10px 20px;
  color: white;
  text-decoration: none;
  transition: background-color 0.3s;

  &:hover {
    background-color: #555;
  }
`;

const Navbar = styled.nav`
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

const NavbarLink = styled.a`
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

const NavbarComponent = () => {
  const [collapsed, setCollapsed] = useState(false);

  const toggleSidebar = () => {
    setCollapsed(!collapsed);
  };

  return (
    <>
      <Navbar>
        <Logo>Logo</Logo>
        <Links>
          <NavbarLink href="/">Home</NavbarLink>
          <NavbarLink href="/contacts">Contacts</NavbarLink>
          <NavbarLink href="/allfuncs">All Functions</NavbarLink>
        </Links>
        <AuthLinks>
          <AuthLink href="#">Login / Signup</AuthLink>
          <AuthLink href="#">Logout</AuthLink>
        </AuthLinks>
        <button onClick={toggleSidebar}>Toggle Sidebar</button>
      </Navbar>
      <Sidebar collapsed={collapsed}>
        <SidebarHeader>Logo</SidebarHeader>
        <SidebarNav>
          <Nav>
            <NavLink href="/">
              <FaHome /> Home
            </NavLink>
            <NavLink href="/contacts">
              <FaAddressBook /> Contacts
            </NavLink>
            <NavLink href="/works">
              <FaBriefcase /> Works <FaChevronRight />
              {collapsed ? null : (
                <Nav>
                  <NavLink href="/works/sublink1">Sublink 1</NavLink>
                  <NavLink href="/works/sublink2">Sublink 2</NavLink>
                  <NavLink href="/works/sublink3">Sublink 3</NavLink>
                </Nav>
              )}
            </NavLink>
            <NavLink href="/allfuncs">All Functions</NavLink>
            <NavLink href="/servicos">
              <FaCogs /> Servicos <FaChevronRight />
              {collapsed ? null : (
                <Nav>
                  <NavLink href="/servicos/sublink1">Sublink 1</NavLink>
                  <NavLink href="/servicos/sublink2">Sublink 2</NavLink>
                </Nav>
              )}
            </NavLink>
          </Nav>
        </SidebarNav>
      </Sidebar>
    </>
  );
};

export default NavbarComponent;
