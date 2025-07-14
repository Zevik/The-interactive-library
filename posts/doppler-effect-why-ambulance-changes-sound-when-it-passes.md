---
title: "אפקט דופלר: למה סירנה של אמבולנס משנה צליל כשהוא חולף?"
english_slug: doppler-effect-why-ambulance-changes-sound-when-it-passes
category: "פיזיקה"
tags: [אפקט דופלר, גלים, תדר, קול, פיזיקה]
---
# אפקט דופלר: למה סירנה של אמבולנס משנה צליל כשהוא חולף?
שמעתם פעם סירנה של אמבולנס או ניידת משטרה חולפים במהירות לידכם? האם שמתם לב שהצליל שהם מפיקים משנה את גובהו באופן דרמטי מרגע שהם מתקרבים אליכם ועד שהם מתרחקים? התופעה המרתקת הזו, שנשמעת כמו קסם, היא בעצם ביטוי יומיומי של עיקרון פיזיקלי בסיסי הקשור לתנועה ולגלים – אפקט דופלר. לאפקט הזה יש יישומים לא רק בצפירה של רכב חירום, אלא גם במגוון תחומים מרתקים, ממכ"ם משטרתי ועד לחקר הגלקסיות הרחוקות ביותר ביקום.

<div id="doppler-simulation">
    <div id="background-gradient"></div>
    <div id="wave-plane"></div>
    <div id="waves-container"></div>
    <div id="source" class="object">
        <div class="label">מקור</div>
        <div class="direction-arrow"></div>
    </div>
    <div id="observer" class="object">
         <div class="label">צופה</div>
         <div class="listening-indicator"></div>
    </div>
    <div id="controls">
        <label for="speed-slider">מהירות המקור:</label>
        <input type="range" id="speed-slider" min="-0.9" max="0.9" value="0" step="0.01">
        <span id="current-speed">0.0</span> <span class="unit">x מהירות הגל</span>
        <button id="start-audio" class="control-button" disabled>הפעל אודיו (נדרשת אינטראקציה)</button>
         <span id="audio-status"></span>
    </div>
</div>

<button id="toggle-explanation" class="control-button">הצג הסבר מלא</button>

