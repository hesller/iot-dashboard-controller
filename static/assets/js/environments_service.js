
class EnvironmentDataService {
  getAll() {
    return axios_api.get("environments/");
  }

  get(id) {
    return axios_crm.get(`/ambientes/editar/${id}`);
  }

  // create(data) {
  //   return axios_http.post("/tutorials", data);
  // }
  //
  // update(id, data) {
  //   return axios_http.put(`/tutorials/${id}`, data);
  // }
  //
  // delete(id) {
  //   return axios_http.delete(`/tutorials/${id}`);
  // }
  //
  // deleteAll() {
  //   return axios_http.delete(`/tutorials`);
  // }
  //
  // findByTitle(title) {
  //   return axios_http.get(`/tutorials?title=${title}`);
  // }
}