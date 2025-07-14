---
title: "הפלסטיות הסינפטית: מסע אל תוך הזיכרון והלמידה במוח"
english_slug: synaptic-plasticity-how-brain-learns-remembers-v2
category: "מדעי המוח"
tags: [סינפסה, פלסטיות, למידה, זיכרון, נוירונים, נוירוביולוגיה]
---

# הפלסטיות הסינפטית: מסע אל תוך הזיכרון והלמידה במוח

האם אי פעם עצרתם לחשוב איך אתם זוכרים את שמו של חבר חדש, לומדים מיומנות חדשה כמו רכיבה על אופניים, או פשוט זוכרים היכן הנחתם את המפתחות? הקסם הזה מתרחש ברמה המיקרוסקופית, בנקודות החיבור הזעירות בין תאי העצב במוח - הסינפסות. והדבר המדהים ביותר הוא שהסינפסות הללו אינן סטטיות; הן משתנות כל הזמן, מתחזקות או נחלשות בתגובה לכל חוויה ולכל פיסת מידע. היכולת המדהימה הזו, הנקראת **פלסטיות סינפטית**, היא אבן היסוד לאופן שבו המוח שלנו לומד, מסתגל, ובונה את עולם הזיכרונות והידע שלנו. בואו נחקור אותה באמצעות סימולציה אינטראקטיבית!

<div id="synapse-simulation">
    <h2>חקרו את הסינפסה</h2>
    <div class="synapse-area">
        <div class="neuron pre-synaptic" id="pre-synaptic">
             <div class="neuron-label">נוירון שולח</div>
            <div class="vesicles-area">
                <div class="synaptic-vesicle"></div>
                <div class="synaptic-vesicle"></div>
                <div class="synaptic-vesicle"></div>
                <div class="synaptic-vesicle"></div>
            </div>
             <div class="signal-flow pre-signal"></div>
        </div>
        <div class="synaptic-cleft" id="synaptic-cleft">
             <div class="neurotransmitter-burst" id="neurotransmitter-burst"></div>
        </div>
        <div class="neuron post-synaptic" id="post-synaptic">
            <div class="neuron-label">נוירון מקבל</div>
            <div class="receptors-area" id="receptors-area">
                </div>
             <div class="signal-flow post-signal"></div>
             <div class="response-indicator" id="response-indicator"></div>
        </div>
    </div>
    <div class="controls">
        <button id="send-signal-btn">שלח אות עצבי</button>
        <button id="send-strong-series-btn">שלח רצף חזק (חיזוק - LTP)</button>
        <button id="send-weak-series-btn">שלח רצף חלש (החלשה - LTD)</button>
        <button id="reset-btn">אפס סימולציה</button>
        <div class="status">חוזק סינפסה: <span id="synapse-strength">רגיל</span></div>
    </div>
</div>

