document.addEventListener("DOMContentLoaded", function () {
    const intervalId = setInterval(function () {
        const cookie = document.cookie;
        if (cookie.includes("dev_tools")) {
            document.getElementById("status").innerHTML = "✅ opened";
            clearInterval(intervalId);
        }
    }, 200);
});
//# sourceMappingURL=main.js.map
