import http from "../http-common";

const upload = (file: File, title: string, description: string, onUploadProgress: any): Promise<any> => {
  let formData = new FormData();
  formData.append("file", file);
  formData.append("title", title); // Adicionando o título à FormData
  formData.append("description", description); // Adicionando a descrição à FormData

  return http.post("/api/images/add/", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
    onUploadProgress,
  });
};

const getFiles = () : Promise<any> => {
  return http.get("/api/images/list-by-type/");
};

const FileUploadService = {
  upload,
  getFiles,
};

export default FileUploadService;
