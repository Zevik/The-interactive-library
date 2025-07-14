---
title: "קסם ההתפלה: איך להפוך מי ים למים ראויים לשתייה בעזרת אוסמוזה הפוכה"
english_slug: water-desalination-how-reverse-osmosis-works
category: "כימיה"
tags:
  - התפלה
  - אוסמוזה הפוכה
  - ממברנה
  - טיהור מים
  - הנדסת מים
  - מים מתוקים
---
# קסם ההתפלה: כך עובדת אוסמוזה הפוכה

דמיינו לרגע: להפוך את מי הים המלוחים, הלא ראויים לשתייה, למים צלולים ומתוקים. איך עושים את זה? התשובה טמונה בתהליך חכם שמכונה 'אוסמוזה הפוכה'. הוא מבוסס על עיקרון טבעי, אבל "הופך" אותו כדי לשרת את הצרכים שלנו. בואו נצלול פנימה ונראה איך הקסם הזה קורה, צעד אחר צעד, מול העיניים שלכם.

<div id="app-container">
    <div id="tank">
        <div id="left-side" class="side">
            <div class="side-label">מי ים מלוחים</div>
            <div id="water-left" class="water">
                 <div id="salt-ions-container"></div>
                 <div id="water-molecules-left-container"></div>
            </div>
             <div id="pressure-piston">
                <div class="piston-rod"></div>
                 <div class="piston-head"></div>
            </div>
        </div>
        <div id="membrane">
            <div class="membrane-label">ממברנה חצי-חדירה</div>
            <div class="membrane-pores"></div> <!-- Visual pores -->
        </div>
        <div id="right-side" class="side">
            <div class="side-label">מים טהורים</div>
            <div id="water-right" class="water">
                 <div id="water-molecules-right-container"></div>
            </div>
             <div id="flow-arrow-r-l" class="flow-arrow">←</div>
             <div id="flow-arrow-l-r" class="flow-arrow">→</div>
        </div>
    </div>
    <div id="controls">
        <label for="pressure-slider">הפעלת לחץ חיצוני:</label>
        <input type="range" id="pressure-slider" min="0" max="120" value="0">
        <span id="pressure-value">0</span>%
        <div id="pressure-status">לחץ אוסמוטי טיפוסי: ~50%</div>
    </div>
</div>

