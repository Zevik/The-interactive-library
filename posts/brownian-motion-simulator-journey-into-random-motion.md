---
title: "מסע אל הלב של התנועה האקראית: סימולטור תנועה בראונית"
english_slug: brownian-motion-simulator-journey-into-random-motion
category: "מדעים מדויקים / פיזיקה"
tags:
  - פיזיקה
  - סימולציה
  - הדמיה
  - תנועה-בראונית
  - חלקיקים
  - אקראיות
  - מיקרוסקופ
---
# מסע אל הלב של התנועה האקראית: סימולטור תנועה בראונית

צאו למסע וירטואלי אל העולם המיקרוסקופי והתבוננו בפלא הפיזיקלי של תנועה בראונית! גלו כיצד חלקיק גלוי לעין "קופץ" ונע ללא הרף במסלול אקראי לחלוטין, רק בגלל ההתנגשויות הבלתי-פוסקות עם צבא בלתי-נראה של חלקיקים קטנים וזריזים. חוו בעצמכם כיצד רעש מיקרוסקופי יוצר ריקוד כאוטי ברמה המקרוסקופית, והבינו את אחת הראיות החזקות ביותר לקיומן של מולקולות ואטומים.

<div class="simulation-container">
    <canvas id="brownianCanvas"></canvas>
     <div class="controls-and-stats">
        <div class="controls">
            <div class="control-group">
                <label for="smallParticlesCount">מספר חלקיקים זריזים:</label>
                <input type="range" id="smallParticlesCount" min="50" max="800" value="300" step="10">
                <span id="smallParticlesValue">300</span>
            </div>

            <div class="control-group">
                <label for="particleSpeed">מהירות החלקיקים הזריזים:</label>
                <input type="range" id="particleSpeed" min="0.5" max="7" value="3" step="0.2">
                <span id="particleSpeedValue">3</span>
            </div>
        </div>
        <div class="stats">
             <p>התנגשויות בחלקיק הגדול (לשנייה): <span id="collisionRate">0</span></p>
             <p>כוח כולל מורגש (משוער): <span id="totalForce">0.00</span></p>
        </div>
         <button id="startResetButton" class="action-button">התחל את הריקוד הכאוטי!</button>
    </div>
</div>

<button id="toggleExplanation" class="explanation-button">מה קורה כאן בעצם? (הסבר)</button>

<div id="explanation" class="explanation-text">
    <h2>מהי התנועה הבלתי-צפויה הזו? תנועה בראונית!</h2>
    <p>דמיינו אבק צף בקרן שמש, או גרגר אבקה מרחף במים. האם שמתם לב פעם לתנועה הקופצנית והחסרת הכיוון שלהם? זוהי בדיוק **תנועה בראונית** בפעולה!</p>
    <p>החלקיק הגדול שאתם רואים בסימולטור (האדום!) אינו נע מעצמו. הוא נדחף לכל עבר על ידי אינספור התנגשויות עם חלקיקים קטנים בהרבה ובלתי-נראים לעין (במקרה האמיתי - מולקולות או אטומים), הנמצאים בתנועה תרמית תמידית וחסרת מנוח.</p>
    <p>למרות שהתנגשות בודדת כמעט ואינה משפיעה על החלקיק הגדול בשל מסתו העצומה יחסית, סך כל הדחיפות הרגעיות מכל הכיוונים אינו מתאזן אף פעם באופן מושלם. ברגע מסוים, יהיו יותר התנגשויות מצד אחד, מה שיגרום לחלקיק הגדול "לקפוץ" בכיוון הזה. רגע לאחר מכן, יחסי הכוחות ישתנו, והוא יזנק לכיוון אחר לחלוטין. התוצאה היא מסלול מפותל, אקראי ובלתי-פוסק - הריקוד הבראוני.</p>
    <p>הבוטניקאי רוברט בראון היה הראשון שתיעד את התופעה ב-1827, כשהתבונן באבקת פרחים במים. למעלה מ-70 שנה אחר כך, אלברט איינשטיין הסביר אותה כתופעת לוואי של התנועה התרמית של מולקולות המים. התנועה הבראונית הפכה לאחת הראיות המכריעות לקיומם של אטומים ומולקולות!</p>
    <h3>התנסו בסימולטור:</h3>
    <ul>
        <li>**הגדילו את מספר החלקיקים הזריזים:** ראו כיצד יותר התנגשויות מגבירות את הכאוס ומאיצות את תנועת החלקיק הגדול.</li>
        <li>**הגדילו את מהירות החלקיקים הזריזים:** מהירות גבוהה יותר פירושה אנרגיה קינטית רבה יותר, התנגשויות חזקות יותר, ושוב - תנועה ערה ומהירה יותר של החלקיק הגדול.</li>
    </ul>
    <p>התנועה הבראונית היא דוגמה אלגנטית ומרתקת כיצד אינטראקציות מיקרוסקופיות אקראיות יכולות להוביל לתופעות מקרוסקופיות הנראות לעין, ומדגימה את הקשר העמוק בין חום לתנועה ברמה המולקולרית.</p>
