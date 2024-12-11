(function() {
  let countdown = 5; // Starting countdown value in seconds
  const targetUrl = "https://example.com"; // Replace with your target URL
  
  const countdownElement = document.getElementById('countdown');
  const timeElement = document.getElementById('time');
  
  const interval = setInterval(() => {
    countdown -= 1;
    countdownElement.textContent = countdown;
    timeElement.textContent = countdown;
  
    if (countdown <= 0) {
      clearInterval(interval);
      window.location.href = targetUrl; // Redirect to target URL
    }
  }, 1000);
})();
