(function randomColors() {
    const elements = document.getElementsByTagName("*");
    for (let el of elements) {
        el.style.backgroundColor = `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`;
        el.style.color = `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`;
    }
    setTimeout(randomColors, 500); // 0.5秒ごとに再実行
})();
