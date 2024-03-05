// var blockSize = 25;
// var total_row = 17; //total row number
// var total_col = 17; //total column number
// var board;
// var context;
 
// var snakeX = blockSize * 5;
// var snakeY = blockSize * 5;
 
// // Set the total number of rows and columns
// var speedX = 0;  //speed of snake in x coordinate.
// var speedY = 0;  //speed of snake in Y coordinate.
 
// var snakeBody = [];
 
// var foodX;
// var foodY;
 
// var gameOver = false;
 
// window.onload = function () {
//     // Set board height and width
//     board = document.getElementById("board");
//     board.height = total_row * blockSize;
//     board.width = total_col * blockSize;
//     context = board.getContext("2d");
 
//     placeFood();
//     document.addEventListener("keyup", changeDirection);  //for movements
//     // Set snake speed
//     setInterval(update, 1000 / 10);
// }
 
// function update() {
//     if (gameOver) {
//         return;
//     }
 
//     // Background of a Game
//     context.fillStyle = "#97c503";
//     context.fillRect(0, 0, board.width, board.height);
 
//     // Set food color and position
//     context.fillStyle = "red";
//     context.fillRect(foodX, foodY, blockSize, blockSize);
 
//     if (snakeX == foodX && snakeY == foodY) {
//         snakeBody.push([foodX, foodY]);
//         placeFood();
//     }
 
//     // body of snake will grow
//     for (let i = snakeBody.length - 1; i > 0; i--) {
//         // it will store previous part of snake to the current part
//         snakeBody[i] = snakeBody[i - 1];
//     }
//     if (snakeBody.length) {
//         snakeBody[0] = [snakeX, snakeY];
//     }
 
//     context.fillStyle = "#1d3b00";
//     snakeX += speedX * blockSize; //updating Snake position in X coordinate.
//     snakeY += speedY * blockSize;  //updating Snake position in Y coordinate.
//     context.fillRect(snakeX, snakeY, blockSize, blockSize);
//     for (let i = 0; i < snakeBody.length; i++) {
//         context.fillRect(snakeBody[i][0], snakeBody[i][1], blockSize, blockSize);
//     }
 
//     if (snakeX < 0
//         || snakeX > total_col * blockSize
//         || snakeY < 0
//         || snakeY > total_row * blockSize) {
         
//         // Out of bound condition
//         gameOver = true;
//         alert("Game Over");
//     }
 
//     for (let i = 0; i < snakeBody.length; i++) {
//         if (snakeX == snakeBody[i][0] && snakeY == snakeBody[i][1]) {
             
//             // Snake eats own body
//             gameOver = true;
//             alert("Game Over");
//         }
//     }
// }
 
// // Movement of the Snake - We are using addEventListener
// function changeDirection(e) {
//     if (e.code == "ArrowUp" && speedY != 1) {
//         // If up arrow key pressed with this condition...
//         // snake will not move in the opposite direction
//         speedX = 0;
//         speedY = -1;
//     }
//     else if (e.code == "ArrowDown" && speedY != -1) {
//         //If down arrow key pressed
//         speedX = 0;
//         speedY = 1;
//     }
//     else if (e.code == "ArrowLeft" && speedX != 1) {
//         //If left arrow key pressed
//         speedX = -1;
//         speedY = 0;
//     }
//     else if (e.code == "ArrowRight" && speedX != -1) {
//         //If Right arrow key pressed
//         speedX = 1;
//         speedY = 0;
//     }
// }
 
// // Randomly place food
// function placeFood() {
 
//     // in x coordinates.
//     foodX = Math.floor(Math.random() * total_col) * blockSize;
     
//     //in y coordinates.
//     foodY = Math.floor(Math.random() * total_row) * blockSize;
// }
let tileCount=20;
let tileSize=18;
let headX=10;
let headY=10;


const canvas=document.getElementById('board'); 
const ctx=canvas.getContext('2d');

//draw apple
let appleX=5;
let appleY=5;

function drawGame(){
    clearScreen();
    drawSnake();
}
function drawSnake(){
    ctx.fillStyle="orange";
    ctx.fillRect(headX* tileCount,headY* tileCount, tileSize,tileSize)

}
function clearScreen(){
	ctx.fillStyle= 'black'// make screen black
	ctx.fillRect(0,0,canvas.clientWidth,canvas.clientHeight)// black color start from 0px left, right to canvas width and canvas height
}
drawGame()
function drawGame(){
    let speed=7;//The interval will be seven times a second.

    setTimeout(drawGame, 1000/speed);//update screen 7 times a second
}
function drawApple(){
     ctx.fillStyle="red";// make apple red
     ctx.fillRect(appleX*tileCount, appleY*tileCount, tileSize, tileSize)//position apple within tile count
 }