<div id="explanation" style="display: none;">
    <h2>מה מסתתר מאחורי הצליל המשתנה? הכירו את אפקט דופלר</h2>
    <p>אפקט דופלר הוא תופעה פיזיקלית שבה התדר (ומכאן גם אורך הגל) של גל – בין אם זה גל קול, גל אור או כל גל אחר – משתנה עבור צופה, כאשר מקור הגל או הצופה (או שניהם יחד) נמצאים בתנועה יחסית זה לזה בקו הראייה. במילים פשוטות ונוגעות לצליל: אם מקור קול מתקרב אליך, תשמע אותו בתדר גבוה יותר (כלומר, צליל גבוה יותר) מאשר אם הוא היה נייח. אם הוא מתרחק ממך, תשמע אותו בתדר נמוך יותר (צליל נמוך יותר).</p>

    <h2>איך זה עובד בפועל? דמיינו את הגלים</h2>
    <p>הסבר ויזואלי ועוצמתי לתופעה נעוץ באופן שבו "חזיתות" הגלים מתפשטות במרחב. דמיינו מקור קול קטן שפולט גלים מעגליים (כמו אדוות במים). אם המקור נייח, הוא נמצא במרכז כל הגלים שהוא פולט, וחזיתות הגלים מתפשטות באופן אחיד לכל הכיוונים. צופה בכל נקודה ישמע את הגלים מגיעים אליו במרווחי זמן קבועים, התואמים לתדר האמיתי של המקור.</p>
    <p>אבל מה קורה כשהמקור מתחיל לנוע? דמיינו שהמקור פולט גל, מתקדם קצת, ורק אז פולט את הגל הבא. בכיוון התנועה, המקור "רודף" אחרי הגל הקודם שפלט. התוצאה? המרווחים בין חזיתות הגלים בכיוון זה מתקצרים, הם "נדחסים". בכיוון ההפוך, המקור מתרחק מהגל הקודם, והמרווחים בין חזיתות הגלים "נמתחים" ומתארכים. צופה בכיוון ההתקרבות יקלוט גלים בתכיפות גדולה יותר (תדר גבוה), וצופה בכיוון ההתרחקות יקלוט גלים בתכיפות נמוכה יותר (תדר נמוך). הסימולציה שלמעלה מדגימה בדיוק את הדחיסה והמתיחה הזו של הגלים.</p>

    <h2>תרחישים נפוצים:</h2>
    <ul>
        <li>**מקור נע, צופה נייח:** זהו המקרה הקלאסי של האמבולנס. אתם עומדים בצד הדרך (צופה נייח) והאמבולנס עם הסירנה (מקור נע) מתקרב, חולף ומתרחק. כשהוא מתקרב, התדר הנקלט באוזניכם גבוה מהתדר האמיתי של הסירנה. ברגע שהוא חולף על פניכם, התדר הנקלט יורד בצורה ניכרת ומהירה, ונעשה נמוך מהתדר האמיתי כשהוא מתרחק. בסימולציה זו מדגימה בעיקר מקרה של תנועה על קו ישר שעובר דרך הצופה או קרוב אליו.</li>
        <li>**צופה נע, מקור נייח:** גם אם אתם בתנועה והמקור נייח, תתרחש תופעת דופלר. לדוגמה, אם תרוצו לכיוון פעמון נייח, "תפגשו" את הגלים שהוא פולט בקצב מהיר יותר, ולכן תשמעו צליל מעט גבוה יותר. אם תתרחקו בריצה, תשמעו צליל נמוך יותר. חשוב לציין שהאפקט על התדר זהה בשני המקרים כאשר המהירות היחסית זהה, אך יש הבדלים קלים בניתוח הפיזיקלי המדויק, במיוחד במהירויות גבוהות.</li>
    </ul>

    <h2>הנוסחה הפיזיקלית (לסקרנים):</h2>
    <p>הקשר המתמטי בין התדר הנקלט (f<sub>l</sub>, frequency of listener) לתדר הנפלט על ידי המקור (f<sub>s</sub>, frequency of source) במקרה של תנועה יחסית בקו ישר הוא:</p>
    <p style="text-align: center; font-size: 1.2em; font-weight: bold;">f<sub>l</sub> = f<sub>s</sub> * ((v + v<sub>l</sub>) / (v + v<sub>s</sub>))</p>
    <p>כאשר:</p>
    <ul>
        <li>**v** היא מהירות התפשטות הגל במתווה (למשל, מהירות הקול באוויר). בסימולציה שלנו, זוהי מהירות התפשטות העיגולים.</li>
        <li>**v<sub>l</sub>** היא מהירות הצופה ביחס למתווה. היא חיובית אם הצופה מתקרב למקור, ושלילית אם הוא מתרחק. בסימולציה שלנו, הצופה נייח, ולכן v<sub>l</sub> = 0.</li>
        <li>**v<sub>s</sub>** היא מהירות המקור ביחס למתווה. בגרסה הנפוצה של הנוסחה הזו, v<sub>s</sub> חיובית אם המקור מתרחק מהצופה, ושלילית אם הוא מתקרב.</li>
    </ul>
    <p>שימו לב שיש מוסכמות סימן שונות מעט בספרים שונים, אך הרעיון המרכזי נשאר זהה: תנועה יחסית של התקרבות מגדילה את התדר הנקלט, ותנועה יחסית של התרחקות מקטינה אותו. הסימולציה שלנו מחשבת את התדר הנקלט על סמך הרכיב של מהירות המקור בכיוון הצופה.</p>


    <h2>מעבר לאמבולנס: יישומים מפתיעים של אפקט דופלר</h2>
    <p>אפקט דופלר אינו רק עניין אקדמי או תופעת לוואי של סירנות. הוא כלי רב עוצמה שמשמש במגוון עצום של טכנולוגיות ותחומי מדע:</p>
    <ul>
        <li>**רדאר משטרתי:** כלי האכיפה המוכר ביותר משתמש בגלי רדיו. המכ"ם שולח גלי רדיו לעבר מכונית, והם מוחזרים ממנה (הד). אם המכונית נעה, תדר גלי הרדיו המוחזרים משתנה בהתאם למהירותה היחסית עקב אפקט דופלר. המכשיר מנתח את שינוי התדר ומחשב את מהירות הרכב.</li>
        <li>**אולטרסאונד רפואי:** מכשירים אלו משתמשים בגלי קול בתדר גבוה במיוחד. "דופלר זרימה" הוא טכניקה באולטרסאונד המשתמשת באפקט דופלר למדידת מהירות וכיוון זרימת הדם בכלי הדם. גלי הקול מוחזרים מתאי הדם האדומים, ושינוי התדר שלהם מאפשר לחשב את מהירות הזרימה.</li>
        <li>**אסטרונומיה וחקר היקום:** אחד היישומים המדהימים ביותר הוא באסטרונומיה. אור מכוכבים וגלקסיות רחוקות עובר גם הוא אפקט דופלר עקב תנועתם היחסית אלינו. אם גלקסיה מתרחקת, אורכה גל האור שהיא פולטת "נמתח" לכיוון האדום של הספקטרום ("הסחה לאדום" - Redshift). אם היא מתקרבת, אורכה גל האור "נדחס" לכיוון הכחול ("הסחה לכחול" - Blueshift). מדידת הסחה זו מאפשרת לאסטרונומים לדעת את מהירות גרמי השמיים, ואף הובילה לגילוי המרעיש שהיקום כולו מתפשט (רוב הגלקסיות מראות הסחה לאדום).</li>
        <li>**מטאורולוגיה (חיזוי מזג אוויר):** מכ"מי דופלר המשמשים לחיזוי מזג אוויר יכולים לנתח את מהירות תנועת טיפות הגשם והאוויר בתוך סופות, ובכך לספק מידע חיוני על מבנה הסופה, סיכון לטורנדו ועוד.</li>
    </ul>
    <p>כפי שניתן לראות, אפקט דופלר הוא לא רק סקרנות פיזיקלית, אלא עיקרון יסוד שמעצב את הבנתנו את העולם סביבנו ואת היקום הגדול, ומאפשר פיתוח טכנולוגיות חיוניות.</p>
