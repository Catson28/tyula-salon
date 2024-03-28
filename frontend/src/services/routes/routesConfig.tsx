// src/routes/routesConfig.tsx
import { RouteProps } from 'react-router-dom';
import React from 'react';
import ItemsPage from '../../components/pages/CRUD-Context/ItemsPage';
import HomeContextPage from '../../components/pages/HomeContextPage';
import LumeIt from '../../components/pages/LumeIt';
// import HomeSale from '../../components/pages/sale/HomeSale';
import HomePage from '../../components/pages/AllRoutes/HomePage';
import SaleBeauty from '../../components/pages/SaleBeauty';
// import AllBeauty from '../../../lixo/AllBeauty';
import TestAllBeauty from '../../components/pages/Services/AllService';
import Palavras from '../../components/pages/Palavras/Palavras';
import NavbarComponent from '../../components/partials/NavbarCompone';
import Table1 from '../../components/pages/Table/Table1';
import TableService from '../../components/pages/Table/TableService';
import TableServiceProvider from '../../components/pages/Table/TableServiceProvider';
import TableServiceSoldItems from '../../components/pages/Table/TableServiceSoldItems';
// import TableService from '../../components/pages/Table/TableService';
import AllGraphs from '../../components/partials/graficos/AllGraphs';
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
    element: <TableService />,
  },
  {
    path: '/products',
    element: <TableServiceSoldItems />,
  },
  {
    path: '/graficos',
    element: <AllGraphs />,
  },
  {
    path: '/employees',
    element: <TableServiceProvider />,
  }/*
  {
    path: '/sales',
    element:       <HomeSale
    clients={clientsData}
    services={servicesData}
    sellers={sellersData}
    onConfirm={confirmSale}
    onCancel={cancelSale}
  />,
  }*/,
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
