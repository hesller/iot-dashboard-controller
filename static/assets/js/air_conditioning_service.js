const urlPrefix = 'air_conditioning/';

class AirConditioningDataService {
    getAll() {
        return axios_http.get(urlPrefix);
    }

    get(id) {
        return axios_http.get(`${urlPrefix}${id}`);
    }

    create(data) {
        return axios_http.post(urlPrefix, data);
    }

    update(id, data) {
        return axios_http.put(`${urlPrefix}${id}`, data);
    }

    delete(id) {
        return axios_http.delete(`${urlPrefix}${id}`);
    }

    deleteAll() {
        return axios_http.delete(`${urlPrefix}`);
    }

    findByTitle(title) {
        return axios_http.get(`${urlPrefix}?title=${title}`);
    }
}