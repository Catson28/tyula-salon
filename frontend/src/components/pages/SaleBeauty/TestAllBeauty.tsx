import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

import WholeCategory from '../../partials/category/WholeCategory';
import WholeSubcategory from '../../partials/subcategory/WholeSubcategory';
import WholeProduct from '../../partials/product/WholeProduct';
import WholeService from '../../partials/service/WholeService';
import ComponentSlider from '../../partials/carrocel/ComponentSlider';
import TelaDoNavegador from '../../partials/HelperResposnve/TelaDoNavegador';
import ParentWithDynamicChild from '../../partials/HelperResposnve/ParentWithDynamicChild';
import NavbarComponent from './NavbarComponent'
const TestAllBeauty: React.FC = () => {

  const components = [<WholeCategory />, <WholeSubcategory />, <WholeProduct />, <WholeService />];
  return (
      <NavbarComponent>
        <div className="container">            
            <ComponentSlider components={components} />
            <WholeCategory />
            <WholeSubcategory />
            <WholeProduct />
            <WholeService />
            <ParentWithDynamicChild />
            <TelaDoNavegador />
        </div>        
      </NavbarComponent>

  );
};

export default TestAllBeauty;
