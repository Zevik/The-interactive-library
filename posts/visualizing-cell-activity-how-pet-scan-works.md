---
title: "פענוח הגוף: מסע ויזואלי אל תוך סודות ה-PET סקאן"
english_slug: visualizing-cell-activity-how-pet-scan-works
category: "רפואה"
tags:
  - PET סקאן
  - דימות גרעיני
  - מטבוליזם תאי
  - רפואה גרעינית
  - גילוי ואבחון סרטן
  - הדמיה פונקציונלית
---
# פענוח הגוף: מסע ויזואלי אל תוך סודות ה-PET סקאן

האם אי פעם תהיתם איך רופאים יכולים "לראות" אילו תאים בגוף שלכם עובדים קשה במיוחד? לא רק לראות את הצורה של איבר, אלא להבין את ה"שיחות" הביולוגיות שמתרחשות בתוכו? הצטרפו למסע ויזואלי שמגלה את הקסם מאחורי טכנולוגיית ה-PET סקאן, ומראה כיצד אנו יכולים לאתר אזורים חריגים בגוף על בסיס הפעילות הביוכימית שלהם.

<div id="pet-simulation">
    <div id="scan-area">
        <div id="body">
            <div id="hot-spot"></div>
        </div>
        <div id="scanner-ring"></div>
         <div id="detectors"></div> <!-- Container for dynamic detectors -->
        <div id="tracer-particles"></div>
        <div id="detection-lines-container"></div>
         <div id="reconstruction-overlay"></div> <!-- For reconstruction visualization -->
    </div>
    <div id="simulation-controls">
        <button id="reset-simulation" class="sim-button">התחל מחדש</button>
        <button id="next-step" class="sim-button">הצעד הבא</button>
        <span id="current-step-text" class="step-text">מוכנים למסע? לחצו 'הצעד הבא'!</span>
    </div>
</div>

<button id="toggle-explanation" class="explanation-button">הצג/הסתר את הסיפור המלא (הסבר מפורט)</button>

