---
title: "ריקוד הרובוטים: אינטליגנציה קולקטיבית בחוקים פשוטים"
english_slug: robot-swarm-shared-task-simple-rules
category: "טכנולוגיה / מדעי המחשב"
tags:
  - רובוטיקה
  - נחיל רובוטים
  - אינטליגנציה קולקטיבית
  - מערכות מבוזרות
  - בינה מלאכותית
---
# ריקוד הרובוטים: אינטליגנציה קולקטיבית בחוקים פשוטים

דמיינו מאות ואלפי רובוטים קטנים, שכל אחד מהם פועל לפי כמה כללים פשוטים בלבד, מצליחים יחד לבצע משימות ענק שרובוט יחיד לא יכול אפילו להתחיל לדמם? ברוכים הבאים לעולם המרתק של נחילי רובוטים! איך אוסף של יחידות "לא חכמות" יוצר התנהגות קבוצתית מדהימה בלי מנהיג מרכזי? התנסו בסימולציה ושחקו עם החוקים כדי לגלות את הקסם של אינטליגנציית הנחיל.

<div id="swarm-app-container">
    <canvas id="swarmCanvas" width="800" height="500"></canvas>
    <div id="controls">
        <h3>קבעו את החוקים לריקוד הרובוטים:</h3>

        <div class="control-group">
            <label for="separationWeight">דחייה (שמירת מרחק משכנים):</label>
            <input type="range" id="separationWeight" min="0" max="10" value="3" step="0.1">
            <span id="separationValue">3.0</span>
            <p class="rule-explanation">כמה חזק הרובוט דוחה שכנים קרובים מדי. מונע התנגשויות וצפיפות.</p>
        </div>

        <div class="control-group">
            <label for="alignmentWeight">התיישרות (תנועה בכיוון שכנים):</label>
            <input type="range" id="alignmentWeight" min="0" max="10" value="1" step="0.1">
            <span id="alignmentValue">1.0</span>
             <p class="rule-explanation">כמה חזק הרובוט שואף להתיישר עם כיוון התנועה הממוצע של שכניו.</p>
        </div>

        <div class="control-group">
            <label for="cohesionWeight">משיכה (התקבצות עם שכנים):</label>
            <input type="range" id="cohesionWeight" min="0" max="10" value="1" step="0.1">
            <span id="cohesionValue">1.0</span>
            <p class="rule-explanation">כמה חזק הרובוט נמשך למרכז המסה של שכניו. גורם לנחיל להישאר מגובש.</p>
        </div>

        <div class="control-group">
            <label for="targetWeight">משיכה למטרות (נקודות איסוף):</label>
            <input type="range" id="targetWeight" min="0" max="10" value="5" step="0.1">
            <span id="targetValue">5.0</span>
            <p class="rule-explanation">כמה חזק הרובוט נמשך למטרה הקרובה ביותר שטרם נאספה.</p>
        </div>

         <div class="control-group">
            <label for="wallAvoidanceWeight">דחייה מקירות:</label>
            <input type="range" id="wallAvoidanceWeight" min="0" max="20" value="10" step="0.5">
            <span id="wallAvoidanceValue">10.0</span>
            <p class="rule-explanation">כמה חזק הרובוט נדחה מגבולות המסך. מונע "בריחה" מהסביבה.</p>
        </div>

        <div id="score-display">
            מטרות נאספו: <span id="collected-count">0</span> / <span id="total-count">0</span>
        </div>

        <div class="button-row">
            <button id="startButton">התחל סימולציה</button>
            <button id="stopButton" disabled>עצור סימולציה</button>
            <button id="resetButton">אפס סימולציה</button>
        </div>
         <p class="task-description">המשימה: אספו את כל הנקודות הצהובות. לחצו על המסך להוספת מטרות חדשות!</p>
    </div>
</div>

