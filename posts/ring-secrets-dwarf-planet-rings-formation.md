---
title: "סודות טבעתיים: הריקוד הכבידתי שיוצר טבעות סביב כוכבי לכת ננסיים"
english_slug: ring-secrets-dwarf-planet-rings-formation
category: "אסטרונומיה"
tags:
  - האומיה
  - טבעות פלנטריות
  - כוכב לכת ננסי
  - חגורת קויפר
  - אימפקט
  - גבול רוש
---
# סודות טבעתיים: הריקוד הכבידתי שיוצר טבעות סביב כוכבי לכת ננסיים

שבתאי גונב את ההצגה עם טבעותיו הענקיות והמרהיבות, אבל מתברר שהפלא הקוסמי הזה לא שמור רק לענקי הגז! גלו את הסוד האפלולי: גם גופים קטנטנים הרבה יותר, כמו כוכבי לכת ננסיים המקיפים את השמש הרחק בחגורת קויפר הקפואה, עשויים לענוד טבעות משלהם. איך ייתכן קסם כבידתי שכזה? אילו אירועים דרמטיים מעצבים את הנוף סביבם?

הפעילו את הסימולציה למטה כדי לחשוף את המנגנונים הפיזיקליים הנדירים שמאפשרים את היווצרות הטבעות הללו, ולהבין את ההבדל בין התנגשות קוסמית למפגש כבידתי קרוב.

<div id="simulation-container">
    <canvas id="ringSimulationCanvas" width="600" height="450"></canvas>
    <div id="controls">
        <h3>שחקו עם הקוסמוס:</h3>
        <div class="control-group">
             <label for="scenario">בחר תרחיש:</label>
             <select id="scenario">
                <option value="impact">אימפקט קוסמי (התנגשות)</option>
                <option value="flyby">מפגש כבידתי קרוב (קריעה גאותית)</option>
            </select>
        </div>


        <div id="impact-controls" class="scenario-controls control-group">
            <h4>פרמטרי אימפקט:</h4>
            <label for="impact-speed">מהירות פגיעה (יחסי):</label>
            <input type="range" id="impact-speed" min="1" max="10" value="5"><span id="impact-speed-value">5</span><br>
            <label for="impact-angle">זווית פגיעה (מעלות ממרכז):</label>
            <input type="range" id="impact-angle" min="0" max="90" value="45"><span id="impact-angle-value">45</span><br>
            <label for="impactor-mass">עוצמת הפגיעה (יחסי):</label>
            <input type="range" id="impactor-mass" min="0.5" max="3" step="0.1" value="1.5"><span id="impactor-mass-value">1.5</span><br>
        </div>

        <div id="flyby-controls" class="scenario-controls control-group" style="display:none;">
             <h4>פרמטרי מפגש:</h4>
            <label for="flyby-distance">מרחק מעבר (רדיוסים מגוף ננסי):</label>
            <input type="range" id="flyby-distance" min="1.8" max="4" step="0.1" value="2.5"><span id="flyby-distance-value">2.5</span><br>
            <label for="flyby-speed">מהירות מעבר (יחסי):</label>
            <input type="range" id="flyby-speed" min="0.8" max="4" step="0.1" value="1.5"><span id="flyby-speed-value">1.5</span><br>
            <label for="moon-size">גודל הגוף החולף (יחסי):</label>
            <input type="range" id="moon-size" min="0.2" max="1.5" step="0.1" value="0.7"><span id="moon-size-value">0.7</span><br>
        </div>
        <div class="button-group">
            <button id="runSimulation">הפעל ריקוד קוסמי!</button>
            <button id="resetSimulation">אפס</button>
        </div>
         <p id="status-message">בחרו תרחיש והפעילו סימולציה...</p>
    </div>
</div>

<button id="toggleExplanation" class="explanation-button" style="margin-top: 20px;">גלו עוד: הסבר מורחב</button>