<div id="detailed-explanation" style="display: none;">
    <h2>מהו PET סקאן ולמה הוא כמו "מצלמת מטבוליזם"?</h2>
    <p>PET (Positron Emission Tomography) סקאן היא טכניקת דימות רפואי פורצת דרך, המאפשרת לנו "לראות" את התהליכים הביוכימיים המתרחשים בתוך תאי הגוף. בניגוד לטכניקות דימות סטנדרטיות כמו רנטגן או CT, המתמקדות בצורת האיברים והמבנים, PET מתמקד בפונקציה - בפעילות המטבולית של התאים. דמיינו שבמקום מפת דרכים (מבנה), אתם מקבלים מפה של עומסי תנועה ופעילות (מטבוליזם).</p>

    <h2>ה"גשש" המולקולרי: הסמן הרדיואקטיבי</h2>
    <p>כדי שנוכל לעקוב אחר פעילות התאים, אנו משתמשים ב"גשש" מיוחד - חומר סמן (Tracer). זהו לרוב מולקולה ביולוגית שהגוף מכיר ומשתמש בה, כמו מולקולת סוכר (גלוקוז), אליה מצורף אטום רדיואקטיבי בעל אורך חיים קצר. הסמן הנפוץ ביותר נקרא FDG (Fluorodeoxyglucose). התאים בגוף משתמשים בגלוקוז לאנרגיה, ולכן FDG מתנהג דומה לגלוקוז רגיל, אך האטום הרדיואקטיבי (פלואור-18) מאפשר לנו לעקוב אחריו.</p>

    <h2>מרוץ הסמן והצטברותו ב"מוקדים חמים"</h2>
    <p>לאחר הזרקת הסמן לוריד, הוא מתפזר במהירות דרך מחזור הדם לכל חלקי הגוף. תאים פעילים במיוחד - כמו תאי סרטן הגדלים במהירות, תאי מוח חושבים, או תאי שריר בפעולה - צורכים הרבה יותר סוכר מאשר תאים רגילים. כתוצאה מכך, הם "בולעים" כמויות גדולות יותר של FDG מהסביבה. הסמן מצטבר בריכוזים גבוהים באזורים אלו, שהופכים ל"מוקדים חמים" (Hot Spots) מבחינה מטבולית.</p>

    <h2>האירוע הקוונטי: פליטת פוזיטרון ו"התאבדות"</h2>
    <p>האטום הרדיואקטיבי בסמן (כמו F-18) אינו יציב. הוא עובר תהליך טבעי של דעיכה רדיואקטיבית, במהלכו הוא פולט חלקיק קטן בשם פוזיטרון (positron). פוזיטרון הוא למעשה "אנטי-אלקטרון" - חלקיק עם מסה זהה לאלקטרון, אך עם מטען חשמלי חיובי. הפוזיטרון שנוצר נע מרחק קצר מאוד ברקמה (מילימטרים ספורים) עד שהוא פוגש אלקטרון. כשהם נפגשים, הם מחסלים זה את זה בתהליך מרהיב שנקרא "התאבדות" (annihilation). המסה של שני החלקיקים הופכת כולה לאנרגיה, שמשתחררת בצורה של שני פוטונים (חלקיקי אור אנרגטיים, במקרה זה קרני גמא). ההיבט הקריטי הוא ששני הפוטונים הללו נפלטים תמיד בכיוונים מנוגדים לחלוטין, בזווית של 180 מעלות!</p>

    <h2>הגלאים עובדים: קליטת הפוטונים וזיהוי "הקווים"</h2>
    <p>זה השלב בו סורק ה-PET נכנס לפעולה. הסורק הוא טבעת גדולה המצופה באלפי גלאים רגישים. כאשר שני פוטונים שנפלטו באותה "התאבדות" פוגעים בשני גלאים הנמצאים בדיוק בצדדים הנגדיים של הטבעת, ובאותו רגע ממש (או בהפרש זמן זעיר מאוד), הסורק מזהה את זה כ"אירוע זוגי". המחשב יודע כעת שאירוע ההתאבדות, שהוליד את זוג הפוטונים הללו, התרחש היכן שהוא לאורך הקו הישר המחבר את שני הגלאים שקלטו אותם.</p>

    <h2>הפיכת נקודות אור לתמונה: שחזור המפה</h2>
    <p>הסורק אוסף מיליוני ואף מיליארדי אירועים זוגיים כאלה מכל הכיוונים מסביב לגוף. דמיינו רשת של קווים רבים הנמתחים בין זוגות גלאים מנוגדים. היכן שקווים רבים מצטלבים או מתרכזים - זהו האזור שבו התרחשו הכי הרבה אירועי "התאבדות" פוזיטרונים. המחשב, באמצעות אלגוריתמים מתמטיים מתוחכמים (כמו שחזור איטרטיבי), משתמש בכל הקווים הללו כדי לבנות מפה תלת-ממדית מדויקת של פיזור הסמן בגוף. האזורים ה"חמים" - בהם הסמן הצטבר הכי הרבה - מופיעים בתמונה כנקודות בהירות או אדומות, המצביעות על פעילות מטבולית גבוהה.</p>

    <h2>PET סקאן בשירות הרפואה: למה זה חשוב?</h2>
    <p>היכולת לראות פעילות מטבולית פותחת דלתות לאבחון וטיפול מדויקים יותר. השימוש הנפוץ ביותר ב-PET סקאן (לרוב בשילוב עם CT או MRI לקבלת מידע מבני) הוא ברפואת הסרטן: איתור גידולים (שלעיתים קרובות צורכים גלוקוז בשיעור גבוה), קביעת שלב המחלה, מעקב אחר יעילות טיפול, ואיתור חזרות של המחלה. בנוסף, PET משמש לאבחון מחלות נוירולוגיות כמו אלצהיימר (עם סמנים ספציפיים), איתור מוקדים אפילפטיים, הערכת מחלות לב ועוד. הוא מאפשר לרופאים לקבל תמונה פונקציונלית של הגוף, המשלימה את המידע המבני ומסייעת בקבלת החלטות קליניות קריטיות.</p>
</div>

