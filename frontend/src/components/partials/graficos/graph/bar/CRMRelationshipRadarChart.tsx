import React from 'react';
import { Radar } from 'react-chartjs-2';

const CRMRelationshipRadarChart: React.FC = () => {
  const data = {
    labels: ['Atendimento', 'Suporte', 'Qualidade do Produto'],
    datasets: [
      {
        label: 'Cliente A',
        data: [8, 9, 7],
        backgroundColor: 'rgba(255, 206, 86, 0.6)',
        borderColor: 'rgba(255, 206, 86, 1)',
        borderWidth: 1,
        pointRadius: 4,
      },
      {
        label: 'Cliente B',
        data: [9, 8, 9],
        backgroundColor: 'rgba(255, 99, 132, 0.6)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1,
        pointRadius: 4,
      },
    ],
  };

  const options = {
    scales: {
      r: {
        beginAtZero: true,
        max: 10,
      },
    },
  };

  return (
    <div>
      <h1>Gráfico de Radar - Satisfação dos Clientes em Diferentes Aspectos</h1>
      <Radar data={data} options={options} />
    </div>
  );
};

export default CRMRelationshipRadarChart;