<div id="explanation" class="explanation-box" style="display: none;">
    <h2>הסבר מורחב: הסודות מאחורי טבעות כוכבי לכת ננסיים</h2>
    <p>כוכבי לכת ננסיים כמו האומיה (Haumea) הם גופים קטנים יחסית המקיפים את השמש מעבר למסלול נפטון, באזור המכונה חגורת קויפר. הם שונים מכוכבי לכת "רגילים" בכך שלא פינו את אזור מסלולם מגופים אחרים. גילוי טבעת סביב האומיה ב-2017 היה מפתיע במיוחד, שכן עד אז חשבו שטבעות כמעט בלעדיות לענקיות הגז הגדולות.</p>

    <h3>מבנה ודינמיקה של טבעות פלנטריות</h3>
    <p>טבעות פלנטריות אינן מבנה אחיד מוצק, אלא אוסף עצום של מיליארדי חלקיקים נפרדים – החל מאבק מיקרוסקופי ועד גושי סלע וקרח בגודל בניינים קטנים. כל חלקיק כזה מקיף את כוכב הלכת במסלול משלו, והאינטראקציות הכבידתיות ביניהם ועם הירחים הסמוכים מעצבות את מבנה הטבעת, יוצרות רווחים, גלים ומבנים מורכבים אחרים.</p>

    <h3>האתגר בהיווצרות טבעות סביב גופים קטנים</h3>
    <p>ככל שכוכב הלכת קטן יותר, כך כוח המשיכה שלו חלש יותר. זה מקשה על לכידת חומר למסלול יציב סביבו, ומקשה על שמירת חומר כזה במבנה טבעתי. חלקיקים נוטים להימלט לחלל או ליפול בחזרה על פני השטח. לכן, היווצרות טבעות סביב גוף קטן כמו כוכב לכת ננסי דורשת תנאים ספציפיים ואירועים אנרגטיים.</p>

    <h3>מנגנוני היווצרות אפשריים</h3>
    <p>שני מנגנונים עיקריים נחשבים לאפשריים ליצירת טבעות סביב כוכבי לכת ננסיים:</p>
    <ul>
        <li><strong>אימפקט קטסטרופלי:</strong> התנגשות אדירה של גוף אחר (אסטרואיד או גוף חגורת קויפר קטן) עם כוכב הלכת הננסי. אנרגיית הפגיעה גורמת לפליטת כמויות גדולות של חומר מפני השטח של הגוף הננסי ושל הגוף הפוגע כאחד. חלק מהחומר הנפלט מקבל מהירות וכיוון שמאפשרים לו להיכנס למסלול סביב הגוף הננסי ולהישאר לכוד שם, בתנאי שהוא בטווח הנכון.</li>
        <li><strong>קריעה כבידתית (Tidal Disruption):</strong> ירח קטן המקיף את כוכב הלכת הננסי חודר עמוק מדי פנימה, מעבר ל'גבול רוש'. כוחות הגאות של הגוף הננסי גוברים על כוח המשיכה העצמי של הירח, וקורעים אותו לגזרים. שרידי הירח המפורק ממשיכים לנוע סביב כוכב הלכת הננסי ויוצרים טבעת.</li>
    </ul>

    <h3>גבול רוש (Roche Limit) ותפקידו</h3>
    <p>גבול רוש הוא המרחק הקריטי מכוכב לכת (או גוף מסיבי אחר), שבתוכו כוחות הגאות (ההפרש בכוח המשיכה הפועל על הצד הקרוב והצד הרחוק של גוף נלווה) חזקים יותר מכוח המשיכה הפנימי המחזיק את הגוף הנלווה (כמו ירח או אסטרואיד) יחד. אם גוף נלווה חודר לגבול רוש, הוא ייקרע לגזרים. בהקשר של טבעות, גבול רוש מסביר מדוע החלקיקים בתוך הטבעת אינם מתאחדים ומתגבשים ליצירת ירח. בתוך הגבול, כוחות הגאות של כוכב הלכת גדולים מכוחות המשיכה ההדדיים בין חלקיקי הטבעת, ומונעים מהם להתאחד.</p>

    <h3>עדויות תצפיתיות: גילוי הטבעת סביב האומיה</h3>
    <p>הטבעת של האומיה התגלתה באמצעות הסתרה (Occultation), כלומר, כאשר האומיה עבר מול כוכב רחוק. המעבר גרם לירידה קלה באור הכוכב. הנתונים הראו ירידה נוספת, קצרה יותר, באור הכוכב לפני ואחרי ההסתרה המרכזית של האומיה עצמו, מה שהצביע על נוכחות חומר נוסף סביבו – טבעת.</p>

    <h3>השוואה לטבעות של פלנטות ענקיות גזיות</h3>
    <p>הטבעות של ענקיות הגז (שבתאי, צדק, אורנוס, נפטון) ענקיות ומאסיביות הרבה יותר מאלו של כוכבי לכת ננסיים. הן מכילות הרבה יותר חומר, והכבידה החזקה של הפלנטות הענקיות מאפשרת להן ללכוד ולשמר טבעות גדולות לאורך זמן. גם מנגנוני ההיווצרות יכולים להיות שונים, כולל לכידת אסטרואידים או שביטים, או פירוק של ירחים גדולים יותר. היווצרות טבעות סביב גופים קטנים היא אירוע נדיר יותר וייתכן שהטבעות סביבם אינן יציבות לאורך זמן כמו אלו של ענקי הגז.</p>

    <h3>חשיבות המחקר</h3>
    <p>חקר טבעות סביב גופים קטנים כמו האומיה מספק תובנות חשובות על דינמיקות כבידה במערכות פלנטריות, תהליכי התנגשות ופירוק גאותי, והתנאים המאפשרים קיום מבנים טבעתיים. גילויים אלו מרחיבים את הבנתנו את המגוון והמורכבות של מערכת השמש.</p>