<style>
/* Enhanced Design & Animations */
#pet-simulation {
    position: relative;
    width: 100%; /* Make it more responsive */
    max-width: 600px; /* Max width for large screens */
    height: 500px; /* Increased height */
    margin: 40px auto; /* More margin */
    border: 1px solid #e0e0e0;
    background: linear-gradient(to bottom, #f8f8f8, #e8e8e8); /* Subtle gradient */
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    font-family: 'Arial', sans-serif; /* Better font */
}

#scan-area {
    position: absolute;
    top: 20px; /* Space for controls */
    bottom: 70px; /* Space for controls */
    left: 20px;
    right: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative; /* Needed for absolute children */
}


#body {
    position: absolute;
    width: 180px; /* Slightly larger body */
    height: 300px; /* Slightly larger body */
    background-color: #e0bfa5; /* Softer skin tone */
    border-radius: 90px / 150px; /* Oval shape */
    border: 2px solid #c29d84;
    z-index: 2;
     box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* Inner shadow */
}

#hot-spot {
    position: absolute;
    top: 35%; /* Example position */
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50px; /* Larger hot spot */
    height: 50px;
    background-color: rgba(255, 50, 50, 0.6); /* More vibrant red */
    border-radius: 50%;
    border: 2px dashed rgba(255, 0, 0, 0.8);
    display: none; /* Initially hidden */
    z-index: 4; /* Above particles */
    transition: all 0.5s ease-in-out; /* Smooth size/color changes */
}

#scanner-ring {
    position: absolute;
    width: 500px; /* Larger ring */
    height: 400px;
    border: 25px solid rgba(30, 144, 255, 0.3); /* DodgerBlue with transparency */
    border-radius: 50%;
    box-sizing: border-box;
    z-index: 1;
     pointer-events: none; /* Don't block clicks */
     animation: rotateScan 30s linear infinite; /* Subtle continuous rotation */
}

@keyframes rotateScan {
    from { transform: translate(-50%, -50%) rotate(0deg); }
    to { transform: translate(-50%, -50%) rotate(360deg); }
}

/* Position scanner ring relative to scan-area center */
#scan-area > #scanner-ring {
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(0deg); /* Reset initial transform */
}


#detectors {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 500px; /* Match ring size */
    height: 400px;
    border-radius: 50%;
    z-index: 3; /* Between body and lines */
    pointer-events: none;
}

.detector {
    position: absolute;
    width: 8px; /* Larger detectors */
    height: 15px;
    background-color: rgba(0, 150, 0, 0.4); /* Dim green when inactive */
    border-radius: 3px;
    opacity: 0; /* Initially hidden */
    transition: background-color 0.1s ease-out; /* Fast flash effect */
}

.detector.hit {
     background-color: yellow !important; /* Bright yellow flash */
}


#tracer-particles {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: 4; /* Above body */
    pointer-events: none;
}

.tracer {
    position: absolute;
    width: 5px; /* Slightly larger particles */
    height: 5px;
    background-color: #ff8c00; /* Dark orange */
    border-radius: 50%;
    opacity: 0; /* Initially hidden */
     transition: all 0.5s linear; /* Default smooth transition */
}

.tracer.injecting {
    transition: all 0.8s ease-out;
    opacity: 1;
}

.tracer.diffusing {
    transition: all 3s linear; /* Slower diffusion */
    opacity: 0.7;
}

.tracer.accumulated {
    background-color: #ff4500; /* Red-orange for accumulated */
     transition: all 0.5s ease-in; /* Faster move to hotspot */
    opacity: 0.9;
}


#detection-lines-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%); /* Center the container */
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 5; /* Above body and hot spot */
    overflow: hidden;
}

.detection-line {
    position: absolute;
    width: 0px; /* Start with zero width */
    height: 3px; /* Thicker line */
    background-color: #ffff00; /* Bright yellow */
    opacity: 0.9;
    transform-origin: 0 0;
    display: none; /* Initially hidden */
     transition: width 0.5s linear; /* Animation for line growth */
}

#reconstruction-overlay {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 180px;
    height: 300px; /* Match body size */
    border-radius: 90px / 150px;
    z-index: 6; /* Above everything else in scan area */
    pointer-events: none;
    background: radial-gradient(circle at 50% 35%, rgba(255,0,0,0.3) 0%, rgba(255,0,0,0) 70%); /* Subtle heatmap */
    opacity: 0;
    transition: opacity 1s ease-in-out;
}


