const axios = require('axios');

const BASE_URL = 'http://localhost:8080/api/2/things';

// Create a Thing
exports.createThing = async (id, payload) => {
  const url = `${BASE_URL}/${id}`;
  return axios.put(url, payload);
};

// Get a Thing by ID
exports.getThing = async (id) => {
  const url = `${BASE_URL}/${id}`;
  return axios.get(url);
};
