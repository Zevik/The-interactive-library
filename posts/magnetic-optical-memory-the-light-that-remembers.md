---
title: "זיכרון מגנטי-אופטי: האור שזוכר ומספר"
english_slug: magnetic-optical-memory-the-light-that-remembers
category: "מדעים מדויקים / פיזיקה"
tags:
  - זיכרון
  - אופטיקה
  - מגנטיות
  - אחסון נתונים
  - אפקט קר
---

<div id="mo-simulation" class="simulation-container">
    <div class="simulation-header">
        <div class="simulation-title">זיכרון מגנטי-אופטי בפעולה</div>
        <div class="controls-panel">
            <div class="control-group">
                <label for="mode-select">בחר מצב:</label>
                <select id="mode-select" class="control-select">
                    <option value="write">כתיבה</option>
                    <option value="read">קריאה</option>
                </select>
            </div>
            <div id="write-controls" class="control-group action-controls">
                <label>כתיבת ביט:</label>
                <button class="control-button" id="set-bit-0" data-bit="0">כתוב 0 (שדה למעלה)</button>
                <button class="control-button" id="set-bit-1" data-bit="1">כתוב 1 (שדה למטה)</button>
            </div>
            <div id="read-controls" class="control-group action-controls" style="display: none;">
                <!-- Read mode is triggered by mode switch and simulation flow -->
                 <button class="control-button" id="read-button">בצע קריאה</button>
            </div>
        </div>
    </div>

    <div class="simulation-area">
        <div class="component laser-source">לייזר</div>

        <div class="component magnetic-field-indicator field-up" id="magnetic-field-up">
            <div class="field-arrow">↑</div>
            <div class="field-label">שדה מגנטי (0)</div>
        </div>
        <div class="component magnetic-field-indicator field-down" id="magnetic-field-down">
            <div class="field-arrow">↓</div>
            <div class="field-label">שדה מגנטי (1)</div>
        </div>

        <div class="component mo-disk-spot" id="disk-spot">
            <div class="magnetization-arrow" id="magnetization-arrow">?</div>
            <div class="temperature-indicator" id="temperature-indicator">קר</div>
             <div class="heating-pulse"></div>
        </div>

         <div class="component polarization-beam" id="incoming-polarization"></div>
         <div class="component polarization-beam reflected" id="reflected-polarization"></div>

        <div class="component polarization-detector" id="polarization-detector">
            גלאי קיטוב
            <div class="detected-angle" id="detected-angle">--</div>
             <div class="detector-readout" id="detector-readout">?</div>
        </div>
    </div>

    <div class="status-area">
        <p>מצב הסימולציה: <span id="current-status">בחר מצב פעולה</span></p>
        <div class="bit-info">
            <p>ביט אגור: <span id="stored-bit" class="bit-value">?</span></p>
            <p>ביט שנקרא: <span id="read-bit" class="bit-value">?</span></p>
        </div>
    </div>
</div>

<style>
/* General Layout and Styling */
#mo-simulation {
    font-family: 'Varela Round', sans-serif; /* More modern font */
    direction: rtl; /* Right-to-left */
    border: 1px solid #d1d1d1;
    padding: 20px;
    margin-bottom: 25px;
    background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Soft gradient background */
    border-radius: 12px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    color: #333;
}

.simulation-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 25px;
    padding-bottom: 15px;
    border-bottom: 1px solid #b2ebf2;
}

.simulation-title {
    font-size: 1.8em;
    font-weight: bold;
    color: #00796b; /* Teal color */
}

.controls-panel {
    display: flex;
    gap: 20px;
    align-items: center;
}

.control-group {
    display: flex;
    align-items: center;
    gap: 8px;
    background-color: rgba(255, 255, 255, 0.8);
    padding: 10px 15px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
}

.control-group label {
    font-weight: bold;
    color: #004d40; /* Darker teal */
}

.control-select, .control-button {
    padding: 8px 15px;
    border: 1px solid #00796b;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
}

.control-select {
    background-color: #e0f2f7;
    color: #004d40;
    appearance: none; /* Remove default arrow */
    background-image: url('data:image/svg+xml;utf8,<svg fill="%2300796b" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>');
    background-repeat: no-repeat;
    background-position: left 8px center; /* Position arrow on the left */
    padding-left: 30px; /* Space for arrow */
}

