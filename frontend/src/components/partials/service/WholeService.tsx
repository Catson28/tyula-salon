import React, { useEffect } from 'react';

import AddService from './add-service.component';
import ServicesList from './services-list.component'; // Importando o componente de listagem de serviços
import Service from './service.component'; // Importando o componente de exibição de serviço
import { useServiceState } from '../../../services/utils/serviceUtils'; // Importando o hook de estado para serviços

const WholeService: React.FC = () => {
  const {
    currentService,
    showServiceForm,
    showService,
    showServicesList,
    deletedServiceId,

    setShowServiceForm, // Adicionando as funções de configuração ao objeto de retorno
    setShowService,
    setShowServicesList,
    handleServicesListClick,
    handleAddServiceClick,
    handleEditService,
    handleImageService,
    handleDeleteService,
    handleUpdateService
  } = useServiceState();

  useEffect(() => {
    if (!currentService && deletedServiceId) {
      setShowService(false);
      setShowServicesList(false);
    }
  }, [currentService, deletedServiceId]);

  const servicesButtonViewText = showService || showServicesList ? "Fechar" : "Abrir";
  const servicesButtonAddText = showServiceForm ? "Fechar" : "Adicionar";

  return (
      <>
        <div className="btn-toolbar justify-content-between p-2" role="toolbar" aria-label="Toolbar with button groups">
          <h2 id="vertical-variation">Lista de Servicos<a className="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="#" href="#vertical-variation"></a></h2>
          <button type="button" className="btn btn-primary" onClick={handleServicesListClick}>{servicesButtonViewText}</button>
          <button type="button" className="btn btn-primary" onClick={handleAddServiceClick}>{servicesButtonAddText}</button>
        </div>
        {showServiceForm && (
          <AddService onClose={() => setShowServiceForm(false)} />
        )}
        {showServicesList && (
          <ServicesList onClose={() => setShowServicesList(false)} onEditService={handleEditService} onImgService={handleImageService} />
        )}
        {showService && currentService && (
          <Service id={currentService.id} onEdit={handleUpdateService} onDelete={handleDeleteService} />
        )}
      </>
  );
};

export default WholeService;
