---
title: "לראות בתוך הגוף: מסע אל תוך MRI"
english_slug: seeing-inside-the-body-how-mri-works
category: "מדעים מדויקים / פיזיקה"
tags:
  - MRI
  - דימות רפואי
  - תהודה מגנטית
  - פיזיקה רפואית
  - אטומים
  - הדמיה
---
# לראות בתוך הגוף: מסע אל תוך MRI

איך מצליחים רופאים לצלול עמוק לתוך גוף האדם, לבחון איברים ורקמות בפירוט מדהים, מבלי לבצע חתך אחד? האם יש כוח נסתר שיכול לחדור דרך העור והעצמות ולחשוף את המתרחש בפנים? הצטרפו אלינו למסע ויזואלי אל הלב הפועם של טכנולוגיית ה-MRI, שם שדות מגנטיים וגלי רדיו רוקמים יחד תמונות עוצרות נשימה.

בואו נדמה יחד את העקרונות הפיזיקליים המאפשרים את הקסם הזה!

<div id="mri-app" lang="he">
    <h2>הסימולציה: צעד אחר צעד אל עולם התהודה</h2>
    <div id="mri-sim-container">
        <div id="mri-protons">
            <!-- Protons will be generated here by JS -->
        </div>
        <div id="sim-status">מצב נוכחי: אתחול</div>
        <div id="sim-controls">
            <button id="btn-b0">שלב 1: הפעל שדה מגנטי (B0)</button>
            <button id="btn-rf" disabled>שלב 2: שלח פולס רדיו (RF)</button>
            <button id="btn-relax" disabled>שלב 3: עצור פולס רדיו (התחל רגיעה)</button>
            <button id="btn-reset">אתחל מחדש</button>
        </div>
    </div>
    <div id="signal-area">
        <h3>אות ה-MRI הנמדד (ייצוג קונספטואלי)</h3>
        <canvas id="signal-canvas" width="400" height="150"></canvas>
    </div>
</div>

<button id="toggle-explanation" style="margin-top: 20px;">הצג/הסתר הסבר מלא</button>

