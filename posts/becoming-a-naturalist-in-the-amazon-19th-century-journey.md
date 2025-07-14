---
title: "להיות חוקר טבע באמזונס: מסע במאה ה-19"
english_slug: becoming-a-naturalist-in-the-amazon-19th-century-journey
category: "מדעי החיים / ביולוגיה"
tags:
  - חוקרי טבע
  - אמזונס
  - המאה ה-19
  - ביולוגיה
  - היסטוריה של המדע
---
# מסע החוקר אל לב האמזונס הפראי (המאה ה-19)
דמיינו את עצמכם על סירה קטנה בנהר שוצף, מוקפים בקולות הג'ונגל הבלתי נודע. האמזונס במאה ה-19 היה יעד מסוכן אך מפתה לחוקרי טבע אירופאים, אוצר בלום של חיים חדשים למדע. האם יש לכם את מה שנדרש כדי לנווט, לתעד, ולאסוף דגימות בסביבה האקזוטית והמסוכנת ביותר על פני כדור הארץ? צאו למסע, גלו את פלאי הטבע, ותעדו את ממצאיכם במחברת השדה!

<div id="game-container">
    <div id="scene" class="scene river-scene">
        <!-- Interactive elements represented by dynamic markers -->
    </div>

    <div id="notes-panel" class="panel">
        <h3><span class="panel-icon">📝</span> ממצא שדה</h3>
        <p id="item-description"></p>
        <div id="collection-options">
            <!-- Collection buttons loaded by JS -->
        </div>
        <button id="close-notes" class="panel-button">סגור</button>
    </div>

    <div id="notebook-panel" class="panel">
        <h3><span class="panel-icon">📖</span> מחברת תצפיות ודגימות</h3>
        <ul id="notebook-list">
            <!-- Collected items appear here -->
        </ul>
         <div id="score-display">פריטים מתועדים: <span id="collected-count">0</span></div>
    </div>

    <div id="challenge-panel" class="panel">
        <h3 id="challenge-title"><span class="panel-icon">⚠️</span> אירוע בלתי צפוי!</h3>
        <p id="challenge-description"></p>
        <div id="challenge-choices" class="challenge-choices">
            <!-- Challenge choices loaded by JS -->
        </div>
         <div id="challenge-outcome" class="challenge-outcome"></div>
    </div>

     <div id="scene-navigation" class="navigation-buttons">
        <button data-scene="river" class="nav-button">נהר האמזונס</button>
        <button data-scene="forest" class="nav-button">לב הג'ונגל</button>
        <button data-scene="village" class="nav-button">כפר מקומי</button>
    </div>
</div>

