exports.handleAxiosError = (error) => {
    if (error.response) {
      console.error(`Error: ${error.response.status} - ${error.response.data}`);
    } else if (error.request) {
      console.error('No response received from the server.');
    } else {
      console.error(`Request Error: ${error.message}`);
    }
  };
  