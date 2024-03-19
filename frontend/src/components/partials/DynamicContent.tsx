import React from 'react';
import styled from 'styled-components';

interface ContentProps {
  sidebarWidth: string;
}

const ContentContainer = styled.div<ContentProps>`
  margin-left: ${({ sidebarWidth }) => sidebarWidth};
  transition: margin-left 0.5s;
`;

const Content = styled.div`
  padding: 20px;
  background-color: #fff;
`;

const DynamicContent = ({ sidebarWidth, children }: React.PropsWithChildren<ContentProps>) => {
  return (
    <ContentContainer sidebarWidth={sidebarWidth}>
      <Content>
        {children} {/* Renderizando o conteúdo dinâmico aqui */}
      </Content>
    </ContentContainer>
  );
};

export default DynamicContent;