<style>
    :root {
        --neuron-color: #E0F2F7; /* Light Cyan */
        --cleft-color: #BBDEFB; /* Light Blue */
        --pre-synaptic-border: #0277BD; /* Dark Blue */
        --post-synaptic-border: #0288D1; /* Blue */
        --vesicle-color: #FF8A65; /* Light Salmon */
        --neurotransmitter-color: #81C784; /* Light Green */
        --receptor-color: #4DB6AC; /* Teal */
        --receptor-bound-color: #FFD54F; /* Amber */
        --signal-color: #FFEB3B; /* Yellow */
        --ltp-color-tint: #C8E6C9; /* Light Green Tint */
        --ltd-color-tint: #FFCDD2; /* Light Red Tint */
        --text-color: #333;
        --control-button-bg: #039BE5; /* Blue */
        --control-button-hover: #0277BD; /* Darker Blue */
        --reset-button-bg: #EF5350; /* Red */
        --reset-button-hover: #D32F2F; /* Darker Red */
    }

    #synapse-simulation {
        border: 2px solid var(--pre-synaptic-border);
        padding: 30px;
        margin: 30px 0;
        background-color: #E1F5FE; /* Extra Light Blue */
        border-radius: 12px;
        font-family: 'Heebo', sans-serif; /* Assuming Heebo is available or common */
        direction: rtl;
        text-align: right;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* Ensure animations stay within bounds */
    }

    #synapse-simulation h2 {
        text-align: center;
        color: var(--text-color);
        margin-top: 0;
        margin-bottom: 30px;
    }

    .synapse-area {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 30px;
        position: relative;
        min-height: 250px; /* Increased height */
        transition: background-color 0.5s ease;
    }

    .neuron {
        width: 180px; /* Wider neurons */
        height: 150px; /* Taller neurons */
        border: 3px solid var(--pre-synaptic-border);
        border-radius: 20px; /* More rounded */
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 15px;
        background-color: var(--neuron-color);
        position: relative;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* Clip internal elements */
    }

    .neuron-label {
        position: absolute;
        top: 10px;
        font-size: 0.9em;
        font-weight: bold;
        color: var(--text-color);
    }

    .pre-synaptic {
        border-right: none;
        border-top-right-radius: 0;
        border-bottom-right-radius: 0;
        align-items: flex-end;
        padding-right: 30px; /* More space for vesicles */
    }

    .post-synaptic {
        border-left: none;
        border-top-left-radius: 0;
        border-bottom-left-radius: 0;
        align-items: flex-start;
        padding-left: 30px; /* More space for receptors */
    }

    .synaptic-cleft {
        width: 60px; /* Wider cleft */
        height: 180px; /* Taller to match neurons */
        border-top: 3px solid var(--pre-synaptic-border);
        border-bottom: 3px solid var(--pre-synaptic-border);
        background-color: var(--cleft-color);
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
         box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.1);
    }

    .vesicles-area {
        position: absolute;
        right: 15px; /* Position within pre-synaptic */
        top: 50%;
        transform: translateY(-50%);
        display: flex;
        flex-direction: column;
        gap: 8px; /* Space between vesicles */
    }

    .synaptic-vesicle {
        width: 25px; /* Larger vesicles */
        height: 25px;
        background-color: var(--vesicle-color);
        border-radius: 50%;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease-in-out;
        position: relative; /* For fusion animation */
    }

    .synaptic-vesicle.fusing {
         animation: fuse-anim 0.3s ease-out forwards;
         opacity: 0; /* Disappear after fusion */
         transform: scale(1.2);
    }

    @keyframes fuse-anim {
        0% { transform: scale(1); opacity: 1; }
        100% { transform: scale(1.5); opacity: 0; }
    }

     .signal-flow {
         position: absolute;
         top: 50%;
         transform: translateY(-50%);
         height: 6px;
         background-color: var(--signal-color);
         box-shadow: 0 0 8px var(--signal-color);
         opacity: 0;
         transition: opacity 0.1s ease-out;
     }

    .pre-signal {
        left: 10px;
        width: 70%; /* Length within neuron */
        border-radius: 3px;
    }

    .post-signal {
        right: 10px;
        width: 70%; /* Length within neuron */
        border-radius: 3px;
    }

    .signal-flow.active {
        opacity: 1;
    }

    .neurotransmitter-burst {
        width: 0px; /* Start small */
        height: 0px;
        background-color: var(--neurotransmitter-color);
        border-radius: 50%;
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%) scale(0);
        opacity: 0;
         box-shadow: 0 0 10px var(--neurotransmitter-color);
    }

    .neurotransmitter-burst.active {
        animation: burst-anim 0.6s ease-out forwards; /* Longer, smoother burst */
    }

    @keyframes burst-anim {
        0% { transform: translate(-50%, -50%) scale(0); opacity: 0.9; width: 0; height: 0;}
        50% { opacity: 0.9; }
        100% { transform: translate(-50%, -50%) scale(1.5); opacity: 0; width: 60px; height: 60px;} /* Larger burst area */
    }

    .receptors-area {
        display: flex;
        flex-direction: column;
        gap: 10px; /* Space between receptors */
        position: absolute;
        left: 15px; /* Position within post-synaptic */
         top: 50%;
         transform: translateY(-50%);
    }

    .receptor {
        width: 20px; /* Larger receptors */
        height: 20px;
        background-color: var(--receptor-color);
        border-radius: 4px; /* Slightly rounded squares */
        opacity: 1;
        transition: background-color 0.2s ease-in-out, opacity 0.3s ease-in-out, transform 0.3s ease-in-out;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }

     .receptor.bound {
        background-color: var(--receptor-bound-color);
        transform: scale(1.1); /* Pop out slightly when bound */
        box-shadow: 0 0 8px var(--receptor-bound-color);
     }

    .response-indicator {
         position: absolute;
        bottom: 10px;
        right: 10px;
        font-size: 1em; /* Larger text */
        font-weight: bold;
        color: var(--signal-color); /* Use signal color */
        opacity: 0;
        transition: opacity 0.3s ease-in-out;
         text-shadow: 0 0 5px var(--signal-color);
    }

    .response-indicator.active {
        opacity: 1;
        animation: response-pulse 1s ease-out infinite;
    }

     @keyframes response-pulse {
         0% { transform: scale(1); opacity: 1; }
         50% { transform: scale(1.1); opacity: 0.8; }
         100% { transform: scale(1); opacity: 1; }
     }


    .controls {
        text-align: center;
        margin-top: 25px;
        padding-top: 20px;
        border-top: 1px dashed #B0BEC5; /* Light Grey Blue */
    }

    .controls button {
        margin: 0 8px; /* More space between buttons */
        padding: 12px 25px; /* Larger buttons */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* More rounded */
        background-color: var(--control-button-bg);
        color: white;
        font-size: 1.1em; /* Larger font */
        font-weight: bold;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
    }

    .controls button:hover {
        background-color: var(--control-button-hover);
        transform: translateY(-1px); /* Slight lift effect */
    }
     .controls button:active {
         transform: translateY(1px); /* Press effect */
     }

     #reset-btn {
         background-color: var(--reset-button-bg);
     }
     #reset-btn:hover {
         background-color: var(--reset-button-hover);
     }


    .controls .status {
        margin-top: 20px;
        font-size: 1.1em;
        font-weight: bold;
        color: var(--text-color);
    }

    /* LTP State Styles */
    .synapse-area.ltp {
         background-color: var(--ltp-color-tint);
    }
     .synapse-area.ltp .post-synaptic .receptors-area {
         gap: 7px; /* Receptors can be denser */
     }
     .synapse-area.ltp .receptor {
         background-color: #66BB6A; /* Brighter Green */
         transform: scale(1.2); /* Larger receptors */
         box-shadow: 0 0 10px #66BB6A;
     }
     .synapse-area.ltp .synaptic-vesicle {
          background-color: #E57373; /* Reddish tint */
     }
    .synapse-area.ltp .neurotransmitter-burst.active {
         animation: burst-anim-ltp 0.6s ease-out forwards; /* Larger burst */
         box-shadow: 0 0 12px #81C784;
    }
     @keyframes burst-anim-ltp {
        0% { transform: translate(-50%, -50%) scale(0); opacity: 0.9; width: 0; height: 0;}
        50% { opacity: 0.9; }
        100% { transform: translate(-50%, -50%) scale(1.8); opacity: 0; width: 70px; height: 70px;}
     }
     .synapse-area.ltp .response-indicator.active {
          color: #4CAF50; /* Green response */
         text-shadow: 0 0 8px #4CAF50;
     }


    /* LTD State Styles */
    .synapse-area.ltd {
         background-color: var(--ltd-color-tint);
    }
     .synapse-area.ltd .post-synaptic .receptors-area {
         gap: 15px; /* Receptors are sparser */
         opacity: 0.8; /* Area looks less effective */
     }
     .synapse-area.ltd .receptor {
         background-color: #E57373; /* Muted Red */
         transform: scale(0.8); /* Smaller receptors */
         opacity: 0.6; /* Less responsive appearance */
          box-shadow: none;
     }
      .synapse-area.ltd .synaptic-vesicle {
          background-color: #FFB74D; /* Orangish tint */
     }
    .synapse-area.ltd .neurotransmitter-burst.active {
         animation: burst-anim-ltd 0.6s ease-out forwards; /* Smaller burst */
        box-shadow: 0 0 6px #81C784;
    }
     @keyframes burst-anim-ltd {
        0% { transform: translate(-50%, -50%) scale(0); opacity: 0.9; width: 0; height: 0;}
        50% { opacity: 0.9; }
        100% { transform: translate(-50%, -50%) scale(1.0); opacity: 0; width: 40px; height: 40px;}
     }
     .synapse-area.ltd .response-indicator.active {
          color: #FBC02D; /* Amber response */
         text-shadow: 0 0 6px #FBC02D;
     }


    #explanation-button {
        display: block;
        width: fit-content;
        margin: 30px auto;
        padding: 12px 25px;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #4CAF50; /* Green */
        color: white;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.2s ease, transform 0.1s ease;
         box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
    }

    #explanation-button:hover {
        background-color: #388E3C; /* Darker Green */
         transform: translateY(-1px);
    }
     #explanation-button:active {
         transform: translateY(1px);
     }

    #detailed-explanation {
        display: none; /* Initially hidden */
        margin-top: 30px;
        padding-top: 30px;
        border-top: 2px solid #B0BEC5;
        color: var(--text-color);
        line-height: 1.7;
        font-size: 1.1em;
    }

     #detailed-explanation h2, #detailed-explanation h3 {
         color: #0277BD; /* Dark Blue */
         margin-bottom: 15px;
         padding-bottom: 5px;
         border-bottom: 1px solid #E1F5FE;
     }

     #detailed-explanation h2 {
         font-size: 1.8em;
     }
     #detailed-explanation h3 {
         font-size: 1.4em;
     }

     #detailed-explanation p {
         margin-bottom: 20px;
         text-align: justify;
     }

      #detailed-explanation p strong {
          color: #01579B; /* Even Darker Blue */
      }
