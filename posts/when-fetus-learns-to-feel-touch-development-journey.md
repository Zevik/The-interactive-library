---
title: "מסע החושים: כשהעובר לומד לחוש מגע"
english_slug: when-fetus-learns-to-feel-touch-development-journey
category: "מדעי המוח"
tags: [התפתחות עוברית, מערכת מישוש, מערכת עצבים, חישה, הריון, התפתחות סנסומוטורית]
---
<h1>מסע החושים: כשהעובר לומד לחוש מגע</h1>

<p>מתי בפעם הראשונה עובר מרגיש מגע בבטן? האם מגע עדין מרגיש לו כמו דקירה, או שמא יש הבדל באופן שבו הוא חווה גירויים שונים במהלך ההריון? הצטרפו למסע מרתק אל תוך רחם וגלו כיצד מתפתחת מערכת המישוש, חוש החקר הראשוני של העובר.</p>

<div id="app-container">
    <div id="timeline-area">
        <label for="week-slider">שבוע הריון:</label>
        <input type="range" id="week-slider" min="8" max="40" value="8">
        <span id="current-week">שבוע 8</span>
    </div>

    <div id="fetus-area">
        <!-- Replaced placeholder with a hypothetical, cleaner diagram URL -->
        <img src="https://interactive.example.com/images/fetus-diagram-clean.svg" alt="איור התפתחות העובר" id="fetus-diagram">
        <div id="fetus-highlights">
            <!-- Dynamic highlight elements will be added here -->
        </div>
    </div>

    <div id="stimulation-area">
        <h3>בחרו גירוי לחקור:</h3>
        <button class="stimulus-button" data-stimulus="touch">מגע עדין</button>
        <button class="stimulus-button" data-stimulus="pressure">לחץ קל</button>
        <button class="stimulus-button" data-stimulus="temperature">טמפרטורה</button>
        <!-- Consider adding vibration later if complexity allows -->
    </div>

    <div id="response-area">
        <h3>תגובת העובר ותפיסתו המשוערת:</h3>
        <p id="perception-text">בחרו שבוע בציר הזמן ובחרו סוג גירוי כדי לגלות מה העובר מרגיש.</p>
    </div>
</div>

