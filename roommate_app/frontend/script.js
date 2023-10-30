fetch('https://your-api-url/rooms')
  .then(response => response.json())
  .then(data => {
    console.log(data); 
  })
  .catch(error => {
    console.error('Error:', error);
  });
