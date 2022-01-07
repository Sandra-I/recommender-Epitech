import axios from "axios"

const URL_API = "http://127.0.0.1:8000";

function getTopBy(category) {
    return new Promise((resolve, reject) => {
        const url = `${URL_API}/get_top_categories/${category}/3`;
        axios.get(url)
            .then((response) => {
                let data = {};
                if (response.status === 200 && response.data) {
                    data = JSON.parse(response.data.data);
                    resolve(data);
                }
                reject(data);
            })
            .catch((error) => {
                if (error.response && error.response.status === 404) {
                    reject({status: 404, message: "Data not found !"});
                }
                reject(error);
            })
    });
}

function getCustomerEvolution() {
    return new Promise((resolve, reject) => {
        const url = `${URL_API}/customer_evolution`;
        axios.get(url)
            .then((response) => {
                let data = {};
                if (response.status === 200 && response.data) {
                    data = JSON.parse(response.data.data);
                    resolve(data);
                }
                reject(data);
            })
            .catch((error) => {
                if (error.response && error.response.status === 404) {
                    reject({status: 404, message: "Data not found !"});
                }
                reject(error);
            })
    });
}

function getCAEvolution() {
    return new Promise((resolve, reject) => {
        const url = `${URL_API}/ca_evolution`;
        axios.get(url)
            .then((response) => {
                let data = {};
                if (response.status === 200 && response.data) {
                    data = JSON.parse(response.data.data);
                    resolve(data);
                }
                reject(data);
            })
            .catch((error) => {
                if (error.response && error.response.status === 404) {
                    reject({status: 404, message: "Data not found !"});
                }
                reject(error);
            })
    });
}

export { getTopBy, getCustomerEvolution, getCAEvolution }