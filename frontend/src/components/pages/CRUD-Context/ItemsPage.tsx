import React from 'react';
import Body from '../../partials/Body';
import { CrudProvider } from '../../../services/context/CrudContext'; // Ajuste a importação aqui
import ItemList from '../../partials/CRUD-Context/ItemList';
import Layout from '../../partials/CRUD-Context/Layout';

const ItemsPage: React.FC = () => {
  return (
    <CrudProvider>
      <div> {/* Use uma tag que aceite children */}
        <Layout>
          <Body>
            <ItemList />
          </Body>
        </Layout>
      </div>
    </CrudProvider>
  );
};

export default ItemsPage;