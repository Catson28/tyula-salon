import React from 'react';
import styled from 'styled-components';

const TwoColumnLayoutContainer = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
`;

interface TwoColumnLayoutProps {
  children: React.ReactNode;
}

const TwoColumnLayout: React.FC<TwoColumnLayoutProps> = ({ children }) => {
  return (
    <TwoColumnLayoutContainer>
      {React.Children.map(children, (child, index) => (
        <div key={index}>{child}</div>
      ))}
    </TwoColumnLayoutContainer>
  );
};

export default TwoColumnLayout;