</div>

<style>
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        background: linear-gradient(to bottom, #0a0a1a, #1a1a2e);
        color: #e0e0e0;
        min-height: 100vh;
    }
    h1, h2, h3 {
        color: #9be8ff; /* Lighter blue for headings */
        text-align: center;
        margin-bottom: 15px;
    }
    h1 {
        font-size: 2.5em;
        margin-top: 0;
    }
     h2 {
        font-size: 1.8em;
        margin-top: 20px;
        border-bottom: 2px solid #9be8ff;
        padding-bottom: 5px;
        display: inline-block;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
     }
    h3 {
        font-size: 1.4em;
        margin-top: 15px;
        color: #a0a0ff; /* Slightly purplish blue */
    }

    #simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 30px;
        background-color: #0f0f23;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    }

    #ringSimulationCanvas {
        border: 1px solid #333;
        background-color: #000; /* Deep space black */
        margin-bottom: 20px;
        border-radius: 8px;
        box-shadow: inset 0 0 10px rgba(155, 232, 255, 0.2); /* Inner glow */
    }

    #controls {
        width: 100%;
        max-width: 550px; /* Wider controls */
        background-color: #1a1a2e;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    }

    .control-group {
        margin-bottom: 15px;
        padding-bottom: 10px;
        border-bottom: 1px dashed #333; /* Separator line */
    }
     .control-group:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
     }

    #controls label {
        display: inline-block;
        width: 220px; /* Adjust width for Hebrew text */
        margin-bottom: 8px;
        font-size: 1.1em;
        color: #b0b0b0; /* Lighter grey */
    }

    #controls input[type="range"] {
        width: calc(100% - 270px); /* Adjust width */
        margin-bottom: 8px;
        vertical-align: middle;
        -webkit-appearance: none; /* Override default chrome styles */
        appearance: none;
        height: 8px;
        background: #333;
        outline: none;
        opacity: 0.7;
        -webkit-transition: .2s;
        transition: opacity .2s;
        border-radius: 5px;
    }

    #controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: #64b5f6; /* Blue thumb */
        cursor: pointer;
        box-shadow: 0 0 5px rgba(100, 181, 246, 0.5);
    }

    #controls input[type="range"]:hover {
        opacity: 1;
    }

    #controls select {
        width: calc(100% - 230px); /* Adjust width */
        margin-bottom: 8px;
        vertical-align: middle;
        padding: 5px;
        border-radius: 5px;
        border: 1px solid #333;
        background-color: #2a2a3e;
        color: #e0e0e0;
        font-size: 1em;
        cursor: pointer;
    }
    #controls select option {
         background-color: #2a2a3e;
         color: #e0e0e0;
    }


    #controls span {
         display: inline-block;
         width: 40px;
         text-align: center;
         vertical-align: middle;
         font-weight: bold;
         color: #e0e0e0;
    }

    .button-group {
        text-align: center;
        margin-top: 20px;
    }

    #controls button {
        margin: 0 8px; /* Add space between buttons */
        padding: 12px 20px; /* Bigger buttons */
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #runSimulation {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    #runSimulation:hover {
        background-color: #45a049;
        transform: translateY(-2px);
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    #resetSimulation {
        background-color: #f44336; /* Red */
        color: white;
    }
     #resetSimulation:hover {
        background-color: #d32f2f;
        transform: translateY(-2px);
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    #status-message {
        margin-top: 15px;
        text-align: center;
        min-height: 1.5em; /* Reserve space */
        font-size: 1.1em;
        color: #ffeb3b; /* Yellowish */
        font-weight: bold;
    }

    .explanation-button {
        display: block;
        margin: 30px auto 20px auto;
        padding: 12px 25px;
        background-color: #008CBA; /* Blue */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.2em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }
    .explanation-button:hover {
        background-color: #007bb5;
        transform: translateY(-2px);
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .explanation-box {
        margin-top: 20px;
        padding: 25px;
        background-color: #0f0f23;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    }
    .explanation-box h2, .explanation-box h3 {
        color: #9be8ff;
    }
    .explanation-box p {
        margin-bottom: 15px;
        color: #d0d0d0; /* Slightly lighter text in explanation */
    }
    .explanation-box ul {
        list-style-type: disc;
        margin-left: 30px;
        padding-left: 0;
        color: #d0d0d0;
    }
    .explanation-box li {
        margin-bottom: 8px;
    }

    /* Subtle particle colors for visual differentiation */
    .particle-color-escaping { color: rgba(255, 100, 100, 0.7); } /* Reddish */
    .particle-color-falling { color: rgba(255, 180, 80, 0.7); } /* Orange/Yellow */
    .particle-color-ring { color: rgba(100, 200, 255, 0.8); } /* Bluish/Cyan */

</style>

<script>
    const canvas = document.getElementById('ringSimulationCanvas');
    const ctx = canvas.getContext('2d');
    const scenarioSelect = document.getElementById('scenario');
    const impactControls = document.getElementById('impact-controls');
    const flybyControls = document.getElementById('flyby-controls');
    const impactSpeedInput = document.getElementById('impact-speed');
    const impactAngleInput = document.getElementById('impact-angle');
    const impactorMassInput = document.getElementById('impactor-mass');
    const impactSpeedValueSpan = document.getElementById('impact-speed-value');
    const impactAngleValueSpan = document.getElementById('impact-angle-value');
    const impactorMassValueSpan = document.getElementById('impactor-mass-value');
    const flybyDistanceInput = document.getElementById('flyby-distance');
    const flybySpeedInput = document.getElementById('flyby-speed');
    const moonSizeInput = document.getElementById('moon-size'); // Renamed from moon-mass for visual focus
    const flybyDistanceValueSpan = document.getElementById('flyby-distance-value');
    const flybySpeedValueSpan = document.getElementById('flyby-speed-value');
    const moonSizeValueSpan = document.getElementById('moon-size-value');
    const runButton = document.getElementById('runSimulation');
    const resetButton = document.getElementById('resetSimulation');
    const statusMessage = document.getElementById('status-message');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    // Constants and simulation parameters (scaled for visualization)
    const DWARF_PLANET_RADIUS = 50; // pixels (slightly larger for better visual)
    const DWARF_PLANET_MASS = 5000; // increased mass for stronger gravity
    const G = 1; // gravitational constant (arbitrary)
    // Roche Limit Calculation: simplified for visualization. Actual Roche Limit depends on density ratio.
    // Approx formula: d = R * (2 * rho_planet / rho_moon)^(1/3)
    // We'll use a base factor and scale it slightly with 'moon-size' (as a proxy for density/cohesion)
    const BASE_ROCHE_FACTOR = 2.5;
    let ROCHE_LIMIT_RADIUS;

    const PARTICLE_SIZE = 1.8; // Slightly larger particles
    const MAX_PARTICLES = 300; // More particles
    let particles = [];
    let simulationRunning = false;
    let animationFrameId = null;
    let flybyBody = null; // For flyby scenario visualization

    // Calculate Roche Limit radius for visualization
    function calculateRocheLimitRadius(moonRelativeSize = 1) {
         // Simulate lower effective cohesion/higher density ratio for larger 'moon'
         // This is a simplification; actual Roche limit depends on material properties
         const cohesionFactor = 1.0 / Math.max(0.1, moonRelativeSize * 0.8); // Stronger cohesion for smaller "moons"
         ROCHE_LIMIT_RADIUS = DWARF_PLANET_RADIUS * BASE_ROCHE_FACTOR * cohesionFactor;
         // Clamp Roche limit to a reasonable visual range
         ROCHE_LIMIT_RADIUS = Math.max(DWARF_PLANET_RADIUS * 1.5, Math.min(ROCHE_LIMIT_RADIUS, canvas.width / 2 * 0.9));
    }

    // Update parameter value displays
    impactSpeedInput.oninput = () => impactSpeedValueSpan.textContent = impactSpeedInput.value;
    impactAngleInput.oninput = () => impactAngleValueSpan.textContent = impactAngleInput.value;
    impactorMassInput.oninput = () => impactorMassValueSpan.textContent = impactorMassInput.value;
    flybyDistanceInput.oninput = () => flybyDistanceValueSpan.textContent = flybyDistanceInput.value;
    flybySpeedInput.oninput = () => flybySpeedValueSpan.textContent = flybySpeedInput.value;
    moonSizeInput.oninput = () => moonSizeValueSpan.textContent = moonSizeInput.value;

    // Toggle controls based on scenario
    scenarioSelect.onchange = () => {
        if (scenarioSelect.value === 'impact') {
            impactControls.style.display = 'block';
            flybyControls.style.display = 'none';
        } else {
            impactControls.style.display = 'none';
            flybyControls.style.display = 'block';
        }
        resetSimulation(); // Reset simulation when changing scenario
    };

    // Particle class (with minor enhancements)
    class Particle {
        constructor(x, y, vx, vy, color = 'rgba(200,200,200,0.7)', initialAlpha = 1) {
            this.x = x;
            this.y = y;
            this.vx = vx;
            this.vy = vy;
            this.color = color;
            this.alpha = initialAlpha; // For fading effects
            this.isRingCandidate = false; // Flag to indicate potential ring particle
        }

        update() {
            // Calculate gravity from dwarf planet (at origin 0,0 relative to canvas center)
            const dx = -this.x; // Physics origin is center of canvas
            const dy = -this.y;
            const distSq = dx * dx + dy * dy;
            const dist = Math.sqrt(distSq);

            // Simple inverse square law gravity
             if (dist > DWARF_PLANET_RADIUS + PARTICLE_SIZE/2) { // Avoid division by zero or extremely strong forces / hitting planet
                const force = (G * DWARF_PLANET_MASS) / distSq;
                const ax = (force * dx) / dist;
                const ay = (force * dy) / dist;

                this.vx += ax;
                this.vy += ay;
            } else {
                // Particle hit the dwarf planet
                 return false; // Indicate particle should be removed
            }


            this.x += this.vx;
            this.y += this.vy;

            // Check if particle is potentially in a stable orbit/ring area
            // This is a simplified check based on distance and velocity magnitude (conceptually)
            const speedSq = this.vx * this.vx + this.vy * this.vy;
            // Escape velocity squared: v_esc^2 = 2*G*M/r
            // Orbital velocity squared (circular): v_orb^2 = G*M/r
            const escapeSpeedSq = 2 * G * DWARF_PLANET_MASS / dist; // approx escape speed

            if (dist >= DWARF_PLANET_RADIUS && dist <= ROCHE_LIMIT_RADIUS) {
                 // Within Roche limit and outside planet
                 this.isRingCandidate = true;
                 // Potentially fade out if speed is too high (escaping)
                 if (speedSq > escapeSpeedSq * 0.95) { // Slightly less than escape velocity to fade potential escapers
                    this.alpha -= 0.005; // Start fading out
                 } else {
                     this.alpha = Math.min(1, this.alpha + 0.01); // Fade in/maintain opacity if stable-ish
                 }
                  // If clearly bound and within Roche, make it brighter
                 if (speedSq < escapeSpeedSq * 0.8) {
                     this.color = 'rgba(100, 200, 255, ' + this.alpha + ')'; // Ring color
                 } else {
                      this.color = 'rgba(150, 180, 255, ' + this.alpha + ')'; // Potentially escaping/falling within Roche
                 }

            } else if (dist < DWARF_PLANET_RADIUS) {
                // Inside dwarf planet (should have been caught by the hit check, but safety)
                 return false;
            }
            else { // Outside Roche limit or inside planet
                 this.isRingCandidate = false;
                 this.alpha -= 0.01; // Fade out particles outside the 'action' zone

                 // Differentiate color for escaping vs. falling back from far
                 if (speedSq > escapeSpeedSq * 1.05) { // Clearly escaping
                      this.color = 'rgba(255, 100, 100, ' + this.alpha + ')'; // Reddish escaping color
                 } else { // Falling back or unbound far away
                      this.color = 'rgba(255, 180, 80, ' + this.alpha + ')'; // Orange/Yellow unbound color
                 }
            }


            // Remove particle if too far or completely faded
            if (Math.abs(this.x) > canvas.width / 2 + 50 || Math.abs(this.y) > canvas.height / 2 + 50 || this.alpha <= 0) {
                 return false; // Indicate particle should be removed
            }

            return true; // Indicate particle is still active
        }

        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            // Draw relative to canvas center
            ctx.arc(this.x, this.y, PARTICLE_SIZE, 0, Math.PI * 2);
            ctx.fill();
        }
    }

     // Flyby Body class (simplified visual representation)
    class FlybyBody {
        constructor(x, y, vx, vy, size, color = '#cccccc') {
            this.x = x;
            this.y = y;
            this.vx = vx;
            this.vy = vy;
            this.size = size; // Relative size, affects visual radius and possibly breakup behavior
            this.color = color;
            this.shattered = false;
            this.alpha = 1; // For fading after shattering
        }

        update() {
             if (this.shattered) {
                this.alpha -= 0.02; // Fade out shattered body representation
                return this.alpha > 0; // Remove when faded
             }

            // Check distance to dwarf planet
            const dx = -this.x;
            const dy = -this.y;
            const dist = Math.sqrt(dx*dx + dy*dy);

            // Simple movement (assuming linear path for visualization before breakup)
             this.x += this.vx;
             this.y += this.vy;

            // Check for breakup condition (crosses Roche Limit)
            // We shatter it slightly *before* the strict calculated limit for visual effect
            if (dist <= ROCHE_LIMIT_RADIUS * 1.05 && !this.shattered) {
                this.shatter();
            }

             // Remove if too far off-screen after shattering
             if (this.shattered && (Math.abs(this.x) > canvas.width / 2 + 100 || Math.abs(this.y) > canvas.height / 2 + 100) ) {
                 return false;
             }


            return true; // Still active
        }

        shatter() {
            this.shattered = true;
            // Generate particles at the current location with inherited velocity + scatter
            const numBreakupParticles = Math.floor(MAX_PARTICLES / 3 * this.size); // More particles for larger body
            const breakupSpeed = Math.sqrt(this.vx*this.vx + this.vy*this.vy) * 0.2; // Scatter speed relative to flyby speed

            for (let i = 0; i < numBreakupParticles; i++) {
                 const scatterAngle = Math.random() * Math.PI * 2;
                 const p_vx = this.vx * 0.5 + breakupSpeed * Math.cos(scatterAngle) * (0.5 + Math.random()); // Inherit some bulk velocity
                 const p_vy = this.vy * 0.5 + breakupSpeed * Math.sin(scatterAngle) * (0.5 + Math.random()); // Inherit some bulk velocity

                 // Start particles slightly scattered around the breakup point
                 const startScatter = this.size * 5; // Scatter range based on moon size
                 const p_x = this.x + (Math.random() - 0.5) * startScatter;
                 const p_y = this.y + (Math.random() - 0.5) * startScatter;


                 particles.push(new Particle(p_x, p_y, p_vx, p_vy, 'rgba(180, 180, 180, 0.8)')); // Breakup particle color
             }
             statusMessage.textContent = "קריעה גאותית מתרחשת! פיזור חלקיקים...";
        }

        draw() {
             if (this.shattered) {
                 // Draw a fading visual of the shattered body? Or just let particles take over.
                 // For now, just don't draw the main body once shattered.
                 return;
             }
            ctx.fillStyle = this.color;
            ctx.beginPath();
            // Draw relative to canvas center
            ctx.arc(this.x, this.y, this.size * DWARF_PLANET_RADIUS * 0.4, 0, Math.PI * 2); // Visual size relative to DP
            ctx.fill();
        }
    }


    function resetSimulation() {
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }
        particles = [];
        flybyBody = null;
        simulationRunning = false;
        draw(); // Draw initial state (dwarf planet only)
        statusMessage.textContent = "בחרו תרחיש והפעילו סימולציה...";
    }

    function runSimulation() {
        resetSimulation(); // Ensure clean start
        simulationRunning = true;

        const scenario = scenarioSelect.value;

        if (scenario === 'impact') {
            const speed = parseFloat(impactSpeedInput.value);
            const angleDeg = parseFloat(impactAngleInput.value);
            const impactorMass = parseFloat(impactorMassInput.value);
            const angleRad = angleDeg * Math.PI / 180; // Angle relative to horizontal, 0 is right

            calculateRocheLimitRadius(); // Calculate even for impact, it's the target zone

            // Determine impact location on the dwarf planet edge based on angle
            const impactX = DWARF_PLANET_RADIUS * Math.cos(angleRad + Math.PI); // Start opposite side
            const impactY = DWARF_PLANET_RADIUS * Math.sin(angleRad + Math.PI);

            statusMessage.textContent = "סימולציית אימפקט: עומד לפגוע...";

             // Simulate impact effect after a short delay or animation
            setTimeout(() => {
                // Generate debris from the impact site
                const numEjectedParticles = Math.floor(MAX_PARTICLES * (0.5 + impactorMass * 0.2)); // More particles for larger impactor
                const baseEjectionSpeed = speed * 5; // Scale ejection speed

                for (let i = 0; i < numEjectedParticles; i++) {
                    // Eject particles from near the impact site
                    const startOffsetAngle = angleRad + Math.PI; // Angle of impact site from center
                    const startOffsetDistance = DWARF_PLANET_RADIUS + Math.random() * 5; // Start just outside planet
                    const startX = startOffsetDistance * Math.cos(startOffsetAngle);
                    const startY = startOffsetDistance * Math.sin(startOffsetAngle);

                    // Ejection velocity: outwards from impact site with variations
                    const ejectionAngleSpread = Math.PI * (0.5 + (1 - impactorMass/3)); // Wider spread for less massive/faster impacts? Or simpler: fixed spread
                    const ejectionAngle = startOffsetAngle + (Math.random() - 0.5) * ejectionAngleSpread; // Eject outwards

                    const ejectionSpeed = baseEjectionSpeed * (0.5 + Math.random() * 0.8); // Vary speed

                    const vx = ejectionSpeed * Math.cos(ejectionAngle);
                    const vy = ejectionSpeed * Math.sin(ejectionAngle);

                    particles.push(new Particle(startX, startY, vx, vy, 'rgba(220, 220, 220, 0.9)'));
                }
                 statusMessage.textContent = "אימפקט! פיזור חלקיקים...";
            }, 500); // Small delay to simulate impact event

        } else if (scenario === 'flyby') {
            const flybyDistance = parseFloat(flybyDistanceInput.value) * DWARF_PLANET_RADIUS;
            const initialFlybySpeedFactor = parseFloat(flybySpeedInput.value);
            const moonRelativeSize = parseFloat(moonSizeInput.value);

            calculateRocheLimitRadius(moonRelativeSize);

            // Set initial position and velocity for the flyby body (or particle cluster)
            const startX = -canvas.width / 2 - 50; // Start off-screen left
            const pathY = -flybyDistance;    // Path is horizontal at this Y coordinate (relative to center)

             // Calculate base speed needed for a roughly parabolic trajectory at flyby distance
            // v_parabolic = sqrt(2 * G * M / r)
            const baseSpeed = Math.sqrt(2 * G * DWARF_PLANET_MASS / Math.abs(pathY)); // Use absolute pathY as distance

            const initialFlybySpeed = initialFlybySpeedFactor * baseSpeed; // Scale speed

            flybyBody = new FlybyBody(startX, pathY, initialFlybySpeed, 0, moonRelativeSize);

             statusMessage.textContent = "סימולציית קריעה גאותית: גוף מתקרב...";
        }

        // Start the main animation loop
        updateAndDraw();
    }

    function updateAndDraw() {
        if (!simulationRunning) return;

        // Clear canvas
        ctx.fillStyle = '#000';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Translate context so origin 0,0 is center
        ctx.save();
        ctx.translate(canvas.width / 2, canvas.height / 2);

        // Draw Roche Limit (dashed circle)
        ctx.beginPath();
        ctx.arc(0, 0, ROCHE_LIMIT_RADIUS, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(255, 0, 0, 0.6)'; /* More prominent red */
        ctx.setLineDash([8, 8]); // Larger dashes
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.setLineDash([]); // Reset line dash
        ctx.lineWidth = 1;

         // Draw faint text for Roche Limit
         const rocheText = "גבול רוש";
         ctx.fillStyle = 'rgba(255, 0, 0, 0.5)';
         ctx.font = '12px Arial';
         ctx.textAlign = 'center';
         ctx.fillText(rocheText, 0, -ROCHE_LIMIT_RADIUS - 10);


        // Draw Dwarf Planet
        ctx.fillStyle = '#8b4513'; // Brownish color
        ctx.beginPath();
        ctx.arc(0, 0, DWARF_PLANET_RADIUS, 0, Math.PI * 2);
        ctx.fill();
         // Add a subtle glow or detail to DP
        ctx.shadowBlur = 20;
        ctx.shadowColor = 'rgba(255, 150, 0, 0.4)'; /* Orange glow */
        ctx.fillStyle = '#a0522d'; /* Slightly lighter fill */
        ctx.beginPath();
        ctx.arc(0, 0, DWARF_PLANET_RADIUS - 3, 0, Math.PI * 2);
        ctx.fill();
         ctx.shadowBlur = 0; // Reset shadow

        // Update and draw flyby body
        if (flybyBody) {
            const isActive = flybyBody.update();
            if (isActive) {
                flybyBody.draw();
            } else {
                flybyBody = null; // Remove flyby body if inactive
            }
        }


        // Update and draw particles
        const activeParticles = [];
        let particlesInRingZoneCount = 0; // Particles within Roche limit AND potentially bound
        for (const particle of particles) {
            const isAlive = particle.update();
            if (isAlive) {
                particle.draw();
                 if (particle.isRingCandidate && particle.alpha > 0.5) { // Count particles that are in the zone and visible
                     particlesInRingZoneCount++;
                 }
                activeParticles.push(particle);
            }
        }
        particles = activeParticles;

         // Update status message based on particle count in the ring zone
         if (simulationRunning) {
             if (particles.length === 0 && !flybyBody) {
                 statusMessage.textContent = "הסימולציה הסתיימה. אין חלקיקים במסלול.";
             } else if (particlesInRingZoneCount > MAX_PARTICLES * 0.2) { // Arbitrary threshold for "ring forming"
                  statusMessage.textContent = `טבעת נוצרת! ${particlesInRingZoneCount} חלקיקים בטווח גבול רוש.`;
                  statusMessage.style.color = '#aaffaa'; /* Greenish */
             } else if (particles.length < MAX_PARTICLES * 0.1 && !flybyBody) {
                  statusMessage.textContent = `הסימולציה הסתיימה. מעט חלקיקים נלכדו.`;
                   statusMessage.style.color = '#ffeb3b'; /* Yellowish */
             } else {
                  statusMessage.textContent = ` ${particlesInRingZoneCount} חלקיקים בטווח גבול רוש. סך הכל: ${particles.length} חלקיקים פעילים.`;
                  statusMessage.style.color = '#ffeb3b'; /* Yellowish */
             }
         }


        // Restore context translation
        ctx.restore();

        // Continue animation loop only if particles or flyby body exist or simulation is waiting for impact delay
        if (particles.length > 0 || flybyBody || (scenarioSelect.value === 'impact' && particles.length === 0)) {
             animationFrameId = requestAnimationFrame(updateAndDraw);
        } else {
             simulationRunning = false; // Stop animation loop if no particles or flyby body left
        }

    }

    // Initial draw (just the dwarf planet)
    function draw() {
         // Clear canvas
        ctx.fillStyle = '#000';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Translate context so origin 0,0 is center
        ctx.save();
        ctx.translate(canvas.width / 2, canvas.height / 2);

        // Draw Dwarf Planet
        ctx.fillStyle = '#8b4513';
        ctx.beginPath();
        ctx.arc(0, 0, DWARF_PLANET_RADIUS, 0, Math.PI * 2);
        ctx.fill();
         // Add subtle glow
        ctx.shadowBlur = 20;
        ctx.shadowColor = 'rgba(255, 150, 0, 0.4)';
        ctx.fillStyle = '#a0522d';
        ctx.beginPath();
        ctx.arc(0, 0, DWARF_PLANET_RADIUS - 3, 0, Math.PI * 2);
        ctx.fill();
         ctx.shadowBlur = 0;

         // Draw Roche Limit placeholder? Or just show DP
         // Let's just show DP initially
        ctx.restore();
        statusMessage.textContent = "בחרו תרחיש והפעילו סימולציה...";
    }

    // Event Listeners
    runButton.addEventListener('click', runSimulation);
    resetButton.addEventListener('click', resetSimulation);
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'גלו עוד: הסבר מורחב';
         // Scroll to explanation if revealing
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth' });
         }
    });

    // Initial setup
    draw(); // Draw the dwarf planet on load
    scenarioSelect.dispatchEvent(new Event('change')); // Trigger initial control display
    calculateRocheLimitRadius(parseFloat(moonSizeInput.value)); // Calculate initial Roche limit based on default flyby parameters

</script>
---