<style>
    /* גופנים בסיסיים */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6; /* Light background */
        margin: 0;
        padding: 20px;
    }

     h1, h2, h3 {
        color: #0056b3; /* Theme color */
        margin-bottom: 10px;
    }

     h1 {
         text-align: center;
         margin-bottom: 20px;
     }


    #swarm-app-container {
        display: flex;
        flex-direction: column;
        gap: 25px;
        margin: 20px auto;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        max-width: 840px; /* Slightly wider to accommodate padding + canvas */
        align-items: center;
    }

    #swarmCanvas {
        border: 1px solid #a0a0a0;
        background: linear-gradient(to bottom right, #e9f5f5, #d0e9ea); /* Subtle gradient */
        display: block;
        border-radius: 8px;
        box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.05);
    }

    #controls {
        width: 100%;
        max-width: 800px; /* Match canvas width */
        display: flex;
        flex-direction: column;
        gap: 15px;
        padding: 20px;
        border: 1px solid #d0d0d0;
        border-radius: 8px;
        background-color: #f8f8f8;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    }

    #controls h3 {
        margin-top: 0;
        margin-bottom: 15px;
        text-align: center;
        color: #007bff; /* Accent color */
    }

    .control-group {
        display: flex;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        align-items: center;
        gap: 10px;
        padding: 5px 0;
        border-bottom: 1px dashed #eee; /* Separator */
    }

     .control-group:last-child {
         border-bottom: none;
         margin-bottom: 10px;
     }


     .control-group label {
        flex-basis: 180px; /* Fixed width for labels */
        min-width: 120px;
        font-weight: bold;
        color: #555;
     }

    .control-group input[type="range"] {
        flex-grow: 1; /* Range slider takes available space */
        margin-right: 5px; /* Space between slider and value */
    }

     .control-group span {
         min-width: 35px; /* Ensure value display has space */
         text-align: right;
         font-weight: bold;
         color: #007bff;
     }

    .rule-explanation {
        flex-basis: 100%; /* Takes full width */
        font-size: 0.9em;
        color: #666;
        margin-top: -5px; /* Reduce space above */
        margin-bottom: 5px;
        padding-left: 180px; /* Align with slider start */
        box-sizing: border-box; /* Include padding in width */
    }
     @media (max-width: 600px) {
        .control-group label, .rule-explanation {
             flex-basis: 100%; /* Full width on small screens */
             padding-left: 0;
             text-align: left;
        }
         .control-group input[type="range"] {
             width: 100%; /* Slider takes full width */
             margin-right: 0;
         }
         .control-group span {
             flex-grow: 1; /* Value takes remaining space */
             text-align: right;
         }
         .control-group {
            flex-direction: column;
            align-items: flex-start;
         }
     }


    #score-display {
        text-align: center;
        font-size: 1.1em;
        font-weight: bold;
        margin: 15px 0 10px 0;
        color: #007bff;
    }

    .button-row {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 10px;
    }

    .button-row button {
        padding: 10px 20px;
        font-size: 1rem;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #startButton {
        background-color: #28a745; /* Green */
        color: white;
    }

    #startButton:hover:not(:disabled) {
        background-color: #218838;
         transform: translateY(-1px);
    }

     #stopButton {
        background-color: #dc3545; /* Red */
        color: white;
     }

     #stopButton:hover:not(:disabled) {
        background-color: #c82333;
         transform: translateY(-1px);
     }

      #stopButton:disabled {
         background-color: #cccccc;
         cursor: not-allowed;
      }

    #resetButton {
        background-color: #007bff; /* Blue */
        color: white;
    }

    #resetButton:hover:not(:disabled) {
        background-color: #0069d9;
        transform: translateY(-1px);
    }

    .task-description {
        text-align: center;
        font-style: italic;
        color: #555;
        margin-top: 15px;
    }


    #explanation-toggle {
        display: block;
        width: fit-content;
        margin: 20px auto;
        padding: 10px 20px;
        font-size: 1rem;
        cursor: pointer;
        border: 1px solid #0056b3;
        border-radius: 4px;
        background-color: #e7f0ff;
        color: #0056b3;
        transition: background-color 0.3s ease, box-shadow 0.2s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    #explanation-toggle:hover {
        background-color: #d0e4ff;
         box-shadow: 0 3px 6px rgba(0,0,0,0.1);
    }

    #explanation-content {
        display: none; /* Hidden by default */
        margin: 20px auto;
        padding: 20px;
        border: 1px solid #d0d0d0;
        border-radius: 8px;
        background-color: #f9f9f9;
        max-width: 800px; /* Match control width */
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    }

    #explanation-content h2 {
        color: #333;
        margin-top: 15px;
        margin-bottom: 8px;
        border-bottom: 1px solid #eee;
        padding-bottom: 4px;
    }

    #explanation-content p {
        margin-bottom: 12px;
        line-height: 1.7;
        color: #444;
    }

     #explanation-content ul {
        margin-bottom: 12px;
        padding-left: 25px;
     }

     #explanation-content li {
         margin-bottom: 6px;
         color: #444;
     }

     #explanation-content li::marker {
         color: #007bff; /* Bullet color */
     }

    /* Animation for completion message */
    @keyframes fadeInOut {
        0% { opacity: 0; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1); }
        100% { opacity: 0; transform: scale(0.8); }
    }

    .completion-message {
        font-size: 36px;
        font-weight: bold;
        color: #28a745; /* Green */
        text-align: center;
        position: absolute; /* Position over canvas */
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        animation: fadeInOut 3s ease-out forwards; /* Animation */
        pointer-events: none; /* Allow clicks on canvas underneath */
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }


