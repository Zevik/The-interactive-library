---
title: "כימיה של קסם הצבע: מסע בזמן למעבדת פיגמנטים היסטורית"
english_slug: color-creation-chemistry-journey-to-19th-century-lab
category: "כימיה"
tags:
  - כימיה
  - היסטוריה של המדע
  - צבעים
  - פיגמנטים
  - מעבדה
---
# כימיה של קסם הצבע: מסע בזמן למעבדת פיגמנטים היסטורית

דמיינו עולם לפני צבעים שיוצרו בפס ייצור. במאה ה-19, יצירת צבעים בהירים ועמידים הייתה אמנות מסתורית ומלאכת יד כימית מדויקת, שדרשה שילוב של ידע, ניסוי וטעייה, ולעיתים גם אומץ (עקב הסכנות הכרוכות בחומרים). הצטרפו אלינו למסע וירטואלי מרתק למעבדה היסטורית, וגלו בעצמכם כיצד חומרים פשוטים לכאורה הפכו לפיגמנטים שצבעו את העולם.

<style>
/* Global styles */
body {
    font-family: 'Arial', sans-serif; /* Modern yet readable font */
    line-height: 1.6;
    color: #333;
    background-color: #f4f7f6; /* Light background */
}

/* App container */
#app-container {
    max-width: 850px; /* Slightly wider */
    margin: 30px auto; /* More margin */
    padding: 30px;
    border: 1px solid #d3dce0; /* Softer border */
    border-radius: 12px; /* More rounded corners */
    background-color: #ffffff; /* Clean white background */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    overflow: hidden; /* Clear floats */
}

#app-container h2 {
    text-align: center;
    color: #2c3e50; /* Darker, professional header color */
    margin-top: 0;
    margin-bottom: 25px;
    font-size: 2em; /* Larger title */
}

/* Recipe selection */
#recipe-selection {
    margin-bottom: 30px;
    text-align: center;
    background-color: #ecf0f1; /* Light grey background */
    padding: 15px;
    border-radius: 8px;
    display: flex; /* Use flexbox for alignment */
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    gap: 15px; /* Space between elements */
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
}

#recipe-selection label {
    font-weight: bold;
    color: #34495e; /* Darker text */
    font-size: 1.1em;
}

#recipes {
    padding: 10px;
    border-radius: 6px;
    border: 1px solid #bdc3c7; /* Softer border */
    font-size: 1em;
    min-width: 180px; /* Ensure reasonable width */
}

#start-experiment {
    padding: 10px 20px;
    background-color: #2ecc71; /* Green button */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transition */
}

#start-experiment:hover:not(:disabled) {
    background-color: #27ae60; /* Darker green on hover */
    transform: translateY(-2px); /* Slight lift */
}

#start-experiment:active:not(:disabled) {
    transform: translateY(0); /* Press effect */
}

#start-experiment:disabled {
    background-color: #a9cce3; /* Grey out when disabled */
    cursor: not-allowed;
}


/* Lab area layout */
#lab-area {
    display: flex;
    justify-content: space-around;
    align-items: flex-start;
    background-color: #f9f9f9; /* Very light background */
    padding: 25px;
    border-radius: 8px;
    min-height: 400px; /* Taller */
    flex-wrap: wrap; /* Allow wrapping */
    gap: 20px; /* Space between cabinet and experiment */
    border: 1px dashed #bdc3c7; /* Dashed border for lab bench feel */
}

/* Chemicals Cabinet */
#chemicals-cabinet {
    width: 35%; /* Slightly wider */
    min-width: 200px; /* Minimum width */
    border: 1px solid #bdc3c7;
    padding: 15px;
    background-color: #ecf0f1; /* Light grey background */
    border-radius: 8px;
    box-shadow: inset 0 2px 5px rgba(0,0,0,0.05); /* Inner shadow */
}

#chemicals-cabinet h4 {
    margin-top: 0;
    color: #34495e;
    text-align: center;
    margin-bottom: 15px;
    font-size: 1.2em;
}

#chemical-list {
    list-style: none;
    padding: 0;
}

