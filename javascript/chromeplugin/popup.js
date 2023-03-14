
$(document).ready(function() {
    // 在这里编写你的代码
    var btn = document.getElementById('btn');
    alert(btn);
    btn.addEventListener('click', function() {
        chrome.tabs.executeScript(null, {file: ["jquery-3.6.0.min.js","content.js"]});
    });
  });