.control-button {
    background-color: #4db6ac; /* Light teal */
    color: white;
    font-weight: bold;
    border: none;
}

.control-button:hover {
    background-color: #26a69a; /* Darker teal on hover */
}

.control-button:active {
    transform: scale(0.98);
}

.control-button:disabled {
    background-color: #b2dfdb;
    cursor: not-allowed;
}


.simulation-area {
    position: relative;
    width: 100%;
    min-height: 450px; /* Increased height for visual flow */
    background-color: #ffffff;
    border: 1px solid #b2ebf2;
    border-radius: 8px;
    box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.05);
    padding: 20px;
    display: flex;
    justify-content: center; /* Center content horizontally */
    align-items: flex-start; /* Align content to the top */
}

.component {
    position: absolute;
    text-align: center;
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 0.9em;
    white-space: nowrap;
}

.laser-source {
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #e57373; /* Light red */
    color: white;
    font-weight: bold;
    z-index: 20; /* Above beams initially */
}

.magnetic-field-indicator {
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(100, 181, 246, 0.9); /* Light blue with opacity */
    color: #0d47a1; /* Dark blue */
    font-weight: bold;
    box-shadow: 0 0 10px rgba(66, 165, 245, 0.5); /* Blue glow */
    opacity: 0; /* Hidden by default */
    transition: opacity 0.5s ease, transform 0.5s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    width: 80px;
    padding: 10px;
}

.magnetic-field-indicator.field-up {
    right: 10%; /* Position on the right for RTL */
    transform: translateY(-50%) translateX(20px); /* Start slightly off-screen */
}

.magnetic-field-indicator.field-down {
    left: 10%; /* Position on the left for RTL */
    transform: translateY(-50%) translateX(-20px); /* Start slightly off-screen */
}

.magnetic-field-indicator.active {
    opacity: 1;
     transform: translateY(-50%) translateX(0);
}

.field-arrow {
    font-size: 1.8em;
    font-weight: bold;
}

.field-label {
    font-size: 0.8em;
}


.mo-disk-spot {
    width: 100px;
    height: 100px;
    background-color: #80cbc4; /* Cool state */
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 150px; /* Center vertically in the intended flow */
    left: 50%;
    transform: translateX(-50%);
    transition: background-color 0.6s ease, transform 0.3s ease;
    overflow: visible; /* Allow pulse animation to extend */
    border: 3px solid #004d40; /* Dark teal border */
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    z-index: 5; /* Below beams initially */
}

.mo-disk-spot.hot {
    background-color: #ffab91; /* Hot state */
     box-shadow: 0 4px 15px rgba(255, 87, 34, 0.6); /* Orange glow */
}

.heating-pulse {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 0;
    height: 0;
    background-color: rgba(255, 87, 34, 0.7); /* Pulse color */
    border-radius: 50%;
    opacity: 0;
    transition: all 0.8s ease-out;
     z-index: -1; /* Behind main spot content */
}

.mo-disk-spot.heating .heating-pulse {
    animation: pulse-heat 1.5s ease-out forwards;
}

@keyframes pulse-heat {
    0% { width: 0; height: 0; opacity: 0.7; }
    50% { width: 150px; height: 150px; opacity: 0.3; }
    100% { width: 200px; height: 200px; opacity: 0; }
}


.magnetization-arrow {
    font-size: 3.5em; /* Larger arrow */
    font-weight: bolder;
    color: #0d47a1; /* Dark blue */
    transition: transform 0.5s ease-in-out;
}

.magnetization-arrow.up {
    transform: rotate(0deg);
}

.magnetization-arrow.down {
    transform: rotate(180deg);
}