#simulation-controls {
    position: absolute;
    bottom: 10px;
    left: 10px;
    right: 10px;
    display: flex; /* Use flexbox for layout */
    justify-content: center; /* Center items */
    align-items: center;
    z-index: 10;
    padding: 10px;
    background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background */
    border-radius: 5px;
}

.sim-button {
    margin: 0 10px; /* More space between buttons */
    padding: 10px 20px; /* Larger padding */
    font-size: 1rem;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    background-color: #007bff; /* Primary blue */
    color: white;
    transition: background-color 0.2s ease, transform 0.1s ease;
}

.sim-button:hover {
    background-color: #0056b3;
}

.sim-button:active {
    transform: scale(0.98);
}

.sim-button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
}

.step-text {
    margin-left: 15px;
    font-size: 1rem;
    color: #333;
    font-weight: bold;
}

.explanation-button {
    display: block; /* Full width button below simulation */
    width: max-content;
    margin: 20px auto; /* Center button */
    padding: 10px 20px;
    font-size: 1rem;
    cursor: pointer;
    border: 1px solid #007bff;
    border-radius: 5px;
    background-color: #f8f9fa;
    color: #007bff;
    transition: background-color 0.2s ease, color 0.2s ease;
}

.explanation-button:hover {
    background-color: #e9ecef;
}


#detailed-explanation {
    margin: 20px auto; /* Center explanation */
    max-width: 800px; /* Max width for readability */
    padding: 20px;
    border: 1px solid #ddd;
    background-color: #f9f9f9;
    border-radius: 8px;
    line-height: 1.6; /* Improved readability */
    color: #333;
}

#detailed-explanation h2 {
    margin-top: 0;
    color: #0056b3; /* Darker blue for headers */
    border-bottom: 2px solid #007bff; /* Underline headers */
    padding-bottom: 5px;
    margin-bottom: 15px;
}

#detailed-explanation p {
    margin-bottom: 15px;
}

/* Keyframes for additional animations */
@keyframes flashYellow {
    from { background-color: rgba(0, 150, 0, 0.4); }
    to { background-color: yellow; }
}

@keyframes pulseHotSpot {
    0% { transform: translate(-50%, -50%) scale(1); opacity: 0.9; }
    50% { transform: translate(-50%, -50%) scale(1.1); opacity: 1; }
    100% { transform: translate(-50%, -50%) scale(1); opacity: 0.9; }
}

</style>

<script>
const simContainer = document.getElementById('pet-simulation');
const scanArea = document.getElementById('scan-area'); // New container for relative positioning
const body = document.getElementById('body');
const hotSpot = document.getElementById('hot-spot');
const scannerRing = document.getElementById('scanner-ring');
const detectorsContainer = document.getElementById('detectors'); // New container for detectors
const tracerParticlesContainer = document.getElementById('tracer-particles');
const detectionLinesContainer = document.getElementById('detection-lines-container');
const reconstructionOverlay = document.getElementById('reconstruction-overlay'); // New overlay
const nextStepBtn = document.getElementById('next-step');
const resetBtn = document.getElementById('reset-simulation');
const stepText = document.getElementById('current-step-text');
const toggleExplanationBtn = document.getElementById('toggle-explanation');
const explanationDiv = document.getElementById('detailed-explanation');

let currentStep = 0;
const steps = [
    "מוכנים למסע? לחצו 'הצעד הבא'!", // Initial State (Step 0)
    "שלב 1: הזרקת ה'גשש' (סמן רדיואקטיבי)",
    "שלב 2: פיזור הסמן בגוף וקליטתו בתאים פעילים (מוקדים חמים)",
    "שלב 3: פליטת פוזיטרונים ואירועי 'התאבדות'",
    "שלב 4: גלאי הסורק קולטים פוטונים מנוגדים",
    "שלב 5: בניית התמונה על סמך נתוני הגלאים",
    "הסימולציה הסתיימה. לחצו 'התחל מחדש'." // Final State (Step 6)
];

const numTracerParticles = 150; // More particles
const numAnnihilationPairs = 40; // More events
const numDetectors = 72; // More detectors for realism