</div>

<style>
/* כלל עיצוב כללי - שפה עברית */
body {
    direction: rtl;
    text-align: right;
    font-family: 'Arial Hebrew', sans-serif; /* או פונט עברי נעים אחר */
    line-height: 1.6;
    color: #333;
}

h1, h2 {
    color: #005662; /* גוון טורקיז עמוק יותר */
    text-align: center;
    margin-bottom: 15px;
}

p {
    margin-bottom: 10px;
}

ul {
    margin-bottom: 10px;
}

/* שדרוג ויזואלי של הסימולציה */
#doppler-simulation {
    width: 95%; /* גמישות רבה יותר */
    max-width: 800px;
    height: 350px; /* גובה מעט יותר */
    border: 1px solid #005662; /* מסגרת תואמת לצבעים */
    border-radius: 10px; /* פינות מעוגלות */
    margin: 20px auto;
    position: relative;
    overflow: hidden;
    background: linear-gradient(to bottom, #e0f7fa, #b2ebf2); /* רקע גרדיאנט עדין */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* צל עדין */
}

#background-gradient {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1; /* מאחורי הגלים והאובייקטים */
}

#wave-plane {
    position: absolute;
    top: 50%;
    left: 0;
    width: 100%;
    height: 2px; /* קו דמיוני של "מדיום" */
    background-color: rgba(0, 0, 0, 0.1); /* קו עדין */
    z-index: 5;
}


.object {
    width: 24px; /* גודל מעט גדול יותר */
    height: 24px;
    border-radius: 50%;
    position: absolute;
    top: 50%;
    transform: translate(-50%, -50%);
    z-index: 15; /* מעל הכל */
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.7em;
    font-weight: bold;
    color: white;
    text-shadow: 0 0 3px rgba(0,0,0,0.5);
}

.object .label {
    position: absolute;
    bottom: -20px;
    width: max-content;
    font-size: 0.8em;
    color: #333;
    text-shadow: none;
}

#source {
    background-color: #ff5722; /* Deep Orange */
    box-shadow: 0 0 8px rgba(255, 87, 34, 0.7); /* זוהר עדין */
    transition: background-color 0.2s ease; /* מעבר צבע חלק */
}

#observer {
    background-color: #1e88e5; /* Blue */
    box-shadow: 0 0 8px rgba(30, 136, 229, 0.7); /* זוהר עדין */
    transition: background-color 0.2s ease; /* מעבר צבע חלק */
}

.listening-indicator {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.8);
    opacity: 0; /* נסתר כברירת מחדל */
    animation: pulse-indicator 1s infinite ease-out; /* אנימציה עדינה */
    animation-play-state: paused; /* בהשהיה כברירת מחדל */
}

.observer-listening .listening-indicator {
     opacity: 1;
     animation-play-state: running;
}


@keyframes pulse-indicator {
    0% { transform: scale(0.5); opacity: 0.8; }
    50% { transform: scale(1.2); opacity: 0.2; }
    100% { transform: scale(0.5); opacity: 0.8; }
}


#waves-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none; /* מאפשר הקלקה דרך אל הרקע או בקרות */
    overflow: hidden;
    z-index: 10; /* מעל הרקע, מתחת לאובייקטים */
}

.wave {
    position: absolute;
    /* Initially set by JS */
    border: 2px solid rgba(255, 87, 34, 0.6); /* צבע גל תואם למקור, שקיפות */
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 1;
    box-sizing: border-box;
    /* Animation handled by JS updating size and opacity, can add CSS transitions if preferred */
}

