---
title: "איך הרוח בונה אדמת לוס? מסע מדהים של גרגר אבק"
english_slug: how-wind-creates-loess-soil
category: "מדעי הסביבה / כדור הארץ"
tags:
  - לוס
  - קרקע
  - רוח
  - סחיפה
  - גאולוגיה
  - פוריות קרקע
---
<h1>איך הרוח בונה אדמת לוס? מסע מדהים של גרגר אבק</h1>
<p>איך ייתכן שכוח הרוח, שנתפס לרוב כמחריב ומכלה, הוא דווקא זה שיוצר את אחת הקרקעות הפוריות והחשובות ביותר לחקלאות בעולם? הצטרפו אלינו למסע וירטואלי מרתק בעקבות גרגר אבק זעיר אחד, שייקח אתכם מאזור מקור יבש ושומם ועד להיווצרות אדמת הלוס העשירה. גלו את הכוחות הנסתרים שמעצבים את פני כדור הארץ!</p>

<div id="simulation-container" aria-label="סימולציית יצירת אדמת לוס על ידי רוח">
    <div id="source-area" class="area" aria-label="אזור מקור לגרגירים: מדבר או אפיק נהר יבש">אזור מקור<br>(מדבר / אפיק יבש)</div>
    <div id="deposition-area" class="area" aria-label="אזור שקיעת גרגירים: צמחייה או מחסום">אזור שקיעה<br>(צמחייה / מחסום)</div>
    <div id="ground-line"></div> <!-- Added for visual ground -->
    <div id="particles-container" aria-hidden="true"></div>
    <div id="wind-control">
        <label for="wind-speed">עוצמת רוח:</label>
        <input type="range" id="wind-speed" min="0" max="100" value="50" aria-label="בקר עוצמת רוח">
        <span id="wind-value">50</span>
        <div id="wind-indicator">
             <span id="wind-low" class="wind-level">חלשה</span>
             <span id="wind-medium" class="wind-level">בינונית</span>
             <span id="wind-high" class="wind-level">חזקה</span>
        </div>
    </div>
</div>

<style>
/* כללי גופן ובסיס */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.7;
    color: #333;
    direction: rtl; /* Hebrew support */
    text-align: right; /* Hebrew support */
}

h1, h2, h3 {
    color: #1a4e8b; /* Deep blue */
    text-align: center;
    margin-bottom: 15px;
}

p {
    margin-bottom: 1em;
}

/* סגנון הסימולציה */
#simulation-container {
    width: 900px; /* Wider for better visual flow */
    height: 350px; /* Taller */
    border: 1px solid #ccc;
    position: relative;
    overflow: hidden;
    background: linear-gradient(to bottom, #b2e0ff 0%, #e0f0ff 80%, #d2b48c 80%, #d2b48c 100%); /* Sky and ground gradient */
    margin: 30px auto;
    border-radius: 12px; /* More rounded corners */
    box-shadow: 0 4px 12px rgba(0,0,0,0.15); /* Softer, larger shadow */
    perspective: 1000px; /* For potential 3D effects if needed, good practice */
}

#ground-line {
    position: absolute;
    bottom: 80px; /* Aligned with the top of the area divs */
    left: 0;
    width: 100%;
    height: 5px; /* Visual ground line */
    background-color: rgba(180, 140, 90, 0.5); /* Ground color hint */
    z-index: 1; /* Below particles */
}


.area {
    position: absolute;
    bottom: 0; /* Position at the very bottom */
    width: 200px; /* Adjusted width */
    height: 80px; /* Fixed height from the bottom */
    color: rgba(255, 255, 255, 0.9); /* White with slight transparency */
    text-align: center;
    padding-top: 10px;
    box-sizing: border-box;
    font-size: 0.9em;
    font-weight: bold;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.6); /* Stronger shadow for readability */
    z-index: 2; /* Above ground line */
    border-top: 3px solid rgba(255,255,255,0.3); /* Subtle top border */
}

#source-area {
    left: 0;
    background: linear-gradient(to bottom, rgba(210, 180, 140, 0.9) 0%, rgba(180, 140, 90, 0.9) 100%); /* Sandy/dry gradient */
    border-bottom-right-radius: 0; /* Sharp bottom edge */
    border-top-left-radius: 12px; /* Match container */
}