function updateStepText() {
    stepText.textContent = steps[currentStep];
}

function createTracerParticle() {
    const particle = document.createElement('div');
    particle.classList.add('tracer');
    tracerParticlesContainer.appendChild(particle);
    return particle;
}

function injectTracer() {
    // Simulate injection from a side point outside the body
    const bodyRect = body.getBoundingClientRect();
    const scanAreaRect = scanArea.getBoundingClientRect();
    const startX = bodyRect.left - scanAreaRect.left - 20; // Inject from left of body
    const startY = bodyRect.top - scanAreaRect.top + bodyRect.height / 4; // Inject into arm area

    for (let i = 0; i < numTracerParticles; i++) {
        const particle = createTracerParticle();
        const duration = 1.5 + Math.random() * 1; // Injection duration
        const delay = i * 15; // Stagger injection

        particle.style.left = `${startX}px`;
        particle.style.top = `${startY}px`;
        particle.style.opacity = 0; // Start invisible

        // Target is a random point inside the body bounds relative to scanArea
         const targetX = (bodyRect.left - scanAreaRect.left) + Math.random() * bodyRect.width;
        const targetY = (bodyRect.top - scanAreaRect.top) + Math.random() * bodyRect.height;


        setTimeout(() => {
             particle.classList.add('injecting');
             particle.style.left = `${targetX}px`;
             particle.style.top = `${targetY}px`;
             particle.style.opacity = 1;
         }, delay);

         // After injection, prepare for diffusion
         setTimeout(() => {
             particle.classList.remove('injecting');
             particle.classList.add('diffusing');
         }, delay + duration * 1000);
    }
}

function diffuseAndAccumulateTracer() {
     hotSpot.style.display = 'block'; // Show hot spot outline
     hotSpot.style.animation = 'pulseHotSpot 1.5s infinite alternate'; // Add pulsing effect

    const particles = tracerParticlesContainer.querySelectorAll('.tracer');
    const hotSpotRect = hotSpot.getBoundingClientRect();
    const scanAreaRect = scanArea.getBoundingClientRect();

     const hsCenterX = hotSpotRect.left + hotSpotRect.width / 2 - scanAreaRect.left;
     const hsCenterY = hotSpotRect.top + hotSpotRect.height / 2 - scanAreaRect.top;

    particles.forEach(particle => {
        if (!particle.classList.contains('diffusing')) return; // Only diffuse particles

        const pRect = particle.getBoundingClientRect();
        const pCenterX = pRect.left + pRect.width / 2 - scanAreaRect.left;
        const pCenterY = pRect.top + pRect.height / 2 - scanAreaRect.top;

        const distanceToHotSpot = Math.sqrt(Math.pow(pCenterX - hsCenterX, 2) + Math.pow(pCenterY - hsCenterY, 2));
        const hotSpotRadius = hotSpotRect.width / 2;

        // Simulate diffusion with slight pull towards hotspot
        const duration = 4 + Math.random() * 3; // Longer diffusion time
        let targetX, targetY;

        if (distanceToHotSpot < hotSpotRadius * 2) { // If within accumulation radius
             // Higher chance to move towards hotspot center
             targetX = hsCenterX + (Math.random() - 0.5) * hotSpotRadius;
             targetY = hsCenterY + (Math.random() - 0.5) * hotSpotRadius;
             particle.classList.remove('diffusing');
             particle.classList.add('accumulated');
             particle.style.transition = `all 1s ease-in-out`; // Faster move towards center
        } else {
             // Random walk within body bounds (relative to scanArea)
             const bodyRect = body.getBoundingClientRect();
             targetX = (bodyRect.left - scanAreaRect.left) + Math.random() * bodyRect.width;
             targetY = (bodyRect.top - scanAreaRect.top) + Math.random() * bodyRect.height;
             particle.style.transition = `all ${duration}s linear`;
        }

        particle.style.left = `${targetX}px`;
        particle.style.top = `${targetY}px`;

         // After transition ends, maybe loop diffusion or mark as stable?
         // For simplicity, let them reach target and stay for this step
    });
}

