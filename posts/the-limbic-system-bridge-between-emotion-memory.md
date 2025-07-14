---
title: "המערכת הלימבית: הגשר בין רגש לזיכרון"
english_slug: the-limbic-system-bridge-between-emotion-memory
category: "פסיכולוגיה"
tags: [מוח, מערכת לימבית, רגשות, זיכרון]
---
# המערכת הלימבית: הגשר הסודי בין רגש לזיכרון

האם תהיתם פעם למה אנחנו זוכרים כל כך טוב רגעים טעונים רגשית – אותה חופשה בלתי נשכחת, הפעם הראשונה שעליתם על במה, או בחינה שגרמה לדופק לזנק? מסתבר שלא מדובר בצירוף מקרים. יש אזור סודי וקסום במוח שלנו, שמשמש גשר רב עוצמה בין עולם הרגש הסוער לבין היכולת שלנו לאגור ולשלוף זיכרונות. בואו נחקור אותו יחד!

<div class="limbic-app-container">
    <div class="brain-model">
        <h2>המוח הרגשי (מבט מבפנים)</h2>
        <div id="limbic-system-area" class="limbic-system-area">
             <div id="amygdala" class="brain-part" data-part="amygdala" title="אמיגדלה: מרכז הרגש!">אמיגדלה</div>
             <div id="hippocampus" class="brain-part" data-part="hippocampus" title="היפוקמפוס: מפעל הזיכרון!">היפוקמפוס</div>
             <div id="hypothalamus" class="brain-part" data-part="hypothalamus" title="היפותלמוס: מפקד התגובה הגופנית!">היפותלמוס</div>
             <div id="thalamus" class="brain-part" data-part="thalamus" title="תלמוס: תחנת הממסר המרכזית!">תלמוס</div>
             <div id="cingulate-cortex" class="brain-part" data-part="cingulate-cortex" title="קורטקס סינגולרי: מיתוג כאב, רגש וזיכרון!">קורטקס סינגולרי</div>
             <div id="info-display" class="info-display"><p>לחצו על חלק במוח כדי לגלות את סודותיו...</p></div>
             <!-- Animation elements that can move from parts to memory -->
             <div id="emotion-signal" class="signal-animation emotion-signal"></div>
             <div id="memory-signal" class="signal-animation memory-signal"></div>
        </div>
    </div>
    <div class="interaction-panel">
        <h2>המעבדה הלימבית</h2>
        <div class="memory-area">
            <h3>מצב הזיכרון</h3>
            <div id="virtual-memory" class="virtual-memory">
                <p>זיכרון רגיל</p>
            </div>
            <p class="interaction-hint">לחצו על <strong>האמיגדלה</strong> (רגש) ו<strong>ההיפוקמפוס</strong> (זיכרון) כדי לראות איך רגש "צובע" ומחזק זיכרונות!</p>
        </div>
         <!-- Animation area visually connected to the memory -->
         <div id="memory-animation-target" class="animation-target"></div>
    </div>
</div>

