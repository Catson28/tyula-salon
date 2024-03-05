import http from "../http-common";

const upload = (file: File, Path: string, contentType: string, objectId: number, onUploadProgress: any): Promise<any> => {
  let formData = new FormData();
  formData.append("file", file);
  formData.append("Path", Path);
  formData.append("content_type", contentType);
  formData.append("object_id", objectId.toString());

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
