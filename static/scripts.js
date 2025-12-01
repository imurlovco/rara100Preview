document.addEventListener("DOMContentLoaded", () => {
    const imgs = document.querySelectorAll(".cell img");

    imgs.forEach(img => {
        // 마우스 호버
        img.addEventListener("pointerenter", () => img.classList.add("touch-active"));
        img.addEventListener("pointerleave", () => img.classList.remove("touch-active"));

        // 모바일 터치: touchstart -> 확대, touchend -> 원래대로
        img.addEventListener("touchstart", () => img.classList.add("touch-active"), { passive: true });
        img.addEventListener("touchend", () => img.classList.remove("touch-active"));
    });

    // 배경 클릭 시 모든 이미지 확대 해제
    document.addEventListener("click", (e) => {
        if (!e.target.closest(".cell")) {
            imgs.forEach(img => img.classList.remove("touch-active"));
        }
    });
});