</style>

<button id="explanation-button">מה בעצם קורה כאן? (הצג/הסתר הסבר)</button>

<div id="detailed-explanation">
    <h2>הפלסטיות הסינפטית: צלילה לעומק</h2>

    <h3>נקודת המפגש: מהי סינפסה ואיך היא עובדת?</h3>
    <p>דמיינו את המוח כרשת עצומה של מיליארדי תאי עצב (נוירונים). כדי לתקשר, הנוירונים שולחים "אותות" זה לזה. נקודת המפגש והתקשורת המרכזית הזו נקראת **סינפסה**. סינפסה מורכבת בדרך כלל מקצהו של נוירון אחד (הנוירון ה**קדם-סינפטי**), מרווח זעיר ביניהם (ה**מרווח הסינפטי**), וקרום התא של הנוירון השני (הנוירון ה**בתר-סינפטי**).</p>
    <p>כאשר אות חשמלי מגיע לקצה הנוירון הקדם-סינפטי, הוא מורה ל**וסיקולות סינפטיות** (שלפוחיות זעירות) המכילות **נוירוטרנסמיטרים** (חומרים כימיים) להתמזג עם קרום התא ולשחרר את תכולתן אל המרווח הסינפטי. הנוירוטרנסמיטרים הללו חוצים במהירות את המרווח ונקשרים ל**רצפטורים** ספציפיים על קרום הנוירון הבתר-סינפטי. קישור זה הוא כמו מפתח שנכנס למנעול, והוא גורם לשינויים חשמליים או כימיים בנוירון המקבל, וכך האות ממשיך במסעו ברשת.</p>

    <h3>הגמישות המדהימה: הצגת מושג הפלסטיות הסינפטית</h3>
    <p>**פלסטיות סינפטית** היא היכולת של הסינפסות לשנות את ה"חוזק" או היעילות של התקשורת ביניהן. "חוזק" סינפסה מתייחס למידת ההשפעה של אות יחיד מהנוירון השולח על הנוירון המקבל. בסינפסה חזקה, אות קדם-סינפטי יחיד יגרום לתגובה חזקה בנוירון הבתר-סינפטי. בסינפסה חלשה, אותו אות יגרום לתגובה חלשה יותר או לא יגרום לתגובה כלל.</p>
    <p>שינויים אלו בחוזק הסינפסה אינם קבועים – הם דינמיים ויכולים להתרחש במהירות מפתיעה, כתגובה לפעילות העצבית שעוברת דרך הסינפסה. השינויים הללו, לחיזוק או החלשה של קשרים ספציפיים, הם הדרך שבה המוח מקודד מידע, יוצר זיכרונות, ולומד להגיב ביעילות לסביבה המשתנה.</p>

    <h3>מתחזקים יחד: Long-Term Potentiation (LTP) - חיזוק סינפטי ארוך-טווח</h3>
    <p>כששני נוירונים יורים יחד שוב ושוב (כלומר, הנוירון השולח מעביר אות, והנוירון המקבל מגיב לו או פעיל בו זמנית), הקשר הסינפטי ביניהם נוטה להתחזק באופן מתמשך. תהליך זה נקרא **LTP** (Long-Term Potentiation). לאחר חוויה של רצף אותות "חזק", הנוירון המקבל יהפוך לרגיש יותר לאותות עתידיים מאותו נוירון שולח. בסימולציה, רצף האותות ה"חזק" גורם לסינפסה להיכנס למצב LTP, בו היא מגיבה בעוצמה רבה יותר (למשל, על ידי הוספת רצפטורים או הגברת יעילותם), וכך מסלול המידע הזה במוח מתחזק. LTP נחשב למנגנון התאי המרכזי שעומד בבסיס רכישת זיכרונות חדשים ולמידה.</p>

    <h3>נחלשים בנפרד: Long-Term Depression (LTD) - היחלשות סינפטית ארוכת-טווח</h3>
    <p>מצד שני, פעילות סינפטית בתדירות נמוכה, או סוגים מסוימים של פעילות עצבית, יכולים לגרום דווקא ל**היחלשות** מתמשכת של הקשר הסינפטי. תהליך זה נקרא **LTD** (Long-Term Depression). בסימולציה, רצף אותות "חלש" גורם לסינפסה להיכנס למצב LTD, בו היא מגיבה בעוצמה פחותה לאותות עתידיים (למשל, על ידי הפחתת רצפטורים או הפחתת יעילותם). LTD חשוב לא פחות מ-LTP; הוא מאפשר לנו "לשכוח" מידע לא רלוונטי, לחדד מיומנויות מוטוריות על ידי היחלשות קשרים מיותרים, ולהתאים את הרשתות העצביות שלנו לשינויים בסביבה. הוא קריטי לאיזון וגמישות המוח.</p>

    <h3>מנגנונים בלב הסינפסה: איך זה קורה ברמה המולקולרית?</h3>
    <p>LTP ו-LTD מערבים שינויים מורכבים בתוך הנוירונים עצמם. לדוגמה, בסינפסות המשתמשות בנוירוטרנסמיטר גלוטמט (הנפוץ ביותר במוח), LTP לעיתים קרובות קשור להוספת רצפטורים מסוג AMPA לקרום הנוירון הבתר-סינפטי, מה שהופך אותו לרגיש יותר לגלוטמט. LTD יכול להיות קשור להסרת רצפטורי AMPA או שינוי בהם שהופך אותם לפחות יעילים. שינויים אלו הם תוצאה של מסלולים מורכבים בתוך התא, המושפעים מכניסת יוני סידן ופעילות של חלבונים שונים המבצעים את ה"שדרוגים" הסינפטיים.</p>

    <h3>הקשר הגדול: פלסטיות סינפטית, למידה וזיכרון</h3>
    <p>על פי עקרון יסוד בחקר המוח, המכונה לעיתים קרובות "חוק הב" (על שם דונלד הב): "נוירונים שיורים יחד, נקשרים יחד" (Neurons that fire together, wire together). כל למידה, כל זיכרון חדש, משקפים שינויים פיזיים ברשתות הסינפטיות במוח. זיכרונות מגובשים כדפוסים ספציפיים של סינפסות מחוזקות, בעוד ששכחה עשויה לערב היחלשות סינפטית. הבנה מעמיקה של הפלסטיות הסינפטית היא המפתח להבנת הדרך שבה אנו רוכשים ידע, יוצרים זיכרונות ומתאימים את עצמנו ללא הרף לעולם שמסביבנו.</p>

    <h3>חשיבות לבריאות: פלסטיות בבריאות ובמחלה</h3>
    <p>פלסטיות סינפטית תקינה חיונית לבריאות המוח לאורך כל החיים. היא מאפשרת התאוששות מסוימת מפציעות (כמו שבץ) על ידי יצירת נתיבי תקשורת חדשים. אולם, שיבושים בפלסטיות נקשרים למגוון רחב של הפרעות נוירולוגיות ופסיכיאטריות, כולל מחלת אלצהיימר (אובדן סינפסות וירידה בפלסטיות), אוטיזם, סכיזופרניה והתמכרות. חקר הפלסטיות פותח אפיקים חדשים לפיתוח טיפולים המכוונים לחיזוק או החלשה ספציפית של קשרים סינפטיים כדי להחזיר תפקוד תקין.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const sendSignalBtn = document.getElementById('send-signal-btn');
        const sendStrongSeriesBtn = document.getElementById('send-strong-series-btn');
        const sendWeakSeriesBtn = document.getElementById('send-weak-series-btn');
        const resetBtn = document.getElementById('reset-btn');
        const preSynapticNeuron = document.getElementById('pre-synaptic');
        const postSynapticNeuron = document.getElementById('post-synaptic');
        const synapticCleft = document.getElementById('synaptic-cleft');
        const neurotransmitterBurst = document.getElementById('neurotransmitter-burst');
        const receptorsArea = document.getElementById('receptors-area');
        const responseIndicator = document.getElementById('response-indicator');
        const synapseArea = document.querySelector('.synapse-area');
        const synapseStrengthSpan = document.getElementById('synapse-strength');
        const explanationButton = document.getElementById('explanation-button');
        const detailedExplanation = document.getElementById('detailed-explanation');
        const preSignalFlow = preSynapticNeuron.querySelector('.pre-signal');
        const postSignalFlow = postSynapticNeuron.querySelector('.post-signal');

        let isSimulating = false; // Prevent multiple simulations running

        // Initial state
        let currentReceptorCount = 4; // Default number of receptors
        const maxReceptorCount = 6;
        const minReceptorCount = 2;
        let synapseState = 'normal'; // 'normal', 'ltp', 'ltd'

        // Function to update visual receptors based on count
        function updateReceptorVisuals() {
            receptorsArea.innerHTML = ''; // Clear existing receptors
            for (let i = 0; i < currentReceptorCount; i++) {
                const receptorDiv = document.createElement('div');
                receptorDiv.classList.add('receptor');
                 // Add visual state classes if needed (optional, CSS handles most)
                 // receptorDiv.classList.add(synapseState);
                receptorsArea.appendChild(receptorDiv);
            }
             // Update gap based on state (handled by CSS classes on synapseArea)
        }

        // Function to simulate vesicle movement and fusion
        function simulateVesicleFusion() {
             const vesicles = preSynapticNeuron.querySelectorAll('.synaptic-vesicle');
             if (vesicles.length > 0) {
                 const vesicleToFuse = vesicles[vesicles.length - 1]; // Fuse the last one
                 vesicleToFuse.classList.add('fusing');
                 setTimeout(() => {
                     vesicleToFuse.remove(); // Remove after animation
                     // Optionally add a new vesicle off-screen to replenish visual stock
                     const newVesicle = document.createElement('div');
                     newVesicle.classList.add('synaptic-vesicle');
                     // Position off-screen or further back initially
                     newVesicle.style.cssText = 'position: absolute; right: -20px; top: 50%; transform: translateY(-50%); opacity: 0;'; // Example, adjust as needed
                     preSynapticNeuron.querySelector('.vesicles-area').appendChild(newVesicle);
                     // Animate it back to position and opacity
                     setTimeout(() => {
                         newVesicle.style.cssText = ''; // Reset to CSS defined styles
                     }, 50); // Small delay before animating in
                 }, 300); // Match fusion animation duration
             }
        }


        // Function to simulate a single signal transmission with animations
        function simulateSignal(isSeries = false, seriesType = 'none') {
            if (isSimulating) return; // Prevent spamming
            isSimulating = true;

            // Reset keyframe animations by cloning (forces re-run)
            const oldBurst = neurotransmitterBurst;
            const newBurst = oldBurst.cloneNode(true);
            oldBurst.parentNode.replaceChild(newBurst, oldBurst);
            const currentNeurotransmitterBurst = newBurst;

            // Reset states
            responseIndicator.classList.remove('active');
            preSignalFlow.classList.remove('active');
            postSignalFlow.classList.remove('active');
            document.querySelectorAll('.receptor').forEach(rec => rec.classList.remove('bound'));

            // 1. Signal arrives at pre-synaptic neuron
            preSignalFlow.classList.add('active');
            simulateVesicleFusion(); // Animate vesicle fusion

            setTimeout(() => {
                preSignalFlow.classList.remove('active');

                // 2. Neurotransmitter burst into cleft
                currentNeurotransmitterBurst.classList.add('active');

                // 3. Neurotransmitters bind to receptors
                setTimeout(() => {
                    const receptors = document.querySelectorAll('.receptor');
                    let boundCount = 0;
                    const bindingProbability = synapseState === 'ltp' ? 0.9 : synapseState === 'ltd' ? 0.4 : 0.6; // Higher chance in LTP, lower in LTD

                    receptors.forEach(rec => {
                        if (Math.random() < bindingProbability) {
                            rec.classList.add('bound');
                            boundCount++;
                        }
                    });

                    // 4. Post-synaptic response (graded)
                    const responseThreshold = synapseState === 'ltp' ? Math.max(1, currentReceptorCount * 0.3) : synapseState === 'ltd' ? Math.max(1, currentReceptorCount * 0.6) : Math.max(1, currentReceptorCount * 0.4); // Lower threshold in LTP, higher in LTD
                    const maxResponseIntensity = currentReceptorCount;

                    if (boundCount >= responseThreshold) {
                         responseIndicator.textContent = 'תגובה!'; // Or a visual intensity bar
                         responseIndicator.classList.add('active');
                         postSignalFlow.classList.add('active');
                    } else {
                        responseIndicator.textContent = 'אין תגובה מספקת';
                         // Keep indicator visible briefly to show lack of response? Or just leave it off. Let's leave off for clearer feedback.
                         // responseIndicator.classList.add('active'); // Optional: show "no response" text briefly
                         // setTimeout(() => responseIndicator.classList.remove('active'), 500);
                    }


                    // End of simulation cycle
                    setTimeout(() => {
                         postSignalFlow.classList.remove('active');
                         // Reset receptor bound state after a brief moment if not in a series
                         if (!isSeries) {
                            document.querySelectorAll('.receptor').forEach(rec => rec.classList.remove('bound'));
                         }
                        isSimulating = false; // Allow next signal
                    }, 400); // Keep bound state visible briefly

                }, 300); // Delay after burst appears

            }, 200); // Delay for pre-signal flow


        }

        // Function to update synapse strength state (LTP/LTD)
        function updateSynapseState(type) {
            synapseArea.classList.remove('ltp', 'ltd');
            synapseState = type; // Update JS state variable

            if (type === 'ltp') {
                synapseArea.classList.add('ltp');
                synapseStrengthSpan.textContent = 'חזק (LTP)';
                 if (currentReceptorCount < maxReceptorCount) currentReceptorCount++; // Add a receptor
            } else if (type === 'ltd') {
                synapseArea.classList.add('ltd');
                synapseStrengthSpan.textContent = 'חלש (LTD)';
                 if (currentReceptorCount > minReceptorCount) currentReceptorCount--; // Remove a receptor
            } else { // normal
                synapseStrengthSpan.textContent = 'רגיל';
                currentReceptorCount = 4; // Reset to default
            }
            updateReceptorVisuals(); // Update visual representation
        }


        // --- Event Listeners ---
        sendSignalBtn.addEventListener('click', () => {
            simulateSignal();
             // Single signal doesn't change long-term strength in this simple model
             // updateSynapseState('normal'); // Keep normal state explicitly if needed
        });

        sendStrongSeriesBtn.addEventListener('click', () => {
             if (isSimulating) return;

             let seriesCount = 0;
             const totalSeries = 6; // Number of rapid signals for LTP
             const intervalTime = 250; // Time between signals in series

             const seriesInterval = setInterval(() => {
                 if (seriesCount < totalSeries) {
                     simulateSignal(true, 'ltp'); // Simulate signal, indicate it's part of a series
                     seriesCount++;
                 } else {
                     clearInterval(seriesInterval);
                     // Allow last animation to finish before updating state
                     setTimeout(() => {
                         updateSynapseState('ltp');
                         // Reset bound state visually after series applies
                          document.querySelectorAll('.receptor').forEach(rec => rec.classList.remove('bound'));
                     }, 800); // Wait for last signal animation
                 }
             }, intervalTime);
        });

         sendWeakSeriesBtn.addEventListener('click', () => {
             if (isSimulating) return;

             let seriesCount = 0;
             const totalSeries = 8; // More signals, or slower/weaker signals for LTD
             const intervalTime = 400; // Slower succession

             const seriesInterval = setInterval(() => {
                 if (seriesCount < totalSeries) {
                     simulateSignal(true, 'ltd'); // Simulate signal
                     seriesCount++;
                 } else {
                     clearInterval(seriesInterval);
                      // Allow last animation to finish before updating state
                     setTimeout(() => {
                        updateSynapseState('ltd');
                         // Reset bound state visually after series applies
                         document.querySelectorAll('.receptor').forEach(rec => rec.classList.remove('bound'));
                     }, 800); // Wait for last signal animation
                 }
             }, intervalTime);
         });

         resetBtn.addEventListener('click', () => {
              if (isSimulating) return;
             updateSynapseState('normal');
             // Ensure all animations/states are reset visually
             neurotransmitterBurst.classList.remove('active');
             responseIndicator.classList.remove('active');
             preSignalFlow.classList.remove('active');
             postSignalFlow.classList.remove('active');
             document.querySelectorAll('.receptor').forEach(rec => rec.classList.remove('bound'));
              // Reset vesicle positions (can be tricky with cloning, manual reset might be needed if we added complex vesicle positions)
              // For now, let updateReceptorVisuals handle receptor refresh and assume vesicles replenish off-screen.
         });


        // Explanation button functionality (unchanged)
        explanationButton.addEventListener('click', () => {
            if (detailedExplanation.style.display === 'none' || detailedExplanation.style.display === '') {
                detailedExplanation.style.display = 'block';
                 explanationButton.textContent = 'הסתר הסבר מפורט';
            } else {
                detailedExplanation.style.display = 'none';
                 explanationButton.textContent = 'מה בעצם קורה כאן? (הצג/הסתר הסבר)';
            }
        });

         // Initialize simulation display
         updateSynapseState('normal'); // Set initial state and create receptors
    });
</script>
---
```