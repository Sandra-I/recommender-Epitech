import axios from "axios"

const URL_API = "http://127.0.0.1:8000";

function getAllCustomers(search) {
    return new Promise((resolve, reject) => {
        const url = `${URL_API}/all_customers/${search}`;
        axios.get(url)
            .then((response) => {
                let data = {};
                if (response.status === 200 && response.data) {
                    data = response.data.data;
                    resolve(data);
                }
                reject(data);
            })
            .catch((error) => {
                if (error.response && error.response.status === 404) {
                    reject({status: 404, message: "Customers not found !"});
                }
                reject(error);
            })
    });
}

function getCustomerDetails(customer_id) {
    return new Promise((resolve, reject) => {
        const url = `${URL_API}/customers_details/${customer_id}`;
        axios.get(url)
            .then((response) => {
                let data = {};
                if (response.status === 200 && response.data) {
                    data = JSON.parse(response.data.data)[0];
                    resolve(data);
                }
                reject(data);
            })
            .catch((error) => {
                if (error.response && error.response.status === 404) {
                    reject({status: 404, message: "Customer not found !"});
                }
                reject(error);
            })
    });
}

function getRecommendations(customer_id) {
    return new Promise((resolve, reject) => {
        const url = `${URL_API}/all/${customer_id}`;
        axios.get(url)
            .then((response) => {
                let data = {};
                if (response.status === 200 && response.data) {
                    data = response.data.data;
                    resolve(data);
                }
                reject(data);
            })
            .catch((error) => {
                if (error.response && error.response.status === 404) {
                    reject({status: 404, message: "Customer not found !"});
                }
                reject(error);
            })
    });
}

function getLastOrder(customer_id) {
    return new Promise((resolve, reject) => {
        const url = `${URL_API}/last_order/${customer_id}`;
        axios.get(url)
            .then((response) => {
                let data = {};
                if (response.status === 200 && response.data) {
                    data = Object.values(JSON.parse(response.data.data));
                    resolve(data);
                }
                reject(data);
            })
            .catch((error) => {
                if (error.response && error.response.status === 404) {
                    reject({status: 404, message: "Customer not found !"});
                }
                reject(error);
            })
    });
}

export { getCustomerDetails, getRecommendations, getLastOrder, getAllCustomers }