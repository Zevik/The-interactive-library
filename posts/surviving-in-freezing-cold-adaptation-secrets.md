---
title: "קרב ההישרדות הגדול: איך בעלי חיים מנצחים את הקור הקיצוני?"
english_slug: surviving-in-freezing-cold-adaptation-secrets
category: "מדעי החיים / ביולוגיה"
tags:
  - ביולוגיה
  - אקולוגיה
  - פיזיולוגיה
  - התאמות
  - קור קיצוני
---
<div class="article-intro">
    <h1>קרב ההישרדות הגדול: איך בעלי חיים מנצחים את הקור הקיצוני?</h1>
    <p>דמיינו לעצמכם לחיות באנטארקטיקה, כשהטמפרטורה צונחת עמוק מתחת לאפס והרוח מקפיאה עצמות. איך יצורים כמו פינגווינים או דובי קוטב לא קופאים למוות? זו לא קסם, זו הנדסה ביולוגית מדהימה! גלו בסמולציה האינטראקטיבית הזו כמה מהסודות המדהימים שמאפשרים להם לשרוד בממלכת הקרח.</p>
</div>

<div id="simulation-app">
    <h2>מעבדת הישרדות: סימולציית אובדן חום בגף</h2>
    <p class="simulation-description">שנו את המשתנים כדי לראות איך הם משפיעים על טמפרטורת קצה הגף וקצב אובדן החום.</p>

    <div class="controls-panel">
        <div class="control-group">
            <label for="environment-temp">טמפרטורת סביבה חיצונית (°C):</label>
            <input type="range" id="environment-temp" min="-50" max="10" value="-10" step="1">
            <span id="environment-temp-value">-10°C</span>
        </div>

        <div class="control-group">
            <label for="insulation-type">סוג בידוד:</label>
            <select id="insulation-type">
                <option value="0.03">עור חשוף (מינימלי)</option>
                <option value="0.015">פרווה דקה / נוצות</option>
                <option value="0.008">פרווה עבה / שכבת שומן דקה</option>
                <option value="0.004">שכבת שומן עבה (בלבר)</option>
            </select>
        </div>

        <div class="control-group">
            <label for="insulation-thickness">עובי בידוד (יחסי):</label>
            <input type="range" id="insulation-thickness" min="1" max="10" value="3" step="1">
            <span id="insulation-thickness-value">3</span>
        </div>

        <div class="control-group">
            <label for="blood-flow">זרימת דם לגף (יחסי):</label>
            <input type="range" id="blood-flow" min="1" max="10" value="10" step="1">
            <span id="blood-flow-value">10</span> (רגילה)
        </div>

        <div class="control-group">
            <label for="countercurrent-exchange">מנגנון מחלף חום נגדי:</label>
            <input type="checkbox" id="countercurrent-exchange" checked>
            <label class="checkbox-label" for="countercurrent-exchange">מופעל</label>
        </div>
    </div>

    <div class="simulation-area">
        <div class="limb-model">
            <div class="core-body">גוף ליבה (<span id="core-temp">37</span>°C)</div>
            <div class="limb">
                <div class="artery"></div>
                <div class="vein"></div>
                <div class="tissue"></div>
                <div class="frozen-overlay"></div> <!-- Added for frozen effect -->
            </div>
            <div class="extremity">גף קצה (<span id="extremity-temp-display">?</span>°C)</div> <!-- Display label -->
             <div class="heat-loss-indicator">
                <div class="heat-waves"></div> <!-- Added for heat loss animation -->
             </div>
        </div>

        <div class="info-box">
            <h3>תוצאות סימולציה:</h3>
            <p>קצב אובדן חום יחסי: <span id="heat-loss-rate">?</span></p>
            <p>טמפרטורת קצה הגף: <span id="calculated-extremity-temp">?</span>°C</p>
             <p class="freezing-warning" style="display: none;">
                 <strong>⚠️ סכנת קפיאה! ⚠️</strong><br>
                 הרקמה מתקררת מדי!
             </p>
        </div>
    </div>
    <p class="note"><strong>שימו לב:</strong> מודל זה מפשט תהליכים ביולוגיים מורכבים לצורך הדגמה.</p>
</div>

<button id="toggle-explanation">גלו את הסודות: הצג/הסתר הסבר מפורט</button>