<div id="explanation" style="display: none; margin-top: 20px;">
    <h2>פיענוח הקסם: עקרונות ה-MRI לעומק</h2>

    <h3>מה זה בדיוק MRI?</h3>
    <p>MRI, או דימות תהודה מגנטית (Magnetic Resonance Imaging), היא שיטת הדמיה רפואית מהפכנית. בניגוד לשיטות כמו רנטגן או CT המשתמשות בקרינה מייננת, MRI רותם שדות מגנטיים עוצמתיים וגלי רדיו כדי ליצור תמונות חתך מפורטות של רקמות ואיברים בגוף. זהו כלי אבחון לא פולשני וחיוני ברפואה המודרנית.</p>

    <h3>הלב הפיזיקלי: תהודה מגנטית גרעינית (NMR)</h3>
    <p>בבסיס ה-MRI עומדת תופעה פיזיקלית שנקראת תהודה מגנטית גרעינית (NMR). תופעה זו מתרחשת כאשר גרעינים של אטומים מסוימים, הנמצאים בשדה מגנטי חיצוני חזק, נחשפים לקרינת רדיו בתדר מדויק ותואם (תדר התהודה שלהם), וכתוצאה מכך הם בולעים אנרגיה ומשנים את מצבם.</p>

    <h3>הגיבורים: פרוטוני המימן בגופנו</h3>
    <p>גופנו מכיל כמות עצומה של אטומי מימן, בעיקר במולקולות המים (H₂O) וברקמות השומן. לגרעין של אטום מימן - הפרוטון - יש תכונה פיזיקלית מהותית הנקראת "ספין". אפשר לדמות את הספין הזה כמגנט זעיר המסתובב סביב צירו. במצב רגיל, מחוץ לשדה מגנטי, המגנטים הזעירים הללו מכוונים באופן אקראי לחלוטין.</p>

    <h3>שלב 1 בסימולציה: השדה המגנטי החזק (B0) מיישר את השורות</h3>
    <p>כאשר המטופל נכנס למגנט הענק של מכשיר ה-MRI, הוא נחשף לשדה מגנטי סטטי וחזק מאוד (מסומן כ-B0). עוצמת שדה זה גדולה פי אלפים משדה כדור הארץ. שדה B0 גורם למגנטים הזעירים (הפרוטונים) לחוש כוח שמנסה ליישר אותם במקביל לכיוונו. מרבית הפרוטונים יתיישרו עם כיוון השדה (מצב אנרגטי נמוך יותר), וחלק קטן יתיישרו נגד כיוון השדה (מצב אנרגטי גבוה יותר). בפועל, זה יוצר "מגנוט נטו" קטן בכיוון השדה B0. בנוסף ליישור, הפרוטונים גם מתחילים להסתובב סביב כיוון שדה B0 בתנועה הקרויה "פרצסיה", בדומה לסביבון שמאבד יציבות. תדר הפרצסיה (תדר למור) תלוי בעוצמת שדה B0 ובסוג הגרעין (במקרה שלנו - מימן).</p>

    <h3>שלב 2 בסימולציה: פולס הרדיו (RF) מרעיד את המערכת ומייצר מגנוט רוחבי</h3>
    <p>בשלב הבא, המכשיר שולח פולס קצר של גלי רדיו בעוצמה גבוהה בתדר מדויק - בדיוק תדר למור של פרוטוני המימן בשדה B0 הנתון. כאשר תדר גלי הרדיו תואם את תדר הפרצסיה של הפרוטונים, מתרחשת "תהודה". אנרגיית גלי הרדיו נבלעת על ידי הפרוטונים, במיוחד אלו המיושרים עם B0, וחלקם "קופצים" למצב האנרגטי הגבוה יותר ומתהפכים. חשוב מכך, הפולס גורם לפרוטונים להסתנכרן מבחינת הפאזה של הפרצסיה שלהם - הם מתחילים להסתובב "יחד" במישור המאונך לשדה B0 (המישור הרוחבי). סנכרון זה יוצר "מגנוט רוחבי" זמני ועוצמתי.</p>

    <h3>שלב 3 בסימולציה: הפסקת פולס הרדיו ותהליכי הרגיעה (Relaxation) - פליטת האות הנמדד</h3>
    <p>ברגע שפולס גלי הרדיו נפסק, המערכת "נרגעת" וחוזרת למצב שיווי משקל. זה קורה בשני תהליכים מקבילים שנקראים רגיעה:</p>
    <ul>
        <li>**רגיעה אורכית (T1):** הפרוטונים שקיבלו אנרגיה והתהפכו נוטים לחזור ולהתיישר בכיוון השדה B0 (המגנוט האורכי מתאושש). קצב ההתאוששות שונה ברקמות שונות.</li>
        <li>**רגיעה רוחבית (T2):** המגנוט הרוחבי שנוצר על ידי סנכרון הפאזות של הפרוטונים במישור הרוחבי מתחיל לדעוך. הדעיכה נגרמת מאובדן סנכרון הפאזות בין הפרוטונים עקב אינטראקציות הדדיות ואי-אחידויות מיקרוסקופיות בשדה המגנטי המקומי. זהו התהליך העיקרי היוצר את האות הנמדד.</li>
    </ul>
    <p>במהלך תהליך הרגיעה (בעיקר רגיעה רוחבית), הפרוטונים "פולטים" את האנרגיה העודפת שבלעו מגל הרדיו בצורת גלי רדיו משלהם, גם הם בתדר למור. גלים אלו נקלטים על ידי סלילי קליטה מיוחדים במכשיר ה-MRI. אות הרדיו הנקלט הוא למעשה זרם חשמלי המושרה בסליל עקב השדה המגנטי המשתנה הנוצר על ידי המגנוט הרוחבי הדועך של הפרוטונים. עוצמת האות וקצב הדעיכה שלו תלויים בצפיפות הפרוטונים וזמני הרגיעה (T1 ו-T2) של הרקמה.</p>

    <h3>הסוד של התמונה: ניגודיות (Contrast) על בסיס זמני T1 ו-T2</h3>
    <p>העוצמה הגדולה של MRI היא שזמני הרגיעה T1 ו-T2 שונים באופן משמעותי בין סוגי רקמות שונים (לדוגמה, מים, שומן, שריר, עצם, נוזל מוחי-שדרתי, גידולים). תוכנת המכשיר מודדת את קצב דעיכת האות בכל נקודה בגוף. על ידי בחירת סדרות פולסים חכמות (Sequencing), ניתן "להדגיש" רקמות על בסיס ההבדלים בזמני הרגיעה שלהן, ובכך ליצור את הניגודיות המאפשרת להבדיל בין סוגי רקמות שונים, כולל רקמות חולות.</p>

    <h3>איך בונים תמונה? קידוד מיקום (Spatial Encoding) ועיבוד נתונים</h3>
    <p>כדי לדעת מאיפה בגוף מגיע כל אות, המכשיר מפעיל שדות מגנטיים נוספים המשתנים במרחב (גרדיאנטים) בנוסף לשדה הראשי B0. שדות הגרדיאנט גורמים לכך שתדר למור של הפרוטונים יהיה שונה במקצת בכל נקודה במרחב. על ידי ניתוח התדרים והפאזות באות הכולל הנמדד, המחשב יכול לפענח את המיקום המדויק של מקור האות. באמצעות עיבוד מתמטי מורכב (כמו טרנספורם פורייה), האותות הנמדדים הופכים לתמונה דו-ממדית או תלת-ממדית, כאשר כל פיקסל (או ווקסל) מייצג את עוצמת האות מהמיקום התואם בגוף.</p>

    <h3>למה MRI מצטיין בהדמיית רקמות רכות?</h3>
    <p>האות ב-MRI מקורו בעיקר מפרוטוני מים ושומן, הנפוצים מאוד ברקמות רכות כמו מוח, שרירים, איברים פנימיים וגידולים. לעומת זאת, בעצמות קורטיקליות צפיפות המים נמוכה מאוד, וזמני T2 קצרים במיוחד, מה שגורם לאות לדעוך מהר מדי מכדי להיקלט ביעילות. לכן, MRI מספק תמונות מפורטות במיוחד של רקמות רכות.</p>

    <h3>בטיחות בבדיקת MRI</h3>
    <p>בדיקת MRI בטוחה בדרך כלל, אך חשוב לזכור את עוצמתו העצומה של השדה המגנטי. אסור להכניס לחדר ה-MRI חפצים מתכתיים או אלקטרוניים (טלפונים, שעונים, תכשיטים, כרטיסי אשראי). יש לדווח לצוות הרפואי על כל שתל, קוצב לב, קליע, רסיס מתכת או כל מתכת אחרת בגוף, שכן נוכחותם עלולה להוות סכנה או לפגוע באיכות הבדיקה. בנוסף, רעש הנקישות של המכשיר במהלך הבדיקה דורש שימוש באטמי אוזניים.</p>
