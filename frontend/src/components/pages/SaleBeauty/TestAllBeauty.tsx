import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

import AboutCategory from '../../partials/category/AboutCategory';
import AboutSubcategory from '../../partials/subcategory/AboutSubcategory';
import AboutProduct from '../../partials/product/AboutProduct';
import ComponentSlider from '../../partials/carrocel/ComponentSlider';
import TelaDoNavegador from '../../partials/HelperResposnve/TelaDoNavegador';
import ParentWithDynamicChild from '../../partials/HelperResposnve/ParentWithDynamicChild';
const TestAllBeauty: React.FC = () => {

  const components = [<AboutCategory />, <AboutSubcategory />, <AboutProduct />];
  return (
    <div className="container-fluid">
      <div className="container">
          <AboutCategory />
          <AboutSubcategory />
          <AboutProduct />
          <ComponentSlider components={components} />
          <ParentWithDynamicChild />
          <TelaDoNavegador />
      </div>
    </div>
  );
};

export default TestAllBeauty;