<style>
    /* CSS styles for the interactive component */
    #app-container {
        direction: rtl;
        font-family: 'Arial', sans-serif; /* Use a common system font stack */
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px; /* Increased gap for better spacing */
        padding: 30px; /* More padding */
        border: 1px solid #e0e0e0; /* Lighter border */
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* Clean white background */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08); /* Subtle shadow */
        max-width: 700px; /* Limit max width */
        margin: 20px auto; /* Center the container */
    }

    h1 {
        text-align: center;
        color: #333; /* Darker heading color */
        margin-bottom: 20px;
    }

    p {
        color: #555;
        line-height: 1.7;
    }

    #timeline-area {
        width: 100%;
        max-width: 600px;
        text-align: center;
        display: flex; /* Align slider and text */
        align-items: center;
        gap: 15px;
    }

    #timeline-area label {
        font-weight: bold;
        color: #333;
        flex-shrink: 0; /* Prevent label from shrinking */
    }

    #week-slider {
        flex-grow: 1; /* Slider takes available space */
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        height: 8px;
        background: linear-gradient to right, #a8dadc, #457b9d; /* Gradient track */
        outline: none;
        opacity: 0.8;
        transition: opacity .2s;
        border-radius: 4px;
    }

    #week-slider:hover {
        opacity: 1;
    }

    #week-slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #1d3557; /* Darker thumb color */
        border: 2px solid #f1faee;
        border-radius: 50%;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

     #week-slider::-webkit-slider-thumb:hover {
        background-color: #457b9d;
        transform: scale(1.1);
     }

    #week-slider::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #1d3557;
        border: 2px solid #f1faee;
        border-radius: 50%;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    #week-slider::-moz-range-thumb:hover {
        background-color: #457b9d;
        transform: scale(1.1);
    }


    #current-week {
        font-weight: bold;
        color: #1d3557; /* Dark blue */
        font-size: 1.1em;
        min-width: 80px; /* Reserve space to prevent layout shifts */
        text-align: left;
    }

    #fetus-area {
        position: relative;
        width: 250px; /* Keep initial size, can adjust if diagram changes */
        height: 400px;
        display: flex; /* Center the image */
        justify-content: center;
        align-items: center;
        background-color: #a8dadc; /* Simulate amniotic fluid background */
        border-radius: 8px;
        overflow: hidden; /* Hide highlight overflow */
    }

    #fetus-diagram {
        display: block;
        width: 95%; /* Make it slightly smaller than container */
        height: 95%;
        object-fit: contain; /* Ensure image fits without distortion */
        transition: filter 0.5s ease; /* Smooth transition for filter */
    }

    #fetus-highlights {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none; /* Don't interfere with mouse events */
        overflow: hidden;
    }

    /* Styles for dynamically created highlight elements */
    .highlight {
        position: absolute;
        background-color: rgba(241, 250, 238, 0.6); /* Light color base for highlights */
        border-radius: 50%; /* Default to circular highlights */
        opacity: 0; /* Start hidden */
        transition: opacity 0.5s ease, background-color 0.5s ease, transform 0.5s ease;
        transform: scale(0.8); /* Start slightly smaller */
    }

    .highlight.active {
        opacity: 1;
        transform: scale(1);
    }

    /* Stimulus specific colors for highlights */
    .highlight.touch { background-color: rgba(168, 218, 220, 0.7); } /* Soft blue-green */
    .highlight.pressure { background-color: rgba(69, 123, 157, 0.7); } /* Muted blue */
    .highlight.temperature { background-color: rgba(230, 57, 70, 0.7); } /* Soft red */

    /* Optional: pulsing animation for active highlight */
    .highlight.pulse {
        animation: pulse-animation 1.5s infinite alternate;
    }

    @keyframes pulse-animation {
        from { opacity: 0.7; transform: scale(1); }
        to { opacity: 1; transform: scale(1.05); }
    }


    #stimulation-area {
        text-align: center;
        width: 100%;
    }

    #stimulation-area h3 {
         color: #333;
         margin-bottom: 15px;
    }

    .stimulus-button {
        padding: 12px 20px; /* Larger buttons */
        margin: 5px;
        border: none; /* No border */
        border-radius: 25px; /* Pill shape */
        background-color: #457b9d; /* Muted blue */
        color: white;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        min-width: 100px; /* Ensure consistent width */
    }

    .stimulus-button:hover {
        background-color: #1d3557; /* Darker blue on hover */
    }

    .stimulus-button:active {
         transform: scale(0.98); /* Slight press effect */
    }

    .stimulus-button.active {
        background-color: #e63946; /* Accent color when active */
        font-weight: bold;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }

    #response-area {
        width: 100%;
        max-width: 600px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 8px;
        background-color: #f1faee; /* Very light green background */
        min-height: 100px; /* Ensure enough space for text */
        display: flex;
        flex-direction: column;
        justify-content: center; /* Center text vertically */
    }

    #response-area h3 {
        margin-top: 0;
        color: #333;
        text-align: center;
        margin-bottom: 10px;
    }

    #perception-text {
        text-align: center;
        color: #1d3557; /* Dark blue text */
        font-size: 1.1em;
    }


    /* Styles for the Explanation section */
    #show-explanation-button {
        display: block;
        margin: 30px auto; /* More space above/below */
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* Pill shape */
        background-color: #a8dadc; /* Soft blue-green */
        color: #1d3557; /* Dark blue text */
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #show-explanation-button:hover {
        background-color: #457b9d;
        color: white;
    }
     #show-explanation-button:active {
         transform: scale(0.98);
    }


    #explanation {
        display: none; /* Hidden by default */
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: #f9f9f9; /* Light grey background */
        direction: rtl;
        font-family: 'Arial', sans-serif;
        line-height: 1.8;
        color: #333;
    }

    #explanation h2, #explanation h3 {
        color: #1d3557; /* Dark blue headings */
        margin-top: 20px;
        margin-bottom: 12px;
    }

    #explanation p {
        margin-bottom: 15px;
        color: #555;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Add padding for list bullets */
    }

     #explanation ul li {
         margin-bottom: 8px;
     }

</style>

<button id="show-explanation-button">הצגת המסע המלא: הסבר מעמיק</button>

