---
title: "מסע חיידקי: הסוד שמאחורי היוגורט והקפיר"
english_slug: the-secret-behind-yogurt-and-kefir
category: "ביולוגיה"
tags: ["תסיסה", "יוגורט", "קפיר", "חיידקים", "מדעי המזון", "פרוביוטיקה", "מעבדה ביתית"]
---
<div class="intro-text">
    <h1>מסע חיידקי: הסוד שמאחורי היוגורט והקפיר</h1>
    <p>מכירים את הקסם? לוקחים חלב רגיל, נוזלי ומתוק, ועם קצת עזרה מחברים מיקרוסקופיים בלתי נראים, מקבלים יוגורט סמיך ועשיר או קפיר תוסס ומרענן. איך זה קורה? מה הם עושים שם בפנים, ובאיזה תנאים הם עובדים הכי טוב? בואו נצא למסע מדעי קצר אל לב המיכל, ונגלה איך אתם יכולים להפוך לבמאים של התהליך הביולוגי המרתק הזה במעבדה הביתית שלנו!</p>
</div>

<div class="simulation-container">
    <h2>המעבדה המיקרוסקופית שלכם</h2>
    <p class="simulation-intro">בחרו את סוג המוצר, כוונו את הטמפרטורה והזמן, וראו איך המיקרואורגניזמים פועלים! האם תצליחו ליצור את התוצאה המושלמת?</p>

    <div class="controls">
        <div class="control-group">
            <label for="product-type">סוג התרבית:</label>
            <select id="product-type">
                <option value="yogurt">תרבית יוגורט (תרמופילית)</option>
                <option value="kefir">גרגרי קפיר (מזופילית/שמרים)</option>
            </select>
        </div>
        <div class="control-group">
            <label for="temperature">טמפרטורה (°C):</label>
            <input type="range" id="temperature" min="15" max="55" value="42">
            <span id="temp-value">42</span>
            <span class="temp-hint">אופטימלי ליוגורט: 40-45°C | אופטימלי לקפיר: 20-25°C</span>
        </div>
        <div class="control-group">
            <label for="duration">זמן תסיסה (שעות):</label>
            <input type="range" id="duration" min="2" max="72" value="12">
            <span id="duration-value">12</span>
             <span class="duration-hint">יוגורט: 6-12 שעות | קפיר: 12-48 שעות (עד שמתעבה)</span>
        </div>
        <button id="start-simulation"><i class="fas fa-play"></i> התחילו את התהליך!</button>
    </div>

    <div class="lab-display">
        <div class="beaker">
             <div class="liquid" id="beaker-liquid">
                <div class="microbes" id="beaker-microbes">
                    <!-- Microbe visual elements will be added here by JS -->
                </div>
                 <div class="kefir-bubbles" id="kefir-bubbles"></div>
                <div class="ph-indicator" id="ph-indicator">pH: 6.7</div>
                 <div class="texture-indicator" id="texture-indicator">מרקם: נוזלי</div>
            </div>
        </div>
        <div class="process-info">
            <p id="process-status" class="status-ready">מוכנים לצאת לדרך...</p>
            <div class="progress-bar-container">
                <div class="progress-bar" id="process-progress"></div>
            </div>
             <p id="elapsed-time">זמן שחלף: 0 שעות</p>
        </div>
    </div>

    <div class="results" id="simulation-results">
        <h3>תוצאות הניסוי המיקרוסקופי:</h3>
        <p id="final-texture"><span class="result-label">מרקם סופי:</span> <span class="result-value">טרם בוצע</span></p>
        <p id="final-ph"><span class="result-label">pH סופי:</span> <span class="result-value">טרם בוצע</span></p>
        <p id="final-outcome"><span class="result-label">תוצאה סופית:</span> <span class="result-value">טרם בוצע</span></p>
        <p id="outcome-explanation"></p>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button"><i class="fas fa-book"></i> הצגת ההסבר המדעי המלא</button>

