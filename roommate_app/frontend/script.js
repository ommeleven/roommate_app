fetch('https://your-api-url/rooms')
  .then(response => response.json())
  .then(data => {
    // Process the data and update your frontend
    console.log(data); // You may want to update the UI with this data
  })
  .catch(error => {
    console.error('Error:', error);
  });
