import React from 'react';
import Graphs from './phatherGraph/Graphs';
import SalesComparisonGraph from './phatherGraph/SalesComparisonGraph';
import CostComparisonGraph from './phatherGraph/CostComparisonGraph';
import TwoColumnLayout from './TwoColumnLayout';
import SalesRadarChart from './phatherGraph/SalesRadarChart';
import ProjectManagementRadarChart from './phatherGraph/ProjectManagementRadarChart';
import CRMRelationshipRadarChart from './phatherGraph/CRMRelationshipRadarChart';
import FinancialPieChart from './phatherGraph/FinancialPieChart';


const AllGraphs: React.FC = () => {
  return (
    <TwoColumnLayout>
        <div>
            <Graphs />
            <SalesComparisonGraph
            data={[200, 300, 400, 500, 600]} // Exemplo de dados de vendas para diferentes produtos
            labels={['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E']} // Exemplo de rótulos para produtos
        />
        </div>
            <CostComparisonGraph />
    </TwoColumnLayout>
  );
};

export default AllGraphs;