.wave.high-freq {
    border-color: rgba(255, 0, 0, 0.6); /* צבע אדום לתדר גבוה */
     border-width: 3px; /* קו מעט עבה יותר */
}

.wave.low-freq {
     border-color: rgba(0, 0, 255, 0.6); /* צבע כחול לתדר נמוך */
}

/* בקרות שדרוג */
#controls {
    position: absolute;
    bottom: 15px; /* מרחק מהתחתית */
    left: 15px; /* מרחק מהצד */
    background-color: rgba(255, 255, 255, 0.9); /* רקע מעט שקוף */
    padding: 12px;
    border-radius: 8px; /* פינות מעוגלות יותר */
    z-index: 20;
    display: flex;
    align-items: center;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* צל קטן */
}

#controls label {
    margin-right: 8px;
    font-size: 0.9em;
    font-weight: bold;
    color: #005662;
}

#controls input[type="range"] {
    width: 180px; /* רוחב גדול יותר */
    margin-right: 8px;
    /* ניתן לעצב את הסליידר עצמו בצורה מתקדמת יותר באמצעות CSS */
}

#controls span#current-speed {
    font-family: 'Courier New', monospace;
    min-width: 40px; /* רוחב קבוע לתצוגת המהירות */
    text-align: center;
    font-weight: bold;
    color: #333;
}

.unit {
    font-size: 0.8em;
    color: #555;
    margin-left: 3px;
}

.control-button {
    margin-left: 10px;
    padding: 8px 15px;
    font-size: 0.9em;
    cursor: pointer;
    background-color: #00796b; /* Teal */
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.2s ease, transform 0.1s ease;
}

.control-button:hover:not(:disabled) {
    background-color: #004d40; /* Teal כהה יותר */
    transform: translateY(-1px);
}

.control-button:active:not(:disabled) {
     transform: translateY(0);
}

.control-button:disabled {
    background-color: #b2dfdb; /* Teal בהיר יותר */
    cursor: not-allowed;
}

#audio-status {
    margin-left: 10px;
    font-size: 0.8em;
    color: #00796b;
    min-width: 80px;
    text-align: right;
}


/* הסבר שדרוג ויזואלי */
#explanation {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #b2ebf2; /* מסגרת בהירה */
    background-color: #e0f7fa; /* רקע בהיר */
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: opacity 0.3s ease-in-out; /* מעבר חלק להופעה/הסתרה */
    opacity: 0; /* נסתר כברירת מחדל */
    height: 0;
    overflow: hidden;
}

#explanation.visible {
    opacity: 1;
    height: auto; /* גובה אוטומטי */
}

#explanation h2 {
    color: #00796b;
    margin-top: 0; /* אין רווח עליון בראש ההסבר */
    margin-bottom: 10px;
    font-size: 1.4em;
    border-bottom: 1px solid #b2dfdb; /* קו תחתון לכותרת */
    padding-bottom: 5px;
}

#explanation ul {
    margin-top: 10px;
    padding-right: 20px; /* ריווח מימין ברשימה */
}

#explanation li {
    margin-bottom: 8px;
}

#toggle-explanation {
    display: block;
    margin: 20px auto;
    padding: 12px 20px;
    font-size: 1em;
    font-weight: bold;
}

/* הוספת אנימציות ותחושת "משחק" (באמצעות JS ושינוי CSS) */
/* אנימציה עדינה של המקור */
.source-moving {
    /* אין צורך באנימציה CSS ישירה לתנועה, היא מבוצעת ב-JS */
}

