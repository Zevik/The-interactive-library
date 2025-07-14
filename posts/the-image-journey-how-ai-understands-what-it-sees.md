---
title: "המסע הויזואלי של בינה מלאכותית: מפיקסלים להבנה עמוקה"
english_slug: the-image-journey-how-ai-understands-what-it-sees
category: "בינה מלאכותית"
tags:
  - בינה מלאכותית
  - למידה עמוקה
  - ראייה ממוחשבת
  - רשתות נוירונים
  - זיהוי תמונה
---
# המסע הויזואלי של בינה מלאכותית: מפיקסלים להבנה עמוקה

דמיינו רגע: אתם מביטים בתמונה ומייד מזהים חתול, בית, או מכונית. זה קורה בטבעיות מדהימה! אבל איך מחשב, שמבחינתו תמונה היא רק רשת אינסופית של מספרים, מצליח להגיע לאותה רמת הבנה? בואו נצא למסע קסום ונחקור את "העיניים" של הבינה המלאכותית, ואיך תמונה עוברת טרנספורמציה משכבה לשכבה בתוך רשת נוירונים, עד שהיא הופכת מידע גולמי לתובנה.

<div class="interactive-app">
    <h2>צאו למסע: בחרו תמונה וצפו בה עוברת את "המסננים" של הרשת:</h2>
    <div class="image-selection">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Simple_House_Image_example.svg/120px-Simple_House_Image_example.svg.png" data-image-key="house" alt="בית פשוט" class="thumbnail">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_Cafe_Cat_1.jpg/120px-Cat_Cafe_Cat_1.jpg" data-image-key="cat" alt="ראש של חתול" class="thumbnail">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Simple_car_image.svg/120px-Simple_car_image.svg.png" data-image-key="car" alt="מכונית פשוטה" class="thumbnail">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Number_3.svg/120px-Number_3.svg.png" data-image-key="three" alt="הספרה 3" class="thumbnail">
    </div>

    <div class="processing-area">
        <div class="selected-image">
            <h3>הקלט לרשת:</h3>
            <img id="current-image" src="" alt="תמונה נבחרת" style="display: none;">
            <p id="image-placeholder">בחרו תמונה מהגלריה למעלה כדי להתחיל את המסע שלה!</p>
        </div>

        <div class="network-visualization">
            <h3>מסלול ה"מחשבה" בשכבות:</h3>
            <div id="layers-display" class="layers-display">
                <div class="layer" data-layer="input">קלט</div>
                <div class="arrow">→</div>
                <div class="layer" data-layer="conv1">שכבת מאפיינים 1 (קווים/צורות בסיס)</div>
                <div class="arrow">→</div>
                <div class="layer" data-layer="pool1">Pooling 1 (סינון והפשטה)</div>
                 <div class="arrow">→</div>
                <div class="layer" data-layer="conv2">שכבת מאפיינים 2 (צורות מורכבות)</div>
                 <div class="arrow">→</div>
                <div class="layer" data-layer="pool2">Pooling 2 (סינון והפשטה)</div>
                 <div class="arrow">→</div>
                <div class="layer" data-layer="fc1">שכבת חיבור (שילוב מאפיינים)</div>
                 <div class="arrow">→</div>
                <div class="layer" data-layer="output">פלט (החלטה סופית)</div>
            </div>
             <div class="layer-navigation">
                <button id="prev-layer" disabled>← קודמת</button>
                <button id="next-layer" disabled>הבאה →</button>
            </div>
        </div>

        <div class="layer-output-visualization">
            <h3>ה"מבט" של הרשת בשכבה <span id="current-layer-name">...</span>:</h3>
            <div id="output-content">
                <p class="placeholder-text">כשתבחרו תמונה ותתקדמו בשכבות, תראו כאן מה הרשת "רואה" או "חושבת" בכל שלב.</p>
                <!-- Content for different layers will be injected here -->
            </div>
        </div>
    </div>
</div>

<button id="toggle-explanation">רוצים להבין לעומק? לחצו כאן להסבר מורחב</button>