<div class="explanation" id="scientific-explanation">
    <h2>ההסבר המדעי המרתק</h2>
    <p>מאחורי השינוי המדהים מחלב ליוגורט או קפיר עומד תהליך ביולוגי עתיק ורב עוצמה: <strong>תסיסה</strong>. זהו תהליך "אנרגטי" שבו מיקרואורגניזמים זעירים הופכים סוכרים (במקרה של חלב, בעיקר לקטוז) לתוצרים שונים, ללא צורך בחמצן.</p>

    <h3>השחקנים הראשיים: חיידקים ושמרים</h3>
    <p>בחלב, הגיבורים שלנו הם בעיקר <strong>חיידקי חומצת חלב (LAB - Lactic Acid Bacteria)</strong>. כל מוצר חלב מותסס משתמש ב"נבחרת" שונה של מיקרואורגניזמים:</p>
    <ul>
        <li><strong>יוגורט:</strong> מתבסס בעיקר על צמד חיידקים תרמופיליים (אוהבי חום): <em>Lactobacillus bulgaricus</em> ו-<em>Streptococcus thermophilus</em>. הם עובדים בטמפרטורות גבוהות יחסית (40-45 מעלות צלזיוס).</li>
        <li><strong>קפיר:</strong> עולם ומלואו! התרבית ("גרגרי קפיר") היא סימביוזה (חיים משותפים) מורכבת של חיידקי חומצת חלב (מגוון גדול של זנים), חיידקי חומצה אצטית ואפילו שמרים. הם פעילים בטמפרטורות חדר (20-25 מעלות צלזיוס) ואף בקירור איטי.</li>
    </ul>

    <h3>הפיכת הלקטוז לחומצה לקטית (והתוצרים האחרים בקפיר)</h3>
    <p>החלב עשיר בלקטוז, סוכר שהרבה יונקים מתקשים לעכל בבגרותם. המיקרואורגניזמים המותססים טורפים את הלקטוז. חיידקי ה-LAB מפרקים אותו וממירים אותו ביעילות ל<strong>חומצה לקטית</strong>. החומצה הזו היא שמעניקה ליוגורט ולקפיר את הטעם החמצמץ האופייני.</p>
    <p><strong>הייחודיות של הקפיר:</strong> בזכות נוכחות השמרים וחיידקי החומצה האצטית בגרגרים, תסיסת הקפיר מורכבת יותר. בנוסף לחומצה לקטית, נוצרות כמויות קטנות של אלכוהול, חומצה אצטית, ובעיקר <strong>פחמן דו-חמצני (CO2)</strong>, האחראי לגיזוז העדין שמאפיין את הקפיר.</p>

    <h3>הקסם של הגיבון: איך נוזל הופך לסמיך?</h3>
    <p>חלבון הקזאין הוא החלבון העיקרי בחלב. במצב רגיל, הוא מפוזר בחלב בצורה יציבה. ככל שרמת החומצה הלקטית עולה (וה-pH יורד), הסביבה הופכת חומצית יותר. כשה-pH יורד לאזור ה-4.6 (נקודת ה-pH האיזואלקטרית של הקזאין), חלבוני הקזאין מאבדים את המטען החשמלי שלהם, נצמדים זה לזה ויוצרים מבנה רשת תלת-ממדי – זהו תהליך ה<strong>גיבון</strong> או ה<strong>קרישה</strong>! רשת זו לוכדת את הנוזלים ויוצרת את המרקם הסמיך והג'לטיני של היוגורט והקפיר.</p>

    <h3>השפעת הטמפרטורה והזמן: סוד ההצלחה שלכם!</h3>
    <p><strong>טמפרטורה:</strong> לכל סוג של מיקרואורגניזמים יש טמפרטורת שיא לפעילות. חיידקי היוגורט עובדים הכי מהר וחזק בטמפרטורות "חמות" יחסית (40-45°C). טמפרטורות נמוכות מדי יאטו אותם דרמטית, וטמפרטורות גבוהות מדי עלולות להרוג אותם או לעודד חיידקים אחרים לא רצויים. גרגרי הקפיר לעומת זאת, מעדיפים טמפרטורות "קרירות" יותר (20-25°C), אבל יכולים לעבוד גם בטמפרטורות נמוכות יותר, פשוט לאט יותר.</p>
    <p><strong>זמן:</strong> הזמן קובע כמה חומצה יספיקו המיקרואורגניזמים לייצר. זמן קצר מדי = מעט חומצה, ה-pH לא יירד מספיק, והחלב לא יגבן (יישאר נוזלי). זמן ארוך מדי = הרבה חומצה, ה-pH יירד נמוך מדי, והמוצר יהיה חמוץ יתר על המידה, לפעמים גבשושי או עם הפרשת נוזלים (מי גבן). הזמן האופטימלי תלוי בסוג התרבית, הטמפרטורה, וכמות התרבית ההתחלתית.</p>

    <h3>היגיינה ויתרונות בריאותיים</h3>
    <p>כמו בכל ניסוי מדעי (וגם בבישול!), היגיינה קריטית! כלים נקיים מונעים כניסת חיידקים "רעים" שיתחרו בתרבית הרצויה, יקלקלו את המוצר או יהפכו אותו ללא בטוח לאכילה.</p>
    <p>יוגורט וקפיר טריים (שלא עברו פיסטור לאחר התסיסה) הם מקור מצוין ל<strong>פרוביוטיקה</strong> - מיקרואורגניזמים מועילים שתורמים לבריאות מערכת העיכול ואיזון פלורת המעיים. אכילתם היא דרך טעימה ובריאה לתמוך ב"חברים" הטובים שבפנים!</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'); /* For icons */

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        background-color: #f5f5f5;
        color: #333;
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3 {
        color: #4a2e00; /* Darker brown */
        text-align: center;
        margin-bottom: 15px;
        font-weight: 700;
    }

     h1 { font-size: 2em; margin-bottom: 25px; }
     h2 { font-size: 1.6em; border-bottom: 2px solid #ffcc80; padding-bottom: 5px; margin-top: 20px;}
     h3 { font-size: 1.3em; color: #795548; margin-top: 15px;}


    .intro-text {
        max-width: 800px;
        margin: 0 auto 30px auto;
        text-align: center;
    }

    .simulation-container {
        border: 1px solid #ffcc80; /* Lighter orange/brown */
        padding: 25px;
        margin-bottom: 30px;
        background: linear-gradient(to bottom, #fff8e1, #fff2d5); /* Light milk gradient */
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }

     .simulation-intro {
         text-align: center;
         margin-bottom: 25px;
         color: #5d4037; /* Brown */
         font-size: 1.1em;
     }

    .controls {
        display: flex;
        flex-wrap: wrap;
        gap: 25px;
        margin-bottom: 35px;
        justify-content: center;
        align-items: flex-end; /* Align items to bottom for consistent look */
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        min-width: 180px; /* Ensure consistent width */
    }

    .control-group label {
        margin-bottom: 8px;
        font-weight: 700;
        color: #5d4037; /* Brown */
        font-size: 1em;
    }

     .control-group select,
     .control-group input[type="range"] {
         width: 100%; /* Make inputs fill the container */
         margin-top: 0; /* Remove default margin */
     }

     .control-group input[type="range"] {
         -webkit-appearance: none; /* Override default styling */
         appearance: none;
         height: 8px;
         background: #ffb74d; /* Light orange */
         outline: none;
         opacity: 0.7;
         transition: opacity .2s;
         border-radius: 5px;
     }

      .control-group input[type="range"]:hover {
          opacity: 1;
      }

     .control-group input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px;
         height: 20px;
         background: #f57c00; /* Orange */
         cursor: pointer;
         border-radius: 50%;
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
     }

     .control-group input[type="range"]::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: #f57c00; /* Orange */
         cursor: pointer;
         border-radius: 50%;
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
     }


    #start-simulation {
        padding: 12px 25px;
        background-color: #4CAF50; /* Green for start */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: 700;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
         display: flex;
         align-items: center;
         gap: 8px;
    }

    #start-simulation i {
        font-size: 1.2em;
    }

    #start-simulation:hover {
        background-color: #45a049; /* Darker green */
        transform: translateY(-2px);
    }

    #start-simulation:active {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

     #start-simulation:disabled {
         background-color: #cccccc;
         cursor: not-allowed;
         box-shadow: none;
         transform: none;
     }

     .temp-hint, .duration-hint {
         font-size: 0.85em;
         color: #757575; /* Grey */
         margin-top: 5px;
         text-align: center; /* Center hints below sliders */
         width: 100%;
     }


    .lab-display {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 20px;
        position: relative; /* Needed for absolute positioning of elements */
    }

    .beaker {
        width: 150px;
        height: 220px;
        border: 3px solid #bcaaa4; /* Subtle grey-brown border */
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        border-bottom-left-radius: 30px;
        border-bottom-right-radius: 30px;
        position: relative;
        overflow: hidden;
        background-color: #eee; /* Light grey background for empty part */
        margin-bottom: 15px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
    }

    .liquid {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 100%; /* Starts full */
        background: linear-gradient(to top, #fff8e1, #fff2d5); /* Initial milk color */
        transition: all 0.8s ease-out; /* Smooth transition for visual changes */
        will-change: height, background; /* Optimize transitions */
    }

    .microbes {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0; /* Hidden initially */
        transition: opacity 1.5s ease-in;
        pointer-events: none; /* Allow clicks to pass through */
        z-index: 2; /* Above liquid */
    }

     .microbe {
         position: absolute;
         width: 8px;
         height: 8px;
         background-color: rgba(128, 0, 128, 0.5); /* Purple with opacity */
         border-radius: 50%;
         animation: pulsate 1.5s infinite ease-in-out;
     }

    @keyframes pulsate {
        0% { transform: scale(0.8); opacity: 0.6; }
        50% { transform: scale(1.2); opacity: 0.9; }
        100% { transform: scale(0.8); opacity: 0.6; }
    }

    .kefir-bubbles {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        pointer-events: none;
        z-index: 3; /* Above microbes */
    }

    .bubble {
         position: absolute;
         bottom: 0;
         width: 4px;
         height: 4px;
         background-color: rgba(255, 255, 255, 0.6); /* White with opacity */
         border-radius: 50%;
         animation: bubble-rise linear infinite;
     }

     @keyframes bubble-rise {
         0% { bottom: 0; opacity: 0.5; }
         100% { bottom: 100%; opacity: 0; }
     }


    .ph-indicator, .texture-indicator {
        position: absolute;
        right: 10px; /* Adjust for RTL */
        background-color: rgba(255, 255, 255, 0.9);
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.9em;
        color: #333;
        z-index: 5; /* Ensure indicators are on top */
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .ph-indicator {
        top: 10px;
    }

    .texture-indicator {
        top: 45px; /* Position below pH */
    }


    .process-info {
        width: 90%; /* Wider info area */
        max-width: 350px;
        text-align: center;
    }

     #process-status {
         font-weight: bold;
         margin-bottom: 10px;
         font-size: 1.1em;
         color: #5d4037; /* Brown */
     }

    .status-ready { color: #607d8b; /* Blue grey */ }
    .status-running { color: #f57c00; /* Orange */ }
    .status-completed { color: #4CAF50; /* Green */ }
    .status-warning { color: #ff9800; /* Amber */ }
    .status-failure { color: #f44336; /* Red */ }


    .progress-bar-container {
        width: 100%;
        height: 18px; /* Thicker progress bar */
        background-color: #e0e0e0;
        border-radius: 9px;
        overflow: hidden;
        margin-top: 10px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .progress-bar {
        height: 100%;
        width: 0;
        background-color: #8bc34a; /* Light green */
        border-radius: 9px;
        transition: width 0.4s linear; /* Smooth linear transition */
    }

     #elapsed-time {
         margin-top: 8px;
         font-size: 0.9em;
         color: #757575; /* Grey */
     }

    .results {
        margin-top: 30px;
        border-top: 2px dashed #ffcc80; /* Dashed orange/brown */
        padding-top: 20px;
        text-align: center;
         background-color: #fff; /* White background for results */
         padding: 20px;
         border-radius: 8px;
         box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    .results h3 {
        margin-bottom: 15px;
        color: #795548; /* Brown */
    }

    #simulation-results p {
        margin-bottom: 8px;
        font-size: 1.1em;
        color: #5d4037; /* Brown */
    }

     .result-label {
         font-weight: bold;
         color: #4a2e00; /* Darker brown */
     }

     .result-value {
         font-weight: normal;
     }

    #final-outcome .result-value {
        font-weight: bold;
    }

    .outcome-success .result-value { color: #4CAF50; } /* Green */
    .outcome-warning .result-value { color: #ff9800; } /* Amber */
    .outcome-failure .result-value { color: #f44336; } /* Red */

    #outcome-explanation {
        margin-top: 15px;
        font-size: 0.95em;
        color: #616161; /* Dark grey */
        font-style: italic;
    }


    .toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #607d8b; /* Blue grey */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: 700;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .toggle-button i {
         font-size: 1.2em;
    }

    .toggle-button:hover {
        background-color: #546e7a; /* Darker blue grey */
        transform: translateY(-2px);
    }

     .toggle-button:active {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
     }


    .explanation {
        border: 1px solid #bcaaa4; /* Subtle grey-brown */
        padding: 25px;
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        display: none; /* Hidden by default */
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    .explanation h3 {
        margin-top: 20px;
        margin-bottom: 10px;
        color: #6d4c41; /* Slightly lighter brown */
        text-align: right;
    }

     .explanation p, .explanation ul {
         text-align: right;
         margin-bottom: 1.2em;
         color: #424242; /* Dark grey */
     }

     .explanation ul {
         padding-right: 25px; /* Add padding for list items */
         list-style: disc outside; /* Disc bullets */
     }

     .explanation ul li {
         margin-bottom: 0.6em;
     }

     .explanation strong {
         color: #5d4037; /* Brown */
     }

    /* Responsive adjustments */
    @media (max-width: 600px) {
        body {
            padding: 15px;
        }

        h1 { font-size: 1.6em; }
        h2 { font-size: 1.4em; }
        h3 { font-size: 1.2em; }

        .controls {
            flex-direction: column;
            align-items: stretch;
            gap: 15px;
        }

        .control-group {
            min-width: 100%;
        }

        .beaker {
            width: 100px;
            height: 150px;
        }

        .ph-indicator, .texture-indicator {
            font-size: 0.8em;
            padding: 4px 8px;
        }

        .ph-indicator { top: 5px; right: 5px;}
        .texture-indicator { top: 35px; right: 5px;}

        #start-simulation, .toggle-button {
             width: 100%;
             justify-content: center;
        }

        .simulation-container, .explanation {
            padding: 15px;
        }
    }

     /* Animations for liquid texture change */
     @keyframes thicken-color-yogurt {
         0% { background: linear-gradient(to top, #fff8e1, #fff2d5); } /* Initial milk */
         50% { background: linear-gradient(to top, #ffecb3, #ffb300); } /* Slightly thicker */
         100% { background: linear-gradient(to top, #fff0c7, #ffc107); } /* Yogurt color */
     }

      @keyframes thicken-color-kefir {
         0% { background: linear-gradient(to top, #fff8e1, #fff2d5); } /* Initial milk */
         50% { background: linear-gradient(to top, #e1f5fe, #81d4fa); } /* Slightly thicker */
         100% { background: linear-gradient(to top, #e0f7fa, #80deea); } /* Kefir color */
     }

     @keyframes spoil-color {
          0% { background: linear-gradient(to top, #fff8e1, #fff2d5); } /* Initial milk */
          50% { background: linear-gradient(to top, #ffe0b2, #ff8a65); } /* Starting off */
          100% { background: linear-gradient(to top, #ffebee, #ef9a9a); } /* Reddish/spoiled */
     }


</style>

<script>
    const productTypeSelect = document.getElementById('product-type');
    const temperatureInput = document.getElementById('temperature');
    const tempValueSpan = document.getElementById('temp-value');
    const durationInput = document.getElementById('duration');
    const durationValueSpan = document.getElementById('duration-value');
    const startButton = document.getElementById('start-simulation');
    const beakerLiquid = document.getElementById('beaker-liquid');
    const beakerMicrobes = document.getElementById('beaker-microbes');
    const kefirBubblesContainer = document.getElementById('kefir-bubbles');
    const phIndicator = document.getElementById('ph-indicator');
    const textureIndicator = document.getElementById('texture-indicator');
    const processStatus = document.getElementById('process-status');
    const processProgress = document.getElementById('process-progress');
    const elapsedTimeSpan = document.getElementById('elapsed-time');
    const simulationResults = document.getElementById('simulation-results');
    const finalTextureSpan = document.getElementById('final-texture').querySelector('.result-value');
    const finalPhSpan = document.getElementById('final-ph').querySelector('.result-value');
    const finalOutcomeSpan = document.getElementById('final-outcome').querySelector('.result-value');
    const finalOutcomeP = document.getElementById('final-outcome'); // To add class for color
    const outcomeExplanation = document.getElementById('outcome-explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const scientificExplanationDiv = document.getElementById('scientific-explanation');

    const initialPh = 6.7;
    let simulationInterval = null;
    let bubbleInterval = null;
    let microbeInterval = null;


    // Update value spans when sliders move
    temperatureInput.addEventListener('input', () => {
        tempValueSpan.textContent = temperatureInput.value;
    });

    durationInput.addEventListener('input', () => {
        durationValueSpan.textContent = durationInput.value;
    });

     // Update hints based on product type selection
     productTypeSelect.addEventListener('change', () => {
         const productType = productTypeSelect.value;
         const tempHint = document.querySelector('.temp-hint');
         const durationHint = document.querySelector('.duration-hint');

         if (productType === 'yogurt') {
             tempHint.textContent = 'אופטימלי ליוגורט: 40-45°C';
             durationHint.textContent = 'יוגורט: 6-12 שעות';
             // Set default/suggested range values for yogurt
              temperatureInput.value = 42;
              durationInput.value = 8;
         } else { // kefir
             tempHint.textContent = 'אופטימלי לקפיר: 20-25°C';
             durationHint.textContent = 'קפיר: 12-48 שעות (עד שמתעבה)';
              // Set default/suggested range values for kefir
             temperatureInput.value = 24;
             durationInput.value = 24;
         }
          // Update displayed values
          tempValueSpan.textContent = temperatureInput.value;
          durationValueSpan.textContent = durationInput.value;

         // Reset display if simulation isn't running
         if (!startButton.disabled) {
            resetDisplay();
         }
     });


    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        if (scientificExplanationDiv.style.display === 'none' || scientificExplanationDiv.style.display === '') {
            scientificExplanationDiv.style.display = 'block';
            toggleExplanationButton.innerHTML = '<i class="fas fa-book-open"></i> הסתר הסבר מדעי';
        } else {
            scientificExplanationDiv.style.display = 'none';
            toggleExplanationButton.innerHTML = '<i class="fas fa-book"></i> הצגת ההסבר המדעי המלא';
        }
    });

    // Function to reset display elements
    function resetDisplay() {
        clearInterval(simulationInterval);
        clearInterval(bubbleInterval);
         clearInterval(microbeInterval);
        beakerLiquid.style.background = 'linear-gradient(to top, #fff8e1, #fff2d5)'; // Initial milk color
        beakerLiquid.style.height = '100%'; // Full liquid
        beakerMicrobes.style.opacity = 0;
         beakerMicrobes.innerHTML = ''; // Remove microbe elements
        kefirBubblesContainer.innerHTML = ''; // Remove bubble elements
        phIndicator.textContent = `pH: ${initialPh.toFixed(1)}`;
        phIndicator.style.color = '#333';
        textureIndicator.textContent = 'מרקם: נוזלי';
        processStatus.textContent = 'מוכנים לצאת לדרך...';
         processStatus.className = 'status-ready';
        processProgress.style.width = '0%';
        elapsedTimeSpan.textContent = 'זמן שחלף: 0 שעות';
        finalTextureSpan.textContent = 'טרם בוצע';
        finalPhSpan.textContent = 'טרם בוצע';
        finalOutcomeSpan.textContent = 'טרם בוצע';
        finalOutcomeP.className = '';
        outcomeExplanation.textContent = '';
        startButton.disabled = false;
    }


     // Function to simulate microbes visually
     function addMicrobes(count, isActive) {
         beakerMicrobes.innerHTML = ''; // Clear previous microbes
         beakerMicrobes.style.opacity = isActive ? 1 : 0.3; // Show if active, dim if slow
         const beakerRect = beakerMicrobes.getBoundingClientRect();
         for (let i = 0; i < count; i++) {
             const microbe = document.createElement('div');
             microbe.className = 'microbe';
             // Position randomly within the liquid area
             const x = Math.random() * (beakerRect.width - 8); // 8 is microbe size
             const y = Math.random() * (beakerRect.height - 8);
             microbe.style.left = `${x}px`;
             microbe.style.top = `${y}px`;
             // Adjust animation speed based on activity
             microbe.style.animationDuration = isActive ? '1.5s' : '3s';
             beakerMicrobes.appendChild(microbe);
         }
     }

     // Function to simulate kefir bubbles visually
     function addBubble() {
        const bubble = document.createElement('div');
        bubble.className = 'bubble';
        const size = Math.random() * 3 + 2; // Bubble size 2-5px
        bubble.style.width = `${size}px`;
        bubble.style.height = `${size}px`;
        // Position randomly at the bottom
        const x = Math.random() * 90 + 5; // 5-95% width
        bubble.style.left = `${x}%`;
        // Animation duration based on size (smaller bubbles rise faster)
        bubble.style.animationDuration = `${Math.random() * 2 + 3}s`;
        // Delay start slightly
         bubble.style.animationDelay = `-${Math.random() * 2}s`;

        kefirBubblesContainer.appendChild(bubble);

         // Remove bubble element after it finishes animating
         bubble.addEventListener('animationend', () => {
             bubble.remove();
         });
     }


    startButton.addEventListener('click', () => {
        resetDisplay(); // Ensure clean state before starting

        const productType = productTypeSelect.value;
        const temperature = parseInt(temperatureInput.value);
        const totalDurationHours = parseInt(durationInput.value); // Total desired duration

        startButton.disabled = true; // Disable button during simulation
        processStatus.textContent = 'מתחילים תסיסה...';
         processStatus.className = 'status-running';


        // --- Simulation Parameters (tuned for better realism) ---
        let optimalTemp, tempRange, optimalDurationHours;
        let tempSensitivity = 0.1; // How much temp affects speed/outcome (higher = more sensitive)
        let durationSensitivity = 0.05; // How much duration affects outcome

        if (productType === 'yogurt') {
            optimalTemp = 43;
            tempRange = [40, 46]; // Optimal range for yogurt bacteria
            optimalDurationHours = 8;
            // Yogurt bacteria die/slow significantly above 50-55 or below 30
        } else { // kefir
            optimalTemp = 24;
            tempRange = [20, 28]; // Optimal range for kefir culture
            optimalDurationHours = 24; // Kefir takes longer generally
            // Kefir culture is more resilient, works slower outside range, very slow below 15 or above 35-40
        }

        // Calculate activity multiplier based on temperature
        // Activity is peak at optimalTemp, drops off outside tempRange, very low far outside
        let activity = 0;
        if (temperature >= tempRange[0] && temperature <= tempRange[1]) {
            activity = 1.0; // Optimal
        } else if (temperature > tempRange[1] && temperature <= optimalTemp + 10) { // Slightly above optimal
             activity = Math.max(0.2, 1 - (temperature - tempRange[1]) * tempSensitivity);
         } else if (temperature < tempRange[0] && temperature >= optimalTemp - 15) { // Slightly below optimal
              activity = Math.max(0.2, 1 - (tempRange[0] - temperature) * tempSensitivity);
         } else { // Far from optimal
             activity = 0.05; // Very low activity
         }

        // Simulate microbes visually based on activity
        addMicrobes(50, activity > 0.5);
        if (microbeInterval) clearInterval(microbeInterval);
         microbeInterval = setInterval(() => addMicrobes(50, activity > 0.5), 2000); // Refresh microbe positions/activity visual

        // Simulate kefir bubbles based on activity and product type
        if (productType === 'kefir' && activity > 0.3) {
             if (bubbleInterval) clearInterval(bubbleInterval);
             // Produce more bubbles with higher activity
            const bubbleRate = Math.max(50, 200 - activity * 150); // Faster rate with higher activity
             bubbleInterval = setInterval(addBubble, bubbleRate);
        } else {
             kefirBubblesContainer.innerHTML = ''; // No bubbles if not kefir or low activity
        }


        // Simulation Loop
        const simulationSteps = 100; // Number of steps for animation
        const timePerStepMs = 50; // Milliseconds per animation step (total time = steps * timePerStepMs)
        const totalSimulatedTimeMs = simulationSteps * timePerStepMs;
        const hoursPerStep = totalDurationHours / simulationSteps;

        let currentStep = 0;
        let currentPh = initialPh;


        simulationInterval = setInterval(() => {
            currentStep++;
            const elapsedSimulatedHours = currentStep * hoursPerStep;
            const progressPercent = (currentStep / simulationSteps) * 100;

            // Simulate pH drop based on activity and elapsed *simulated* time
             // A simplified model: pH drops faster with higher activity
            const phDropRate = (activity * 2.5) / optimalDurationHours; // Max drop of ~2.5 pH over optimal duration at optimal activity
             currentPh = Math.max(3.5, initialPh - phDropRate * elapsedSimulatedHours); // pH stops dropping around 3.5


            // Update display during simulation
            processProgress.style.width = progressPercent + '%';
            elapsedTimeSpan.textContent = `זמן שחלף: ${elapsedSimulatedHours.toFixed(1)} שעות`;
            phIndicator.textContent = `pH: ${currentPh.toFixed(1)}`;

             // Update texture indicator based on current pH
            if (currentPh <= 4.6) {
                textureIndicator.textContent = productType === 'yogurt' ? 'מרקם: מסמיך...' : 'מרקם: מסמיך קלות...';
                textureIndicator.style.color = '#f57c00'; // Orange/amber
            } else if (currentPh < initialPh - (phDropRate * optimalDurationHours * 0.3)) { // Started dropping pH
                 textureIndicator.textContent = 'מרקם: מתחיל שינוי...';
                 textureIndicator.style.color = '#ffb74d'; // Light orange
            } else {
                 textureIndicator.textContent = 'מרקם: עדיין נוזלי';
                 textureIndicator.style.color = '#333';
            }

             // Simulate texture change visual slightly before coagulation pH
             if (currentPh <= 5.5 && currentPh > 4.6) {
                 const thickenFactor = 1 - (currentPh - 4.6) / (5.5 - 4.6); // 0 at 5.5, 1 at 4.6
                 if (productType === 'yogurt') {
                     beakerLiquid.style.background = `linear-gradient(to top, rgba(255, 248, 225, ${1-thickenFactor*0.5}), rgba(255, 224, 178, ${1-thickenFactor*0.5})), linear-gradient(to top, rgba(255, 236, 179, ${thickenFactor*0.5}), rgba(255, 179, 0, ${thickenFactor*0.5}))`;
                     beakerLiquid.style.background = `linear-gradient(to top, #fff0c7, rgba(255, 193, 7, ${thickenFactor}))`; // Simpler transition
                 } else { // Kefir
                      beakerLiquid.style.background = `linear-gradient(to top, #e1f5fe, rgba(129, 212, 250, ${thickenFactor}))`; // Simpler transition
                 }
                 // beakerLiquid.style.height = `${100 - thickenFactor * 2}%`; // Simulate slight thickening visual
             }


            if (currentStep >= simulationSteps) {
                clearInterval(simulationInterval);
                clearInterval(bubbleInterval);
                 clearInterval(microbeInterval);
                processStatus.textContent = 'התסיסה הסתיימה!';
                 processStatus.className = 'status-completed';
                startButton.disabled = false; // Re-enable button


                // --- Determine Final Outcome ---
                let finalTexture = 'נוזלי';
                let outcomeText = 'תוצאה: לא ברור';
                let outcomeClass = '';
                let explanation = '';

                const reachedCoagulation = currentPh <= 4.6;

                if (activity < 0.1 && totalDurationHours < 48) { // Very low activity, not enough time
                    outcomeText = 'כשלון: תרבית לא פעילה';
                    outcomeClass = 'outcome-failure';
                    explanation = `הטמפרטורה (${temperature}°C) הייתה רחוקה מאוד מהטווח האופטימלי של התרבית, או שהזמן קצר מדי עבור רמת פעילות נמוכה כל כך. התרבית לא הצליחה לגרום לשינוי משמעותי ב-pH.`;
                    finalTexture = 'נוזלי לחלוטין';
                     beakerLiquid.style.background = 'linear-gradient(to top, #fff8e1, #fff2d5)'; // Stay milk color
                } else if (reachedCoagulation) {
                    finalTexture = productType === 'yogurt' ? 'סמיך ויציב' : 'סמיך קלות עם גיזוז';
                    if (currentPh <= 4.0) { // Over-fermented
                        outcomeText = `${productType === 'yogurt' ? 'יוגורט' : 'קפיר'} חומצי מדי`;
                        outcomeClass = 'outcome-warning';
                        explanation = `התוצר סמיך, אך הגיע לרמת חומציות (pH ${currentPh.toFixed(1)}) נמוכה מדי, כנראה עקב זמן תסיסה ארוך מדי או טמפרטורה גבוהה מדי ביחס לזמן. הטעם יהיה חמוץ מאוד.`;
                         if (productType === 'yogurt') finalTexture = 'גבשושי קלות עם נוזלים';
                         beakerLiquid.style.background = productType === 'yogurt'
                             ? 'linear-gradient(to top, #fff0c7, #ffc107)' : 'linear-gradient(to top, #e0f7fa, #80deea)'; // Still looks okay visually
                    } else { // Coagulated successfully
                        const tempScore = Math.max(0, 1 - Math.abs(temperature - optimalTemp) / 5); // Score 0-1 for temp closeness
                        const durationScore = Math.max(0, 1 - Math.abs(totalDurationHours - optimalDurationHours) / (optimalDurationHours * 0.5)); // Score 0-1 for duration closeness

                        if (tempScore > 0.8 && durationScore > 0.7) {
                             outcomeText = `${productType === 'yogurt' ? 'יוגורט' : 'קפיר'} מושלם!`;
                             outcomeClass = 'outcome-success';
                             explanation = `הטמפרטורה (${temperature}°C) והזמן (${totalDurationHours} שעות) היו אופטימליים לסוג התרבית, והביאו לגיבון אידיאלי וחומציות מאוזנת (pH ${currentPh.toFixed(1)}).`;
                             // Apply successful color
                             if (productType === 'yogurt') {
                                 beakerLiquid.style.animation = 'thicken-color-yogurt 1s forwards';
                             } else {
                                  beakerLiquid.style.animation = 'thicken-color-kefir 1s forwards';
                             }

                        } else {
                             outcomeText = `${productType === 'yogurt' ? 'יוגורט' : 'קפיר'} טוב`;
                             outcomeClass = 'outcome-warning';
                             explanation = `התוצר גובן בהצלחה (pH ${currentPh.toFixed(1)}), אך התנאים לא היו אידיאליים לחלוטין. אולי ניתן לשפר את המרקם והטעם עם התאמה עדינה של הטמפרטורה ו/או הזמן.`;
                              beakerLiquid.style.background = productType === 'yogurt'
                                 ? 'linear-gradient(to top, #fff0c7, #ffc107)' : 'linear-gradient(to top, #e0f7fa, #80deea)'; // Still looks okay visually
                        }
                    }
                } else { // Did not coagulate (pH > 4.6)
                    outcomeText = `כשלון: לא גובן`;
                    outcomeClass = 'outcome-failure';
                     if (activity < 0.5) {
                         explanation = `התרבית לא היתה פעילה מספיק בגלל טמפרטורה לא אופטימלית (${temperature}°C) או שהזמן (${totalDurationHours} שעות) היה קצר מדי עבור רמת הפעילות שהושגה (pH סופי ${currentPh.toFixed(1)}).`;
                     } else { // Activity was decent but time too short
                          explanation = `התהליך לא הושלם. הזמן (${totalDurationHours} שעות) כנראה היה קצר מדי כדי להגיע לחומציות הנדרשת לגיבון (pH סופי ${currentPh.toFixed(1)}).`;
                     }
                    finalTexture = 'נוזלי';
                     beakerLiquid.style.background = 'linear-gradient(to top, #fff8e1, #fff2d5)'; // Stay milk color
                }

                 // Check for spoilage signs (simplified: high temp + long time + no coagulation)
                 if (!reachedCoagulation && temperature > (productType === 'yogurt' ? 50 : 40) && totalDurationHours > (productType === 'yogurt' ? 12 : 36) && activity < 0.5) {
                     outcomeText = `כשלון: כנראה מקולקל`;
                     outcomeClass = 'outcome-failure';
                     explanation = `טמפרטורה גבוהה מדי לאורך זמן ארוך מדי (כשאין פעילות תרבית מספקת) עלולה לעודד התפתחות חיידקים לא רצויים. התוצר נשאר נוזלי וכנראה אינו בטוח או טעים.`;
                     finalTexture = 'נוזלי (מקולקל)';
                     beakerLiquid.style.animation = 'spoil-color 1s forwards'; // Animate to spoiled color
                 }


                // Update final results display
                finalTextureSpan.textContent = finalTexture;
                finalPhSpan.textContent = currentPh.toFixed(1);
                finalOutcomeSpan.textContent = outcomeText;
                finalOutcomeP.className = outcomeClass; // Add class to the <p> tag
                outcomeExplanation.textContent = explanation;
                 textureIndicator.textContent = `מרקם: ${finalTexture}`; // Final texture display
                phIndicator.style.color = currentPh <= 4.6 ? '#4CAF50' : '#f44336'; // Green for low pH, Red for high pH


                 // Remove any ongoing animations applied during simulation steps
                 beakerLiquid.style.animation = '';

            }
        }, timePerStepMs); // Interval speed based on total simulation time
    });

    // Initial state display on load
    tempValueSpan.textContent = temperatureInput.value;
    durationValueSpan.textContent = durationInput.value;
    scientificExplanationDiv.style.display = 'none'; // Ensure hidden on load
    resetDisplay(); // Set initial display state

     // Populate initial microbes (static representation before sim starts)
     addMicrobes(30, false); // Dim and fewer microbes when inactive

</script>
```