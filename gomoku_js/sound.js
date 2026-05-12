let bgm;
let clickSound;
let hoverSound;
let winSound;
let moveSound;

document.addEventListener("DOMContentLoaded", () => {

  bgm = document.getElementById("bgm");
  clickSound = document.getElementById("clickSound");
  hoverSound = document.getElementById("hoverSound");
  winSound = document.getElementById("winSound");
  moveSound = document.getElementById("moveSound");
  window:startBgm();
  bindGlobalSoundSystem();
});

function startBgm() {
  const bgm = document.getElementById("bgm");

  if (!bgm) return;

  bgm.volume = 0.1;

  const playPromise = bgm.play();

  if (playPromise !== undefined) {
    playPromise.catch(() => {
      console.log("BGM blocked by browser, waiting user interaction");
    });
  }
}

// GLOBAL BUTTON SOUND SYSTEM
function bindGlobalSoundSystem() {

  // hover sound (ALL buttons)
  document.addEventListener("mouseover", (e) => {
    const btn = e.target.closest("button");
    if (!btn || !hoverSound) return;

    hoverSound.currentTime = 0;
    hoverSound.play().catch(() => {});
  });

  // click sound (ALL buttons)
  document.addEventListener("click", (e) => {
    const btn = e.target.closest("button");
    if (!btn || !clickSound) return;
    playClick();


    clickSound.currentTime = 0;
    clickSound.play().catch(() => {});
  });
}



// EXPORT for game actions
window.playMoveSound = () => {
  if (!moveSound) return;
  moveSound.currentTime = 0;
  moveSound.play().catch(() => {});
};

window.playWinSound = () => {
  if (!winSound) return;
  winSound.currentTime = 0;
  winSound.play().catch(() => {});
};
window.playClick = () => {
  if (!clickSound) return;
  clickSound.currentTime = 0;
  clickSound.play().catch(() => {});
};