function annihilateAndEmitPhotons() {
    const accumulatedParticles = tracerParticlesContainer.querySelectorAll('.tracer.accumulated');
    const scanAreaRect = scanArea.getBoundingClientRect();
    const hsRect = hotSpot.getBoundingClientRect();
    const hsCenterX = hsRect.left + hsRect.width / 2 - scanAreaRect.left;
    const hsCenterY = hsRect.top + hsRect.height / 2 - scanAreaRect.top;

    // Remove particles (simulate annihilation)
    accumulatedParticles.forEach(p => p.remove());

    // Simulate a flash at the hot spot
    const flash = document.createElement('div');
    flash.style.position = 'absolute';
    flash.style.width = '80px';
    flash.style.height = '80px';
    flash.style.borderRadius = '50%';
    flash.style.backgroundColor = 'rgba(255, 255, 0, 0.8)';
    flash.style.top = `${hsCenterY}px`;
    flash.style.left = `${hsCenterX}px`;
    flash.style.transform = 'translate(-50%, -50%)';
    flash.style.zIndex = 6;
    flash.style.opacity = 1;
    flash.style.transition = 'opacity 0.3s ease-out, transform 0.3s ease-out';
    scanArea.appendChild(flash);

    // Animate flash
    setTimeout(() => {
        flash.style.opacity = 0;
        flash.style.transform = 'translate(-50%, -50%) scale(1.5)';
    }, 50); // Short delay for appearance

    // Remove flash after animation
    setTimeout(() => {
        flash.remove();
        // Start emitting lines AFTER the flash fades
        emitLines(hsCenterX, hsCenterY);
    }, 400); // Matches flash transition duration

     hotSpot.style.animation = 'none'; // Stop pulsing during annihilation
}

function emitLines(originX, originY) {
     const scanAreaRect = scanArea.getBoundingClientRect();
     const containerWidth = scanAreaRect.width;
     const containerHeight = scanAreaRect.height;
     const lineLength = Math.sqrt(containerWidth * containerWidth + containerHeight * containerHeight); // Long enough to cross container

    for (let i = 0; i < numAnnihilationPairs; i++) {
        const angle = Math.random() * 360; // Angle in degrees
        const radians = angle * Math.PI / 180;

        // Line 1
        const line1 = document.createElement('div');
        line1.classList.add('detection-line');
        line1.style.left = `${originX}px`;
        line1.style.top = `${originY}px`;
        line1.style.transform = `rotate(${angle}deg)`;
        line1.style.display = 'block';
        detectionLinesContainer.appendChild(line1);

        // Animate line growth
         requestAnimationFrame(() => {
             setTimeout(() => {
                 line1.style.width = `${lineLength}px`;
             }, 50 + i * 10); // Stagger line appearance
         });


        // Line 2 (180 degrees opposite)
        const angle2 = angle + 180;
         const line2 = document.createElement('div');
        line2.classList.add('detection-line');
        line2.style.left = `${originX}px`;
        line2.style.top = `${originY}px`;
        line2.style.transform = `rotate(${angle2}deg)`;
        line2.style.display = 'block';
        detectionLinesContainer.appendChild(line2);

         // Animate line growth for the second line
         requestAnimationFrame(() => {
             setTimeout(() => {
                 line2.style.width = `${lineLength}px`;
             }, 50 + i * 10); // Use same delay as first line in pair
         });
    }
}


