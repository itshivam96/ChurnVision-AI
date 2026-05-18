async function predictChurn() {
  const resultBox = document.getElementById("result");

  // collect inputs
  const data = {
    tenure_months: Number(document.getElementById("tenure").value),
    monthly_charges: Number(document.getElementById("charges").value),
    support_tickets: Number(document.getElementById("tickets").value),
    last_login_days: Number(document.getElementById("login").value)
  };

  // basic validation
  if (
    isNaN(data.tenure_months) ||
    isNaN(data.monthly_charges) ||
    isNaN(data.support_tickets) ||
    isNaN(data.last_login_days)
  ) {
    resultBox.innerHTML = "⚠️ Please enter valid numbers";
    return;
  }

  resultBox.innerHTML = "🧠 running inference...";

  try {
    const res = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    if (!res.ok) {
      throw new Error("Server error: " + res.status);
    }

    const result = await res.json();

    const prob = result.churn_probability;
    const risk = result.risk;

    resultBox.innerHTML = `
      <div>Churn Probability: <span style="color:var(--accent2)">
      ${prob}</span></div>
      <div>Risk: <span style="color:var(--accent)">
      ${risk}</span></div>
    `;

  } catch (err) {
    console.error(err);
    resultBox.innerHTML = "❌ Backend not reachable";
  }
}