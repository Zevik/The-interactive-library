---
title: "מסע התגלית הגדול: בעקבות דרווין והביגל"
english_slug: darwin-beagle-voyage-simulation
category: "ביולוגיה"
tags: [דרווין, ביגל, אבולוציה, ביולוגיה, היסטוריה של המדע, סימולציה, למידה אינטראקטיבית]
---
# מסע התגלית הגדול: בעקבות דרווין והביגל

צא למסע חובק עולם על סיפונה של ה-HMS ביגל, בדיוק כפי שעשה צ'ארלס דרווין הצעיר! חקור יבשות רחוקות ואיי פלא, אסוף תצפיות על עולם הטבע הפראי, ותראה במו עיניך את השונות המדהימה שמניעה את החיים. האם תוכל לגלות את הרמזים שהובילו לתובנה הגדולה ביותר על האבולוציה?

<div id="app-container">
    <div id="map-view" class="view active">
        <h2>בחר יעד: תחנות במסע הביגל</h2>
        <div id="map-area">
            <!-- Enhanced Map Placeholder - suggest a more dynamic or stylized look -->
            <img id="world-map" src="https://via.placeholder.com/900x450/a0c0ff/ffffff/?text=Stylized+World+Map+with+Beagle+Route" alt="מפת עולם עם מסלול ההפלגה של הביגל">
            <!-- Points of interest - data-location matches keys in JS locations object -->
            <!-- Added more descriptive styling and potential future animation hooks -->
            <button class="location-point" style="top: 60%; left: 15%;" data-location="south_america">
                <span class="point-label">חופי דרום אמריקה</span>
            </button>
            <button class="location-point" style="top: 45%; left: 25%;" data-location="galapagos">
                 <span class="point-label">איי גלפגוס</span>
            </button>
            <button class="location-point" style="top: 70%; left: 30%;" data-location="tierra_del_fuego">
                <span class="point-label">טיירה דל פואגו</span>
            </button>
             <!-- Add more points as needed based on a real map -->
             <!-- Example: australia, africa, etc. -->
             <!--
             <button class="location-point" style="top: 65%; left: 75%;" data-location="australia">
                  <span class="point-label">אוסטרליה</span>
             </button>
             -->
        </div>
         <div id="map-stats">
             <p>יעדים שנחקרו: <span id="visited-count">0</span> מתוך <span id="total-locations">0</span></p>
         </div>
        <div id="journal-preview">
            <h3>יומן מסע (תצפיות אחרונות)</h3>
            <div id="journal-entries">לחץ על נקודות במפה כדי לעגון ולהתחיל לחקור את הטבע סביבך.</div>
            <button id="view-journal-btn" class="secondary-button">הצג יומן מלא</button>
        </div>
    </div>

    <div id="shore-view" class="view hidden">
        <h2 id="shore-location-name"></h2>
        <div id="shore-scene">
            <!-- Scene image or representation - Placeholder with more specific alt text -->
            <img id="shore-image" src="https://via.placeholder.com/700x350/c0a080/ffffff/?text=Coastal+Landscape" alt="נוף יבשתי או חופי במיקום הנוכחי">
            <!-- Interactive elements (species, fossils, etc.) - data-location and data-element must match data in JS locations object -->
            <!-- These buttons are static and are shown/hidden by JS based on the selected location -->
            <!-- Added classes for type differentiation (creature, fossil, geology) -->
            <button class="interactive-element element-creature" style="top: 50%; left: 20%;" data-location="galapagos" data-element="finch_galapagos">פינץ' (גלפגוס)</button>
            <button class="interactive-element element-creature" style="top: 65%; left: 40%;" data-location="galapagos" data-element="giant_tortoise">צב גלפגוס ענק</button>
            <button class="interactive-element element-creature" style="top: 70%; left: 60%;" data-location="galapagos" data-element="iguana_marine">איגואנת ים</button>
            <button class="interactive-element element-fossil" style="top: 60%; left: 30%;" data-location="south_america" data-element="fossil_mega">מאובן יונק ענק</button>
            <button class="interactive-element element-creature" style="top: 75%; left: 50%;" data-location="south_america" data-element="finch_mainland">פינץ' (יבשה)</button>
            <button class="interactive-element element-geology" style="top: 80%; left: 70%;" data-location="south_america" data-element="geology_andes">תצורה גאולוגית</button>
            <button class="interactive-element element-creature" style="top: 50%; left: 50%;" data-location="tierra_del_fuego" data-element="penguins">פינגווינים</button>
            <!-- Add more interactive elements as needed for each location -->
        </div>
        <div id="observation-panel" class="hidden">
            <h3>תצפית: <span id="observation-name"></span></h3>
            <p id="observation-description"></p>
            <button id="add-to-journal-btn">הוסף ליומן</button>
            <p id="observation-feedback" class="feedback"></p>
        </div>
        <button id="back-to-map-btn" class="secondary-button">חזור למפה</button>
    </div>

    <div id="journal-view" class="view hidden">
        <h2>יומן מסע - התגליות שלך</h2>
        <div id="full-journal-entries">עוד לא אספת תצפיות. חזור למפה וחקר יעדים חדשים!</div>
        <p class="journal-hint">השווה תצפיות ממיקומים שונים כדי למצוא דפוסים והתאמות. לדוגמה, השווה את מקורי הפינצ'ים מגלפגוס עם אלו מהיבשה, או את שריוני צבי הענק מאיים שונים בגלפגוס (אם הוספו לסימולציה), ואת המאובנים למינים החיים.</p>
        <button id="close-journal-btn" class="secondary-button">סגור יומן</button>
        <!-- Kept back-to-map for consistency, though close does the same here -->
        <!-- <button id="back-to-map-from-journal-btn" class="secondary-button">חזור למפה</button> -->
    </div>