.chemical-item {
    padding: 12px; /* More padding */
    margin-bottom: 8px; /* More space between items */
    background-color: #e0e5e9; /* Slightly darker background for items */
    border: 1px solid #c0c8cf;
    border-radius: 6px; /* Rounded corners */
    cursor: pointer;
    transition: background-color 0.2s ease, transform 0.1s ease;
    font-size: 0.95em;
    display: flex; /* Flex for potential icon/styling */
    align-items: center;
    justify-content: center; /* Center text */
}

.chemical-item:hover {
    background-color: #d5dde4; /* Hover effect */
    transform: translateY(-2px); /* Slight lift */
}

.chemical-item.correct-next {
    border-color: #2ecc71; /* Highlight border */
    background-color: #d4edda; /* Highlight background */
    font-weight: bold;
    animation: pulse 1s infinite ease-in-out; /* Subtle pulse animation */
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.02); }
    100% { transform: scale(1); }
}

/* Experiment area */
#experiment-area {
    width: 55%; /* Slightly narrower */
    min-width: 280px;
    text-align: center;
    position: relative;
    display: flex; /* Flexbox for beaker and content */
    flex-direction: column; /* Stack vertically */
    align-items: center; /* Center horizontally */
    justify-content: flex-end; /* Align to bottom */
    padding-bottom: 20px; /* Space below beaker */
}

#beaker-container {
    position: relative;
    width: 150px; /* Larger beaker */
    height: 200px; /* Taller beaker */
    margin-bottom: 15px;
}

#beaker-img {
    width: 100%;
    height: 100%;
    object-fit: contain; /* Maintain aspect ratio */
    position: absolute;
    bottom: 0;
    left: 0;
    z-index: 2; /* Ensure beaker is above liquid */
}

#beaker-content {
    position: absolute;
    bottom: 15px; /* Adjust based on beaker image base */
    left: 50%;
    transform: translateX(-50%);
    width: 80%; /* Width relative to beaker container */
    height: 0; /* Starts empty */
    background-color: transparent;
    border-radius: 0 0 20px 20px; /* Rounded bottom to fit beaker */
    z-index: 1; /* Below beaker image */
    transition: height 1.2s ease-out, background-color 1.5s ease-in-out; /* Smoother, slightly longer transitions */
}

.beaker-content-fill {
     transition: height 1.2s ease-out, background-color 1.5s ease-in-out; /* Ensure transition is active */
}

.beaker-final-pigment {
    border-radius: 15px; /* Change shape for solid pigment */
    bottom: 10px; /* Lower slightly */
    transition: height 1.2s ease-out, background-color 1.5s ease-in-out, border-radius 0.8s ease, bottom 0.8s ease; /* Include radius and position transitions */
}


#current-chemicals {
    font-size: 1em;
    color: #555;
    min-height: 1.2em; /* Reserve space */
}

/* Controls */
#controls {
    margin-top: 30px;
    text-align: center;
}

#reset-experiment {
    padding: 10px 20px;
    background-color: #e74c3c; /* Red button */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
     transition: background-color 0.3s ease, transform 0.1s ease;
}
#reset-experiment:hover {
     background-color: #c0392b; /* Darker red on hover */
      transform: translateY(-2px);
}
#reset-experiment:active {
     transform: translateY(0);
}


/* Feedback area */
#feedback-area {
    margin-top: 20px;
    padding: 15px;
    border-radius: 6px;
    min-height: 40px; /* Taller to prevent layout shifts */
    text-align: center;
    font-weight: bold;
    background-color: #fefce8; /* Light yellow background */
    border: 1px solid #fcd34d; /* Yellow border */
    color: #b45309; /* Dark yellow text */
    transition: background-color 0.5s ease; /* Smooth transition */
}

.feedback-success {
    background-color: #d4edda !important; /* Light green */
    border-color: #28a745 !important; /* Green border */
    color: #155724 !important; /* Dark green text */
}

.feedback-error {
    background-color: #f8d7da !important; /* Light red */
    border-color: #dc3545 !important; /* Red border */
    color: #721c24 !important; /* Dark red text */
}