<div id="explanation" style="display: none;">
    <h2>המסע מאחורי הקלעים: איך מחשב באמת "רואה"?</h2>

    <h3>תמונה בעיני מכונה: לא ציור, אלא מטריצה של מספרים</h3>
    <p>בניגוד לנו, שתופסים תמונה כיחידה ויזואלית אחת, מחשב "רואה" אותה כאוסף עצום של נקודות צבע זעירות - פיקסלים. כל פיקסל מיוצג על ידי קבוצת מספרים המציינים את ערכי הצבע שלו (לרוב אדום, ירוק, כחול - RGB). כך, תמונה דיגיטלית היא למעשה טבלה ענקית (או "מטריצה") של מספרים.</p>

    <h3>רשתות נוירונים: מבנה חישובי בהשראת המוח</h3>
    <p>רשת נוירונים מלאכותית היא ניסיון לחקות את פעולת המוח האנושי באופן חישובי. היא בנויה מ"נוירונים" וירטואליים, המחוברים זה לזה ב"שכבות". המידע (במקרה שלנו, ערכי הפיקסלים) זורם משכבת הקלט דרך שכבות נסתרות ועד שכבת הפלט שמספקת את התוצאה הסופית (למשל, זיהוי האובייקט). כל חיבור בין נוירונים מקבל "משקל" מספרי, שנקבע בתהליך האימון. הנוירונים מבצעים חישובים פשוטים (סכום משוקלל של הקלטים) ומעבירים את התוצאה הלאה.</p>

    <h3>למידה עמוקה: כוחן של שכבות רבות</h3>
    <p>המונח "למידה עמוקה" מתייחס לרשתות נוירונים עם מספר רב של שכבות נסתרות. העומק הזה מאפשר לרשת ללמוד ולבנות ייצוגים מורכבים יותר ויותר של הנתונים. חשבו על זה כעל בניין קומות: הקומה התחתונה מזהה מאפיינים מאוד בסיסיים (קווים, פינות). הקומה שמעליה משלבת קווים ופינות אלו כדי לזהות צורות פשוטות (עיגולים, ריבועים). הקומות העליונות יותר משלבות את הצורות הללו כדי לזהות חלקים של אובייקטים (גלגל, אוזן, גג), והשכבה האחרונה משלבת את חלקי האובייקטים כדי לזהות את האובייקט כולו. היררכיית זיהוי זו היא המפתח ל"ראייה" של בינה מלאכותית.</p>

    <h3>CNNs: המומחים לזיהוי תמונה</h3>
    <p>רשתות נוירונים קונבולוציה (Convolutional Neural Networks - CNNs) הן הארכיטקטורה הסטנדרטית למשימות ראייה ממוחשבת, וההדמיה כאן מבוססת עליהן. אלו המרכיבים העיקריים שראיתם בהדמיה:</p>
    <ul>
        <li>**שכבות קונבולוציה (Convolutional Layers):** אלו השכבות שמבצעות את "זיהוי המאפיינים" הראשוני. הן עוברות על התמונה עם "פילטרים" קטנים (מעין משקפיים קטנות שמחפשות משהו ספציפי, כמו קו אלכסוני או נקודה בהירה). כל פילטר יוצר "מפת מאפיינים" חדשה שמראה איפה הוא מצא את מה שהוא חיפש בתמונה המקורית. בשכבות הראשונות הפילטרים מחפשים מאפיינים פשוטים, ובהמשך מאפיינים מורכבים יותר.</li>
        <li>**שכבות Pooling:** תפקידן הוא לסנן ולהקטין את מפות המאפיינים. הן שומרות רק את המידע החשוב ביותר מכל אזור קטן (למשל, את הערך המקסימלי) וזורקות את השאר. זה עוזר לרשת להיות פחות רגישה לשינויים קטנים במיקום האובייקט בתמונה, ומפחית את כמות המידע לעיבוד.</li>
        <li>**שכבות Fully Connected:** לאחר שמפות המאפיינים עברו סינון והפשטה, המידע מגיע לשכבות ה-Fully Connected. כאן, כל נוירון מחובר לכל נוירון בשכבה הקודמת. שכבות אלו לוקחות את כל המאפיינים המופשטים שזוהו ומבצעות את ההחלטה הסופית: איזה אובייקט נמצא בתמונה, ועם איזו הסתברות.</li>
    </ul>

    <h3>אימון הרשת: הדרך ל"ללמוד לראות"</h3>
    <p>רשת נוירונים לא "רואה" נכון מהרגע הראשון. היא עוברת תהליך אימון: מראים לה מיליוני תמונות עם התשובות הנכונות (למשל, "זו תמונה של חתול"). הרשת מנסה לנחש, ואם היא טועה, היא "מתקנת" את המשקלים הפנימיים שלה כדי שבפעם הבאה היא תטעה פחות. התהליך הזה חוזר על עצמו שוב ושוב עד שהרשת מגיעה לרמת דיוק גבוהה.</p>

    <h3>לסיכום: מסע של הפשטה ובניית ייצוגים</h3>
    <p>כפי שראיתם בהדמיה, המסע של התמונה ברשת הוא תהליך הדרגתי: ממידע גולמי ומפורט (פיקסלים), דרך זיהוי מאפיינים פשוטים (קווים), בנייתם למאפיינים מורכבים (צורות), ועד לשילוב כל אלו להחלטה סופית. זהו כוחה של הלמידה העמוקה בראייה ממוחשבת!</p>