</div>

<button id="toggle-explanation-btn" class="tertiary-button">הצג/הסתר סיפור המסע ורעיון האבולוציה</button>

<div id="explanation" class="hidden">
    <h2>הסבר: מסע הביגל ומשמעותו המדעית הגדולה</h2>

    <h3>מסע הביגל: הרקע ההיסטורי והיציאה למסע</h3>
    <p>תארו לעצמכם מסע ימי שנמשך כמעט חמש שנים! זו הייתה המשימה של ה-HMS ביגל, ספינת מחקר בריטית שיצאה בשנת 1831 למפות את חופי דרום אמריקה. צ'ארלס דרווין, אז רק בן 22 ועם תואר באומנויות אך תשוקה בוערת לטבע, הצטרף למסע כחוקר טבע ללא שכר. הוא ידע שזו הזדמנות של פעם בחיים לאסוף דגימות ולערוך תצפיות שיעשירו את הידע המדעי. הוא לא ידע אז כמה עמוק המסע הזה ישנה את הבנתו - ואת הבנת העולם כולו - על מקור החיים.</p>

    <h3>המסלול הבלתי נשכח ותחנות מפתח</h3>
    <p>הביגל יצאה מאנגליה, חצתה את האוקיינוס האטלנטי ועצרה בברזיל. היא בילתה שנים רבות בחקירה מדוקדקת של חופי ארגנטינה, צ'ילה ופרו. נקודות דרמטיות במסלול כללו את המעבר במצרי מגלן הקפואים בטיירה דל פואגו, והעגינה באיי גלפגוס הגעשיים באוקיינוס השקט. משם המשיכה הביגל מערבה, חצתה את האוקיינוס השקט עם עצירות באי טהיטי וניו זילנד, ביקרה באוסטרליה ובאיים נוספים, חצתה את האוקיינוס ההודי, הקיפה את כף התקווה הטובה בדרום אפריקה וחזרה לאנגליה בשנת 1836. המסע הזה כיסה מרחק עצום וחשף את דרווין למגוון ביולוגי וגיאולוגי עוצר נשימה.</p>

    <h3>תצפיות המפתח ששינו את התמונה: מגלפגוס ועד המאובנים</h3>
    <p>בכל תחנת עגינה, ירד דרווין מהספינה, חקר את הסביבה, אסף אלפי דגימות של צמחים, בעלי חיים ומאובנים, ותיעד הכול ביומניו. התצפיות המפורסמות ביותר, ולימים המשפיעות ביותר, נאספו באיי גלפגוס. באיים שונים, שנפרדים זה מזה במרחק קצר יחסית, הוא מצא מינים קרובים אך שונים להפליא. הפינצ'ים (ציפורי שיר קטנות), לדוגמה, הראו הבדלים בולטים בצורת המקור שלהם מאי לאי – התאמה מושלמת לסוג המזון הזמין בכל אי. גם צבי הענק הראו שוני בצורת השריון בהתאם לצמחייה המקומית. דרווין גם מצא בדרום אמריקה מאובנים של יונקים ענקיים נכחדים (כמו העצלן הענק, מגתריום), שהיו דומים באופן מסתורי ליונקים קטנים יותר שחיים באותם אזורים כיום.</p>

    <h3>התובנות הגדולות: שונות, התאמה ושינוי לאורך זמן</h3>
    <p>מכל אוסף הראיות הזה, החלו להתגבש אצל דרווין מספר רעיונות מכוננים: ראשית, בתוך כל אוכלוסייה של בעלי חיים או צמחים, קיימת שונות טבעית גדולה (לא כל הפרטים זהים). שנית, לעיתים קרובות ישנה התאמה מדהימה בין התכונות של יצור לבין הסביבה בה הוא חי (מקור לפינץ' לאכילת זרעים קשים או חרקים דקים). שלישית, ממצאי המאובנים רמזו לו שמינים אינם קבועים לנצח, אלא משתנים ונכחדים לאורך זמן גיאולוגי ארוך, ושהמינים החיים כיום קשורים למינים שנכחדו בעבר.</p>

    <h3>הברירה הטבעית: המפתח להבנת האבולוציה</h3>
    <p>השילוב של רעיונות השונות וההתאמה, יחד עם תובנות ממדענים אחרים (כמו רעיונותיו של מלתוס על גידול אוכלוסין ותחרות על משאבים, ותצפיותיו העצמאיות של אלפרד ראסל וולאס), הובילו את דרווין לפתח את רעיון "הברירה הטבעית". הוא הבין שפרטים בתוך אוכלוסייה בעלי תכונות שמעניקות להם יתרון קל בסביבה (למשל, מקור יעיל יותר לאכילת מזון זמין) נוטים לשרוד ולהתרבות בהצלחה רבה יותר מאחרים. עם הזמן, תכונות אלו הופכות נפוצות יותר באוכלוסייה. לאורך דורות רבים, הצטברות שינויים קטנים כאלה יכולה להוביל להיווצרות מינים חדשים לגמרי, מותאמים באופן מושלם לסביבתם. זהו מנגנון האבולוציה – השינוי של מינים לאורך זמן.</p>

    <h3>מורשת המסע: מהפכה מדעית</h3>
    <p>מסע הביגל לא היה רק מסע גיאוגרפי חשוב, אלא בעיקר מסע תגלית מדעי ששינה את ההיסטוריה. הוא סיפק לדרווין את הבסיס האמפירי המוצק לבניית תיאוריית האבולוציה באמצעות ברירה טבעית – אחת התיאוריות המרכזיות והמאוששות ביותר בכל המדע המודרני. הסימולציה הזו מאפשרת לך לחוות קמצוץ קטן ממסע התגלית הזה ולראות בעצמך חלק מהראיות שדרווין אסף, שהובילו אותו לתובנות העמוקות ביותר על עולם החי.</p>
</div>

<style>
    /* General Reset and Base Styles */
    #app-container {
        direction: rtl;
        font-family: 'Arial Hebrew', 'David', 'Hebrew', sans-serif; /* More specific Hebrew fonts */
        max-width: 960px; /* Slightly wider container */
        margin: 30px auto; /* More vertical margin */
        border: 1px solid #e0e0e0; /* Lighter border */
        padding: 20px; /* More padding */
        border-radius: 12px; /* More rounded corners */
        background-color: #f8f8f8; /* Slightly darker background */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        overflow: hidden; /* Contains floats/margins */
    }

    h1, h2, h3 {
        color: #333; /* Darker heading color */
        text-align: center; /* Center headings */
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2em;
        margin-bottom: 20px;
        border-bottom: 2px solid #007bff; /* Accent line under main title */
        padding-bottom: 10px;
    }

    h2 {
        font-size: 1.5em;
        color: #0056b3; /* Primary color for subheadings */
    }

    h3 {
        font-size: 1.2em;
        color: #007bff; /* Accent color for panel titles */
    }

    p {
        line-height: 1.7; /* Improved readability */
        color: #555; /* Slightly lighter text */
        margin-bottom: 10px;
    }

    .view {
        margin-bottom: 25px; /* More space between views */
        padding: 15px;
        border: 1px solid #ddd;
        border-radius: 8px;
        background-color: #fff; /* White background for content areas */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05); /* Subtle inner shadow */
        opacity: 1;
        transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out; /* Smooth transitions */
         transform: translateY(0);
    }

    .view.hidden {
        opacity: 0;
        transform: translateY(20px); /* Slide down slightly when hidden */
        pointer-events: none; /* Disable clicks when hidden */
        height: 0; /* Collapse height */
        padding-top: 0;
        padding-bottom: 0;
        margin-top: 0;
        margin-bottom: 0;
        overflow: hidden;
        border-color: transparent;
        box-shadow: none;
    }
     .view.active {
        opacity: 1;
        transform: translateY(0);
        height: auto; /* Allow content height */
        padding: 15px; /* Restore padding */
        margin-bottom: 25px; /* Restore margin */
         border-color: #ddd; /* Restore border */
         box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05); /* Restore shadow */
         pointer-events: auto; /* Enable clicks */
     }


    /* Map View Specific Styles */
    #map-area {
        position: relative;
        width: 100%;
        height: 450px; /* Adjusted height */
        background: linear-gradient(to bottom, #a0c0ff, #70a0e0); /* Gradient background */
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
     #world-map {
         display: block;
         width: 100%;
         height: 100%;
         object-fit: cover; /* Cover area */
         border-radius: 8px;
         transition: transform 0.3s ease; /* Smooth hover effect */
     }
     #map-area:hover #world-map {
         transform: scale(1.02); /* Slightly zoom on hover */
     }

    .location-point {
        position: absolute;
        transform: translate(-50%, -50%);
        padding: 0; /* Remove button padding */
        background: none; /* No button background */
        border: none; /* No button border */
        cursor: pointer;
        font-size: 1em;
        z-index: 10;
        transition: all 0.3s ease; /* Smooth transitions for point */
        filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.3)); /* Subtle shadow for point */
    }
     .location-point::before {
         content: '';
         display: block;
         width: 15px;
         height: 15px;
         background-color: #007bff; /* Blue dot */
         border-radius: 50%;
         border: 3px solid #fff; /* White border */
         box-shadow: 0 0 8px rgba(0, 123, 255, 0.5); /* Glow effect */
         margin: 0 auto 5px auto; /* Center dot above text */
         transition: all 0.3s ease;
     }
    .location-point:hover::before {
        background-color: #0056b3; /* Darker blue on hover */
        transform: scale(1.2); /* Enlarge dot on hover */
        box-shadow: 0 0 12px rgba(0, 123, 255, 0.7); /* More intense glow */
    }
     .location-point .point-label {
         display: block;
         white-space: nowrap; /* Prevent text wrapping */
         background-color: rgba(0, 0, 0, 0.6); /* Dark background for label */
         color: white;
         padding: 3px 8px;
         border-radius: 4px;
         font-size: 0.8em;
         opacity: 0; /* Hide label by default */
         transition: opacity 0.3s ease;
     }
     .location-point:hover .point-label {
         opacity: 1; /* Show label on hover */
     }

    .location-point.visited::before {
        background-color: #28a745; /* Green for visited */
        box-shadow: 0 0 8px rgba(40, 167, 69, 0.5);
    }
     .location-point.visited:hover::before {
         background-color: #218838;
         box-shadow: 0 0 12px rgba(40, 167, 69, 0.7);
     }

    #map-stats {
        text-align: center;
        margin-top: 15px;
        font-size: 0.95em;
        color: #555;
    }
     #map-stats span {
         font-weight: bold;
         color: #007bff;
     }


    #journal-preview {
        margin-top: 20px;
        border-top: 1px dashed #ddd;
        padding-top: 15px;
    }
    #journal-preview h3 {
         text-align: right;
         margin-bottom: 10px;
         border-bottom: none;
         padding-bottom: 0;
         color: #555;
         font-size: 1.1em;
    }
    #journal-entries {
        max-height: 120px; /* Slightly more height */
        overflow-y: auto;
        border: 1px solid #eee;
        padding: 10px; /* More padding */
        margin-bottom: 15px;
        background-color: #fafafa; /* Lighter background */
        font-size: 0.85em; /* Slightly larger font */
        border-radius: 5px;
    }
     #journal-entries div {
         margin-bottom: 8px; /* More space between entries */
         padding-bottom: 5px;
         border-bottom: 1px dotted #ccc; /* Stronger dotted line */
         color: #444;
     }
     #journal-entries div:last-child {
         border-bottom: none;
         margin-bottom: 0;
     }
     #journal-entries strong {
         color: #0056b3; /* Highlight location name */
         font-weight: normal; /* Less bold */
         margin-left: 5px; /* Space after location */
     }


    /* Shore View Specific Styles */
    #shore-scene {
        position: relative;
        width: 100%;
        height: 380px; /* Adjusted height */
        background: linear-gradient(to bottom, #d0b090, #b09070); /* Earthy gradient */
        margin-bottom: 20px; /* More margin */
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
     #shore-image {
         display: block;
         width: 100%;
         height: 100%;
         object-fit: cover;
         border-radius: 8px;
         transition: transform 0.3s ease;
     }
      #shore-scene:hover #shore-image {
         transform: scale(1.02);
     }

    .interactive-element {
        position: absolute;
        transform: translate(-50%, -50%);
        padding: 6px 12px; /* Larger clickable area */
        background-color: rgba(40, 167, 69, 0.85); /* Greenish */
        color: white;
        border: none;
        border-radius: 20px; /* Pill shape */
        cursor: pointer;
        font-size: 0.9em;
        z-index: 10;
        transition: all 0.3s ease; /* Smooth transition */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Button shadow */
    }
     .interactive-element:hover {
         background-color: rgba(30, 120, 50, 0.95);
         transform: translate(-50%, -50%) scale(1.1); /* Enlarge slightly on hover */
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
     }

     /* Specific styles for element types */
     .element-creature { background-color: rgba(40, 167, 69, 0.85); }
     .element-creature:hover { background-color: rgba(30, 120, 50, 0.95); }

     .element-fossil { background-color: rgba(108, 117, 125, 0.85); } /* Grayish */
     .element-fossil:hover { background-color: rgba(80, 90, 100, 0.95); }

     .element-geology { background-color: rgba(23, 162, 184, 0.85); } /* Cyan/Teal */
     .element-geology:hover { background-color: rgba(19, 138, 156, 0.95); }


    #observation-panel {
        border: 1px solid #cce5ff; /* Light blue border */
        background-color: #e9f7ff; /* Light blue background */
        padding: 15px; /* More padding */
        margin-bottom: 20px; /* More margin */
        border-radius: 8px;
        transition: all 0.4s ease; /* Smooth transition for panel */
        box-shadow: 0 2px 6px rgba(0, 123, 255, 0.15); /* Subtle blue shadow */
    }
     #observation-panel.hidden {
         opacity: 0;
         max-height: 0; /* Collapse height */
         padding-top: 0;
         padding-bottom: 0;
         margin-top: 0;
         margin-bottom: 0;
         overflow: hidden;
         border-color: transparent;
         box-shadow: none;
     }
      #observation-panel h3 {
         margin-top: 0;
         font-size: 1.2em;
         border-bottom: 1px solid #b8daff; /* Lighter blue border */
         padding-bottom: 8px;
         color: #004085; /* Darker blue text */
     }
     #observation-panel p {
         font-size: 1em;
         line-height: 1.6;
         color: #004085;
         margin-bottom: 15px; /* More space below description */
     }

     .feedback {
         margin-top: 10px;
         font-weight: bold;
     }
     #observation-feedback[style*="color: green"] { /* Target specific color for styling */
         color: #28a745; /* Bootstrap success green */
     }
     #observation-feedback[style*="color: red"] { /* Target specific color for styling */
          color: #dc3545; /* Bootstrap danger red */
     }


    /* Journal View Specific Styles */
    #full-journal-entries {
        border: 1px solid #e0e0e0; /* Lighter border */
        padding: 15px; /* More padding */
        max-height: 350px; /* More height */
        overflow-y: auto;
        margin-bottom: 20px; /* More margin */
        background-color: #fffbf0; /* Journal-like background */
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }
     #full-journal-entries div {
         margin-bottom: 15px; /* More space */
         padding-bottom: 10px;
         border-bottom: 1px dashed #d0d0d0; /* Lighter dashed line */
         color: #333;
     }
      #full-journal-entries div:last-child {
         border-bottom: none;
         margin-bottom: 0;
     }
      #full-journal-entries strong {
          color: #0056b3;
          font-weight: bold; /* Back to bold for emphasis */
          margin-left: 8px; /* Space after location */
      }
     #full-journal-entries em {
         font-size: 0.9em;
         color: #777;
         display: block; /* Timestamp on new line */
         margin-top: 5px;
     }
     .journal-hint {
         font-style: italic;
         color: #666;
         margin-bottom: 20px;
         text-align: center;
         font-size: 0.9em;
     }


    /* Button Styles */
    button {
        padding: 10px 20px; /* Larger buttons */
        background-color: #007bff; /* Primary blue */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em; /* Standard font size */
        margin-right: 8px; /* More space between buttons */
        transition: background-color 0.2s ease, transform 0.1s ease; /* Smooth hover/active */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }
    button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
    }
    button:active {
         transform: scale(0.98); /* Slight press effect */
    }

    .secondary-button {
         background-color: #6c757d; /* Secondary gray */
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
    }
    .secondary-button:hover {
         background-color: #545b62; /* Darker gray on hover */
         box-shadow: 0 3px 6px rgba(0, 0, 0, 0.12);
    }

    #add-to-journal-btn {
        background-color: #28a745; /* Success green */
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
     #add-to-journal-btn:hover {
         background-color: #218838; /* Darker green */
         box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
     }

     .tertiary-button {
         display: block; /* Make it a block element */
         margin: 25px auto; /* Center button */
         background-color: #17a2b8; /* Info cyan */
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
     }
      .tertiary-button:hover {
          background-color: #138496; /* Darker cyan */
          box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
      }


    /* Explanation Section Styles */
    #explanation {
        margin-top: 30px; /* More space above */
        padding: 20px; /* More padding */
        border: 1px solid #ccc;
        border-radius: 12px; /* More rounded corners */
        background-color: #e9ecef; /* Light gray-blue */
        direction: rtl;
        line-height: 1.7; /* Ensure readability */
        opacity: 1;
        transition: opacity 0.5s ease-in-out;
    }
     #explanation.hidden {
        opacity: 0;
        height: 0; /* Collapse height */
        padding-top: 0;
        padding-bottom: 0;
        margin-top: 0;
        margin-bottom: 0;
        overflow: hidden;
        border-color: transparent;
     }
     #explanation h2, #explanation h3 {
         color: #343a40; /* Darker text */
         text-align: right; /* Align explanation headings right */
     }
     #explanation h2 {
        border-bottom: 2px solid #17a2b8; /* Accent line */
        padding-bottom: 10px;
        margin-bottom: 15px;
     }
     #explanation h3 {
         margin-top: 20px; /* More space above section headings */
         border-bottom: 1px dashed #adb5bd;
         padding-bottom: 8px;
         margin-bottom: 10px;
         color: #495057;
     }
     #explanation p {
         font-size: 1em;
         line-height: 1.7;
         color: #495057;
         margin-bottom: 15px;
     }

     /* Responsive adjustments */
     @media (max-width: 768px) {
        #app-container {
            padding: 10px;
            margin: 15px auto;
        }
        h1 { font-size: 1.6em; }
        h2 { font-size: 1.3em; }
        h3 { font-size: 1.1em; }
        button { padding: 8px 15px; font-size: 0.9em; }
        .location-point .point-label { font-size: 0.7em; }
        .interactive-element { font-size: 0.8em; padding: 5px 10px; }
        #explanation { padding: 15px; }
     }