/* Result area */
#result-area {
    margin-top: 30px;
    padding: 20px;
    border: 2px solid #3498db; /* Blue border */
    border-radius: 8px;
    text-align: center;
    display: none; /* Initially hidden */
    background-color: #ecf0f1; /* Light grey background */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

#result-area h4 {
    color: #2980b9; /* Dark blue header */
    margin-top: 0;
    margin-bottom: 15px;
}

#final-pigment {
    width: 120px; /* Larger swatch */
    height: 120px; /* Larger swatch */
    margin: 15px auto;
    border: 2px solid #333; /* Dark border */
    border-radius: 8px; /* Rounded corners */
    box-shadow: inset 0 0 10px rgba(0,0,0,0.2); /* Inner shadow */
    transition: background-color 1s ease; /* Animate color appearance */
}

#result-text {
    font-size: 1.1em;
    color: #34495e;
    font-weight: bold;
}

/* Explanation toggle */
#toggle-explanation {
    display: block;
    margin: 30px auto;
    padding: 12px 25px;
    background-color: #3498db; /* Blue button */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
}

#toggle-explanation:hover {
    background-color: #2980b9; /* Darker blue on hover */
    transform: translateY(-2px);
}
#toggle-explanation:active {
     transform: translateY(0);
}


/* Explanation area */
#explanation {
    display: none; /* Initially hidden */
    margin-top: 30px;
    padding: 25px;
    border: 1px solid #d3dce0;
    border-radius: 12px;
    background-color: #fefefe;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
}

#explanation h2 {
     color: #2c3e50;
     margin-top: 0;
     margin-bottom: 20px;
}

#explanation p {
    margin-bottom: 15px;
    text-align: justify;
}

#explanation b {
    color: #34495e;
}

#explanation ul {
    margin-bottom: 15px;
    padding-left: 20px;
}

#explanation li {
    margin-bottom: 8px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    #lab-area {
        flex-direction: column; /* Stack vertically */
        align-items: center; /* Center items */
    }

    #chemicals-cabinet, #experiment-area {
        width: 95%; /* Full width on smaller screens */
        min-width: 0; /* Remove min-width constraint */
    }

    #recipe-selection {
        flex-direction: column; /* Stack selection elements */
        gap: 10px;
    }
}

</style>

<div id="app-container">

    <h2>מעבדת הפיגמנטים ההיסטורית</h2>

    <div id="recipe-selection">
        <label for="recipes">בחר מתכון כימי עתיק:</label>
        <select id="recipes">
            <option value="">-- בחר מסע --</option>
            <option value="prussian-blue">כחול פרוסי (Prussian Blue)</option>
            <option value="chrome-yellow">כרום צהוב (Chrome Yellow)</option>
        </select>
        <button id="start-experiment">התחל את המסע הכימי</button>
    </div>

    <div id="lab-area">

        <div id="chemicals-cabinet">
            <h4>מלאי כימיקלים</h4>
            <ul id="chemical-list">
                <!-- כימיקלים יטענו לכאן עם בחירת המתכון -->
            </ul>
        </div>

        <div id="experiment-area">
            <div id="beaker-container">
                 <img id="beaker-img" src="https://www.svgrepo.com/show/146295/beaker.svg" alt="כוס כימית"> <!-- SVG beaker -->
                 <div id="beaker-content"></div>
            </div>
            <p id="current-chemicals">בחר מתכון והתחל ניסוי...</p>
        </div>

    </div>

    <div id="controls">
         <button id="reset-experiment">התחל מחדש</button>
    </div>


    <div id="feedback-area"></div>

    <div id="result-area">
        <h4>הקסם התרחש! התוצאה במבחנה:</h4>
        <div id="final-pigment"></div>
        <p id="result-text"></p>
    </div>

</div>

<button id="toggle-explanation">פענוח הקסם: הסבר מדעי והיסטורי</button>