<div id="explanation">
    <h2>מסע החושים: התפתחות מערכת המישוש בעובר</h2>

    <p>מערכת המישוש, הידועה גם כמערכת הסומטוסנסורית, היא מחלוצות החישה של העובר ואבן יסוד קריטית להתפתחותו. היא מאפשרת לו לא רק לחוש את סביבתו הפנימית והחיצונית (המוגבלת כרגע לרחם), אלא גם לבנות תפיסה של גופו, לפתח תנועה וללמוד. היכולת המופלאה לחוש מגע עדין, לחץ, שינויי טמפרטורה ואף כאב מתפתחת במסע הדרגתי ומרתק במהלך ההריון.</p>

    <h3>נקודת ההתחלה: ניצני הרגישות הראשונים</h3>
    <p>הסימנים הראשונים לרגישות למגע מופיעים מוקדם מאוד. כבר בשבוע 8, אזור הפה והשפתיים הוא הראשון שמגיב במעין רפלקס ראשוני למגע. מכאן, הרגישות מתפשטת במהירות: תחילה לחלקים נוספים בפנים, ולאחר מכן לידיים, לרגליים ולבסוף, מכסה את כל גופו הזעיר של העובר.</p>

    <h3>בניית מפת החושים: התפתחות קולטני המישוש בעור</h3>
    <p>העור, האיבר הגדול ביותר בגוף, הופך למעבדה חושית של ממש בזכות התפתחות מגוון עצום של קולטנים (רצפטורים) ייעודיים:</p>
    <ul>
        <li><strong>מכאנורצפטורים:</strong> אלו הם החיישנים הראשונים שמגיבים לכוחות מכאניים – מגע, לחץ, רטט ואף מתיחה. קולטנים שונים (כמו מייסנר, פאצ'יני, מרקל, רפיני) נוצרים בקצב משתנה, בשכבות עור שונות, והתפתחותם נמשכת גם לאחר הלידה.</li>
        <li><strong>תרמורצפטורים:</strong> קולטים שינויים בטמפרטורה (חום וקור). פעילותם מתגברת בשלבים מאוחרים יותר של ההריון ומאפשרת לעובר לחוש בשינויים בסביבת מי השפיר.</li>
        <li><strong>נוציספטורים (קולטני כאב):</strong> אלו הם קצוות עצב חופשיים המזהים גירויים שעלולים לגרום נזק לרקמה. היכולת לחוש כאב כתחושה מובחנת היא נושא מורכב, אך המסלולים העצביים הבסיסיים הקשורים בתגובה לכאב מתפתחים מוקדם יחסית.</li>
    </ul>

    <h3>סלילת הדרכים העצביות: התפתחות סיבים ומסלולים</h3>
    <p>המידע הנקלט בקולטנים בעור מועבר דרך סיבי עצב תחושתיים אל חוט השדרה ומשם במעלה למוח. זהו תהליך מורכב הכולל צמיחה ענפה של סיבי עצב (עצבוב) לכל פינות הגוף, ובמקביל בניית מסלולים עצביים מרכזיים:</p>
    <ul>
        <li><strong>גזע המוח:</strong> כאן מתבצע עיבוד ראשוני ומתפתחות תגובות רפלקסיביות אוטומטיות.</li>
        <li><strong>תלמוס:</strong> תחנת ממסר מרכזית וחיונית לתפיסה ראשונית של תחושות לפני הגעתן לאזורים הגבוהים במוח. מתפתח מוקדם ופעיל כבר בשלבים אמצעיים של ההריון.</li>
        <li><strong>קורטקס סומטוסנסורי:</strong> אזור מיוחד בקליפת המוח האחראי על העיבוד המתוחכם ביותר: זיהוי מדויק של מיקום המגע, הבדלה בין סוגי גירויים, ואינטגרציה של מידע תחושתי מורכב. אזור זה מבשיל באופן משמעותי לקראת סוף ההריון ולאחר הלידה, ומאפשר תפיסה מודעת ומובחנת יותר.</li>
    </ul>
    <p>ההתפתחות ההדרגתית של מסלולים אלו היא שמעצבת את האופן שבו העובר מגיב - מרפלקסים פשוטים לתפיסה מורכבת.</p>

    <h3>שינויים בתפיסת מגע: ממגע עמום לחישה מובחנת</h3>
    <p>האופן שבו עובר תופס ומגיב למגע משתנה דרמטית:</p>
    <ul>
        <li><strong>שבועות מוקדמים (עד שבוע 20):</strong> התגובה היא בעיקר רפלקסיבית, מקומית ואוטומטית. ייתכן שיש תחושה בסיסית מאוד, אך סביר להניח שהיא עמומה, לא מובחנת ובוודאי לא מלווה בתפיסה מודעת כמו אצל מבוגר.</li>
        <li><strong>שבועות אמצעיים (שבוע 20-30):</strong> עם התפתחות המסלולים המגיעים למוח (ובעיקר לתלמוס), התגובות הופכות מורכבות יותר. יש רגישות גוברת ללחץ, והעובר מגיב בתנועה ברורה יותר למגע, במיוחד באזורים המפותחים כמו פנים וידיים.</li>
        <li><strong>שבועות מאוחרים (משבוע 30 ואילך):</strong> התפתחות הקורטקס הסומטוסנסורי מאפשרת עיבוד עמוק יותר. העובר יכול להבדיל טוב יותר בין סוגי מגע שונים, לזהות מיקום מדויק יחסית, לחוש טמפרטורה, וייתכן שאף לחוות כאב ברמה כלשהי (אם כי חווית הכאב המודעת של מבוגר עדיין אינה קיימת).</li>
    </ul>

    <h3>מגע עצמי וחקירת הסביבה: תנועה ככלי חישה</h3>
    <p>בעיטות, מציצת אגודל, נגיעה בפנים או בדפנות הרחם - תנועות אלו אינן סתם "התפרעויות". הן מהוות מנוע קריטי להתפתחות חוש המישוש ומודעות הגוף. כל מגע עצמי או מגע עם סביבת הרחם שולח פידבק תחושתי למוח, ומסייע לו "למפות" את הגוף ולבנות את התפיסה הפנימית שלו. אינטראקציה בלתי פוסקת זו בין תנועה לחישה היא ליבת ההתפתחות הסנסומוטורית התקינה.</p>

    <h3>סיכום</h3>
    <p>מסע התפתחות מערכת המישוש הוא עדות מדהימה למורכבות החיים המתהווים ברחם. מריפלקסים פשוטים וקולטנים בודדים ועד למערכת משוכללת המסוגלת לעבד מגוון תחושות מורכבות – חוש המישוש מאפשר לעובר לחקור את גופו ואת עולמו עוד לפני שהוא נולד, ומכין אותו לחוויה המלאה של החיים מחוץ לרחם.</p>
</div>

<script>
    // JavaScript for the interactive component
    const weekSlider = document.getElementById('week-slider');
    const currentWeekSpan = document.getElementById('current-week');
    const stimulusButtons = document.querySelectorAll('.stimulus-button');
    const perceptionText = document.getElementById('perception-text');
    const fetusDiagram = document.getElementById('fetus-diagram');
    const fetusHighlightsArea = document.getElementById('fetus-highlights');
    const showExplanationButton = document.getElementById('show-explanation-button');
    const explanationDiv = document.getElementById('explanation');

    let currentWeek = parseInt(weekSlider.value);
    let activeStimulus = null; // 'touch', 'pressure', 'temperature'

    // --- Data Simulation based on general timeline ---
    // This is a simplified model for visualization purposes
    const sensitivityTimeline = {
        8: ['mouth_lips'], // Start around mouth
        10: ['face', 'palms_soles'], // Face, palms, soles become sensitive
        12: ['limbs'], // Arms and legs
        14: ['trunk'], // Torso
        18: ['entire_body_basic'], // Basic sensitivity everywhere
        25: ['entire_body_enhanced'], // Enhanced sensitivity and differentiation
        30: ['entire_body_refined'] // More refined perception and processing
    };

     // Estimated relative positions for highlight areas within fetus-area (as percentages)
     // These need to be adjusted based on the actual fetus diagram used.
     const highlightPositions = {
        'mouth_lips': { top: 75, left: 48, width: 8, height: 4, radius: '50%' },
        'face': { top: 65, left: 45, width: 20, height: 15, radius: '50% / 40%' },
        'palms_soles': [
            { top: 55, left: 25, width: 8, height: 8, radius: '50%' }, // Left hand (example position)
            { top: 55, left: 67, width: 8, height: 8, radius: '50%' }, // Right hand (example position)
            { top: 88, left: 35, width: 10, height: 5, radius: '50%' }, // Left foot (example position)
            { top: 88, left: 55, width: 10, height: 5, radius: '50%' }  // Right foot (example position)
        ],
        'limbs': [
             { top: 40, left: 15, width: 15, height: 50, radius: '20px' }, // Left arm/leg area
             { top: 40, left: 70, width: 15, height: 50, radius: '20px' }  // Right arm/leg area
        ],
        'trunk': { top: 30, left: 30, width: 40, height: 40, radius: '30% / 40%' }, // Torso area
        'entire_body_basic': { top: 10, left: 10, width: 80, height: 90, radius: '50px' }, // General full body area
        'entire_body_enhanced': { top: 10, left: 10, width: 80, height: 90, radius: '50px' }, // General full body area
        'entire_body_refined': { top: 10, left: 10, width: 80, height: 90, radius: '50px' } // General full body area
     };


    const stimulusPerception = {
        // Week ranges (inclusive) -> Stimulus type -> Perception description
        '8-14': {
            'default': 'בשבוע זה, רגישות מתחילה להתפתח. בחרו גירוי לראות תגובה משוערת.',
            'touch': 'מגע קל באזורים הרגישים (כרגע רק סביב הפה) עשוי לעורר רפלקס פשוט או תנועה מקומית. זו כנראה לא תחושה מודעת, אלא תגובה בסיסית.',
            'pressure': 'ייתכן שינוי קל בתנועה בתגובה ללחץ משמעותי מאוד, אבל אין תפיסה מובחנת של לחץ. המערכת החושית עדיין בסיסית.',
            'temperature': 'לא צפויה תגובה או תפיסה לשינויי טמפרטורה במי השפיר בשלב זה.'
        },
        '15-24': {
             'default': 'רגישות העובר מתפשטת ומתפתחת. בחרו גירוי לראות כיצד הוא עשוי להגיב.',
            'touch': 'רגישות למגע עולה משמעותית, במיוחד בפנים, בידיים וברגליים. מגע עשוי לעורר תנועות מורכבות יותר וחקירה של הגוף עצמו.',
            'pressure': 'רגישות ללחץ הולכת וגוברת. לחץ על דפנות הרחם עשוי לעורר תגובה ברורה יותר, ייתכן גם שינויים בקצב הלב. העובר מתחיל לחוש גבולות.',
            'temperature': 'ייתכן שינוי מסוים בתגובה פיזיולוגית לשינויי טמפרטורה חדים, אך תפיסה מודעת של חום/קור מוגבלת.'
        },
        '25-40': {
            'default': 'מערכת המישוש מפותחת מאוד. גלו את טווח התחושות האפשרי.',
            'touch': 'תפיסת מגע עדינה ומדויקת יותר. העובר מסוגל להבדיל טוב יותר בין סוגי מגע ומיקומים. מגע הוא דרך מרכזית לחקור את העולם הפנימי שלו.',
            'pressure': 'רגישות טובה ללחץ מאפשרת לעובר לחוש את המנח שלו ברחם ואף לדחוף כנגד דפנות. לחץ הוא חלק מחוויית העולם שלו.',
            'temperature': 'ייתכן שוני בתגובה לתנאי טמפרטורה במי השפיר. יש יכולת כלשהי לחוש חום או קור.'
        }
    };

    function getStimulusColorClass(stimulus) {
        switch(stimulus) {
            case 'touch': return 'touch';
            case 'pressure': return 'pressure';
            case 'temperature': return 'temperature';
            default: return '';
        }
    }

    function updateFetusVisualization(week, stimulus) {
        // Clear previous highlights
        fetusHighlightsArea.innerHTML = '';
        fetusDiagram.style.filter = 'none'; // Reset filter
        fetusDiagram.style.outline = 'none'; // Reset outline

        let sensitiveAreas = [];
        for (let w = 8; w <= week; w++) {
            if (sensitivityTimeline[w]) {
                 // In a real app, you'd merge or prioritize based on progression
                 // For this simulation, just add all areas that became sensitive by this week
                 sensitivityTimeline[w].forEach(area => {
                     if (!sensitiveAreas.includes(area)) {
                         sensitiveAreas.push(area);
                     }
                 });
            }
        }

        // Determine the highest level of "entire_body" sensitivity reached
        let entireBodySensitivity = null;
        if (week >= 30) entireBodySensitivity = 'entire_body_refined';
        else if (week >= 25) entireBodySensitivity = 'entire_body_enhanced';
        else if (week >= 18) entireBodySensitivity = 'entire_body_basic';

        // If any entire body sensitivity is reached, just highlight the whole body representation
        if (entireBodySensitivity && highlightPositions[entireBodySensitivity]) {
             const entireBodyPos = highlightPositions[entireBodySensitivity];
             const div = document.createElement('div');
             div.classList.add('highlight', 'active', 'pulse', getStimulusColorClass(stimulus));
             div.style.cssText = `
                 top: ${entireBodyPos.top}%;
                 left: ${entireBodyPos.left}%;
                 width: ${entireBodyPos.width}%;
                 height: ${entireBodyPos.height}%;
                 border-radius: ${entireBodyPos.radius};
             `;
             fetusHighlightsArea.appendChild(div);

        } else {
             // Otherwise, add specific area highlights for areas sensitive up to this week
             sensitiveAreas.forEach(areaKey => {
                 if (highlightPositions[areaKey]) {
                     const positions = Array.isArray(highlightPositions[areaKey]) ? highlightPositions[areaKey] : [highlightPositions[areaKey]];

                     positions.forEach(pos => {
                          const div = document.createElement('div');
                          div.classList.add('highlight', 'active', getStimulusColorClass(stimulus));
                          // Add pulse only if a stimulus is selected
                          if (stimulus) {
                              div.classList.add('pulse');
                          }
                          div.style.cssText = `
                              top: ${pos.top}%;
                              left: ${pos.left}%;
                              width: ${pos.width}%;
                              height: ${pos.height}%;
                              border-radius: ${pos.radius || '50%'}; /* Default to 50% if not specified */
                              transform: scale(1); /* Ensure initial scale is correct */
                              opacity: 1; /* Ensure initial opacity is correct */
                          `;
                          fetusHighlightsArea.appendChild(div);
                     });
                 }
             });
        }


        // Update text description after visualization
        updatePerceptionText(week, stimulus, sensitiveAreas);
    }

    function updatePerceptionText(week, stimulus, sensitiveAreas) {
        let perceptionKey = null;

        if (week >= 25) {
            perceptionKey = '25-40';
        } else if (week >= 15) {
            perceptionKey = '15-24';
        } else {
            perceptionKey = '8-14';
        }

        let description = '';
        if (stimulus && stimulusPerception[perceptionKey] && stimulusPerception[perceptionKey][stimulus]) {
             description = stimulusPerception[perceptionKey][stimulus];
        } else {
             // Fallback or default message
             description = stimulusPerception[perceptionKey]['default'] || 'בחרו שבוע וגירוי כדי לגלות כיצד העובר חווה מגע.';
        }

         perceptionText.textContent = description;
    }


    // Event Listeners
    weekSlider.addEventListener('input', (event) => {
        currentWeek = parseInt(event.target.value);
        currentWeekSpan.textContent = `שבוע ${currentWeek}`;
        updateFetusVisualization(currentWeek, activeStimulus);
    });

    stimulusButtons.forEach(button => {
        button.addEventListener('click', () => {
            const stimulusType = button.getAttribute('data-stimulus');

            // Remove active from all buttons
            stimulusButtons.forEach(btn => btn.classList.remove('active'));

            // If the clicked button was already active, deactivate it
            if (activeStimulus === stimulusType) {
                activeStimulus = null;
            } else {
                // Activate the clicked button
                button.classList.add('active');
                activeStimulus = stimulusType;
            }

            // Update visualization and text based on the new state
            updateFetusVisualization(currentWeek, activeStimulus);
        });
    });

    showExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        showExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצגת המסע המלא: הסבר מעמיק'; // Toggle button text
    });

    // Initial update on page load
    updateFetusVisualization(currentWeek, activeStimulus);

</script>
```