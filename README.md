  <h1>Global Relief Actions (GRA) </h1> <h2>World Funder (WF) </h2> <h4> Humanitarian Action (HA)</h4>
<p>About Humanitarian Action. </p>
<p> Donation page: button- below the page.</p>
<p><ol>
  <li>Solve puzzle, fill in details, then click 'Donate'.</li>
  <li>Scroll up then click the first "<i>Donate Now</i>" <mark>(VERY IMPORTANT)</mark>.</li>
<li>Wait, then click '<i>Stabalize System</i>'.</li>
<li>Play the minigame.</li>
<li>Reach the end by clicking on the ball(s).</li>
<li>Choose your tasks to do and start working.</li>
<li>You can add tasks or abort them. </li>
<li>Check your calendar and start the timer.</li>
<li>Read the <i> Motivational </i> quotes.</li>
</ol>
</p>
<p>Enjoy!</p>

the blob game:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chaotic Blob Challenge</title>
    <style>
        * { margin: 0; padding: 0; overflow: hidden; }
        body { background: black; position: relative; height: 100vh; width: 100vw; color: white; font-family: Arial, sans-serif; text-align: center; }
        .blob, .goal {
            position: absolute;
            width: 50px;
            height: 50px;
            border-radius: 50%;
        }
        .blob {
            background: radial-gradient(circle, cyan, blue);
            box-shadow: 0 0 20px cyan;
        }
        .goal {
            background: radial-gradient(circle, yellow, orange);
            box-shadow: 0 0 20px yellow;
        }
        #score {
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 24px;
        }
    </style>
</head>
<body>
    <div id="score">Score: 0</div>
    <div class="blob"></div>
    <div class="goal"></div>
    <script>
        const blob = document.querySelector('.blob');
        const goal = document.querySelector('.goal');
        const scoreDisplay = document.getElementById('score');
        let vx = (Math.random() - 0.5) * 10;
        let vy = (Math.random() - 0.5) * 10;
        let spin = 0;
        let score = 0;

        blob.style.left = `${window.innerWidth / 2}px`;
        blob.style.top = `${window.innerHeight / 2}px`;

        function moveBlob() {
            let x = parseFloat(blob.style.left || window.innerWidth / 2);
            let y = parseFloat(blob.style.top || window.innerHeight / 2);
            
            x += vx;
            y += vy;
            
            if (x <= 0 || x >= window.innerWidth - 50) vx *= -1;
            if (y <= 0 || y >= window.innerHeight - 50) vy *= -1;
            
            spin += 10;
            blob.style.left = `${x}px`;
            blob.style.top = `${y}px`;
            blob.style.transform = `rotate(${spin}deg)`;
            blob.style.background = `radial-gradient(circle, hsl(${Math.random() * 360}, 100%, 70%), blue)`;
            blob.style.boxShadow = `0 0 20px hsl(${Math.random() * 360}, 100%, 70%)`;
            
            checkCollision();
            requestAnimationFrame(moveBlob);
        }

        function moveGoal() {
            goal.style.left = `${Math.random() * (window.innerWidth - 50)}px`;
            goal.style.top = `${Math.random() * (window.innerHeight - 50)}px`;
        }

        function checkCollision() {
            let blobRect = blob.getBoundingClientRect();
            let goalRect = goal.getBoundingClientRect();
            if (
                blobRect.left < goalRect.right &&
                blobRect.right > goalRect.left &&
                blobRect.top < goalRect.bottom &&
                blobRect.bottom > goalRect.top
            ) {
                score++;
                scoreDisplay.textContent = `Score: ${score}`;
                moveGoal();
            }
        }

        document.body.addEventListener('click', (e) => {
            blob.style.left = `${e.clientX - 25}px`;
            blob.style.top = `${e.clientY - 25}px`;
            vx = (Math.random() - 0.5) * 10;
            vy = (Math.random() - 0.5) * 10;
            blob.style.width = `${Math.random() * 100 + 20}px`;
            blob.style.height = blob.style.width;
        });
        
        moveGoal();
        moveBlob();
    </script>
</body>
</html>
