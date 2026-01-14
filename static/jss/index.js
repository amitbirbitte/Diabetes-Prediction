const totalSteps = 8;
let currentStep = 1;

// Step images (diabetes related)
const images = {
  1: "/static/images/pregnency.png", // Pregnancies
  2: "/static/images/glucose.png", // Glucose
  3: "/static/images/bp.avif", // Blood Pressure
  4: "/static/images/skin.jpg", // Skin Thickness
  5: "/static/images/insulin.png", // Insulin
  6: "/static/images/bmi.jpg", // BMI
  7: "/static/images/dpf.png", // DPF
  8: "/static/images/age.png"  // Age
};

function showStep(step) {
  if (step < 1) step = 1;
  if (step > totalSteps) step = totalSteps;

  document.querySelectorAll(".fade-section").forEach((section, idx) => {
    section.classList.toggle("active", idx === step - 1);
  });

  // Button state
  document.getElementById("prevBtn").disabled = step === 1;
  document.getElementById("nextBtn").textContent =
    step === totalSteps ? "Predict Result" : "Next";

  // Image transition
  const img = document.getElementById("stepImage");
  img.classList.add("fade-out");

  setTimeout(() => {
    img.src = images[step];
    img.classList.remove("fade-out");
  }, 250);
}

function changeStep(n) {
  // If final step → submit form
  if (currentStep === totalSteps && n === 1) {
    document.getElementById("predictionForm").submit();
    return;
  }

  currentStep += n;
  showStep(currentStep);
}

// Initialize
document.addEventListener("DOMContentLoaded", () => {
  showStep(currentStep);
});
