$(document).ready(function () {
  let pageLocUrl = window.location.href;
  let caseIndex;
  if (pageLocUrl.indexOf("Dashboard") > -1) {
    caseIndex = "dashboard";
  } else if (pageLocUrl.indexOf("Home") > -1) {
    caseIndex = "home";
  } else if (pageLocUrl.indexOf("Reporting") > -1) {
    caseIndex = "reporting";
  }

  switch (caseIndex) {
    case "home":
      initiateHome();
      break;
    case "dashboard":
      initiateDashboard();
    case "reporting":
      initiateReporting();
      break;
    default:
      break;
  }

  $("#loginBtn").on("click", function () {
    window.location.href = "pages/Dashboard.html";
  });
});
