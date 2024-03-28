import React from 'react';
import { Pie } from 'react-chartjs-2';

const FinancialPieChart: React.FC = () => {
  const data = {
    // dados do gráfico de pizza para financeiro e contabilidade
  };

  const options = {
    // opções do gráfico de pizza
  };

  return (
    <div>
      <h1>Gráfico de Pizza - Distribuição de Despesas</h1>
      <Pie data={data} options={options} />
    </div>
  );
};

export default FinancialPieChart;