#deposition-area {
    right: 0;
    background: linear-gradient(to bottom, rgba(107, 142, 35, 0.9) 0%, rgba(85, 107, 47, 0.9) 100%); /* Green/earthy gradient */
    border-bottom-left-radius: 0; /* Sharp bottom edge */
    border-top-right-radius: 12px; /* Match container */
}

#particles-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none; /* Don't interfere with controls */
    z-index: 5; /* Above areas and ground */
}

.silt-particle {
    position: absolute;
    width: 3px; /* Particle size */
    height: 3px;
    background-color: #c0b283; /* Loess color */
    border-radius: 50%;
    opacity: 0.9; /* Slightly less opaque */
    transform: translate(-50%, -50%); /* Center the particle */
    transition: opacity 0.5s ease-out; /* Smooth fade out on removal */
    will-change: transform, opacity; /* Optimize animation */
}

.silt-particle.deposited {
    background-color: #a09468; /* Slightly darker when deposited */
    opacity: 1;
    transition: none; /* No opacity transition after depositing */
}

/* סגנון בקר הרוח */
#wind-control {
    position: absolute;
    top: 20px; /* Positioned near the top */
    left: 50%;
    transform: translateX(-50%);
    background-color: rgba(255, 255, 255, 0.95); /* More opaque white */
    padding: 10px 20px;
    border-radius: 8px; /* More rounded */
    z-index: 10;
    display: flex;
    align-items: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

#wind-control label {
    margin-right: 15px; /* More spacing */
    font-weight: bold;
    color: #555;
    font-size: 0.95em;
}

#wind-control input[type="range"] {
    width: 200px; /* Wider slider */
    margin-right: 10px;
    -webkit-appearance: none; /* Remove default slider style */
    appearance: none;
    height: 8px;
    background: #ddd;
    outline: none;
    opacity: 0.7;
    transition: opacity .2s;
    border-radius: 5px;
}

#wind-control input[type="range"]:hover {
    opacity: 1;
}

#wind-control input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 18px;
    height: 18px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 1px 4px rgba(0,0,0,0.2);
}

#wind-control input[type="range"]::-moz-range-thumb {
    width: 18px;
    height: 18px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 1px 4px rgba(0,0,0,0.2);
}

#wind-value {
    font-weight: bold;
    color: #007bff;
    min-width: 25px; /* Ensure consistent width */
    text-align: left;
}

#wind-indicator {
    display: flex;
    position: absolute;
    top: -15px; /* Position above slider */
    width: calc(100% - 40px); /* Match slider width roughly */
    left: 20px; /* Align with padding */
    justify-content: space-between;
    font-size: 0.75em;
    color: #777;
}

.wind-level:before {
    content: '•'; /* Dot indicator */
    margin-left: 3px;
}
#wind-low { text-align: right; }
#wind-medium { text-align: center; transform: translateX(-50%); left: 50%; position: absolute; }
#wind-high { text-align: left; }


/* סגנון הסבר נוסף */
#explanation {
    border-top: 1px solid #eee;
    margin-top: 30px;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    line-height: 1.8; /* Increased line height */
    color: #444;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    /* Smooth transition for display toggle */
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.5s ease-out, visibility 0.5s ease-out;
}

#explanation.visible {
    opacity: 1;
    visibility: visible;
}

#explanation h2 {
    color: #0056b3;
    margin-bottom: 15px;
    padding-bottom: 5px;
    border-bottom: 2px solid #007bff; /* Underline effect */
    display: inline-block; /* Shrink border to text width */
}
#explanation h3 {
    color: #0069d9; /* Slightly lighter blue */
    margin-top: 20px;
    margin-bottom: 10px;
}

#explanation p {
    margin-bottom: 15px;
}

#explanation ul {
    margin-top: 10px;
    margin-bottom: 15px;
    padding-right: 25px; /* Indent list */
}

#explanation li {
    margin-bottom: 8px; /* More space between list items */
    list-style-type: disc;
    line-height: 1.6;
}

/* סגנון כפתור הצג/הסתר */
button#toggle-explanation {
    display: block;
    margin: 30px auto 20px auto; /* More space */
    padding: 12px 25px; /* Larger button */
    cursor: pointer;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 6px; /* More rounded */
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth hover & press effect */
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

