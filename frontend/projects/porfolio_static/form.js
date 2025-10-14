const form = document.getElementById('myForm');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const data = Object.fromEntries(formData);
  console.log('Form Data:', data);
  // send to backend
  const response = await fetch("/api/submit", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  if (response.ok) {
    alert(`Thank you, ${data.name}! Your message was saved.`);
    form.reset();
  } else {
    alert('Error saving your message.');
  }
});
