<!DOCTYPE html>
<html>
<head>
    <title>Box Dodger</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background-color: #222;
        }
        canvas {
            display: block;
            background: #333;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas"></canvas>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        canvas.width = 400;
        canvas.height = 500;

        let player = { x: 175, y: 450, width: 50, height: 50, speed: 5 };
        let obstacles = [];
        let gameOver = false;

        document.addEventListener("keydown", (e) => {
            if (e.key === "ArrowLeft" && player.x > 0) player.x -= player.speed;
            if (e.key === "ArrowRight" && player.x < canvas.width - player.width) player.x += player.speed;
        });

        function createObstacle() {
            let size = Math.random() * 50 + 20;
            let x = Math.random() * (canvas.width - size);
            obstacles.push({ x: x, y: 0, width: size, height: size, speed: 3 });
        }

        function update() {
            if (gameOver) return;

            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "cyan";
            ctx.fillRect(player.x, player.y, player.width, player.height);
            
            ctx.fillStyle = "red";
            obstacles.forEach((obstacle, index) => {
                obstacle.y += obstacle.speed;
                ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);

                if (obstacle.y > canvas.height) obstacles.splice(index, 1);
                if (
                    player.x < obstacle.x + obstacle.width &&
                    player.x + player.width > obstacle.x &&
                    player.y < obstacle.y + obstacle.height &&
                    player.y + player.height > obstacle.y
                ) {
                    gameOver = true;
                    alert("Game Over! Refresh to play again.");
                }
            });

            requestAnimationFrame(update);
        }

        setInterval(createObstacle, 1000);
        update();
    </script>
</body>
</html>
