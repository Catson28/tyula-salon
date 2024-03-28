import React from 'react';
import { Radar } from 'react-chartjs-2';

const SalesRadarChart: React.FC = () => {
  const data = {
    // dados do gráfico de radar para vendas
  };

  const options = {
    // opções do gráfico de radar
  };

  return (
    <div>
      <h1>Gráfico de Radar - Competências de Vendas por Vendedor</h1>
      <Radar data={data} options={options} />
    </div>
  );
};

export default SalesRadarChart;