</div>

<style>
    #mri-app {
        direction: rtl;
        font-family: 'Heebo', sans-serif; /* Use a modern Hebrew-friendly font */
        border: 1px solid #e0e0e0; /* Softer border */
        padding: 25px;
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* Clean white background */
        max-width: 800px;
        margin: 30px auto; /* More margin */
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    #mri-app h2 {
        color: #1a2b4c; /* Darker blue title */
        margin-bottom: 20px;
        font-size: 1.8em;
    }

    #mri-sim-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 25px;
        background: linear-gradient(to bottom, #eef2f7, #dce1e8); /* Light gradient background */
        padding: 20px;
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    #sim-status {
         margin-bottom: 15px;
         font-size: 1.1em;
         color: #333;
         min-height: 1.2em; /* Reserve space */
    }

    #mri-protons {
        position: relative;
        width: 350px; /* Slightly larger */
        height: 250px;
        border: 2px solid #b0c4de; /* Softer blue border */
        background-color: #e8f0fe; /* Very light blue background */
        overflow: hidden;
        margin-bottom: 20px;
        border-radius: 8px;
        perspective: 600px; /* Add perspective for 3D rotation */
    }

    .proton {
        position: absolute;
        width: 10px; /* Larger proton */
        height: 10px;
        background: radial-gradient(circle, #4a90e2 0%, #2d7cdb 100%); /* Gradient blue */
        border-radius: 50%;
        transform-origin: center center;
        /* Initial transform handled by JS */
        box-shadow: 0 0 5px rgba(0, 0, 255, 0.3); /* Subtle glow */
    }

    .proton::after {
        content: '';
        position: absolute;
        width: 2px; /* Thicker line */
        height: 16px; /* Longer line (spin vector) */
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white */
        transform-origin: top center;
        transform: translateY(-8px); /* Position line relative to center */
        transition: background-color 0.3s ease;
    }

    .proton.excited {
         background: radial-gradient(circle, #f5a623 0%, #e38c00 100%); /* Orange/Yellow gradient for excited state */
         box-shadow: 0 0 8px rgba(255, 165, 0, 0.5); /* Orange glow */
    }


    #sim-controls button {
        margin: 8px; /* More space between buttons */
        padding: 12px 20px; /* Larger padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* More rounded buttons */
        background-color: #007bff; /* Primary blue */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        min-width: 150px; /* Ensure minimum width */
    }

    #sim-controls button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
    }

    #sim-controls button:hover:not(:disabled) {
        background-color: #0056b3; /* Darker blue on hover */
    }

     #sim-controls button:active:not(:disabled) {
        transform: scale(0.98); /* Press effect */
    }

    #signal-area {
        margin-top: 25px;
        border-top: 1px solid #e0e0e0;
        padding-top: 20px;
        text-align: right; /* Align text right */
    }

    #signal-area h3 {
        color: #1a2b4c;
        margin-bottom: 10px;
        font-size: 1.3em;
    }

    #signal-canvas {
        border: 1px solid #b0c4de;
        background-color: #eef0f4; /* Light background */
        display: block;
        margin: 0 auto;
        border-radius: 4px;
    }

    #explanation {
        border: 1px solid #e0e0e0;
        padding: 25px;
        border-radius: 12px;
        background-color: #f9f9f9; /* Slightly different background */
        max-width: 800px;
        margin: 30px auto;
        text-align: right;
        line-height: 1.7; /* Improved readability */
        color: #333; /* Darker text */
    }

    #explanation h2, #explanation h3 {
        color: #1a2b4c;
        border-bottom: 1px solid #d0d0d0; /* Softer border */
        padding-bottom: 8px;
        margin-top: 20px; /* More space above headings */
        margin-bottom: 10px;
    }

    #explanation p {
        margin-bottom: 15px;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 20px;
    }

    #explanation li {
        margin-bottom: 8px;
    }


    #toggle-explanation {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 4px;
        background-color: #6c757d; /* Secondary grey button */
        color: white;
        transition: background-color 0.3s ease;
    }

    #toggle-explanation:hover {
        background-color: #5a6268;
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const protonContainer = document.getElementById('mri-protons');
        const btnB0 = document.getElementById('btn-b0');
        const btnRF = document.getElementById('btn-rf');
        const btnRelax = document.getElementById('btn-relax');
        const btnReset = document.getElementById('btn-reset');
        const simStatus = document.getElementById('sim-status');
        const signalCanvas = document.getElementById('signal-canvas');
        const toggleExplanationBtn = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        const ctx = signalCanvas.getContext('2d');
        const canvasWidth = signalCanvas.width;
        const canvasHeight = signalCanvas.height;
        const signalAmplitude = canvasHeight * 0.4; // Peak signal height
        const signalBaseline = canvasHeight / 2;

        const numProtons = 150; // More protons for a better visual density
        let protons = [];
        let currentState = 'initial'; // initial, b0, rf, relaxing
        let animationFrameId = null;
        let signalAnimationFrameId = null;
        let relaxationStartTime = null;
        const relaxationDuration = 4000; // Simulate relaxation for 4 seconds

        function createProtons() {
            protonContainer.innerHTML = '';
            protons = [];
            for (let i = 0; i < numProtons; i++) {
                const proton = document.createElement('div');
                proton.classList.add('proton');
                // Random initial position
                const x = Math.random() * (protonContainer.offsetWidth - 10) + 5;
                const y = Math.random() * (protonContainer.offsetHeight - 10) + 5;
                proton.style.left = `${x}px`;
                proton.style.top = `${y}px`;
                // Random initial 3D rotation (yaw, pitch, roll)
                const initialYaw = Math.random() * 360;
                const initialPitch = Math.random() * 180 - 90; // Up/down tilt
                const initialRoll = Math.random() * 360; // Spin around its own axis

                proton.style.transform = `translate(-50%, -50%) rotateY(${initialPitch}deg) rotateZ(${initialYaw}deg) rotateX(${initialRoll}deg)`;

                protons.push({
                    element: proton,
                    x: x,
                    y: y,
                    rotation: { yaw: initialYaw, pitch: initialPitch, roll: initialRoll },
                    phase: Math.random() * 360, // Initial phase for precession
                    precessionFreq: 360 + (Math.random() - 0.5) * 20, // Base freq + small random variation
                    state: 'initial' // 'initial', 'aligned', 'excited', 'dephasing'
                });
                protonContainer.appendChild(proton.element);
            }
        }

        function updateButtons() {
            btnB0.disabled = currentState !== 'initial' && currentState !== 'b0_relaxed';
            btnRF.disabled = currentState !== 'b0';
            btnRelax.disabled = currentState !== 'rf';
            btnReset.disabled = currentState === 'initial';

            let statusText = 'מצב נוכחי: ';
            switch(currentState) {
                case 'initial': statusText += 'אתחול - פרוטונים מכוונים באקראי'; break;
                case 'b0': statusText += 'שלב 1: שדה מגנטי B0 - יישור ופרצסיה'; break;
                case 'rf': statusText += 'שלב 2: פולס רדיו RF - עירור ויצירת מגנוט רוחבי'; break;
                case 'relaxing': statusText += 'שלב 3: רגיעה - אות MRI נפלט ודועך'; break;
                case 'b0_relaxed': statusText += 'חזרה לשיווי משקל בשדה B0 - מוכנים לפולס הבא'; break;
            }
             simStatus.textContent = statusText;
        }

        function drawSignal(elapsedTime = 0) {
            ctx.clearRect(0, 0, canvasWidth, canvasHeight);

            // Draw equilibrium line
            ctx.strokeStyle = '#ccc';
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(0, signalBaseline);
            ctx.lineTo(canvasWidth, signalBaseline);
            ctx.stroke();

            ctx.strokeStyle = '#007bff';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(0, signalBaseline);

            if (currentState === 'rf') {
                 // Simulate high signal while RF is active (instantaneous concept)
                 // A real signal might build up, but for simplicity, show it's 'on'
                 ctx.lineTo(canvasWidth, signalBaseline); // Just a conceptual line indicating signal presence
                 // Or draw a simple sine wave to indicate RF frequency? Let's keep it simple for now.
                  ctx.strokeStyle = '#28a745'; // Green for RF pulse conceptual signal
                   ctx.beginPath();
                  const rfSignalAmplitude = signalAmplitude * 0.8;
                  const rfFrequency = 10; // Conceptual high frequency
                  for (let x = 0; x < canvasWidth; x++) {
                       const y = signalBaseline - Math.sin((x / canvasWidth) * Math.PI * 2 * rfFrequency) * rfSignalAmplitude * 0.2; // Small wavy line
                       if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
                  }
                  ctx.stroke();


            } else if (currentState === 'relaxing' && elapsedTime >= 0) {
                // Simulate signal decay after RF stops (Conceptual T2 decay of transverse magnetization)
                // Animate the decay of a sine wave over time
                const timeProgress = Math.min(elapsedTime / relaxationDuration, 1);
                const currentAmplitude = signalAmplitude * Math.exp(-timeProgress * 3); // Exponential decay
                const frequency = 15; // Conceptual Larmor frequency visualization
                const dephasingFactor = timeProgress * 0.5; // Conceptual increase in dephasing over time

                for(let x = 0; x <= canvasWidth; x++) {
                    // Time represented by x for the wave's phase, elapsedTime for decay amplitude
                    const wavePhase = (x / canvasWidth) * Math.PI * 2 * frequency + elapsedTime * 0.01; // Add time to phase for animation
                     // Introduce slight frequency variation along x for T2* hint
                    const freqVariation = Math.sin(x/canvasWidth * Math.PI) * dephasingFactor * 5;
                    const signalY = signalBaseline - Math.sin(wavePhase + freqVariation) * currentAmplitude;
                    if (x === 0) ctx.moveTo(x, signalY); else ctx.lineTo(x, signalY);
                }
                ctx.strokeStyle = '#007bff'; // Blue for the relaxing signal
                ctx.stroke();

            }
             // else state (initial, b0, b0_relaxed) - draw baseline only, done above
        }

        function animateProtons(currentTime) {
             let timeElapsed = currentTime - (animateProtons.startTime || currentTime);
             animateProtons.startTime = currentTime;
             let deltaTime = timeElapsed / 1000; // Time in seconds

            protons.forEach(p => {
                 let { element, rotation, phase, precessionFreq, state } = p;
                 let currentYaw = rotation.yaw;
                 let currentPitch = rotation.pitch;
                 let currentRoll = rotation.roll;

                 if (state === 'aligned') {
                     // Precession in B0 state
                     phase = (phase + precessionFreq * deltaTime) % 360;
                     currentPitch = 0; // Keep aligned with B0 (conceptually)
                      currentRoll = (currentRoll + precessionFreq * 0.5 * deltaTime) % 360; // Spin on axis
                 } else if (state === 'excited') {
                     // Immediately after RF pulse - rotating in the transverse plane
                     // Phase progresses, pitch is 90 deg (conceptually)
                      phase = (phase + precessionFreq * deltaTime) % 360;
                     currentPitch = 90;
                      currentRoll = (currentRoll + precessionFreq * 0.5 * deltaTime) % 360; // Spin on axis
                 } else if (state === 'dephasing') {
                     // T2 Relaxation: Precession continues, but phase coherence is lost
                     // Add random drift to phase progress for visual dephasing
                     const dephaseSpeed = (Math.random() - 0.5) * 100; // Random phase drift speed
                      phase = (phase + (precessionFreq + dephaseSpeed) * deltaTime) % 360;

                     // T1 Relaxation: Pitch returns from 90deg towards 0deg over time
                     const relaxProgress = Math.min((currentTime - relaxationStartTime) / relaxationDuration, 1);
                     currentPitch = 90 * (1 - relaxProgress) ; // Pitch returns to 0
                     currentRoll = (currentRoll + precessionFreq * 0.5 * deltaTime) % 360; // Spin on axis
                 }


                 // Apply rotation transform
                 element.style.transform = `translate(-50%, -50%) rotateX(${currentRoll}deg) rotateY(${currentPitch}deg) rotateZ(${phase}deg)`;

                 // Update proton object state
                 p.rotation.yaw = currentYaw; // Yaw isn't explicitly used in transform, but kept for conceptual rotation
                 p.rotation.pitch = currentPitch;
                 p.rotation.roll = currentRoll;
                 p.phase = phase;
            });

            animationFrameId = requestAnimationFrame(animateProtons);
        }

         function animateSignalCanvas(currentTime) {
             let timeElapsed = currentTime - (animateSignalCanvas.startTime || currentTime);
             animateSignalCanvas.startTime = currentTime;

             if (currentState === 'relaxing') {
                 drawSignal(currentTime - relaxationStartTime);
             } else if (currentState === 'rf') {
                 drawSignal(0); // Draw high signal state
             } else {
                 drawSignal(-1); // Draw baseline
             }


             signalAnimationFrameId = requestAnimationFrame(animateSignalCanvas);
         }

        function stopAnimations() {
            if (animationFrameId) {
                cancelAnimationFrame(animationFrameId);
                animationFrameId = null;
            }
             if (signalAnimationFrameId) {
                 cancelAnimationFrame(signalAnimationFrameId);
                 signalAnimationFrameId = null;
             }
             animateProtons.startTime = null; // Reset start time
             animateSignalCanvas.startTime = null; // Reset start time
        }


        // Initial state setup
        createProtons();
        currentState = 'initial';
        updateButtons();
        drawSignal(-1); // Draw initial baseline

         // Start signal canvas animation loop immediately, it will draw based on state
         animateSignalCanvas(performance.now());


        // Event Listeners
        btnB0.addEventListener('click', () => {
            if (currentState !== 'initial' && currentState !== 'b0_relaxed') return;

            currentState = 'b0';
            updateButtons();
            stopAnimations(); // Stop previous animation loop if any

            // Animate alignment first (quick visual effect)
            protons.forEach(p => {
                // Animate pitch rotation towards 0 or 180, with majority towards 0
                const targetPitch = (Math.random() < 0.85) ? 0 : 180;
                 p.element.style.transition = 'transform 1s ease-out';
                 p.element.style.transform = `translate(-50%, -50%) rotateX(${p.rotation.roll}deg) rotateY(${targetPitch}deg) rotateZ(${p.phase}deg)`;
                 p.rotation.pitch = targetPitch;
                 p.state = 'aligned'; // Mark state as aligned

            });

            // After alignment transition, start precession animation
             setTimeout(() => {
                  protons.forEach(p => p.element.style.transition = 'none'); // Disable transition for continuous animation
                  animateProtons(performance.now()); // Start the animation loop for precession
             }, 1000); // Match the CSS transition duration

             // Signal stays at baseline
             currentState = 'b0'; // Ensure state is set after timeout if needed, or manage state carefully
             updateButtons();
        });

        btnRF.addEventListener('click', () => {
            if (currentState !== 'b0') return;

             stopAnimations(); // Stop precession briefly for the flip animation

            // Animate flip to transverse plane (pitch to 90deg)
            protons.forEach(p => {
                 if (p.rotation.pitch === 0) { // Only flip protons aligned "up"
                    p.element.style.transition = 'transform 0.5s ease-in-out';
                    p.element.style.transform = `translate(-50%, -50%) rotateX(${p.rotation.roll}deg) rotateY(90deg) rotateZ(${p.phase}deg)`;
                    p.rotation.pitch = 90;
                    p.state = 'excited';
                    p.element.classList.add('excited'); // Add excited class for color change
                 }
            });

            currentState = 'rf';
            updateButtons();
             // The signal animation loop is already running and will draw RF signal based on state
             // No need to restart animateProtons yet, it will restart in the next state


             // Transition to relaxation state automatically after a short RF pulse duration
             setTimeout(() => {
                 btnRelax.click(); // Auto trigger relaxation after RF pulse
             }, 1000); // Simulate short RF pulse duration
        });

        btnRelax.addEventListener('click', () => {
            if (currentState !== 'rf') return;

            currentState = 'relaxing';
            updateButtons();
            relaxationStartTime = performance.now(); // Record start time for decay calculation

             // Transition protons to dephasing/relaxing states
             protons.forEach(p => {
                 if (p.state === 'excited') {
                    p.state = 'dephasing'; // Start T2 dephasing and T1 relaxation
                 }
                 p.element.classList.remove('excited'); // Return to relaxed color visually

                 p.element.style.transition = 'none'; // Disable transition for continuous animation
             });

             animateProtons(performance.now()); // Restart animation loop for dephasing/realigning

             // Signal canvas animation loop is already running and will draw decaying signal

             // After relaxation duration, return to B0 state
             setTimeout(() => {
                 stopAnimations(); // Stop dephasing/realigning animation
                 currentState = 'b0_relaxed'; // Use a specific state for 'back to B0 after relaxation'
                 updateButtons();
                 // Force protons back to aligned state visually for clarity after sim segment
                  protons.forEach(p => {
                     p.element.style.transition = 'transform 1s ease-out';
                      const targetPitch = (Math.random() < 0.85) ? 0 : 180; // Re-establish alignment bias
                      p.rotation.pitch = targetPitch;
                     p.state = 'aligned';
                      p.element.style.transform = `translate(-50%, -50%) rotateX(0deg) rotateY(${targetPitch}deg) rotateZ(${p.phase}deg)`; // Reset roll/pitch
                 });
                 setTimeout(() => {
                      protons.forEach(p => p.element.style.transition = 'none'); // Disable transition again
                       animateProtons(performance.now()); // Restart precession animation in B0
                 }, 1000);


                 drawSignal(-1); // Signal returns to baseline
             }, relaxationDuration);
        });

        btnReset.addEventListener('click', () => {
            stopAnimations();
            createProtons();
            currentState = 'initial';
            updateButtons();
            drawSignal(-1); // Draw initial baseline
             // Ensure the signal animation loop restarts
             animateSignalCanvas(performance.now());
        });

        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מלא' : 'הצג/הסתר הסבר מלא';
        });

        // Ensure animations start correctly when stepping through after reset/relax
        // This is handled within the button click handlers and the timeouts triggering state changes.
        // The signal canvas animation loop runs continuously and adapts to the state.

    });
</script>
```