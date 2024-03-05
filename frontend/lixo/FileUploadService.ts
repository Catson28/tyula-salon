import http from "../http-common";

const upload = (file: File, onUploadProgress: any): Promise<any> => {
  let formData = new FormData();
  formData.append("file", file);

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