<style>
    #app-container {
        width: 100%;
        max-width: 700px;
        margin: 30px auto;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        border: 1px solid #0077cc; /* More vibrant border */
        border-radius: 12px;
        padding: 25px;
        box-sizing: border-box;
        background: linear-gradient(to bottom right, #e0f7fa, #b3e5fc); /* Soft gradient background */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* Prevent particles from overflowing */
    }

     h1 {
         text-align: center;
         color: #0056b3;
         margin-bottom: 20px;
         font-size: 1.8em;
     }

     #app-container + p { /* Style for the intro paragraph right after container */
         text-align: center;
         color: #333;
         margin-top: -10px; /* Adjust spacing */
         margin-bottom: 30px;
         font-size: 1.1em;
         line-height: 1.6;
     }


    #tank {
        display: flex;
        width: 100%;
        height: 350px; /* Slightly taller tank */
        border: 3px solid #0056b3; /* Stronger tank border */
        border-radius: 15px;
        overflow: hidden;
        position: relative;
        background-color: #e1f5fe; /* Lighter blue base */
    }

    .side {
        flex: 1;
        position: relative;
        overflow: hidden;
    }

    #membrane {
        width: 15px; /* Wider membrane */
        background-color: #673ab7; /* Purple tone for membrane */
        border-left: 2px dashed rgba(255, 255, 255, 0.5);
        border-right: 2px dashed rgba(255, 255, 255, 0.5);
        position: relative;
        z-index: 2;
        display: flex;
        align-items: center;
        justify-content: center;
         flex-direction: column; /* Stack label and pores */
    }

    .membrane-label {
        position: absolute; /* Keep absolute for rotation */
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%) rotate(90deg);
        white-space: nowrap;
        font-size: 0.9em; /* Slightly larger font */
        color: #fff;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.4); /* More prominent shadow */
        font-weight: bold;
    }

    .membrane-pores {
        position: absolute;
        width: 100%;
        height: 100%;
         background: repeating-linear-gradient(-45deg, rgba(255,255,255,0.2), rgba(255,255,255,0.2) 2px, transparent 2px, transparent 8px); /* Visual representation of pores */
        z-index: 1;
    }


    .side-label {
        position: absolute;
        top: 15px; /* Lowered slightly */
        left: 15px; /* Moved slightly right */
        font-size: 1em; /* Slightly larger */
        color: #01579b; /* Darker blue color */
        z-index: 3;
        font-weight: bold;
        text-shadow: 0 0 5px rgba(255,255,255,0.5); /* Subtle text shadow */
    }

    .water {
        position: absolute;
        bottom: 0;
        width: 100%;
        background: linear-gradient(to bottom, #4fc3f7, #0277bd); /* Vibrant blue gradient */
        transition: height 1s ease-in-out; /* Smooth level transition */
        min-height: 10%; /* Minimum base level */
        z-index: 0; /* Ensure water is below labels and particles */
    }

     #water-left {
         height: 50%; /* Starting height */
     }

     #water-right {
         height: 50%; /* Starting height */
     }

    /* Containers for particles within the water divs */
    #water-molecules-right-container,
    #water-molecules-left-container,
    #salt-ions-container {
         position: absolute;
         bottom: 0; /* Particles position relative to water bottom */
         left: 0;
         width: 100%;
         height: 100%; /* Containers take up full water area */
         pointer-events: none;
         z-index: 1; /* Above water, below labels/piston */
    }


    .molecule, .ion {
        position: absolute;
        width: 10px; /* Slightly larger particles */
        height: 10px;
        border-radius: 50%;
        transition: transform 0.5s ease-out; /* Smooth movement transition */
        will-change: transform; /* Optimize animation */
    }

    .molecule {
        background-color: rgba(255, 255, 255, 0.9); /* Bright white, less translucent */
        box-shadow: 0 0 4px rgba(0, 188, 212, 0.5); /* Subtle glow */
        border: 1px solid rgba(0, 188, 212, 0.3);
    }

    .ion {
        background-color: rgba(255, 87, 34, 0.9); /* Orange/Red for salt */
        box-shadow: 0 0 4px rgba(255, 87, 34, 0.5); /* Subtle glow */
        border: 1px solid rgba(255, 87, 34, 0.3);
    }

     /* Flow Arrows */
     .flow-arrow {
         position: absolute;
         bottom: 50%; /* Vertically centered in tank */
         font-size: 3em;
         font-weight: bold;
         color: rgba(0, 150, 136, 0.7); /* Teal color, semi-transparent */
         text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.3);
         opacity: 0; /* Initially hidden */
         transition: opacity 0.5s ease;
         z-index: 4; /* Above everything */
         pointer-events: none;
     }

     #flow-arrow-r-l {
         left: calc(50% + 20px); /* Position to the right of membrane */
         transform: translateX(-100%); /* Center the arrow head */
     }

     #flow-arrow-l-r {
         right: calc(50% + 20px); /* Position to the left of membrane */
         transform: translateX(100%); /* Center the arrow head */
     }


     #pressure-piston {
        position: absolute;
        top: 0; /* Position from the top */
        left: 0;
        width: 100%;
        z-index: 3; /* Above water */
        display: flex;
        flex-direction: column;
        align-items: center;
        transform: translateY(-40px); /* Start off-screen (more substantial piston) */
        transition: transform 0.5s ease-out; /* Animate movement */
     }

    #pressure-piston .piston-head {
        width: 105%; /* Slightly wider than tank */
        height: 25px; /* Thicker head */
        background-color: #546e7a; /* Greyish blue */
        border-radius: 5px 5px 0 0;
         box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
    }

    #pressure-piston .piston-rod {
        width: 30%; /* Wider rod */
        height: 40px; /* Initial rod height */
        background-color: #78909c; /* Lighter greyish blue */
        border-radius: 0 0 5px 5px;
    }


    #controls {
        margin-top: 30px; /* More space */
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px; /* Wider gap */
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    #controls label {
        font-weight: bold;
        color: #01579b;
        font-size: 1.1em;
    }

    #controls input[type="range"] {
        flex-grow: 1; /* Allow slider to take available space */
        max-width: 300px; /* Max width for slider */
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        height: 10px;
        background: #b0bec5; /* Light grey track */
        outline: none;
        opacity: 0.8;
        transition: opacity .2s;
        border-radius: 5px;
         cursor: pointer;
    }

    #controls input[type="range"]:hover {
        opacity: 1;
    }

    #controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #007bff; /* Blue thumb */
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    #controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff; /* Blue thumb */
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }


    #pressure-value {
        font-weight: bold;
        color: #007bff;
        min-width: 30px; /* Ensure space for value */
        display: inline-block;
        text-align: left;
    }


    #pressure-status {
        font-size: 0.95em;
        color: #555;
        margin-top: 5px;
        flex-basis: 100%; /* Place below slider */
        text-align: center;
    }


    #explanation-button {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 25px; /* Larger padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 8px; /* More rounded corners */
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3); /* Subtle button shadow */
    }

    #explanation-button:hover {
        background-color: #0056b3;
        box-shadow: 0 6px 12px rgba(0, 123, 255, 0.4);
    }

    #explanation-button:active {
        transform: translateY(2px); /* Press effect */
    }


    #explanation-content {
        margin-top: 30px; /* More space */
        padding: 20px; /* More padding */
        border: 1px solid #b3e5fc; /* Lighter border */
        border-radius: 8px;
        background-color: #e1f5fe; /* Soft background */
        display: none; /* Hidden by default */
         line-height: 1.7;
         color: #333;
         box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.05); /* Inner shadow */
    }

    #explanation-content h2 {
        color: #0056b3;
        margin-top: 20px;
        margin-bottom: 12px;
        border-bottom: 2px solid #b3e5fc; /* Styled border */
        padding-bottom: 8px;
        font-size: 1.5em;
    }

     #explanation-content h2:first-child {
         margin-top: 0;
     }

    #explanation-content p {
        margin-bottom: 15px; /* More space between paragraphs */
    }

    #explanation-content ul {
        margin-bottom: 15px;
        padding-left: 25px; /* More indent */
    }

    #explanation-content li {
         margin-bottom: 8px; /* More space between list items */
    }

     #explanation-content strong {
         color: #0056b3; /* Highlight key terms */
     }