</style>

<script>
    // Data structure holds all information
    const locations = {
        south_america: {
            name: "חופי דרום אמריקה",
            english_slug: "south_america",
            image: "https://via.placeholder.com/700x350/d0b090/333?text=South+America+Coast", // Placeholder suggestive of the region
            elements: [
                { id: "finch_mainland", name: "פינץ' (יבשה)", description: "פינץ' עם מקור חסון, אופייני לאכילת זרעים קשים שנמצאים בשפע ביבשת." },
                 { id: "fossil_mega", name: "מאובן יונק ענק", description: "מאובן של יונק ענק נכחד, כמו עצלן ענק (מגתריום) או גליפטודון (ארמדילו ענק). דומה ליונקים קטנים יותר החיים כיום באותו אזור, אך גדול בהרבה. רמז לשינוי מינים לאורך זמן!" },
                 { id: "geology_andes", name: "תצורת סלע באנדים", description: "שכבות סלע ימיות שנמצאו גבוה בהרי האנדים, מראות שהאזור היה פעם מתחת לפני הים והתרומם לאט לאורך מיליוני שנים. שינויים אדירים מתרחשים גם בנוף, לא רק בחיים!"}
            ]
        },
        galapagos: {
            name: "איי גלפגוס",
             english_slug: "galapagos",
            image: "https://via.placeholder.com/700x350/80a0a0/fff?text=Galapagos+Volcanic+Island", // Placeholder suggestive of volcanic islands
            elements: [
                { id: "finch_galapagos", name: "פינץ' (גלפגוס)", description: "פינץ' באיי גלפגוס. צורת המקור משתנה מאוד מאי לאי. באחד האיים המקור עבה לאכילת זרעים, באחר דק וארוך לאכילת חרקים, ובאחר קצר לאכילת ניצנים. דוגמה מובהקת להתאמה לסביבה המקומית!" },
                 { id: "giant_tortoise", name: "צב גלפגוס ענק", description: "צב יבשתי ענק, אנדמי לגלפגוס. גם צורת השריון משתנה בין תת-מינים באיים שונים. באיים עם צמחייה נמוכה, השריון כיפתי ונמוך. באיים יבשים עם קקטוסים גבוהים, השריון 'אוכפי' ומאפשר להרים את הראש גבוה יותר כדי להגיע למזון. התאמה מדהימה לסביבה!" },
                 { id: "iguana_marine", name: "איגואנת ים", description: "הלטרטאור היחיד בעולם שמבלה חלק ניכר מזמנו בים וניזון מאצות. הוא מתחמם על הסלעים בשמש לאחר הצלילה במים הקרים. יצור מותאם בצורה ייחודית לסביבה הימית של גלפגוס!"}
            ]
        },
         tierra_del_fuego: {
            name: "טיירה דל פואגו",
             english_slug: "tierra_del_fuego",
            image: "https://via.placeholder.com/700x350/a0b0c0/fff?text=Tierra+del+Fuego+Shore", // Placeholder suggestive of cold, southern lands
            elements: [
                { id: "penguins", name: "פינגווינים", description: "מושבת פינגווינים מסוג Magellanic. עופות ימיים מותאמים לחיים במים הקרים של אזורי הדרום, עם כנפיים שהפכו לסנפירים ושכבת שומן מבודדת. מראים מגוון החיים גם בתנאים קיצוניים!"}
            ]
         }
        // Add more locations and elements following this structure
    };

    let journal = []; // Array to store journal entries
    let visitedLocations = new Set(); // Set to track visited locations

    // Get UI elements
    const appContainer = document.getElementById('app-container');
    const mapView = document.getElementById('map-view');
    const shoreView = document.getElementById('shore-view');
    const journalView = document.getElementById('journal-view');

    const mapPoints = appContainer.querySelectorAll('.location-point');
    const visitedCountSpan = document.getElementById('visited-count');
    const totalLocationsSpan = document.getElementById('total-locations');

    const shoreScene = document.getElementById('shore-scene');
    const shoreImage = document.getElementById('shore-image');
    const shoreLocationName = document.getElementById('shore-location-name');
    const observationPanel = document.getElementById('observation-panel');
    const observationName = document.getElementById('observation-name');
    const observationDescription = document.getElementById('observation-description');
    const addToJournalBtn = document.getElementById('add-to-journal-btn');
    const observationFeedback = document.getElementById('observation-feedback');

    const backToMapBtn = document.getElementById('back-to-map-btn');
    const viewJournalBtn = document.getElementById('view-journal-btn');
    const fullJournalEntries = document.getElementById('full-journal-entries');
    const closeJournalBtn = document.getElementById('close-journal-btn');
    const journalPreviewEntries = document.getElementById('journal-entries');
    // const backToMapFromJournalBtn = document.getElementById('back-to-map-from-journal-btn'); // Keeping hidden as closeJournalBtn does the same

    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');


    // --- View Switching ---
    function showView(viewId) {
        const views = [mapView, shoreView, journalView];
        views.forEach(view => {
            if (view.id === viewId) {
                view.classList.add('active');
                view.classList.remove('hidden');
                 // Set focus for accessibility after view change animation
                 // setTimeout(() => view.focus(), 600); // Maybe add a focus element inside views
            } else {
                view.classList.remove('active');
                view.classList.add('hidden');
            }
        });
    }

     // --- Update Map Stats ---
     function updateMapStats() {
         const total = Object.keys(locations).length;
         visitedCountSpan.textContent = visitedLocations.size;
         totalLocationsSpan.textContent = total;
     }

    // --- Shore Scene Rendering ---
    function renderShoreScene(locationKey) {
        const locationData = locations[locationKey];
        if (!locationData) {
            console.error("Location data not found for key:", locationKey);
            return;
        }
        shoreLocationName.textContent = `חקר ב: ${locationData.name}`; // More descriptive title
        shoreImage.src = locationData.image;
        shoreImage.alt = `נוף ב${locationData.name}`; // Update alt text

        // Hide all interactive elements first
        shoreScene.querySelectorAll('.interactive-element').forEach(btn => {
            btn.style.display = 'none'; // Use style to override CSS display rules
        });

        // Show only elements belonging to the current location
        // This relies on the static buttons having the correct data-location attribute
        const elementsToShow = shoreScene.querySelectorAll(`.interactive-element[data-location="${locationKey}"]`);

        if (elementsToShow.length === 0) {
             // Add a message if there are no interactive elements at this location
             const noElementsMessage = document.createElement('div');
             noElementsMessage.id = 'no-elements-message';
             noElementsMessage.textContent = 'אין כרגע תצפיות זמינות במיקום זה.';
             noElementsMessage.style.cssText = `
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: rgba(255, 255, 255, 0.9);
                padding: 10px 15px;
                border-radius: 8px;
                font-size: 1.1em;
                color: #555;
                z-index: 5;
             `;
             // Remove previous message if exists
             const existingMessage = shoreScene.querySelector('#no-elements-message');
             if (existingMessage) {
                 existingMessage.remove();
             }
             shoreScene.appendChild(noElementsMessage);

        } else {
            // Remove any "no elements" message
            const existingMessage = shoreScene.querySelector('#no-elements-message');
            if (existingMessage) {
                existingMessage.remove();
            }
             elementsToShow.forEach(btn => {
                 btn.style.display = ''; // Show the button
                 // Listeners are added once during initialization below
             });
        }


        observationPanel.classList.add('hidden'); // Hide panel when changing location
        observationFeedback.textContent = ''; // Clear feedback
         observationFeedback.style.color = ''; // Reset feedback color
    }

    // --- Display Observation ---
     function displayObservation(elementId, locationKey) { // Pass IDs to look up data
         const locationData = locations[locationKey];
         if (!locationData) {
             console.error("Location data not found for key:", locationKey);
             return;
         }
         const element = locationData.elements.find(el => el.id === elementId);
         if (element) {
             observationName.textContent = element.name;
             observationDescription.textContent = element.description;
             addToJournalBtn.dataset.elementId = element.id; // Store element ID
             addToJournalBtn.dataset.locationKey = locationKey; // Store location key
             observationFeedback.textContent = ''; // Clear previous feedback
             observationFeedback.style.color = ''; // Reset feedback color
             observationPanel.classList.remove('hidden');
         } else {
             console.error("Element data not found for ID:", elementId, "at location:", locationKey);
             observationPanel.classList.add('hidden'); // Hide if element not found
         }
     }


    // --- Journal Interaction ---
    addToJournalBtn.addEventListener('click', () => {
        const elementId = addToJournalBtn.dataset.elementId;
        const locationKey = addToJournalBtn.dataset.locationKey;

        if (!elementId || !locationKey) {
            console.error("No element or location data stored for journal entry.");
            observationFeedback.textContent = 'שגיאה: לא ניתן לרשום תצפית זו (חסרים נתונים פנימיים).';
            observationFeedback.style.color = 'red';
            return;
        }

        const locationData = locations[locationKey];
        if (!locationData) {
            console.error("Location data not found for key:", locationKey, "when adding to journal.");
            observationFeedback.textContent = 'שגיאה: לא ניתן לרשום תצפית זו (בעיה בזיהוי מיקום).';
            observationFeedback.style.color = 'red';
            return;
        }

        const element = locationData.elements.find(el => el.id === elementId);

        if (element) {
             // Prevent duplicate entries for the exact same element at the same location
             const isDuplicate = journal.some(entry =>
                 entry.locationKey === locationKey && entry.elementId === elementId
             );

             if (isDuplicate) {
                  observationFeedback.textContent = `כבר רשמת תצפית על "${element.name}" מ${locationData.name}.`;
                  observationFeedback.style.color = 'orange'; // Indicate already recorded
                  return;
             }

            const entry = {
                location: locationData.name,
                locationKey: locationKey, // Store key for internal use
                elementId: elementId, // Store ID for internal use
                elementName: element.name,
                description: element.description,
                timestamp: new Date().toLocaleString('he-IL')
            };
            journal.push(entry);
            updateJournalDisplays();
            observationFeedback.textContent = `"${element.name}" מ${locationData.name} נרשם ביומן!`;
            observationFeedback.style.color = 'green'; // Ensure color is green for success
        } else {
            console.error("Element data not found for ID:", elementId, "when adding to journal.");
            observationFeedback.textContent = 'שגיאה: לא ניתן לרשום תצפית זו.';
            observationFeedback.style.color = 'red';
        }
    });

    function updateJournalDisplays() {
        const formatEntry = (entry) => `<div><strong>${entry.location}:</strong> ${entry.elementName}</div><p>${entry.description}</p><em>(${entry.timestamp})</em>`;
        const formatPreviewEntry = (entry) => `<div><strong>${entry.location}:</strong> ${entry.elementName}</div>`;

        // Update preview
        journalPreviewEntries.innerHTML = '';
        if (journal.length === 0) {
            journalPreviewEntries.textContent = 'לחץ על נקודות במפה כדי לעגון ולהתחיל לחקור את הטבע סביבך.';
        } else {
            // Show only latest few in preview
            journal.slice(-3).reverse().forEach(entry => {
                 const div = document.createElement('div');
                 div.innerHTML = formatPreviewEntry(entry);
                 journalPreviewEntries.appendChild(div);
             });
             if(journal.length > 3) {
                 const moreDiv = document.createElement('div');
                 moreDiv.textContent = `... ועוד ${journal.length - 3} תצפיות נוספות ביומן המלא.`;
                 moreDiv.style.cssText = 'font-style: italic; color: #777; margin-top: 5px;';
                 journalPreviewEntries.appendChild(moreDiv);
             }
        }

        // Update full journal view
        fullJournalEntries.innerHTML = '';
        if (journal.length === 0) {
             fullJournalEntries.textContent = 'עוד לא אספת תצפיות. חזור למפה וחקר יעדים חדשים!';
        } else {
             journal.forEach(entry => {
                 const div = document.createElement('div');
                 div.innerHTML = formatEntry(entry);
                 fullJournalEntries.appendChild(div);
             });
        }
    }

    viewJournalBtn.addEventListener('click', () => {
        updateJournalDisplays(); // Ensure it's updated before showing
        showView('journal-view');
    });

    closeJournalBtn.addEventListener('click', () => {
        showView('map-view'); // Return to map view
    });

     // backToMapFromJournalBtn.addEventListener('click', () => {
     //    showView('map-view'); // Return to map view
     // });


    // --- Navigation Buttons ---
    backToMapBtn.addEventListener('click', () => {
        showView('map-view');
    });

    // --- Explanation Toggle ---
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.toggle('hidden');
        if (!isHidden) {
            toggleExplanationBtn.textContent = 'הסתר סיפור המסע ורעיון האבולוציה';
             // Scroll to the explanation section
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
            toggleExplanationBtn.textContent = 'הצג סיפור המסע ורעיון האבולוציה';
        }
    });


    // --- Initialization ---

    // Add click listeners to Map Points
    mapPoints.forEach(point => {
        point.addEventListener('click', () => {
            const locationKey = point.dataset.location;
             if (!visitedLocations.has(locationKey)) {
                  visitedLocations.add(locationKey);
                  point.classList.add('visited'); // Mark visually
                  updateMapStats(); // Update counter
             }
            renderShoreScene(locationKey); // Pass the key to renderScene
            showView('shore-view');
        });
         // Initially hide all interactive elements until a location is selected by renderShoreScene
         // This is also done in renderShoreScene, but good to ensure on load
         // point.style.display = 'none'; // This hides the map points themselves! NO, this is wrong.
    });

    // Add click listeners to ALL Interactive Element buttons ONCE during setup
    // These buttons are static in the HTML, but shown/hidden by renderShoreScene
    shoreScene.querySelectorAll('.interactive-element').forEach(btn => {
        const elementId = btn.dataset.element;
        const locationKey = btn.dataset.location;

        // Find the corresponding element data to ensure it exists
        const locationData = locations[locationKey];
        if (locationData) {
            const elementData = locationData.elements.find(el => el.id === elementId);
            if (elementData) {
                 // Add event listener only if data exists
                 btn.addEventListener('click', () => {
                      displayObservation(elementId, locationKey);
                 });
            } else {
                 console.warn(`Element data not found for ID: ${elementId} at location: ${locationKey}. Button may be hidden or non-functional.`);
                 // Button will be hidden by renderShoreScene anyway if data-location doesn't match current view
            }
        } else {
             console.warn(`Location data not found for key: ${locationKey} for interactive element. Button may be hidden or non-functional.`);
             // Button will be hidden by renderShoreScene anyway
        }

         // Initially hide all interactive elements until a location is selected by renderShoreScene
         // This is handled inside renderShoreScene based on data-location, but a default hidden state in CSS or here is also fine.
         // CSS handles the initial hidden state better.
         btn.style.display = 'none'; // Hide all initially
    });


     // Ensure the correct number of total locations is displayed on load
     totalLocationsSpan.textContent = Object.keys(locations).length;
     visitedCountSpan.textContent = visitedLocations.size; // Should be 0 initially

    showView('map-view'); // Start on the map view
    updateJournalDisplays(); // Initialize journal display (will show empty message)

</script>
```