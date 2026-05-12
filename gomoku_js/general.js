let currentPlayer = 1;
let boardState = Array(225).fill(null);
let winningCells = [];
let gameOver = false;

export let AI_MODE = "hard";


export function getState() {
  return {
    currentPlayer,
    boardState,
    winningCells,
    gameOver,
    AI_MODE
  };
}


export function setMove(index, player) {
  if (index < 0 || index >= 225) return false;
  boardState[index] = player;
  return true;
}

export function switchTurn() {
  currentPlayer = currentPlayer === 1 ? 2 : 1;
}

export function setGameOver(v) {
  gameOver = v;
}

export function resetGame() {
  currentPlayer = 1;
  boardState = Array(225).fill(null);
  winningCells = [];
  gameOver = false;
}

export function checkWin(index, player) {
  const r = Math.floor(index / 15);
  const c = index % 15;

  const dirs = [[1,0],[0,1],[1,1],[1,-1]];

  for (let [dr, dc] of dirs) {
    let count = 1;

    count += countLine(r,c,dr,dc,player);
    count += countLine(r,c,-dr,-dc,player);

    if (count >= 5) return true;
  }

  return false;
}

export function countLine(r,c,dr,dc,player) {
  let count = 0;

  r += dr;
  c += dc;

  while (
    r >= 0 && r < 15 &&
    c >= 0 && c < 15 &&
    boardState[r * 15 + c] === player
  ) {
    count++;
    r += dr;
    c += dc;
  }

  return count;
}

export function getCandidates() {
  let set = new Set();

  for (let i = 0; i < 225; i++) {
    if (boardState[i] !== null) {
      let r = Math.floor(i / 15);
      let c = i % 15;

      for (let dr = -2; dr <= 2; dr++) {
        for (let dc = -2; dc <= 2; dc++) {
          let nr = r + dr;
          let nc = c + dc;

          if (nr >= 0 && nc >= 0 && nr < 15 && nc < 15) {
            set.add(nr * 15 + nc);
          }
        }
      }
    }
  }

  return set.size ? [...set] : [112];
}