</style>

<button id="explanation-button">חשיפת הסבר מעמיק</button>

<div id="explanation-content">
    <h2>מהי אוסמוזה ולחץ אוסמוטי?</h2>
    <p>דמיינו קרום דקיק עם חורים זעירים שרק מולקולות מים קטנות יכולות לעבור דרכם, אבל מולקולות מומסים גדולות יותר (כמו מלח) נתקעות. זהו העיקרון של **ממברנה חצי-חדירה**. בטבע, כשיש ממברנה כזו בין מים מתוקים למים מלוחים, המים המתוקים "שואפים" לעבור דרך הממברנה אל הצד המלוח. למה? כי המים בצד המתוק "פחות עסוקים" בלהיקשר למומסים ויש להם יותר "מקום פנוי" לעבור. תנועה ספונטנית זו של מים מהצד הטהור יותר לריכוזי נקראת **אוסמוזה**.</p>
    <p>ככל שהמים מלוחים יותר (ריכוז המומסים גבוה יותר), כך "כוח המשיכה" האוסמוטי גדול יותר. כדי לעצור את תנועת המים הזו לחלוטין, צריך להפעיל לחץ *נגדי* על הצד המלוח. הלחץ המינימלי הנדרש כדי לעצור את האוסמוזה נקרא **הלחץ האוסמוטי**. במי ים טיפוסיים, לחץ זה שקול לכ-25 אטמוספירות!</p>

    <h2>מהי ממברנה חצי-חדירה (semipermeable membrane)?</h2>
    <p>כמו מסננת על-אטומית! ממברנה חצי-חדירה היא חומר מיוחד (לרוב פולימר סינתטי בהתפלה) בעל נקבוביות זעירות, בגודל של ננומטרים בודדים. נקבוביות אלו מתוכננות בקפידה כדי לאפשר למולקולות מים (H₂O) לעבור יחסית בקלות, בעוד שהן חוסמות ביעילות מעבר של רוב יוני המלחים (כמו נתרן וכלוריד), חיידקים, וירוסים ומומסים אחרים. הן הלב הפועם של תהליך ההתפלה באוסמוזה הפוכה.</p>

    <h2>כיצד תהליך האוסמוזה ההפוכה שונה מאוסמוזה טבעית?</h2>
    <p>כאן טמון הקסם ההנדסי! במקום לתת למים לזרום *מה*מתוק *אל*המלוח (אוסמוזה טבעית), אנחנו מכריחים אותם לזרום בכיוון ההפוך: *מה*מלוח *אל*המתוק. איך? על ידי הפעלת **לחץ חיצוני** על המים המלוחים. הלחץ הזה חייב להיות גדול יותר מהלחץ האוסמוטי הטבעי. כאשר הלחץ החיצוני "גובר" על הלחץ האוסמוטי, הוא דוחף בכוח את מולקולות המים דרך הממברנה, ומשאיר את המלחים והמומסים האחרים מאחור. זהו תהליך **אוסמוזה הפוכה**.</p>

    <h2>מה תפקיד הלחץ החיצוני בתהליך ההתפלה?</h2>
    <p>הלחץ החיצוני הוא הכוח המניע של ההתפלה! הוא כמו שריר עוצמתי שמתגבר על הכוח הטבעי של האוסמוזה. כדי לדחוף מים מלוחים דרך הממברנה ולהפריד אותם מהמלחים, הלחץ המופעל על מי הים חייב להיות **גבוה משמעותית** מהלחץ האוסמוטי של מי הים (כ-25 אטמוספירות, כלומר מאות רבות של מטרים עמוד מים!). ככל שהלחץ המופעל גבוה יותר (עד גבול מסוים), כך קצב ייצור המים הטהורים (הפרמייט) יהיה גבוה יותר ויעילות ההפרדה תשתפר.</p>

    <h2>מרכיבים עיקריים במערכת התפלה באוסמוזה הפוכה</h2>
    <p>מפעל התפלה מודרני הוא פלא הנדסי. הנה המרכיבים המרכזיים:</p>
    <ul>
        <li><strong>צריבת המים וטיפול מקדים:</strong> שלבים ראשוניים קריטיים בהם מסננים את מי הים גס, מסירים חול, אצות וחלקיקים גדולים, ומוסיפים כימיקלים למניעת גדילת מיקרואורגניזמים ומשקעים מזיקים. זה חיוני להגנה על הממברנות העדינות.</li>
        <li><strong>משאבות לחץ גבוה:</strong> אלו הן "השרירים" של המפעל, המספקות את האנרגיה העצומה הנדרשת להעלות את לחץ מי הים המטופלים מקדימה ללחץ גבוה מאוד (בדרך כלל 60-80 אטמוספירות ולעיתים אף יותר), הנדרש לתהליך האוסמוזה ההפוכה.</li>
        <li><strong>מכלי לחץ (Pressure Vessels) וממברנות:</strong> זהו לב המערכת. מכלי הלחץ הם צינורות גליליים ארוכים ועמידים בלחץ קיצוני. בתוכם מסודרות הממברנות הגליליות זו אחר זו (לרוב 6-8 ממברנות במכל). המים המלוחים נדחסים לתוך המכלים בלחץ גבוה, והמים הטהורים עוברים דרך הממברנות וזורמים במרכז המכל, בעוד המלחים ומי ההפרשה (הבריין) יוצאים מהקצה השני.</li>
        <li><strong>מערכות שחזור אנרגיה (Energy Recovery Devices):</strong> טכנולוגיה גאונית המאפשרת "לשחזר" חלק ניכר מהאנרגיה המושקעת ביצירת הלחץ הגבוה במי ההפרשה המלוחים (הבריין) ולהשתמש בה לחימום מי הים הנכנסים, ובכך לחסוך משמעותית בצריכת החשמל - מרכיב עלות משמעותי בהתפלה.</li>
        <li><strong>טיפול לאחר (Post-Treatment):</strong> המים הטהורים שיוצאים מהממברנות הם כמעט טהורים לחלוטין (אפילו יותר מדי!). כדי להפוך אותם לראויים לשתייה, מוסיפים להם בחזרה מינרלים חיוניים (כמו סידן) ומבצעים התאמות אחרונות באיכות המים לפי תקנים מחמירים.</li>
    </ul>

    <h2>שימושים נפוצים של טכנולוגיית אוסמוזה הפוכה</h2>
    <p>האוסמוזה ההפוכה היא גיבורה סמויה בחיינו. היא מאפשרת לנו:</p>
    <ul>
        <li><strong>להתפיל מי ים ומים מליחים:</strong> זהו הפתרון המוביל בעולם למחסור במים, המאפשר למיליוני אנשים גישה למים מתוקים, במיוחד באזורים צחיחים כמו ישראל.</li>
        <li><strong>לייצר מים באיכות גבוהה לתעשייה:</strong> מפעלים רבים (אלקטרוניקה, תרופות, מזון) זקוקים למים טהורים במיוחד, שהאוסמוזה ההפוכה מספקת.</li>
        <li><strong>לטהר מי שתייה ביתיים ומסחריים:</strong> מסנני מים רבים בבתים ובמשרדים משתמשים בטכנולוגיה זו לשיפור טעם ואיכות המים.</li>
        <li><strong>לטפל בשפכים תעשייתיים:</strong> מאפשר למפעלים לשחזר מים מתוך השפכים ולהפחית את כמות המים המזוהמים המוזרמים החוצה.</li>
        <li><strong>להפיק מים אולטרה-טהורים למעבדות ומחקר:</strong> מים ברמת טוהר גבוהה ביותר הנדרשת בתהליכים מדעיים עדינים.</li>
    </ul>