</style>

<button id="explanation-toggle">הצג/הסתר הסבר על נחילי רובוטים</button>

<div id="explanation-content">
    <h2>מהו נחיל רובוטים (Robot Swarm)?</h2>
    <p>נחיל רובוטים הוא אוסף גדול של רובוטים פשוטים יחסית, הפועלים יחד כמערכת אחת לביצוע משימה משותפת, ממש כמו נחיל חרקים או להקת ציפורים בטבע. המאפיינים המרכזיים שלהם כוללים:</p>
    <ul>
        <li>**מספר רב:** לרוב עשרות, מאות או אפילו אלפי יחידות.</li>
        <li>**יחידות פשוטות:** כל רובוט בודד בעל יכולות חישה, עיבוד ותנועה בסיסיות ומוגבלות. הם אינם "חכמים" לבדם ואינם בעלי ידע גלובלי על מצב הנחיל כולו.</li>
        <li>**אינטראקציה מקומית:** הרובוטים מתקשרים (אם בכלל) או מגיבים רק לרובוטים קרובים אליהם או לסביבתם המיידית. אין "מוח" מרכזי המנהל את כולם.</li>
    </ul>

    <h2>למה נחילים? היתרונות הגדולים:</h2>
    <p>במקום רובוט יחיד ומורכב, נחילי רובוטים מציעים יתרונות משמעותיים באתגרים רבים:</p>
    <ul>
        <li>**עמידות לתקלות (Robustness):** גם אם יחידות בודדות כושלות, המשימה הכוללת לרוב נמשכת, מכיוון שהמשימה מבוזרת בין רבים.</li>
        <li>**סקלביליות (Scalability):** קל יחסית להוסיף עוד רובוטים לנחיל כדי להגדיל את יכולת הביצוע או להתמודד עם משימות גדולות יותר.</li>
        <li>**גמישות והתאמה:** נחיל יכול להסתגל במהירות לשינויים בסביבה או למשימות חדשות.</li>
        <li>**יעילות במשימות מבוזרות:** איסוף מידע משטח נרחב, חיפוש באזור גדול, או בנייה מודולרית - כל אלו הופכים יעילים ואפשריים יותר עם שיתוף פעולה של יחידות רבות.</li>
    </ul>

    <h2>לב הסיפור: אינטליגנציה קולקטיבית</h2>
    <p>הרעיון המדהים כאן הוא "אינטליגנציה קולקטיבית" (Collective Intelligence) או "אינטליגנציית נחיל" (Swarm Intelligence). זוהי היכולת של קבוצה ליצור התנהגות מורכבת, מתואמת ויעילה, הנובעת אך ורק מהאינטראקציות הפשוטות והמקומיות בין היחידות הבודדות, מבלי שאינטליגנציה זו מתוכננת או מקודדת באופן ישיר בכל יחידה. זוהי דוגמה קלאסית ל"התנהגות מתהווה" (Emergent Behavior).</p>
    <p>המפתח טמון בתכנון חוקים פשוטים לכל רובוט (כמו אלה ששיניתם בסימולציה!), כך שסך כל התגובות המקומיות יוביל להתנהגות גלובלית רצויה - כמו שמירה על מבנה אחיד, הימנעות ממכשולים, או התקדמות משותפת לעבר מטרה.</p>

    <h2>השראה מהטבע ויישומים:</h2>
    <p>נחילי רובוטים שואבים השראה עמוקה ממערכות ביולוגיות כמו:</p>
    <ul>
        <li>**נמלים וטרמיטים:** בניית מבנים מורכבים, חיפוש ואסוף מזון.</li>
        <li>**להקות דגים וציפורים (סטירמר):** תנועה מתואמת ומרהיבה להגנה מטורפים או לניווט.</li>
    </ul>
    <p>היישומים הפוטנציאליים לנחילי רובוטים עצומים וכוללים:</p>
    <ul>
        <li>**חיפוש והצלה:** סריקת שטחים נרחבים במהירות אחרי אסונות.</li>
        <li>**חקלאות:** ניטור שדות ענק וטיפול נקודתי בצמחים.</li>
        <li>**בנייה והרכבה:** הקמת מבנים מורכבים על ידי יחידות קטנות.</li>
        <li>**ניטור סביבתי:** מדידות נרחבות של איכות אוויר/מים.</li>
        <li>**לוגיסטיקה:** מיון והובלת מוצרים במחסנים או נמלים.</li>
        <li>**ביטחון:** סיור, מעקב, וסילוק מוקשים.</li>
    </ul>
    <p>הסימולציה בה התנסיתם מציגה מודל בסיסי של התנהגות נחיל - היכולת לנוע יחד, לשמור על מרחק, ולהימשך למטרות. על ידי שינוי החוקים, ראיתם כיצד התנהגות הנחיל כולו משתנה באופן דרמטי, מדגימה את העיקרון המרכזי של יצירת סדר מורכב מחוקים מקומיים פשוטים.</p>