<style>
    /* Google Fonts - Example: use fonts that evoke the era/setting */
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Roboto:wght@400;700&display=swap');
     @import url('https://fonts.googleapis.com/css2?family=Old+Standard+TT:ital,wght@0,400;0,700;1,400&display=swap');


    :root {
        --primary-color: #5a4b3b; /* Earthy brown */
        --secondary-color: #d3c7b8; /* Aged paper */
        --accent-color: #8b7a6b; /* Darker paper */
        --background-color: #e0d8cc; /* Light background */
        --panel-bg: rgba(245, 245, 220, 0.98); /* Near white with transparency */
        --border-color: #5a4b3b;
        --text-color: #333;
        --hover-color: #c3b7a8;
         --success-color: #28a745; /* Green */
         --fail-color: #dc3545; /* Red */
    }

    #game-container {
        position: relative;
        width: 100%;
        max-width: 800px;
        height: 500px; /* Fixed height for game area */
        margin: 20px auto;
        border: 3px solid var(--primary-color);
        overflow: hidden;
        background-color: var(--background-color);
        box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.4);
        border-radius: 8px;
    }

    .scene {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-size: cover;
        background-position: center;
        display: none; /* Scenes are hidden by default, JS shows one */
        transition: opacity 1s ease-in-out; /* Smooth scene transition */
        opacity: 0; /* Start hidden for fade-in */
    }

    .scene.active {
         display: block;
         opacity: 1;
    }

    /* Improved Placeholder Images with descriptive text */
    .river-scene {
        background-image: url('https://via.placeholder.com/800x500/637d3f/e0d8cc?text=Amazon+River+Flowing+in+the+1800s');
    }

     .forest-scene {
        background-image: url('https://via.placeholder.com/800x500/3a5a2d/e0d8cc?text=Dense+Amazon+Rainforest');
    }

     .village-scene {
        background-image: url('https://via.placeholder.com/800x500/7d633f/e0d8cc?text=Indigenous+Village+by+the+River');
    }


    .interactive-item {
        position: absolute;
        width: 40px; /* Slightly smaller target */
        height: 40px;
        /* Use a subtle visual cue instead of invisible box */
        background-color: rgba(255, 255, 0, 0); /* Invisible */
        border-radius: 50%; /* Circular hit area */
        cursor: pointer;
        z-index: 10; /* Above background */
        /* Add a subtle shimmer or pulse effect to draw attention */
        animation: pulse-subtle 2s infinite ease-in-out;
        /* Optional: add a small icon image later if needed */
    }

    .interactive-item:hover {
        background-color: rgba(255, 255, 0, 0.2); /* Slight highlight on hover */
        box-shadow: 0 0 10px rgba(255, 255, 0, 0.5);
        animation: none; /* Stop pulsing on hover */
    }

     @keyframes pulse-subtle {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.05); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }


    .panel {
        position: absolute;
        background-color: var(--panel-bg);
        border: 2px solid var(--border-color);
        padding: 20px;
        z-index: 30; /* Above scene and items */
        font-family: 'Old Standard TT', serif;
        box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.4);
        border-radius: 5px;
        transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
        opacity: 0;
        pointer-events: none; /* Initially non-interactive */
    }

    .panel.active {
        opacity: 1;
        pointer-events: all; /* Make interactive when active */
         /* Reset transform for entry animation */
    }


    #notes-panel {
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%) translateY(20px); /* Start slightly lower */
        width: 90%;
        max-width: 450px;
        text-align: center;
    }

     #notes-panel.active {
         transform: translateX(-50%) translateY(0); /* Slide up */
     }

    #notebook-panel {
        top: 20px;
        right: 20px;
        width: 250px; /* Slightly wider */
        height: 400px; /* Adjusted height */
        overflow-y: auto;
        background-color: var(--secondary-color); /* Aged paper color */
        border: 2px solid var(--accent-color);
         font-size: 0.95em;
         transform: translateX(20px); /* Start slightly right */
    }

     #notebook-panel.active {
         transform: translateX(0); /* Slide left */
     }

     #notebook-panel h3 {
         margin-top: 0;
         color: var(--primary-color);
         border-bottom: 1px dashed var(--accent-color);
         padding-bottom: 10px;
     }

     #score-display {
        margin-top: 10px;
        padding-top: 10px;
        border-top: 1px dashed var(--accent-color);
        font-weight: bold;
        color: var(--primary-color);
        text-align: center;
     }


    #challenge-panel {
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) scale(0.9); /* Start slightly smaller */
        width: 80%;
        max-width: 550px;
        text-align: center;
        padding: 30px;
         background-color: rgba(255, 255, 255, 0.95);
    }
     #challenge-panel.active {
         transform: translate(-50%, -50%) scale(1); /* Scale to normal */
     }

    #challenge-panel h3 {
        color: var(--fail-color); /* Warning color */
        margin-top: 0;
        font-size: 1.5em;
    }

     #challenge-description {
         margin-bottom: 20px;
         font-size: 1.1em;
         line-height: 1.5;
     }

    .challenge-choices button {
        margin: 5px;
        padding: 10px 15px;
        border: 1px solid var(--border-color);
        background-color: var(--secondary-color);
        cursor: pointer;
        font-family: 'Old Standard TT', serif;
        font-size: 1em;
        transition: background-color 0.2s ease;
    }

    .challenge-choices button:hover {
        background-color: var(--hover-color);
    }

     .challenge-outcome {
         margin-top: 20px;
         padding-top: 15px;
         border-top: 1px dashed var(--accent-color);
         font-weight: bold;
         min-height: 1.2em; /* Reserve space */
     }
     .challenge-outcome.success { color: var(--success-color); }
     .challenge-outcome.fail { color: var(--fail-color); }


    .panel-button, .navigation-buttons button {
        margin: 5px;
        padding: 10px 15px;
        border: 1px solid var(--primary-color);
        background-color: var(--secondary-color);
        cursor: pointer;
        font-family: 'Old Standard TT', serif;
        font-size: 1em;
        transition: background-color 0.2s ease, transform 0.1s ease;
        border-radius: 4px;
    }

    .panel-button:hover, .navigation-buttons button:hover {
        background-color: var(--hover-color);
        transform: translateY(-2px);
    }
     .panel-button:active, .navigation-buttons button:active {
         transform: translateY(0);
         background-color: var(--accent-color);
     }

    #notebook-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    #notebook-list li {
        border-bottom: 1px dotted var(--accent-color);
        padding: 8px 0;
        font-size: 1em;
        color: var(--text-color);
        display: flex;
        align-items: center;
         line-height: 1.4;
    }

    #notebook-list li .entry-icon {
        margin-left: 8px;
        font-size: 1.2em;
        color: var(--primary-color);
    }


     .navigation-buttons {
        position: absolute;
        bottom: 20px;
        left: 20px;
        z-index: 20;
        display: flex;
        gap: 10px;
     }

     #show-explanation {
        display: block;
        margin: 30px auto;
        padding: 12px 20px;
        border: 2px solid #0056b3;
        background-color: #007bff;
        color: white;
        font-size: 1.1em;
        cursor: pointer;
        border-radius: 5px;
        transition: background-color 0.3s ease;
     }
     #show-explanation:hover {
        background-color: #004085;
     }

     #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #ccc;
        background-color: #f9f9f9;
        display: none; /* Ensures explanation is hidden by default */
        font-family: 'Roboto', sans-serif; /* Modern font for explanation */
        line-height: 1.6;
        border-radius: 8px;
     }

     #explanation h2, #explanation h3 {
        color: #333;
        font-family: 'Merriweather', serif; /* Serif font for headings */
        margin-bottom: 15px;
     }

     .panel-icon {
         margin-left: 5px;
         color: var(--primary-color);
     }
