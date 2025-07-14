---
title: "המסע האפי של הצלופח: מהנהר העיקש אל הים הפתוח ובחזרה"
english_slug: the-epic-journey-of-the-eel-from-river-to-open-sea-and-back
category: "מדעי החיים / ביולוגיה ימית"
tags: [צלופח, נדידה, אוקיינוס, נהר, מעגל חיים, ים סרגסו, מסע מופלא, טבע]
---
<div class="simulation-wrapper">
    <h1>המסע האפי של הצלופח: מהנהר העיקש אל הים הפתוח ובחזרה</h1>
    <p>מסתוריים, עמידים וחדורי מטרה. צלופחים ימיים חיים שנים רבות בנהרות ובאגמים, אך כשהטבע קורא להם, הם יוצאים למסע היסטורי בן אלפי קילומטרים אל לב האוקיינוס כדי להתרבות. בואו נצלול לעומק התעלומה ונראה כיצד הם עושים זאת!</p>

    <div id="eel-simulation-container">
        <div id="map-representation">
            <div id="land-europe" class="land-mass">
                <p>אירופה</p>
                <div class="river-spot" id="europe-river"></div>
            </div>
            <div id="land-na" class="land-mass">
                <p>צפון אמריקה</p>
                 <div class="river-spot" id="na-river"></div>
            </div>
            <div id="ocean-atlantic" class="ocean"></div>
            <div id="sargasso-sea" class="ocean-area">
                <span>ים סרגסו</span>
                <span class="area-subtitle">אזור רבייה סודי</span>
            </div>

            <!-- Eels - Represented as dynamic points/groups -->
            <div id="eel-yellow" class="eel yellow"></div>
            <div id="eel-silver" class="eel silver hidden"></div>
            <div id="eel-leptocephalus" class="eel leptocephalus hidden"></div>
            <div id="eel-glass" class="eel glass hidden"></div>

            <!-- Dynamic captions -->
            <div id="eel-caption" class="eel-caption hidden"></div>
        </div>

        <div id="controls">
            <button id="start-simulation">צאו למסע!</button>
            <div id="stage-indicator">שלב נוכחי: צלופח צהוב בנהר</div>
        </div>
    </div>

    <button id="toggle-explanation">גלו את כל הסודות (הסבר מורחב)</button>

    <div id="explanation" class="hidden">
        <h2>אודות המסע המסתורי של הצלופח</h2>

        <h3>מבוא: גיבורי המסע - הצלופחים הקטדרומיים</h3>
        <p>הכירו את הצלופחים הימיים (האירופאי <em>Anguilla anguilla</em> והאמריקאי <em>Anguilla rostrata</em>) - יצורים מופלאים עם מחזור חיים יוצא דופן. הם נולדים במים מלוחים עמוק בים, מבלים את רוב חייהם במים מתוקים או מליחים (כמו נהרות ושפכי נהרות), ונודדים בחזרה לים, לאותו אזור הולדת בדיוק, רק כדי להתרבות ולסיים את חייהם. מסע הרבייה שלהם הוא אחד הפלאים הגדולים וחסרי הפשר עד הסוף בעולם הטבע - מסע שחוצה אוקיינוס שלם!</p>

        <h3>מסע בזמן ובמרחב: שלבי החיים</h3>
        <p>מחזור חיי הצלופח הוא סדרה של שינויים דרמטיים (מטמורפוזות), שבהם הצלופח משנה את צורתו, פיזיולוגיה והתנהגות כדי להתאים עצמו לסביבות מחיה שונות לחלוטין (מים מלוחים מול מים מתוקים). השלבים העיקריים:</p>
        <ul>
            <li><strong>פגית (Leptocephalus):</strong> הדור הבא! זוהי צורת הזחל הראשונית - יצור שקוף, דק ושטוח דמוי עלה ערבה קטן. הפגיות בוקעות בים סרגסו ופשוט נסחפות ללא מאמץ גדול בזרמי האוקיינוס העצומים, כמו זרם הגולף, במשך חודשים ארוכים ואפילו שנים, בדרכן חזרה ליבשות.</li>
            <li><strong>צלופח זכוכית (Glass eel):</strong> סוף המסע הימי! כשהפגיות מתקרבות למדף היבשתי (ליד החופים), הן עוברות מטמורפוזה נוספת והופכות ליצורים שקופים דמויי צלופח קטן, כמעט בלתי נראים. זהו שלב מעבר קצר לפני שהן מתחילות להיכנס אל תוך שפכי נהרות ומים מתוקים.</li>
            <li><strong>צלופחון (Elver):</strong> העלייה מתחילה! צלופחי זכוכית שמקבלים פיגמנטציה חלקית וצבע חום-ירקרק עדין. הם ממשיכים את המסע במעלה הנהרות והנחלים, לעיתים קרובות מטפסים מעל מכשולים בעזרת גופם הרירי.</li>
            <li><strong>צלופח צהוב (Yellow eel):</strong> שנות הזהב בנהר! זהו שלב הגדילה הארוך ביותר בחיי הצלופח, שיכול להימשך 10, 15 ואף 20 שנה ויותר! הצלופחים חיים במים מתוקים או מליחים, צבעם צהבהב-ירקרק בגחון והם טורפים זריזים וזללנים. זהו השלב שבו רוב האנשים פוגשים צלופחים.</li>
            <li><strong>צלופח כסוף (Silver eel):</strong> ההכנה למסע הגדול! כאשר הצלופח הצהוב מגיע לבגרות מינית (מבחינת גודל וגיל), הוא עובר מטמורפוזה דרסטית נוספת, הנקראת "הכספוף" (Silvering). העיניים גדלות, צבע הגחון הופך כסוף-מבריק, מערכת העיכול מתנוונת (הם מפסיקים לאכול), ומערכת הרבייה מתפתחת. שינויים אלו מכינים אותם לחיים במים מלוחים עמוקים ולמסע הנדידה האדיר אל ים סרגסו.</li>
        </ul>

        <h3>הקריאה לים: המסע החוצה</h3>
        <p>עם בוא הסתיו, מונעים על ידי שעון ביולוגי פנימי ורמזים סביבתיים (כמו ירידת טמפרטורת המים והתקצרות היום), הצלופחים הכסופים מתחילים את ירידתם במורד הנהרות והנחלים. הם שוחים אל שפכי הנהרות ומשם אל הים הפתוח, ומתחילים את המסע המאתגר אל יעד הרבייה הסודי.</p>

        <h3>ניווט על-אוקייני: איך הם מוצאים את הדרך?</h3>
        <p>אחת התעלומות הגדולות בביולוגיה ימית היא כיצד הצלופחים הכסופים, שמעולם לא היו באוקיינוס קודם לכן, מצליחים לנווט אל נקודה כה ספציפית בלב האוקיינוס האטלנטי. מדובר באלפי קילומטרים של ים פתוח ללא שום נקודת ציון נראית לעין! התיאוריות המדעיות המובילות גורסות שהם משתמשים בשילוב של יכולות: אולי חשים בשדה המגנטי של כדור הארץ כסוג של "מפה", אולי מזהים חומרים כימיים מסוימים בזרמי האוקיינוס, ואולי פשוט מנצלים את זרמי הים העיקריים בצורה מתוחכמת. המחקר עדיין מתקדם, ומנסה לפענח את המנגנונים המדויקים של הניווט המופלא הזה.</p>

        <h3>ים סרגסו: הסוף וההתחלה</h3>
        <p>ים סרגסו, אזור ייחודי באוקיינוס האטלנטי הצפון-מערבי המאופיין במים שקטים יחסית ושפע של אצות סרגסום צפות, הוא היעד הבלעדי והקדוש למסע הרבייה. כאן, הצלופחים הבוגרים מטילים את ביציהם בעומק רב. לאחר ההטלה, הם משלימים את מחזור חייהם ומתים (תופעה הנקראת סמליפריות - רבייה פעם אחת בלבד בחיים). מביצי הצלופחים בוקעות הפגיות (Leptocephali) שקופות ונסחפות, שיתחילו את מסע החזרה הארוך ליבשות, ויסגרו מעגל חיים מופלא!</p>

        <h3>המסע חזרה: זרמים ושינויים</h3>
        <p>הפגיות הצעירות אינן שוחות באופן אקטיבי, אלא נסחפות עם זרמי האוקיינוס העיקריים, כמו זרם הגולף העוצמתי, בחזרה מזרחה (ליבשת אירופה) או מערבה (ליבשת צפון אמריקה). מסע פסיבי זה יכול להימשך בין חצי שנה לשלוש שנים, תלוי במין הצלופח ובכיוון הזרמים. כשהן מתקרבות לחופי היבשות, מים פחות מלוחים ושינויים סביבתיים נוספים מגרים אותן לעבור את המטמורפוזה השלישית שלהן - ולהפוך לצלופחי זכוכית, מוכנות לכניסה למים מתוקים.</p>

        <h3>אתגרי ההישרדות וסטטוס שימור</h3>
        <p>למרות שהמסע של הצלופחים נחקר כבר עשרות שנים, עדיין ישנם פערים עצומים בהבנתנו את אחוזי ההישרדות שלהם בשלבים הימיים, ובמיוחד המסע המפרך אל ים סרגסו ובחזרה. אוכלוסיות הצלופח האירופאי והאמריקאי נמצאות בירידה חדה ומדאיגה בעשורים האחרונים, ומסווגות כמינים בסכנת הכחדה חמורה או בסכנת הכחדה. האיומים רבים ומשולבים: דיג לא מבוקר (גם של צלופחונים צעירים), חסימת נתיבי נדידה על ידי סכרים, זיהום מים, מחלות וטפילים, וכן שינויי אקלים המשפיעים על טמפרטורת המים ועל זרמי האוקיינוס החיוניים למסע הפגיות. שימור הצלופחים הוא אתגר גלובלי הדורש שיתוף פעולה בינלאומי דחוף ומאמצים משולבים בכל שלבי מחזור החיים שלהם.</p>
    </div>
