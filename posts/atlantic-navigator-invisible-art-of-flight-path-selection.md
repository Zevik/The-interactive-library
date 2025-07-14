---
title: "נווט אטלנטי: האמנות הבלתי נראית של בחירת נתיב טיסה"
english_slug: atlantic-navigator-invisible-art-of-flight-path-selection
category: "טכנולוגיה / אווירונאוטיקה וחלל"
tags:
  - תעופה
  - ניווט
  - קבלת החלטות
  - אווירנאוטיקה
  - מטאורולוגיה אווירית
---

# נווט אטלנטי: האמנות הבלתי נראית של בחירת נתיב טיסה

האם ידעת שטיסה מניו יורק ללונדון לא עוברת תמיד במסלול הקצר ביותר? מעל האוקיינוס העצום, הנווט האווירי הוא אמן. הוא לא רק מוצא את הדרך, אלא מקבל סדרה מורכבת של החלטות שקופות לרוב הנוסעים. גלו מדוע בחירת נתיב הטיסה האופטימלי היא אומנות של ממש, ומהם הכוחות הבלתי נראים שמעצבים אותו בשמיים. נסו להיות הנווטים!

<div class="app-container">
    <div class="map-area">
        <div id="atlanticMap" class="map">
            <!-- Map layers -->
            <div class="map-base"></div>
            <div class="layer wind-layer"></div>
            <div class="layer weather-layer"></div>
            <div class="layer restricted-layer"></div>
            <!-- Path drawing area -->
            <canvas id="pathCanvas"></canvas>
             <!-- Start/End points markers -->
            <div class="start-point marker" data-city="NYC">NYC</div>
            <div class="end-point marker" data-city="LON">LON</div>
            <!-- Plane icon -->
            <div id="plane" class="plane-icon">✈️</div>
        </div>
    </div>
    <div class="controls-area">
        <h2>תוכנן את הנתיב שלך!</h2>
        <p>לחץ על המפה כדי להוסיף נקודות ציון לנתיב הטיסה (התחל קרוב ל-NYC, סיים קרוב ל-LON).</p>
        <button id="clearPathBtn">אפס נתיב</button>

        <h3>הפעל שכבות מידע:</h3>
        <label><input type="checkbox" class="layer-toggle" data-layer="wind"> רוחות (זרם סילון)</label><br>
        <label><input type="checkbox" class="layer-toggle" data-layer="weather"> מזג אוויר (סופות/טורבולנסיה)</label><br>
        <label><input type="checkbox" class="layer-toggle" data-layer="restricted"> אזורים מוגבלים</label><br>

        <h3>צא לדרך!</h3>
        <button id="runSimulationBtn">הרץ סימולציה ובדוק ביצועים</button>

        <div class="results-area">
            <h3>ביצועי הטיסה הנוכחית:</h3>
            <div id="currentResults">
                <p>שרטט נתיב והרץ סימולציה כדי לראות תוצאות...</p>
            </div>
            <div id="comparisonResults">
                <h4>השוואת נתיבים קודמים:</h4>
                <!-- Results of previous runs will appear here -->
                 <p class="no-results">עוד לא הרצת סימולציות להשוואה.</p>
            </div>
        </div>
    </div>
</div>

<button id="explanationButton" class="explanation-toggle-btn">הצג הסבר מעמיק: להיות נווט טרנס-אטלנטי</button>