<div id="explanation">
    <h2>הסבר מדעי והיסטורי: יצירת צבעים במעבדה</h2>

    <p><b>הקדמה: הקסם של הצבע והצורך האנושי לצבוע את העולם.</b></p>
    <p>מאז שחר ההיסטוריה, האנושות שאפה להעניק צבעוניות עשירה ומגוונת לסביבתה – בבגדים, באמנות, בקישוטים ובחיי היום-יום. צבעים לא היו רק עניין אסתטי, אלא גם סמלים של מעמד, כוח וזהות. אך השגת צבעים יציבים, בהירים וזמינים הייתה אתגר טכנולוגי עצום במשך אלפי שנים. לפני המצאת הצבעים הסינתטיים, העולם הסתמך על מקורות טבעיים, שלרוב היו נדירים, יקרים, דהויים או לא עמידים.</p>

    <p><b>המעבר מהטבע למעבדה: לידת הכימיה של הפיגמנטים.</b></p>
    <p>בעוד צבעים טבעיים הופקו מצמחים, מינרלים או בעלי חיים, המהפכה הכימית במאות ה-18 וה-19 פתחה דלתות חדשות. כימאים החלו לחקור כיצד ליצור חומרים צבעוניים באופן מלאכותי, במעבדה. זה לא היה תהליך פשוט; הוא דרש הבנה הולכת וגוברת של תגובות כימיות ושל התכונות של חומרים שונים, במיוחד מלחי מתכות.</p>

    <p><b>צבע בעולם הכימיה: איך חומרים "רואים" אור?</b></p>
    <p>צבעו של חומר נובע מהאינטראקציה שלו עם האור הנראה. פיגמנטים, במיוחד אלו המבוססים על מתכות מעבר, מכילים אלקטרונים שיכולים לבלוע אור באורכי גל מסוימים. האור שלא נבלע – כלומר, אורכי הגל המוחזרים או המועברים – הוא מה שאנו תופסים כצבע של הפיגמנט. לדוגמה, חומר שנראה כחול בולע בעיקר אור אדום וצהוב, ומחזיר את האור הכחול.</p>

    <p><b>טכניקות אלכימיה מודרנית: יצירת פיגמנטים על ידי שקיעה.</b></p>
    <p>אחת השיטות הנפוצות והאפקטיביות ביותר ליצירת פיגמנטים אנאורגניים במאה ה-19 הייתה באמצעות "תגובות שקיעה". בתגובה כזו, מערבבים שתי תמיסות מימיות של מלחים מסיסים. כאשר היונים מהמלחים הללו נפגשים בתמיסה, הם מתארגנים מחדש ויוצרים תרכובת יונית חדשה שאינה מסיסה במים. תרכובת זו נופלת מתוך התמיסה כמוצק מוצק – משקע – והוא הפיגמנט הצבעוני שאותו רצו ליצור.</p>

    <p><b>החומרים הסודיים (ולעיתים מסוכנים): מלחי מתכות כבדות.</b></p>
    <p>רבים מהפיגמנטים המרהיבים של המאה ה-19 יצרו באמצעות מלחי מתכות כבדות כמו עופרת, כרום, נחושת, ברזל ואף ארסן. מתכות אלו היו חיוניות לקבלת מגוון רחב של גוונים ויציבות יחסית (ביחס לצבעים טבעיים מסוימים), אך טמנו בחובן סכנות בריאותיות חמורות ביותר. כימאים ופועלים שעבדו עם חומרים אלו, ואף אנשים שהשתמשו במוצרים צבועים בהם (טפטים, צעצועים!), היו חשופים להרעלות קשות.</p>

    <p><b>פיגמנטים אייקונים ממעבדת העבר (והמתכונים שלהם):</b></p>
    <ul>
        <li><b>כחול פרוסי (Prussian Blue):</b> פיגמנט כחול עמוק ואינטנסיבי, מהראשונים שנוצרו באופן סינתטי (תחילת המאה ה-18, שימושי במאה ה-19). יצירתו כוללת לרוב ערבוב תמיסה המכילה יוני ברזל תלת-ערכי (Fe³⁺) עם תמיסה המכילה יוני פרוציאניד ([Fe(CN)₆]⁴⁻). התוצר הוא תרכובת מורכבת בעלת הנוסחה האופיינית Fe₄[Fe(CN)₆]₃, השוקעת כמשקע כחול כהה.</li>
        <li><b>כרום צהוב (Chrome Yellow):</b> צהוב בוהק ועשיר שהפך פופולרי מאוד במאה ה-19 ושימש אמנים רבים. הוא נוצר בתגובת שקיעה בין מלח עופרת מסיס (המכיל יוני Pb²⁺, למשל עופרת ניטראט) ומלח כרומט מסיס (המכיל יוני CrO₄²⁻, למשל אשלגן כרומט). התוצר הוא עופרת כרומט, PbCrO₄, ששוקע כפיגמנט צהוב. למרות יופיו, הוא מכיל עופרת רעילה.</li>
        <li><b>ירוק פריז (Paris Green / Schweinfurt Green):</b> ירוק זוהר, אך קטלני, שהכיל ארסן ונחושת. נוצר מערבוב נחושת אצטט וארסן תלת-חמצני. שימש לצביעת טפטים, בגדים וצעצועים, וגרם לתחלואה קשה.</li>
    </ul>

    <p><b>אתגרי "הבישול" הכימי: טוהר, יציבות וסכנה.</b></p>
    <p>ייצור הפיגמנטים במעבדה ההיסטורית היה אתגר תמידי. קשה היה לשלוט באופן מדויק על התגובה כדי לקבל פיגמנט טהור לחלוטין ללא זיהומים שפגעו בגוון או ביציבות. פיגמנטים רבים דהו באור או השחירו בחשיפה לאוויר המזוהם של הערים המתועשות. בנוסף, העבודה עם חומרים רעילים ללא אמצעי בטיחות מתאימים הייתה סכנה יומיומית.</p>

    <p><b>המהפכה הבאה: עידן צבעי האנילין.</b></p>
    <p>באמצע המאה ה-19, גילוי ופיתוח צבעי אנילין סינתטיים מחומרי גלם שמקורם בפחם (תרכובות אורגניות) חולל מהפכה נוספת. צבעים אלו היו לעיתים קרובות זולים יותר לייצור, בהירים יותר ועמידים יותר מפיגמנטים אנאורגניים היסטוריים או צבעים טבעיים. הם פתחו עידן חדש בתעשיית הטקסטיל, הדפוס והאמנות, והפחיתו בהדרגה את התלות (והחשיפה) לפיגמנטים המסוכנים מבוססי מתכות כבדות, אך סיפורם של הפיגמנטים ההיסטוריים נותר מרתק – הצצה לשילוב הייחודי של כימיה, אמנות, תעשייה וסיכון.</p>

