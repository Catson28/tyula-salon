import React from 'react';
import Body from '../partials/Body';
import { CrudProvider } from '../../services/context/CrudContext'; // Ajuste a importação aqui
import CrudForm from '../partials/CrudForm';
import CrudList from '../partials/CrudList';
import Layout from '../partials/CRUD-Context/Layout';

const SeuComponente: React.FC = () => {
  return (
    <CrudProvider>
      <div> {/* Use uma tag que aceite children */}
        <Layout>
          <Body>
            <CrudForm />
            <CrudList />
          </Body>
        </Layout>
      </div>
    </CrudProvider>
  );
};

export default SeuComponente;