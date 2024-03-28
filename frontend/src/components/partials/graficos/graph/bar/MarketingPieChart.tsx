import React from 'react';
import { Pie } from 'react-chartjs-2';

const MarketingPieChart: React.FC = () => {
  const data = {
    labels: ['Produto A', 'Produto B', 'Produto C'],
    datasets: [
      {
        label: 'Participação de Mercado',
        data: [50, 30, 20],
        backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(153, 102, 255, 0.6)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
        ],
        borderWidth: 1,
      },
    ],
  };

  const options = {
    plugins: {
      legend: {
        position: 'bottom',
      },
    },
  };

  return (
    <div>
      <h1>Gráfico de Pizza - Participação de Mercado</h1>
      <Pie data={data} options={options} />
    </div>
  );
};

export default MarketingPieChart;
