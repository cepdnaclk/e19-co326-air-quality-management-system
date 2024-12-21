const axios = require('axios');

const BASE_URL = 'http://localhost:8080/api/2/policies';

// Create a Policy
exports.createPolicy = async (id, payload) => {
  const url = `${BASE_URL}/${id}`;
  return axios.put(url, payload);
};

// Get a Policy by ID
exports.getPolicy = async (id) => {
  const url = `${BASE_URL}/${id}`;
  return axios.get(url);
};
