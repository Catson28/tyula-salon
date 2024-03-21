import { useState } from 'react';
import ServiceDataService from "../net/ServiceDataService";
import IServiceData from "./../types/service.type";

export const useServiceState = () => {
  const [currentService, setCurrentService] = useState<IServiceData | null>(null);
  const [showServiceForm, setShowServiceForm] = useState<boolean>(false);
  const [showService, setShowService] = useState<boolean>(false);
  const [showImgService, setShowImgService] = useState<boolean>(false);
  const [showServicesList, setShowServicesList] = useState<boolean>(false);
  const [deletedServiceId, setDeletedServiceId] = useState<string | null>(null);

  const handleServiceClose = () => {
    setShowServiceForm(false);
    setShowServicesList(false);
    setShowService(false);
  };

  const handleServicesListClick = () => {
    if (showServicesList) {
      handleServiceClose();
    } else {
      handleServiceClose();
      setShowServicesList(true);
    }
  };

  const handleAddServiceClick = () => {
    if (showServiceForm) {
      handleServiceClose();
    } else {
      handleServiceClose();
      setShowServiceForm(true);
    }
  };

  const handleEditService = (service: IServiceData) => {
    if (service) {
      setCurrentService(service);
      handleServiceClose();
      setShowService(true);
    }
  };

  const handleImageService = (service: IServiceData) => {
    if (service) {
      setCurrentService(service);
      handleServiceClose();
      setShowImgService(true);
    }
  };

  const handleDeleteService = (serviceId: string) => {
    ServiceDataService.delete(serviceId)
      .then((response: any) => {
        handleServiceClose();
        setDeletedServiceId(serviceId);
        setCurrentService(null);
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };

  const handleUpdateService = (updatedService: IServiceData) => {
    ServiceDataService.update(updatedService, updatedService.id)
      .then((response: any) => {
        // setCurrentService(currentService);
        handleServiceClose();
      })
      .catch((e: Error) => {
        console.log(e);
      });
  };

  return {
    currentService,
    showServiceForm,
    showService,
    showServicesList,
    deletedServiceId,
    setShowServiceForm,
    setShowService,
    setShowServicesList,
    setShowImgService,
    handleServicesListClick,
    handleAddServiceClick,
    handleEditService,
    handleImageService,
    handleDeleteService,
    handleUpdateService
  };
};
