---
title: "עולם נסתר: חקר אגמים תת-קרחוניים באנטארקטיקה"
english_slug: hidden-world-exploring-antarctic-subglacial-lakes
category: "מדעי הסביבה / אקולוגיה וקיימות"
tags: אנטארקטיקה, אגמים תת-קרחוניים, אקולוגיה, חיים קיצוניים, מיקרוביולוגיה
---
# עולם נסתר: חקר אגמים תת-קרחוניים באנטארקטיקה

דמיינו מסע אל לב אנטארקטיקה, אלפי מטרים מתחת לכיפת הקרח האדירה. שם, הרחק מאור השמש ומהעולם שמעל, שוכנים ימים נסתרים – אגמים תת-קרחוניים. האם יכולים להתקיים חיים בסביבה כה מבודדת, חשוכה וקיצונית? הצטרפו למסע וגלו את הסודות המדהימים החבויים במעמקים.

<div class="simulation-container">
    <div class="ice-column" id="iceColumn">
        <div class="column-section ice-upper" data-depth-start="0" data-depth-end="1500"></div>
        <div class="column-section ice-lower" data-depth-start="1500" data-depth-end="3700"></div>
        <div class="column-section lake-upper" data-depth-start="3700" data-depth-end="3850"></div>
        <div class="column-section lake-mid" data-depth-start="3850" data-depth-end="4000"></div>
        <div class="column-section lake-bottom" data-depth-start="4000" data-depth-end="4100"></div>
        <div class="diver" id="diver">探</div> <!-- Changed icon to something more exploratory/submersible -->
    </div>
    <div class="info-panel">
        <h3>🔍 נתוני סביבה</h3>
        <div class="depth-display">
            <span class="icon">🔽</span> עומק: <span id="current-depth">0</span> מטרים
        </div>
        <div class="conditions-display">
            <h4>תנאי סביבה:</h4>
            <p><span class="icon">🌡️</span> טמפרטורה: <span id="temp">-</span></p>
            <p><span class="icon">🔬</span> לחץ: <span id="pressure">-</span></p>
            <p><span class="icon">🧂</span> מליחות: <span id="salinity">-</span></p>
            <p><span class="icon">🌬️</span> חמצן: <span id="oxygen">-</span></p>
            <p><span class="icon">🍔</span> חומרים מזינים: <span id="nutrients">-</span></p>
        </div>
        <div class="microbe-display">
            <h4>✨ חיים נסתרים (אורגניזמים אופייניים):</h4>
            <div id="microbe-list">אין נתונים עבור אזור זה.</div>
            <div id="microbe-details">לחצו על שם אורגניזם לפרטים.</div>
        </div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
    }

    .simulation-container {
        display: flex;
        direction: rtl; /* Right-to-left for Hebrew text */
        align-items: flex-start;
        gap: 30px; /* Increased gap */
        margin: 30px 0;
        padding: 20px;
        border: 1px solid #cfe2f3; /* Softer border */
        border-radius: 12px; /* More rounded corners */
        background-color: #eef5f9; /* Lighter background */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    .ice-column {
        position: relative;
        width: 100px; /* Wider column */
        height: 600px; /* Taller simulation area */
        background: linear-gradient(to bottom, #e0f7fa 0%, #b2ebf2 40%, #80deea 70%, #4dd0e1 90%, #26c6da 100%); /* More detailed gradient */
        border: 2px solid #0097a7; /* Stronger border */
        border-radius: 8px;
        overflow: hidden; /* Keep diver inside */
        flex-shrink: 0; /* Prevent shrinking */
    }

    .column-section {
        position: absolute;
        width: 100%;
        left: 0;
        opacity: 0.9; /* Slightly transparent */
    }

    /* Visual mapping based on depth ranges (relative to total height) */
    .ice-upper {
        top: 0%;
        height: calc(1500 / 4100 * 100%); /* Calculate height based on depth ratio */
        background-color: rgba(224, 247, 250, 0.7); /* Light ice */
    }
    .ice-lower {
        top: calc(1500 / 4100 * 100%);
        height: calc((3700 - 1500) / 4100 * 100%); /* Calculate height based on depth ratio */
        background-color: rgba(178, 235, 242, 0.7); /* Denser ice */
    }
    .lake-upper {
        top: calc(3700 / 4100 * 100%);
         height: calc((3850 - 3700) / 4100 * 100%); /* Calculate height based on depth ratio */
        background-color: rgba(128, 222, 234, 0.7); /* Water near ice */
    }
    .lake-mid {
        top: calc(3850 / 4100 * 100%);
        height: calc((4000 - 3850) / 4100 * 100%); /* Calculate height based on depth ratio */
        background-color: rgba(77, 182, 172, 0.7); /* Deeper water */
    }
    .lake-bottom {
        top: calc(4000 / 4100 * 100%);
        height: calc((4100 - 4000) / 4100 * 100%); /* Calculate height based on depth ratio */
        background-color: rgba(38, 166, 154, 0.7); /* Near bottom - darker teal */
    }


    .diver {
        position: absolute;
        top: 0; /* Start at the top */
        left: 50%;
        transform: translateX(-50%) translateY(-50%); /* Center the diver icon */
        cursor: grab; /* Indicate draggable */
        font-size: 30px; /* Larger icon */
        z-index: 10; /* Ensure it's above sections */
        user-select: none; /* Prevent text selection on drag */
        color: #ff5722; /* Accent color for diver */
        text-shadow: 0 0 5px rgba(0,0,0,0.2);
        transition: top 0.1s ease-out; /* Smooth animation for movement */
    }

     .diver:active {
        cursor: grabbing;
     }

    .info-panel {
        flex-grow: 1; /* Takes remaining space */
        background-color: #ffffff;
        border: 1px solid #e1f5fe; /* Lighter border */
        border-radius: 8px;
        padding: 20px; /* More padding */
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05); /* Subtle inner shadow */
        direction: rtl; /* Ensure text is RTL */
        text-align: right; /* Align text right */
    }

    .info-panel h3, .info-panel h4 {
        margin-top: 0;
        color: #0277bd; /* Darker blue headers */
        border-bottom: 2px solid #b3e5fc; /* Header underline */
        padding-bottom: 8px;
        margin-bottom: 15px;
    }

    .depth-display, .conditions-display, .microbe-display {
        margin-bottom: 20px; /* More space between sections */
        padding-bottom: 15px;
        border-bottom: 1px dashed #e0e0e0; /* Dashed separator */
    }

    .icon {
        margin-left: 8px; /* Space after icon */
        font-size: 1.2em;
        vertical-align: middle;
    }

    .conditions-display p {
        margin-bottom: 8px;
        font-size: 1.1em;
    }

    #microbe-list {
         min-height: 2em; /* Reserve space */
         margin-top: 10px;
    }

    .microbe-item {
        display: inline-block; /* Allow multiple items per line */
        margin-left: 15px; /* Space between items */
        margin-bottom: 5px;
        cursor: pointer;
        color: #0097a7; /* Teal color for links */
        text-decoration: none; /* No underline initially */
        border-bottom: 1px dashed transparent; /* Subtle hover effect base */
        transition: all 0.3s ease;
    }
     .microbe-item:hover {
        color: #006064; /* Darker teal on hover */
        border-bottom-color: #006064;
     }
     .microbe-item:active {
        color: #004d40;
     }


    #microbe-details {
        margin-top: 15px;
        padding: 12px;
        background-color: #e3f2fd; /* Very light blue background */
        border: 1px solid #bbdefb; /* Light blue border */
        border-radius: 6px;
        min-height: 4em; /* Reserve more space */
        font-size: 0.95em;
        color: #01579b; /* Darker blue text */
        animation: fadeIn 0.5s ease-out; /* Fade-in animation */
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Button styling */
    .btn {
        display: inline-block;
        font-weight: 400;
        color: #fff;
        text-align: center;
        vertical-align: middle;
        user-select: none;
        background-color: #0288d1; /* Primary blue */
        border: 1px solid #0277bd;
        padding: .6rem 1.2rem;
        font-size: 1rem;
        line-height: 1.5;
        border-radius: .25rem;
        transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
        cursor: pointer;
        margin-top: 20px;
    }

    .btn:hover {
        background-color: #0277bd;
        border-color: #01579b;
    }

    .btn:focus {
        outline: 0;
        box-shadow: 0 0 0 .2rem rgba(2, 136, 209, .25);
    }

    #detailed-explanation h2 {
        color: #0277bd;
        margin-top: 30px;
        border-bottom: 2px solid #b3e5fc;
        padding-bottom: 10px;
    }

    #detailed-explanation h3 {
         color: #0277bd;
         margin-top: 20px;
         margin-bottom: 10px;
    }

    #detailed-explanation ul {
        list-style: disc;
        margin-right: 20px;
        padding-right: 0;
    }

    #detailed-explanation li {
        margin-bottom: 8px;
    }

