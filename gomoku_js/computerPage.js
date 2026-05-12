import {
  getState,
  setMove,
  switchTurn,
  setGameOver,
  resetGame,
  checkWin,
  getCandidates,
  countLine
} from "./general.js";

document.addEventListener("DOMContentLoaded", init);

let thinking = false;

/* 
   INIT
 */

function init() {
  createBoard();
  bindUI();
  bindBack();
  updateTurnUI();
}

/* 
   BOARD
 */

function createBoard() {
  const board = document.getElementById("board");
  board.innerHTML = "";

  for (let i = 0; i < 225; i++) {
    const cell = document.createElement("div");
    cell.classList.add("cell");

    cell.addEventListener("click", () => onPlayerMove(i, cell));
    board.appendChild(cell);
  }
}

/* 
   PLAYER MOVE
 */

function onPlayerMove(i, cell) {
  const state = getState();
  if (state.gameOver || thinking || cell.innerText) return;

  setMove(i, 1);
  cell.innerText = "⚫";
  playMoveSound?.();

  if (checkWin(i, 1)) return handleWin(1);
  if (isBoardFull()) return handleDraw();

  switchTurn();
  updateTurnUI();

  thinking = true;

  setTimeout(() => {
    const ai = aiMove();

    setMove(ai, 2);
    document.querySelectorAll(".cell")[ai].innerText = "⚪";

    playMoveSound?.();

    if (checkWin(ai, 2)) return handleWin(2);
    if (isBoardFull()) return handleDraw();

    switchTurn();
    thinking = false;
    updateTurnUI();
  }, 80);
}

/* 
   AI CORE 
 */

function aiMove() {
  const board = getState().boardState;
  const candidates = getCandidates().filter(i => board[i] === null);
  if (!candidates.length) return null;

  let best = -1;
  let bestScore = -Infinity;

  for (let i of candidates) {

    if (isWin(i, 2)) return i;
    if (isWin(i, 1)) return i;

    let score = 0;

    const attack = evaluate(i, 2);
    const defense = evaluate(i, 1);

    score += attack * 1.8;   
    score += defense * 1.2;  

    if (isDoubleThreat(i, 2)) score += 200000;
    if (isDoubleThreat(i, 1)) score += 180000;

    score += futureScore(i, 2) * 0.6;

    score += center(i);

    if (defense > 8000 && attack < 3000) {
      score *= 0.7;
    }

    if (score > bestScore) {
      bestScore = score;
      best = i;
    }
  }

  return best;
}

/*  KEY AI LOGIC */

function evaluate(i, player) {
  const r = Math.floor(i / 15);
  const c = i % 15;

  let score = 0;

  for (let [dr, dc] of [[1,0],[0,1],[1,1],[1,-1]]) {

    let left = countLine(r,c,-dr,-dc,player);
    let right = countLine(r,c,dr,dc,player);

    let total = 1 + left + right;

    let open = openEnds(r,c,dr,dc,left,right);

    if (total >= 5) score += 100000;
    else if (total === 4 && open === 2) score += 12000;
    else if (total === 4) score += 8000;
    else if (total === 3 && open === 2) score += 5000;
    else if (total === 3) score += 1200;
    else if (total === 2) score += 200;
  }

  return score;
}

function isDoubleThreat(i, player) {
  setMove(i, player);

  let threats = 0;
  const next = getCandidates();

  for (let n of next) {
    if (evaluate(n, player) >= 10000) threats++;
  }

  setMove(i, null);

  return threats >= 2;
}

function futureScore(i, player) {
  setMove(i, player);

  let score = 0;
  const next = getCandidates();

  for (let n of next) {
    score += evaluate(n, player);
  }

  setMove(i, null);

  return score;
}

/* WIN CHECK */

function isWin(i, player) {
  setMove(i, player);
  const win = checkWin(i, player);
  setMove(i, null);
  return win;
}

/* HELPERS */

function center(i) {
  const r = Math.floor(i / 15);
  const c = i % 15;
  return 10 - (Math.abs(r - 7) + Math.abs(c - 7));
}

function openEnds(r,c,dr,dc,left,right) {
  let open = 0;

  if (getCell(r + dr*(right+1), c + dc*(right+1)) === null) open++;
  if (getCell(r - dr*(left+1), c - dc*(left+1)) === null) open++;

  return open;
}

function getCell(r,c) {
  if (r < 0 || c < 0 || r >= 15 || c >= 15) return null;
  return getState().boardState[r*15+c];
}

function handleWin(player) {
  setGameOver(true);
  thinking = false;

  highlightWin(player);
  playWinSound?.();

  setTimeout(() => {
    alert(player === 1 ? "You Win!" : "Computer Win!");
  }, 100);
}

function handleDraw() {
  setGameOver(true);
  thinking = false;
  alert("Draw!");
}

/* HIGHLIGHT */

function highlightWin(player) {
  const cells = document.querySelectorAll(".cell");
  const board = getState().boardState;

  const dirs = [[1,0],[0,1],[1,1],[1,-1]];

  for (let i = 0; i < 225; i++) {
    if (board[i] !== player) continue;

    const r = Math.floor(i / 15);
    const c = i % 15;

    for (let [dr, dc] of dirs) {
      let line = [{r,c}];

      let rr = r + dr;
      let cc = c + dc;

      while (
        rr >= 0 && cc >= 0 &&
        rr < 15 && cc < 15 &&
        board[rr*15+cc] === player
      ) {
        line.push({r:rr,c:cc});
        rr += dr;
        cc += dc;
      }

      if (line.length >= 5) {
        line.forEach(p =>
          cells[p.r*15+p.c].classList.add("win")
        );
        return;
      }
    }
  }
}

/* UTIL*/

function isBoardFull() {
  return getState().boardState.every(c => c !== null);
}

/* UI*/

function bindUI() {
  document.getElementById("restart-btn").onclick = () => {
    resetGame();
    createBoard();
    thinking = false;
    updateTurnUI();
  };
}

function bindBack() {
  const btn = document.getElementById("back-btn");
  if (!btn) return;

  btn.onclick = (e) => {
    e.preventDefault();
    playClick?.();

    setTimeout(() => {
      window.location.href = "index.html";
    }, 120);
  };
}

function updateTurnUI() {
  const s = getState();

  document.getElementById("turn").innerText =
    s.gameOver
      ? "Game Over"
      : s.currentPlayer === 1
        ? "Your Turn"
        : "Computer Thinking...";
}