</div>

<style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    @keyframes flow {
        0% { background-position: 0 0; }
        100% { background-position: 100% 100%; }
    }

    .simulation-wrapper {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        max-width: 960px;
        margin: 20px auto;
        padding: 15px;
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2);
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        overflow: hidden;
    }

    h1, h2, h3 {
        color: #004d40; /* Dark Teal */
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2em;
        margin-top: 0;
    }

    p {
        text-align: center;
        margin-bottom: 20px;
        font-size: 1.1em;
        color: #00695c; /* Medium Teal */
    }

    #eel-simulation-container {
        width: 100%;
        max-width: 800px;
        margin: 20px auto;
        border: 2px solid #004d40;
        border-radius: 8px;
        padding: 10px;
        background-color: #80deea; /* Cyan */
        position: relative;
        overflow: hidden;
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.2);
    }

    #map-representation {
        position: relative;
        width: 100%;
        height: 450px; /* Increased height */
        background: linear-gradient(to bottom, #4fc3f7, #0277bd); /* Ocean Gradient */
        border-radius: 6px;
        overflow: hidden; /* Clip land/areas */
         box-sizing: border-box;
         animation: flow 60s linear infinite; /* Subtle water movement */
         background-size: 200% 200%;
    }

    .land-mass {
        background: linear-gradient(to bottom right, #a5d6a7, #66bb6a); /* Green Gradient */
        position: absolute;
        border: 1px solid #388e3c;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: #1b5e20; /* Dark Green */
        text-align: center;
        padding: 10px;
        box-sizing: border-box;
        border-radius: 80px; /* More rounded shapes */
        opacity: 0.95; /* Slightly transparent */
        z-index: 2; /* Above ocean background */
    }

    .land-mass p {
         color: #1b5e20;
         margin: 0;
         font-size: 1.1em;
         text-shadow: 0 0 5px rgba(255,255,255,0.5);
    }

    #land-europe {
        width: 35%; /* Wider */
        height: 75%; /* Taller */
        top: 10%;
        left: -5%; /* Slightly off-center left */
        border-top-right-radius: 150px;
        border-bottom-left-radius: 100px;
        border-bottom-right-radius: 100px;
    }

    #land-na {
        width: 35%; /* Wider */
        height: 75%; /* Taller */
        top: 10%;
        right: -5%; /* Slightly off-center right */
        border-top-left-radius: 150px;
        border-bottom-right-radius: 100px;
        border-bottom-left-radius: 100px;
    }

     .river-spot {
         width: 20px;
         height: 20px;
         background-color: #0277bd; /* River Blue */
         border-radius: 50%;
         border: 2px solid #e1f5fe;
         position: absolute;
         z-index: 3; /* Above land */
         box-shadow: 0 0 8px rgba(0, 0, 255, 0.5); /* Watery glow */
     }

     #europe-river {
         top: 50%;
         left: 60%; /* Position within Europe */
     }
     #na-river {
          top: 50%;
          left: 30%; /* Position within NA */
     }


    .ocean {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1; /* Below land/areas */
    }

     .ocean-area {
        background-color: rgba(2, 119, 189, 0.6); /* Darker Blue */
        position: absolute;
        width: 20%; /* Larger */
        height: 30%; /* Larger */
        top: 35%;
        left: 40%; /* Centered */
        border: 3px dashed #e1f5fe; /* Lighter dashed border */
        border-radius: 15px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-size: 1em;
        text-align: center;
        color: #e1f5fe; /* Light Blue */
        font-weight: bold;
        text-shadow: 0 0 5px rgba(0,0,0,0.3);
        z-index: 3; /* Above general ocean and land edges */
        animation: pulse 2s infinite ease-in-out; /* Pulsing effect */
     }
     .ocean-area span { display: block; }
     .ocean-area .area-subtitle { font-size: 0.8em; font-weight: normal; margin-top: 3px; }


    .eel {
        position: absolute;
        width: 25px; /* Size of the eel representation */
        height: 25px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.6em;
        font-weight: bold;
        color: #333;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.4);
        z-index: 4; /* Above map elements and areas */
        transition: left var(--transition-duration, 0s) linear, top var(--transition-duration, 0s) linear; /* JS sets duration */
        box-sizing: border-box;
    }

    /* Distinct styles for each stage */
    .eel.yellow {
        background-color: #ffeb3b; /* Bright Yellow */
        border: 2px solid #fbc02d; /* Darker Yellow Border */
    }
     .eel.silver {
        background-color: #e0e0e0; /* Light Grey */
        border: 2px solid #9e9e9e; /* Medium Grey Border */
        box-shadow: 1px 1px 5px rgba(0,0,0,0.5), 0 0 15px rgba(255,255,255,0.6); /* Metallic sheen effect */
     }
    .eel.leptocephalus {
        background-color: rgba(255, 243, 224, 0.7); /* Very light beige, translucent */
        border: 2px solid #d7ccc8; /* Pale brown border */
        width: 30px; /* Slightly larger, flatter shape feel */
        height: 20px;
        border-radius: 10px; /* More rectangular/leafy feel */
        opacity: 0.9;
     }
    .eel.glass {
        background-color: rgba(255, 255, 255, 0.9); /* Almost transparent white */
        border: 2px solid #b0bec5; /* Light blue-grey border */
        backdrop-filter: blur(1px); /* Subtle blur effect */
        width: 20px;
        height: 20px;
        opacity: 0.95;
     }

    .eel.hidden {
        display: none;
    }

    .eel-caption {
        position: absolute;
        background-color: rgba(0, 0, 0, 0.6);
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.8em;
        white-space: nowrap;
        pointer-events: none; /* Allow clicks to pass through */
        transform: translate(-50%, -100%); /* Position above the eel */
        z-index: 5; /* Above eels */
        transition: opacity 0.3s ease-in-out;
        opacity: 0; /* Hidden by default */
    }

    .eel-caption:before {
         content: '';
         position: absolute;
         bottom: -5px;
         left: 50%;
         transform: translateX(-50%);
         width: 0;
         height: 0;
         border-left: 5px solid transparent;
         border-right: 5px solid transparent;
         border-top: 5px solid rgba(0, 0, 0, 0.6);
    }

     .eel-caption.visible {
         opacity: 1;
     }


    #controls {
        text-align: center;
        margin-top: 20px;
    }

    #start-simulation {
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #00796b; /* Dark Cyan */
        color: white;
        border: none;
        border-radius: 6px;
        margin-bottom: 12px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    #start-simulation:hover:not(:disabled) {
        background-color: #004d40; /* Even Darker Cyan */
        transform: translateY(-2px);
    }

    #start-simulation:disabled {
        background-color: #b2dfdb; /* Light Cyan */
        cursor: not-allowed;
        box-shadow: none;
    }

    #stage-indicator {
        font-size: 1.2em;
        font-weight: bold;
        color: #004d40; /* Dark Teal */
        min-height: 1.2em; /* Prevent layout shift */
    }


    #toggle-explanation {
         display: block;
         margin: 25px auto 15px auto;
         padding: 10px 20px;
         font-size: 1em;
         cursor: pointer;
         background-color: #0277bd; /* Dark Blue */
         color: white;
         border: none;
         border-radius: 5px;
         transition: background-color 0.3s ease;
          box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    #toggle-explanation:hover {
        background-color: #01579b; /* Even Darker Blue */
    }

     #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #004d40;
        background-color: #e0f2f7; /* Very Light Blue */
        border-radius: 8px;
         box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.1);
    }

    #explanation.hidden {
         display: none;
    }

    #explanation h2, #explanation h3 {
        color: #004d40; /* Dark Teal */
        margin-top: 15px;
        margin-bottom: 8px;
        text-align: right;
    }

    #explanation p, #explanation ul {
        margin-bottom: 15px;
        line-height: 1.7;
        color: #333;
        text-align: right;
    }
     #explanation ul {
         padding-right: 20px;
     }
     #explanation li {
         margin-bottom: 8px;
     }

