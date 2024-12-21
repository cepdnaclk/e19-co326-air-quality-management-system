const express = require('express');
const { createThing, getThing } = require('./thing-service');
const { createPolicy, getPolicy } = require('./policy-service');

const app = express();
app.use(express.json());

// Thing Endpoints
app.post('/thing/:id', async (req, res) => {
  try {
    const response = await createThing(req.params.id, req.body);
    res.status(201).send(response.data);
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});

app.get('/thing/:id', async (req, res) => {
  try {
    const response = await getThing(req.params.id);
    res.status(200).send(response.data);
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});

// Policy Endpoints
app.post('/policy/:id', async (req, res) => {
  try {
    const response = await createPolicy(req.params.id, req.body);
    res.status(201).send(response.data);
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});

app.get('/policy/:id', async (req, res) => {
  try {
    const response = await getPolicy(req.params.id);
    res.status(200).send(response.data);
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Ditto Extended API is running on port ${PORT}`);
});