/* אנימציה של גלים - מבוצעת ב-JS ע"י שינוי גודל ושקיפות */
/* ניתן להוסיף אנימציות נוספות כאן אם נדרש, למשל טשטוש תנועה */

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const simulationContainer = document.getElementById('doppler-simulation');
    const sourceElement = document.getElementById('source');
    const observerElement = document.getElementById('observer');
    const wavesContainer = document.getElementById('waves-container');
    const speedSlider = document.getElementById('speed-slider');
    const currentSpeedSpan = document.getElementById('current-speed');
    const startAudioButton = document.getElementById('start-audio');
    const audioStatusSpan = document.getElementById('audio-status');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const observerListeningIndicator = observerElement.querySelector('.listening-indicator');


    // --- Simulation Parameters ---
    // Get dimensions dynamically if needed, but for now match CSS/design intent
    const SIM_WIDTH = simulationContainer.offsetWidth; // Use actual rendered width
    const SIM_HEIGHT = simulationContainer.offsetHeight; // Use actual rendered height
    const SOURCE_SIZE = sourceElement.offsetWidth;
    const OBSERVER_SIZE = observerElement.offsetWidth;

    const WAVE_SPEED_PIXELS_PER_SEC = 150; // Speed of wave expansion in pixels/sec - increased for more visual dynamics
    const BASE_FREQUENCY_HZ = 330; // Hz - E4 note, slightly more pleasant than A4?
    const SIM_SPEED_SCALE = 1.0; // Factor to speed up/slow down simulation time relative to real time
    // Generate waves less often than real frequency for visual clarity
    const VISUAL_WAVE_RATE_HZ = BASE_FREQUENCY_HZ / 15; // Generate 1/15th of the actual waves visually
    const WAVE_GENERATION_INTERVAL_SIM_SEC = 1 / VISUAL_WAVE_RATE_HZ;
    const MAX_WAVE_RADIUS = Math.max(SIM_WIDTH, SIM_HEIGHT) * 1.5; // Waves disappear after reaching this size - slightly larger margin
     const AUDIO_UPDATE_INTERVAL_MS = 50; // Update audio frequency every X ms

    // --- State Variables ---
    // Source starts left, moves towards center
    let sourceX = SIM_WIDTH * 0.1;
    const sourceY = SIM_HEIGHT / 2; // Assume objects are centered vertically
    const observerX = SIM_WIDTH / 2;
    const observerY = SIM_HEIGHT / 2;
    let sourceVelocityRatio = parseFloat(speedSlider.value); // Ratio relative to wave speed
    let sourceVelocityPixelsPerSecond = sourceVelocityRatio * WAVE_SPEED_PIXELS_PER_SEC; // Pixels/sec
    let waves = []; // Array to hold wave objects { element, originX, originY, startTimeSim }
    let lastWaveTimeSim = 0;
    let simulationTime = 0; // Simulation time in seconds
    let lastTime; // For animation frame deltaTime

    // --- Audio Context ---
    let audioContext = null;
    let oscillator = null;
    let gainNode = null;
    let isAudioStarted = false;
    let audioIntervalId = null;

    // Set initial positions
    sourceElement.style.left = `${sourceX}px`;
    sourceElement.style.top = `${sourceY}px`;
    observerElement.style.left = `${observerX}px`;
    observerElement.style.top = `${observerY}px`;

    // Enable audio button after DOM is ready
    startAudioButton.disabled = false;
    audioStatusSpan.textContent = 'אודיו מושהה';
     observerElement.classList.remove('observer-listening');


    // Function to initialize and start audio
    function startAudio() {
        if (isAudioStarted) return;

        try {
            audioContext = new (window.AudioContext || window.webkitAudioContext)();
            oscillator = audioContext.createOscillator();
            gainNode = audioContext.createGain();

            oscillator.type = 'sine'; // Basic sine wave
            oscillator.frequency.setValueAtTime(BASE_FREQUENCY_HZ, audioContext.currentTime); // Start at base frequency
            gainNode.gain.setValueAtTime(0.3, audioContext.currentTime); // Volume control (0 to 1) - slightly lower volume
            gainNode.gain.linearRampToValueAtTime(0.5, audioContext.currentTime + 0.1); // Fade in volume

            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);

            oscillator.start();
            isAudioStarted = true;
            startAudioButton.textContent = 'אודיו מופעל';
            startAudioButton.disabled = true; // Disable after starting, user can't stop/restart simple sim
            audioStatusSpan.textContent = ''; // Clear status
            observerElement.classList.add('observer-listening'); // Add listening animation class

            // Start audio frequency update loop
            audioIntervalId = setInterval(updateAudioFrequency, AUDIO_UPDATE_INTERVAL_MS);

        } catch (e) {
            console.error('Web Audio API is not supported or failed to start:', e);
            startAudioButton.textContent = 'שגיאת אודיו';
            startAudioButton.disabled = true;
            audioStatusSpan.textContent = 'שגיאה';
        }
    }

     function stopAudio() {
         if (!isAudioStarted) return;

         if (audioIntervalId) {
             clearInterval(audioIntervalId);
             audioIntervalId = null;
         }

         if (oscillator) {
             oscillator.stop(audioContext.currentTime + 0.1); // Fade out
             oscillator = null;
         }
         if (gainNode) {
             gainNode.disconnect();
             gainNode = null;
         }
         if (audioContext && audioContext.state !== 'closed') {
              audioContext.close().then(() => {
                 audioContext = null;
                 isAudioStarted = false;
                 startAudioButton.textContent = 'הפעל אודיו';
                 startAudioButton.disabled = false;
                 audioStatusSpan.textContent = 'אודיו מושהה';
                 observerElement.classList.remove('observer-listening');
              });
         } else {
              isAudioStarted = false;
              startAudioButton.textContent = 'הפעל אודיו';
              startAudioButton.disabled = false;
              audioStatusSpan.textContent = 'אודיו מושהה';
              observerElement.classList.remove('observer-listening');
         }

     }


    startAudioButton.addEventListener('click', startAudio);


    speedSlider.addEventListener('input', (event) => {
        // Map slider value (-0.9 to 0.9) to velocity ratio relative to wave speed.
        const vSourceRatio = parseFloat(event.target.value);
        sourceVelocityRatio = vSourceRatio;
        sourceVelocityPixelsPerSecond = vSourceRatio * WAVE_SPEED_PIXELS_PER_SEC;
        currentSpeedSpan.textContent = vSourceRatio.toFixed(1); // Display ratio

        // Start audio on first slider interaction if not started (alternative trigger)
        if (!isAudioStarted && Math.abs(sourceVelocityRatio) > 0.01) {
             // Don't auto-start immediately, the button click is the required gesture.
             // User must click the button first. Slider only controls speed *after* audio is enabled.
             // Let's leave the button as the explicit audio start.
        }
         // Update arrow direction visually (basic)
         const arrow = sourceElement.querySelector('.direction-arrow');
         if (sourceVelocityRatio > 0.05) {
             arrow.style.display = 'block';
             arrow.style.transform = 'translate(-50%, -50%) rotate(0deg)'; // Right
         } else if (sourceVelocityRatio < -0.05) {
             arrow.style.display = 'block';
             arrow.style.transform = 'translate(-50%, -50%) rotate(180deg)'; // Left
         } else {
             arrow.style.display = 'none'; // Hide if velocity is near zero
         }
    });

    // Initial arrow state
    const initialArrow = sourceElement.querySelector('.direction-arrow');
    initialArrow.style.display = 'none'; // Hide arrow initially


    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.height === '0px';
        if (isHidden) {
            explanationDiv.style.display = 'block';
            // Force reflow to ensure transition works from height 0
            explanationDiv.offsetHeight;
            explanationDiv.classList.add('visible');
            toggleExplanationButton.textContent = 'הסתר הסבר מלא';
        } else {
             explanationDiv.classList.remove('visible');
             // Set a timeout to hide completely after transition
             setTimeout(() => {
                 explanationDiv.style.display = 'none';
             }, 300); // Match CSS transition duration
            toggleExplanationButton.textContent = 'הצג הסבר מלא';
        }
    });

    // Initial state for explanation on load
    if(explanationDiv.classList.contains('visible')) {
         explanationDiv.style.display = 'block'; // Ensure it's block if CSS makes it visible initially
         toggleExplanationButton.textContent = 'הסתר הסבר מלא';
    } else {
        explanationDiv.style.display = 'none'; // Ensure it's hidden if CSS doesn't make it visible
        explanationDiv.style.height = '0'; // Ensure height is 0 for transition
        explanationDiv.style.opacity = '0'; // Ensure opacity is 0 for transition
        toggleExplanationButton.textContent = 'הצג הסבר מלא';
    }


    function updateAudioFrequency() {
        if (!isAudioStarted || !oscillator || !audioContext) return;

        // Calculate instantaneous distance between source and observer
        const dx = observerX - sourceX;
        const dy = observerY - sourceY; // In this 1D sim, dy is always 0, but useful for generalization
        const distance = Math.sqrt(dx * dx + dy * dy);

        // Avoid division by zero or issues when distance is tiny
        if (distance < 5) { // Source is very close to observer's X position
             // The frequency should be close to the base frequency when the source is directly
             // in front of/behind the observer, and rapidly change sign as it passes.
             // Let's simplify and use the base frequency when source is directly aligned vertically.
             // For motion along X, this occurs when dx is near zero.
             // A smooth transition is needed here. For simplicity, use the formula, it handles dx=0 gracefully.
             // If source is exactly at observerX and moving horizontally, velocity component towards observer is 0.
        }

        // Calculate the component of source velocity along the line connecting source to observer
        // Velocity vector of source: (sourceVelocityPixelsPerSecond, 0)
        // Unit vector from source to observer: (dx / distance, dy / distance)
        // v_s_towards_observer = dot(SourceVelocityVector, UnitVector_SO)
        // v_s_towards_observer = sourceVelocityPixelsPerSecond * (dx / distance) + 0 * (dy / distance)
        let v_s_towards_observer = 0;
        if (distance > 0.1) { // Avoid division by tiny distance
             v_s_towards_observer = sourceVelocityPixelsPerSecond * (dx / distance);
        }
         // If distance is ~0, source is AT observer. Velocity component towards is ambiguous/rapidly changing.
         // Our formula naturally gives 0 when dx=0, assuming dy=0.

        // Doppler formula for stationary observer, moving source:
        // f_observed = f_source * (v_wave / (v_wave - v_s_towards_observer))
        // where v_s_towards_observer is positive if source moves TOWARDS observer.

        let f_observed = BASE_FREQUENCY_HZ;
        const denominator = WAVE_SPEED_PIXELS_PER_SEC - v_s_towards_observer;

        // Handle cases where source velocity towards observer is >= wave speed (sonic boom territory, not simulated visually)
        if (Math.abs(denominator) > 0.1) { // Avoid near-zero or negative denominator
             f_observed = BASE_FREQUENCY_HZ * (WAVE_SPEED_PIXELS_PER_SEC / denominator);

             // Clamp frequency to a reasonable audible range for the simulation
             const maxFreq = BASE_FREQUENCY_HZ * 3; // Cap high frequency
             const minFreq = BASE_FREQUENCY_HZ * 0.5; // Cap low frequency
             f_observed = Math.max(minFreq, Math.min(maxFreq, f_observed));

        } else {
             // Denominator is near zero or negative (source moving near/above wave speed towards observer)
             // This causes frequency to spike very high theoretically. In audible simulation, cap it.
             if (v_s_towards_observer > 0) { // Moving towards observer
                  f_observed = BASE_FREQUENCY_HZ * 3; // Cap at max frequency
             } else { // Moving away or stationary near observer (shouldn't hit this case often with >0.1 check)
                  f_observed = BASE_FREQUENCY_HZ * 0.5; // Cap at min frequency or BASE_FREQUENCY_HZ
             }
        }


        // Smoothly update the oscillator frequency
        if (oscillator && audioContext) {
             // Use a smooth transition rather than setting valueAtTime directly
             oscillator.frequency.linearRampToValueAtTime(f_observed, audioContext.currentTime + (AUDIO_UPDATE_INTERVAL_MS / 1000) * 0.8); // Ramp over most of the interval
        }

         // Visual feedback: change wave color based on perceived frequency at observer?
         // This is tricky as waves are generated at the source's perceived frequency at creation time.
         // A simpler approach: Change observer color or add indicator animation based on the calculated f_observed.
         // Add class to observer based on frequency deviation
         const freqRatio = f_observed / BASE_FREQUENCY_HZ;
         if (freqRatio > 1.1) { // Significantly higher
             observerElement.style.backgroundColor = '#ef5350'; // Reddish
         } else if (freqRatio < 0.9) { // Significantly lower
             observerElement.style.backgroundColor = '#42a5f5'; // Bluish
         } else { // Near base frequency
              observerElement.style.backgroundColor = '#1e88e5'; // Original blue
         }
    }


    function updateSimulation(currentTime) {
        if (lastTime === undefined) lastTime = currentTime;
        const deltaTime = (currentTime - lastTime) / 1000; // Delta time in seconds
        lastTime = currentTime;

        const simDeltaTime = deltaTime * SIM_SPEED_SCALE;
        simulationTime += simDeltaTime;

        // --- Update Source Position ---
        sourceX += sourceVelocityPixelsPerSecond * simDeltaTime;

        // Bounce off walls with a slight damping/visual cue
        const bouncePadding = SOURCE_SIZE / 2; // Bounce when center is near edge
        if (sourceX < bouncePadding) {
            sourceX = bouncePadding;
            sourceVelocityPixelsPerSecond *= -0.9; // Bounce and lose some speed
            sourceVelocityRatio = sourceVelocityPixelsPerSecond / WAVE_SPEED_PIXELS_PER_SEC;
            speedSlider.value = sourceVelocityRatio.toFixed(2);
            currentSpeedSpan.textContent = sourceVelocityRatio.toFixed(1);
        } else if (sourceX > SIM_WIDTH - bouncePadding) {
            sourceX = SIM_WIDTH - bouncePadding;
            sourceVelocityPixelsPerSecond *= -0.9; // Bounce and lose some speed
            sourceVelocityRatio = sourceVelocityPixelsPerSecond / WAVE_SPEED_PIXELS_PER_SEC;
            speedSlider.value = sourceVelocityRatio.toFixed(2);
            currentSpeedSpan.textContent = sourceVelocityRatio.toFixed(1);
        }

        sourceElement.style.left = `${sourceX}px`;

        // --- Generate New Waves ---
        if (simulationTime - lastWaveTimeSim >= WAVE_GENERATION_INTERVAL_SIM_SEC) {
            waves.push({
                element: null, // Will create on first render
                originX: sourceX, // Wave originates from source's position at time of emission
                originY: sourceY,
                startTimeSim: simulationTime // Time in simulation seconds when wave was emitted
            });
            lastWaveTimeSim = simulationTime;
        }

        // --- Update Waves ---
        const wavesToRemove = [];
        waves.forEach((wave, index) => {
            const elapsedSimTime = simulationTime - wave.startTimeSim;
            const radius = WAVE_SPEED_PIXELS_PER_SEC * elapsedSimTime;

            if (radius > MAX_WAVE_RADIUS) {
                wavesToRemove.push(index);
                if (wave.element) {
                    wave.element.remove(); // Remove the DOM element
                }
            } else {
                if (!wave.element) {
                    // Create element if it doesn't exist yet
                    wave.element = document.createElement('div');
                    wave.element.classList.add('wave');
                    wavesContainer.appendChild(wave.element);
                     // Set initial style on creation
                    wave.element.style.width = `0px`;
                    wave.element.style.height = `0px`;
                    wave.element.style.left = `${wave.originX}px`;
                    wave.element.style.top = `${wave.originY}px`;
                    wave.element.style.opacity = 1; // Start fully opaque
                }
                // Update element style
                const size = radius * 2;
                wave.element.style.width = `${size}px`;
                wave.element.style.height = `${size}px`;

                // Fade out as waves expand - fade starts later
                wave.element.style.opacity = Math.max(0, 1 - (radius / MAX_WAVE_RADIUS) * 1.5); // Fade out faster towards the end

                // Optional: Change wave color/style based on emission frequency IF source frequency wasn't constant
                // For this sim, source frequency is constant, only the *perceived* frequency changes.
                // Could add classes based on which side they were emitted from if source is moving,
                // to visually emphasize the compressed/stretched side.
                if (sourceVelocityPixelsPerSecond > 0.01 && wave.originX < SIM_WIDTH * 0.5) { // Emitted while moving right (towards observer)
                     // wave.element.classList.add('high-freq'); // Visual cue for compression (only if moving right AND left of observer)
                     // wave.element.classList.remove('low-freq');
                } else if (sourceVelocityPixelsPerSecond < -0.01 && wave.originX > SIM_WIDTH * 0.5) { // Emitted while moving left (towards observer)
                      // wave.element.classList.add('high-freq'); // Visual cue for compression (only if moving left AND right of observer)
                     // wave.element.classList.remove('low-freq');
                } else if (sourceVelocityPixelsPerSecond > 0.01 && wave.originX > SIM_WIDTH * 0.5) { // Emitted while moving right (away from observer)
                     // wave.element.classList.add('low-freq'); // Visual cue for stretching
                     // wave.element.classList.remove('high-freq');
                } else if (sourceVelocityPixelsPerSecond < -0.01 && wave.originX < SIM_WIDTH * 0.5) { // Emitted while moving left (away from observer)
                     // wave.element.classList.add('low-freq'); // Visual cue for stretching
                     // wave.element.classList.remove('high-freq');
                } else {
                    // Remove high/low freq classes if source is stationary
                     // wave.element.classList.remove('high-freq', 'low-freq');
                }
                // Simplified: Just color the waves based on whether they were emitted while source was moving
                if (Math.abs(sourceVelocityRatio) > 0.01) {
                     if (sourceVelocityRatio > 0 && wave.originX < observerX) { /* Moving right towards observer when emitted */ wave.element.style.borderColor = 'rgba(255, 0, 0, 0.6)'; }
                     else if (sourceVelocityRatio < 0 && wave.originX > observerX) { /* Moving left towards observer when emitted */ wave.element.style.borderColor = 'rgba(255, 0, 0, 0.6)'; }
                     else if (sourceVelocityRatio > 0 && wave.originX > observerX) { /* Moving right away from observer when emitted */ wave.element.style.borderColor = 'rgba(0, 0, 255, 0.6)'; }
                      else if (sourceVelocityRatio < 0 && wave.originX < observerX) { /* Moving left away from observer when emitted */ wave.element.style.borderColor = 'rgba(0, 0, 255, 0.6)'; }
                      else { wave.element.style.borderColor = 'rgba(255, 87, 34, 0.6)'; } // Default if calculation is tricky near observer X
                } else {
                    wave.element.style.borderColor = 'rgba(255, 87, 34, 0.6)'; // Default color when source is stationary
                }

            }
        });

        // Remove waves that are too large
        for (let i = wavesToRemove.length - 1; i >= 0; i--) {
            waves.splice(wavesToRemove[i], 1);
        }

        requestAnimationFrame(updateSimulation);
    }

    // Start the simulation loop
    requestAnimationFrame(updateSimulation);

});
</script>
---
```