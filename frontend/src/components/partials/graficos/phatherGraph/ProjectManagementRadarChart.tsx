import React from 'react';
import { Radar } from 'react-chartjs-2';

const ProjectManagementRadarChart: React.FC = () => {
  const data = {
    // dados do gráfico de radar para gestão de projetos
  };

  const options = {
    // opções do gráfico de radar
  };

  return (
    <div>
      <h1>Gráfico de Radar - Distribuição de Recursos em Projetos</h1>
      <Radar data={data} options={options} />
    </div>
  );
};

export default ProjectManagementRadarChart;