function detectPhotons() {
    const lines = detectionLinesContainer.querySelectorAll('.detection-line');
    const scanAreaRect = scanArea.getBoundingClientRect();
    const scannerRect = scannerRing.getBoundingClientRect();
    const detectorsContainerRect = detectorsContainer.getBoundingClientRect(); // Use detectors container for positioning

    // Create detectors if not already present
    if (detectorsContainer.children.length === 0) {
        const ringCenterX = detectorsContainerRect.width / 2;
        const ringCenterY = detectorsContainerRect.height / 2;
        const ringRadiusX = scannerRect.width / 2;
        const ringRadiusY = scannerRect.height / 2;

        for(let i=0; i<numDetectors; i++) {
            const angle = (i / numDetectors) * 360;
            const radians = angle * Math.PI / 180;
            const detX = ringCenterX + ringRadiusX * Math.cos(radians);
            const detY = ringCenterY + ringRadiusY * Math.sin(radians);

            const detector = document.createElement('div');
            detector.classList.add('detector');
             // Position the detector directly on the circle within its container
            detector.style.left = `${detX - detector.offsetWidth/2}px`;
            detector.style.top = `${detY - detector.offsetHeight/2}px`;
            detector.style.opacity = 1; // Make detectors visible

            // Store position (relative to detectorsContainer) and angle
            detector.dataset.x = detX;
            detector.dataset.y = detY;
            detector.dataset.angle = angle;
            detectorsContainer.appendChild(detector);
        }
    }

    const detectors = detectorsContainer.querySelectorAll('.detector');
    detectionLinesContainer.style.opacity = 0.5; // Dim lines after they appear

    // Simulate detection logic: Check if line endpoint hits a detector
     lines.forEach(line => {
         const originX = parseFloat(line.style.left); // Relative to scanArea
         const originY = parseFloat(line.style.top); // Relative to scanArea
         const angle = parseFloat(line.style.transform.replace('rotate(', '').replace('deg)', ''));
         const radians = angle * Math.PI / 180;

         // Find the point where the line intersects the scanner ellipse
         // This is mathematically complex for ellipse-line intersection.
         // Simplified approach: find endpoint of line that reaches the ring radius.
         const ringCenterX_scanArea = scannerRect.left + scannerRect.width/2 - scanAreaRect.left;
         const ringCenterY_scanArea = scannerRect.top + scannerRect.height/2 - scanAreaRect.top;
         const ringRadiusX = scannerRect.width / 2;
         const ringRadiusY = scannerRect.height / 2;

         let hitX = NaN, hitY = NaN;
         let closestDistToRing = Infinity;
         const lineTestPoints = 100;
         const maxTestLength = Math.max(scanAreaRect.width, scanAreaRect.height);

         for(let j=1; j<=lineTestPoints; j++) {
             const currentLength = (j / lineTestPoints) * maxTestLength;
             const testX = originX + Math.cos(radians) * currentLength;
             const testY = originY + Math.sin(radians) * currentLength;

             // Check distance from (testX, testY) to the ellipse boundary
             // Formula for ellipse: ((x-h)/a)^2 + ((y-k)/b)^2 = 1
             // Where (h, k) is center, a, b are radii
             const normX = (testX - ringCenterX_scanArea) / ringRadiusX;
             const normY = (testY - ringCenterY_scanArea) / ringRadiusY;
             const distToBoundary = Math.abs(normX * normX + normY * normY - 1); // How close to 1

             if (distToBoundary < closestDistToRing) {
                  closestDistToRing = distToBoundary;
                 if (distToBoundary < 0.05) { // If close enough to boundary
                    hitX = testX;
                    hitY = testY;
                    break; // Found a hit point
                 }
             }
         }

         if (!isNaN(hitX)) {
              // Find the closest detector to this hit point
              let closestDetector = null;
              let minDist = Infinity;

              detectors.forEach(detector => {
                 // Detector positions are relative to detectorsContainer
                 const detX_scanArea = parseFloat(detector.dataset.x) + detectorsContainerRect.left - scanAreaRect.left;
                 const detY_scanArea = parseFloat(detector.dataset.y) + detectorsContainerRect.top - scanAreaRect.top;

                  const dist = Math.sqrt(Math.pow(hitX - detX_scanArea, 2) + Math.pow(hitY - detY_scanArea, 2));
                  if (dist < minDist) {
                      minDist = dist;
                      closestDetector = detector;
                  }
              });

              if (closestDetector && minDist < 15) { // If hit is close to a detector
                  // Highlight the detector briefly
                  closestDetector.classList.add('hit');
                  setTimeout(() => {
                      closestDetector.classList.remove('hit');
                  }, 200); // Flash duration
                  // In a real system, we'd record the pair of detectors and the line
                  // For this sim, just highlighting the hit detector is visual feedback.
              }
         }
     });
     // Keep lines visible but dimmed
}