.temperature-indicator {
    position: absolute;
    bottom: -20px; /* Below the disk */
    left: 50%;
    transform: translateX(-50%);
    font-size: 0.85em;
    color: #333;
    background-color: rgba(255, 255, 255, 0.9);
    padding: 3px 8px;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.polarization-beam {
     position: absolute;
     width: 8px; /* Thicker beam */
     height: 120px; /* Longer beam */
     background: linear-gradient(to bottom, rgba(255,238,88,0.9), rgba(255,160,0,0.9)); /* Yellow/Orange polarized light */
     left: calc(50% - 4px); /* Center over the spot */
     transform-origin: center top;
     top: 60px; /* Starts below laser */
     opacity: 0; /* Hidden initially */
     transition: transform 0.6s ease-in-out, opacity 0.5s ease, top 0.6s ease;
     z-index: 8; /* Above disk, below laser source */
     box-shadow: 0 0 10px rgba(255, 160, 0, 0.5); /* Orange glow */
}

#incoming-polarization {
     height: 90px; /* Length to hit the disk */
     transform: translateY(0); /* Start position */
     opacity: 0;
}

#reflected-polarization {
    top: calc(60px + 90px); /* Starts exactly where incoming beam hits disk */
    transform-origin: center top; /* Rotate from the point of reflection */
    transform: rotate(0deg); /* Initial state */
    height: 100px; /* Length reflecting upwards */
    background: linear-gradient(to top, rgba(255,238,88,0.9), rgba(255,160,0,0.9)); /* Gradient direction reversed */
    opacity: 0;
}

.polarization-detector {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #bdbdbd; /* Grey color */
    color: #424242;
    padding: 10px 15px;
    border-radius: 8px;
    text-align: center;
    width: 150px;
    opacity: 0; /* Hidden initially */
    transition: opacity 0.5s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    font-weight: bold;
    z-index: 8; /* Same as beams */
}

.detected-angle {
    margin-top: 5px;
    font-weight: bold;
    color: #004d40; /* Dark teal */
    font-size: 1.1em;
}

.detector-readout {
    margin-top: 8px;
    font-size: 1.6em;
    font-weight: bolder;
    color: #e65100; /* Deep Orange */
}

/* Status Area Styling */
.status-area {
    margin-top: 25px;
    padding-top: 15px;
    border-top: 1px solid #b2ebf2;
    text-align: center;
    font-size: 1em;
    color: #004d40;
}

.status-area p {
    margin-bottom: 8px;
    font-weight: bold;
}

.status-area span {
    font-weight: normal;
    color: #333;
}

.bit-info {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-top: 10px;
}

.bit-value {
    font-weight: bold;
    color: #e65100; /* Deep Orange */
    font-size: 1.1em;
}


/* Explanation Section Styling */
button#toggle-explanation {
    display: block;
    margin: 30px auto 20px auto;
    padding: 12px 25px;
    font-size: 1.1em;
    cursor: pointer;
    background-color: #00796b; /* Teal */
    color: white;
    border: none;
    border-radius: 6px;
    transition: background-color 0.3s ease;
    font-family: 'Varela Round', sans-serif;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

button#toggle-explanation:hover {
    background-color: #004d40; /* Darker teal */
}

#explanation-content {
    border: 1px solid #d1d1d1;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
    display: none; /* Hidden by default */
    line-height: 1.7;
    color: #333;
}

#explanation-content h2, #explanation-content h3 {
    color: #00796b;
    margin-top: 20px;
    margin-bottom: 10px;
    border-bottom: 1px solid #e0f2f7;
    padding-bottom: 5px;
}

#explanation-content h2 {
    font-size: 1.6em;
}

#explanation-content h3 {
    font-size: 1.3em;
}

#explanation-content p {
    margin-bottom: 15px;
}

#explanation-content ol, #explanation-content ul {
    margin-bottom: 15px;
    padding-right: 20px; /* Indent list items */
}

#explanation-content li {
    margin-bottom: 8px;
}

#explanation-content strong {
    color: #004d40;
}

/* Add some basic responsive adjustments */
@media (max-width: 768px) {
    .simulation-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 15px;
    }
    .controls-panel {
        flex-direction: column;
        gap: 10px;
        width: 100%;
    }
    .control-group {
        width: 100%;
        justify-content: center;
        flex-wrap: wrap;
    }
     .simulation-area {
         min-height: 400px;
     }
     .component {
         position: static; /* Allow components to stack */
         transform: none !important; /* Override absolute positioning transforms */
         margin-bottom: 15px; /* Add space between stacked components */
     }
     .mo-disk-spot {
         width: 80px;
         height: 80px;
     }
     .magnetization-arrow {
         font-size: 2.5em;
     }
     .heating-pulse {
         /* May need specific adjustments for stacked layout */
     }
     .polarization-beam, #reflected-polarization {
         display: none; /* Hide complex animations on small screens */
     }
     .polarization-detector {
         width: auto;
     }
}