</div>


<script>
    document.addEventListener('DOMContentLoaded', () => {
        const pressureSlider = document.getElementById('pressure-slider');
        const pressureValueSpan = document.getElementById('pressure-value');
        const pressureStatusDiv = document.getElementById('pressure-status');
        const waterLeft = document.getElementById('water-left');
        const waterRight = document.getElementById('water-right');
        const moleculesLeftContainer = document.getElementById('water-molecules-left-container');
        const moleculesRightContainer = document.getElementById('water-molecules-right-container');
        const ionsLeftContainer = document.getElementById('salt-ions-container');
        const explanationButton = document.getElementById('explanation-button');
        const explanationContent = document.getElementById('explanation-content');
        const pressurePiston = document.getElementById('pressure-piston');
        const flowArrowRL = document.getElementById('flow-arrow-r-l');
        const flowArrowLR = document.getElementById('flow-arrow-l-r');


        const TANK_HEIGHT_PX = 350; // Match CSS #tank height
        const INITIAL_WATER_PERCENT = 50; // %
        const OSMOTIC_PRESSURE_THRESHOLD = 50; // Slider percentage representing osmotic pressure
        const MAX_PRESSURE_SLIDER = 120; // Max value of the slider

        // Particle Simulation Settings
        const NUM_WATER_MOLECULES = 100; // Total water molecules initially
        const NUM_SALT_IONS = 50;      // Total salt ions initially
        const PARTICLE_SIZE = 10;      // px
        const PARTICLE_SPEED = 0.2;    // px per frame (base speed)
        const OSMOSIS_BIAS = 0.01;     // Chance multiplier for R->L crossing in osmosis
        const REVERSE_OSMOSIS_BIAS = 0.03; // Chance multiplier for L->R crossing in reverse osmosis
        const ION_BLOCK_CHANCE = 0.95;   // Chance an ion is blocked at the membrane

        let waterMolecules = [];
        let saltIons = [];
        let animationFrameId = null;

        // Function to get current water heights in pixels
        function getWaterHeightsPx() {
            const leftHeightPx = waterLeft.offsetHeight;
            const rightHeightPx = waterRight.offsetHeight;
            return { left: leftHeightPx, right: rightHeightPx };
        }

        // Create particles and position them randomly within the initial water levels
        function createParticles() {
             const { left: initialLeftPx, right: initialRightPx } = getWaterHeightsPx();

             // Create Water Molecules (initially split between both sides)
             const waterPerSide = NUM_WATER_MOLECULES / 2;
             for (let i = 0; i < waterPerSide; i++) {
                 // Left Side Water (with salt)
                 const molL = document.createElement('div');
                 molL.classList.add('molecule');
                 // Position within the water on the left
                 molL.style.left = `${Math.random() * 90 + 5}%`;
                 molL.style.bottom = `${Math.random() * (initialLeftPx / TANK_HEIGHT_PX * 100 - (PARTICLE_SIZE/TANK_HEIGHT_PX*100)) + (PARTICLE_SIZE/TANK_HEIGHT_PX*100)/2}%`;
                 moleculesLeftContainer.appendChild(molL);
                 waterMolecules.push({ element: molL, side: 'left', type: 'water' });

                 // Right Side Water (pure)
                 const molR = document.createElement('div');
                 molR.classList.add('molecule');
                 // Position within the water on the right
                 molR.style.left = `${Math.random() * 90 + 5}%`;
                 molR.style.bottom = `${Math.random() * (initialRightPx / TANK_HEIGHT_PX * 100 - (PARTICLE_SIZE/TANK_HEIGHT_PX*100)) + (PARTICLE_SIZE/TANK_HEIGHT_PX*100)/2}%`;
                 moleculesRightContainer.appendChild(molR);
                 waterMolecules.push({ element: molR, side: 'right', type: 'water' });
             }

             // Create Salt Ions (only on the left side)
             for (let i = 0; i < NUM_SALT_IONS; i++) {
                 const ion = document.createElement('div');
                 ion.classList.add('ion');
                  // Position within the water on the left
                 ion.style.left = `${Math.random() * 90 + 5}%`;
                 ion.style.bottom = `${Math.random() * (initialLeftPx / TANK_HEIGHT_PX * 100 - (PARTICLE_SIZE/TANK_HEIGHT_PX*100)) + (PARTICLE_SIZE/TANK_HEIGHT_PX*100)/2}%`;
                 ionsLeftContainer.appendChild(ion);
                 saltIons.push({ element: ion, side: 'left', type: 'salt' });
             }
        }

        // Update particle positions and simulate flow attempts
        function updateParticles(currentPressure) {
            const { left: currentLeftPx, right: currentRightPx } = getWaterHeightsPx();
            const tankWidthPx = document.getElementById('tank').offsetWidth;
            const membraneLeftPx = tankWidthPx / 2 - (document.getElementById('membrane').offsetWidth / 2);
            const membraneRightPx = tankWidthPx / 2 + (document.getElementById('membrane').offsetWidth / 2);


            const pressureDiff = currentPressure - OSMOTIC_PRESSURE_THRESHOLD; // Negative means osmosis, positive means reverse osmosis

            let netFlow = 0; // -1 for R->L, 1 for L->R, 0 for none

            // Determine net flow direction for visual arrows
            if (pressureDiff < -5) { // Significant osmosis pressure
                netFlow = -1;
            } else if (pressureDiff > 5) { // Significant reverse osmosis pressure
                netFlow = 1;
            }

             // Update flow arrows visibility
            flowArrowRL.style.opacity = netFlow === -1 ? 1 : 0;
            flowArrowLR.style.opacity = netFlow === 1 ? 1 : 0;


            // Simulate particle movement attempts and crossings
            const allParticles = waterMolecules.concat(saltIons);

            allParticles.forEach(p => {
                const currentBottomPercent = parseFloat(p.element.style.bottom);
                const currentLeftPercent = parseFloat(p.element.style.left);

                // Convert percentage positions to pixels for calculations
                const sideContainer = p.side === 'left' ? waterLeft : waterRight;
                const currentBottomPx = currentBottomPercent / 100 * sideContainer.offsetHeight;
                const currentLeftPxAbs = (p.side === 'left' ? 0 : tankWidthPx / 2 + document.getElementById('membrane').offsetWidth / 2) + currentLeftPercent / 100 * (tankWidthPx/2 - document.getElementById('membrane').offsetWidth/2) ;


                // Jiggle/random movement within water level
                const wiggleAmount = PARTICLE_SPEED * 0.5;
                 const newLeftPercent = Math.max(0, Math.min(100, currentLeftPercent + (Math.random() - 0.5) * wiggleAmount / (tankWidthPx/2 - document.getElementById('membrane').offsetWidth/2) * 100));
                 const maxBottomPx = p.side === 'left' ? currentLeftPx : currentRightPx;
                 const newBottomPercent = Math.max((PARTICLE_SIZE/TANK_HEIGHT_PX*100)/2, Math.min(maxBottomPx / TANK_HEIGHT_PX * 100 - (PARTICLE_SIZE/TANK_HEIGHT_PX*100)/2, currentBottomPercent + (Math.random() - 0.5) * wiggleAmount / TANK_HEIGHT_PX * 100));

                p.element.style.left = `${newLeftPercent}%`;
                p.element.style.bottom = `${newBottomPercent}%`; // Position relative to water element's bottom=0

                // --- Attempt Crossing ---
                // Define membrane boundary based on element positions
                const membraneLeftBoundary = document.getElementById('left-side').offsetWidth - (document.getElementById('membrane').offsetWidth / 2);
                const membraneRightBoundary = document.getElementById('left-side').offsetWidth + (document.getElementById('membrane').offsetWidth / 2);

                // Get absolute position for crossing logic
                const particleAbsLeft = p.element.getBoundingClientRect().left + PARTICLE_SIZE / 2; // Center of particle
                const membraneAbsLeft = document.getElementById('membrane').getBoundingClientRect().left;
                const membraneAbsRight = document.getElementById('membrane').getBoundingClientRect().right;
                const particleAbsBottom = p.element.getBoundingClientRect().bottom; // Bottom edge of particle


                // Check if particle is near membrane and within water level on its side
                const particleIsInWater = p.side === 'left'
                    ? particleAbsBottom > waterLeft.getBoundingClientRect().top
                    : particleAbsBottom > waterRight.getBoundingClientRect().top;

                 if (!particleIsInWater) return; // Don't try to cross if floating above water

                // Attempt crossing based on current state (Osmosis or Reverse Osmosis)
                let shouldAttemptCross = false;
                let attemptDirection = 0; // -1: R->L, 1: L->R

                if (p.side === 'right' && particleAbsLeft < membraneAbsRight && pressureDiff < -5) { // Near membrane on Right, Osmosis state
                     // Water molecules try to move R->L
                     shouldAttemptCross = (Math.random() < OSMOSIS_BIAS * Math.abs(pressureDiff) * 0.1); // Chance increases with osmosis pressure
                     attemptDirection = -1;
                } else if (p.side === 'left' && particleAbsLeft > membraneAbsLeft && pressureDiff > 5) { // Near membrane on Left, Reverse Osmosis state
                     // Water molecules try to move L->R. Salt ions also try.
                     shouldAttemptCross = (Math.random() < REVERSE_OSMOSIS_BIAS * pressureDiff * 0.1); // Chance increases with reverse osmosis pressure
                     attemptDirection = 1;
                }

                if (shouldAttemptCross) {
                     // Simulate moving towards the membrane center initially
                     let targetAbsLeft = attemptDirection === -1 ? membraneAbsLeft + PARTICLE_SIZE : membraneAbsRight - PARTICLE_SIZE;
                     // This direct manipulation of style.left based on absolute position is complex.
                     // A simpler approach is to flag particles for crossing and animate them separately.

                     // Let's simplify: when a particle is near the membrane and attempts to cross,
                     // if successful, immediately teleport it to the other side in a random valid water position.
                     // This is less realistic but visually shows net flow and is performant.

                     let crossSuccessful = false;
                     if (p.type === 'water') {
                         crossSuccessful = true; // Water can always cross if the pressure difference allows attempts
                     } else if (p.type === 'salt') {
                         // Salt ions only attempt from the left side (Reverse Osmosis) and are usually blocked
                         if (attemptDirection === 1) { // Salt ions only try L->R
                             crossSuccessful = Math.random() > ION_BLOCK_CHANCE; // High chance of being blocked
                         }
                     }

                     if (crossSuccessful) {
                         // Move particle to the other side
                         if (attemptDirection === 1 && p.side === 'left') { // Move L -> R
                              p.side = 'right';
                              moleculesRightContainer.appendChild(p.element);
                              // Random position within new side's water level
                              const newMaxBottomPx = waterRight.offsetHeight;
                              p.element.style.left = `${Math.random() * 90 + 5}%`;
                              p.element.style.bottom = `${Math.random() * (newMaxBottomPx / TANK_HEIGHT_PX * 100 - (PARTICLE_SIZE/TANK_HEIGHT_PX*100)) + (PARTICLE_SIZE/TANK_HEIGHT_PX*100)/2}%`;
                         } else if (attemptDirection === -1 && p.side === 'right') { // Move R -> L
                              p.side = 'left';
                              moleculesLeftContainer.appendChild(p.element);
                               // Random position within new side's water level
                              const newMaxBottomPx = waterLeft.offsetHeight;
                              p.element.style.left = `${Math.random() * 90 + 5}%`;
                              p.element.style.bottom = `${Math.random() * (newMaxBottomPx / TANK_HEIGHT_PX * 100 - (PARTICLE_SIZE/TANK_HEIGHT_PX*100)) + (PARTICLE_SIZE/TANK_HEIGHT_PX*100)/2}%`;
                         }
                         // else: salt ion trying R->L (shouldn't happen), or water trying from wrong side in current state
                     } else if (p.type === 'salt' && attemptDirection === 1) {
                          // Salt ion blocked - maybe small animation effect?
                           p.element.style.transform = `translateX(${attemptDirection === 1 ? -5 : 5}px)`; // Push back slightly
                           setTimeout(() => p.element.style.transform = 'translateX(0)', 200); // Reset position after brief push back
                     }
                }
            }); // End forEach particle

             // Adjust water levels based on particle counts (simplified)
             const waterLeftCount = waterMolecules.filter(p => p.side === 'left').length;
             const waterRightCount = waterMolecules.filter(p => p.side === 'right').length;
             const totalWater = waterLeftCount + waterRightCount;

             if (totalWater > 0) { // Prevent division by zero
                 const targetLeftPercent = (waterLeftCount / totalWater) * (NUM_WATER_MOLECULES / (NUM_WATER_MOLECULES + NUM_SALT_IONS)) * 100 * (TANK_HEIGHT_PX / (TANK_HEIGHT_PX)); // Scale to total available height ignoring ions for level calculation
                 const targetRightPercent = (waterRightCount / totalWater) * (NUM_WATER_MOLECULES / (NUM_WATER_MOLECULES + NUM_SALT_IONS)) * 100 * (TANK_HEIGHT_PX / (TANK_HEIGHT_PX));

                 // Smoothly transition levels towards target based on particle distribution
                 const currentLeftPercent = parseFloat(waterLeft.style.height);
                 const currentRightPercent = parseFloat(waterRight.style.height);

                 const levelAdjustSpeed = 0.1; // Adjust this for faster/slower level changes
                 waterLeft.style.height = `${currentLeftPercent + (targetLeftPercent - currentLeftPercent) * levelAdjustSpeed}%`;
                 waterRight.style.height = `${currentRightPercent + (targetRightPercent - currentRightPercent) * levelAdjustSpeed}%`;
             }


        }


        // Update piston position based on pressure slider value
        function updatePiston(pressurePercent) {
            const tankTopAbs = document.getElementById('tank').getBoundingClientRect().top;
            const leftSideAbs = document.getElementById('left-side').getBoundingClientRect().top;
             const pistonHeadHeight = 25; // px, match CSS
             const pistonRodBaseHeight = 40; // px, match CSS initial
             const maxPistonTravel = TANK_HEIGHT_PX - pistonHeadHeight; // How far down the piston head can go

            if (pressurePercent === 0) {
                 // Piston is off-screen at the top
                pressurePiston.style.transform = `translateY(-${pistonHeadHeight + pistonRodBaseHeight}px)`;
            } else {
                 // Calculate how far down the piston should be
                 // Pressure 0% should be at the top edge of the tank
                 // Pressure 100% should be pressing on the water surface (or near bottom)
                 // Let's make 0% pressure translateY(-pistonHeadHeight), and 100% pressure push down by maxTravel
                 const pistonOffset = (pressurePercent / MAX_PRESSURE_SLIDER) * maxPistonTravel; // Scale travel by slider max value
                 // Position the top of the piston head at the calculated offset
                 pressurePiston.style.transform = `translateY(${pistonOffset}px)`;

                 // Optional: Scale rod visually with pressure
                 // const rodScale = 1 + (pressurePercent / MAX_PRESSURE_SLIDER) * 0.5; // Rod gets up to 50% longer
                 // pressurePiston.querySelector('.piston-rod').style.height = `${pistonRodBaseHeight * rodScale}px`;

            }
        }

         // Update pressure status text
         function updatePressureStatus(pressurePercent) {
             if (pressurePercent < OSMOTIC_PRESSURE_THRESHOLD - 5) {
                 pressureStatusDiv.textContent = `לחץ מופעל: ${pressurePercent}% - אוסמוזה טבעית מתרחשת (מים עוברים מהטהור למלוח)`;
                 pressureStatusDiv.style.color = '#d32f2f'; // Reddish
             } else if (pressurePercent > OSMOTIC_PRESSURE_THRESHOLD + 5) {
                 pressureStatusDiv.textContent = `לחץ מופעל: ${pressurePercent}% - אוסמוזה הפוכה מתרחשת (מים עוברים מהמלוח לטהור!)`;
                 pressureStatusDiv.style.color = '#388e3c'; // Greenish
             } else {
                 pressureStatusDiv.textContent = `לחץ מופעל: ${pressurePercent}% - שיווי משקל אוסמוטי (אין מעבר מים נטו)`;
                 pressureStatusDiv.style.color = '#fbc02d'; // Yellowish
             }
         }


        // --- Animation Loop ---
         let lastTimestamp = 0;
         const particlesPerFrameRatio = 0.5; // How many particle update cycles per frame (can be < 1 for performance)

         function animateTank(timestamp) {
             if (!lastTimestamp) lastTimestamp = timestamp;
             const deltaTime = timestamp - lastTimestamp; // Time elapsed since last frame
             lastTimestamp = timestamp;

             const currentPressure = parseInt(pressureSlider.value, 10);

             // Update piston and status based on current slider value
             updatePiston(currentPressure);
             updatePressureStatus(currentPressure);


             // Update particles (attempting flow and jiggling)
             // We update particles more frequently than requestAnimationFrame to smooth movement
             // This approach might be too complex with DOM elements. Let's keep it simpler and update particles directly in the loop.
             // It's not a true physics engine, just visual representation.

            // Limit particle updates to improve performance on slower devices
            // Only update a subset of particles or less frequently
             updateParticles(currentPressure); // Update all particles each frame, simplified movement


             // Update water levels based on particle count changes (handled inside updateParticles for simplicity)


             animationFrameId = requestAnimationFrame(animateTank);
         }


        // --- Event Listeners ---
        pressureSlider.addEventListener('input', (event) => {
            const pressure = parseInt(event.target.value, 10);
            pressureValueSpan.textContent = pressure;
            // Animation loop handles the rest
        });

         // Initial piston update based on starting slider value (0)
         updatePiston(parseInt(pressureSlider.value, 10));
         updatePressureStatus(parseInt(pressureSlider.value, 10));


        explanationButton.addEventListener('click', () => {
            const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
            explanationContent.style.display = isHidden ? 'block' : 'none';
            explanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'חשיפת הסבר מעמיק';
        });

        // --- Initial Setup ---
        createParticles(); // Populate initial particles
        animateTank(0); // Start the animation loop

         // Ensure particles are re-positioned if window resizes
         window.addEventListener('resize', () => {
             // Recalculate particle positions based on new water levels (simplified: just re-position)
             // A more robust solution would update transforms/bottom styles based on percentage
             waterMolecules.forEach(p => {
                  const container = p.side === 'left' ? waterLeft : waterRight;
                  const maxBottomPx = container.offsetHeight;
                  // Maintain approximate vertical position within water
                  const currentBottomPercent = parseFloat(p.element.style.bottom);
                  p.element.style.bottom = `${Math.min(currentBottomPercent, maxBottomPx / TANK_HEIGHT_PX * 100 - (PARTICLE_SIZE/TANK_HEIGHT_PX*100)/2)}%`;
             });
             saltIons.forEach(p => {
                  const container = waterLeft;
                  const maxBottomPx = container.offsetHeight;
                   const currentBottomPercent = parseFloat(p.element.style.bottom);
                  p.element.style.bottom = `${Math.min(currentBottomPercent, maxBottomPx / TANK_HEIGHT_PX * 100 - (PARTICLE_SIZE/TANK_HEIGHT_PX*100)/2)}%`;
             });
         });


    });
</script>
```