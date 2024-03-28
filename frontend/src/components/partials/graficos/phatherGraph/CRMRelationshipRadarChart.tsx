import React from 'react';
import { Radar } from 'react-chartjs-2';

const CRMRelationshipRadarChart: React.FC = () => {
  const data = {
    // dados do gráfico de radar para relacionamento com clientes
  };

  const options = {
    // opções do gráfico de radar
  };

  return (
    <div>
      <h1>Gráfico de Radar - Satisfação dos Clientes em Diferentes Aspectos</h1>
      <Radar data={data} options={options} />
    </div>
  );
};

export default CRMRelationshipRadarChart;