</div>

<style>
    /* כללי ופונטים */
    .interactive-app, #explanation {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        margin: 20px auto;
        padding: 25px;
        border: none; /* Modern look, remove border */
        border-radius: 12px; /* More rounded corners */
        max-width: 900px;
        background-color: #ffffff; /* Clean white background */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* Softer, larger shadow */
        line-height: 1.6; /* Improved readability */
    }

    .interactive-app h2, .interactive-app h3, #explanation h2, #explanation h3 {
        text-align: center; /* Center titles */
        color: #333;
        margin-bottom: 15px;
    }
    #explanation h2, #explanation h3 {
         text-align: right; /* Align explanation titles right */
    }

    /* גלריית תמונות */
    .image-selection {
        text-align: center;
        margin-bottom: 30px; /* More space below thumbnails */
        padding-bottom: 20px;
        border-bottom: 1px solid #eee;
    }

    .thumbnail {
        width: 90px; /* Slightly larger thumbnails */
        height: 90px;
        object-fit: cover;
        margin: 0 8px; /* More space around thumbnails */
        border: 3px solid transparent; /* Thicker border */
        border-radius: 8px; /* Rounded corners for images */
        cursor: pointer;
        transition: all 0.3s ease-in-out; /* Smooth transitions */
        vertical-align: middle;
        opacity: 0.7; /* Slightly dim when not selected */
    }

    .thumbnail:hover {
        border-color: #007bff; /* Highlight on hover */
        transform: translateY(-3px); /* Subtle lift effect */
        opacity: 1; /* Full opacity on hover */
    }

    .thumbnail.selected {
        border-color: #28a745; /* Green border for selected */
        box-shadow: 0 0 8px rgba(40, 167, 69, 0.4); /* Green glow */
        transform: scale(1.05); /* Slight zoom effect */
        opacity: 1; /* Full opacity when selected */
    }

    /* אזור עיבוד (Flexbox) */
    .processing-area {
        display: flex;
        flex-wrap: wrap;
        gap: 25px; /* Increased gap */
        justify-content: center;
        align-items: stretch; /* Make items stretch to fill height if needed */
    }

    .selected-image,
    .network-visualization,
    .layer-output-visualization {
        background-color: #f9f9f9; /* Light grey background for sections */
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #e0e0e0; /* Lighter border */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05); /* Inner shadow for depth */
        display: flex; /* Use flexbox for internal layout */
        flex-direction: column;
    }

    .selected-image {
        flex-basis: 180px; /* Wider size for image */
        flex-shrink: 0; /* Prevent shrinking */
        text-align: center;
        align-items: center; /* Center content vertically */
        justify-content: center; /* Center content horizontally */
    }

    #current-image {
        max-width: 100%;
        height: auto;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        transition: opacity 0.5s ease; /* Smooth fade in */
    }

    #image-placeholder {
        font-style: italic;
        color: #888; /* Softer color */
        text-align: center;
        min-height: 100px; /* Maintain more space */
        display: flex;
        align-items: center;
        justify-content: center;
        flex-grow: 1; /* Allow placeholder to fill space */
    }

    .network-visualization {
        flex-grow: 1; /* Allows network vis to take available space */
        min-width: 300px; /* Ensure minimum width */
        text-align: center;
        justify-content: space-between; /* Push navigation to bottom */
    }

    .layers-display {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 8px 12px; /* Increased gap, different horizontal/vertical */
        margin-bottom: 15px;
        flex-grow: 1; /* Allow layers to take vertical space */
        align-content: center; /* Center items if they wrap */
    }

    .layer {
        background-color: #cfe2ff; /* Light blue, softer */
        color: #084298; /* Dark blue text */
        padding: 10px 15px; /* More padding */
        border-radius: 25px; /* More rounded, pill shape */
        font-size: 0.95em;
        cursor: pointer;
        transition: all 0.3s ease;
        white-space: nowrap;
        border: 1px solid transparent;
    }

    .layer:hover {
        background-color: #a0caff; /* Lighter blue on hover */
        border-color: #0d6efd; /* Blue border on hover */
    }

    .layer.active {
        background-color: #d1e7dd; /* Light green for active */
        color: #0f5132; /* Dark green text */
        border-color: #198754; /* Green border */
        transform: scale(1.05); /* Slight zoom */
        box-shadow: 0 0 10px rgba(40, 167, 69, 0.3); /* Green glow */
    }

     .arrow {
        font-size: 1.5em; /* Larger arrows */
        color: #999; /* Softer color */
         font-weight: bold;
    }

    .layer-navigation {
        margin-top: 15px;
        text-align: center;
    }

    .layer-navigation button {
        margin: 0 8px; /* More space */
        padding: 10px 20px; /* Larger buttons */
        font-size: 1em;
        cursor: pointer;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #f0f0f0;
        transition: all 0.3s ease;
        min-width: 120px; /* Fixed width for buttons */
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    .layer-navigation button:hover:not(:disabled) {
        background-color: #e0e0e0;
        border-color: #bbb;
         box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }

    .layer-navigation button:active:not(:disabled) {
        background-color: #d5d5d5;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1); /* Pressed effect */
        transform: translateY(1px);
    }

    .layer-navigation button:disabled {
        opacity: 0.4; /* More faded when disabled */
        cursor: not-allowed;
         box-shadow: none;
         transform: none;
    }

    /* ויזואליזציית פלט השכבה */
    .layer-output-visualization {
         flex-basis: 100%; /* Takes full width below network vis */
        min-height: 250px; /* Ensure ample space */
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

     #current-layer-name {
         color: #007bff; /* Highlight layer name in title */
         font-weight: bold;
     }

    #output-content {
        margin-top: 10px;
        border: 2px dashed #d0d0d0; /* Clearer boundary */
        border-radius: 8px;
        padding: 15px;
        min-height: 180px;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        box-sizing: border-box;
        background-color: #fafafa;
        overflow: hidden; /* Hide overflow, use scroll for specific content types */
        position: relative; /* Needed for potential absolute positioning inside */
         transition: opacity 0.5s ease; /* Fade effect on content switch */
    }
    #output-content.loading {
         opacity: 0.5;
         pointer-events: none; /* Prevent clicks while loading */
    }


    #output-content img {
        max-width: 100%;
        max-height: 300px;
        object-fit: contain;
        border: 1px solid #eee;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .feature-map-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(40px, 1fr)); /* Larger grid cells */
        gap: 6px; /* More space */
        width: 100%;
        max-width: 500px; /* Wider grid */
        margin-top: 10px; /* Space below title */
        overflow-y: auto; /* Allow scrolling if many feature maps */
        max-height: 200px; /* Limit grid height */
        padding-right: 5px; /* Space for scrollbar */
    }

    .feature-map-cell {
        width: 100%;
        padding-top: 100%; /* Maintain square aspect ratio */
        position: relative;
        background: linear-gradient(45deg, #eee, #ddd); /* Simple gradient */
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
        overflow: hidden;
        display: flex; /* For centering potential content */
        align-items: center;
        justify-content: center;
    }
    /* Add a subtle pattern hint */
    .feature-map-cell::after {
        content: '';
        display: block;
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-image: radial-gradient(#fff 10%, transparent 10%), radial-gradient(#fff 10%, transparent 10%);
        background-size: 12px 12px;
        background-position: 0 0, 6px 6px;
        opacity: 0.1; /* Subtle visual cue */
    }
    .feature-map-cell img {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         object-fit: cover;
     }

    /* Description for Grid/FC */
    .layer-description {
        margin-top: 10px;
        font-size: 0.9em;
        color: #555;
        font-style: italic;
        text-align: center;
        width: 100%;
    }


    /* Classification Results (Bar Chart) */
     .classification-results {
         width: 100%;
         max-width: 450px; /* Wider result area */
         margin: 10px auto;
         text-align: left;
         padding-top: 10px; /* Space above results */
     }

    .classification-item {
        display: flex; /* Arrange label and bar side-by-side */
        align-items: center;
        margin-bottom: 12px; /* Space between items */
        font-size: 1.1em;
    }

     .classification-item strong {
         flex-basis: 120px; /* Fixed width for class name */
         flex-shrink: 0;
         margin-left: 15px; /* Space between name and bar */
         color: #333;
     }

    .probability-bar {
        flex-grow: 1; /* Bar takes remaining space */
        height: 20px; /* Bar height */
        background-color: #28a745; /* Green color for bars */
        border-radius: 4px;
        text-align: right;
        line-height: 20px;
        color: white;
        font-weight: bold;
        padding-left: 8px;
        box-sizing: border-box;
        overflow: hidden; /* Hide text if bar is too short */
        transition: width 0.8s ease-out; /* Animate bar width */
        min-width: 2%; /* Ensure tiny bars are visible */
    }

    .placeholder-text {
        color: #888;
        font-style: italic;
        text-align: center;
    }


    /* כפתור הסבר */
    #toggle-explanation {
        display: block;
        margin: 30px auto; /* More space around button */
        padding: 12px 25px; /* Larger button */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        background-color: #007bff;
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3); /* Blue shadow */
    }

    #toggle-explanation:hover {
        background-color: #0056b3;
         box-shadow: 0 4px 10px rgba(0, 123, 255, 0.4);
    }
     #toggle-explanation:active {
         background-color: #004085;
         transform: translateY(1px); /* Pressed effect */
          box-shadow: 0 2px 5px rgba(0, 123, 255, 0.3);
     }


    /* אזור הסבר */
    #explanation {
        margin-top: 20px;
        padding: 25px;
        border: none;
        border-radius: 12px;
        background-color: #f8f9fa; /* Very light background */
        direction: rtl;
        text-align: right;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* Softer shadow */
    }

    #explanation ul {
        margin-top: 15px;
        padding-right: 25px; /* Increased padding */
    }

     #explanation li {
         margin-bottom: 10px; /* More space between list items */
         line-height: 1.5;
     }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .processing-area {
            flex-direction: column; /* Stack elements vertically */
            align-items: center;
        }

        .selected-image,
        .network-visualization,
        .layer-output-visualization {
            width: 100%; /* Full width on smaller screens */
            flex-basis: auto; /* Auto size */
            min-width: auto;
        }

         .thumbnail {
             width: 70px;
             height: 70px;
         }

         .layers-display {
             flex-direction: row; /* Keep layers horizontal flow */
             justify-content: center;
         }

        .layer {
            font-size: 0.85em;
            padding: 8px 10px;
        }

         .arrow {
             font-size: 1.2em;
         }

         .feature-map-grid {
             grid-template-columns: repeat(auto-fit, minmax(30px, 1fr)); /* Smaller cells on mobile */
             gap: 4px;
             max-width: 100%;
         }

         .classification-item {
             flex-direction: column; /* Stack label and bar */
             align-items: flex-start;
         }
         .classification-item strong {
             margin-left: 0;
             margin-bottom: 5px;
         }
         .probability-bar {
             width: 100% !important; /* Let JS control width based on parent */
             text-align: center;
         }
         .classification-results {
             max-width: 100%;
         }
    }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const thumbnails = document.querySelectorAll('.thumbnail');
        const currentImage = document.getElementById('current-image');
        const imagePlaceholder = document.getElementById('image-placeholder');
        const layersDisplay = document.getElementById('layers-display');
        const layerElements = layersDisplay.querySelectorAll('.layer');
        const outputContent = document.getElementById('output-content');
        const currentLayerNameSpan = document.getElementById('current-layer-name');
        const prevLayerButton = document.getElementById('prev-layer');
        const nextLayerButton = document.getElementById('next-layer');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        let currentImageKey = null;
        let currentLayerIndex = -1; // -1 means no image selected or before first layer

        // --- Simulated Data ---
        // Store simulated outputs for each image and layer
        // In a real app, this would be computed by a model
        // Added more descriptive names matching the UI layers
        const simulatedOutputs = {
            house: {
                input: { type: 'image', src: 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Simple_House_Image_example.svg/250px-Simple_House_Image_example.svg.png', name: 'קלט' },
                'conv1': { type: 'grid', count: 8, description: 'זיהוי קווים, פינות ומאפיינים בסיסיים', name: 'שכבת מאפיינים 1' }, // Simulate 8 feature maps
                'pool1': { type: 'grid', count: 8, description: 'הקטנת מימדים וסינון רעשים (קווים)', name: 'Pooling 1' },
                'conv2': { type: 'grid', count: 16, description: 'זיהוי צורות פשוטות יותר (חלון, גג)', name: 'שכבת מאפיינים 2' }, // Simulate 16 feature maps
                'pool2': { type: 'grid', count: 16, description: 'הקטנת מימדים וסינון רעשים (צורות)', name: 'Pooling 2' },
                'fc1': { type: 'text', content: 'הנתונים עובדו לייצוג מופשט, מוכנים לסיווג', name: 'שכבת חיבור' }, // Abstract representation
                output: { type: 'classification', probabilities: { 'בית': 0.95, 'מכונית': 0.02, 'חתול': 0.01, 'ספרה': 0.00 }, name: 'פלט' }
            },
            cat: {
                input: { type: 'image', src: 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_Cafe_Cat_1.jpg/250px-Cat_Cafe_Cat_1.jpg', name: 'קלט' },
                'conv1': { type: 'grid', count: 8, description: 'זיהוי קווים, נקודות וטקסטורות פרווה', name: 'שכבת מאפיינים 1' },
                'pool1': { type: 'grid', count: 8, description: 'הקטנת מימדים וסינון רעשים (קווים/טקסטורות)', name: 'Pooling 1' },
                'conv2': { type: 'grid', count: 16, description: 'זיהוי מאפייני פנים (עיניים, אוזניים, אף)', name: 'שכבת מאפיינים 2' },
                'pool2': { type: 'grid', count: 16, description: 'הקטנת מימדים וסינון רעשים (מאפייני פנים)', name: 'Pooling 2' },
                 'fc1': { type: 'text', content: 'הנתונים עובדו לייצוג מופשט, מוכנים לסיווג', name: 'שכבת חיבור' },
                output: { type: 'classification', probabilities: { 'חתול': 0.98, 'בית': 0.00, 'מכונית': 0.01, 'ספרה': 0.00 }, name: 'פלט' }
            },
             car: {
                input: { type: 'image', src: 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Simple_car_image.svg/250px-Simple_car_image.svg.png', name: 'קלט' },
                'conv1': { type: 'grid', count: 8, description: 'זיהוי קווים אופקיים, אנכיים ומעוגלים', name: 'שכבת מאפיינים 1' },
                'pool1': { type: 'grid', count: 8, description: 'הקטנת מימדים וסינון רעשים (קווים)', name: 'Pooling 1' },
                'conv2': { type: 'grid', count: 16, description: 'זיהוי גלגלים, חלונות וצורת הרכב הכללית', name: 'שכבת מאפיינים 2' },
                'pool2': { type: 'grid', count: 16, description: 'הקטנת מימדים וסינון רעשים (גלגלים/צורות)', name: 'Pooling 2' },
                 'fc1': { type: 'text', content: 'הנתונים עובדו לייצוג מופשט, מוכנים לסיווג', name: 'שכבת חיבור' },
                output: { type: 'classification', probabilities: { 'מכונית': 0.96, 'בית': 0.01, 'חתול': 0.01, 'ספרה': 0.00 }, name: 'פלט' }
            },
            three: {
                input: { type: 'image', src: 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Number_3.svg/250px-Number_3.svg.png', name: 'קלט' },
                'conv1': { type: 'grid', count: 8, description: 'זיהוי קווים מעוגלים וקשתות', name: 'שכבת מאפיינים 1' },
                'pool1': { type: 'grid', count: 8, description: 'הקטנת מימדים וסינון רעשים (קשתות)', name: 'Pooling 1' },
                'conv2': { type: 'grid', count: 16, description: 'זיהוי שילוב קשתות היוצר את הספרה 3', name: 'שכבת מאפיינים 2' },
                'pool2': { type: 'grid', count: 16, description: 'הקטנת מימדים וסינון רעשים (ספרה)', name: 'Pooling 2' },
                 'fc1': { type: 'text', content: 'הנתונים עובדו לייצוג מופשט, מוכנים לסיווג', name: 'שכבת חיבור' },
                output: { type: 'classification', probabilities: { 'ספרה': 0.99, 'בית': 0.00, 'מכונית': 0.00, 'חתול': 0.00 }, name: 'פלט' }
            }
        };

        const layerKeys = Object.keys(simulatedOutputs.house); // Assuming same layers for all images

        // --- Functions ---

        function selectImage(imageKey) {
            if (currentImageKey === imageKey) {
                 // If already selected, do nothing
                 return;
             }
            currentImageKey = imageKey;
            const imageData = simulatedOutputs[imageKey];

            // Update selected thumbnail style
            thumbnails.forEach(thumb => {
                if (thumb.dataset.imageKey === imageKey) {
                    thumb.classList.add('selected');
                } else {
                    thumb.classList.remove('selected');
                }
            });

            // Display selected image with animation
            currentImage.style.opacity = 0; // Start fade out
             setTimeout(() => { // Wait for fade out
                currentImage.src = imageData.input.src;
                currentImage.style.display = 'block';
                imagePlaceholder.style.display = 'none';
                 currentImage.style.opacity = 1; // Fade in
            }, 300);


            // Reset to input layer and update display
            currentLayerIndex = 0;
            updateLayerDisplay();
            updateNavigationButtons();
        }

        function updateLayerDisplay() {
             outputContent.classList.add('loading'); // Add loading class for animation
            if (currentImageKey === null || currentLayerIndex === -1) {
                outputContent.innerHTML = '<p class="placeholder-text">בחרו תמונה והתחילו את המסע.</p>';
                 currentLayerNameSpan.textContent = '...';
                 layerElements.forEach(layer => layer.classList.remove('active'));
                 outputContent.classList.remove('loading');
                return;
            }

            // Highlight active layer in the network visualization
            layerElements.forEach((layer, index) => {
                if (index === currentLayerIndex) {
                    layer.classList.add('active');
                } else {
                    layer.classList.remove('active');
                }
            });

            // Get the current layer key and data
            const currentLayerKey = layerKeys[currentLayerIndex];
            const layerData = simulatedOutputs[currentImageKey][currentLayerKey];

            // Update the layer name span
            currentLayerNameSpan.textContent = layerData.name;

            // Update the output visualization area
            outputContent.innerHTML = ''; // Clear previous content

             // Add description below the title for relevant layers
             if (layerData.description) {
                  const descriptionDiv = document.createElement('div');
                  descriptionDiv.className = 'layer-description';
                  descriptionDiv.textContent = layerData.description;
                  outputContent.appendChild(descriptionDiv);
             }


            if (layerData.type === 'image') {
                const img = document.createElement('img');
                img.src = layerData.src;
                img.alt = `${layerData.name} output`;
                 outputContent.style.justifyContent = 'center'; // Center image
                 outputContent.style.alignItems = 'center';
                 outputContent.style.display = 'flex';
                 outputContent.appendChild(img);
            } else if (layerData.type === 'grid') {
                const gridDiv = document.createElement('div');
                gridDiv.className = 'feature-map-grid';
                // Simulate feature map appearance - just colored squares or abstract patterns
                for (let i = 0; i < layerData.count; i++) {
                     const cell = document.createElement('div');
                     cell.className = 'feature-map-cell';
                     // Simple color simulation - varies slightly per cell
                     const hue = (i * 45) % 360; // Vary hue more significantly
                     const saturation = 60 + (i % 4) * 5; // Slightly vary saturation
                     const lightness = 50 + (i % 6) * 3; // Slightly vary lightness
                     cell.style.backgroundColor = `hsl(${hue}, ${saturation}%, ${lightness}%)`;
                     cell.title = `${layerData.name} - מפת מאפיין ${i+1}`; // Tooltip
                     // Optional: Add a tiny abstract pattern image if available and suits the layer
                     // const patternImg = document.createElement('img'); patternImg.src = '...'; cell.appendChild(patternImg);
                     gridDiv.appendChild(cell);
                }
                 outputContent.style.justifyContent = 'center'; /* Center grid block */
                 outputContent.style.alignItems = 'flex-start'; /* Start items at top (description first) */
                 outputContent.style.display = 'flex';
                 outputContent.style.flexDirection = 'column';
                 outputContent.appendChild(gridDiv);
            } else if (layerData.type === 'classification') {
                const resultsDiv = document.createElement('div');
                 resultsDiv.className = 'classification-results';
                // Sort probabilities descending
                const sortedProbabilities = Object.entries(layerData.probabilities)
                    .sort(([, a], [, b]) => b - a);

                sortedProbabilities.forEach(([className, probability]) => {
                    const itemDiv = document.createElement('div');
                    itemDiv.className = 'classification-item';

                    const nameSpan = document.createElement('strong');
                    nameSpan.textContent = className;
                    itemDiv.appendChild(nameSpan);

                    const barDiv = document.createElement('div');
                    barDiv.className = 'probability-bar';
                    const percentage = (probability * 100).toFixed(1);
                     // Use a small timeout to trigger CSS transition after element is added
                     setTimeout(() => {
                        barDiv.style.width = `${percentage}%`;
                     }, 50); // Small delay is enough

                    barDiv.textContent = `${percentage}%`;
                    itemDiv.appendChild(barDiv);

                    resultsDiv.appendChild(itemDiv);
                });
                 outputContent.style.justifyContent = 'flex-start'; /* Start items at top */
                 outputContent.style.alignItems = 'center'; /* Center block */
                 outputContent.style.display = 'flex';
                 outputContent.style.flexDirection = 'column';
                 outputContent.appendChild(resultsDiv);
            } else if (layerData.type === 'text') {
                 const textDiv = document.createElement('div');
                 textDiv.textContent = layerData.content;
                 textDiv.style.fontStyle = 'italic';
                 textDiv.style.color = '#555';
                 textDiv.style.textAlign = 'center';
                 textDiv.style.width = '100%';
                 outputContent.style.justifyContent = 'center'; /* Center content */
                 outputContent.style.alignItems = 'center';
                 outputContent.style.display = 'flex';
                 outputContent.appendChild(textDiv);
             }
             else {
                // Default or unsupported type
                outputContent.innerHTML = '<p class="placeholder-text">אין הדמיה זמינה עבור שכבה זו.</p>';
                 outputContent.style.justifyContent = 'center';
                 outputContent.style.alignItems = 'center';
                 outputContent.style.display = 'flex';
            }

            // Remove loading class after content is ready (or with a slight delay)
            setTimeout(() => {
                 outputContent.classList.remove('loading');
            }, 100);

        }

        function updateNavigationButtons() {
            prevLayerButton.disabled = currentLayerIndex <= 0;
            nextLayerButton.disabled = currentLayerIndex >= layerKeys.length - 1;
        }

        function goToNextLayer() {
            if (currentImageKey !== null && currentLayerIndex < layerKeys.length - 1) {
                currentLayerIndex++;
                updateLayerDisplay();
                updateNavigationButtons();
            }
        }

        function goToPreviousLayer() {
            if (currentImageKey !== null && currentLayerIndex > 0) {
                currentLayerIndex--;
                updateLayerDisplay();
                updateNavigationButtons();
            }
        }

        // --- Event Listeners ---

        thumbnails.forEach(thumbnail => {
            thumbnail.addEventListener('click', () => {
                selectImage(thumbnail.dataset.imageKey);
            });
        });

        prevLayerButton.addEventListener('click', goToPreviousLayer);
        nextLayerButton.addEventListener('click', goToNextLayer);

         layerElements.forEach((layer, index) => {
             layer.addEventListener('click', () => {
                 if (currentImageKey !== null) { // Only allow clicking layers if an image is selected
                     if (currentLayerIndex === index) return; // Do nothing if clicking active layer
                     currentLayerIndex = index;
                     updateLayerDisplay();
                     updateNavigationButtons();
                 }
             });
         });

        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            // Use CSS class and transitions for smoother toggle if needed, but display property is simpler
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'רוצים להבין לעומק? לחצו כאן להסבר מורחב';
             // Scroll to explanation when shown
             if (isHidden) {
                 explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
             }
        });

        // Initial state
        updateLayerDisplay(); // Set initial placeholder state
        updateNavigationButtons();
    });
</script>
---
```