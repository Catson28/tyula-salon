import React from 'react';
import { Radar } from 'react-chartjs-2';

const SalesRadarChart: React.FC = () => {
  const data = {
    labels: ['Prospecção', 'Fechamento de Negócios', 'Atendimento ao Cliente'],
    datasets: [
      {
        label: 'Vendedor A',
        data: [8, 7, 9],
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1,
        pointRadius: 4,
      },
      {
        label: 'Vendedor B',
        data: [9, 8, 7],
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
      <h1>Gráfico de Radar - Competências de Vendas por Vendedor</h1>
      <Radar data={data} options={options} />
    </div>
  );
};

export default SalesRadarChart;
