async function sendInvocation() {
  const invocation = document.getElementById('invocation').value.trim();
  const status = document.getElementById('status');
  const historyList = document.getElementById('history-list');

  if (!invocation) {
    status.textContent = 'Please enter an invocation';
    return;
  }

  status.textContent = 'Sending...';

  try {
    const res = await fetch('/api/invoke', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ invocation, password: 'AddieMaeLeSane33' })
    });
    const data = await res.json();
    status.textContent = data.message || 'Ritual launched';

    const li = document.createElement('li');
    li.textContent = invocation;
    historyList.prepend(li);
  } catch (err) {
    status.textContent = 'Error: ' + err.message;
  }
}

document.querySelector('button').addEventListener('click', sendInvocation);