</div>

<style>
    /* הגדרות גלובליות משופרות */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* פונט מודרני יותר */
        direction: rtl;
        text-align: right;
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* רקע עם גרדיאנט עדין */
        color: #333;
        padding: 20px;
        line-height: 1.6;
    }

    h1, h2 {
        color: #00796b; /* צבע טורקיז כהה יותר */
        text-align: center; /* ממורכז */
        margin-bottom: 15px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }

    p {
        margin-bottom: 10px;
    }

    /* עיצוב קונטיינר הסימולציה */
    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 20px auto; /* ממורכז */
        padding: 25px;
        background-color: #ffffff; /* רקע לבן לקונטיינר */
        border-radius: 12px; /* פינות מעוגלות יותר */
        box-shadow: 0 8px 16px rgba(0,0,0,0.2); /* צל עמוק יותר */
        max-width: 700px; /* רוחב מקסימלי */
        width: 95%; /* רוחב רספונסיבי */
    }

    /* עיצוב קנבס */
    canvas {
        border: 2px solid #00bcd4; /* גבול בצבע טורקיז בהיר */
        background-color: #e0f2f7; /* רקע תכלכל בהיר לקנבס */
        display: block;
        margin-bottom: 20px;
        border-radius: 8px; /* פינות מעוגלות */
        box-shadow: inset 0 0 8px rgba(0,0,0,0.1); /* צל פנימי עדין */
        width: 100%; /* התאמה לרוחב הקונטיינר */
        height: auto; /* שמירה על יחס גובה-רוחב */
        aspect-ratio: 600 / 400; /* יחס גובה-רוחב מקורי */
    }

    /* קונטיינר לבקרות ולסטטיסטיקות */
    .controls-and-stats {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
    }

    /* קונטיינר לבקרות */
    .controls {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 10px;
        align-items: stretch; /* מותח את הפקדים */
    }

    .control-group {
         display: flex;
         align-items: center;
         justify-content: space-between; /* מרווח בין אלמנטים */
         width: 100%;
         gap: 10px; /* רווח בין האלמנטים בקבוצה */
     }

     .control-group label {
         font-weight: bold;
         color: #00796b;
         flex-shrink: 0; /* מונע מהתווית להתכווץ */
     }

    /* עיצוב סליידרים */
    input[type="range"] {
        flex-grow: 1; /* מותח את הסליידר למקסימום רוחב */
        -webkit-appearance: none; /* הסתרת עיצוב ברירת מחדל */
        appearance: none;
        height: 8px;
        background: #b2ebf2; /* צבע מסלול הסליידר */
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 5px;
    }

    input[type="range"]:hover {
        opacity: 1;
    }

    input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #00796b; /* צבע גרירה */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #00796b;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .control-group span {
        width: 40px; /* רוחב קבוע להצגת הערך */
        text-align: center;
        font-weight: bold;
        color: #004d40; /* צבע כהה יותר לערך */
    }

    /* סטטיסטיקות */
    .stats {
        width: 100%;
        background-color: #e0f2f7;
        border: 1px solid #b2ebf2;
        border-radius: 8px;
        padding: 10px 15px;
        text-align: center;
        margin-top: 10px;
        font-size: 0.9em;
        color: #004d40;
        display: flex;
        justify-content: space-around; /* מרווח בין הסטטיסטיקות */
    }

    .stats p {
        margin: 0;
        font-weight: bold;
    }
     .stats span {
         font-weight: normal; /* כדי שהערך עצמו לא יהיה מודגש מדי */
         color: #00796b;
     }


    /* עיצוב כפתורים כללי */
    button {
        padding: 12px 25px;
        border: none;
        border-radius: 8px; /* פינות מעוגלות */
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    button:hover {
        transform: translateY(-2px); /* אפקט הרמה במעבר עכבר */
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }

    button:active {
        transform: translateY(0); /* אפקט לחיצה */
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }


    /* עיצוב כפתור התחל/אתחל */
    #startResetButton {
        background-color: #4caf50; /* ירוק */
        color: white;
        align-self: center; /* ממורכז */
        margin-top: 10px;
    }

    #startResetButton:hover {
        background-color: #388e3c; /* ירוק כהה יותר */
    }

    /* עיצוב כפתור הסבר */
    .explanation-button {
        display: block;
        margin: 30px auto 20px auto; /* ממורכז, רווח מעל ומתחת */
        background-color: #03a9f4; /* כחול בהיר */
        color: white;
    }

    .explanation-button:hover {
        background-color: #0288d1; /* כחול כהה יותר */
    }

    /* עיצוב תיבת הסבר */
    .explanation-text {
        margin: 20px auto; /* ממורכז */
        padding: 20px;
        background-color: #e1f5fe; /* רקע תכלכל בהיר מאוד */
        border: 1px solid #b3e5fc; /* גבול תכלכל */
        border-radius: 8px;
        max-width: 700px; /* רוחב מקסימלי */
        width: 95%;
        opacity: 0; /* נסתר בהתחלה */
        height: 0; /* גובה 0 בהתחלה */
        overflow: hidden; /* הסתרת תוכן חורג */
        transition: opacity 0.6s ease-in-out, height 0.6s ease-in-out, padding 0.6s ease-in-out; /* אנימציית הופעה */
    }

    .explanation-text.visible {
        opacity: 1; /* הופעה */
        height: auto; /* גובה אוטומטי לתוכן */
        padding: 20px; /* החזרת ריפוד */
    }

     .explanation-text h2 {
         margin-top: 0;
     }
