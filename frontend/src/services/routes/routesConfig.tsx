// src/routes/routesConfig.tsx
import { RouteProps } from 'react-router-dom';
import React from 'react';
import ItemsPage from '../../components/pages/CRUD-Context/ItemsPage';
import HomeContextPage from '../../components/pages/HomeContextPage';
import LumeIt from '../../components/pages/LumeIt';
import HomePage from '../../components/pages/AllRoutes/HomePage';
import SaleBeauty from '../../components/pages/SaleBeauty';
import AllBeauty from '../../components/pages/SaleBeauty/AllBeauty';
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
    path: '/AllBeauty',
    element: <AllBeauty />,
  }/*,
  {
    path: '/contact',
    element: <ContactPage />,
  },*/
  // ...outras rotas
];

export default routes;
