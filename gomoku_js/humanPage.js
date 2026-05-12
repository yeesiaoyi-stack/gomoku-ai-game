import {
  getState,
  setMove,
  switchTurn,
  setGameOver,
  resetGame,
  checkWin
} from "./general.js";

document.addEventListener("DOMContentLoaded", init);

//  BACK 
document.getElementById("back-btn").addEventListener("click", () => {
  playClick();

  setTimeout(() => {
    window.location.href = "index.html";
  }, 120); 
});

//  INIT 
function init() {
  createBoard();
  bindRestart();
  updateUI();
}



//  BOARD 
function createBoard() {
  const board = document.getElementById("board");
  board.innerHTML = "";

  for (let i = 0; i < 225; i++) {
    const cell = document.createElement("div");
    cell.classList.add("cell");

    cell.addEventListener("click", () => handleMove(i, cell));
    board.appendChild(cell);
  }
}

//  MOVE 
function handleMove(i, cell) {
  const state = getState();

  if (state.gameOver || cell.innerText) return;

  const player = state.currentPlayer;

  setMove(i, player);
  cell.innerText = player === 1 ? "⚫" : "⚪";

  playMoveSound(); 

  // WIN
  const win = getWinCells(i, player);
  if (win) {
    highlightWin(win);
    playWinSound();
    endGame(`Player ${player} wins!`);
    return;
  }

  // DRAW
  if (isBoardFull()) {
    endGame("Draw!");
    return;
  }

  switchTurn();
  updateUI();
}

//  WIN DETECTION 
function getWinCells(index, player) {
  const r = Math.floor(index / 15);
  const c = index % 15;

  const dirs = [[1,0],[0,1],[1,1],[1,-1]];

  for (let [dr, dc] of dirs) {
    let line = [{r, c}];

    let i = 1;
    while (getCell(r + dr*i, c + dc*i) === player) {
      line.push({ r: r + dr*i, c: c + dc*i });
      i++;
    }

    i = 1;
    while (getCell(r - dr*i, c - dc*i) === player) {
      line.unshift({ r: r - dr*i, c: c - dc*i });
      i++;
    }

    if (line.length >= 5) return line;
  }

  return null;
}

//  HIGHLIGHT 
function highlightWin(win) {
  const cells = document.querySelectorAll(".cell");

  win.forEach(p => {
    const index = p.r * 15 + p.c;
    if (cells[index]) {
      cells[index].classList.add("win");
    }
  });
}

//  GAME END 
function endGame(msg) {
  setGameOver(true);
  setTimeout(() => alert(msg), 100);
}

//  UTIL 
function getCell(r, c) {
  if (r < 0 || c < 0 || r >= 15 || c >= 15) return null;
  return getState().boardState[r * 15 + c];
}

function isBoardFull() {
  return getState().boardState.every(c => c !== null);
}

//  UI 
function updateUI() {
  const state = getState();

  document.getElementById("turn").innerText =
    state.gameOver
      ? "Game Over"
      : state.currentPlayer === 1
        ? "Player 1 Turn"
        : "Player 2 Turn";
}

//  RESET 
function bindRestart() {
  document.getElementById("restart-btn").addEventListener("click", () => {
    playClick();

    resetGame();

    document.querySelectorAll(".cell").forEach(cell => {
      cell.innerText = "";
      cell.classList.remove("win");
    });

    updateUI();
  });
}

//  BACK 
window.goBack = () => {
  window.location.href = "index.html";
};

//  SOUND HOOKS 
function playMoveSound() {
  const s = document.getElementById("moveSound");
  if (!s) return;
  s.currentTime = 0;
  s.play().catch(() => {});
}

function playWinSound() {
  const s = document.getElementById("winSound");
  if (!s) return;
  s.currentTime = 0;
  s.play().catch(() => {});
}

function playClick() {
  const s = document.getElementById("clickSound");
  if (!s) return;
  s.currentTime = 0;
  s.play().catch(() => {});
}