button#toggle-explanation:hover {
    background-color: #0056b3;
}

button#toggle-explanation:active {
     transform: scale(0.98); /* Slight press effect */
     box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

/* הוספת אנימציה עדינה לרקע או אלמנטים? קצת יותר מורכב ב-CSS בלבד עם מבנה נתון */
/* נסתמך על אנימציות חלקיקים ב-JS */

</style>

<button id="toggle-explanation">גלו עוד: הסבר מעמיק על אדמת לוס</button>

<div id="explanation" style="display: none;"> <!-- JS will manage class for transition -->
    <h2>המסע המופלא של הלוס: מהמקור ועד לשדה החקלאי</h2>
    <h3>מהו לוס ולמה הוא כה מיוחד?</h3>
    <p>לוס (Loess) הוא סוג קרקע ייחודי, המורכב ברובו מגרגירי סילט עדינים (0.002-0.05 מ"מ). חשבו עליו כעל אבק דק במיוחד! הרכבו עשיר במינרלים חיוניים כמו קוורץ, פלדספטים וקרבונטים (סידן). מה שהופך את הלוס לפורה כל כך הוא לא רק הרכבו, אלא גם מבנהו: הוא נקבובי ומאוורר, מאפשר למים לחלחל ביעילות ועם זאת שומר על לחות זמינה לשורשי הצמחים. הוא גם נוח לעיבוד - יתרון אדיר לחקלאים!</p>
    <h3>היכן נולדים גרגרי הלוס? סיפורי מקור</h3>
    <p>גרגרי הסילט הזעירים שמרכיבים את הלוס אינם נוצרים יש מאין. הם תוצר של כוחות טבע אדירים המפוררים סלעים למרכיביהם הדקים. מקורותיהם העיקריים הם:</p>
    <ul>
        <li><strong>שאריות עידן הקרח:</strong> בתקופות קרח, יריעות קרח ענקיות פעלו כמטחנות ענק, שחקו סלעים ויצרו כמויות עצומות של "קמח סלעים" מכל הגדלים. כשהקרחונים נסוגו, נחשפו משקעים אלו, והרוח סחפה מהם את החלקיקים הקלים ביותר - הסילט.</li>
        <li><strong>לידות במדבר:</strong> במדבריות, שינויי טמפרטורה קיצוניים ותהליכי בליה פיזית מפוררים סלעים. הרוח המדברית החזקה אוספת את החול והסילט שנוצרו ומסיעה אותם.</li>
        <li><strong>מזכרות מנהרות ואגמים:</strong> משקעי סילט מצטברים בקרקעית נהרות ואגמים. כאשר מקורות מים אלו מתייבשים או משנים את מסלולם, נחשפים משקעים עדינים אלו לרוח.</li>
    </ul>
    <h3>ריקוד הרוח: איך גרגרי סילט עפים רחוק?</h3>
    <p>הרוח מסיעה חלקיקי קרקע בשלוש דרכים עיקריות, התלויות בגודל החלקיק ובעוצמת הרוח:</p>
    <ul>
        <li><strong>התגלגלות (Creep):</strong> החלקיקים הכבדים ביותר (כמו חול גס) פשוט מתגלגלים על פני השטח.</li>
        <li><strong>טלטול (Saltation):</strong> חלקיקים בגודל חול קופצים ומנתרים באוויר למרחקים קצרים, מונעים על ידי הרוח או פגיעות של חלקיקים אחרים.</li>
        <li><strong>רחף (Suspension):</strong> וזה המנגנון החשוב ביותר עבור לוס! חלקיקי סילט וחרסית, שהם קלים במיוחד, נישאים באוויר בתוך זרמי הרוח, ממש כמו אבק. הם יכולים להישאר מרחפים במשך שעות ואף ימים ולעבור כך מאות ואלפי קילומטרים ממקורם הראשוני, גם בעוצמות רוח שאינן קיצוניות.</li>
    </ul>
    <p>ככל שהרוח חזקה יותר, כך היא יכולה להרים חלקיקים גדולים יותר ולהסיע אותם רחוק יותר.</p>
    <h3>סוף המסע: איפה עוצרת הרוח את הלוס?</h3>
    <p>לאחר מסע ארוך באוויר, גרגרי הסילט שוקעים כאשר כוח הרוח נחלש מספיק כדי שלא יוכל להחזיקם יותר ברחף. זה קורה לרוב כשהרוח נתקלת במכשולים שמאטים אותה:</p>
    <ul>
        <li><strong>מחסומי צמחייה:</strong> יערות, שיחים סבוכים או אפילו שדות עשב גבוה פועלים כמסנני רוח טבעיים. כשהרוח חודרת לתוך צמחייה, מהירותה יורדת בחדות, וגרגרי הלוס נושרים מזרם האוויר ומצטברים למרגלות הצמחייה או בתוכה.</li>
        <li><strong>שינויים טופוגרפיים:</strong> גבעות, רכסים או אפילו שיפועים עדינים יכולים לגרום לרוח להאט את מהירותה בצד הפונה לרוח, מה שמעודד שקיעה.</li>
        <li><strong>היחלשות טבעית:</strong> ככל שהרוח מתרחקת ממקור עוצמתי (למשל, שקע ברומטרי), היא נחלשת בהדרגה, מה שמוביל לשקיעה איטית ומפוזרת יותר לאורך הדרך.</li>
    </ul>
    <p>הצטברות הדרגתית של גרגירי סילט אלו, שכבה אחר שכבה, במשך אלפי שנים, בונה בסופו של דבר את מרבצי הלוס העבים והפוריים שאנו מוצאים היום.</p>
    <h3>לוס בישראל ובעולם: קרקע של חיים</h3>
    <p>אדמות לוס מכסות שטחים עצומים על פני כדור הארץ, ולרוב מהוות בסיס לחקלאות ענפה. מישורי הלוס העצומים בסין (שכמה מטרים מהם בנויים מהאבק שהגיע ממדבר גובי), ה"קורנבלט" (חגורת התירס) הפורה של אמריקה הצפונית, מישורים במרכז אירופה - כולם בנויים על לוס. בישראל, הנגב הצפוני והמערבי מכוסים בשכבת לוס עבה, שמקורה בעיקר באבק שהגיע במשך אלפי שנים ממדבריות סיני וצפון אפריקה, ובלוס שהגיע בדרך הים והרוח מערוצי הנילוס. הלוס בנגב, למרות תנאי האקלים היבשים, הוא הבסיס לחקלאות מדברית משגשגת.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const simulationContainer = document.getElementById('simulation-container');
    const particlesContainer = document.getElementById('particles-container');
    const windSpeedControl = document.getElementById('wind-speed');
    const windValueSpan = document.getElementById('wind-value');
    const sourceArea = document.getElementById('source-area');
    const depositionArea = document.getElementById('deposition-area');
    const groundLine = document.getElementById('ground-line'); // Get the ground line element
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    const simWidth = simulationContainer.clientWidth;
    const simHeight = simulationContainer.clientHeight;
    const sourceWidth = sourceArea.clientWidth;
    const sourceAreaBottom = simHeight - sourceArea.clientHeight; // Y coordinate of source area top
    const depoStart = depositionArea.offsetLeft;
    const depoEnd = depoStart + depositionArea.clientWidth;
    const groundY = groundLine.offsetTop; // Y coordinate of the ground line

    let particles = [];
    const maxParticles = 400; // Increased particle limit
    const baseSpawnRate = 1.5; // Increased base spawn rate
    const particleSize = 3; // Match CSS

    let windSpeed = parseInt(windSpeedControl.value, 10);

    // Update wind speed display and value
    const updateWindSpeed = () => {
        windSpeed = parseInt(windSpeedControl.value, 10);
        windValueSpan.textContent = windSpeed;
    };

    // Create a single particle
    const createParticle = () => {
        if (particles.length >= maxParticles || windSpeed < 5) { // Minimum wind to spawn
            return;
        }

        const particleElement = document.createElement('div');
        particleElement.classList.add('silt-particle');

        // Spawn position within source area, very close to the 'ground'
        // Added some randomness to the initial Y position near the ground
        const startX = Math.random() * sourceWidth;
        const startY = groundY - (Math.random() * 10 + 1); // Spawn just above the ground line in source area

        particleElement.style.left = startX + 'px';
        particleElement.style.top = startY + 'px';

        particlesContainer.appendChild(particleElement);

        particles.push({
            element: particleElement,
            x: startX,
            y: startY,
            // Initial velocity - mostly horizontal, slight upward kick
            velocity: {
                 x: (windSpeed / 100) * 0.5 + Math.random() * 0.2, // Base horizontal speed
                 y: - (windSpeed / 100) * 0.1 - Math.random() * 0.1 // Slight initial upward velocity
            },
            isDeposited: false,
            // Store initial position for potential ground interaction if needed (not implementing complex bounce here)
            // initialY: startY
        });
    };

    // Physics constants (simplified)
    const gravity = 0.05; // Pulls particles down
    const airResistanceFactor = 0.005; // Slows particles down
    const turbulenceFactor = 0.1; // Randomness in movement

    // Update particle positions
    const updateParticles = (deltaTime) => {
        const dt = deltaTime / 16; // Normalize movement speed to 60fps

        particles.forEach(particle => {
            if (particle.isDeposited) {
                 // Deposited particles don't move
                 return;
            }

            // Apply gravity
            particle.velocity.y += gravity * dt;

            // Apply wind force (mostly horizontal acceleration)
            const windForceX = (windSpeed / 100) * 0.8 * dt; // Stronger horizontal push
            particle.velocity.x += windForceX;

             // Apply air resistance (opposes velocity)
             const speed = Math.sqrt(particle.velocity.x * particle.velocity.x + particle.velocity.y * particle.velocity.y);
             if (speed > 0.01) {
                 const resistanceX = -particle.velocity.x / speed * airResistanceFactor * dt;
                 const resistanceY = -particle.velocity.y / speed * airResistanceFactor * dt;
                 particle.velocity.x += resistanceX;
                 particle.velocity.y += resistanceY;
             }


            // Apply turbulence (random fluctuations, stronger with more wind)
            if (windSpeed > 10) {
                 particle.velocity.x += (Math.random() - 0.5) * (windSpeed / 100) * turbulenceFactor * dt;
                 particle.velocity.y += (Math.random() - 0.5) * (windSpeed / 100) * turbulenceFactor * dt;
            }


            // Update position based on velocity
            particle.x += particle.velocity.x * dt;
            particle.y += particle.velocity.y * dt;

            // Clamp vertical position to prevent going too high (simulated ceiling)
             particle.y = Math.max(10, particle.y); // Don't go above 10px from top


            // Check for deposition within deposition area (y >= groundY)
            if (particle.x >= depoStart && particle.x <= depoEnd && particle.y >= groundY - particleSize/2) {
                 particle.isDeposited = true;
                 particle.element.classList.add('deposited');
                 // Snap to ground Y position and slightly randomize X within deposition area to look like accumulation
                 particle.y = groundY - particleSize/2;
                 // Optional: Adjust X slightly for visual layering if many particles deposit on the same X
                 // For simplicity, keep current X or randomize slightly
                 // particle.x = Math.max(depoStart, Math.min(depoEnd - particleSize, particle.x + (Math.random() - 0.5) * 5)); // Adjust X slightly
                 particle.element.style.zIndex = 4; // Put deposited below active particles

                 // Stop updating this particle in future frames (will filter it out below)

            } else if (particle.y >= groundY - particleSize/2 && particle.x < depoStart) {
                // Particle hit the ground in the source area BEFORE deposition area - simulate staying there or a small bounce/roll
                // For simplicity, let's just stop horizontal movement or make it very slow
                particle.velocity.x *= 0.1; // Drastically reduce horizontal speed
                particle.velocity.y = -particle.velocity.y * 0.3; // Small bounce
                particle.y = groundY - particleSize/2; // Reset to ground level
                 if (windSpeed < 20) { // If wind is low, particles stay put
                     particle.velocity.x = 0;
                     particle.velocity.y = 0;
                 }
            }


            // Update element position
            particle.element.style.left = particle.x + 'px';
            particle.element.style.top = particle.y + 'px';

        });

        // Filter out particles that went off screen or are deposited
        particles = particles.filter(particle => {
            // Remove if off-screen to the right
            const isOffScreenRight = particle.x > simWidth + 10;
            // Remove if deposited (already handled visual class, just filter from active list)
            const isAlreadyDeposited = particle.isDeposited;

            if (isOffScreenRight) {
                 particle.element.remove(); // Remove from DOM
            }
            // Keep deposited particles in DOM but not in the 'active' particles array for updates
            if(isAlreadyDeposited) {
                // The element is kept, but the object is removed from the 'particles' array for next frame's update loop
                return true; // Keep in array for this frame, filtered next frame
            }


            return !isOffScreenRight; // Keep particle if it's not off-screen and not deposited
        });

         // Important: Rebuild particles array *after* filtering, keeping only those that remain active
         // Need a better way to manage deposited vs active. Let's keep deposited in a separate array or just filter the main one and rely on isDeposited flag.
         // Let's refactor: keep *all* particles in the array, but update *only* those !isDeposited. Filter out only when off-screen.
         particles = particles.filter(particle => {
             const isOffScreenRight = particle.x > simWidth + 10;
             if (isOffScreenRight) {
                 particle.element.remove();
             }
             return !isOffScreenRight; // Keep particle if it's not off-screen
         });

         // Now update positions only for non-deposited particles
         // (The loop above should be re-run or logic changed to iterate over all, update only non-deposited)
         // Let's stick to the previous filter logic for now as it's simpler to manage the list size, just ensure deposited ones are handled.
         // The current filter removes off-screen AND implicitly relies on the isDeposited flag to stop updates in the loop. This seems functional.

    };

    // Animation loop
    let lastTime = 0;
    const gameLoop = (currentTime) => {
        if (!lastTime) lastTime = currentTime;
        const deltaTime = currentTime - lastTime; // Time elapsed since last frame

        // Spawn particles based on wind speed and time
        // Higher wind means more particles lifted
        const spawnRate = (windSpeed / 100) * baseSpawnRate * (windSpeed > 10 ? 1 : 0); // Only spawn if wind > 10
        const particlesToSpawn = Math.floor(spawnRate * (deltaTime / 16)); // Adjust based on wind and delta time

        for (let i = 0; i < particlesToSpawn; i++) {
             createParticle();
        }


        updateParticles(deltaTime);

        lastTime = currentTime;
        requestAnimationFrame(gameLoop);
    };

    // Toggle explanation visibility with transition
    const toggleExplanation = () => {
        const isHidden = explanationDiv.classList.contains('visible') === false;
        if (isHidden) {
            explanationDiv.style.display = 'block'; // Show before animating opacity
            // Use a small timeout to allow display:block to apply before transition
            setTimeout(() => {
                explanationDiv.classList.add('visible');
            }, 10); // A 10ms timeout is often enough
            toggleButton.textContent = 'הסתר הסבר נוסף';
        } else {
            explanationDiv.classList.remove('visible');
            // Wait for transition to finish before hiding completely
            explanationDiv.addEventListener('transitionend', function handler() {
                explanationDiv.style.display = 'none';
                explanationDiv.removeEventListener('transitionend', handler);
            });
            toggleButton.textContent = 'גלו עוד: הסבר מעמיק על אדמת לוס';
        }
    };


    // Event listeners
    windSpeedControl.addEventListener('input', updateWindSpeed);
    toggleButton.addEventListener('click', toggleExplanation);

    // Initial setup
    updateWindSpeed(); // Set initial wind speed and display
    gameLoop(0); // Start the animation loop

    // Improve visual indication of wind level on the slider
    windSpeedControl.addEventListener('input', () => {
        const value = parseInt(windSpeedControl.value, 10);
        const max = parseInt(windSpeedControl.max, 10);
        const min = parseInt(windSpeedControl.min, 10);
        const range = max - min;
        const percentage = (value - min) / range;

        const low = document.getElementById('wind-low');
        const medium = document.getElementById('wind-medium');
        const high = document.getElementById('wind-high');

        // Remove active class from all
        low.style.color = '#777';
        medium.style.color = '#777';
        high.style.color = '#777';
        low.style.fontWeight = 'normal';
        medium.style.fontWeight = 'normal';
        high.style.fontWeight = 'normal';

        // Highlight current level
        if (percentage < 0.33) {
            low.style.color = '#007bff';
            low.style.fontWeight = 'bold';
        } else if (percentage < 0.66) {
            medium.style.color = '#007bff';
             medium.style.fontWeight = 'bold';
        } else {
            high.style.color = '#007bff';
             high.style.fontWeight = 'bold';
        }
    });

    // Initial highlight
     windSpeedControl.dispatchEvent(new Event('input'));

});
</script>