</style>

<button id="show-explanation">הצג רקע והסבר מדעי על המסע</button>

<div id="explanation">
    <h2>מסע אל הלא נודע: חוקרי טבע באמזונס של המאה ה-19</h2>
    <p>במאה ה-19, האמזונס היה אחד האזורים האחרונים שנותרו כמעט בלתי מוכרים למדע המערבי. הוא נחשב לאוצר בלום של חי וצומח אקזוטיים, יעד חלומי לחוקרי טבע שרצו לתאר, לסווג ולאסוף דגימות מהמינים הרבים שהתגלו.</p>

    <h3>מי היו חוקרי הטבע של המאה ה-19 ומה הניע אותם?</h3>
    <p>היו אלו לרוב גברים (ולעיתים נדירות נשים) מאירופה, בעלי רקע באספנות, רפואה, בוטניקה או זואולוגיה. רבים פעלו בחסות מוסדות אקדמיים, מוזיאונים, או אספנים פרטיים. הניע אותם שילוב של סקרנות מדעית טהורה, רצון לתרום לידע האנושי, התלהבות מהתגליות החדשות, ולעיתים גם היבטים כלכליים (מכירת דגימות לאספנים ולמוזיאונים) והרפתקניים.</p>

    <h3>חשיבות האמזונס כיעד לחקר מדעי בתקופה זו</h3>
    <p>המגוון הביולוגי העצום של האמזונס, שכלל אינספור מינים חדשים למדע, הפך אותו למעבדת שדה אולטימטיבית. חקר האמזונס היה חיוני להבנת תפוצת מינים, יחסי גומלין בין אורגניזמים, והגבולות הפיזיולוגיים של חיים בסביבה טרופית קיצונית. הוא סיפק את חומר הגלם הדרוש לגיבוש תורות חדשות בביולוגיה.</p>

    <h3>שיטות עבודה שדה של חוקרי טבע</h3>
    <p>העבודה התבססה בעיקר על תצפית מדוקדקת בטבע, איסוף דגימות (צמחים, חרקים, בעלי חוליות קטנים), רישום מפורט במחברות שדה (כולל סקיצות), ושימור הדגימות. צמחים יובשו ונקשרו, חרקים שומרו באלכוהול או נעצו, בעלי חוליות קטנים שומרו בפורמלין (או אלכוהול). הדגימות נארזו ונשלחו במסע ימי ארוך לאירופה לצורך מחקר וסיווג נוספים.</p>

    <h3>קשיים ואתגרים פיזיים ולוגיסטיים</h3>
    <p>המסע באמזונס במאה ה-19 היה כרוך בסכנות רבות: מחלות טרופיות (מלריה, קדחת צהובה), בעלי חיים מסוכנים (נחשים, עקרבים, יגוארים, דגים טורפים), תנאי שטח קשים (חום, לחות, שטח בוצי, הצפות), ניווט מורכב בנהרות ובג'ונגל, קשיי אספקה ותקשורת, וסיכונים מצד קבוצות אנושיות עוינות או מחלות מקומיות. ציוד מדעי היה בסיסי, ושימור דגימות לטווח ארוך בתנאי לחות היה אתגר.</p>

    <h3>כיצד תצפיות ודגימות מהאמזונס השפיעו על התפתחות תורות כמו האבולוציה והטקסונומיה?</h3>
    <p>הכמות העצומה ומגוון המינים הבלתי נתפסים שנאספו באמזונס (ובאזורים טרופיים אחרים) סיפקו בסיס אמפירי חזק לתורת האבולוציה של דרווין ו-וואלאס. התצפיות על הסתגלויות של אורגניזמים לסביבתם, והגילוי של קבוצות מינים קרובות עם שוני עדין, תמכו ברעיון הברירה הטבעית. בתחום הטקסונומיה (מדע המיון), הדגימות מהאמזונס היו חיוניות להרחבת הידע על ממלכת החי והצומח, ולפיתוח שיטות מיון חדשות המבוססות על קרבה אבולוציונית.</p>

    <h3>ההבדל בין חקר טבע במאה ה-19 לבין שיטות מחקר ביולוגיות מודרניות</h3>
    <p>בעוד שחקר הטבע במאה ה-19 התמקד בעיקר בתצפית, תיאור ואיסוף דגימות למטרות מיון (טקסונומיה מורפולוגית), הביולוגיה המודרנית משתמשת במגוון רחב של כלים מתקדמים: גנטיקה וגנומיקה (זיהוי מינים ויחסים אבולוציוניים באמצעות דנ"א), אקולוגיה כמותית (מודלים סטטיסטיים, ניתוח נתונים גדולים, חישה מרחוק), פיזיולוגיה מודרנית, וטכניקות הדמיה מיקרוסקופיות. המחקר כיום לרוב שיתופי, מבוסס על ציוד מתוחכם, ומאפשר הבנה מעמיקה יותר של תהליכים ביולוגיים ברמה מולקולרית, תאית ואקולוגית.</p>
</div>


<script>
    const gameContainer = document.getElementById('game-container');
    const sceneElement = document.getElementById('scene');
    const notesPanel = document.getElementById('notes-panel');
    const itemDescriptionElement = document.getElementById('item-description');
    const collectionOptionsElement = document.getElementById('collection-options');
    const closeNotesButton = document.getElementById('close-notes');
    const notebookPanel = document.getElementById('notebook-panel');
    const notebookListElement = document.getElementById('notebook-list');
    const scoreDisplay = document.getElementById('collected-count');
    const challengePanel = document.getElementById('challenge-panel');
    const challengeTitleElement = document.getElementById('challenge-title');
    const challengeDescriptionElement = document.getElementById('challenge-description');
    const challengeChoicesElement = document.getElementById('challenge-choices');
    const challengeOutcomeElement = document.getElementById('challenge-outcome');
    const sceneNavigation = document.getElementById('scene-navigation');
    const showExplanationButton = document.getElementById('show-explanation');
    const explanationDiv = document.getElementById('explanation');

    let notebook = [];
    let collectedCount = 0;
    let currentSceneName = 'river'; // Start scene

    const scenes = {
        river: {
            className: 'river-scene',
            items: [
                { id: 'vitoria-regia', top: '60%', left: '30%', type: 'plant', name: 'ויקטוריה רג\'יה', description: 'עלי ענק הצפים על המים, מספיק גדולים כדי לשאת ילד! פרחים לבנים הנפתחים בלילה ונסגרים ביום. אולי זן חדש של חבצלת מים?', collectOptions: [{ text: 'לאסוף דגימת עלה ולייבש', icon: '🌿' }, { text: 'לרשום תצפית במחברת', icon: '✍️' }] },
                { id: 'caiman', top: '40%', left: '70%', type: 'animal', name: 'קיימן', description: 'עיניים בולטות מעל פני המים. תנועה איטית, טורף אורב. מסוכן. יש לשמור מרחק!', collectOptions: [{ text: 'לרשום תצפית במחברת', icon: '✍️' }, { text: 'לנסות ללכוד (מסוכן!)', icon: '⚠️' }] },
                { id: 'strong-current', top: '80%', left: '50%', type: 'phenomenon', name: 'זרם חזק', description: 'הנהר רחב ועוצמתי. הזרם מהיר במיוחד כאן. יש להזהר בניווט הסירה.', collectOptions: [{ text: 'לרשום תצפית במחברת', icon: '✍️' }] },
                { id: 'unidentified-aquatic-plant', top: '50%', left: '10%', type: 'plant', name: 'צמח מים לא מזוהה', description: 'עלי מים צפים בצפיפות. צבע ירוק עמוק. נראה עמיד. מעניין לדעת את מבנהו.', collectOptions: [{ text: 'לאסוף דגימה ולייבש', icon: '🌿' }, { text: 'לרשום תצפית במחברת', icon: '✍️' }] }
            ],
             challenge: {
                 title: 'הסירה מתנדנדת בזרם!',
                 description: 'הזרם החזק מטלטל את הסירה. גלים עולים על הסיפון, הציוד עלול ליפול למים!',
                 choices: [
                     { text: 'אחוז בציוד בחוזקה והמתן', outcome: 'success', resultText: 'החזקת חזק! הסירה עברה את האזור הסוער והציוד נשאר יבש ובטוח.', scoreChange: 5 },
                     { text: 'נסה לחתור במהירות החוצה מהזרם', outcome: 'fail', resultText: 'חתירה מהירה מדי בזרם קשה גרמה למעידה. כמה כלי איסוף קטנים נפלו למים!', scoreChange: -5 }
                 ]
             }
        },
        forest: {
            className: 'forest-scene',
            items: [
                { id: 'exotic-orchid', top: '30%', left: '20%', type: 'plant', name: 'סחלב אקזוטי', description: 'פרח מדהים ביופיו, צבעים עזים וצורה יוצאת דופן. נדיר ביותר, תגלית יקרת ערך!', collectOptions: [{ text: 'לאסוף את הפרח ולייבש בזהירות', icon: '🌸' }, { text: 'לרשום תצפית מפורטת ולצייר', icon: '✍️' }] },
                { id: 'giant-beetle', top: '70%', left: '60%', type: 'animal', name: 'חיפושית גדולה', description: 'חיפושית שריון בצבעים מתכתיים כחול וירוק. זמזום חזק כשהיא עפה. נראית עמידה להפליא.', collectOptions: [{ text: 'ללכוד ולשמר באלכוהול', icon: '🐞' }, { text: 'לרשום תצפית במחברת', icon: '✍️' }] },
                 { id: 'tree-snake', top: '50%', left: '45%', type: 'animal', name: 'נחש עץ ירוק', description: 'נחש ירוק ודק מסתווה היטב בין העלים. נראה רגוע אך רצוי להיזהר - ייתכן שהוא ארסי.', collectOptions: [{ text: 'לרשום תצפית ולצייר סקיצה מהירה', icon: '✍️' }, { text: 'לנסות להתקרב לצילום מקרוב (מסוכן מאוד!)', icon: '☠️' }] },
                 { id: 'aerial-roots', top: '85%', left: '15%', type: 'phenomenon', name: 'שורשי אוויר ענקיים', description: 'עצים עם שורשים ענקיים הנשלחים מטה מהענפים ומשתרשים באדמה. תמיכה נוספת בעץ או דרך לקלוט מים מהאוויר הלח?', collectOptions: [{ text: 'לרשום תצפית במחברת ולתעד את המבנה', icon: '✍️' }] }
            ],
            challenge: {
                 title: 'קולות טורף מהשיחים!',
                 description: 'אתה שומע רשרוש חזק וקול נהמה נמוכה וקרובה. משהו גדול מסתתר שם.',
                 choices: [
                     { text: 'הישאר במקום ללא תנועה והמתן', outcome: 'success', resultText: 'עצרת את נשימתך. הקול מתרחק בהדרגה. החיה (אולי יגואר?) המשיכה בדרכה מבלי שהבחינה בך.', scoreChange: 10 },
                     { text: 'שלוף את הרובה ונסה להפחיד', outcome: 'fail', resultText: 'ניסית להפחיד, אך הרעש רק הגביר את הנהמה והפך אותה לאזהרה ברורה. נאלצת לסגת במהירות תוך כדי אובדן דגימה קטנה.', scoreChange: -10 }
                 ]
             }
        },
         village: {
            className: 'village-scene',
            items: [
                { id: 'local-village', top: '50%', left: '50%', type: 'phenomenon', name: 'כפר מקומי ידידותי', description: 'מקום בטוח יחסית למנוחה, חידוש אספקה, ואיסוף ידע יקר מפז מהתושבים המקומיים על הצמחייה, בעלי החיים, ודרכי ההישרדות.', collectOptions: [{ text: 'לשוחח עם ראש הכפר ולאסוף מידע', icon: '🤝' }, { text: 'לרשום תצפיות על מבנה הכפר ואורח החיים', icon: '✍️' }] },
                { id: 'cacao-tree', top: '60%', left: '30%', type: 'plant', name: 'עץ קקאו טרופי', description: 'עץ נמוך יחסית עם פירות תרמילים צבעוניים המכילים פולי קקאו. משמש את המקומיים להכנת משקה מר וממריץ.', collectOptions: [{ text: 'לשאול את התושבים על שימושי העץ והפרי', icon: '🤝' }, { text: 'לאסוף דגימת פרי ולרשום את מאפייניו', icon: '🍫' }] },
                 { id: 'local-basket', top: '70%', left: '70%', type: 'tool', name: 'סל קלוע מקומי', description: 'סל חזק, גמיש וקלוע בצורה מיוחדת מסיבים מקומיים. שימושי ביותר לנשיאת ציוד ודגימות במסעות ארוכים.', collectOptions: [{ text: 'לקנות סל אחד מהמקומיים', icon: '🛍️' }, { text: 'לרשום ולצייר את אופן הקליעה המיוחד', icon: '✍️' }] }
            ],
             challenge: {
                 title: 'הרגשה רעה...',
                 description: 'אתה מתחיל להרגיש חולשה, כאבי שרירים וחום עולה. אולי נדבקת במחלה טרופית?',
                 choices: [
                     { text: 'השתמש בתרופות אירופאיות מערכת העזרה הראשונה', outcome: 'fail', resultText: 'התרופה האירופאית המודרנית לא הועילה נגד המחלה המקומית. מצבך מחמיר מעט.', scoreChange: -15 },
                     { text: 'בקש עזרה ותרופות מצמחי מרפא מהמקומיים', outcome: 'success', resultText: 'תושב מקומי מנוסה נתן לך חליטה מצמחי מרפא מסורתיים. החום יורד ואתה מתחיל להרגיש טוב יותר!', scoreChange: 15 }
                 ]
             }
        }
    };

    function updateScore(change) {
        collectedCount += change;
        if (collectedCount < 0) collectedCount = 0; // Don't let score go below zero
        scoreDisplay.innerText = collectedCount;
    }

    function loadScene(sceneName) {
        if (currentSceneName === sceneName) return; // Avoid reloading the same scene

        // Hide current scene and panels with animation
        if (scenes[currentSceneName]) {
             const currentSceneElement = document.querySelector('.scene.active');
             if (currentSceneElement) {
                 currentSceneElement.classList.remove('active');
             }
        }
        notesPanel.classList.remove('active');
        challengePanel.classList.remove('active');


        // Remove old interactive items after fade out
        setTimeout(() => {
            document.querySelectorAll('.interactive-item').forEach(item => item.remove());

            // Show the selected scene
            currentSceneName = sceneName;
            const sceneData = scenes[sceneName];
            sceneElement.className = 'scene ' + sceneData.className;
            sceneElement.classList.add('active'); // Add active class for fade-in

            // Add interactive items for the new scene
            sceneData.items.forEach(itemData => {
                const itemElement = document.createElement('div');
                itemElement.classList.add('interactive-item');
                itemElement.style.top = itemData.top;
                itemElement.style.left = itemData.left;
                // Store all item data in dataset
                Object.keys(itemData).forEach(key => {
                    if (typeof itemData[key] !== 'object') { // Avoid storing objects directly
                         itemElement.dataset[key] = itemData[key];
                    }
                });
                 itemElement.dataset.collectOptions = JSON.stringify(itemData.collectOptions);


                // Simple visual marker (could be an image later)
                 const marker = document.createElement('span');
                 marker.innerText = '✨'; // Placeholder icon
                 marker.style.fontSize = '2em';
                 marker.style.position = 'absolute';
                 marker.style.transform = 'translate(-50%, -50%)';
                 itemElement.appendChild(marker);


                itemElement.addEventListener('click', () => showNotes(itemData));
                sceneElement.appendChild(itemElement);
            });

             // Potentially trigger a challenge when entering a new scene
             // Add a random chance or specific condition later if needed
            if (sceneData.challenge) {
                 // Simple delay to show challenge after scene loads
                 setTimeout(() => showChallenge(sceneData.challenge), 2500); // Delay increased for transition
            }
        }, 1000); // Wait for fade out (CSS transition duration)
    }

    function showNotes(itemData) {
        itemDescriptionElement.innerText = itemData.description;
        collectionOptionsElement.innerHTML = ''; // Clear previous options
        challengePanel.classList.remove('active'); // Hide challenge if open

        const options = JSON.parse(itemData.dataset.collectOptions); // Get options from dataset
        options.forEach(option => {
            const button = document.createElement('button');
            button.innerText = `${option.icon || ''} ${option.text}`;
            button.addEventListener('click', () => collectItem(itemData.name, option.text, option.icon));
            collectionOptionsElement.appendChild(button);
        });

        notesPanel.classList.add('active'); // Show with animation
    }

    function collectItem(itemName, collectionMethod, icon = '') {
        const entryText = `${icon} [${collectionMethod}] ${itemName}`;
        // Avoid adding the same exact entry multiple times? Or allow duplicates?
        // For simplicity, let's just add every collection action.
        notebook.push(entryText);
        updateNotebook();
        updateScore(5); // Add points for documenting/collecting

        notesPanel.classList.remove('active'); // Hide with animation
    }

    function updateNotebook() {
        notebookListElement.innerHTML = ''; // Clear current list
        notebook.forEach(itemText => {
            const li = document.createElement('li');
            // Split icon and text for potential styling
            const match = itemText.match(/(\S+)\s\[(.*?)\]\s(.*)/);
            if (match) {
                const icon = match[1];
                const method = match[2];
                const name = match[3];
                 li.innerHTML = `<span class="entry-icon">${icon}</span> <strong>[${method}]</strong> ${name}`;
            } else {
                 li.innerText = itemText; // Fallback
            }
            notebookListElement.appendChild(li);
        });
         // Scroll to bottom of notebook?
         notebookPanel.scrollTop = notebookPanel.scrollHeight;
    }

    function showChallenge(challengeData) {
        // Prevent showing challenge if another panel is open
        if (notesPanel.classList.contains('active')) {
             // Re-schedule challenge? Or just skip? Let's just skip for simplicity.
             console.log("Notes panel open, skipping challenge for now.");
             return;
        }

        challengeTitleElement.innerText = challengeData.title;
        challengeDescriptionElement.innerText = challengeData.description;
        challengeChoicesElement.innerHTML = ''; // Clear previous choices
        challengeOutcomeElement.innerText = ''; // Clear previous outcome
        challengeOutcomeElement.className = 'challenge-outcome'; // Reset class

        challengeData.choices.forEach(choice => {
            const button = document.createElement('button');
            button.innerText = choice.text;
            button.addEventListener('click', () => handleChallengeChoice(choice));
            challengeChoicesElement.appendChild(button);
        });

        challengePanel.classList.add('active'); // Show with animation
         // Disable scene navigation or interactions during challenge? Yes, temporarily.
         sceneNavigation.style.pointerEvents = 'none';
         document.querySelectorAll('.interactive-item').forEach(item => item.style.pointerEvents = 'none');
    }

    function handleChallengeChoice(choice) {
        // Display outcome
        challengeOutcomeElement.innerText = choice.resultText;
        challengeOutcomeElement.classList.add(choice.outcome);

        // Update score based on outcome
        if (choice.scoreChange) {
             updateScore(choice.scoreChange);
             // Add score change feedback?
             const scoreFeedback = document.createElement('span');
             scoreFeedback.innerText = ` (${choice.scoreChange > 0 ? '+' : ''}${choice.scoreChange} נקודות)`;
             scoreFeedback.style.color = choice.outcome === 'success' ? 'var(--success-color)' : 'var(--fail-color)';
              scoreFeedback.style.fontWeight = 'normal';
              scoreOutcomeElement.appendChild(scoreFeedback);
        }

        // Disable choices and show a 'continue' button
        challengeChoicesElement.innerHTML = '<button id="close-challenge" class="panel-button">המשך המסע</button>';
        document.getElementById('close-challenge').addEventListener('click', () => {
             challengePanel.classList.remove('active');
             // Re-enable interactions
             sceneNavigation.style.pointerEvents = 'all';
             document.querySelectorAll('.interactive-item').forEach(item => item.style.pointerEvents = 'all');
        });

        // Optional: Add more complex outcomes like adding an item, removing an item, etc.
        if (choice.outcome === 'success') {
             // Maybe add a 'successful event' entry to notebook?
              notebook.push(`✅ [אתגר הושלם] ${choice.resultText.split('.')[0]}`); // Log event
              updateNotebook();
        } else if (choice.outcome === 'fail') {
            // Maybe add a 'difficulty' entry to notebook?
             notebook.push(`❌ [קשיים במסע] ${choice.resultText.split('.')[0]}`); // Log event
             updateNotebook();
        }
    }


    // Event listeners
    closeNotesButton.addEventListener('click', () => notesPanel.classList.remove('active'));

    sceneNavigation.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', () => {
            loadScene(button.dataset.scene);
            notesPanel.classList.remove('active'); // Hide notes when changing scene
            challengePanel.classList.remove('active'); // Hide challenge when changing scene
        });
    });

    showExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        showExplanationButton.innerText = isHidden ? 'הסתר רקע והסבר מדעי' : 'הצג רקע והסבר מדעי על המסע';

        // Scroll to the explanation if showing
        if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });


    // Initialize the game
    loadScene(currentSceneName);
    updateNotebook(); // Show empty notebook initially
    updateScore(0); // Display initial score (0)
    // Ensure notebook panel is initially visible
    notebookPanel.classList.add('active');


</script>
```