</style>

<button id="toggle-explanation">הצג/הסתר הסבר על זיכרון מגנטי-אופטי</button>

<div id="explanation-content">
    <h2>קסם האור והמגנט: איך זיכרון מגנטי-אופטי עובד?</h2>
    <p>דמיינו דיסק שמצד אחד נראה כמו תקליטור רגיל, אבל מצד שני יכול לשמור ולמחוק מידע שוב ושוב! זה בדיוק הקסם שמאחורי זיכרון מגנטי-אופטי (MO). במקום להשתמש רק במגנטיות כמו בדיסק קשיח, או רק באור כמו בתקליטור חד-פעמי, זיכרון MO מחבר בין שני העולמות כדי לאחסן נתונים בצורה יציבה וניתנת לשינוי.</p>

    <h3>לב הטכנולוגיה: מגנטיות שמושפעת מחום</h3>
    <p>החומר הסודי בדיסק MO הוא שכבה דקה של חומר מיוחד (למשל, סגסוגת של מתכות נדירות עם ברזל). החומר הזה הוא מגנטי, אבל יש לו תכונה מעניינת: מעל טמפרטורה מסוימת, הנקראת 'טמפרטורת קירי', הוא מאבד את ה'זיכרון' המגנטי שלו. בטמפרטורה הזו, קל מאוד לשנות את כיוון המגנוט שלו באמצעות שדה מגנטי חיצוני חלש.</p>

    <h3>שלב 1: כתיבת המידע (הפיכת המגנט בעזרת לייזר)</h3>
    <p>כדי לכתוב ביט מידע (0 או 1) על הדיסק, מתרחשים שני דברים במקביל:</p>
    <ol>
        <li><strong>חימום נקודתי בלייזר:</strong> קרן לייזר חזקה יחסית מתמקדת בנקודה זעירה על הדיסק ומחממת אותה במהירות מעל טמפרטורת קירי. בנקודה זו, החומר "שוכח" את המגנוט הקודם שלו.</li>
        <li><strong>הפעלת שדה מגנטי:</strong> בזמן שהנקודה חמה, מופעל עליה שדה מגנטי חיצוני חלש בכיוון הרצוי - למעלה עבור 0, או למטה עבור 1. כשהנקודה מתקררת (מיד לאחר שהלייזר מפסיק לחמם אותה), החומר "זוכר" את כיוון השדה שהיה שם ברגע הקירור, ושומר עליו גם לאחר שהשדה החיצוני מוסר. כך נכתב הביט.</li>
    </ol>
     <p><strong>טיפ למתקדמים:</strong> לרוב, כתיבה מלאה כללה למעשה שתי פעולות: מחיקה (חימום והפעלת שדה בכיוון ניטרלי או קבוע) ולאחר מכן כתיבה (חימום והפעלת שדה בכיוון הרצוי). זה הפך את הכתיבה לאיטית יחסית.</p>

    <h3>שלב 2: קריאת המידע (גילוי סיבוב האור)</h3>
    <p>הקריאה היא החלק המגניב והאופטי של הסיפור, והיא לא משנה את המידע האגור:</p>
    <ol>
        <li><strong>לייזר עדין ומקוטב:</strong> קרן לייזר חלשה (שלא מחממת את הדיסק) מוקרנת על הנקודה. קרן זו מקוטבת, כלומר גלי האור שלה מתנדנדים רק בכיוון אחד (נניח, אנכית).</li>
        <li><strong>אפקט קר - הריקוד המגנטי של האור:</strong> כשהאור הזה מוחזר מהנקודה הממוגנטת, כיוון המגנוט של הנקודה גורם למישור הקיטוב של האור המוחזר להסתובב בזווית קטנה מאוד. הכיוון של הסיבוב הזה (ימינה או שמאלה) תלוי בכיוון המגנוט של הנקודה (למעלה או למטה). זהו 'אפקט קר המגנטו-אופטי'.</li>
        <li><strong>גלאי הקיטוב קולט:</strong> האור המוחזר עובר דרך גלאי קיטוב. הגלאי הזה יודע לזהות את זווית הקיטוב של האור. אם האור הסתובב ימינה, זה אומר שהנקודה ממוגנטת בכיוון 0; אם הסתובב שמאלה, זה אומר 1 (או להיפך, תלוי בתכנון המערכת). כך המערכת 'קוראת' את הביט האגור.</li>
    </ol>

    <h3>למה זה לא איתנו היום?</h3>
    <p>למרות שהיה לזיכרון MO יתרונות כמו עמידות ויכולת מחיקה וכתיבה רב פעמית (בניגוד לתקליטורים צרובים חד-פעמיים), היו לו חסרונות משמעותיים שהביאו לדעיכתו מול טכנולוגיות אחרות. העיקרי שבהם היה המהירות: תהליך הכתיבה שדורש חימום וקירור היה איטי משמעותית מדי בהשוואה לכוננים קשיחים שהלכו והשתפרו במהירות. בנוסף, הדרייבים והמדיות היו יקרים יותר, והקיבולת, למרות שגדלה עם השנים, נותרה נמוכה יותר ממתחרים אחרים.</p>

    <h3>לסיכום</h3>
    <p>זיכרון מגנטי-אופטי הוא דוגמה מצוינת לשילוב גאוני של עקרונות מפיזיקה שונים - מגנטיות, חום ואופטיקה - כדי ליצור אמצעי אחסון ייחודי שסיפק פתרון מעניין לצורך באחסון מידע ארכיוני וניתן לשינוי בתקופה שלפני עידן ה-USB והענן.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const modeSelect = document.getElementById('mode-select');
    const writeControls = document.getElementById('write-controls');
    const readControls = document.getElementById('read-controls');
    const setBit0Button = document.getElementById('set-bit-0');
    const setBit1Button = document.getElementById('set-bit-1');
    const readButton = document.getElementById('read-button'); // Added read button
    const diskSpot = document.getElementById('disk-spot');
    const magnetizationArrow = document.getElementById('magnetization-arrow');
    const temperatureIndicator = document.getElementById('temperature-indicator');
    const magneticFieldUp = document.getElementById('magnetic-field-up');
    const magneticFieldDown = document.getElementById('magnetic-field-down');
    const incomingPolarization = document.getElementById('incoming-polarization');
    const reflectedPolarization = document.getElementById('reflected-polarization');
    const polarizationDetector = document.getElementById('polarization-detector');
    const detectedAngleSpan = document.getElementById('detected-angle'); // Renamed for clarity
     const detectorReadout = document.getElementById('detector-readout'); // Added for clarity
    const currentStatus = document.getElementById('current-status');
    const storedBitSpan = document.getElementById('stored-bit');
    const readBitSpan = document.getElementById('read-bit');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationContent = document.getElementById('explanation-content');
    const heatingPulse = diskSpot.querySelector('.heating-pulse'); // Get the pulse element

    let storedBit = '?'; // Can be '0', '1', or '?'
    const kerrRotationDegrees = 15; // Example angle in degrees for Kerr effect (made it slightly larger for visibility)
    let isSimulating = false; // Flag to prevent multiple operations at once

    // --- Helper Functions ---

    function updateStatus(statusText) {
        currentStatus.textContent = statusText;
    }

    function setStoredBit(bit) {
        storedBit = bit;
        storedBitSpan.textContent = storedBit === '?' ? '?' : bit;
        magnetizationArrow.className = 'magnetization-arrow'; // Reset class
        if (storedBit === '0') {
            magnetizationArrow.classList.add('up');
            magnetizationArrow.textContent = '↑';
            magnetizationArrow.style.opacity = '1';
        } else if (storedBit === '1') {
            magnetizationArrow.classList.add('down');
            magnetizationArrow.textContent = '↓';
            magnetizationArrow.style.opacity = '1';
        } else {
             magnetizationArrow.textContent = '?';
             magnetizationArrow.style.opacity = '0.5'; // Indicate unknown state visually
        }
         readBitSpan.textContent = '?'; // Reset read bit on change
         detectedAngleSpan.textContent = '--'; // Reset detected angle
         detectorReadout.textContent = '?'; // Reset detector readout
    }

    function setTemperature(state) {
        diskSpot.classList.remove('hot', 'cool', 'heating');
        diskSpot.classList.add(state);
        temperatureIndicator.textContent = state === 'hot' ? 'חם (מעל Tc)' : 'קר (מתחת לTc)';
         if (state === 'hot') {
             diskSpot.classList.add('heating'); // Trigger pulse animation
         }
    }

    function showMagneticField(direction) {
        magneticFieldUp.classList.remove('active');
        magneticFieldDown.classList.remove('active');
        if (direction === 'up') {
            magneticFieldUp.classList.add('active');
        } else if (direction === 'down') {
            magneticFieldDown.classList.add('active');
        }
    }

     function showPolarizationBeams(incomingOpacity, reflectedOpacity, reflectedRotation = 0) {
         incomingPolarization.style.opacity = incomingOpacity;
         reflectedPolarization.style.opacity = reflectedOpacity;

         // Reset rotation immediately if hiding
         if (reflectedOpacity === 0) {
             reflectedPolarization.style.transition = 'none';
             reflectedPolarization.style.transform = 'rotate(0deg)';
             // Force reflow to apply the non-transitioned change before setting transition back
             reflectedPolarization.offsetHeight;
         }

         // Apply rotation with transition if showing
         if (reflectedOpacity > 0) {
             reflectedPolarization.style.transition = 'transform 1s ease-in-out, opacity 0.5s ease';
             reflectedPolarization.style.transform = `rotate(${reflectedRotation}deg)`;
         }
     }

    function showDetector(opacity) {
        polarizationDetector.style.opacity = opacity;
        detectedAngleSpan.style.opacity = opacity;
         detectorReadout.style.opacity = opacity;
    }

    function setControlsEnabled(enabled) {
        modeSelect.disabled = !enabled;
        setBit0Button.disabled = !enabled;
        setBit1Button.disabled = !enabled;
        readButton.disabled = !enabled;
         isSimulating = !enabled;
    }


    // --- Mode Handling ---

    function setMode(mode) {
         if (isSimulating) return; // Prevent mode change during simulation

        if (mode === 'write') {
            writeControls.style.display = 'flex'; // Use flex for layout
            readControls.style.display = 'none';
             showPolarizationBeams(0, 0); // Hide light beams
             showDetector(0); // Hide detector
            updateStatus('בחר ביט לכתיבה על הדיסק');
             // Ensure spot is cool and magnetization is visible based on stored bit
             setTemperature('cool');
             showMagneticField('none');
             setStoredBit(storedBit); // Refresh magnetization arrow
        } else if (mode === 'read') {
            writeControls.style.display = 'none';
            readControls.style.display = 'block';
             showMagneticField('none'); // Hide magnetic fields
            updateStatus('מוכן לקריאה. לחץ "בצע קריאה"');
             // Ensure spot is cool
             setTemperature('cool');
            // Show polarization beams and detector structure (will become visible with opacity)
            showPolarizationBeams(0, 0); // Start hidden, animation will show
            showDetector(1); // Detector background appears, text hidden
            detectedAngleSpan.textContent = '--';
             detectorReadout.textContent = '?';
        }
    }

    // --- Write Process Simulation ---

    function startWrite(bit) {
         if (isSimulating) return;
         setControlsEnabled(false);

        updateStatus(`מתחיל תהליך כתיבת ביט ${bit}...`);
        setStoredBit('?'); // Indicate state change is starting

        // Step 1: Apply Magnetic Field
        setTimeout(() => {
             showMagneticField(bit === '0' ? 'up' : 'down');
             updateStatus(`מפעיל שדה מגנטי בכיוון ${bit === '0' ? 'למעלה' : 'למטה'}`);
        }, 500); // Delay before field appears

        // Step 2: Heat with Laser
        setTimeout(() => {
            setTemperature('hot');
            updateStatus('מחמם את הנקודה עם לייזר...');
        }, 1500); // Delay after field appears

        // Step 3: Spot is Hot and Field is On - Magnetization changes
        setTimeout(() => {
             updateStatus(`נקודה חמה, שדה פעיל. משנה מגנוט...`);
        }, 2500); // Delay during hot phase

        // Step 4: Cool down, Magnetization locks, Field removed
        setTimeout(() => {
            setTemperature('cool');
            setStoredBit(bit); // Lock in the new bit
            showMagneticField('none');
            updateStatus(`התקררות הסתיימה. ביט ${bit} נכתב ואוחסן!`);
             setControlsEnabled(true);
        }, 3500); // Delay for cooling/locking

    }

    // --- Read Process Simulation ---

    function performRead() {
        if (isSimulating) return;

        if (storedBit === '?') {
            updateStatus('אין ביט אגור לקריאה.');
            readBitSpan.textContent = '?';
            detectedAngleSpan.textContent = '--';
            detectorReadout.textContent = '?';
             showPolarizationBeams(0, 0); // Ensure beams are off
             showDetector(1); // Keep detector visible but show no reading
            return;
        }

         setControlsEnabled(false);
        updateStatus(`מתחיל תהליך קריאת ביט אגור (${storedBit})...`);
         detectedAngleSpan.textContent = '--'; // Reset angle display
         detectorReadout.textContent = '?'; // Reset readout display

        // Step 1: Fire Laser (Low Power) and show incoming beam
        setTimeout(() => {
             updateStatus('שולח קרן לייזר מקוטבת לעבר הדיסק...');
             showPolarizationBeams(1, 0); // Show incoming, hide reflected
        }, 500); // Delay before beam appears

        // Step 2: Beam hits disk, reflected beam appears
         setTimeout(() => {
             updateStatus('הקרן פוגעת בדיסק, האור מוחזר...');
              // Simulate Kerr effect rotation based on stored bit
             let angle = 0;
             if (storedBit === '0') {
                  angle = kerrRotationDegrees; // e.g., Rotate +15 deg for 0
             } else if (storedBit === '1') {
                  angle = -kerrRotationDegrees; // e.g., Rotate -15 deg for 1
             }
              showPolarizationBeams(1, 1, angle); // Show reflected beam with rotation
         }, 1500); // Delay for beam travel to disk and reflection start

        // Step 3: Reflected beam reaches detector, angle is detected
        setTimeout(() => {
             updateStatus('האור המוחזר מגיע לגלאי הקיטוב...');
             let angleDisplay = storedBit === '0' ? `+${kerrRotationDegrees}°` : `-${kerrRotationDegrees}°`;
             detectedAngleSpan.textContent = `זווית: ${angleDisplay}`;
             detectorReadout.textContent = storedBit; // Display the read bit
             readBitSpan.textContent = storedBit;

            updateStatus(`קריאה בוצעה! ביט שנקרא: ${storedBit}`);
             setControlsEnabled(true);
        }, 2500); // Delay for reflected beam travel to detector

         // Step 4: Simulation ends, beams fade out slightly after
         setTimeout(() => {
             showPolarizationBeams(0.5, 0.5, reflectedPolarization.style.transform.match(/rotate\(([^)]+)\)/)[1]); // Keep rotation but reduce opacity
         }, 3500);

    }


    // --- Event Listeners ---

    modeSelect.addEventListener('change', (event) => {
        setMode(event.target.value);
    });

    setBit0Button.addEventListener('click', () => {
        if (modeSelect.value === 'write') {
             startWrite('0');
        }
    });

    setBit1Button.addEventListener('click', () => {
         if (modeSelect.value === 'write') {
            startWrite('1');
        }
    });

     readButton.addEventListener('click', () => {
         if (modeSelect.value === 'read') {
             performRead();
         }
     });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר על זיכרון מגנטי-אופטי' : 'הצג/הסתר הסבר על זיכרון מגנטי-אופטי';
    });


    // --- Initial Setup ---
     setStoredBit('?'); // Start with no bit stored
    setMode('write'); // Start in write mode
     setControlsEnabled(true); // Ensure controls are enabled initially
});
</script>
---