</div>

<script>
    const recipes = {
        'prussian-blue': {
            name: 'כחול פרוסי',
            chemicals: [
                { name: 'ברזל כלורי', id: 'ferric-chloride', formula: 'FeCl₃' },
                { name: 'אשלגן פרוציאנידי', id: 'potassium-ferrocyanide', formula: 'K₄[Fe(CN)₆]' }
            ],
            steps: [
                { chemical_id: 'ferric-chloride', visual_change: '#f0f0f0', text: 'הוסף את הברזל הכלורי. התמיסה שקופה/צהבהבה עדינה...' },
                { chemical_id: 'potassium-ferrocyanide', visual_change: '#003366', text: 'ועכשיו את האשלגן הפרוציאנידי... צפה בקסם הכימי!', result_text: 'וואלה! יצרת פיגמנט כחול פרוסי מרהיב!', result_color: '#003366' }
            ]
        },
        'chrome-yellow': {
            name: 'כרום צהוב',
            chemicals: [
                { name: 'עופרת ניטראט', id: 'lead-nitrate', formula: 'Pb(NO₃)₂' },
                { name: 'אשלגן כרומט', id: 'potassium-chromate', formula: 'K₂CrO₄' }
            ],
             steps: [
                { chemical_id: 'lead-nitrate', visual_change: '#f0f0f0', text: 'הוסף את העופרת הניטראט לתמיסה. היא נראית שקופה...' },
                { chemical_id: 'potassium-chromate', visual_change: '#FFD700', text: 'הגיע תור האשלגן הכרומט... הנה בא הצבע!', result_text: 'מדהים! נוצר פיגמנט כרום צהוב בוהק!', result_color: '#FFD700' }
            ]
        }
    };

    let currentRecipe = null;
    let currentStep = 0;
    let addedChemicals = [];
    const maxBeakerHeight = 140; // Max height in pixels for the liquid visually

    const recipeSelect = document.getElementById('recipes');
    const startButton = document.getElementById('start-experiment');
    const chemicalListElement = document.getElementById('chemical-list');
    const beakerContent = document.getElementById('beaker-content');
    const currentChemicalsText = document.getElementById('current-chemicals');
    const feedbackArea = document.getElementById('feedback-area');
    const resultArea = document.getElementById('result-area');
    const finalPigmentDiv = document.getElementById('final-pigment');
    const resultTextP = document.getElementById('result-text');
    const resetButton = document.getElementById('reset-experiment');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Helper to update feedback with styling
    function setFeedback(message, type = 'info') {
        feedbackArea.textContent = message;
        feedbackArea.className = ''; // Clear previous classes
        feedbackArea.classList.add(type === 'success' ? 'feedback-success' : (type === 'error' ? 'feedback-error' : ''));
    }

    function resetExperiment() {
        currentRecipe = null;
        currentStep = 0;
        addedChemicals = [];
        recipeSelect.value = "";
        chemicalListElement.innerHTML = '';
        // Reset beaker visuals
        beakerContent.style.height = '0';
        beakerContent.style.backgroundColor = 'transparent';
        beakerContent.classList.remove('beaker-final-pigment', 'beaker-content-fill'); // Remove animation classes
        beakerContent.style.borderRadius = '0 0 20px 20px'; // Reset border radius
        beakerContent.style.bottom = '15px'; // Reset position
        beakerContent.style.transition = 'none'; // Disable transition temporarily
        // Force reflow to apply reset immediately
        beakerContent.offsetHeight;
        // Re-enable transition after reflow
        beakerContent.style.transition = 'height 1.2s ease-out, background-color 1.5s ease-in-out';


        currentChemicalsText.textContent = 'בחר מתכון והתחל ניסוי...';
        setFeedback(''); // Clear feedback
        resultArea.style.display = 'none';
        finalPigmentDiv.style.backgroundColor = '';
        resultTextP.textContent = '';
        startButton.disabled = false;

         // Remove highlight from chemical list items
         document.querySelectorAll('.chemical-item').forEach(item => {
             item.classList.remove('correct-next');
         });
    }

    function startExperiment() {
        const selectedRecipeKey = recipeSelect.value;
        if (!selectedRecipeKey) {
            setFeedback('אנא בחר מתכון כדי להתחיל את המסע הכימי.', 'error');
            return;
        }

        currentRecipe = recipes[selectedRecipeKey];
        currentStep = 0;
        addedChemicals = [];

        // Populate chemicals cabinet
        chemicalListElement.innerHTML = '';
        currentRecipe.chemicals.forEach(chem => {
            const li = document.createElement('li');
            li.classList.add('chemical-item');
            li.textContent = `${chem.name} (${chem.formula})`;
            li.dataset.chemicalId = chem.id;
            li.onclick = () => addChemical(chem.id);
            chemicalListElement.appendChild(li);
        });

        // Reset visual and feedback
        beakerContent.style.height = '0';
        beakerContent.style.backgroundColor = 'transparent';
        beakerContent.classList.remove('beaker-final-pigment');
        beakerContent.style.borderRadius = '0 0 20px 20px';
        beakerContent.style.bottom = '15px';
         // Re-enable transition
        beakerContent.style.transition = 'height 1.2s ease-out, background-color 1.5s ease-in-out';

        const firstStepText = currentRecipe.steps[0].text.split('.')[0] + '.'; // Get first sentence
        currentChemicalsText.textContent = 'הוסף את החומר הראשון: ' + firstStepText;
        setFeedback('התחל בהוספת החומרים לפי המתכון. לחץ על החומר הראשון בארון.', 'info');
        resultArea.style.display = 'none';
        startButton.disabled = true; // Disable start button until reset

        highlightNextChemical(); // Highlight the first chemical needed
    }

     function highlightNextChemical() {
        // Remove highlight from all chemicals first
        document.querySelectorAll('.chemical-item').forEach(item => {
            item.classList.remove('correct-next');
            item.style.animation = 'none'; // Stop pulse
             item.offsetHeight; // Trigger reflow
             item.style.animation = null; // Re-enable animation if needed later
        });

        if (currentRecipe && currentStep < currentRecipe.steps.length) {
            const nextChemicalId = currentRecipe.steps[currentStep].chemical_id;
            const nextChemicalItem = document.querySelector(`.chemical-item[data-chemical-id="${nextChemicalId}"]`);
            if (nextChemicalItem) {
                nextChemicalItem.classList.add('correct-next');
                 nextChemicalItem.style.animation = 'pulse 1s infinite ease-in-out'; // Start pulse
            }
        }
     }


    function addChemical(chemicalId) {
        if (!currentRecipe || currentStep >= currentRecipe.steps.length) {
            setFeedback('המסע הכימי הסתיים או טרם החל. אנא התחל ניסוי חדש.', 'info');
            return;
        }

        const expectedChemicalId = currentRecipe.steps[currentStep].chemical_id;
        const stepInfo = currentRecipe.steps[currentStep];

        if (chemicalId === expectedChemicalId) {
            addedChemicals.push(chemicalId);
            setFeedback('בול בפוני! החומר הנכון נוסף למבחנה.', 'success');

            // Simulate adding liquid/precipitate
            // Calculate target height based on step number
            const targetHeight = (currentStep + 1) / currentRecipe.steps.length * maxBeakerHeight;

            // Add class to ensure transitions are active before setting properties
            beakerContent.classList.add('beaker-content-fill');
             // Set height and color - transitions handle the animation
            beakerContent.style.height = targetHeight + 'px';
            beakerContent.style.backgroundColor = stepInfo.visual_change;

             // Remove pulse from the added chemical and add a temporary "added" visual?
            const addedItem = document.querySelector(`.chemical-item[data-chemical-id="${chemicalId}"]`);
             if(addedItem) {
                 addedItem.classList.remove('correct-next');
                 addedItem.style.animation = 'none'; // Stop pulse immediately
                 // Optional: add a temporary class for a quick visual confirmation like fading or shrinking
             }


            if (currentStep === currentRecipe.steps.length - 1) {
                // Last step - pigment formed!
                currentChemicalsText.textContent = stepInfo.text;
                 setFeedback('מצוין! כל החומרים נוספו. צפה בתוצאה הסופית!', 'success');

                // Delay showing result slightly to allow beaker animation to finish
                setTimeout(() => {
                    showResult(stepInfo.result_text, stepInfo.result_color);
                    beakerContent.classList.add('beaker-final-pigment'); // Change shape for final pigment
                    // beakerContent.style.bottom = '10px'; // Lower slightly for sediment effect - handled by class now
                     // Remove the general fill class to prevent conflicting transitions if needed, or let final class override
                     beakerContent.classList.remove('beaker-content-fill');

                }, 1500); // Wait for beaker animation

            } else {
                // Move to next step
                currentStep++;
                 const nextStepText = currentRecipe.steps[currentStep].text.split('.')[0] + '.';
                 currentChemicalsText.textContent = 'מצוין! כעת הוסף את החומר הבא: ' + nextStepText;
                 highlightNextChemical(); // Highlight the next chemical
            }

        } else {
            setFeedback('רגע, זה לא החומר הנכון לשלב הזה במתכון. אנא בדוק שוב.', 'error');
            // Optional: Add a small animation to the beaker on error (e.g., shake)
        }
    }

    function showResult(text, color) {
        resultArea.style.display = 'block';
        finalPigmentDiv.style.backgroundColor = color; // This will transition due to CSS
        resultTextP.textContent = text;
    }

    // Event listeners
    startButton.addEventListener('click', startExperiment);
    resetButton.addEventListener('click', resetExperiment);
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מדעי והיסטורי' : 'פענוח הקסם: הסבר מדעי והיסטורי';
        // Scroll to explanation if shown
        if (!isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // Initial state - setup on page load
    document.addEventListener('DOMContentLoaded', resetExperiment);
</script>
---