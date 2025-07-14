---
title: "המיקרוביום של העור: שותפים סמויים לבריאות"
english_slug: skin-microbiome-under-the-surface
category: "ביולוגיה"
tags: [מיקרוביום, עור, חיידקים, אקולוגיה, בריאות, סימולציה]
---
<div class="intro-section">
    <h1>המיקרוביום של העור: שותפים סמויים לבריאות</h1>
    <p>האם דמיינתם פעם שעל פני העור שלכם חיים מיליארדי יצורים זעירים, בקהילה תוססת שמשפיעה ישירות על בריאותכם? הכירו את המיקרוביום של העור – עולם מיקרוסקופי של חיידקים, פטריות, וירוסים ועוד, הפועלים בשיתוף פעולה מרתק. גלו כיצד איזון עדין זה שומר עלינו, ואיך שינויים סביבתיים יכולים להשפיע עליו.</p>
</div>

<div class="interactive-container">
    <div class="body-map-container">
        <!-- Replace with a high-quality, modern body map illustration -->
        <img src="https://via.placeholder.com/400x600?text=Body+Map+Illustration" alt="איור מפת גוף אנושי עם אזורים שונים" class="body-map-image">
        <!-- Hotspots - maintain position logic but enhance appearance -->
        <div class="hotspot" data-area="forehead" style="top: 12%; left: 50%;">מצח</div>
        <div class="hotspot" data-area="elbow" style="top: 38%; left: 22%;">מרפק</div>
        <div class="hotspot" data-area="armpit" style="top: 28%; left: 75%;">בית שחי</div>
        <div class="hotspot" data-area="foot" style="top: 90%; left: 45%;">כף רגל</div>
         <!-- Add more hotspots for richer interaction -->
         <div class="hotspot" data-area="hand" style="top: 50%; left: 30%;">כף יד</div>
         <div class="hotspot" data-area="back" style="top: 45%; left: 50%;">גב</div>
    </div>

    <div class="info-panel">
        <div class="panel-header">
             <h2 id="panel-title">בחר אזור בגוף</h2>
        </div>
        <div class="panel-content">
            <div id="microbiome-data" class="data-display initial-message">
                לחץ על אחד האזורים המודגשים במפת הגוף כדי לראות את הרכב המיקרוביום האופייני לו.
            </div>

            <div id="simulation-controls" style="display: none;">
                <h3>השפעת גורמים (בחר אחד או יותר):</h3>
                <div class="factors">
                    <label class="factor-label"><input type="checkbox" name="factor" value="antibacterial-soap"><i class="icon soap-icon">🧼</i> שטיפה תכופה עם סבון אנטיבקטריאלי</label>
                    <label class="factor-label"><input type="checkbox" name="factor" value="moisturizer"><i class="icon cream-icon">🧴</i> שימוש בקרם לחות</label>
                    <label class="factor-label"><input type="checkbox" name="factor" value="sun-exposure"><i class="icon sun-icon">☀️</i> חשיפה ממושכת לשמש</label>
                     <label class="factor-label"><input type="checkbox" name="factor" value="antibiotics"><i class="icon antibiotics-icon">💊</i> נטילת אנטיביוטיקה סיסטמית</label>
                </div>
                <button id="simulate-button">הדמיית שינוי</button>

                <div id="simulation-result" class="data-display simulation-result" style="margin-top: 20px;">
                    <!-- Simulation results will appear here -->
                </div>
            </div>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button" style="margin-top: 20px;">הצג/הסתר הסבר מורחב</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>הסבר מורחב: המיקרוביום של העור – עולם נסתר</h2>
    <p>העור שלנו, המחסום החיצוני הגדול ביותר של הגוף, הוא גם בית גידול למגוון עצום של מיקרואורגניזמים. קהילה מורכבת זו, המכונה המיקרוביום של העור, כוללת בעיקר חיידקים, אך גם פטריות, וירוסים ופרוקי רגליים זעירים (כמו קרדיות). המיקרוביום אינו סתם אורח פסיבי; הוא שותף פעיל וקריטי בשמירה על בריאות העור ותפקודו התקין.</p>

    <h3>אקולוגיה של העור: בתי הגידול המגוונים</h3>
    <p>פני העור אינם אחידים. טמפרטורה, לחות, כמות שומן (חלב), ורמת ה-pH משתנות משמעותית בין אזורים שונים. הבדלים אלו יוצרים בתי גידול מיקרוביאליים מובחנים:</p>
    <ul>
        <li><b>אזורים שומניים (סבוריאים):</b> מצח, קרקפת, גב עליון. מאופיינים בבלוטות חלב רבות ותכולת שומן גבוהה. נפוצים בהם חיידקי <i>Cutibacterium (Propionibacterium)</i> ושמרי <i>Malassezia</i>.</li>
        <li><b>אזורים לחים:</b> בתי שחי, מפשעות, קפלי עור. מאופיינים בלחות גבוהה כתוצאה מזיעה. נפוצים בהם חיידקי <i>Corynebacterium</i> ו-<i>Staphylococcus</i>.</li>
        <li><b>אזורים יבשים:</b> אמות, כפות רגליים (בחלקן). מאופיינים בלחות נמוכה יחסית. מגוון מיקרוביאלי גדול יותר ונפוצים בהם חיידקים מגוונים כמו <i>Staphylococcus</i>, <i>Streptococcus</i> ועוד.</li>
    </ul>

    <h3>שחקנים ראשיים ותפקידם</h3>
    <p>המיקרואורגניזמים החיים על עורנו מקיימים מערכת יחסים הדדית איתנו ובינם לבין עצמם. רבים מהם "תושבי קבע" מועילים:</p>
    <ul>
        <li><b>הגנה מפני פולשים:</b> חיידקי המיקרוביום המקומיים תופסים נישות ומתחרים על משאבים עם חיידקים פתוגניים (מחוללי מחלה) שעלולים לנחות על העור. חלקם אף מייצרים חומרים אנטי-מיקרוביאליים המעכבים גדילת חיידקים מזיקים.</li>
        <li><b>אימון מערכת החיסון:</b> המיקרוביום חיוני להתפתחות ותחזוקת מערכת החיסון העורית. הוא מסייע ל"למד" את תאי החיסון לזהות מיקרואורגניזמים מועילים ולא להגיב אליהם באגרסיביות, ובמקביל להכין תגובה מהירה נגד פולשים אמיתיים.</li>
        <li><b>תרומה למחסום העורי:</b> חלק מהחיידקים מסייעים בפירוק חלב וזיעה, בתהליכים שתורמים לשמירה על חומציות העור (ה-pH), שהיא חשובה להגנה.</li>
    </ul>

    <h3>כשמאזן מופר: דיסביוזיס ומחלות עור</h3>
    <p>הפרה של האיזון העדין בהרכב ובפעילות המיקרוביום נקראת דיסביוזיס. דיסביוזיס נקשרת למגוון רחב של בעיות עור, ביניהן:</p>
    <ul>
        <li><b>אקנה:</b> קשורה לרוב לשגשוג יתר של חיידקי <i>Cutibacterium acnes</i> באזורים שומניים.</li>
        <li><b>אקזמה (אטופיק דרמטיטיס):</b> לעיתים קשורה לנוכחות מוגברת של <i>Staphylococcus aureus</i> והפחתה במגוון המיקרוביאלי.</li>
        <li><b>פסוריאזיס:</b> קשרים מורכבים לשינויים במיקרוביום.</li>
        <li><b>קשקשת (סבוריאה):</b> קשורה לשגשוג יתר של שמרי <i>Malassezia</i>.</li>
    </ul>

    <h3>גורמים המשפיעים על המיקרוביום של העור</h3>
    <p>הקהילה המיקרוביאלית על עורנו דינמית ומושפעת מגורמים רבים:</p>
    <ul>
        <li><b>היגיינה:</b> שטיפה תכופה, במיוחד עם סבונים חזקים או אנטיבקטריאליים, עלולה לפגוע במגוון ובכמות החיידקים המועילים.</li>
        <li><b>תזונה וסגנון חיים:</b> כולל רמות סטרס והשפעות דרך ציר המעי-עור.</li>
        <li><b>סביבה:</b> אקלים, לחות, חשיפה לשמש, זיהום אוויר.</li>
        <li><b>שימוש בתרופות:</b> אנטיביוטיקה (במיוחד סיסטמית), סטרואידים.</li>
        <li><b>מוצרי טיפוח וקוסמטיקה:</b> הרכבם הכימי, ה-pH שלהם.</li>
        <li><b>גיל ומערכת חיסון.</b></li>
    </ul>

    <h3>כיצד נשמור על מיקרוביום עור בריא?</h3>
    <p>הגישה המומלצת היא תמיכה באיזון הטבעי ולא ניסיון ל"השמיד" חיידקים. מספר טיפים:</p>
    <ul>
        <li>הימנעות משטיפת יתר ושימוש בסבונים עדינים בעלי pH מאוזן.</li>
        <li>שימוש מבוקר במוצרי קוסמטיקה.</li>
        <li>לחלוח העור לפי הצורך לשמירה על מחסום עורי תקין.</li>
        <li>תזונה מאוזנת והפחתת סטרס התורמים לבריאות הגוף כולה.</li>
    </ul>
    <p>הבנת המיקרוביום פותחת דלתות לגישות טיפול חדשות במחלות עור, המתמקדות בשיקום האיזון המיקרוביאלי.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        color: #333;
        direction: rtl;
        text-align: right;
        background-color: #f8f8f8;
        padding: 0 15px;
    }

    h1, h2, h3 {
        color: #2c3e50;
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2.2em;
        text-align: center;
        margin-bottom: 10px;
    }

    h2 {
        font-size: 1.8em;
        border-bottom: 2px solid #3498db;
        padding-bottom: 5px;
        margin-top: 20px;
    }

     h3 {
        font-size: 1.4em;
        color: #3498db;
        margin-top: 15px;
        margin-bottom: 10px;
    }

    p {
        margin-bottom: 15px;
    }

    ul {
        margin-bottom: 15px;
        padding-right: 25px; /* Adjust for RTL */
    }

    li {
        margin-bottom: 8px;
    }

    .intro-section {
        text-align: center;
        margin-bottom: 30px;
        padding: 20px;
        background-color: #eef;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .interactive-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px;
        margin: 30px auto;
        max-width: 900px; /* Limit max width for layout */
    }

    .body-map-container {
        position: relative;
        width: 100%; /* Default to full width on small screens */
        max-width: 400px; /* Max width for image container */
        height: 500px; /* Fixed height, adjust if image ratio differs */
        background-color: #ecf0f1; /* Light background */
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        border: 1px solid #ddd;
    }

    .body-map-image {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: contain; /* Ensure image fits without distortion */
        opacity: 0.9; /* Slightly transparent */
        pointer-events: none; /* Prevent clicking the image itself */
    }

    .hotspot {
        position: absolute;
        background-color: rgba(52, 152, 219, 0.8); /* Brighter blue */
        color: white;
        border-radius: 20px; /* Pill shape */
        padding: 6px 12px;
        font-size: 0.95em;
        cursor: pointer;
        text-align: center;
        transform: translate(-50%, -50%);
        z-index: 10;
        border: 2px solid rgba(255, 255, 255, 0.9);
        transition: all 0.3s ease;
        white-space: nowrap; /* Prevent wrapping */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .hotspot:hover {
        background-color: rgba(41, 128, 185, 0.9);
        transform: translate(-50%, -50%) scale(1.1); /* Pop effect */
    }

    .hotspot.selected {
        background-color: #e74c3c; /* Red for selected */
        border-color: #f1c40f;
        box-shadow: 0 0 15px rgba(231, 76, 60, 0.5);
         animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { box-shadow: 0 0 15px rgba(231, 76, 60, 0.5); }
        50% { box-shadow: 0 0 8px rgba(231, 76, 60, 0.3); }
        100% { box-shadow: 0 0 15px rgba(231, 76, 60, 0.5); }
    }

    .info-panel {
        width: 100%;
        max-width: 450px; /* Slightly wider panel */
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        overflow: hidden; /* For header effect */
        display: flex;
        flex-direction: column;
         min-height: 400px; /* Give panel a minimum height */
    }

    .panel-header {
        background-color: #3498db; /* Matching blue */
        color: white;
        padding: 15px 20px;
        text-align: center;
        font-size: 1.5em;
        margin-bottom: 0; /* Remove margin below header */
    }

    .panel-header h2 {
        color: white;
        margin: 0;
        border: none;
        padding: 0;
    }

    .panel-content {
         padding: 20px;
         flex-grow: 1; /* Allow content to fill space */
         display: flex;
         flex-direction: column;
    }

    .data-display {
        min-height: 80px; /* Increased space */
        margin-bottom: 20px;
        padding: 15px;
        border: 1px dashed #bdc3c7; /* Lighter dashed border */
        background-color: #ecf0f1; /* Light background */
        border-radius: 8px;
        transition: all 0.5s ease-in-out; /* Smooth transitions */
        overflow: hidden; /* Hide overflow from charts */
    }

     .initial-message {
         text-align: center;
         color: #7f8c8d; /* Grey text */
         font-size: 1.1em;
         display: flex;
         align-items: center;
         justify-content: center;
         flex-grow: 1; /* Center in available space */
     }

     .species-list {
         list-style: none;
         padding: 0;
         margin: 0;
     }

     .species-item {
         margin-bottom: 10px;
          padding: 5px 0;
          border-bottom: 1px solid #eee;
          display: flex;
          justify-content: space-between;
          align-items: center;
     }
     .species-item:last-child {
         border-bottom: none;
     }

     .species-bar-container {
         width: 60%; /* Bar takes up 60% */
         height: 15px;
         background-color: #ddd;
         border-radius: 4px;
         overflow: hidden;
     }

     .species-bar {
         height: 100%;
         background-color: #2ecc71; /* Green bar */
         width: 0%; /* Start at 0 for animation */
         transition: width 1s ease-out; /* Animate width change */
     }

     .species-name {
         font-weight: bold;
         width: 35%; /* Name takes up 35% */
     }
     .species-percentage {
         font-size: 0.9em;
         color: #555;
         width: 5%; /* Percentage takes up 5% */
         text-align: left;
     }


    .simulation-result {
        border-color: #f39c12; /* Orange border for results */
        background-color: #fef5e7; /* Light orange background */
    }


    .factors {
        margin-bottom: 20px;
    }

    .factor-label {
        display: flex; /* Use flexbox for icon/text alignment */
        align-items: center;
        margin-bottom: 10px;
        cursor: pointer;
        font-size: 1em;
         padding: 8px;
         background-color: #ecf0f1;
         border-radius: 5px;
         transition: background-color 0.3s ease;
    }

    .factor-label:hover {
         background-color: #d5dbdb;
    }

    .factor-label input[type="checkbox"] {
        margin-left: 10px; /* Space between checkbox and text */
         transform: scale(1.2); /* Slightly larger checkbox */
    }

    .factor-label .icon {
         font-size: 1.2em;
         margin-right: 8px; /* Space between icon and text */
         width: 20px; /* Fixed width for alignment */
         text-align: center;
    }

    #simulate-button {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: #2ecc71; /* Green button */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        margin-top: 15px;
        transition: background-color 0.3s ease;
        font-weight: bold;
    }

    #simulate-button:hover:not(:disabled) {
        background-color: #27ae60;
    }

     #simulate-button:disabled {
         background-color: #bdc3c7;
         cursor: not-allowed;
     }


    .toggle-button {
        display: block;
        width: 100%;
        max-width: 600px;
        margin: 30px auto;
        padding: 12px;
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        text-align: center;
        transition: background-color 0.3s ease;
        font-weight: bold;
    }

    .toggle-button:hover {
        background-color: #2980b9;
    }


    .explanation-section {
        max-width: 600px;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid #ddd;
        border-radius: 8px;
        background-color: #fff;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
         opacity: 0; /* Start hidden for fade-in */
         transform: translateY(20px); /* Start slightly lower */
         transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

     .explanation-section.visible {
         opacity: 1;
         transform: translateY(0);
     }


    /* Responsive adjustments */
    @media (min-width: 768px) {
        .interactive-container {
            flex-direction: row;
            justify-content: center;
            align-items: flex-start;
        }

        .body-map-container {
             width: 40%; /* Take up 40% of container width */
             max-width: 400px;
        }

        .info-panel {
            width: 60%; /* Take up 60% */
            max-width: 450px;
        }

        .hotspot {
             padding: 8px 15px;
             font-size: 1em;
             border-radius: 25px;
        }
    }
</style>

<script>
    const microbiomeData = {
        'forehead': {
            description: "אזור שומני במיוחד, בית חם לחיידקים אוהבי חלב.",
            species: [
                { name: 'Cutibacterium', percentage: 65, color: '#f39c12' }, // Orange
                { name: 'Staphylococcus', percentage: 15, color: '#3498db' }, // Blue
                { name: 'Malassezia (שמרים)', percentage: 15, color: '#e74c3c' }, // Red
                { name: 'אחרים', percentage: 5, color: '#bdc3c7' } // Grey
            ]
        },
        'elbow': {
            description: "אזור יבש יחסית, עם מגוון גדול יותר של מיקרובים.",
            species: [
                { name: 'Staphylococcus', percentage: 40, color: '#3498db' },
                { name: 'Corynebacterium', percentage: 20, color: '#2ecc71' }, // Green
                { name: 'Cutibacterium', percentage: 10, color: '#f39c12' },
                { name: 'Streptococcus', percentage: 15, color: '#9b59b6' }, // Purple
                { name: 'אחרים', percentage: 15, color: '#bdc3c7' }
            ]
        },
        'armpit': {
            description: "אזור לח וחם, אידיאלי לשגשוג חיידקים מסוימים, חלקם גורמים ריח גוף.",
            species: [
                { name: 'Corynebacterium', percentage: 55, color: '#2ecc71' },
                { name: 'Staphylococcus', percentage: 35, color: '#3498db' },
                { name: 'אחרים', percentage: 10, color: '#bdc3c7' }
            ]
        },
        'foot': {
            description: "אזור שמשתנה - יבש מלמעלה, לח בין האצבעות. בית לחיידקים ופטריות.",
            species: [
                { name: 'Staphylococcus', percentage: 35, color: '#3498db' },
                { name: 'Corynebacterium', percentage: 25, color: '#2ecc71' },
                { name: 'Malassezia (שמרים)', percentage: 20, color: '#e74c3c' },
                { name: 'אחרים', percentage: 20, color: '#bdc3c7' }
            ]
        },
         'hand': {
            description: "אזור חשוף לסביבה ולשטיפות תכופות, עם מגוון משתנה.",
            species: [
                { name: 'Staphylococcus', percentage: 50, color: '#3498db' },
                { name: 'Corynebacterium', percentage: 15, color: '#2ecc71' },
                { name: 'Streptococcus', percentage: 10, color: '#9b59b6' },
                 { name: 'אחרים', percentage: 25, color: '#bdc3c7' }
            ]
        },
         'back': {
            description: "אזור שומני בחלקו העליון ויבש בחלקו התחתון, סביבה מורכבת.",
            species: [
                 { name: 'Cutibacterium', percentage: 40, color: '#f39c12' },
                 { name: 'Staphylococcus', percentage: 30, color: '#3498db' },
                 { name: 'Malassezia (שמרים)', percentage: 10, color: '#e74c3c' },
                 { name: 'אחרים', percentage: 20, color: '#bdc3c7' }
            ]
        }
    };

    // Define how factors change species percentages (example simple effects)
    // Changes are relative points, not percentages of current percentage.
    // Will need normalization after applying changes.
    const factorEffects = {
        'antibacterial-soap': {
            'Cutibacterium': -15,
            'Staphylococcus': -20,
            'Corynebacterium': -15,
            'Streptococcus': -10,
            'Malassezia (שמרים)': +5 // Can sometimes increase if bacteria suppressed
        },
        'moisturizer': {
            'Cutibacterium': -5, // Moisturizer might slightly reduce oiliness
            'Staphylococcus': +10, // Can slightly increase some moisture-loving bacteria
            'Corynebacterium': +8,
            'Malassezia (שמרים)': -3 // Might slightly inhibit yeast
        },
        'sun-exposure': {
             'Cutibacterium': -10, // UV can reduce bacteria
             'Staphylococcus': -15,
             'Corynebacterium': -8,
             'Streptococcus': -5,
             'Malassezia (שמרים)': +5 // Can sometimes thrive on sun-damaged skin
        },
         'antibiotics': { // Systemic antibiotics have broad effects
            'Cutibacterium': -25,
            'Staphylococcus': -25,
            'Corynebacterium': -20,
            'Streptococcus': -15,
            'Malassezia (שמרים)': +15 // Often leads to fungal overgrowth
         }
    };

    let selectedArea = null;

    const hotspots = document.querySelectorAll('.hotspot');
    const microbiomeDataElement = document.getElementById('microbiome-data');
    const simulationResultElement = document.getElementById('simulation-result');
    const simulateButton = document.getElementById('simulate-button');
    const factorCheckboxes = document.querySelectorAll('input[name="factor"]');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const panelTitle = document.getElementById('panel-title');
    const simulationControlsDiv = document.getElementById('simulation-controls');
    const initialMessageDiv = document.querySelector('.initial-message');


    // Event Listeners
    hotspots.forEach(hotspot => {
        hotspot.addEventListener('click', () => {
            const area = hotspot.getAttribute('data-area');
            selectArea(hotspot, area);
        });
    });

    simulateButton.addEventListener('click', () => {
        if (!selectedArea) return;

        const selectedFactors = Array.from(factorCheckboxes)
            .filter(checkbox => checkbox.checked)
            .map(checkbox => checkbox.value);

        simulateMicrobiome(selectedArea, selectedFactors, 'simulation-result');
    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.contains('visible'); // Check class for animation
        if (isHidden) {
             explanationDiv.classList.remove('visible');
             // Use setTimeout to allow animation to run before hiding
             setTimeout(() => { explanationDiv.style.display = 'none'; }, 500); // Match transition duration
             toggleExplanationButton.textContent = 'הצג הסבר מורחב';
        } else {
             explanationDiv.style.display = 'block';
             // Use setTimeout to allow display change before adding class
             setTimeout(() => { explanationDiv.classList.add('visible'); }, 10); // Small delay
             toggleExplanationButton.textContent = 'הסתר הסבר מורחב';
        }
    });


    // Functions
    function selectArea(clickedHotspot, area) {
         // Remove 'selected' class from all hotspots
        hotspots.forEach(h => h.classList.remove('selected'));
        // Add 'selected' class to the clicked hotspot
        clickedHotspot.classList.add('selected');

        selectedArea = area;
        panelTitle.textContent = clickedHotspot.textContent + ': הרכב המיקרוביום'; // Update panel title
        initialMessageDiv.style.display = 'none'; // Hide initial message
        simulationControlsDiv.style.display = 'block'; // Show simulation controls

        // Clear previous simulation results and factor selections
        simulationResultElement.innerHTML = '';
        factorCheckboxes.forEach(checkbox => checkbox.checked = false);

        displayMicrobiome(area, 'microbiome-data');
        simulateButton.disabled = false; // Enable simulation button
    }


    function displayMicrobiome(area, elementId) {
        const data = microbiomeData[area];
        const element = document.getElementById(elementId);

        if (!data) {
            element.innerHTML = 'אין נתונים עבור אזור זה.';
            return;
        }

        let html = `<p><b>מאפייני האזור:</b> ${data.description}</p>`;
        html += '<h4>הרכב בסיסי:</h4>';
        html += renderSpeciesChart(data.species); // Use chart rendering function

        element.innerHTML = html;

         // Trigger animation for bars
        setTimeout(() => {
             element.querySelectorAll('.species-bar').forEach(bar => {
                 bar.style.width = bar.getAttribute('data-percentage') + '%';
             });
        }, 100); // Small delay to ensure element is rendered
    }

    function simulateMicrobiome(area, factors, elementId) {
        const baseData = microbiomeData[area];
         // Deep copy species data including color
        let simulatedSpecies = baseData.species.map(s => ({ ...s }));

        let changes = {};

        factors.forEach(factor => {
            const effects = factorEffects[factor];
            if (effects) {
                for (const speciesName in effects) {
                     // Find the species object to ensure it exists in the base data
                     const species = simulatedSpecies.find(s => s.name === speciesName);
                     if (species) {
                        if (!changes[speciesName]) {
                            changes[speciesName] = 0;
                        }
                        changes[speciesName] += effects[speciesName];
                     }
                }
            }
        });

        // Apply changes and collect species with changes for explicit display
        let speciesWithChanges = [];
        simulatedSpecies.forEach(s => {
            const basePercentage = baseData.species.find(b => b.name === s.name)?.percentage || 0;
            const change = changes[s.name] || 0;
            s.percentage = basePercentage + change; // Apply additive change points

            if (s.percentage < 0) s.percentage = 0; // Ensure percentage is not negative

            if (change !== 0) {
                 speciesWithChanges.push({ name: s.name, change: change });
            }
        });


         // --- Normalization ---
         // Calculate the current total percentage after applying changes
         let total = simulatedSpecies.reduce((sum, s) => sum + s.percentage, 0);

         // Simple normalization: if total is not 100, scale all percentages.
         // This is a simplification. Real normalization is complex.
         if (total > 0 && total !== 100) {
             simulatedSpecies.forEach(s => {
                 s.percentage = parseFloat(((s.percentage / total) * 100).toFixed(1)); // Re-normalize and round
             });
         } else if (total === 0) {
             // Handle case where all species dropped to 0
             simulatedSpecies.forEach(s => s.percentage = 0);
         }


        let html = '';
         if (factors.length === 0) {
             html += '<p>אנא בחר גורם משפיע אחד או יותר כדי להדמות שינוי.</p>';
         } else {
             html += '<h4>השפעת הגורמים שנבחרו:</h4>';
              // Optional: List specific changes if desired, or just show the final result
              // html += '<ul>';
              // speciesWithChanges.forEach(item => {
              //      const changeText = item.change > 0 ? `+${item.change}` : `${item.change}`;
              //      html += `<li>${item.name}: שינוי של ${changeText} נקודות (לפני נרמול)</li>`;
              // });
              // html += '</ul>';

             html += '<h4>הרכב המיקרוביום לאחר ההדמיה:</h4>';
             html += renderSpeciesChart(simulatedSpecies);

             html += `<p><small><i>הדמיה זו פשטנית ומייצגת שינויים אופייניים. ההשפעה בפועל מורכבת ותלויה בגורמים רבים.</i></small></p>`;
         }

        document.getElementById(elementId).innerHTML = html;

         // Trigger animation for bars
         setTimeout(() => {
             document.getElementById(elementId).querySelectorAll('.species-bar').forEach(bar => {
                 bar.style.width = bar.getAttribute('data-percentage') + '%';
             });
         }, 100); // Small delay
    }

    function renderSpeciesChart(speciesData) {
         let html = '<ul class="species-list">';
         // Sort species by percentage for better visualization
         speciesData.sort((a, b) => b.percentage - a.percentage);

         speciesData.forEach(s => {
             // Ensure percentage is valid
             const percentage = Math.max(0, parseFloat(s.percentage.toFixed(1)));
             const barColor = s.color || '#3498db'; // Default color

              html += `<li class="species-item">
                          <span class="species-name">${s.name}</span>
                          <div class="species-bar-container">
                              <div class="species-bar" style="background-color: ${barColor};" data-percentage="${percentage}"></div>
                          </div>
                          <span class="species-percentage">${percentage}%</span>
                      </li>`;
         });
         html += '</ul>';
         return html;
    }


     // Initialize - disable simulate button until area is selected, set initial panel state
     simulateButton.disabled = true;
     simulationControlsDiv.style.display = 'none'; // Hide controls initially
     explanationDiv.style.display = 'none'; // Ensure explanation is hidden initially


</script>
---
```