<div id="explanation" class="explanation-area">
    <h2>הסבר מעמיק: האמנות של ניווט טרנס-אטלנטי</h2>

    <h3>האתגר הייחודי של ניווט מעל האוקיינוס</h3>
    <p>ניווט מעל האוקיינוס האטלנטי שונה באופן מהותי מניווט יבשתי. על היבשה, נווטים יכולים להסתמך על נקודות ציון ויזואליות (הרים, נהרות, ערים) ומערך צפוף של עזרי ניווט קרקעיים (כמו VOR או NDB). מעל האוקיינוס, הנוף אחיד, המרחקים עצומים, ואין כמעל עזרי ניווט קרקעיים. הניווט מתבצע בעיקר באמצעות מערכות אינרציאליות (INS/IRS) ומערכות לוויניות (GPS), אך בחירת הנתיב עצמה הופכת למורכבת הרבה יותר בשל גורמים סביבתיים.</p>

    <h3>מהו נתיב טיסה אופטימלי ולמה הוא לא תמיד הקו הישר?</h3>
    <p>הקו הקצר ביותר בין שתי נקודות על פני כדור הארץ הוא קשת של מעגל גדול (Orthodromic line). לדוגמה, הקו הישר מניו יורק ללונדון נראה מעוקל על מפה דו-ממדית שטוחה (מטיל מרקטור), אבל הוא הנתיב המרחבי הקצר ביותר. עם זאת, נתיב הטיסה ה"אופטימלי" אינו תמיד הקצר ביותר מבחינת מרחק. הוא הנתיב שממטב שילוב של גורמים כמו זמן טיסה, צריכת דלק, בטיחות ונוחות הנוסעים. לעיתים קרובות, סטייה מהקו הישר יכולה להוביל לחיסכון משמעותי בדלק וזמן.</p>
    <p>לעומת Orthodromic, נתיב Loxodromic (או Rhumb line) הוא קו שחותך את קווי האורך בזווית קבועה. נתיבים אלו נוחים יותר לניווט ימי מסורתי אך אינם יעילים למרחקים ארוכים בטיסה.</p>

    <h3>הכוחות הבלתי נראים: השפעת רוחות בגובה רב</h3>
    <p>הגורם המשמעותי ביותר המשפיע על אופטימיזציית הנתיב מעל האוקיינוס הוא הרוח, ובפרט זרם הסילון (Jet Stream). זהו זרם אוויר חזק וצר הנע בגובה רב (בדרך כלל בגובה שיוט של מטוסים), לרוב ממערב למזרח. טיסה עם זרם הסילון (רוח גב) יכולה להגדיל משמעותית את מהירות המטוס יחסית לקרקע (Ground Speed), ובכך לקצר את זמן הטיסה ולחסוך דלק. טיסה נגד זרם הסילון (רוח פנים) מאיטה את המטוס ודורשת יותר זמן ודלק.</p>
    <p>הנווט האווירי מנתח את מפות הרוח הנוכחיות והחזויות כדי לבחור נתיב שינצל את רוח הגב בטיסות מזרחה וימנע, ככל הניתן, רוחות פנים חזקות בטיסות מערבה. סטייה של מאות מיילים מהקו הישר יכולה להיות מוצדקת כלכלית ותפעולית אם היא מאפשרת ניצול מיטבי של זרם הסילון.</p>

    <h3>תפקיד המטאורולוגיה: הימנעות מאזורי מזג אוויר מסוכנים או לא נוחים</h3>
    <p>מעבר לרוח, תחזית מזג האוויר חיונית לבטיחות ונוחות. הנווטים חייבים להימנע מאזורי סופות רעמים פעילות (Cumulonimbus clouds), ברד, קפיאת מים בגובה רב (icing), וטורבולנסיה חזקה (Clear Air Turbulence - CAT). אזורים אלו לא רק מהווים סיכון בטיחותי אלא גם פוגעים בנוחות הנוסעים ועלולים לגרום לנזק למטוס. לעיתים קרובות, נתיב ארוך יותר העוקף אזורי מזג אוויר קשים עדיף על פני נתיב קצר יותר החוצה אותם.</p>

    <h3>גורמים נוספים המשפיעים על בחירת הנתיב</h3>
    <p>מלבד רוח ומזג אוויר, גורמים נוספים נלקחים בחשבון:</p>
    <ul>
        <li>**מגבלות מרחב אווירי:** קיימים אזורים אסורים או מוגבלים לטיסה מעל האוקיינוס (למשל, אזורי אימונים צבאיים, אזורים פוליטיים רגישים).</li>
        <li>**עומס תנועה:** מעל צפון האוקיינוס האטלנטי (NAT - North Atlantic Tracks) קיימים נתיבי תנועה מאורגנים המשתנים מדי יום בהתאם לתנועה ולרוחות. לעיתים קרובות יש צורך לטוס בנתיבים אלו או בקרבתם כדי להימנע מהתנגשויות ולשמור על הפרדה בטוחה.</li>
        <li>**דרישות חברת התעופה:** חברות תעופה עשויות לתעדף גורמים שונים (למשל, חיסכון בדלק על פני זמן טיסה קצר מאוד, או להיפך).</li>
        <li>**שדות תעופה חלופיים:** יש לוודא שהנתיב מאפשר גישה לשדות תעופה חלופיים מתאימים במקרה חירום.</li>
    </ul>

    <h3>תהליך קבלת ההחלטות של הנווט האווירי</h3>
    <p>תכנון נתיב טיסה טרנס-אטלנטי הוא תהליך מורכב הכולל:</p>
    <ol>
        <li>**איסוף נתונים:** ניתוח תחזיות רוח, מזג אוויר, מידע על אזורים מוגבלים, ומידע על עומס תנועה.</li>
        <li>**תכנון מקדים:** יצירת מספר נתיבים אפשריים ובחינת ההשפעה של כל אחד מהם על זמן, דלק, בטיחות ונוחות. תוכנות מחשב מסייעות מאוד בתהליך זה.</li>
        <li>**בחירת הנתיב האופטימלי:** קבלת החלטה על הנתיב המועדף בהתאם לסדרי העדיפויות.</li>
        <li>**עדכונים בזמן אמת:** במהלך הטיסה, הנווט והטייסים עוקבים אחר תנאי הסביבה ומוכנים לבצע התאמות בנתיב במידת הצורך (למשל, עקיפת סופת רעמים שהתפתחה).</li>
    </ol>

     <h3>ההבדל בין טיסה מזרחה לטיסה מערבה</h3>
     <p>בשל זרם הסילון העיקרי הנע ממערב למזרח, טיסות מזרחה (למשל, מארה"ב לאירופה) נוטות להיות קצרות יותר וצורכות פחות דלק מטיסות מערבה (מאירופה לארה"ב). הנווט בטיסה מזרחה יחפש נתיב שיש לו את רוח הגב החזקה ביותר. הנווט בטיסה מערבה יחפש נתיב שיש בו את רוח הפנים החלשה ביותר, או שיעקוף את זרם הסילון אם הוא חזק במיוחד, גם אם זה אומר לטוס בנתיב ארוך יותר או בגובה שיוט נמוך יותר.</p>

    <h3>כיצד טכנולוגיה מודרנית מסייעת לנווטים</h3>
    <p>בעבר, הניווט האווירי הסתמך על טכניקות מורכבות כמו ניווט שמיימי (אסטרונומיה). כיום, טכנולוגיות כמו INS/IRS ו-GPS מספקות מיקום מדויק. תוכנות תכנון טיסה מתוחכמות מנתחות כמויות אדירות של נתוני מזג אוויר ותנועה בזמן אמת ומציעות לנווטים מספר נתיבים אופטימליים אפשריים לבחירה, תוך חישוב מדויק של זמן, דלק ועומסי רוח לכל נתיב. טכנולוגיה זו אינה מבטלת את הצורך בנווט אנושי מיומן, אך היא מאפשרת לו לקבל החלטות מושכלות ומדויקות יותר במהירות וביעילות.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap');

    body {
        font-family: 'Rubik', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
        padding: 0;
        margin: 0;
    }

    h1, h2, h3, h4 {
        color: #1a2e3f;
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 20px;
    }

    p {
        margin-bottom: 10px;
    }

    .app-container {
        display: flex;
        flex-wrap: wrap-reverse; /* Controls below map on smaller screens */
        gap: 30px;
        max-width: 1200px;
        margin: 20px auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        direction: rtl;
        text-align: right;
    }

    .map-area {
        flex: 2;
        min-width: 400px; /* Adjusted min-width */
        position: relative;
        border-radius: 8px;
        overflow: hidden; /* Ensures layers/canvas stay within bounds */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .controls-area {
        flex: 1;
        min-width: 300px;
        background-color: #eef2f7; /* Light blueish background */
        padding: 25px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        display: flex;
        flex-direction: column;
    }

    .map {
        width: 100%;
        height: 550px; /* Slightly increased height */
        position: relative;
        background-color: #a8d8f0; /* Deeper blue for ocean */
        overflow: hidden;
    }

    .map-base {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Mercator_projection_SW.jpg/1024px-Mercator_projection_SW.jpg'); /* Real Atlantic map */
        background-size: cover;
        background-position: center;
        z-index: 1;
        opacity: 0.6; /* Make map semi-transparent */
        filter: grayscale(20%); /* Slightly desaturate */
    }

    #pathCanvas {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 10;
        cursor: crosshair;
    }

     /* Drawing style for path and points */
     #pathCanvas.drawing {
         cursor: grabbing;
     }

    .layer {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0; /* Initially hidden */
        transition: opacity 0.5s ease-in-out; /* Smooth transition */
        z-index: 5;
        pointer-events: none; /* Layers shouldn't interfere with mouse events on canvas */
    }

    .layer.active {
        opacity: 0.8; /* Make active layers visible */
    }

    /* Enhanced layer styling */
    .wind-layer {
        background: linear-gradient(to right, rgba(255, 100, 100, 0.2), rgba(255, 200, 0, 0.2), rgba(100, 255, 100, 0.2)); /* Represents varying wind conditions */
         /* Add subtle animation? */
         /* background-size: 200% 100%;
         animation: wind-flow 30s linear infinite; */
    }

    /* @keyframes wind-flow {
        0% { background-position: 0% 0; }
        100% { background-position: 100% 0; }
    } */

    .weather-layer {
        background: radial-gradient(circle, rgba(100, 0, 100, 0.3) 0%, rgba(255, 200, 0, 0.3) 50%, rgba(255, 200, 0, 0) 70%); /* Example: a storm cell */
         background-position: 60% 70%; /* Example position */
         background-repeat: no-repeat;
         background-size: 30% 40%; /* Example size */
    }

    .restricted-layer {
        background: repeating-linear-gradient(45deg, rgba(255, 0, 0, 0.2), rgba(255, 0, 0, 0.2) 10px, transparent 10px, transparent 20px); /* Red stripes for restricted */
        opacity: 0; /* Controlled by .active */
    }


    .marker {
        position: absolute;
        width: 50px; /* Increased size */
        height: 25px; /* Increased size */
        background-color: #fff;
        border: 2px solid #1a2e3f;
        text-align: center;
        line-height: 25px;
        font-size: 13px;
        font-weight: bold;
        color: #1a2e3f;
        z-index: 20;
        border-radius: 6px;
        transform: translate(-50%, -50%); /* Center the marker */
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        cursor: pointer; /* Indicate interactivity */
    }

    .start-point {
        top: 75%; /* Adjusted position */
        left: 15%; /* Adjusted position */
    }

    .end-point {
        top: 25%; /* Adjusted position */
        left: 85%; /* Adjusted position */
    }

    .plane-icon {
        position: absolute;
        font-size: 24px; /* Size of the emoji */
        transform: translate(-50%, -50%) rotate(0deg); /* Center and initial rotation */
        z-index: 25; /* Above everything */
        transition: left linear, top linear, transform linear; /* Smooth movement and rotation */
        pointer-events: none; /* Cannot be clicked */
         display: none; /* Hidden initially */
    }


    .controls-area h2, .controls-area h3 {
        margin-top: 0;
        color: #1a2e3f;
    }

    .controls-area label {
        display: flex; /* Use flex for alignment */
        align-items: center;
        margin-bottom: 12px; /* Increased spacing */
        cursor: pointer;
        font-size: 15px;
    }

    .controls-area label input[type="checkbox"] {
        margin-left: 8px; /* Space between checkbox and label */
        appearance: none; /* Hide default checkbox */
        width: 18px;
        height: 18px;
        border: 2px solid #007bff;
        border-radius: 4px;
        position: relative;
        cursor: pointer;
        flex-shrink: 0; /* Prevent shrinking */
    }

     .controls-area label input[type="checkbox"]:checked {
         background-color: #007bff;
         border-color: #007bff;
     }

      .controls-area label input[type="checkbox"]:checked::after {
          content: '✔';
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          color: white;
          font-size: 12px;
          font-weight: bold;
      }


    .controls-area button {
        display: block;
        width: 100%;
        padding: 12px; /* Increased padding */
        margin-top: 15px; /* Increased spacing */
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 6px; /* Rounded corners */
        cursor: pointer;
        font-size: 17px; /* Increased font size */
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 500;
    }

     #clearPathBtn {
        background-color: #dc3545; /* Red color */
        margin-bottom: 20px;
    }

    .controls-area button:hover {
        background-color: #0056b3;
        transform: translateY(-1px); /* Slight lift effect */
    }

     #clearPathBtn:hover {
         background-color: #c82333;
     }

     #runSimulationBtn:hover {
          background-color: #218838;
     }

     #runSimulationBtn {
         background-color: #28a745; /* Green color */
     }


    .results-area {
        margin-top: 25px; /* Increased spacing */
        border-top: 1px solid #cce5ff; /* Lighter, colorful separator */
        padding-top: 20px;
    }

     .results-area h3 {
         margin-bottom: 10px;
         color: #0056b3;
     }

     .results-area h4 {
        margin-top: 20px;
        margin-bottom: 8px;
        color: #1a2e3f;
        border-bottom: 1px dashed #ccc;
        padding-bottom: 5px;
     }

    #currentResults p {
        margin: 8px 0;
        font-size: 15px;
        color: #333;
    }

     #currentResults strong {
         color: #1a2e3f;
     }


    #comparisonResults {
         max-height: 250px; /* Limit height */
         overflow-y: auto; /* Add scroll if too many results */
         padding-right: 5px; /* Add padding for scrollbar */
     }

     #comparisonResults .no-results {
         text-align: center;
         color: #666;
         font-style: italic;
     }

    #comparisonResults div {
        border: 1px solid #b8daff; /* Light blue border */
        padding: 12px;
        margin-bottom: 15px; /* Increased spacing */
        border-radius: 6px;
        background-color: #e9f7ff; /* Very light blue background */
        transition: background-color 0.3s ease;
    }

     #comparisonResults div:hover {
         background-color: #d9edf7; /* Slightly darker on hover */
     }

    #comparisonResults div p {
        margin: 4px 0; /* Reduced margin */
        font-size: 14px;
        color: #004085; /* Dark blue text */
    }

    #comparisonResults div p em {
        font-size: 12px;
        color: #666;
    }


    .explanation-toggle-btn {
        display: block;
        width: fit-content;
        margin: 30px auto; /* More margin */
        padding: 12px 25px; /* More padding */
        background-color: #28a745;
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 18px;
        font-weight: 500;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .explanation-toggle-btn:hover {
         background-color: #218838;
         transform: translateY(-1px);
    }

    .explanation-area {
        margin-top: 20px;
        padding: 30px; /* More padding */
        background-color: #eef2f7; /* Match controls background */
        border-radius: 8px;
        display: none; /* Initially hidden */
        direction: rtl;
        text-align: right;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: opacity 0.5s ease-in-out;
    }

    .explanation-area h2, .explanation-area h3 {
        color: #1a2e3f;
        margin-bottom: 15px;
    }

    .explanation-area p {
        line-height: 1.7; /* Increased line height */
        margin-bottom: 15px;
        color: #333;
    }

    .explanation-area ul {
        margin-bottom: 15px;
        padding-right: 25px; /* Adjust for RTL */
        list-style: disc;
        color: #333;
    }

    .explanation-area li {
        margin-bottom: 8px;
    }

    .explanation-area ol {
         margin-bottom: 15px;
        padding-right: 25px; /* Adjust for RTL */
         list-style: decimal;
         color: #333;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .app-container {
            flex-direction: column; /* Stack columns */
            padding: 15px;
            gap: 20px;
        }
        .map-area, .controls-area {
            min-width: 100%; /* Full width */
        }
        .map {
            height: 400px; /* Reduce map height on smaller screens */
        }
        .explanation-area {
            padding: 20px;
        }
        .explanation-toggle-btn {
            font-size: 16px;
            padding: 10px 20px;
        }
         .marker {
             width: 40px;
             height: 20px;
             line-height: 20px;
             font-size: 10px;
         }
    }