</style>

<button id="toggle-explanation" class="btn">הצג הסבר מפורט</button>

<div id="detailed-explanation" style="display: none;">
    <h2>הסבר מורחב: אגמים תת-קרחוניים באנטארקטיקה</h2>

    <p>דמיינו יבשת שלמה מכוסה במעטה קרח עצום, שעוביו מגיע לעיתים למעל 4 קילומטרים. מתחת לשכבת הקרח הזו, בסביבה שנחשבה בעבר לקפואה וחסרת חיים, מסתתר עולם שלם של מים נוזלים: מערכת מסועפת של אגמים ונהרות תת-קרחוניים. אגמים אלו מנותקים מהאטמוספירה ומהעולם החיצוני במשך מיליוני שנים, ומהווים מעבדה טבעית לחקר גבולות החיים על פני כדור הארץ – ואולי גם מחוצה לו.</p>

    <h3>אגם ווסטוק - ליבת הסוד</h3>
    <p>גולת הכותרת במערכת זו הוא אגם ווסטוק (Vostok), האגם התת-קרחוני הגדול ביותר הידוע. הוא שוכן מתחת לתחנת המחקר הרוסית ווסטוק, בעומק מדהים של כ-3,700 עד 4,100 מטרים מתחת לפני הקרח. גודלו דומה לאגם אונטריו שבצפון אמריקה, והוא מכיל נפח מים עצום השקול לאלפי קילומטרים מעוקבים. אגם ווסטוק היה הראשון שהתגלה באופן נרחב באמצעות סקרים סייסמיים ורדאר חודר קרח, והניע עניין עולמי בחקר סביבות אלו.</p>

    <h3>תנאים קיצוניים - בית לחיים?</h3>
    <p>הסביבה באגמים התת-קרחוניים היא מהעוינות ביותר שניתן למצוא:</p>
    <ul>
        <li><strong>חושך תהומי:</strong> אלפי מטרים של קרח אטום לחלוטין לאור שמש.</li>
        <li><strong>לחץ כובל:</strong> משקל הקרח והמים יוצר לחץ הידרוסטטי עצום, הגדול פי 300-400 מהלחץ בגובה פני הים.</li>
        <li><strong>טמפרטורה קרובה לקיפאון:</strong> למרות שהטמפרטורה מעט מתחת לאפס מעלות צלזיוס, הלחץ הגבוה מוריד את נקודת הקיפאון, כך שהמים נשארים נוזלים. קרוב לקרקעית האגם, חום גיאותרמי יכול להעלות את הטמפרטורה מעט מעל נקודת הקיפאון.</li>
        <li><strong>מליחות משתנה:</strong> המים מגיעים מקרח נמס (מליחות נמוכה), אך מגע עם סלעי הבסיס וריכוז מלחים לאורך מיליוני שנים יכול ליצור אזורים מלוחים יותר.</li>
        <li><strong>ריכוז גזים ייחודי:</strong> המים מכילים גזים המומסים מהקרח העתיק שמעל, לעיתים בריכוזים גבוהים מהרגיל, וריכוז החמצן יורד משמעותית ככל שמתרחקים מבסיס הקרח ויורדים לעומק האגם.</li>
    </ul>

    <h3>מקורות אנרגיה ותזונה בסביבה חשוכה</h3>
    <p>בהיעדר אור שמש, החיים כאן אינם יכולים להסתמך על פוטוסינתזה. במקום זאת, המיקרואורגניזמים, שהם ככל הנראה צורות החיים היחידות באגמים אלו, מפיקים אנרגיה ותזונה ממקורות חלופיים:</p>
    <ul>
        <li><strong>כימוסינתזה:</strong> רבים מסתמכים על תגובות כימיות של חומרים אי-אורגניים הזמינים בסלעי הבסיס או המומסים במים (כמו תרכובות גופרית, ברזל, מימן). הם "אוכלים אבן" ומפיקים מכך אנרגיה.</li>
        <li><strong>חומר אורגני קדום:</strong> חומר צמחי או מיקרוביאלי שנלכד בקרח לפני מיליוני שנים משתחרר למים כשהקרח נמס ויכול לשמש כמקור מזון.</li>
        <li><strong>מינרלים מסלעים:</strong> בלייה של סלעי הבסיס משחררת מינרלים חיוניים.</li>
    </ul>

    <h3>פלאי המיקרואורגניזמים</h3>
    <p>החיים שנמצאו (בעיקר מניתוח דגימות קרח מבסיס כיפת הקרח או משקעים) הם בעיקר חיידקים וארכיאה, יצורים חד-תאיים המסוגלים לשרוד ולהתקיים בתנאים קיצוניים ביותר. המגוון נמוך יחסית לסביבות מוארות, אך אלו שנמצאו הותאמו באופן מדהים. הם עשויים לנשום ללא חמצן (אנאירובית), לבצע מטבוליזם איטי במיוחד, ולעמוד בלחץ ובקור העז.</p>

    <h3>למה זה חשוב לחקור?</h3>
    <p>חקר האגמים התת-קרחוניים באנטארקטיקה הוא חיוני מכמה סיבות דרמטיות:</p>
    <ul>
        <li><strong>גבולות החיים:</strong> הבנה מעמיקה של האופן שבו חיים יכולים לשרוד בסביבות כל כך קיצוניות מרחיבה את ההבנה שלנו על מה שמאפשר חיים.</li>
        <li><strong>חיפוש חיים מחוץ לכדור הארץ:</strong> תנאים דומים לאגמים אלו עשויים להתקיים על ירחים קפואים במערכת השמש שלנו, כמו אירופה (ירח של צדק) או אנסלדוס (ירח של שבתאי), שם מאמינים שקיימים אוקיינוסים תת-קרחוניים. אנטארקטיקה היא מעבדה אידיאלית להתכוננות למשימות אסטרוביולוגיות עתידיות.</li>
        <li><strong>היסטוריה פלנטרית:</strong> הקרח שמעל האגמים והמשקעים בקרקעיתם מכילים תיעוד קדום של האקלים והסביבה באנטארקטיקה לאורך מיליוני שנים, כולל מידע על מחזורי גזים, חלקיקים מהאטמוספרה העתיקה ואף עדויות לחיים קדומים.</li>
    </ul>

    <h3>אתגרי החקר</h3>
    <p>הגעה לאגמים ודגימתם היא משימה הנדסית ולוגיסטית עצומה ומאתגרת. נדרש קידוח מדויק דרך אלפי מטרים של קרח תוך הקפדה מחמירה על מניעת זיהום האגם הבתולי על ידי ציוד הקידוח או נוזליו. כל משימה כזו מתבצעת בזהירות מרבית כדי לשמור על המערכת האקולוגית הייחודית והעדינה הזו.</p>

    <h3>הקשר לאקלים העולמי</h3>
    <p>קיומם ותנועתם של אגמים תת-קרחוניים יכולים להשפיע על דינמיקת זרימת הקרח ביריעות הקרח האנטארקטיות הגדולות. מים נוזליים בבסיס הקרח פועלים כחומר סיכה, ושינויים במערכת האגמים יכולים להשפיע על מהירות תנועת הקרח לעבר האוקיינוס, ובכך להשפיע על עליית פני הים העולמית בטווחים ארוכים.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const iceColumn = document.getElementById('iceColumn');
        const diver = document.getElementById('diver');
        const currentDepthSpan = document.getElementById('current-depth');
        const tempSpan = document.getElementById('temp');
        const pressureSpan = document.getElementById('pressure');
        const salinitySpan = document.getElementById('salinity');
        const oxygenSpan = document.getElementById('oxygen');
        const nutrientsSpan = document.getElementById('nutrients');
        const microbeListDiv = document.getElementById('microbe-list');
        const microbeDetailsDiv = document.getElementById('microbe-details');
        const explanationDiv = document.getElementById('detailed-explanation');
        const toggleButton = document.getElementById('toggle-explanation');

        let isDragging = false;
        let startY;
        let startTop;

        const totalDepth = 4100; // Approximate max depth (like Vostok)
        let columnHeight = iceColumn.offsetHeight; // Get height dynamically

        // Define zones and their properties (more descriptive ranges)
        const zones = [
            { name: 'Upper Ice', depthStart: 0, depthEnd: 1500, conditions: { temp: 'מתחת ל-0°C', pressure: 'נמוך יחסית (עולה עם העומק)', salinity: 'נמוכה מאוד', oxygen: 'גבוה', nutrients: 'נמוכים מאוד' }, microbes: [], color: '#e0f7fa' },
            { name: 'Lower Ice', depthStart: 1501, depthEnd: 3700, conditions: { temp: 'קרוב ל-0°C (מוקפא)', pressure: 'גבוה מאוד (עולה משמעותית)', salinity: 'נמוכה מאוד', oxygen: 'עדיין גבוה', nutrients: 'נמוכים מאוד' }, microbes: [], color: '#b2ebf2' },
            { name: 'Lake - Upper Water', depthStart: 3701, depthEnd: 3850, conditions: { temp: 'קרוב ל-0°C (נוזלי בלחץ גבוה)', pressure: 'גבוה מאוד', salinity: 'משתנה (מעבר מקרח למים אגם)', oxygen: 'מתחיל לרדת משמעותית', nutrients: 'עולים מעט' }, microbes: [{ name: 'חיידקים מתארופיים', desc: 'מפיקים אנרגיה מכימוסינתזה המייצרת מתאן בתנאים חסרי חמצן.' }, { name: 'חיידקים דנטריפיקטוריים', desc: 'מפיקים אנרגיה באמצעות תרכובות חנקן במקום חמצן.' }], color: '#80deea' },
            { name: 'Lake - Mid Water', depthStart: 3851, depthEnd: 4000, conditions: { temp: 'קרוב ל-0°C (נוזלי)', pressure: 'גבוה מאוד', salinity: 'משתנה (פוטנציאל גבוה יותר מבסיס הקרח)', oxygen: 'נמוך עד אפסי', nutrients: 'עשירים יחסית (מתרכובות גיאולוגיות או קדומות)' }, microbes: [{ name: 'ארכיאה כימוסינתטית', desc: 'מפיקה אנרגיה מתרכובות גופרית או ברזל מהסלע.' }, { name: 'חיידקים מחזרים', desc: 'מבצעים רידוקציה של יונים מתכתיים.' }, { name: 'חיידקים הטרוטרופים', desc: 'ניזונים מחומר אורגני קדום שהשתחרר מהקרח.' }], color: '#4dd0e1' },
            { name: 'Lake - Near Bottom', depthStart: 4001, depthEnd: 4100, conditions: { temp: 'מעט מעל 0°C (השפעת חום גיאותרמי)', pressure: 'הגבוה ביותר', salinity: 'עשויה להיות גבוהה (מגע עם סלעי הבסיס ומינרלים)', oxygen: 'אפסי', nutrients: 'עשירים (ממינרלים ומשקעים מקרקעית האגם)' }, microbes: [{ name: 'חיידקי מחזור גופרית', desc: 'כימוסינתזה המבוססת על תרכובות גופרית מהסלע.' }, { name: 'חיידקים צורכי מתאן', desc: 'ניזונים ממתאן המיוצר ע"י אורגניזמים אחרים.' }, { name: 'ארכיאה היפרתרמופילית (פוטנציאל ליד פתחי חום)', desc: 'ייתכן קיומם ליד מקורות חום תת-קרקעיים מקומיים.' }], color: '#26c6da' }
        ];

        // Function to map pixel top position to depth
        function pixelToDepth(pixelTop) {
             const positionRatio = pixelTop / columnHeight;
             return Math.round(positionRatio * totalDepth);
        }

        // Function to map depth to pixel top position
        function depthToPixel(depth) {
            const positionRatio = depth / totalDepth;
            return positionRatio * columnHeight;
        }

        // Update info panel based on current depth
        function updateInfo(currentDepth) {
            currentDepthSpan.textContent = currentDepth;

            let currentZone = null;
            for (const zone of zones) {
                 if (currentDepth >= zone.depthStart && currentDepth <= zone.depthEnd) {
                    currentZone = zone;
                    break;
                }
            }

            if (currentZone) {
                 // Update conditions
                 tempSpan.textContent = currentZone.conditions.temp;
                 pressureSpan.textContent = currentZone.conditions.pressure;
                 salinitySpan.textContent = currentZone.conditions.salinity;
                 oxygenSpan.textContent = currentZone.conditions.oxygen;
                 nutrientsSpan.textContent = currentZone.conditions.nutrients;

                 // Update microbes list
                 if (currentZone.microbes.length > 0) {
                     microbeListDiv.innerHTML = currentZone.microbes.map(microbe =>
                         `<span class="microbe-item" data-microbe-name="${microbe.name}">${microbe.name}</span>`
                     ).join('');
                 } else {
                     microbeListDiv.textContent = 'אין נתונים עבור אזור זה.';
                 }
                 // Clear previous details or show prompt
                 microbeDetailsDiv.textContent = 'לחצו על שם אורגניזם לפרטים.';

                 // Visually highlight the current zone section (optional, requires more CSS/JS)
                 // For now, we rely on the info panel update.
             } else {
                 // Default info if outside defined ranges (shouldn't happen if ranges cover 0-totalDepth)
                 tempSpan.textContent = '-';
                 pressureSpan.textContent = '-';
                 salinitySpan.textContent = '-';
                 oxygenSpan.textContent = '-';
                 nutrientsSpan.textContent = '-';
                 microbeListDiv.textContent = 'אין נתונים עבור אזור זה.';
                 microbeDetailsDiv.textContent = 'פרטים אינם זמינים.';
             }
        }

        // --- Draggable Diver Logic ---
        function startDrag(e) {
            isDragging = true;
            startY = e.clientY || e.touches[0].clientY; // Handle mouse and touch
            startTop = diver.offsetTop;
            diver.style.cursor = 'grabbing';
            diver.style.transition = 'none'; // Disable smooth transition while dragging
            e.preventDefault();
        }

        function drag(e) {
            if (!isDragging) return;

            const clientY = e.clientY || e.touches[0].clientY; // Handle mouse and touch
            const dy = clientY - startY;
            let newTop = startTop + dy;

            // Constrain the diver within the column's height
            newTop = Math.max(0, Math.min(columnHeight, newTop));

            diver.style.top = newTop + 'px';

            // Update info based on the new position immediately
            const currentDepth = pixelToDepth(newTop);
            updateInfo(currentDepth);
        }

        function endDrag() {
            if (isDragging) {
                isDragging = false;
                diver.style.cursor = 'grab';
                 diver.style.transition = 'top 0.1s ease-out'; // Re-enable smooth transition
            }
        }

        // Add event listeners
        diver.addEventListener('mousedown', startDrag);
        diver.addEventListener('touchstart', startDrag); // Add touch support

        document.addEventListener('mousemove', drag);
        document.addEventListener('touchmove', drag, { passive: false }); // Add touch support

        document.addEventListener('mouseup', endDrag);
        document.addEventListener('touchend', endDrag); // Add touch support
        document.addEventListener('mouseleave', endDrag); // End drag if mouse leaves the window

        // --- Microbe Details Logic ---
        microbeListDiv.addEventListener('click', (e) => {
             if (e.target.classList.contains('microbe-item')) {
                 const microbeName = e.target.dataset.microbeName;
                 const currentDepth = parseInt(currentDepthSpan.textContent);

                 // Find the currently active zone based on depth to get microbe details
                 let currentZone = null;
                 for (const zone of zones) {
                    if (currentDepth >= zone.depthStart && currentDepth <= zone.depthEnd) {
                        currentZone = zone;
                        break;
                    }
                 }

                 if (currentZone) {
                     const microbe = currentZone.microbes.find(m => m.name === microbeName);
                     if (microbe) {
                         // Add animation class temporarily
                         microbeDetailsDiv.classList.remove('fadeIn'); // Reset animation
                         void microbeDetailsDiv.offsetWidth; // Trigger reflow
                         microbeDetailsDiv.classList.add('fadeIn');

                         microbeDetailsDiv.innerHTML = `<strong>${microbe.name}:</strong> ${microbe.desc}`;
                     } else {
                          microbeDetailsDiv.textContent = 'פרטים אינם זמינים.';
                     }
                 }
             }
        });


        // --- Explanation Toggle Logic ---
        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג הסבר מפורט';
        });

        // --- Resize Observer to update height on window resize ---
        const resizeObserver = new ResizeObserver(entries => {
            for (let entry of entries) {
                if (entry.target === iceColumn) {
                    columnHeight = entry.contentRect.height;
                    // Update diver position relative to new height to maintain depth
                     const currentDepth = parseInt(currentDepthSpan.textContent) || 0;
                     const newTop = depthToPixel(currentDepth);
                     diver.style.top = newTop + 'px';
                }
            }
        });

        resizeObserver.observe(iceColumn);


        // Initial state update
        // Set initial diver position to 0 depth and update info
        diver.style.top = '0px'; // Ensure it starts at the very top
        updateInfo(0); // Update info for depth 0
    });
</script>