<div id="explanation" style="display: none;">
    <h2>שורדים בקור מקפיא: סודות ההתאמה</h2>

    <h3>האתגר המקפיא: למה קור כל כך מסוכן?</h3>
    <p>בעלי חיים בעלי דם חם (יונקים ועופות) פועלים בטמפרטורה פנימית קבועה (בדרך כלל סביב 37°C). כשהסביבה קרה, הגוף מאבד חום במהירות. שמירה על חום פנימי היא קרב מתמיד.</p>
    <h4>הסכנות העיקריות שאורבות בקור:</h4>
    <ul>
        <li><strong>היפותרמיה:</strong> ירידה מסוכנת בטמפרטורת גוף הליבה. תפקוד התאים והאיברים נפגע, ובמקרים קיצוניים זה קטלני.</li>
        <li><strong>קפיאת רקמות (כוויות קור):</strong> היווצרות גבישי קרח בתוך התאים ומחוץ להם. זה הורס את מבנה התא וגורם לנזק בלתי הפיך לרקמה הפגועה.</li>
    </ul>

    <h3>מגנים טבעיים: מנגנוני ההתמודדות הבסיסיים</h3>
    <p>לפני שמגיעים לטריקים הפיזיולוגיים המתוחכמים, יש דרכים פשוטות יחסית לשמור על חום:</p>
    <ul>
        <li>
            <strong>בידוד טבעי:</strong> חומרים שהגוף מייצר או נוצרים באופן טבעי ומקטינים מעבר חום לסביבה הקרה.
            <ul>
                <li>**שכבות שומן (בלבר):** במיוחד אצל יונקים ימיים כמו לווייתנים וכלבי ים. השומן מוליך חום הרבה פחות טוב ממים, ומספק שכבת הגנה מעולה. זו גם מאגר אנרגיה חשוב.</li>
                <li>**פרווה ונוצות:** ה"סוד" פה הוא לא השערות/נוצות עצמן, אלא האוויר שהן לוכדות. אוויר הוא מוליך חום גרוע. ככל שהשכבה צפופה ועבה יותר, יותר אוויר נלכד, והבידוד יעיל יותר.</li>
            </ul>
        </li>
        <li>
            <strong>התנהגות חכמה:</strong> פעולות יזומות שמפחיתות חשיפה לקור.
            <ul>
                <li><strong>התקבצות/הצטופפות:</strong> כמו פינגווינים במושבה ענקית או חיות עדר. התכרבלות יחד מקטינה את שטח הפנים החשוף לקור ומאפשרת לבעלי החיים לחלוק חום גוף.</li>
                <li><strong>חיפוש מחסה:</strong> כניסה למאורות, נקיקים, מערות או סתם עמידה בצלע הר - כל דבר שמספק הגנה מרוח, שלג או גשם מקפיא.</li>
            </ul>
        </li>
    </ul>

    <h3>הנדסה ביולוגית מתוחכמת: מנגנונים פיזיולוגיים</h3>
    <p>כדי לשרוד בקור הקיצוני ביותר, נדרשים פתרונות פנימיים:</p>
    <ul>
        <li>
            <strong>מחלף חום נגדי (Countercurrent Heat Exchange): גאונות בוורידים ובעורקים!</strong>
            <ul>
                <li>זהו מנגנון שנראה כמו צינורות מחליפי חום במפעל, רק שזה קורה בתוך הגפיים!</li>
                <li>כלי הדם שמובילים דם חם מהגוף הליבה לכיוון קצה הגף (<strong>עורקים</strong>) עוברים בסמיכות צמודה לכלי הדם שמחזירים דם קר מקצה הגף לכיוון הגוף (<strong>ורידים</strong>).</li>
                <li>**מה קורה?** כשהדם החם מהליבה עובר בעורק בירידה לכף הרגל (למשל), הוא "תורם" את החום שלו לדם הקר שעולה בווריד הסמוך חזרה לגוף. החום עובר מהעורק לווריד לכל אורך הגף.</li>
                <li>**התוצאה המדהימה:** כשהדם מגיע ממש לקצה הגף בעורק, הוא כבר הספיק להתקרר משמעותית (החום עבר לווריד!). כשהדם חוזר בווריד הקר מקצה הגף, הוא מתחמם בהדרגה שוב על ידי הדם החם שזורם בעורק היורד.</li>
                <li>**היתרון העצום:** כמעט שום חום יקר מהליבה לא מגיע עד קצה הגף כדי ללכת לאיבוד לסביבה הקרה. קצה הגף נשאר קר יחסית (אבל מעל נקודת הקיפאון!) ודורש פחות אנרגיה לחימום, והדם שחוזר לגוף הליבה כבר חם, מונע את קירור הגוף המרכזי.</li>
            </ul>
        </li>
        <li>
            <strong>שליטה מדויקת על זרימת הדם (ואזוקונסטריקציה/ואזודילציה):</strong>
            <ul>
                <li>בקור, הגוף יכול להקטין את זרימת הדם לכלי דם קטנים קרוב לפני העור (<strong>ואזוקונסטריקציה</strong> - כיווץ כלי דם). זה מקטין את שטח הפנים המאבד חום ומגן על טמפרטורת הליבה.</li>
                <li>אבל... זה בא במחיר: אם זרימת הדם לקצוות (אצבעות, אוזניים, זנב, כפות רגליים) מופחתת מדי, הם עלולים לקפוא. לכן, בעלי חיים רבים מפעילים שליטה עדינה, לפעמים עם פולסים של זרימת דם כדי למנוע נזק, תוך שמירה על הליבה.</li>
            </ul>
        </li>
    </ul>

    <h3>אלופים בממלכת הקרח: דוגמאות מהטבע</h3>
    <ul>
        <li>
            <strong>פינגווינים:</strong> הרגליים והכפות שלהם חשופות לקרח. איך? הן שומרות על טמפרטורה נמוכה בזכות מנגנון מחלף חום נגדי סופר-יעיל בכלי הדם. גופם הראשי מבודד מדהים בזכות שכבת שומן עבה ונוצות אטומות למים שכולאות אוויר. הם גם מצטופפים!
        </li>
        <li>
            <strong>דובי קוטב:</strong> אלופי הבידוד. יש להם פרווה כפולה וצפופה שלא רק מבודדת אוויר אלא גם דוחה מים. מתחת לפרווה - שכבת שומן עצומה. כפות הרגליים מבודדות בפרווה חלקית וייתכן שגם בהן יש מנגנון מחלף חום.
        </li>
        <li>
            <strong>יונקים ימיים אחרים (כלבי ים, ניבתנים):</strong> חיים במים קפואים, שם אובדן החום מהיר פי 25 מאשר באוויר! הבלבר (שומן עבה) הוא ההגנה העיקרית שלהם. בגפיים (סנפירים וזנב) ובאזורים חשופים אחרים (ראש) הם משתמשים במחלפי חום נגדיים ושולטים בזרימת הדם.
        </li>
    </ul>
    <p>כפי שראיתם בסימולציה וקראתם בהסבר, ההישרדות בקור קיצוני היא הצגה מרתקת של אבולוציה ויכולות פיזיולוגיות מדהימות!</p>