function reconstructImage() {
    // Fade out lines and detectors
    detectionLinesContainer.style.transition = 'opacity 1s ease-out';
    detectionLinesContainer.style.opacity = 0;
    detectorsContainer.style.transition = 'opacity 1s ease-out';
    detectorsContainer.style.opacity = 0;

    // After elements fade, show reconstruction overlay and highlight hotspot
    setTimeout(() => {
        detectionLinesContainer.innerHTML = ''; // Clean up lines
        detectorsContainer.innerHTML = ''; // Clean up detectors

        reconstructionOverlay.style.transition = 'opacity 1s ease-in-out';
        reconstructionOverlay.style.opacity = 1; // Show overlay

        hotSpot.style.display = 'block'; // Ensure hotspot is visible
        hotSpot.style.backgroundColor = 'rgba(255, 0, 0, 1)'; // Solid color
        hotSpot.style.borderColor = 'rgba(255, 255, 0, 0.8)'; // Yellow border
        hotSpot.style.borderWidth = '3px';
        hotSpot.style.width = '60px'; // Emphasize size
        hotSpot.style.height = '60px';
        hotSpot.style.animation = 'pulseHotSpot 1s infinite alternate'; // Make it pulse strongly
         hotSpot.style.zIndex = 7; // Ensure it's above overlay

    }, 1000); // Wait for fade out transition
}


function resetSimulation() {
    currentStep = 0;
    updateStepText();

    // Clear all dynamic elements
    tracerParticlesContainer.innerHTML = '';
    detectionLinesContainer.innerHTML = '';
    detectorsContainer.innerHTML = ''; // Clear detectors container

    // Reset element styles
    hotSpot.style.display = 'none';
     hotSpot.style.backgroundColor = 'rgba(255, 50, 50, 0.6)';
     hotSpot.style.borderColor = 'rgba(255, 0, 0, 0.8)';
     hotSpot.style.borderWidth = '2px';
     hotSpot.style.width = '50px';
     hotSpot.style.height = '50px';
     hotSpot.style.animation = 'none'; // Remove animation
     hotSpot.style.zIndex = 4;

     reconstructionOverlay.style.opacity = 0; // Hide overlay

    // Reset line/detector containers opacity
     detectionLinesContainer.style.transition = 'none';
     detectionLinesContainer.style.opacity = 1;
     detectorsContainer.style.transition = 'none';
     detectorsContainer.style.opacity = 1;


    // Reset controls
    nextStepBtn.disabled = false;
}


function runStep(step) {
    switch (step) {
        case 0: // Initial state - handled by reset
            break;
        case 1: // Injection
            injectTracer();
            break;
        case 2: // Diffusion and Accumulation
             // Allow time for injection animation to finish before starting diffusion
             setTimeout(diffuseAndAccumulateTracer, numTracerParticles * 15 + 1000); // Wait for injection animation + a little extra
            break;
        case 3: // Annihilation
             // Wait for diffusion/accumulation to settle
             setTimeout(annihilateAndEmitPhotons, 4000); // Wait for diffusion animation + a little extra
            break;
        case 4: // Detection
             // Wait for lines to be emitted
             setTimeout(detectPhotons, numAnnihilationPairs * 10 + 1000); // Wait for line emission + a little extra
            break;
        case 5: // Reconstruction
             // Wait for detection flashes/lines to be processed visually
             setTimeout(reconstructImage, 1000); // Wait a bit after detection
            break;
        case 6: // End
            stepText.textContent = steps[6];
            nextStepBtn.disabled = true;
            break;
    }
}

nextStepBtn.addEventListener('click', () => {
    currentStep++;
    if (currentStep < steps.length) {
        updateStepText();
        runStep(currentStep);
    } else {
        // End of steps
         runStep(steps.length); // Run cleanup/final state for step 6 logic
    }
});

resetBtn.addEventListener('click', resetSimulation);

toggleExplanationBtn.addEventListener('click', () => {
    const isHidden = explanationDiv.style.display === 'none';
    explanationDiv.style.display = isHidden ? 'block' : 'none';
    toggleExplanationBtn.textContent = isHidden ? 'הסתר את הסיפור המלא' : 'הצג/הסתר את הסיפור המלא (הסבר מפורט)';
});

// Initial state setup
resetSimulation();
</script>