</div>

<script>
    const canvas = document.getElementById('swarmCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startButton');
    const stopButton = document.getElementById('stopButton');
    const resetButton = document.getElementById('resetButton');
    const explanationToggle = document.getElementById('explanation-toggle');
    const explanationContent = document.getElementById('explanation-content');

    // Rule sliders and value displays
    const separationSlider = document.getElementById('separationWeight');
    const alignmentSlider = document.getElementById('alignmentWeight');
    const cohesionSlider = document.getElementById('cohesionWeight');
    const targetSlider = document.getElementById('targetWeight');
    const wallAvoidanceSlider = document.getElementById('wallAvoidanceWeight');

    const separationValue = document.getElementById('separationValue');
    const alignmentValue = document.getElementById('alignmentValue');
    const cohesionValue = document.getElementById('cohesionValue');
    const targetValue = document.getElementById('targetValue');
    const wallAvoidanceValue = document.getElementById('wallAvoidanceValue');

    // Score display elements
    const collectedCountSpan = document.getElementById('collected-count');
    const totalCountSpan = document.getElementById('total-count');


    let animationFrameId = null;
    let simulationRunning = false;

    // Simulation parameters
    const NUM_ROBOTS = 80; // Increased robots for better swarm effect
    const ROBOT_SIZE = 4; // Slightly smaller robots
    const MAX_SPEED = 2.5; // Slightly faster
    const MAX_FORCE = 0.1; // Steer force
    const NEIGHBOR_RADIUS = 60; // Increased neighbor radius
    const DESIRED_SEPARATION = ROBOT_SIZE * 2.5; // Increased separation distance
    const WALL_AVOIDANCE_DISTANCE = 30; // Wall avoidance radius
    const WALL_AVOIDANCE_FORCE_SCALE = 15; // Stronger force near walls

    const NUM_INITIAL_TARGETS = 8; // Fewer initial targets
    const TARGET_SIZE = 6;
    const TARGET_COLLECTION_RADIUS = 12; // Robots collect when within this distance

    let robots = [];
    let targets = [];
    let collectedTargetCount = 0;
    let totalTargetCount = 0;

    // Rule weights (controlled by sliders)
    let separationWeight = parseFloat(separationSlider.value);
    let alignmentWeight = parseFloat(alignmentSlider.value);
    let cohesionWeight = parseFloat(cohesionSlider.value);
    let targetWeight = parseFloat(targetSlider.value);
    let wallAvoidanceWeight = parseFloat(wallAvoidanceSlider.value);

    // Vector utility functions (kept as they are functional and correct)
    function createVector(x, y) {
        return { x: x, y: y };
    }

    function addVectors(v1, v2) {
        return createVector(v1.x + v2.x, v1.y + v2.y);
    }

    function subtractVectors(v1, v2) {
        return createVector(v1.x - v2.x, v1.y - v2.y);
    }

    function multiplyVectorScalar(v, scalar) {
        return createVector(v.x * scalar, v.y * scalar);
    }

    function divideVectorScalar(v, scalar) {
         if (scalar === 0) return createVector(0, 0);
         return createVector(v.x / scalar, v.y / scalar);
    }

    function vectorMagnitude(v) {
        return Math.sqrt(v.x * v.x + v.y * v.y);
    }

    function normalizeVector(v) {
        const mag = vectorMagnitude(v);
        if (mag === 0) return createVector(0, 0);
        return divideVectorScalar(v, mag);
    }

    function distanceBetween(p1, p2) {
        return vectorMagnitude(subtractVectors(p1, p2));
    }

     function limitVector(v, max) {
        const mag = vectorMagnitude(v);
        if (mag > max) {
            return multiplyVectorScalar(normalizeVector(v), max);
        }
        return v;
     }

     function steerVector(currentVelocity, desiredVelocity, maxForce) {
        let steer = subtractVectors(desiredVelocity, currentVelocity);
        steer = limitVector(steer, maxForce);
        return steer;
     }


    // Robot class (Enhanced drawing and behaviors)
    class Robot {
        constructor(x, y) {
            this.position = createVector(x, y);
            this.velocity = createVector(Math.random() * MAX_SPEED - MAX_SPEED / 2, Math.random() * MAX_SPEED - MAX_SPEED / 2); // Initial velocity towards center maybe?
            this.velocity = limitVector(this.velocity, MAX_SPEED);
            this.acceleration = createVector(0, 0);
            this.color = '#007bff'; // Default color
            this.nearTarget = false; // For visual cue
        }

        update() {
            this.velocity = addVectors(this.velocity, this.acceleration);
            this.velocity = limitVector(this.velocity, MAX_SPEED);
            this.position = addVectors(this.position, this.velocity);
            this.acceleration = createVector(0, 0); // Reset acceleration each frame
        }

        applyForce(force) {
            this.acceleration = addVectors(this.acceleration, force);
        }

        // Boids-like steering behaviors (tuned parameters)
        separate(otherRobots) {
            let steer = createVector(0, 0);
            let count = 0;

            for (let other of otherRobots) {
                let d = distanceBetween(this.position, other.position);
                if (d > 0 && d < DESIRED_SEPARATION) { // Use DESIRED_SEPARATION
                    let diff = subtractVectors(this.position, other.position);
                    diff = normalizeVector(diff);
                    diff = divideVectorScalar(diff, d); // Weight by distance
                    steer = addVectors(steer, diff);
                    count++;
                }
            }

            if (count > 0) {
                steer = divideVectorScalar(steer, count);
                steer = normalizeVector(steer);
                steer = multiplyVectorScalar(steer, MAX_SPEED);
                steer = steerVector(this.velocity, steer, MAX_FORCE);
            }
            return steer;
        }

        align(otherRobots) {
            let steer = createVector(0, 0);
            let count = 0;

            for (let other of otherRobots) {
                 let d = distanceBetween(this.position, other.position);
                if (d > 0 && d < NEIGHBOR_RADIUS) { // Use NEIGHBOR_RADIUS
                    steer = addVectors(steer, other.velocity);
                    count++;
                }
            }

            if (count > 0) {
                steer = divideVectorScalar(steer, count);
                steer = normalizeVector(steer);
                steer = multiplyVectorScalar(steer, MAX_SPEED);
                steer = steerVector(this.velocity, steer, MAX_FORCE);
            }
            return steer;
        }

        cohere(otherRobots) {
            let centerOfMass = createVector(0, 0);
            let count = 0;

            for (let other of otherRobots) {
                 let d = distanceBetween(this.position, other.position);
                if (d > 0 && d < NEIGHBOR_RADIUS) { // Use NEIGHBOR_RADIUS
                    centerOfMass = addVectors(centerOfMass, other.position);
                    count++;
                }
            }

            if (count > 0) {
                centerOfMass = divideVectorScalar(centerOfMass, count);
                // Seek the center of mass
                let desired = subtractVectors(centerOfMass, this.position);
                desired = normalizeVector(desired);
                desired = multiplyVectorScalar(desired, MAX_SPEED);
                let steer = steerVector(this.velocity, desired, MAX_FORCE);
                return steer;
            }
            return createVector(0, 0);
        }

         seekTarget(availableTargets) {
             let steer = createVector(0, 0);
             this.nearTarget = false; // Reset visual cue

             // Find the nearest available target
            let nearestTarget = null;
            let minTargetDistance = Infinity;
            for (let target of availableTargets) {
                let d = distanceBetween(this.position, target.position);
                if (d < minTargetDistance) {
                    minTargetDistance = d;
                    nearestTarget = target;
                }
            }

            if (nearestTarget) {
                 let desired = subtractVectors(nearestTarget.position, this.position);
                 let d = vectorMagnitude(desired);

                 if (d < TARGET_COLLECTION_RADIUS + ROBOT_SIZE) { // Check distance for collection cue
                     this.nearTarget = true;
                 }

                 if (d < TARGET_COLLECTION_RADIUS) {
                      // Mark target as collected by anyone nearby
                      nearestTarget.collected = true; // This will be handled globally in update
                      // Return zero force once target is collected (or let other rules take over)
                       // We still return a small force to keep them moving away from the collected spot
                       // But the primary seek force is negated by the collection logic in flock()
                       desired = createVector(0,0); // Stop seeking this target for now
                 } else {
                     desired = normalizeVector(desired);
                     desired = multiplyVectorScalar(desired, MAX_SPEED);
                 }
                 steer = steerVector(this.velocity, desired, MAX_FORCE);
                 return steer;

            }
            return createVector(0, 0); // No targets available
         }

         avoidWalls() {
            let steer = createVector(0, 0);
            let desired = null;
            const wallDistance = WALL_AVOIDANCE_DISTANCE; // Alias for clarity

            // Check distance to walls
            let distRight = canvas.width - this.position.x;
            let distLeft = this.position.x;
            let distBottom = canvas.height - this.position.y;
            let distTop = this.position.y;

            if (distRight < wallDistance) {
                 desired = createVector(-MAX_SPEED, this.velocity.y); // Steer left
            } else if (distLeft < wallDistance) {
                 desired = createVector(MAX_SPEED, this.velocity.y); // Steer right
            }

            if (distBottom < wallDistance) {
                 if (desired === null) desired = createVector(this.velocity.x, -MAX_SPEED); // Steer up
                 else desired.y = -MAX_SPEED;
            } else if (distTop < wallDistance) {
                 if (desired === null) desired = createVector(this.velocity.x, MAX_SPEED); // Steer down
                 else desired.y = MAX_SPEED;
            }


            if (desired !== null) {
                 // Calculate strength based on proximity (closer = stronger)
                 let minDistance = Math.min(distRight, distLeft, distBottom, distTop);
                 let distanceFactor = 1 - (minDistance / wallDistance); // 1 when at wall, 0 when at wallDistance
                 distanceFactor = Math.max(0, Math.min(1, distanceFactor)); // Clamp between 0 and 1
                 distanceFactor = distanceFactor * WALL_AVOIDANCE_FORCE_SCALE; // Scale force based on proximity

                 desired = normalizeVector(desired);
                 desired = multiplyVectorScalar(desired, MAX_SPEED);
                 steer = steerVector(this.velocity, desired, MAX_FORCE * distanceFactor); // Apply stronger steer force
            }

            return steer;
         }


        // Apply rules based on neighbors and targets
        flock(otherRobots, availableTargets) {
            let separation = this.separate(otherRobots);
            let alignment = this.align(otherRobots);
            let cohesion = this.cohere(otherRobots);
            let targetSeeking = this.seekTarget(availableTargets);
            let wallAvoidance = this.avoidWalls();

            // Apply forces with weights
            separation = multiplyVectorScalar(separation, separationWeight);
            alignment = multiplyVectorScalar(alignment, alignmentWeight);
            cohesion = multiplyVectorScalar(cohesion, cohesionWeight);
            targetSeeking = multiplyVectorScalar(targetSeeking, targetWeight);
            wallAvoidance = multiplyVectorScalar(wallAvoidance, wallAvoidanceWeight);

            this.applyForce(separation);
            this.applyForce(alignment);
            this.applyForce(cohesion);
            this.applyForce(targetSeeking);
            this.applyForce(wallAvoidance);
        }

         // Draw robot as a triangle pointing in direction of velocity
        draw() {
            ctx.save(); // Save current context state
            ctx.translate(this.position.x, this.position.y); // Move context to robot position

            // Calculate angle based on velocity
            const angle = Math.atan2(this.velocity.y, this.velocity.x);
            ctx.rotate(angle); // Rotate context

            // Draw triangle (pointing right in local space, then rotated)
            ctx.beginPath();
            ctx.moveTo(ROBOT_SIZE * 1.5, 0); // Nose
            ctx.lineTo(-ROBOT_SIZE * 0.8, -ROBOT_SIZE); // Back left
            ctx.lineTo(-ROBOT_SIZE * 0.8, ROBOT_SIZE); // Back right
            ctx.closePath();

            // Change color if near a target
            ctx.fillStyle = this.nearTarget ? '#ff9800' : this.color; // Orange when near target, else default blue
            ctx.fill();

            // Optional: Draw a small circle at the center
            // ctx.beginPath();
            // ctx.arc(0, 0, ROBOT_SIZE * 0.3, 0, Math.PI * 2);
            // ctx.fillStyle = '#333';
            // ctx.fill();

            ctx.restore(); // Restore context to previous state (before translate and rotate)
        }
    }

    // Target class (Enhanced drawing and state management)
    class Target {
        constructor(x, y) {
            this.position = createVector(x, y);
            this.collected = false;
             this.scale = 1; // For potential animation
             this.alpha = 1; // For potential fade
        }

        // Check if a robot is close enough to collect this target
        checkCollection(robotPosition) {
             if (this.collected) return false;
             let d = distanceBetween(this.position, robotPosition);
             if (d < TARGET_COLLECTION_RADIUS + ROBOT_SIZE / 2) { // Slightly larger collection area
                 this.collected = true;
                 // Trigger collection effect here if needed
                 return true;
             }
             return false;
        }

        draw() {
            if (this.collected) {
                 // Could add a fade-out or shrink animation here
                 // For simplicity, just don't draw if collected
                return;
            }

            ctx.save();
            ctx.translate(this.position.x, this.position.y);
            ctx.scale(this.scale, this.scale);
            ctx.globalAlpha = this.alpha;

            ctx.beginPath();
            ctx.arc(0, 0, TARGET_SIZE, 0, Math.PI * 2);
            ctx.fillStyle = '#ffc107'; // Yellow color
            ctx.shadowColor = '#ffc107';
            ctx.shadowBlur = 10; // Subtle glow effect
            ctx.fill();

            ctx.restore();
        }
    }


    // --- Simulation Setup and Loop ---

    function initSimulation() {
        robots = [];
        targets = [];
        collectedTargetCount = 0;

        // Create robots at random positions
        for (let i = 0; i < NUM_ROBOTS; i++) {
            robots.push(new Robot(
                Math.random() * canvas.width,
                Math.random() * canvas.height
            ));
        }

        // Create initial targets
        addRandomTargets(NUM_INITIAL_TARGETS);

        totalTargetCount = targets.length;
        updateScoreDisplay();
        draw(); // Initial draw
        updateButtonStates();
        displayCompletionMessage(false); // Hide any previous message
    }

    function addRandomTargets(num) {
         for (let i = 0; i < num; i++) {
             targets.push(new Target(
                Math.random() * (canvas.width - 2 * WALL_AVOIDANCE_DISTANCE) + WALL_AVOIDANCE_DISTANCE, // Prevent targets too close to edge
                Math.random() * (canvas.height - 2 * WALL_AVOIDANCE_DISTANCE) + WALL_AVOIDANCE_DISTANCE
             ));
         }
         totalTargetCount = targets.length; // Update total count
         updateScoreDisplay();
    }


    function updateSimulation() {
        if (!simulationRunning) return;

        // Find available targets (filter out collected ones)
        const availableTargets = targets.filter(target => !target.collected);

        // Update robots and apply flocking rules
        for (let robot of robots) {
            robot.flock(robots, availableTargets); // Pass only available targets
            robot.update();

            // Check for collection against available targets
             for (let i = availableTargets.length - 1; i >= 0; i--) {
                 const target = availableTargets[i];
                 if (target.checkCollection(robot.position)) {
                     collectedTargetCount++;
                     // No need to remove from availableTargets here, filter does it next frame
                     // Removing from `targets` array should happen after iterating through all robots
                 }
             }
        }

        // Remove collected targets from the main array
        targets = targets.filter(target => !target.collected);

        updateScoreDisplay();

        draw(); // Redraw the canvas

        // Check if all initial targets are collected (or just all current targets)
        // Let's check if there are ANY targets left
        const allTargetsCollected = targets.length === 0 && totalTargetCount > 0; // Check if targets array is empty AND there was at least one target initially

        if (allTargetsCollected) {
             stopSimulation();
             displayCompletionMessage(true);
        } else {
            // Loop the update
            animationFrameId = requestAnimationFrame(updateSimulation);
        }
    }

    function draw() {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw targets
        for (let target of targets) {
            target.draw();
        }

        // Draw robots
        for (let robot of robots) {
            robot.draw();
        }

         // Completion message is handled by a separate DOM element now
    }

    function updateScoreDisplay() {
        collectedCountSpan.textContent = collectedTargetCount;
        totalCountSpan.textContent = totalTargetCount;
    }

    function displayCompletionMessage(show) {
        let messageElement = document.getElementById('completion-message');
        if (show) {
            if (!messageElement) {
                 messageElement = document.createElement('div');
                 messageElement.id = 'completion-message';
                 messageElement.className = 'completion-message';
                 messageElement.textContent = 'משימה הושלמה!';
                 canvas.parentElement.style.position = 'relative'; // Make parent relative for absolute positioning
                 canvas.parentElement.appendChild(messageElement);
            } else {
                messageElement.style.display = 'block';
                 messageElement.style.animation = 'none'; // Reset animation
                void messageElement.offsetWidth; // Trigger reflow
                messageElement.style.animation = ''; // Start animation
            }
        } else {
            if (messageElement) {
                messageElement.style.display = 'none';
            }
        }
    }


    function startSimulation() {
        if (!simulationRunning) {
            simulationRunning = true;
            updateButtonStates();
            displayCompletionMessage(false); // Hide message on start
            updateSimulation(); // Start the animation loop
        }
    }

    function stopSimulation() {
        if (simulationRunning) {
            simulationRunning = false;
            cancelAnimationFrame(animationFrameId);
            updateButtonStates();
        }
    }

    function resetSimulation() {
        stopSimulation();
        initSimulation();
    }

    function updateButtonStates() {
        startButton.disabled = simulationRunning;
        stopButton.disabled = !simulationRunning;
    }

    // --- Event Listeners ---

    startButton.addEventListener('click', startSimulation);
    stopButton.addEventListener('click', stopSimulation);
    resetButton.addEventListener('click', resetSimulation);

    // Add target on canvas click
    canvas.addEventListener('click', (event) => {
        // Get click position relative to canvas
        const rect = canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        // Add a new target
        targets.push(new Target(x, y));
        totalTargetCount = targets.length;
        updateScoreDisplay();

        // If simulation was stopped and all targets were collected, clicking adds targets
        // but doesn't restart. Maybe auto-start simulation if stopped and targets are added?
        // Or only allow adding targets when simulation is stopped? Let's allow adding any time.
        // If simulation was completed, adding a target should clear the "mission complete" message.
         if (!simulationRunning && targets.length > 0) {
             displayCompletionMessage(false);
         }
        draw(); // Redraw immediately to show the new target
    });


    explanationToggle.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        explanationToggle.textContent = isHidden ? 'הסתר הסבר על נחילי רובוטים' : 'הצג/הסתר הסבר על נחילי רובוטים';
    });


    // Slider event listeners to update weights and display values
    separationSlider.addEventListener('input', (event) => {
        separationWeight = parseFloat(event.target.value);
        separationValue.textContent = separationWeight.toFixed(1);
    });
    alignmentSlider.addEventListener('input', (event) => {
        alignmentWeight = parseFloat(event.target.value);
        alignmentValue.textContent = alignmentWeight.toFixed(1);
    });
    cohesionSlider.addEventListener('input', (event) => {
        cohesionWeight = parseFloat(event.target.value);
        cohesionValue.textContent = cohesionWeight.toFixed(1);
    });
    targetSlider.addEventListener('input', (event) => {
        targetWeight = parseFloat(event.target.value);
        targetValue.textContent = targetWeight.toFixed(1);
    });
     wallAvoidanceSlider.addEventListener('input', (event) => {
        wallAvoidanceWeight = parseFloat(event.target.value);
        wallAvoidanceValue.textContent = wallAvoidanceWeight.toFixed(1);
    });


    // --- Initialization ---
    initSimulation();

</script>
```