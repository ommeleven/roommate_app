const roomAvailability = {
    'room-1': {
        '9:00 AM': 'Available',
        '10:00 AM': 'Occupied',
        '11:00 AM': 'Available',
        // Add availability status for other time slots
    },
    'room-2': {
        '9:00 AM': 'Available',
        '10:00 AM': 'Available',
        '11:00 AM': 'Occupied',
        // Add availability status for other time slots
    },
    'room-3': {
        '9:00 AM': 'Occupied',
        '10:00 AM': 'Available',
        '11:00 AM': 'Available',
        // Add availability status for other time slots
    },
    // Add availability status for other rooms and time slots
};

// Function to update availability status based on room and time selection
function updateAvailabilityStatus() {
    const selectedRoom = document.getElementById('room-select').value;
    const selectedTime = document.getElementById('reservation-time').value;

    const availabilityStatus = roomAvailability[selectedRoom] ? roomAvailability[selectedRoom][selectedTime] || 'Unknown' : 'Unknown';
    document.getElementById('availability-status').textContent = `Status: ${availabilityStatus}`;
}

// Add event listeners to update availability status when the room or time is selected
document.getElementById('room-select').addEventListener('change', updateAvailabilityStatus);
document.getElementById('reservation-time').addEventListener('change', updateAvailabilityStatus);

// JavaScript code for handling form submissions
document.getElementById('room-selection-form').addEventListener('submit', function (e) {
    e.preventDefault();
    // Handle room selection form submission
    const selectedRoom = document.getElementById('room-select').value;
    // Implement your logic to process the selected room
});

// JavaScript code for handling form submissions
document.getElementById('reservation-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const selectedDate = document.getElementById('reservation-date').value;
    const selectedTime = document.getElementById('reservation-time').value;

    // Get the current date and time
    const currentDate = new Date();
    const selectedDateTime = new Date(selectedDate + ' ' + selectedTime);

    if (selectedDateTime < currentDate) {
        // Reservation date is in the past, show an error message
        const resultElement = document.getElementById('reservation-result');
        resultElement.textContent = 'Error: Please select a future date and time for your reservation.';
    } else {
        // Reservation date is in the future, proceed with the reservation logic
        const resultElement = document.getElementById('reservation-result');
        resultElement.textContent = `Reservation confirmed for ${selectedDate} at ${selectedTime}`;
        // Implement your logic to make a reservation
        // This is where you would send the reservation data to your server, etc.
    }
});


// Initial update of availability status
updateAvailabilityStatus();