</style>

<script>
    const explanationButton = document.getElementById('explanationButton');
    const explanationDiv = document.getElementById('explanation');
    const atlanticMap = document.getElementById('atlanticMap');
    const layerToggles = document.querySelectorAll('.layer-toggle');
    const pathCanvas = document.getElementById('pathCanvas');
    const clearPathBtn = document.getElementById('clearPathBtn');
    const runSimulationBtn = document.getElementById('runSimulationBtn');
    const currentResultsDiv = document.getElementById('currentResults');
    const comparisonResultsDiv = document.getElementById('comparisonResults');
    const planeIcon = document.getElementById('plane');
    const ctx = pathCanvas.getContext('2d');

    let pathPoints = [];
    let startPoint = { x: 0, y: 0, element: document.querySelector('.start-point') };
    let endPoint = { x: 0, y: 0, element: document.querySelector('.end-point') };
    const minDistanceToStart = 30; // Pixels tolerance to start drawing near NYC
    const minDistanceToEnd = 30;   // Pixels tolerance to snap to LON
    const minPointDistance = 10; // Minimum distance between path points added by click

    let simulationRunning = false;
    let comparisonResults = [];

    // Helper to get canvas position relative to map container
    function getCanvasMousePosition(event) {
        const rect = pathCanvas.getBoundingClientRect();
        const scaleX = pathCanvas.width / rect.width;
        const scaleY = pathCanvas.height / rect.height;
        return {
            x: (event.clientX - rect.left) * scaleX,
            y: (event.clientY - rect.top) * scaleY
        };
    }

    // Resize canvas and update marker positions
    function resizeCanvas() {
        const mapRect = atlanticMap.getBoundingClientRect();
        pathCanvas.width = mapRect.width;
        pathCanvas.height = mapRect.height;

        // Get marker positions relative to the map container and convert to canvas coordinates
        const startRect = startPoint.element.getBoundingClientRect();
        const endRect = endPoint.element.getBoundingClientRect();

        // Calculate center of the marker relative to the map container
        startPoint.x = (startRect.left + startRect.width / 2 - mapRect.left);
        startPoint.y = (startRect.top + startRect.height / 2 - mapRect.top);

        endPoint.x = (endRect.left + endRect.width / 2 - mapRect.left);
        endPoint.y = (endRect.top + endRect.height / 2 - mapRect.top);

        redrawPath(); // Redraw path after resizing
    }

    // Draw path, points, and markers on canvas
    function redrawPath() {
        ctx.clearRect(0, 0, pathCanvas.width, pathCanvas.height);

        // Draw previous comparison paths faintly (optional feature, keep simple for now)
        // ...

        if (pathPoints.length > 0) {
            ctx.beginPath();
            ctx.moveTo(pathPoints[0].x, pathPoints[0].y);
            for (let i = 1; i < pathPoints.length; i++) {
                ctx.lineTo(pathPoints[i].x, pathPoints[i].y);
            }
            ctx.strokeStyle = '#007bff';
            ctx.lineWidth = 4; // Thicker path
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';
            ctx.stroke();

            // Draw points as circles
            ctx.fillStyle = '#007bff';
            pathPoints.forEach(p => {
                ctx.beginPath();
                ctx.arc(p.x, p.y, 5, 0, Math.PI * 2); // Larger points
                ctx.fill();
            });
        }

         // Draw start/end circle markers on canvas
         drawCanvasMarker(startPoint, 'NYC', '#007bff');
         drawCanvasMarker(endPoint, 'LON', '#28a745');
    }

     // Draw a circle marker on the canvas
     function drawCanvasMarker(point, text, color) {
         ctx.fillStyle = color;
         ctx.strokeStyle = '#fff';
         ctx.lineWidth = 2;
         ctx.beginPath();
         ctx.arc(point.x, point.y, 10, 0, Math.PI * 2); // Circle radius
         ctx.fill();
         ctx.stroke();

         ctx.fillStyle = '#fff';
         ctx.font = 'bold 10px Rubik';
         ctx.textAlign = 'center';
         ctx.textBaseline = 'middle';
         ctx.fillText(text, point.x, point.y);
     }


    // Handle click to add waypoint
    pathCanvas.addEventListener('click', (event) => {
         if (simulationRunning) return; // Don't add points while simulating

        const pos = getCanvasMousePosition(event);
        const distToStart = Math.sqrt(Math.pow(pos.x - startPoint.x, 2) + Math.pow(pos.y - startPoint.y, 2));
        const distToEnd = Math.sqrt(Math.pow(pos.x - endPoint.x, 2) + Math.pow(pos.y - endPoint.y, 2));

        if (pathPoints.length === 0) {
            // Must start near NYC
            if (distToStart < minDistanceToStart) {
                 pathPoints.push({ x: startPoint.x, y: startPoint.y }); // Snap first point to start
                redrawPath();
            } else {
                 currentResultsDiv.innerHTML = "<p style='color: orange;'>התחל את הנתיב קרוב לניו יורק (NYC).</p>";
            }
        } else {
            // Add subsequent points
             const lastPoint = pathPoints[pathPoints.length - 1];
             const distFromLast = Math.sqrt(Math.pow(pos.x - lastPoint.x, 2) + Math.pow(pos.y - lastPoint.y, 2));

             if (distFromLast > minPointDistance) { // Ensure minimum distance between points
                 pathPoints.push(pos);
                 redrawPath();

                  // Optional: Snap last point to end if close enough
                 if (distToEnd < minDistanceToEnd) {
                     // Add end point as the last point and finish path
                     if (pathPoints[pathPoints.length -1] !== endPoint) { // Avoid adding twice if already snapped
                          pathPoints.push({ x: endPoint.x, y: endPoint.y });
                          redrawPath();
                          currentResultsDiv.innerHTML += "<p>הנתיב מחובר ללונדון (LON). מוכן לסימולציה!</p>";
                     }
                 } else if (pathPoints[pathPoints.length -1] === endPoint) {
                         // If snapped to end but clicked elsewhere, remove snap
                         pathPoints.pop();
                         pathPoints.push(pos);
                         redrawPath();
                  }
             }
        }
         // Check if last point is near end after adding
         if (pathPoints.length > 0) {
             const lastPoint = pathPoints[pathPoints.length - 1];
             const distToEndCheck = Math.sqrt(Math.pow(lastPoint.x - endPoint.x, 2) + Math.pow(lastPoint.y - endPoint.y, 2));
              if (distToEndCheck < minDistanceToEnd && lastPoint !== endPoint) {
                 pathPoints.push({ x: endPoint.x, y: endPoint.y }); // Snap last point to end
                 redrawPath();
                 currentResultsDiv.innerHTML += "<p>הנתיב מחובר ללונדון (LON). מוכן לסימולציה!</p>";
              }
         }
    });

    // Basic simulation logic (more realistic)
    async function runSimulation() {
        if (simulationRunning) return;
        if (pathPoints.length < 2) {
            currentResultsDiv.innerHTML = "<p style='color: red;'>שרטט נתיב על ידי לחיצה על המפה (התחל קרוב ל-NYC, סיים קרוב ל-LON).</p>";
            return;
        }

        // Ensure the path ends near LON, or add LON point if last point is close
         const lastPoint = pathPoints[pathPoints.length - 1];
         const distToEndCheck = Math.sqrt(Math.pow(lastPoint.x - endPoint.x, 2) + Math.pow(lastPoint.y - endPoint.y, 2));
         if (distToEndCheck > minDistanceToEnd) {
             currentResultsDiv.innerHTML = "<p style='color: orange;'>הנתיב חייב להסתיים קרוב ללונדון (LON).</p>";
             return;
         }
         // If the very last point isn't the exact end point, make it so for simulation accuracy
         if (lastPoint !== endPoint) {
             pathPoints.push({ x: endPoint.x, y: endPoint.y });
             redrawPath(); // Redraw with snapped end point
         }


        simulationRunning = true;
        currentResultsDiv.innerHTML = "<p>מריץ סימולציה...</p>";
        planeIcon.style.display = 'block'; // Show plane

        let totalDistance = 0;
        let totalTime = 0;
        let totalFuel = 0;
        let comfortScore = 100; // Start with max comfort
        let warnings = [];

        const baseAirspeedKnots = 500; // Example base speed
        const fuelBurnRate = 10; // Example fuel units per distance unit at base speed
        const canvasPixelToNm = 0.8; // Example conversion factor

        // Reset plane position to start
        planeIcon.style.left = pathPoints[0].x + 'px';
        planeIcon.style.top = pathPoints[0].y + 'px';
        planeIcon.style.transition = 'none'; // Disable transition initially
        await new Promise(resolve => setTimeout(resolve, 50)); // Small delay to apply non-transition style


        // Animate plane and calculate results segment by segment
        for (let i = 0; i < pathPoints.length - 1; i++) {
            const p1 = pathPoints[i];
            const p2 = pathPoints[i+1];

            const segmentDistancePixels = Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
            const segmentDistanceNm = segmentDistancePixels * canvasPixelToNm;
            totalDistance += segmentDistanceNm;

            // Calculate heading for plane rotation (simplified)
            const angleRad = Math.atan2(p2.y - p1.y, p2.x - p1.x);
            const angleDeg = angleRad * 180 / Math.PI;
            // Adjust angle for airplane emoji which points right (0 degrees)
            // Need to rotate it so it points along the path direction
            const planeRotation = angleDeg; // No need for +90 for this emoji

            // --- Simulate Effects for this segment ---
            let currentAirspeedKnots = baseAirspeedKnots;
            let segmentComfort = 0; // Penalty for this segment

            // Simplified Zone Checks (using bounding box for simplicity)
            const segmentMidX = (p1.x + p2.x) / 2;
            const segmentMidY = (p1.y + p2.y) / 2;

            // Wind Effect (Jet Stream: Strong tailwind Eastbound in upper band, Headwind Westbound)
            const windLayerActive = atlanticMap.querySelector('.wind-layer').classList.contains('active');
            if (windLayerActive) {
                 const jetStreamLatBandY = [atlanticMap.offsetHeight * 0.2, atlanticMap.offsetHeight * 0.5]; // Y range for jet stream
                 const isInJetStreamLat = (segmentMidY >= jetStreamLatBandY[0] && segmentMidY <= jetStreamLatBandY[1]);

                 if (isInJetStreamLat) {
                     const directionX = p2.x - p1.x;
                     const directionY = p2.y - p1.y;

                     // Estimate segment angle relative to East (0 deg)
                     const segmentAngle = Math.atan2(directionY, directionX); // Radians, 0 = East, PI = West
                     const windAngle = 0; // Assume Jet Stream flows roughly East (0 rad)

                     // Dot product of segment vector and wind vector (simplified)
                     // segmentVector = (directionX, directionY)
                     // windVector = (1, 0) assuming Eastward wind
                     // dotProduct = directionX * 1 + directionY * 0 = directionX
                     // Positive dot product means tailwind component, Negative means headwind
                     const windComponent = directionX; // Simplified representation of wind effect

                     const maxWindSpeed = 150; // knots, example max jet stream speed
                     // Wind effect is stronger when aligned with directionX and in the core of the jet stream
                      const windStrengthFactor = Math.max(0, 1 - Math.abs(segmentMidY - (jetStreamLatBandY[0] + jetStreamLatBandY[1])/2) / (jetStreamLatBandY[1] - jetStreamLatBandY[0]) * 2); // Strongest in the middle of the band

                     const effectiveWindKnots = (windComponent / pathCanvas.width) * maxWindSpeed * windStrengthFactor; // Scale wind effect by how "eastward" the segment is relative to map width

                     currentAirspeedKnots += effectiveWindKnots; // Add/subtract wind component
                 }
            }

            // Weather Effect (Turbulence/Storms: reduce comfort, slight speed penalty)
            const weatherLayerActive = atlanticMap.querySelector('.weather-layer').classList.contains('active');
            const weatherZoneXRange = [atlanticMap.offsetWidth * 0.5, atlanticMap.offsetWidth * 0.8];
            const weatherZoneYRange = [atlanticMap.offsetHeight * 0.6, atlanticMap.offsetHeight * 0.9]; // Example: South-East Atlantic
            const isInWeatherZone = (segmentMidX >= weatherZoneXRange[0] && segmentMidX <= weatherZoneXRange[1] && segmentMidY >= weatherZoneYRange[0] && segmentMidY <= weatherZoneYRange[1]);

            if (weatherLayerActive && isInWeatherZone) {
                segmentComfort -= (segmentDistancePixels / 5); // Reduce comfort score
                currentAirspeedKnots *= 0.98; // Small speed penalty
                 if (!warnings.includes("עבר באזור מזג אוויר קשה")) warnings.push("עבר באזור מזג אוויר קשה");
            }


            // Restricted Area Effect (Avoidance/Delay: time penalty)
            const restrictedLayerActive = atlanticMap.querySelector('.restricted-layer').classList.contains('active');
             const restrictedZoneXRange = [atlanticMap.offsetWidth * 0.75, atlanticMap.offsetWidth * 0.95];
             const restrictedZoneYRange = [atlanticMap.offsetHeight * 0.05, atlanticMap.offsetHeight * 0.25]; // Example: North-East Atlantic
             const isInRestrictedZone = (segmentMidX >= restrictedZoneXRange[0] && segmentMidX <= restrictedZoneXRange[1] && segmentMidY >= restrictedZoneYRange[0] && segmentMidY <= restrictedZoneYRange[1]);

            if (restrictedLayerActive && isInRestrictedZone) {
                 currentAirspeedKnots *= 0.8; // Simulate delay/detour time penalty
                 if (!warnings.includes("עבר באזור מוגבל (עיכוב)")) warnings.push("עבר באזור מוגבל (עיכוב)");
            }

            // Ensure speed is positive
            if (currentAirspeedKnots <= 0) currentAirspeedKnots = 50; // Minimum speed

            // Time and Fuel calculation for the segment
            const segmentTimeHours = (segmentDistanceNm / currentAirspeedKnots); // Time in hours
            totalTime += segmentTimeHours;

             // Fuel burn slightly increases with lower speed/higher drag (simplified: base burn + penalty for deviation from base speed)
             const segmentFuel = segmentDistanceNm * fuelBurnRate * (baseAirspeedKnots / currentAirspeedKnots);
            totalFuel += segmentFuel;

            comfortScore += segmentComfort; // Apply comfort penalty


            // --- Animate plane movement for the segment ---
            const segmentDurationSec = segmentTimeHours * 30; // Scale time for animation speed (e.g., 30 seconds per hour)
            planeIcon.style.transition = `left ${segmentDurationSec}s linear, top ${segmentDurationSec}s linear, transform 0.5s ease`;
            planeIcon.style.left = p2.x + 'px';
            planeIcon.style.top = p2.y + 'px';
             planeIcon.style.transform = `translate(-50%, -50%) rotate(${planeRotation}deg)`;


            // Wait for the animation segment to finish
            await new Promise(resolve => setTimeout(resolve, segmentDurationSec * 1000));
        }

        // Ensure comfort score doesn't drop below 0
        comfortScore = Math.max(0, comfortScore);

        // Calculate Score (example formula)
        // Base score + Wind bonus - Time penalty - Fuel penalty - Comfort penalty - Restricted penalty
        let simulationScore = 2000; // Starting score
        simulationScore -= totalTime * 50; // Penalize for time (50 points per hour)
        simulationScore -= totalFuel * 0.5; // Penalize for fuel (0.5 points per fuel unit)
        simulationScore -= (100 - comfortScore) * 10; // Penalize for low comfort (10 points per point below 100)
         if (warnings.includes("עבר באזור מוגבל (עיכוב)")) simulationScore -= 200; // Penalty for hitting restricted area

         simulationScore = Math.max(0, simulationScore); // Score cannot be negative

        // Display results
        const resultsHTML = `
            <p>✅ <strong>סימולציה הושלמה!</strong></p>
            <p>📏 <strong>מרחק כולל:</strong> ${totalDistance.toFixed(0)} מייל ימי</p>
            <p>⏱️ <strong>זמן טיסה:</strong> ${totalTime.toFixed(1)} שעות</p>
            <p>⛽ <strong>צריכת דלק:</strong> ${totalFuel.toFixed(0)} יחידות</p>
            <p>😊 <strong>נוחות הנוסעים:</strong> ${comfortScore.toFixed(0)}/100</p>
            <p>⭐ <strong>ניקוד ביצועים:</strong> ${simulationScore.toFixed(0)} נקודות</p>
             ${warnings.length > 0 ? `<p style='color: orange; margin-top: 10px;'><strong>אזהרות:</strong> ${warnings.join(', ')}</p>` : ''}
        `;
        currentResultsDiv.innerHTML = resultsHTML;

        // Add to comparison
        comparisonResults.push({
             pathPoints: pathPoints.slice(), // Save a copy of the path
            distance: totalDistance,
            time: totalTime,
            fuel: totalFuel,
            comfort: comfortScore,
            score: simulationScore,
             layers: Array.from(layerToggles).filter(cb => cb.checked).map(cb => cb.parentElement.textContent.trim()),
             warnings: warnings.slice()
        });

         updateComparisonResultsDisplay();

        simulationRunning = false;
         planeIcon.style.display = 'none'; // Hide plane after simulation
    }

     function updateComparisonResultsDisplay() {
         const comparisonContainer = comparisonResultsDiv;
         comparisonContainer.innerHTML = '<h4>השוואת נתיבים קודמים:</h4>'; // Clear previous
         if (comparisonResults.length === 0) {
             comparisonContainer.innerHTML += '<p class="no-results">עוד לא הרצת סימולציות להשוואה.</p>';
             return;
         }

         // Sort results by score (highest first)
         const sortedResults = [...comparisonResults].sort((a, b) => b.score - a.score);

         sortedResults.forEach((result, index) => {
             const entry = document.createElement('div');
             entry.innerHTML = `
                 <h4>נתיב ${comparisonResults.indexOf(result) + 1} <span style="font-size: 0.8em; color: #555;">(ציון: ${result.score.toFixed(0)})</span>:</h4>
                 <p>📏 מרחק: ${result.distance.toFixed(0)} מייל ימי</p>
                 <p>⏱️ זמן: ${result.time.toFixed(1)} שעות</p>
                 <p>⛽ דלק: ${result.fuel.toFixed(0)} יחידות</p>
                 <p>😊 נוחות: ${result.comfort.toFixed(0)}/100</p>
                  ${result.warnings.length > 0 ? `<p style='color: orange; font-size: 0.9em; margin-top: 5px;'>⚠️ ${result.warnings.join(', ')}</p>` : ''}
                 <p style="font-size: 0.8em; color: #666;"><em>(שכבות פעילות: ${result.layers.join(', ') || 'אף שכבה'})</em></p>
             `;
             comparisonContainer.appendChild(entry);
         });
     }


    // Event Listeners
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationDiv.style.opacity = isHidden ? 1 : 0; // Fade effect
         if (!isHidden) { // Fade out before hiding completely
             setTimeout(() => { explanationDiv.style.display = 'none'; }, 500);
         }

        explanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג הסבר מעמיק: להיות נווט טרנס-אטלנטי';
    });

    layerToggles.forEach(toggle => {
        toggle.addEventListener('change', (event) => {
            const layerName = event.target.dataset.layer;
            const layerElement = atlanticMap.querySelector(`.${layerName}-layer`);
            if (event.target.checked) {
                layerElement.classList.add('active');
            } else {
                layerElement.classList.remove('active');
            }
        });
    });

    clearPathBtn.addEventListener('click', () => {
         if (simulationRunning) return;
        pathPoints = [];
        redrawPath();
        currentResultsDiv.innerHTML = "<p>שרטט נתיב והרץ סימולציה...</p>";
         comparisonResults = []; // Clear comparison results
         updateComparisonResultsDisplay();
         planeIcon.style.display = 'none'; // Hide plane
    });

    runSimulationBtn.addEventListener('click', runSimulation);

    // Initial setup
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas(); // Initial canvas size and point positioning
    updateComparisonResultsDisplay(); // Initialize comparison display
</script>
```