<style>
    :root {
        --limbic-bg-color: #f0f4f8; /* Light blue-grey */
        --container-border-color: #cce0ff; /* Light blue */
        --brain-area-bg: #e3f2fd; /* Pale blue */
        --brain-border-color: #64b5f6; /* Medium blue */
        --brain-part-bg: #90caf9; /* Light blue part */
        --brain-part-border: #2196f3; /* Blue part border */
        --brain-part-hover-bg: #64b5f6; /* Medium blue hover */
        --info-display-bg: rgba(255, 255, 255, 0.95);
        --info-display-border: #42a5f5; /* Slightly darker blue */
        --memory-default-bg: #e0e0e0; /* Grey default */
        --memory-default-border: #bdbdbd;
        --memory-emotional-bg: #fff9c4; /* Pale yellow for emotional influence */
        --memory-emotional-border: #ffeb3b;
        --memory-strong-bg: #ffeb3b; /* Bright yellow for strong */
        --memory-strong-border: #fbc02d;
        --memory-strong-shadow: rgba(255, 235, 59, 0.6);
        --emotion-color: #ef5350; /* Red */
        --memory-color: #42a5f5; /* Blue */
        --combined-color: #ffb300; /* Orange/Gold */
        --button-bg: #1976d2; /* Darker blue */
        --button-hover-bg: #1565c0;
        --explanation-bg: #e1f5fe; /* Very pale blue */
        --explanation-border: #b3e5fc;
        --explanation-heading-color: #0d47a1; /* Dark blue */
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f4f4; /* Soft background */
        padding: 10px;
    }

    h1 {
        text-align: center;
        color: #0d47a1;
        margin-bottom: 30px;
    }

    .limbic-app-container {
        display: flex;
        flex-direction: column;
        gap: 30px;
        max-width: 900px; /* Slightly wider */
        margin: 20px auto;
        padding: 30px;
        border: 1px solid var(--container-border-color);
        border-radius: 12px;
        background-color: var(--limbic-bg-color);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }

    @media (min-width: 768px) {
         .limbic-app-container {
            flex-direction: row;
            gap: 40px; /* More space */
         }
         .brain-model, .interaction-panel {
            flex: 1;
         }
         .brain-model {
             margin-right: 20px; /* Visual separation */
         }
    }

    .brain-model, .interaction-panel {
        padding: 20px;
        border: 1px solid var(--container-border-color);
        border-radius: 10px;
        background-color: #ffffff; /* White panel backgrounds */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
    }


    .brain-model h2, .interaction-panel h2 {
        text-align: center;
        color: var(--explanation-heading-color);
        margin-top: 0;
        margin-bottom: 20px;
    }

    .limbic-system-area {
        position: relative;
        width: 100%;
        padding-bottom: 65%; /* Aspect ratio height (relative to width) */
        height: 0; /* Override height for aspect ratio */
        border: 2px dashed var(--brain-border-color);
        border-radius: 20px;
        background: radial-gradient(circle, var(--brain-area-bg) 0%, #c5e9f7 100%); /* Gradient background */
        overflow: hidden;
        box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px; /* Space for info display */
    }

    .brain-part {
        position: absolute;
        padding: 10px 15px;
        background-color: var(--brain-part-bg);
        border: 1px solid var(--brain-part-border);
        border-radius: 20px; /* More rounded */
        cursor: pointer;
        font-size: 0.9em;
        text-align: center;
        transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.2s ease;
        z-index: 2; /* Above info display and signals */
        color: #333;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .brain-part:hover {
        background-color: var(--brain-part-hover-bg);
        transform: translateY(-3px) scale(1.02); /* Lift and slightly scale */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

     .brain-part:active {
        transform: scale(0.98);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
     }


    /* Positioning (Adjusted for better visual flow and space) */
    #amygdala { top: 45%; left: 10%; transform: translate(-50%, -50%); } /* More central, less cornered */
    #hippocampus { top: 60%; left: 25%; transform: translate(-50%, -50%); } /* Near amygdala */
    #hypothalamus { top: 40%; left: 45%; transform: translate(-50%, -50%); } /* More central */
    #thalamus { top: 25%; left: 55%; transform: translate(-50%, -50%); } /* Above hypothalamus */
    #cingulate-cortex { top: 10%; left: 30%; transform: translate(-50%, -50%); } /* Towards the top */


    .info-display {
        position: absolute;
        bottom: 5%; /* Relative to limbic-system-area height */
        left: 5%;
        right: 5%;
        width: 90%;
        background-color: var(--info-display-bg);
        padding: 12px;
        border-radius: 8px;
        min-height: 50px; /* Ensure visibility */
        text-align: center;
        font-style: italic;
        color: #555;
        border: 1px solid var(--info-display-border);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
        z-index: 1; /* Below parts */
        transition: opacity 0.3s ease-in-out;
    }

    .info-display p {
        margin: 0;
    }


    .interaction-panel {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px; /* More space */
    }

    .memory-area {
        text-align: center;
        margin-bottom: 20px;
    }

    .memory-area h3 {
        color: var(--explanation-heading-color);
        margin-bottom: 10px;
    }

     .interaction-hint {
         font-size: 0.9em;
         color: #555;
         max-width: 250px;
         margin: 10px auto 0;
     }

    .virtual-memory {
        width: 120px; /* Larger circle */
        height: 120px;
        border-radius: 50%;
        background-color: var(--memory-default-bg);
        border: 3px dashed var(--memory-default-border);
        margin: 15px auto;
        display: flex;
        flex-direction: column; /* Text on multiple lines */
        justify-content: center;
        align-items: center;
        font-size: 0.9em;
        color: #555;
        transition: background-color 0.6s ease-in-out, border-color 0.6s ease-in-out, box-shadow 0.6s ease-in-out, transform 0.3s ease-in-out;
        font-weight: normal;
        padding: 10px;
        box-sizing: border-box; /* Include padding in size */
    }

     .virtual-memory p {
         margin: 0;
     }

    .memory-default {
         background-color: var(--memory-default-bg);
         border-color: var(--memory-default-border);
         color: #555;
         font-weight: normal;
         box-shadow: none;
         transform: scale(1);
    }

     .memory-emotional {
        background-color: var(--memory-emotional-bg);
        border-color: var(--memory-emotional-border);
        color: #333;
        font-weight: normal;
        box-shadow: 0 0 8px var(--memory-emotional-border);
        transform: scale(1.03); /* Slightly larger */
     }


    .memory-strong {
        background-color: var(--memory-strong-bg);
        border-color: var(--memory-strong-border);
        box-shadow: 0 0 15px var(--memory-strong-shadow); /* More prominent glow */
        font-weight: bold;
        color: #000;
         transform: scale(1.08); /* Even larger */
    }

     .memory-strong p {
         animation: text-pop 0.5s ease-out; /* Animation for text */
     }

    @keyframes text-pop {
        0% { transform: scale(0.9); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }


    .animation-target {
        /* Placeholder/target for signals */
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background-color: rgba(var(--combined-color, #ffb300), 0.3); /* Subtle visual link */
        border: 2px dashed var(--combined-color, #ffb300);
        margin-top: 10px;
         opacity: 0.7;
         position: absolute; /* Position within the brain model area */
         bottom: 15%;
         left: 75%;
         transform: translate(-50%, -50%);
         z-index: 0; /* Below everything */
    }


    .signal-animation {
        position: absolute;
        width: 15px; /* Smaller */
        height: 15px;
        border-radius: 50%;
        opacity: 0;
        transform: translate(-50%, -50%) scale(0.5); /* Start small from center */
        pointer-events: none; /* Don't interfere with clicks */
        z-index: 3; /* Above parts and info */
    }

     .emotion-signal {
         background-color: var(--emotion-color); /* Red */
         box-shadow: 0 0 8px var(--emotion-color);
     }

      .memory-signal {
         background-color: var(--memory-color); /* Blue */
          box-shadow: 0 0 8px var(--memory-color);
     }

    @keyframes signal-flow {
        0% {
            opacity: 0.8;
            transform: translate(-50%, -50%) scale(0.5);
        }
        20% {
             opacity: 1;
             transform: translate(-50%, -50%) scale(1);
        }
        80% {
            opacity: 0.8;
            transform: translate(var(--target-x), var(--target-y)) scale(0.8);
        }
        100% {
            opacity: 0;
            transform: translate(var(--target-x), var(--target-y)) scale(0.5);
        }
    }

    .signal-active {
         animation: signal-flow 1.5s cubic-bezier(0.4, 0, 0.6, 1) forwards; /* Smoother timing */
    }


    #toggle-explanation {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 25px; /* Larger padding */
        font-size: 1.1em; /* Slightly larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--button-bg);
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    }

    #toggle-explanation:hover {
        background-color: var(--button-hover-bg);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
     #toggle-explanation:active {
        transform: translateY(0);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
     }


    #explanation {
        margin-top: 20px;
        padding: 20px; /* More padding */
        border: 1px solid var(--explanation-border);
        border-radius: 10px;
        background-color: var(--explanation-bg);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
    }

    #explanation h2, #explanation h3 {
        color: var(--explanation-heading-color);
        margin-bottom: 10px;
    }

     #explanation h3 {
         margin-top: 20px; /* More space above */
         margin-bottom: 8px;
     }

    #explanation p {
        margin-bottom: 15px; /* More space below paragraphs */
        line-height: 1.7; /* Better readability */
        color: #444;
    }

    #explanation strong {
        color: #0d47a1; /* Highlight key terms */
    }

</style>

<button id="toggle-explanation">הצג הסבר מורחב: מסע לעומק המוח הלימבי</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מורחב: המערכת הלימבית - המרכז הרגשי והזכרוני של המוח</h2>

    <h3>הקדמה: מהי המערכת הלימבית ומה תפקידה?</h3>
    דמיינו את המוח כעיר סואנת, והמערכת הלימבית היא הלב הפועם שלה – רשת מסועפת של מבנים הממוקמים עמוק בפנים, מתחת לשכבות הקורטקס המודע. היא אינה מבנה יחיד אלא "קבוצת עבודה" מתוחכמת של אזורים שונים, הממלאת תפקידי מפתח בוויסות רגשות, דחפים, מוטיבציה, למידה, והכי חשוב לענייננו – יצירת זיכרונות, במיוחד אלו הטעונים ברגש עז. היא הגשר שמחבר בין העולם הפנימי שלנו לתגובותינו החיצוניות והפנימיות.

    <h3>השחקנים המרכזיים: מבנים ותפקידים</h3>
    <p>
    🧠 <strong>האמיגדלה:</strong> המבנה הקטן אך רב העוצמה הזה, שצורתו מזכירה שקד, הוא "גלאי הרגשות" האישי שלכם. הוא מגיב במהירות מסחררת לגירויים רגשיים – פחד מפני סכנה, התרגשות משמחה גדולה, כעס או תסכול. האמיגדלה היא זו שמפעילה את אזעקת "הילחם או ברח" במקרה של סכנה, והיא גם זו שמקשרת רגשות ספציפיים לאירועים ויוצרת "חותם רגשי" על חוויות. היא מעין "מגבר רגשי" לזיכרונות.
    </p>
    <p>
    🌊 <strong>ההיפוקמפוס:</strong> דמיינו סוסון ים ימי, זו צורתו של ההיפוקמפוס. הוא מפעל הזיכרון המרכזי שלכם ליצירת זיכרונות "אפיזודיים" – זיכרונות של אירועים ספציפיים שקרו לכם: הפעם הראשונה שלמדתם לרכוב על אופניים, איפה חגגתם יום הולדת לפני שנתיים, או הפנים של האדם שפגשתם אתמול. הוא קולט מידע חדש, מעבד אותו, ומכין אותו לאחסון ארוך טווח באזורים אחרים במוח. הוא גם המצפן הפנימי שלכם, חיוני לניווט מרחבי.
    </p>
    <p>
    🎯 <strong>ההיפותלמוס:</strong> מפקד התזמורת הפנימית! מבנה זעיר זה מקשר בין המוח לבין המערכת ההורמונלית והעצבית האוטונומית. הוא מווסת תגובות גופניות חיוניות המלוות רגשות: קצב לב, לחץ דם, טמפרטורה, רעב, צמא, ואפילו דפוסי שינה ותגובת מתח (שחרור קורטיזול). הוא מתרגם את המסרים הרגשיים של האמיגדלה לשפת הגוף.
    </p>
    <p>
    🚦 <strong>התלמוס:</strong> תחנת הממסר העירונית של המוח. כמעט כל מידע חושי מהעולם (חוץ מריח) עובר דרכו בדרכו לקורטקס לעיבוד מודע. אך התלמוס אינו רק נתיב; חלקיו קשורים גם לוויסות מודעות, תשומת לב, ולמעבר מידע רגשי וזיכרוני אל ובתוך המערכת הלימבית.
    </p>
    <p>
    ✨ <strong>הקורטקס הסינגולרי (חלק מחגורת הסינגולום):</strong> שכבה חיצונית יותר במערכת הלימבית, המעורבת בטווח רחב של תפקודים גבוהים: קבלת החלטות מורכבות, בקרת אימפולסיביות, ויסות רגשי (במיוחד התמודדות עם כאב רגשי או פיזי), ואפילו היבטים מסוימים של זיכרון עבודה ומוטיבציה. הוא עוזר לשלב מידע רגשי עם קוגניציה.
    </p>

    <h3>כימיה של זיכרונות: הקשר אמיגדלה-היפוקמפוס</h3>
    הקסם של זיכרונות רגשיים קורה בחיבור בין האמיגדלה להיפוקמפוס. כשאנו חווים אירוע מלווה ברגש חזק – פחד עז, שמחה אקסטטית, הפתעה גדולה – האמיגדלה "נדלקת" ושולחת אותות דחופים להיפוקמפוס. אותות אלו משמשים כמעין "זרקור" שאומר להיפוקמפוס: "היי! האירוע הזה חשוב! תקודד אותו חזק, עכשיו!". כתוצאה מכך, ההיפוקמפוס פועל ביעילות מוגברת, והזיכרון מאותו אירוע מקודד באופן עמוק ומפורט יותר. לכן, רגעים רגשיים נצרבים בזיכרון שלנו בעוצמה רבה יותר מאשר אירועים ניטרליים.

    <h3>צלקות רגשיות: השפעת מתח וטראומה</h3>
    לצד יכולתה המופלאה, המערכת הלימבית גם פגיעה. מתח כרוני או חשיפה לטראומה יכולים לגרום לשינויים דרמטיים בה. ההיפוקמפוס רגיש להורמוני מתח כמו קורטיזול, וחשיפה ממושכת עלולה לפגוע בתאי העצב בו, להקטין את גודלו ולפגוע ביכולתו ליצור זיכרונות חדשים. בו בזמן, האמיגדלה עלולה להפוך לרגישה ופעילה יתר על המידה, מה שמוביל לתגובתיות יתר לגירויי פחד ולקשיי ויסות רגשי. תופעה זו בולטת במצבים כמו הפרעת דחק פוסט-טראומטית (PTSD), בה זיכרונות טראומטיים צפים שוב ושוב כאילו התרחשו בהווה.

    <h3>בשורה התחתונה:</h3>
    המערכת הלימבית היא הליבה הרגשית והזיכרונית של המוח, המאפשרת לנו לחוות את העולם בעושר רגשי, ללמוד מחוויותינו, וליצור את סיפור חיינו דרך זיכרונות עמוקים. הבנת פעילותה המשותפת של האמיגדלה וההיפוקמפוס מספקת לנו הצצה מדהימה לאופן בו רגשות מעצבים את הזהות שלנו, זכרונותינו והתנהגותנו. היא הבסיס לחלקים רבים כל כך של החוויה האנושית.
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const brainParts = document.querySelectorAll('.brain-part');
        const infoDisplay = document.getElementById('info-display');
        const virtualMemory = document.getElementById('virtual-memory');
        const toggleButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const emotionSignal = document.getElementById('emotion-signal');
        const memorySignal = document.getElementById('memory-signal');
        const brainArea = document.getElementById('limbic-system-area'); // Reference the brain area for positioning
        const memoryTarget = document.getElementById('memory-animation-target'); // Reference the visual memory target

        const partInfo = {
            'amygdala': {
                name: 'האמיגדלה',
                role: 'מרכז הרגש: מגיבה לפחד, שמחה, כעס ויוצרת חותם רגשי.',
                signal: emotionSignal
            },
            'hippocampus': {
                name: 'ההיפוקמפוס',
                role: 'מפעל הזיכרון: יוצר זיכרונות חדשים של אירועים ומקומות.',
                signal: memorySignal
            },
            'hypothalamus': {
                name: 'ההיפותלמוס',
                role: 'מפקד הגוף: מווסת תגובות פיזיות הקשורות לרגש (דופק, מתח).',
                signal: null // No specific signal animation for this
            },
            'thalamus': {
                name: 'התלמוס',
                role: 'תחנת ממסר: מעביר מידע חושי, קשור לרגש וזיכרון.',
                 signal: null
            },
            'cingulate-cortex': {
                name: 'הקורטקס הסינגולרי',
                role: 'בקר רגש/זיכרון: קשור להחלטות, ויסות כאב ורגש.',
                signal: null
            }
        };

        let lastAmygdalaClickTime = 0;
        let lastHippocampusClickTime = 0;
        const activeDuration = 3000; // Timeframe for combined effect in ms

        // Function to get the absolute position of an element relative to its parent
        function getRelativePosition(element, parent) {
            const parentRect = parent.getBoundingClientRect();
            const elementRect = element.getBoundingClientRect();
            return {
                top: elementRect.top - parentRect.top,
                left: elementRect.left - parentRect.left
            };
        }

        // Function to trigger animation
        function triggerSignalAnimation(signalElement, startElement) {
            const startPos = getRelativePosition(startElement, brainArea);
            const targetPos = getRelativePosition(memoryTarget, brainArea); // Animate towards the visual target

            // Set initial position at the center of the start element
            signalElement.style.top = `${startPos.top + startElement.offsetHeight / 2}px`;
            signalElement.style.left = `${startPos.left + startElement.offsetWidth / 2}px`;

            // Calculate target position relative to initial position (for transform translate)
            const targetX_relative = targetPos.left + memoryTarget.offsetWidth / 2 - (startPos.left + startElement.offsetWidth / 2);
            const targetY_relative = targetPos.top + memoryTarget.offsetHeight / 2 - (startPos.top + startElement.offsetHeight / 2);


            // Set CSS variables for the animation
            signalElement.style.setProperty('--target-x', `${targetX_relative}px`);
            signalElement.style.setProperty('--target-y', `${targetY_relative}px`);


            // Trigger animation by removing and adding the class
            signalElement.classList.remove('signal-active');
            void signalElement.offsetWidth; // Trigger reflow to restart animation
            signalElement.classList.add('signal-active');
        }


        brainParts.forEach(part => {
            part.addEventListener('click', () => {
                const partId = part.dataset.part;
                const info = partInfo[partId];

                // Update info display
                if (info) {
                    infoDisplay.innerHTML = `<p><strong>${info.name}:</strong> ${info.role}</p>`; // Use innerHTML for strong tag

                    // Trigger specific animation if available
                    if (info.signal) {
                         triggerSignalAnimation(info.signal, part);
                    }

                    // Update click times for A and H
                    const now = Date.now();
                    if (partId === 'amygdala') {
                        lastAmygdalaClickTime = now;
                    } else if (partId === 'hippocampus') {
                        lastHippocampusClickTime = now;
                    }

                    // Check for combined effect or individual influence
                    const isAmygdalaRecent = (now - lastAmygdalaClickTime) < activeDuration;
                    const isHippocampusRecent = (now - lastHippocampusClickTime) < activeDuration;

                    // Reset memory classes first
                    virtualMemory.classList.remove('memory-strong', 'memory-emotional', 'memory-default');

                    if (isAmygdalaRecent && isHippocampusRecent) {
                        virtualMemory.classList.add('memory-strong');
                        virtualMemory.innerHTML = '<p>זיכרון רגשי</p><p><strong>חזק נוצר!</strong></p>';
                        // Optionally reset timers after combined effect triggers
                        lastAmygdalaClickTime = 0;
                        lastHippocampusClickTime = 0;
                    } else if (isAmygdalaRecent) {
                         virtualMemory.classList.add('memory-emotional');
                         virtualMemory.innerHTML = '<p>זיכרון רגיל</p><p>(מושפע מרגש)</p>';
                         // If only Amygdala was clicked recently, but not Hippocampus, reset Hippocampus timer
                         lastHippocampusClickTime = 0;
                    } else if (isHippocampusRecent) {
                         virtualMemory.classList.add('memory-default'); // Or a specific class for non-emotional memory
                         virtualMemory.innerHTML = '<p>זיכרון</p><p>(רגיל נקלט)</p>';
                         // If only Hippocampus was clicked recently, reset Amygdala timer
                          lastAmygdalaClickTime = 0;
                    } else {
                        // Default state if neither is recent
                         virtualMemory.classList.add('memory-default');
                         virtualMemory.innerHTML = '<p>זיכרון רגיל</p><p>...</p>';
                    }
                }
            });
        });

        // Toggle explanation visibility
        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצג הסבר מורחב: מסע לעומק המוח הלימבי';
             // Scroll to explanation if showing
             if (isHidden) {
                explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
             }
        });

        // Initial state for memory text
         virtualMemory.classList.add('memory-default');
         virtualMemory.innerHTML = '<p>זיכרון רגיל</p><p>...</p>'; // Initial state text
    });
</script>
```