</style>

<script>
    const startButton = document.getElementById('start-simulation');
    const stageIndicator = document.getElementById('stage-indicator');
    const yellowEel = document.getElementById('eel-yellow');
    const silverEel = document.getElementById('eel-silver');
    const leptocephalusEel = document.getElementById('eel-leptocephalus');
    const glassEel = document.getElementById('eel-glass');
    const sargassoSea = document.getElementById('sargasso-sea');
    const europeRiverSpot = document.getElementById('europe-river'); // Use this for initial yellow pos
    const naRiverSpot = document.getElementById('na-river'); // Add logic for NA origin if needed, simplifying to Europe for now

    const eelCaption = document.getElementById('eel-caption');

    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    let mapRect; // To store map dimensions and position

    // Define logical locations based on map elements
    let locations = {
        europeRiver: null, // Calculated based on europeRiverSpot
        sargassoSea: null, // Calculated based on sargassoSea
        europeCoast: null, // Approximate point near Europe coast
        midAtlanticOut: null, // Approximate point in mid-Atlantic leaving Europe
        midAtlanticBack: null, // Approximate point in mid-Atlantic returning to Europe
        europeArrival: null // Approximate point near Europe coast arrival
    };

    // Path definitions using calculated locations
    const migrationPathOut = [
        'europeRiver', 'europeCoast', 'midAtlanticOut', 'sargassoSea'
    ];

    const driftPathBack = [
        'sargassoSea', 'midAtlanticBack', 'europeArrival', 'europeRiver' // Back to the river spot
    ];

    // Animation durations for each segment (ms)
    const segmentDurations = {
         outToCoast: 3000, // River to Europe coast
         coastToMidAtlantic: 4000, // Europe coast to mid-Atlantic
         midAtlanticToSargasso: 7000, // Mid-Atlantic to Sargasso
         sargassoStay: 3000, // Time at Sargasso
         sargassoToMidAtlantic: 8000, // Sargasso to mid-Atlantic back
         midAtlanticToArrival: 5000, // Mid-Atlantic back to Europe arrival coast
         arrivalToRiver: 3000 // Europe arrival coast to river
    };

    // Captions for each segment/stage
    const captions = {
        start: 'צאו למסע!',
        leavingRiver: 'מתחילים את המסע לים הפתוח...',
        enteringOcean: 'יורדים לעומק האוקיינוס...',
        migrating: 'נודדים אלפי קילומטרים אל ים סרגסו...',
        arrivingSargasso: 'הגענו לים סרגסו - אזור הרבייה!',
        reproducing: 'רבייה...',
        leptocephaliBorn: 'בוקעים פגיות שקופות ונסחפות...',
        drifting: 'נישאות בזרם הגולף בחזרה ליבשה...',
        arrivingCoast: 'מתקרבות לחופי אירופה...',
        transformingToGlass: 'הופכות לצלופחי זכוכית!',
        enteringFreshwater: 'מטפסות במעלה הנהרות והנחלים!',
        growingYellow: 'מתחילות את שלב הגדילה הארוך בנהר...'
    };


    // --- Helper Functions ---

    // Function to calculate the center position of an element relative to the map container
    function getCenterPosition(element) {
         const elementRect = element.getBoundingClientRect();
         const mapRect = document.getElementById('map-representation').getBoundingClientRect();
         const left = elementRect.left + elementRect.width / 2 - mapRect.left;
         const top = elementRect.top + elementRect.height / 2 - mapRect.top;
         return { left: left, top: top };
    }

    // Function to update the stored location coordinates
    function updateLocations() {
        mapRect = document.getElementById('map-representation').getBoundingClientRect();

        locations.europeRiver = getCenterPosition(europeRiverSpot);
        locations.sargassoSea = getCenterPosition(sargassoSea);

        // Approximate points relative to map container size
        locations.europeCoast = { left: mapRect.width * 0.15, top: mapRect.height * 0.5 };
        locations.midAtlanticOut = { left: mapRect.width * 0.35, top: mapRect.height * 0.6 };
        locations.midAtlanticBack = { left: mapRect.width * 0.55, top: mapRect.height * 0.3 };
        locations.europeArrival = { left: mapRect.width * 0.1, top: mapRect.height * 0.3 };

         // Ensure yellow eel starts at the river spot center
         yellowEel.style.left = `${locations.europeRiver.left - yellowEel.offsetWidth / 2}px`;
         yellowEel.style.top = `${locations.europeRiver.top - yellowEel.offsetHeight / 2}px`;

         // Position river spots accurately (optional, can do in CSS)
         // Example: Europe river spot positioning relative to Europe landmass
         const europeRect = document.getElementById('land-europe').getBoundingClientRect();
         europeRiverSpot.style.left = `${europeRect.width * 0.6 - europeRiverSpot.offsetWidth / 2}px`;
         europeRiverSpot.style.top = `${europeRect.height * 0.5 - europeRiverSpot.offsetHeight / 2}px`;
          const naRect = document.getElementById('land-na').getBoundingClientRect();
         naRiverSpot.style.left = `${naRect.width * 0.3 - naRiverSpot.offsetWidth / 2}px`;
         naRiverSpot.style.top = `${naRect.height * 0.5 - naRiverSpot.offsetHeight / 2}px`;
    }

    // Helper to move an element with CSS transition
    function moveElement(element, targetPos, duration, onComplete) {
        element.style.setProperty('--transition-duration', `${duration / 1000}s`);
        element.style.left = `${targetPos.left - element.offsetWidth / 2}px`;
        element.style.top = `${targetPos.top - element.offsetHeight / 2}px`;

        // Use a timeout to wait for the transition to complete
        // Add a small buffer to ensure transition finishes
        setTimeout(() => {
             element.style.setProperty('--transition-duration', '0s'); // Reset duration
             if (onComplete) onComplete();
        }, duration + 50);
    }

    function showCaption(text, positionElement) {
        eelCaption.textContent = text;
        eelCaption.classList.add('visible');

        // Position the caption near the element
        const elementPos = getCenterPosition(positionElement);
        eelCaption.style.left = `${elementPos.left}px`;
        eelCaption.style.top = `${elementPos.top}px`;
    }

    function hideCaption() {
        eelCaption.classList.remove('visible');
         // Optional: Clear text after transition for safety
         setTimeout(() => { eelCaption.textContent = ''; }, 300);
    }

    // --- Simulation Sequence ---
    async function runSimulation() {
        startButton.disabled = true;
        startButton.textContent = 'המסע בעיצומו...';

        // Ensure positions are up-to-date
        updateLocations();

        // --- Stage 1: Yellow Eel prepares for migration ---
        stageIndicator.textContent = 'שלב: צלופח צהוב מתכונן למסע';
        showCaption(captions.start, yellowEel);
        await new Promise(resolve => setTimeout(resolve, 2000));
        hideCaption();

        // --- Stage 2: Silver Eel migration to Sargasso ---
        stageIndicator.textContent = 'שלב: צלופח כסוף - המסע לים סרגסו';
        yellowEel.classList.add('hidden');
        silverEel.classList.remove('hidden');

        // Move silver eel to start at the river spot
        silverEel.style.left = `${locations.europeRiver.left - silverEel.offsetWidth / 2}px`;
        silverEel.style.top = `${locations.europeRiver.top - silverEel.offsetHeight / 2}px`;


        // Segment 1: River to Coast
        showCaption(captions.leavingRiver, silverEel);
        await new Promise(resolve => moveElement(silverEel, locations.europeCoast, segmentDurations.outToCoast, resolve));
        hideCaption();

        // Segment 2: Coast to Mid-Atlantic
        showCaption(captions.enteringOcean, silverEel);
        await new Promise(resolve => moveElement(silverEel, locations.midAtlanticOut, segmentDurations.coastToMidAtlantic, resolve));
         hideCaption();

        // Segment 3: Mid-Atlantic to Sargasso
        showCaption(captions.migrating, silverEel);
        await new Promise(resolve => moveElement(silverEel, locations.sargassoSea, segmentDurations.midAtlanticToSargasso, resolve));
         hideCaption();

        // --- Stage 3: Reproduction in Sargasso ---
        stageIndicator.textContent = 'שלב: רבייה בים סרגסו';
        showCaption(captions.arrivingSargasso, silverEel);
        await new Promise(resolve => setTimeout(resolve, segmentDurations.sargassoStay));
         hideCaption();

        // Adults die, larvae appear
        silverEel.classList.add('hidden');


        // --- Stage 4: Leptocephali drift back ---
        stageIndicator.textContent = 'שלב: פגיות (Leptocephali) נסחפות בחזרה';
        leptocephalusEel.classList.remove('hidden');

        // Start leptocephali at Sargasso
        leptocephalusEel.style.left = `${locations.sargassoSea.left - leptocephalusEel.offsetWidth / 2}px`;
        leptocephalusEel.style.top = `${locations.sargassoSea.top - leptocephalusEel.offsetHeight / 2}px`;


        // Segment 1: Sargasso to Mid-Atlantic back
        showCaption(captions.leptocephaliBorn, leptocephalusEel);
        await new Promise(resolve => moveElement(leptocephalusEel, locations.midAtlanticBack, segmentDurations.sargassoToMidAtlantic, resolve));
         hideCaption();


        // Segment 2: Mid-Atlantic back to Europe arrival coast
        showCaption(captions.drifting, leptocephalusEel);
        await new Promise(resolve => moveElement(leptocephalusEel, locations.europeArrival, segmentDurations.midAtlanticToArrival, resolve));
         hideCaption();


        // --- Stage 5: Glass Eel transformation and entry ---
        stageIndicator.textContent = 'שלב: צלופח זכוכית - הגעה ליבשה';
        leptocephalusEel.classList.add('hidden');
        glassEel.classList.remove('hidden');

        // Start glass eel at arrival spot
        glassEel.style.left = `${locations.europeArrival.left - glassEel.offsetWidth / 2}px`;
        glassEel.style.top = `${locations.europeArrival.top - glassEel.offsetHeight / 2}px`;

        showCaption(captions.transformingToGlass, glassEel);
         await new Promise(resolve => setTimeout(resolve, 2000)); // Pause for transformation
         hideCaption();

        // Segment 1: Arrival coast to River spot
        showCaption(captions.enteringFreshwater, glassEel);
        await new Promise(resolve => moveElement(glassEel, locations.europeRiver, segmentDurations.arrivalToRiver, resolve));
        hideCaption();


        // --- Stage 6: Yellow Eel - Growth Stage ---
        stageIndicator.textContent = 'שלב: צלופח צהוב - גדילה בנהר';
        glassEel.classList.add('hidden');
        yellowEel.classList.remove('hidden');

        // Ensure yellow eel is positioned at the river spot instantly
         yellowEel.style.setProperty('--transition-duration', '0s');
         yellowEel.style.left = `${locations.europeRiver.left - yellowEel.offsetWidth / 2}px`;
         yellowEel.style.top = `${locations.europeRiver.top - yellowEel.offsetHeight / 2}px`;


        showCaption(captions.growingYellow, yellowEel);
         await new Promise(resolve => setTimeout(resolve, 3000)); // Stay in river briefly
         hideCaption();


        // --- Simulation Complete ---
        stageIndicator.textContent = 'שלב: צלופח צהוב (מחזור חיים הושלם)';
        startButton.disabled = false;
        startButton.textContent = 'התחל מסע מחדש';

         // Reset yellow eel visually to initial position (optional, but nice for loop)
         // updateLocations(); // Recalculate in case of resize
         // yellowEel.style.setProperty('--transition-duration', '1s'); // Add transition for visual reset
         // yellowEel.style.left = `${locations.europeRiver.left - yellowEel.offsetWidth / 2}px`; // Move back to start

         // The yellow eel stays at the river spot where the glass eel arrived, ready for the next run.
         // The 'updateLocations' on resize will correct its position if needed.
    }


    // --- Event Listeners ---
    startButton.addEventListener('click', runSimulation);

    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        if (explanationDiv.classList.contains('hidden')) {
            toggleExplanationButton.textContent = 'גלו את כל הסודות (הסבר מורחב)';
        } else {
            toggleExplanationButton.textContent = 'הסתירו את ההסבר';
        }
    });

    // Update positions on load and resize
    window.addEventListener('load', updateLocations);
    window.addEventListener('resize', updateLocations);

    // Initial state setup
    document.addEventListener('DOMContentLoaded', () => {
        updateLocations(); // Calculate initial positions
         // Ensure only yellow eel is visible initially
        yellowEel.classList.remove('hidden');
        silverEel.classList.add('hidden');
        leptocephalusEel.classList.add('hidden');
        glassEel.classList.add('hidden');
        eelCaption.classList.add('hidden');
        explanationDiv.classList.add('hidden'); // Ensure explanation is hidden initially
    });


</script>
```