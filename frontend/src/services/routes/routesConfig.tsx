// src/routes/routesConfig.tsx
import { RouteProps } from 'react-router-dom';
import React from 'react';
import ItemsPage from '../../components/pages/CRUD-Context/ItemsPage';
import HomeContextPage from '../../components/pages/HomeContextPage';
import LumeIt from '../../components/pages/LumeIt';
import HomePage from '../../components/pages/AllRoutes/HomePage';
import SaleBeauty from '../../components/pages/SaleBeauty';
import AllBeauty from '../../../lixo/AllBeauty';
import TestAllBeauty from '../../components/pages/Services/AllService';
import Palavras from '../../components/pages/Palavras/Palavras';
import NavbarComponent from '../../components/partials/NavbarCompone';
import Table1 from '../../components/pages/Table/Table1';
import Table2 from '../../components/pages/Table/Table12';
// import ComponentSlider from '../../components/partials/carrocel/ComponentSlider';

// import AboutPage from '../../components/pages/AboutPage';
// import ContactPage from '../../components/pages/ContactPage';

interface RouteConfigBase {
  path: string;
  element: React.ReactNode;
}

type RouteConfig = RouteProps & RouteConfigBase;

const routes: RouteConfig[] = [
  {
    path: '/',
    element: <HomePage />,
  },
  {
    path: '/lumeIT',
    element: <LumeIt />,
  }, 
  {
    path: '/Context',
    element: <HomeContextPage />,
  }, 
  {
    path: '/items',
    element: <ItemsPage />,
  },
  {
    path: '/beauty',
    element: <SaleBeauty />,
  },
  {
    path: '/services',
    element: <TestAllBeauty />,
  },
  {
    path: '/estilo',
    element: <NavbarComponent />,
  },
  {
    path: '/sales-reports',
    element: <Table1 />,
  },
  {
    path: '/inventory-control',
    element: <Table2 />,
  },
  {
    path: '/palavras',
    element: <Palavras  />,
  }/*,
  {
    path: '/contact',
    element: <ContactPage />,
  },*/
  // ...outras rotas
];

export default routes;