</style>

<script>
    const canvas = document.getElementById('brownianCanvas');
    const ctx = canvas.getContext('2d');
    const startResetButton = document.getElementById('startResetButton');
    const smallParticlesCountInput = document.getElementById('smallParticlesCount');
    const smallParticlesValueSpan = document.getElementById('smallParticlesValue');
    const particleSpeedInput = document.getElementById('particleSpeed');
    const particleSpeedValueSpan = document.getElementById('particleSpeedValue');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');
    const collisionRateSpan = document.getElementById('collisionRate');
    const totalForceSpan = document.getElementById('totalForce');


    // Use aspect ratio for responsive size based on container
    const aspectRatio = 600 / 400;
    const container = canvas.parentElement;
    let canvasWidth = container.clientWidth; // Start with container width
    let canvasHeight = canvasWidth / aspectRatio;

    // Clamp canvas size to reasonable limits if needed
    canvasWidth = Math.min(canvasWidth, 700); // Max width
    canvasHeight = canvasWidth / aspectRatio;


    canvas.width = 600; // Maintain internal resolution for drawing
    canvas.height = 400;

    const bigParticleRadius = 20;
    let smallParticles = [];
    let bigParticle = {};
    let animationFrameId = null;
    let isRunning = false;

    // Collision tracking
    let collisionCount = 0;
    let lastCollisionUpdateTime = 0;
    let collisionRate = 0;
    let accumulatedForceMagnitude = 0; // To visualize total 'push'


    // Basic Particle Class
    class Particle {
        constructor(x, y, radius, color) {
            this.x = x;
            this.y = y;
            this.radius = radius;
            this.color = color;
            this.vx = 0;
            this.vy = 0;
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
             ctx.shadowBlur = this.radius / 2; // Subtle glow
             ctx.shadowColor = this.color;
            ctx.fill();
            ctx.closePath();
             ctx.shadowBlur = 0; // Reset shadow
        }

        update(deltaTime) {
             // Position update based on velocity
            this.x += this.vx * deltaTime;
            this.y += this.vy * deltaTime;

            // Simple bounce off walls
            if (this.x - this.radius < 0) {
                this.x = this.radius;
                this.vx = -this.vx;
            } else if (this.x + this.radius > canvas.width) {
                 this.x = canvas.width - this.radius;
                 this.vx = -this.vx;
             }

            if (this.y - this.radius < 0) {
                this.y = this.radius;
                this.vy = -this.vy;
            } else if (this.y + this.radius > canvas.height) {
                 this.y = canvas.height - this.radius;
                 this.vy = -this.vy;
             }
        }
    }

     // Small Particle Class (inherits from Particle)
     class SmallParticle extends Particle {
         constructor(x, y, radius, color, speed, direction) {
             super(x, y, radius, color);
             this.speed = speed;
             this.direction = direction; // in radians
             this.vx = Math.cos(direction) * speed;
             this.vy = Math.sin(direction) * speed;
             this.randomness = 0.1; // How much direction can change per update
         }

         update(deltaTime) {
             // Add slight randomness to direction
             this.direction += (Math.random() - 0.5) * this.randomness;
             // Limit direction change to prevent extreme flips
             if (this.direction > Math.PI * 2) this.direction -= Math.PI * 2;
             if (this.direction < 0) this.direction += Math.PI * 2;

             this.vx = Math.cos(this.direction) * this.speed;
             this.vy = Math.sin(this.direction) * this.speed;

             super.update(deltaTime); // Handle movement and wall bounces

             // Re-align direction after bounce
             if (this.x - this.radius < 0 || this.x + this.radius > canvas.width) {
                  this.direction = Math.atan2(this.vy, this.vx); // Update direction based on new velocity
             }
             if (this.y - this.radius < 0 || this.y + this.radius > canvas.height) {
                  this.direction = Math.atan2(this.vy, this.vx); // Update direction based on new velocity
             }
         }

          // Collision response with another particle (simplified elastic collision)
          collide(otherParticle) {
              const dx = otherParticle.x - this.x;
              const dy = otherParticle.y - this.y;
              const distance = Math.sqrt(dx * dx + dy * dy);

              if (distance < this.radius + otherParticle.radius) {
                  // Collision detected
                  const angle = Math.atan2(dy, dx);
                  const overlap = (this.radius + otherParticle.radius) - distance;

                  // Move particles apart to prevent sticking (half each)
                  this.x -= (overlap / 2) * Math.cos(angle);
                  this.y -= (overlap / 2) * Math.sin(angle);
                  otherParticle.x += (overlap / 2) * Math.cos(angle);
                  otherParticle.y += (overlap / 2) * Math.sin(angle);

                   // Simple velocity swap along the collision axis (approximation)
                   const thisSpeed = Math.sqrt(this.vx*this.vx + this.vy*this.vy);
                   const otherSpeed = Math.sqrt(otherParticle.vx*otherParticle.vx + otherParticle.vy*otherParticle.vy);

                   const finalThisVX = otherSpeed * Math.cos(angle + Math.PI); // Bounce back along angle
                   const finalThisVY = otherSpeed * Math.sin(angle + Math.PI);

                   const finalOtherVX = thisSpeed * Math.cos(angle); // Push other particle along angle
                   const finalOtherVY = thisSpeed * Math.sin(angle);

                   this.vx = finalThisVX;
                   this.vy = finalThisVY;

                   otherParticle.vx = finalOtherVX;
                   otherParticle.vy = finalOtherVY;

                   // Add some randomness after collision? (Optional)
                   // this.direction = Math.atan2(this.vy, this.vx) + (Math.random() - 0.5) * 0.2;
                   // otherParticle.direction = Math.atan2(otherParticle.vy, otherParticle.vy) + (Math.random() - 0.5) * 0.2;
              }
          }
     }

     // Big Particle Class (inherits from Particle)
     class BigParticle extends Particle {
          constructor(x, y, radius, color) {
              super(x, y, radius, color);
              this.collisionPulse = 0; // For visual feedback
              this.damping = 0.98; // Velocity damping
              this.maxSpeed = 15; // Limit speed

              this.collisionForceX = 0; // Accumulate force from collisions
              this.collisionForceY = 0;
          }

          update(deltaTime) {
               // Apply accumulated force as acceleration
              this.vx += this.collisionForceX * deltaTime;
              this.vy += this.collisionForceY * deltaTime;

              // Reset accumulated force
              this.collisionForceX = 0;
              this.collisionForceY = 0;


              // Apply damping
              this.vx *= this.damping;
              this.vy *= this.damping;

              // Limit speed
              const speed = Math.sqrt(this.vx * this.vx + this.vy * this.vy);
              if (speed > this.maxSpeed) {
                  const scale = this.maxSpeed / speed;
                  this.vx *= scale;
                  this.vy *= scale;
              }

              super.update(deltaTime); // Handle movement and wall bounces

              // Decay collision pulse
              this.collisionPulse = Math.max(0, this.collisionPulse - 0.05 * deltaTime);
          }

          draw() {
              ctx.beginPath();
              ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
              const colorIntensity = Math.min(1, this.collisionPulse + 0.2); // Base intensity + pulse
              const pulsedColor = `rgba(255, ${Math.max(0, 255 - colorIntensity * 150)}, ${Math.max(0, 255 - colorIntensity * 150)}, 1)`; // Redder when pulsed
              ctx.fillStyle = pulsedColor;

               ctx.shadowBlur = this.radius * 1.5 * colorIntensity; // Glow effect based on pulse
               ctx.shadowColor = 'rgba(255, 100, 100, 0.8)';

              ctx.fill();
              ctx.closePath();
              ctx.shadowBlur = 0; // Reset shadow
          }

          applyImpulse(impulseX, impulseY) {
              this.collisionForceX += impulseX;
              this.collisionForceY += impulseY;
              this.collisionPulse = 1; // Trigger visual pulse
          }
     }


    function initSimulation() {
        bigParticle = new BigParticle(canvas.width / 2, canvas.height / 2, bigParticleRadius, 'red');
        smallParticles = [];
        const numSmallParticles = parseInt(smallParticlesCountInput.value);
        const smallParticleRadius = 2;
        const smallParticleSpeed = parseFloat(particleSpeedInput.value);

        // Attempt to place particles without initial overlap
        const maxAttempts = numSmallParticles * 10;
        let attempts = 0;

        while(smallParticles.length < numSmallParticles && attempts < maxAttempts) {
            attempts++;
            const x = Math.random() * canvas.width;
            const y = Math.random() * canvas.height;
            const direction = Math.random() * Math.PI * 2;

            let overlapping = false;
            // Check overlap with big particle
            const distToBig = Math.sqrt((x - bigParticle.x)**2 + (y - bigParticle.y)**2);
            if (distToBig < bigParticle.radius + smallParticleRadius * 2) { // Use 2*radius for initial spacing
                overlapping = true;
            } else {
                // Check overlap with existing small particles
                for(let j = 0; j < smallParticles.length; j++) {
                    const dist = Math.sqrt((x - smallParticles[j].x)**2 + (y - smallParticles[j].y)**2);
                    if (dist < smallParticleRadius * 2) { // Use 2*radius for initial spacing
                        overlapping = true;
                        break;
                    }
                }
            }

            if (!overlapping) {
                 smallParticles.push(new SmallParticle(x, y, smallParticleRadius, 'rgba(0, 188, 212, 0.7)', smallParticleSpeed, direction)); // Semi-transparent blue/cyan
            }
        }
         // If after attempts we don't have enough particles, log warning
         if (smallParticles.length < numSmallParticles) {
             console.warn(`Could only place ${smallParticles.length} out of ${numSmallParticles} small particles without initial overlap.`);
         }

        collisionCount = 0;
        lastCollisionUpdateTime = performance.now();
        collisionRate = 0;
        accumulatedForceMagnitude = 0;

        updateStatsDisplay();
        draw(); // Draw initial state
    }

    let lastTime = 0;
    function gameLoop(currentTime) {
        if (!isRunning) return;

        const deltaTime = (currentTime - lastTime) / 16.66; // Delta time normalized to 60fps (1000/60 ≈ 16.66)
        lastTime = currentTime;

        updateSimulation(deltaTime);
        draw();
        animationFrameId = requestAnimationFrame(gameLoop);
    }

     function updateSimulation(deltaTime) {
         // Update small particles
         smallParticles.forEach(particle => {
             particle.update(deltaTime);
         });

         // Handle collisions between small particles and the big particle
         let currentFrameCollisions = 0;
         let currentFrameForceMagnitude = 0;

         smallParticles.forEach(smallP => {
             const dx = bigParticle.x - smallP.x;
             const dy = bigParticle.y - smallP.y;
             const distance = Math.sqrt(dx * dx + dy * dy);

             if (distance < bigParticle.radius + smallP.radius) {
                 // Collision detected
                 currentFrameCollisions++;

                 const angle = Math.atan2(dy, dx); // Angle from small to big
                 const totalRadius = bigParticle.radius + smallP.radius;
                 const overlap = totalRadius - distance;

                 // Move particles apart to resolve overlap *before* calculating impulse
                 // Move small particle back along the collision axis
                 smallP.x -= (overlap) * Math.cos(angle + Math.PI);
                 smallP.y -= (overlap) * Math.sin(angle + Math.PI);

                 // Calculate relative velocity along the collision axis
                 const vCollisionX = smallP.vx - bigParticle.vx;
                 const vCollisionY = smallP.vy - bigParticle.vy;
                 const speedAlongCollisionAxis = vCollisionX * Math.cos(angle) + vCollisionY * Math.sin(angle);

                 // Only process if particles are moving towards each other along the axis
                 if (speedAlongCollisionAxis > 0) {
                      // Simple impulse transfer based on relative velocity and masses (approximation)
                      // Assume big particle mass is much larger, small particle bounces off, big particle gets a push
                      const smallMass = smallP.radius * smallP.radius; // Proxy for mass
                      const bigMass = bigParticle.radius * bigParticle.radius * 5; // Make big particle effectively heavier

                      // Simplified impulse magnitude (related to 2*mu*v_rel / (m1+m2))
                      // Given the big particle is much heavier, the small particle velocity reverses, big particle gets a small kick
                      const impulseMagnitude = (2 * smallMass * speedAlongCollisionAxis) / (smallMass + bigMass);

                       const impulseX = impulseMagnitude * Math.cos(angle);
                       const impulseY = impulseMagnitude * Math.sin(angle);

                       bigParticle.applyImpulse(impulseX * 10, impulseY * 10); // Apply impulse to big particle (amplified)
                       currentFrameForceMagnitude += Math.sqrt(impulseX*impulseX + impulseY*impulseY) * 10;


                       // Reverse small particle velocity component along collision axis
                       const sin = Math.sin(angle);
                       const cos = Math.cos(angle);
                       const v1 = { x: smallP.vx * cos + smallP.vy * sin, y: smallP.vy * cos - smallP.vx * sin };
                       v1.x *= -1; // Reverse velocity along collision axis

                       // Rotate velocity back
                       smallP.vx = v1.x * cos - v1.y * sin;
                       smallP.vy = v1.y * cos + v1.x * sin;

                        // Apply slight random change to small particle direction after collision
                        smallP.direction = Math.atan2(smallP.vy, smallP.vx) + (Math.random() - 0.5) * 0.5; // Add small random scatter
                   }
              }
         });

         collisionCount += currentFrameCollisions;
         accumulatedForceMagnitude = accumulatedForceMagnitude * 0.95 + currentFrameForceMagnitude * 0.05; // Smooth average

         // Update big particle
         bigParticle.update(deltaTime);

         // Update collision rate every second or so
         const now = performance.now();
         if (now - lastCollisionUpdateTime >= 1000) {
             collisionRate = collisionCount / ((now - lastCollisionUpdateTime) / 1000); // Collisions per second
             collisionCount = 0; // Reset counter
             lastCollisionUpdateTime = now;
             updateStatsDisplay();
         }

         updateStatsDisplay(); // Update force magnitude every frame

          // Optional: Collisions between small particles (computationally expensive)
          // If performance allows, uncomment or implement optimized collision detection
          // for (let i = 0; i < smallParticles.length; i++) {
          //    for (let j = i + 1; j < smallParticles.length; j++) {
          //        smallParticles[i].collide(smallParticles[j]);
          //    }
          // }
     }


    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear canvas

        // Draw small particles first
        smallParticles.forEach(particle => {
            particle.draw();
        });

         // Draw big particle on top
         bigParticle.draw();
    }

    function startSimulation() {
        if (!isRunning) {
            initSimulation();
            isRunning = true;
            lastTime = performance.now(); // Initialize lastTime for game loop
            gameLoop(lastTime); // Start the loop
            startResetButton.textContent = 'אתחל סימולציה';
            startResetButton.style.backgroundColor = '#f44336'; /* אדום ל"אתחל" */
            startResetButton.style.boxShadow = '0 4px 6px rgba(244,67,54,0.3)';
             smallParticlesCountInput.disabled = true;
             particleSpeedInput.disabled = true;
        }
    }

    function resetSimulation() {
        cancelAnimationFrame(animationFrameId);
        isRunning = false;
        initSimulation(); // Re-initialize particles and positions
        startResetButton.textContent = 'התחל את הריקוד הכאוטי!';
        startResetButton.style.backgroundColor = '#4caf50'; /* ירוק ל"התחל" */
         startResetButton.style.boxShadow = '0 4px 6px rgba(76,175,80,0.3)';
         smallParticlesCountInput.disabled = false;
         particleSpeedInput.disabled = false;
         ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear canvas on reset
         bigParticle.draw(); // Draw big particle at center
         smallParticles.forEach(p => p.draw()); // Draw small particles in initial positions
    }

    function updateStatsDisplay() {
         collisionRateSpan.textContent = collisionRate.toFixed(1);
         totalForceSpan.textContent = accumulatedForceMagnitude.toFixed(2);
    }


    // Event Listeners
    startResetButton.addEventListener('click', () => {
        if (isRunning) {
            resetSimulation();
        } else {
            startSimulation();
        }
    });

    smallParticlesCountInput.addEventListener('input', (event) => {
        smallParticlesValueSpan.textContent = event.target.value;
        // Always reset simulation when changing particle count
         resetSimulation(); // Show the new particle distribution on canvas immediately
    });

     particleSpeedInput.addEventListener('input', (event) => {
        particleSpeedValueSpan.textContent = event.target.value;
         // Always reset simulation when changing speed (to re-init small particles with new speed)
         // Alternative: update speeds of existing particles if running. Reset is simpler and clearer.
         resetSimulation(); // Show the new particle distribution with implicit new speed
    });


    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('visible');
        if (explanationDiv.classList.contains('visible')) {
            toggleExplanationButton.textContent = 'הסתר הסבר';
            // Set height dynamically for smooth transition
             explanationDiv.style.height = explanationDiv.scrollHeight + 'px';
        } else {
             toggleExplanationButton.textContent = 'מה קורה כאן בעצם? (הסבר)';
             explanationDiv.style.height = '0'; // Collapse
        }
    });

    // Adjust explanation height on window resize if it's visible
    window.addEventListener('resize', () => {
        if (explanationDiv.classList.contains('visible')) {
            explanationDiv.style.height = 'auto'; // Temporarily set to auto to measure
            explanationDiv.style.height = explanationDiv.scrollHeight + 'px'; // Set to measured height
        }
         // Potentially resize canvas based on container size
         // container.clientWidth = canvas.parentElement.clientWidth; // Get updated container width
         // canvasWidth = container.clientWidth;
         // canvasHeight = canvasWidth / aspectRatio;
         // canvas.style.width = canvasWidth + 'px';
         // canvas.style.height = canvasHeight + 'px';
         // Note: Changing canvas *style* width/height scales the drawing, does not change internal resolution.
         // Changing canvas *attributes* width/height resets the canvas content. Sticking to fixed resolution for simplicity.

    });


    // Initial setup
    initSimulation();
    resetSimulation(); // Start in reset state showing initial setup
</script>