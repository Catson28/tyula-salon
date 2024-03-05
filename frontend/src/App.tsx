// src/App.tsx
import React from 'react';
import AppRouter from './services/routes';

const App: React.FC = () => {
  return (
    <div>
      {/* Outros componentes globais, cabeçalho, rodapé, etc. */}
      <AppRouter />
    </div>
  );
};

export default App;
