import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

import AboutCategory from './../../partials/category/AboutCategory';
import AboutSubcategory from './../../partials/subcategory/AboutSubcategory';

const TestAllBeauty: React.FC = () => {

  return (
    <div className="container-fluid">
      <div className="container">
          <AboutCategory />
          <AboutSubcategory />
      </div>
    </div>
  );
};

export default TestAllBeauty;