</div>

<style>
    /* General Styles */
    :root {
        --color-primary: #007bff;
        --color-secondary: #6c757d;
        --color-success: #28a745;
        --color-danger: #dc3545;
        --color-warning: #ffc107;
        --color-info: #17a2b8;
        --color-light: #f8f9fa;
        --color-dark: #343a40;
        --color-blue-cold: #00aaff;
        --color-red-hot: #ff4500;
        --color-tissue-cold: #aaddff;
        --color-tissue-hot: #ffaaaa;
        --color-frost: rgba(220, 230, 255, 0.8);

        --border-radius: 8px;
        --box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        --transition-speed: 0.3s ease-in-out;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--color-dark);
        background-color: var(--color-light);
        margin: 0;
        padding: 20px;
        direction: rtl; /* Ensure RTL */
        text-align: right; /* Align text */
    }

    .article-intro h1 {
        color: var(--color-dark);
        text-align: center;
        margin-bottom: 15px;
    }
     .article-intro p {
         max-width: 800px;
         margin: 0 auto 30px auto;
         text-align: center;
         font-size: 1.1em;
         color: #555;
     }


    #simulation-app {
        max-width: 800px;
        margin: 20px auto;
        padding: 30px;
        border: 1px solid #ccc;
        border-radius: var(--border-radius);
        background-color: #ffffff; /* White background for app */
        box-shadow: var(--box-shadow);
        position: relative; /* Needed for absolute positioning inside */
    }

    #simulation-app h2 {
        text-align: center;
        color: var(--color-primary);
        margin-bottom: 10px;
    }
     .simulation-description {
         text-align: center;
         color: #555;
         margin-bottom: 25px;
         font-size: 0.95em;
     }


    .controls-panel {
        margin-bottom: 30px;
        padding: 20px;
        border: 1px solid #eee;
        border-radius: var(--border-radius);
        background-color: #fefefe; /* Lighter background for controls */
         box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }

    .control-group {
         margin-bottom: 15px;
         display: flex;
         align-items: center;
         flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .control-group label {
        display: inline-block;
        font-weight: bold;
        width: 200px; /* Increased width for labels */
        text-align: right; /* Align labels right within group */
        padding-left: 10px; /* Space between label and control */
        box-sizing: border-box;
    }

    .control-group input[type="range"],
    .control-group select {
        flex-grow: 1; /* Take remaining space */
        margin-right: 10px; /* Space after control */
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 4px;
        background-color: white;
        -webkit-appearance: none; /* Remove default styles */
        appearance: none;
        height: 30px; /* Consistent height */
        cursor: pointer;
    }
      .control-group input[type="range"]::-webkit-slider-thumb {
           -webkit-appearance: none;
           appearance: none;
           width: 20px;
           height: 20px;
           background: var(--color-primary);
           cursor: pointer;
           border-radius: 50%;
           margin-top: -5px; /* Center vertically */
           box-shadow: 0 0 2px rgba(0,0,0,0.2);
      }
      .control-group input[type="range"]::-moz-range-thumb {
           width: 20px;
           height: 20px;
           background: var(--color-primary);
           cursor: pointer;
           border-radius: 50%;
           box-shadow: 0 0 2px rgba(0,0,0,0.2);
      }

     .control-group select {
         height: 38px; /* Match input height */
     }


     .control-group input[type="checkbox"] {
        margin-left: 8px; /* Space between checkbox and label */
         width: 18px;
         height: 18px;
         vertical-align: middle;
         cursor: pointer;
     }
      .control-group .checkbox-label {
           width: auto; /* Auto width for checkbox label */
           font-weight: normal;
           text-align: right;
           cursor: pointer;
           padding-left: 0;
      }


     .control-group span {
         display: inline-block;
         min-width: 50px; /* Ensure space for value */
         text-align: left; /* Align values left */
         font-weight: bold;
         color: #555;
     }


    .simulation-area {
        display: flex;
        align-items: flex-start;
        gap: 30px; /* Increased gap */
        margin-top: 30px;
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .limb-model {
        flex: 1 1 250px; /* Allow shrinking/growing, base width */
        display: flex;
        flex-direction: column;
        align-items: center;
        border: 1px solid #ddd;
        padding: 20px 10px; /* More vertical padding */
        border-radius: var(--border-radius);
        background-color: #fefefe;
        position: relative;
        box-shadow: var(--box-shadow);
        min-width: 200px; /* Minimum width */
    }

    .core-body {
        background-color: #ff6347; /* Warm Red */
        color: white;
        padding: 8px 15px;
        border-radius: 20px; /* Pill shape */
        margin-bottom: 20px; /* More space */
        font-size: 1em;
        font-weight: bold;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    .limb {
        width: 100px; /* Wider limb model */
        height: 300px; /* Taller limb model */
        position: relative;
        overflow: hidden;
        border-radius: 15px; /* More rounded */
        background-color: transparent; /* Background handled by tissue */
        border: 1px solid #ccc; /* Outline for the limb */
         box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
    }

     .tissue {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         transition: background var(--transition-speed); /* Smooth gradient transition */
     }

    .frozen-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: var(--color-frost);
        opacity: 0;
        transition: opacity var(--transition-speed);
        pointer-events: none; /* Allow clicking through */
        z-index: 2; /* Above tissue, below vessels */
    }

     .limb-model.is-frozen .frozen-overlay {
         opacity: 1;
     }


    .artery, .vein {
        position: absolute;
        width: 10px; /* Wider blood vessels */
        top: 5%; /* Start slightly down */
        height: 90%; /* Cover most of the limb height */
        border-radius: 5px;
        z-index: 3; /* Ensure vessels are above tissue and overlay */
        opacity: 0.9;
        transition: background var(--transition-speed); /* Smooth color transition */
         animation: pulse 1s infinite alternate; /* Base pulse animation */
    }

    .artery {
        right: 15px; /* Position on the right side */
        background: linear-gradient(to bottom, var(--color-red-hot), #ff8800); /* Red to Orange gradient */
         animation-duration: 1s; /* Default pulse speed */
    }

    .vein {
        left: 15px; /* Position on the left side */
         background: linear-gradient(to bottom, var(--color-blue-cold), #8888ff); /* Blue to Light Blue gradient */
          animation-duration: 1s; /* Default pulse speed */
    }

     /* Vessel pulsing animation */
     @keyframes pulse {
         0% { transform: scaleY(1); opacity: 0.9; }
         100% { transform: scaleY(1.03); opacity: 1; }
     }

     /* Adjust pulse speed based on blood flow (conceptually via JS) */
     /* JS will update animation-duration */

     /* When countercurrent is enabled, show temperature exchange gradient */
    .limb-model.countercurrent-enabled .artery {
         /* More complex gradient showing heat exchange */
         background: linear-gradient(to bottom,
             #ff4500 0%, #ff8800 10%, #ffff00 30%,
             #88ff88 50%, #00ff00 70%, #0088ff 90%, #0000ff 100%
         );
         animation-duration: 1.2s; /* Slower pulse for conserved flow */
    }
     .limb-model.countercurrent-enabled .vein {
         /* Reversed gradient showing heat exchange */
         background: linear-gradient(to bottom,
             #0000ff 0%, #0088ff 10%, #00ff00 30%,
             #88ff88 50%, #ffff00 70%, #ff8800 90%, #ff4500 100%
         );
         animation-duration: 1.2s; /* Slower pulse for conserved flow */
     }

     /* Visual cue for high blood flow -> faster pulse */
      .limb-model.high-blood-flow .artery,
      .limb-model.high-blood-flow .vein {
          animation-duration: 0.7s;
      }


    .extremity {
        background-color: var(--color-tissue-cold); /* Default cold color */
         color: var(--color-dark);
        padding: 8px 15px;
        border-radius: 20px; /* Pill shape */
        margin-top: 20px; /* More space */
         font-size: 1em;
         font-weight: bold;
         box-shadow: 0 1px 3px rgba(0,0,0,0.1);
         transition: background-color var(--transition-speed); /* Smooth color transition */
    }

    .info-box {
        flex: 1 1 250px; /* Allow shrinking/growing, base width */
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: var(--border-radius);
        background-color: #fefefe;
        box-shadow: var(--box-shadow);
        align-self: stretch; /* Stretch to match height of limb model */
        min-width: 200px;
    }
    .info-box h3 {
        margin-top: 0;
        color: var(--color-primary);
        text-align: center;
        margin-bottom: 15px;
    }
     .info-box p {
         margin-bottom: 10px;
         font-size: 1em;
     }
     .info-box span {
         font-weight: bold;
         color: var(--color-dark);
     }

     .heat-loss-indicator {
         position: absolute;
         top: 50%;
         left: calc(100% + 15px); /* Position to the right of the limb */
         transform: translateY(-50%);
         width: 50px;
         height: 50px;
         /* background-color: rgba(var(--color-red-hot), 0.2); */
         border-radius: 50%;
         display: flex;
         justify-content: center;
         align-items: center;
         overflow: hidden;
         opacity: 0; /* Hidden by default */
         transition: opacity var(--transition-speed);
     }

     .heat-waves {
         position: absolute;
         width: 100%;
         height: 100%;
         background: radial-gradient(circle, rgba(255, 69, 0, 0.8) 0%, rgba(255, 69, 0, 0) 70%);
         animation: heat-pulse 2s infinite ease-out;
         opacity: 0; /* Controlled by JS */
     }

     @keyframes heat-pulse {
         0% { transform: scale(0.5); opacity: 0.8; }
         100% { transform: scale(2); opacity: 0; }
     }

     .heat-loss-indicator.high-loss .heat-waves { animation-duration: 1s; }
     .heat-loss-indicator.medium-loss .heat-waves { animation-duration: 1.5s; }
     .heat-loss-indicator.low-loss .heat-waves { animation-duration: 2s; }


     .freezing-warning {
         color: var(--color-danger);
         font-weight: bold;
         text-align: center;
         margin-top: 15px;
         padding: 10px;
         border: 2px dashed var(--color-danger);
         border-radius: 5px;
         background-color: rgba(var(--color-danger, 220, 53, 69), 0.1);
     }


     .note {
         font-size: 0.8em;
         color: #666;
         margin-top: 20px;
         text-align: center;
     }


    #toggle-explanation {
        display: block;
        margin: 30px auto; /* Increased margin */
        padding: 12px 25px; /* Increased padding */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: var(--border-radius);
        background-color: var(--color-primary);
        color: white;
        transition: background-color var(--transition-speed), transform 0.1s ease-in-out;
        box-shadow: var(--box-shadow);
    }

    #toggle-explanation:hover {
        background-color: #0056b3;
        transform: translateY(-1px); /* Subtle lift effect */
    }
     #toggle-explanation:active {
          background-color: #004085;
          transform: translateY(0);
     }


    #explanation {
        margin-top: 20px;
        padding: 30px;
        border: 1px solid #ccc;
        border-radius: var(--border-radius);
        background-color: #ffffff;
        box-shadow: var(--box-shadow);
         direction: rtl;
         text-align: right;
    }

    #explanation h2, #explanation h3 {
        color: var(--color-primary);
        text-align: right;
        margin-bottom: 12px;
    }
     #explanation h3 {
         border-bottom: 1px solid #eee;
         padding-bottom: 5px;
         margin-top: 25px;
     }

    #explanation h4 {
        color: #555;
        margin-top: 18px;
        margin-bottom: 8px;
        text-align: right;
        font-size: 1.05em;
    }

    #explanation ul {
        list-style-type: disc;
        margin-right: 25px; /* Increased indentation */
        margin-bottom: 15px;
        padding: 0; /* Reset default padding */
    }

    #explanation ul ul {
         list-style-type: circle;
         margin-right: 20px;
         margin-top: 5px;
    }

     #explanation li {
         margin-bottom: 8px;
     }

     /* Responsive Adjustments */
     @media (max-width: 600px) {
         body { padding: 10px; }
         #simulation-app { padding: 15px; }
         .controls-panel { padding: 10px; }
         .control-group { flex-direction: column; align-items: flex-end; } /* Stack controls vertically */
         .control-group label { width: 100%; margin-bottom: 5px; text-align: right; padding-left: 0; }
         .control-group input[type="range"], .control-group select { width: 100%; margin-right: 0; }
         .control-group span { min-width: auto; text-align: right; margin-top: 5px; }
         .simulation-area { flex-direction: column; align-items: center; gap: 20px; }
         .limb-model, .info-box { width: 100%; min-width: auto; flex-basis: auto; }
         .limb { width: 80px; height: 250px; } /* Adjust limb size */
         .artery, .vein { right: 10px; left: 10px; width: 8px; }
         .heat-loss-indicator { top: auto; left: auto; bottom: -40px; right: 50%; transform: translateX(50%); } /* Reposition on small screens */
         #toggle-explanation { width: 100%; padding: 10px; box-sizing: border-box; }
     }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // --- Controls ---
        const envTempControl = document.getElementById('environment-temp');
        const envTempValue = document.getElementById('environment-temp-value');
        const insulationTypeControl = document.getElementById('insulation-type');
        const insulationThicknessControl = document.getElementById('insulation-thickness');
        const insulationThicknessValue = document.getElementById('insulation-thickness-value');
        const bloodFlowControl = document.getElementById('blood-flow');
        const bloodFlowValue = document.getElementById('blood-flow-value');
        const countercurrentControl = document.getElementById('countercurrent-exchange');

        // --- Display Elements ---
        const coreTempSpan = document.getElementById('core-temp'); // Assuming core temp is fixed for this simulation
        const extremityTempDisplaySpan = document.getElementById('extremity-temp-display'); // Label part
        const calculatedExtremityTempSpan = document.getElementById('calculated-extremity-temp'); // Value in info box

        const heatLossRateSpan = document.getElementById('heat-loss-rate');
        const limbTissue = document.querySelector('.limb .tissue');
        const limbModel = document.querySelector('.limb-model'); // Parent for class changes
        const arteryVisual = document.querySelector('.limb .artery');
        const veinVisual = document.querySelector('.limb .vein');
        const frozenOverlay = document.querySelector('.limb .frozen-overlay');
        const freezingWarning = document.querySelector('.freezing-warning');
        const heatLossIndicator = document.querySelector('.heat-loss-indicator');
        const heatWaves = document.querySelector('.heat-waves');


        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');

        // --- Constants ---
        const coreBodyTemp = 37; // °C
        const freezingPoint = -1.8; // Approximate freezing point of tissue °C

        // --- Helper Function: Map Temperature to Color ---
        function tempToColor(temp) {
            // Using HSL for a smoother, more intuitive gradient
            // Hue: 240 (Blue) for cold, 0 (Red) for hot
            // Saturation: 100%
            // Lightness: Varies

            const minTemp = -10; // Hottest blue
            const maxTemp = 35; // Coldest red

            if (temp <= minTemp) return 'hsl(240, 100%, 40%)'; // Deep Blue
            if (temp >= maxTemp) return 'hsl(0, 100%, 50%)'; // Bright Red

            // Linear interpolation for Hue (240 to 0) and Lightness
            const hue = 240 - (temp - minTemp) / (maxTemp - minTemp) * 240;
            // Lightness can vary to make it more visually striking - e.g., lighter in the middle temps (greens/yellows)
             let lightness;
             const normalizedTemp = (temp - minTemp) / (maxTemp - minTemp); // 0 to 1
             if (normalizedTemp < 0.5) { // Blue to Greenish-Yellow
                 lightness = 40 + normalizedTemp * 40; // From 40% to 80%
             } else { // Greenish-Yellow to Red
                 lightness = 80 - (normalizedTemp - 0.5) * 60; // From 80% to 20%
             }


            return `hsl(${hue}, 100%, ${lightness}%)`;
        }


        // --- Simulation Logic ---
        function updateSimulation() {
            const envTemp = parseFloat(envTempControl.value);
            const insulationResistancePerUnit = parseFloat(insulationTypeControl.value); // Lower value = better insulation
            const insulationThicknessFactor = parseFloat(insulationThicknessControl.value); // Higher value = more thickness/better insulation
            const bloodFlowFactor = parseFloat(bloodFlowControl.value) / 10; // Scale 1-10 to 0.1-1
            const countercurrentEnabled = countercurrentControl.checked;

            // Update control value displays
            envTempValue.textContent = envTemp + '°C';
            insulationThicknessValue.textContent = insulationThicknessFactor;
            bloodFlowValue.textContent = parseFloat(bloodFlowControl.value);

            // --- Simplified Physics Model ---
            // Thermal Resistance (simplified): Higher value means less heat loss.
            // Base resistance from insulation: R_insulation = (1 / InsulationMaterialResistance) * InsulationThicknessFactor
            // A higher 'value' in select means lower resistance. Let's use 1 / value directly for simplicity.
            const insulationResistance = (1 / insulationResistancePerUnit) * insulationThicknessFactor * 5; // Adjusted scaling

            // Heat loss is complex. Let's model extremity temperature based on influences:
            // 1. Environment temperature (pulls it down)
            // 2. Core body temperature (via blood flow, pulls it up)
            // 3. Insulation (slows down heat loss to env)
            // 4. Countercurrent exchange (reduces heat lost via blood flow)

            let effectiveBloodTempReachingExtremity;
            let heatReturnedViaBlood;

            if (countercurrentEnabled) {
                 // With CC, blood arriving is pre-cooled, returning blood is pre-warmed.
                 // Assume high efficiency (e.g., 90% of the temp difference is exchanged along the vessel length).
                 const ccEfficiency = 0.9;
                 effectiveBloodTempReachingExtremity = envTemp + (coreBodyTemp - envTemp) * (1 - ccEfficiency);
                 // Heat returned is high, so net heat loss via blood is low.
                 heatReturnedViaBlood = (coreBodyTemp - effectiveBloodTempReachingExtremity) * ccEfficiency; // Approx heat recovered
            } else {
                 // Without CC, warm blood (core temp) reaches extremity, returns cold (near extremity temp).
                 effectiveBloodTempReachingExtremity = coreBodyTemp;
                 heatReturnedViaBlood = 0; // No heat recovered on return trip (in this simple model)
            }

            // Extremity temperature is a balance point.
            // It's influenced by environment, insulation, and blood flow bringing heat.
            // A simplified balance equation: ExtremityTemp = EnvTemp + (HeatInput - HeatLoss) * SomeFactor
            // HeatInput is from blood flow: related to (effectiveBloodTemp - EnvTemp) * bloodFlowFactor
            // HeatLoss to environment: related to (ExtremityTemp - EnvTemp) / insulationResistance

            // Let's simplify: Extremity Temp is a weighted average of EnvTemp and EffectiveBloodTemp,
            // influenced by insulation and blood flow.
            // Higher blood flow brings extremity temp closer to effectiveBloodTemp.
            // Higher insulation keeps extremity temp further from EnvTemp (relative to core).

             let extremityTemp;
             if (insulationResistance === 0) insulationResistance = 0.001; // Avoid division by zero

             // This is a highly simplified interpolation. A more physical model would involve heat transfer equations.
             // Let's use a formula that intuitively responds to controls:
             // Extremity temp is between EnvTemp and the temperature blood *would* bring it to without external loss.
             // Blood's heating effect is proportional to (effectiveBloodTemp - EnvTemp) * bloodFlowFactor
             // This effect is counteracted by heat loss to the environment, reduced by insulation.
             const heatGainPotentialFromBlood = (effectiveBloodTempReachingExtremity - envTemp) * bloodFlowFactor * 20; // Scale factor
             const heatLossPotentialToEnv = (coreBodyTemp - envTemp) / insulationResistance * 5; // Scale factor

             // Balance point - this is hand-wavy, trying to get intuitive results
             // ExtremityTemp = EnvTemp + (HeatGainFromBlood / TotalResistance)
             // Let's try: extremityTemp = EnvTemp + (effectiveBloodTempReachingExtremity - EnvTemp) * f(bloodFlow, insulation)
             // Where f increases with bloodFlow and insulation.

             // A better simplified approach: Extremity temperature is a mix of Env temp and blood temp, weighted by factors.
             const insulationEffect = Math.min(1, insulationResistance / 100); // Scales insulation to 0-1
             const bloodEffect = Math.min(1, bloodFlowFactor * 5); // Scales blood flow effect

             // Extremity temp is mainly envTemp, pulled towards coreTemp by blood and held by insulation
             // If blood flow is high AND insulation is poor, extremity temp is closer to core (without CC), high loss.
             // If blood flow is low AND insulation is good, extremity temp is closer to env (but insulated), low loss.
             // With CC, effectiveBloodTempReachingExtremity is closer to envTemp.

             // Let's simplify the extremity temp calculation based on the core concept:
             // Extremity temp is the EnvTemp PLUS some fraction of the temperature difference between
             // the effective incoming blood temp and the Env temp. This fraction is modified by blood flow.
             // Insulation primarily affects *total* heat loss, not just extremity temp directly in this simplified model.

             extremityTemp = envTemp + (effectiveBloodTempReachingExtremity - envTemp) * bloodFlowFactor * 0.6; // Adjust influence factor

             // Ensure extremity doesn't get warmer than the core
             extremityTemp = Math.min(extremityTemp, coreBodyTemp);
             // Ensure extremity doesn't get much colder than freezing point for living tissue
             extremityTemp = Math.max(extremityTemp, freezingPoint - 2); // Allow slightly below, but trigger warning


             // Calculate Total Heat Loss Rate (simplified relative value)
             // Heat loss is proportional to (CoreTemp - EnvTemp), modified by insulation and blood flow (especially without CC)

             let heatLossThroughSurface = (coreBodyTemp - envTemp) / insulationResistance;

             // Heat loss via blood: Without CC, warm blood cools down fully in the extremity and returns cold.
             // With CC, blood is pre-cooled, so less heat arrives, and returning blood is pre-warmed, recovering heat.
             let heatLossViaBlood;
             if (countercurrentEnabled) {
                 // With CC, blood returns warm, so net heat loss from blood loop is low.
                 // It's proportional to the *difference* in temp between incoming pre-cooled blood and returning pre-warmed blood,
                 // which is small, and depends on CC efficiency and blood flow.
                 // Simplified: Heat loss via blood is much lower, related to core-env difference and blood flow, but heavily reduced by CC.
                 heatLossViaBlood = (coreBodyTemp - envTemp) * bloodFlowFactor * 0.1; // Low loss
             } else {
                 // Without CC, blood arrives hot, leaves cold. Net heat loss via blood is significant.
                 // Proportional to (CoreTemp - ExtremityTemp) and blood flow.
                  heatLossViaBlood = (coreBodyTemp - extremityTemp) * bloodFlowFactor * 0.5; // Higher loss
             }

             // Total heat loss is sum of surface loss and net blood loss
             const totalHeatLoss = heatLossThroughSurface + heatLossViaBlood;


             // --- Update Display ---
            calculatedExtremityTempSpan.textContent = extremityTemp.toFixed(1);
            extremityTempDisplaySpan.textContent = extremityTemp.toFixed(1); // Update label display


            // Heat loss rate display (relative 1-10)
            // Need to map totalHeatLoss to a 1-10 scale intuitively.
            // Let's find approximate extremes:
            // Max loss (exposed, min ins thick, max blood, no CC, very cold env): ~40-60
            // Min loss (blubber, max ins thick, min blood, with CC, mild cold env): ~0.1 - 0.5

            const minRealisticLoss = 0.5; // Lower bound for mapping
            const maxRealisticLoss = 50; // Upper bound for mapping

            // Map totalHeatLoss to 1-10, clamping and using log scale might feel better
            const clampedLoss = Math.max(minRealisticLoss, Math.min(maxRealisticLoss, totalHeatLoss));
            const logScaledLoss = Math.log10(clampedLoss) - Math.log10(minRealisticLoss);
            const logScaleRange = Math.log10(maxRealisticLoss) - Math.log10(minRealisticLoss);
            const normalizedHeatLoss = Math.min(10, Math.max(1, (logScaledLoss / logScaleRange) * 9 + 1)); // Scale 1-10

            heatLossRateSpan.textContent = normalizedHeatLoss.toFixed(1);

            // --- Update Visuals ---

            // Update temperature gradient in tissue
             const tissueGradientEndTemp = extremityTemp;
             // The temp at the top of the limb model is closer to core temp. With CC, this drop starts earlier.
             const tissueGradientStartTempVisual = countercurrentEnabled ?
                 coreBodyTemp - (coreBodyTemp - tissueGradientEndTemp) * 0.5 : // Temp drops in upper limb with CC
                 coreBodyTemp; // Temp stays near core for longer without CC

             const gradientStops = [];
             const numStops = 20;
             for (let i = 0; i <= numStops; i++) {
                 const pos = i / numStops;
                 // Make temp drop curve
                 const easedPos = Math.pow(pos, 1.5); // Faster drop towards extremity
                 const tempAtPos = tissueGradientStartTempVisual - easedPos * (tissueGradientStartTempVisual - tissueGradientEndTemp);

                 const color = tempToColor(tempAtPos);
                 gradientStops.push(`${color} ${pos * 100}%`);
             }
             limbTissue.style.background = `linear-gradient(to bottom, ${gradientStops.join(', ')})`;


             // Update vessel colors and animation speed
             if (countercurrentEnabled) {
                 limbModel.classList.add('countercurrent-enabled');
             } else {
                 limbModel.classList.remove('countercurrent-enabled');
                 // Reset vessel colors if CSS class doesn't handle it (but it does here)
                 arteryVisual.style.background = 'linear-gradient(to bottom, var(--color-red-hot), #ff8800)';
                 veinVisual.style.background = 'linear-gradient(to bottom, var(--color-blue-cold), #8888ff)';
             }

             // Adjust pulse speed based on blood flow factor
             const pulseSpeed = 1.5 - (bloodFlowFactor * 0.8); // Faster pulse for higher flow (0.7s to 1.5s)
             arteryVisual.style.animationDuration = `${pulseSpeed}s`;
             veinVisual.style.animationDuration = `${pulseSpeed}s`;

             // Add class for visual high blood flow cue (optional)
             if (bloodFlowFactor > 0.8) {
                 limbModel.classList.add('high-blood-flow');
             } else {
                 limbModel.classList.remove('high-blood-flow');
             }


             // Update extremity color
             extremity.style.backgroundColor = tempToColor(extremityTemp);


             // Show freezing warning and overlay if extremity is too cold
             if (extremityTemp < freezingPoint + 1) { // Trigger warning slightly before actual freezing
                 freezingWarning.style.display = 'block';
                 limbModel.classList.add('is-frozen');
             } else {
                 freezingWarning.style.display = 'none';
                 limbModel.classList.remove('is-frozen');
             }

             // Update heat loss indicator
             if (normalizedHeatLoss > 2) { // Only show indicator for noticeable loss
                 heatLossIndicator.style.opacity = 1;
                 heatWaves.style.opacity = Math.min(1, (normalizedHeatLoss - 1) / 9 * 0.8 + 0.2); // Scale opacity

                 heatLossIndicator.classList.remove('low-loss', 'medium-loss', 'high-loss');
                 if (normalizedHeatLoss > 7) { heatLossIndicator.classList.add('high-loss'); }
                 else if (normalizedHeatLoss > 4) { heatLossIndicator.classList.add('medium-loss'); }
                 else { heatLossIndicator.classList.add('low-loss'); }

             } else {
                  heatLossIndicator.style.opacity = 0;
                  heatWaves.style.opacity = 0; // Hide waves when loss is very low
             }


        }

        // Add event listeners to all controls
        envTempControl.addEventListener('input', updateSimulation);
        insulationTypeControl.addEventListener('change', updateSimulation);
        insulationThicknessControl.addEventListener('input', updateSimulation);
        bloodFlowControl.addEventListener('input', updateSimulation);
        countercurrentControl.addEventListener('change', updateSimulation);

        // Initial update on page load
        updateSimulation();

        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
             toggleExplanationButton.textContent = isHidden ? "הסתר הסבר מפורט" : "גלו את הסודות: הצג/הסתר הסבר מפורט";
            if (isHidden) {
                 // Scroll to explanation if revealing it
                 explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });

         // Optional: Add a slight delay to initial animation for smoother start
         setTimeout(updateSimulation, 100);
    });
</script>
---