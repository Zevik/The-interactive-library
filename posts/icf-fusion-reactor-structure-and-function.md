---
title: "כור היתוך: הצצה אל לב ליבו של כוכב על כדור הארץ"
english_slug: icf-fusion-reactor-structure-and-function
category: "מדעים מדויקים / פיזיקה"
tags: [היתוך גרעיני, אנרגיה נקייה, כור היתוך, כליאה אינרציאלית, פיזיקת פלזמה]
---
# כור היתוך: הצצה אל לב ליבו של כוכב על כדור הארץ

האם אפשר לשחזר את כוחה האדיר של השמש על פני כדור הארץ? דמיינו יצירת כוכב זעיר בתוך קפסולה זעירה. כיצד פועל 'כוכב' כזה, ומה מונע ממנו להתפזר ברגע שהוא נוצר? צללו לסימולציה האינטראקטיבית שלנו וגלו את הקסם הפיזיקלי מאחורי כליאה אינרציאלית!

<div id="fusion-app">
    <div id="simulation-area">
        <div id="lasers">
            <div class="laser laser-top"></div>
            <div class="laser laser-bottom"></div>
            <div class="laser laser-left"></div>
            <div class="laser laser-right"></div>
            <div class="laser laser-top-left"></div>
            <div class="laser laser-top-right"></div>
            <div class="laser laser-bottom-left"></div>
            <div class="laser laser-bottom-right"></div>
        </div>
        <div id="target">
            <div class="target-shell" data-info="המעטפת (Ablator): שכבה חיצונית דקה. כשהלייזרים פוגעים בה, היא מתאדה במהירות כלפי חוץ ומייצרת לחץ עצום שדוחס את הדלק פנימה."></div>
            <div class="target-fuel" data-info="הדלק (Fuel): ליבה קפואה של דאוטריום וטריטיום. הדחיסה הקיצונית הופכת אותו לפלזמה לוהטת שבה מתרחש ההיתוך."></div>
        </div>
        <div id="ignition-flash"></div>
        <div id="explosion"></div>
        <div id="info-box" dir="rtl"></div>
        <div id="status-display">שלב: מוכן להצתה</div>
    </div>
    <div id="controls">
        <button id="start-sim">הצת את הכור!</button>
    </div>
</div>

<style>
    #fusion-app {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        border: none; /* Remove border */
        padding: 0; /* Remove padding */
        border-radius: 12px; /* More rounded corners */
        max-width: 700px;
        margin: 20px auto;
        background: linear-gradient(135deg, #1a1a2e, #16213e); /* Darker, thematic background */
        position: relative;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
        overflow: hidden; /* Ensure nothing spills out */
    }

    #simulation-area {
        width: 100%;
        padding-top: 100%; /* 1:1 Aspect Ratio */
        position: relative;
        background: radial-gradient(circle at center, #0d0d1a 0%, #0a0a0d 100%); /* Dark space-like background */
        border-radius: 12px 12px 0 0;
        overflow: hidden;
        border-bottom: 1px solid #333; /* Separator */
    }

    #simulation-area > div {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    #lasers {
        display: block; /* Override flex */
        pointer-events: none; /* Lasers are visual only */
    }

    .laser {
        position: absolute;
        background: linear-gradient(to right, rgba(0,255,255,0) 0%, cyan 80%, rgba(0,255,255,0.8) 100%);
        box-shadow: 0 0 8px cyan, 0 0 12px cyan;
        height: 4px; /* Thicker laser */
        transform-origin: 100% center; /* Rotate and scale from the tip end */
        width: 0; /* Start invisible */
        opacity: 0;
        z-index: 5; /* Above background, below target */
    }

    /* Positioning for 8 lasers */
    .laser-right { top: 50%; right: 0; transform: translateY(-50%); }
    .laser-left { top: 50%; left: 0; transform: translateY(-50%) rotate(180deg); }
    .laser-top { top: 0; left: 50%; transform: translateX(-50%) rotate(270deg); }
    .laser-bottom { bottom: 0; left: 50%; transform: translateX(-50%) rotate(90deg); }
    .laser-top-right { top: 0; right: 0; transform-origin: bottom left; transform: translate(-50%, 50%) rotate(-45deg); } /* Adjusted origin/transform */
    .laser-top-left { top: 0; left: 0; transform-origin: bottom right; transform: translate(50%, 50%) rotate(45deg); } /* Adjusted origin/transform */
    .laser-bottom-right { bottom: 0; right: 0; transform-origin: top left; transform: translate(-50%, -50%) rotate(45deg); } /* Adjusted origin/transform */
    .laser-bottom-left { bottom: 0; left: 0; transform-origin: top right; transform: translate(50%, -50%) rotate(-45deg); } /* Adjusted origin/transform */


    #target {
        position: relative;
        width: 30%; /* Slightly larger initial target */
        height: 30%;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: width 0.8s cubic-bezier(0.68, -0.55, 0.27, 1.55), height 0.8s cubic-bezier(0.68, -0.55, 0.27, 1.55); /* Add bounce effect */
        z-index: 10; /* Above lasers */
    }

    .target-shell {
        width: 100%;
        height: 100%;
        background: radial-gradient(circle, #666 0%, #333 100%);
        border-radius: 50%;
        position: absolute;
        box-sizing: border-box;
        border: 3px solid #aaa; /* More prominent border */
        cursor: pointer;
        transition: all 0.5s ease-out; /* Transition for ablation */
        box-shadow: inset 0 0 10px rgba(255,255,255,0.2);
    }

    .target-fuel {
        width: 60%; /* Initial fuel size relative to shell */
        height: 60%;
        background: radial-gradient(circle, #444 0%, #111 100%);
        border-radius: 50%;
        position: absolute;
        cursor: pointer;
        transition: all 0.8s ease-in; /* Transition for compression */
        box-shadow: inset 0 0 8px rgba(0,0,0,0.5);
    }

    #ignition-flash {
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background-color: #ffff00; /* Intense yellow */
        box-shadow: 0 0 50px 20px #ffff00, 0 0 100px 40px rgba(255,255,0,0.5); /* Stronger glow */
        transform: translate(-50%, -50%);
        opacity: 0;
        z-index: 20; /* Above target */
        transition: all 0.1s ease-in;
    }

    #explosion {
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(255,165,0,0.9) 0%, rgba(255,0,0,0.7) 30%, rgba(255,0,0,0) 70%); /* Fiery gradient */
        transform: translate(-50%, -50%);
        opacity: 0;
        z-index: 15; /* Between flash and target */
        transition: all 0.6s ease-out; /* Faster expansion */
    }

    #info-box {
        position: absolute;
        background-color: rgba(255, 255, 255, 0.95); /* Almost opaque */
        border: 1px solid #ddd;
        padding: 12px; /* More padding */
        border-radius: 6px;
        z-index: 30; /* Highest z-index */
        max-width: 220px; /* Slightly wider */
        font-size: 0.95em; /* Slightly larger font */
        display: none;
        color: #333;
        text-align: right;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        line-height: 1.5; /* Better readability */
    }

    #status-display {
        position: absolute;
        bottom: 15px; /* More space from bottom */
        left: 50%; /* Center horizontally */
        transform: translateX(-50%);
        background-color: rgba(255, 255, 255, 0.15); /* Semi-transparent white */
        color: white;
        padding: 8px 15px; /* More padding */
        border-radius: 20px; /* Pill shape */
        font-size: 1em; /* Larger font */
        z-index: 10;
        direction: rtl;
        min-width: 200px; /* Minimum width */
        text-align: center;
        backdrop-filter: blur(5px); /* Blurred background effect */
        -webkit-backdrop-filter: blur(5px); /* For Safari */
    }

    #controls {
        text-align: center;
        padding: 15px; /* Add padding */
    }

    button {
        padding: 12px 25px; /* Larger button */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        background: linear-gradient(45deg, #007bff, #0056b3); /* Gradient button */
        color: white;
        border: none;
        border-radius: 25px; /* Rounded button */
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        font-weight: bold;
    }

    button:hover {
        background: linear-gradient(45deg, #0056b3, #003f80);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        transform: translateY(-2px); /* Slight lift effect */
    }

     button:disabled {
        background: #ccc;
        cursor: not-allowed;
        box-shadow: none;
        transform: none;
    }


    #toggle-explanation {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: #28a745;
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }

    #toggle-explanation:hover {
         background-color: #218838;
    }

    #explanation {
        margin-top: 20px;
        padding: 20px; /* More padding */
        border: none; /* Remove border */
        border-radius: 8px;
        background-color: #fff;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        display: none; /* Initially hidden */
        line-height: 1.7; /* Improve readability */
        color: #333;
    }

    #explanation h2, #explanation h3 {
        color: #16213e; /* Dark blue headings */
        margin-top: 25px; /* More space above headings */
        margin-bottom: 12px;
        border-bottom: 1px solid #eee; /* Subtle separator */
        padding-bottom: 5px;
    }

    #explanation p, #explanation ul {
        margin-bottom: 15px;
        text-align: justify;
    }

    #explanation ul {
        padding-right: 20px; /* Indent list */
    }

    #explanation li {
         margin-bottom: 8px;
    }

    .hidden {
        display: none;
    }
</style>

<button id="toggle-explanation">הצג הסבר מלא</button>

<div id="explanation" class="hidden">
    <h2>מהו היתוך גרעיני? כוחה של השמש, כאן על הארץ!</h2>
    <p>היתוך גרעיני הוא התהליך העוצמתי שמניע את השמש ואת שאר הכוכבים ביקום. זהו מפגש אטומי אלים וחם במיוחד, שבו אטומים קלים (כמו דאוטריום וטריטיום, איזוטופים של מימן) נדחסים יחד בכוח אדיר, מתמזגים לאטום כבד יותר (הליום), ומשחררים בו-זמנית כמויות פנומנליות של אנרגיה. בניגוד ביקוע גרעיני (השיטה הנוכחית להפקת חשמל מאטומים), היתוך מבטיח עתיד עם פוטנציאל לאנרגיה נקייה, כמעט בלתי מוגבלת, עם פסולת רדיואקטיבית נמוכה בהרבה וללא הסיכון לתגובת שרשרת בלתי נשלטת. זהו "הגביע הקדוש" של עולם האנרגיה.</p>

    <h2>כליאה אינרציאלית (ICF): לכוד את הכוכב הפנימי</h2>
    <p>כדי לגרום לאטומים להתמזג, צריך לדחוס אותם לנקודה אולטרה-צפופה ולאדמה לטמפרטורות לוהטות יותר מלב ליבה של השמש – מעל 100 מיליון מעלות צלזיוס! כליאה אינרציאלית היא אחת הדרכים להשיג את התנאים הקיצוניים הללו. במקום להשתמש בשדות מגנטיים כדי לרחף את הפלזמה החמה (כמו בשיטת כליאה מגנטית - MCF), ב-ICF אנחנו משתמשים בכוח אדיר שמדחס את הדלק בצורה כה מהירה ואלימה, שהדלק הדחוס נשאר במצבו הקיצוני למשך שבריר שנייה בזכות ה"אינרציה" שלו – הנטייה להתנגד לשינוי בתנועה – מספיק זמן כדי שתתרחש תגובת היתוך ותשתחרר אנרגיה. דמיינו כדור סל שאתם מוחצים ברגע אחד לגרגר חול – זו סדר הגודל של הדחיסה ב-ICF.</p>

    <h2>השחקנים הראשיים: מה מכיל כור היתוך ICF?</h2>
    <ul>
        <li><strong>מערכת ההנעה (Drivers):</strong> אלו הם "השרירים" של המערכת. בדרך כלל מדובר במערך לייזרים עתירי הספק, אבל חוקרים גם מאיצי חלקיקים. הלייזרים מספקים את זרם האנרגיה האדיר שמתחיל את כל התהליך.</li>
        <li><strong>המטרה (Target):</strong> הכוכב הפוטנציאלי שלנו! קפסולה זעירה, לרוב כדורית, בגודל של ראש סיכה או גרגר פלפל. היא מעוצבת בדיוק אבסולוטי ומכילה את דלק ההיתוך.
            <ul>
                <li><strong>המעטפת (Ablator):</strong> השכבה החיצונית של המטרה. עשויה מחומרים קלים. תפקידה לקלוט את אנרגיית הלייזרים, להתאדות במהירות ולהעיף חומר החוצה. זה יוצר את כוח ה"ריאקציה" שדוחף את שאר המטרה פנימה.</li>
                <li><strong>הדלק (Fuel):</strong> בדרך כלל תערובת קפואה של דאוטריום וטריטיום. זהו החומר שיעבור היתוך כשהוא יידחס ויתחמם מספיק.</li>
            </ul>
        </li>
         <li><strong>הולראום (Hohlraum):</strong> (בשיטה עקיפה - Indirect Drive) רכיב אופציונלי. גליל קטן מזהב שמקיף את המטרה. הלייזרים פוגעים בדפנות ההולראום, שמתאדות ופולטות קרינת X. קרינת ה-X היא זו שמדחסת את המטרה. הסימולציה שלנו מציגה שיטה ישירה (Direct Drive) בה הלייזרים פוגעים ישירות במטרה.</li>
    </ul>

    <h2>מסע אל לב הכוכב: שלבי ההיתוך ב-ICF (הנעה ישירה)</h2>
    <p>עקבו אחרי השלבים בסימולציה:</p>
    <ol>
        <li>**מוכן להצתה:** המטרה הזעירה, ובה המעטפת והדלק, מוצבת במרכז הכור. לייזרים רבי עוצמה מכוונים אליה מכל הכיוונים.</li>
        <li>**הנעה ואבלציה (Ablation):** ברגע אחד, כל הלייזרים יורים בו-זמנית. אלומות האור העצמתיות פוגעות במעטפת החיצונית של המטרה. אנרגיית הלייזר מחממת את המעטפת לטמפרטורות קיצוניות, והחומר מתאדה ומתפשט החוצה במהירות אדירה, כמו גז חם שיוצא מבלון.</li>
        <li>**אימפלוזיה (Implosion - קריסה פנימית):** התפשטות המעטפת כלפי חוץ יוצרת כוח ריאקציה אדיר (כמו יציאת גז ממתנפח שדוחפת אותו קדימה). כוח זה דוחף את שאריות המעטפת ואת דלק ההיתוך פנימה, אל עבר מרכז המטרה. הדחיסה מהירה ועוצמתית כל כך, שהמטרה כולה קורסת לתוך עצמה בתוך פחות ממיליארדית השנייה!</li>
        <li>**דחיסה והצתה (Compression & Ignition):** כשהחומר קורס פנימה, הוא נדחס לצפיפות הגבוהה פי אלפי פעמים מצפיפותו במצב מוצק, ומרכז המטרה מתחמם לטמפרטורות של מעל 100 מיליון מעלות צלזיוס. אם התנאים (צפיפות, טמפרטורה, זמן) נכונים, מתרחשת "הצתה" – תגובות היתוך ספונטניות מתחילות במרכז הלוהט (ה"נקודה החמה"). תגובות אלו משחררות חלקיקי אלפא עתירי אנרגיה.</li>
        <li>**"בעירה" ושחרור אנרגיה (Burn & Energy Release):** חלקיקי האלפא מההצתה פוגעים בשכבות הדלק הצפופות יותר שסביב הנקודה החמה ומחממים אותן. חימום זה גורם גם לשכבות הסמוכות להגיע לתנאי היתוך, והתגובה מתפשטת החוצה דרך הדלק הדחוס במהירות אדירה, כמו "בעירה" גרעינית. התוצאה היא שחרור כמות אדירה של אנרגיה בצורת נויטרונים מהירים וחלקיקי אלפא, בתוך שבריר שנייה.</li>
        <li>**תגובה הסתיימה:** הדלק הדחוס מתפשט במהירות לאחר שחרור האנרגיה, והתגובה נפסקת.</li>
    </ol>

    <h2>מדוע "כליאה אינרציאלית"?</h2>
    <p>כפי שהשם מרמז, הכליאה כאן אינה קבועה אלא זמנית, ונמשכת רק למשך שבריר השנייה החיוני. הדלק הדחוס נשאר צפוף וחם מספיק רק בזכות האינרציה שלו – ה"עקשנות" שלו להישאר במצב הדחוס לזמן קצרצר לפני שהוא "מבין" שהוא צריך להתפשט בגלל הלחץ העצום מתוכו. האינרציה הזו היא ש"כולאת" את הפלזמה למשך הזמן הדרוש לתגובת ההיתוך להתרחש. זהו מירוץ נגד הזמן בין כוח הדחיסה לבין כוח ההתפשטות של הפלזמה הלוהטת.</p>

    <h2>המסע אל האנרגיה: אתגרים ותקווה לעתיד</h2>
    <p>היתוך בשיטת ICF הוא אתגר הנדסי ופיזיקלי עצום. הוא דורש מערכות לייזר מפלצתיות, ייצור מטרות בדיוק אטומי, והבנה מעמיקה של פיזיקת פלזמה בתנאים שקיימים רק בכוכבים. למרות הקשיים, הישגים פורצי דרך כמו השגת "הצתה" (Ignition) במתקן NIF בארה"ב (שבו שוחררה יותר אנרגיה מההיתוך מאשר הושקעה בדלק עצמו) מעידים על ההתקדמות. הדרך לכור היתוך מסחרי עדיין ארוכה, אך ההתקדמות המדעית והטכנולוגית בתחום זה מפיחה תקווה לעתיד שבו נוכל לרתום את כוחם של כוכבים להפקת אנרגיה נקייה ובטוחה כאן, על כדור הארץ.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const startButton = document.getElementById('start-sim');
        const statusDisplay = document.getElementById('status-display');
        const targetDiv = document.getElementById('target');
        const shellDiv = targetDiv.querySelector('.target-shell');
        const fuelDiv = targetDiv.querySelector('.target-fuel');
        const lasersDiv = document.getElementById('lasers');
        const lasers = lasersDiv.querySelectorAll('.laser');
        const infoBox = document.getElementById('info-box');
        const ignitionFlash = document.getElementById('ignition-flash');
        const explosionDiv = document.getElementById('explosion');
        const simulationArea = document.getElementById('simulation-area');

        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');

        let simulationRunning = false;

        const resetSimulation = () => {
            simulationRunning = false;
            // Remove any active transitions for instant reset
             lasers.forEach(laser => laser.style.transition = 'none');
            shellDiv.style.transition = 'none';
            fuelDiv.style.transition = 'none';
            targetDiv.style.transition = 'none';
            ignitionFlash.style.transition = 'none';
            explosionDiv.style.transition = 'none';


            targetDiv.style.width = '30%';
            targetDiv.style.height = '30%';
            shellDiv.style.opacity = '1';
            shellDiv.style.transform = 'none';
            fuelDiv.style.width = '60%';
            fuelDiv.style.height = '60%';

            ignitionFlash.style.opacity = '0';
            ignitionFlash.style.width = '0';
            ignitionFlash.style.height = '0';
            ignitionFlash.style.boxShadow = 'none';

            explosionDiv.style.opacity = '0';
            explosionDiv.style.width = '0';
            explosionDiv.style.height = '0';
            explosionDiv.style.background = 'radial-gradient(circle, rgba(255,165,0,0.9) 0%, rgba(255,0,0,0.7) 30%, rgba(255,0,0,0) 70%)'; /* Reset gradient */


            lasers.forEach(laser => {
                laser.style.width = '0';
                laser.style.opacity = '0';
                // Reset specific positioning/transform if needed, though width/opacity handles start state
            });

            statusDisplay.textContent = 'שלב: מוכן להצתה';
            startButton.disabled = false;
            startButton.textContent = 'הצת את הכור!';
            infoBox.style.display = 'none'; // Hide info box on reset
        };

        const runSimulation = async () => {
            if (simulationRunning) return;
            simulationRunning = true;
            startButton.disabled = true;
            startButton.textContent = '...מתבצעת הצתה';
            infoBox.style.display = 'none'; // Hide info box during simulation

            // Re-apply transitions at the start of the simulation
             lasers.forEach(laser => laser.style.transition = 'width 0.4s linear, opacity 0.4s linear');
            shellDiv.style.transition = 'all 0.5s ease-out';
            fuelDiv.style.transition = 'all 0.8s ease-in';
            targetDiv.style.transition = 'width 0.8s ease-in, height 0.8s ease-in';
            ignitionFlash.style.transition = 'all 0.1s ease-in, box-shadow 0.1s ease-in';
            explosionDiv.style.transition = 'all 0.6s ease-out';


            // Step 1 & 2: Lasers & Ablation
            statusDisplay.textContent = 'שלב: הנעה ואבלציה (Ablation)';
            lasers.forEach(laser => {
                laser.style.width = 'calc(50% + 15%)'; /* Extend towards center + overshoot */
                laser.style.opacity = '1';
            });

            await new Promise(resolve => setTimeout(resolve, 400)); // Wait for lasers to reach target

             lasers.forEach(laser => {
                // After hitting, fade out quickly
                 laser.style.transition = 'opacity 0.2s linear';
                 laser.style.opacity = '0';
             });


            shellDiv.style.opacity = '0'; // Ablate the shell
            shellDiv.style.transform = 'scale(1.8)'; // Visual cue of expansion outwards


            // Step 3: Implosion
            statusDisplay.textContent = 'שלב: אימפלוזיה (קריסה פנימית)';
            // Compress fuel and target simultaneously
            fuelDiv.style.width = '10%';
            fuelDiv.style.height = '10%';
            targetDiv.style.width = '5%';
            targetDiv.style.height = '5%';


            await new Promise(resolve => setTimeout(resolve, 800)); // Wait for compression

            // Step 4: Ignition
            statusDisplay.textContent = 'שלב: דחיסה והצתה (Ignition)';
            ignitionFlash.style.opacity = '1';
             // Flash size related to the compressed fuel size, maybe slightly larger
            const compressedSize = targetDiv.clientWidth; // Use actual calculated size after transition
            ignitionFlash.style.width = `${compressedSize * 3}px`; // Size based on compressed target
            ignitionFlash.style.height = `${compressedSize * 3}px`;
             // Ensure flash size is not zero if target size is zero
             if (compressedSize === 0) {
                 ignitionFlash.style.width = '30px';
                 ignitionFlash.style.height = '30px';
             }

            ignitionFlash.style.boxShadow = '0 0 80px 40px #ffff00, 0 0 120px 60px rgba(255,255,0,0.5)';


            await new Promise(resolve => setTimeout(resolve, 150)); // Flash duration

            // Step 5 & 6: Burn & Energy Release
            statusDisplay.textContent = 'שלב: "בעירה" ושחרור אנרגיה';
            ignitionFlash.style.opacity = '0'; // Fade flash quickly
            ignitionFlash.style.boxShadow = 'none';

            explosionDiv.style.opacity = '1';
            explosionDiv.style.width = '250%'; // Expand rapidly beyond container
            explosionDiv.style.height = '250%';
            explosionDiv.style.background = 'radial-gradient(circle, rgba(255,165,0,0.9) 0%, rgba(255,0,0,0.7) 30%, rgba(255,0,0,0) 70%)'; /* Ensure gradient is reset */


            await new Promise(resolve => setTimeout(resolve, 600)); // Explosion duration

            statusDisplay.textContent = 'שלב: תגובה הסתיימה';

            // Reset for next run
            await new Promise(resolve => setTimeout(resolve, 2000)); // Wait before reset
            resetSimulation();
        };

        startButton.addEventListener('click', runSimulation);

        // Info Box functionality
        const clickableElements = [shellDiv, fuelDiv];
        clickableElements.forEach(element => {
            element.addEventListener('click', (event) => {
                // Only show info when not running simulation and on initial state
                if (!simulationRunning && statusDisplay.textContent === 'שלב: מוכן להצתה') {
                    const rect = element.getBoundingClientRect();
                    const simRect = simulationArea.getBoundingClientRect();

                     // Position relative to the simulation area
                    let relativeLeft = rect.left - simRect.left;
                    let relativeTop = rect.top - simRect.top;

                    infoBox.style.display = 'block'; // Temporarily show to measure
                    const infoRect = infoBox.getBoundingClientRect();
                    infoBox.style.display = 'none'; // Hide again

                    let boxLeft = relativeLeft + rect.width / 2 + 15; // Default to right of center
                    let boxTop = relativeTop + rect.height / 2 - infoRect.height / 2; // Vertically center

                    // Adjust if overflows right
                    if (boxLeft + infoRect.width > simRect.width - 10) {
                        boxLeft = relativeLeft + rect.width / 2 - infoRect.width - 15; // Place to the left
                    }
                     // Adjust if overflows bottom
                     if (boxTop + infoRect.height > simRect.height - 10) {
                        boxTop = simRect.height - infoRect.height - 10;
                     }
                     // Adjust if overflows top
                     if (boxTop < 10) {
                        boxTop = 10;
                     }
                     // Adjust if overflows left
                     if (boxLeft < 10) {
                         boxLeft = 10;
                     }


                    infoBox.style.left = `${boxLeft}px`;
                    infoBox.style.top = `${boxTop}px`;
                    infoBox.style.display = 'block';
                    infoBox.textContent = element.dataset.info || 'אין מידע נוסף זמין.';

                    event.stopPropagation(); // Prevent click from bubbling up
                }
            });
        });

        // Hide info box when clicking outside the elements or the info box itself
        document.addEventListener('click', (event) => {
             const isClickInsideApp = event.target.closest('#fusion-app');
             const isClickOnElement = event.target.closest('.target-shell, .target-fuel');
             const isClickInsideInfoBox = event.target.closest('#info-box');
             const isClickOnButton = event.target.closest('button');


             // Hide if click is inside the app but not on a clickable element, info box, or button
             if (isClickInsideApp && !isClickOnElement && !isClickInsideInfoBox && !isClickOnButton) {
                 infoBox.style.display = 'none';
             }
             // Also hide if clicking on the simulation area background itself
             if (event.target === simulationArea) {
                 infoBox.style.display = 'none';
             }
        });


        // Explanation toggle functionality
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.classList.contains('hidden');
            if (isHidden) {
                explanationDiv.classList.remove('hidden');
                explanationDiv.style.maxHeight = explanationDiv.scrollHeight + "px"; // Set max height for smooth transition (if using CSS transitions)
                toggleExplanationButton.textContent = 'הסתר הסבר מלא';
                 // Scroll to explanation if it's revealed
                 explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });

            } else {
                 // Temporarily set max height before adding hidden class for smooth collapse
                 explanationDiv.style.maxHeight = explanationDiv.scrollHeight + "px";
                 // Use a small timeout to allow CSS transition to start
                 setTimeout(() => {
                     explanationDiv.style.maxHeight = '0';
                     explanationDiv.addEventListener('transitionend', function handler() {
                          explanationDiv.classList.add('hidden');
                          explanationDiv.style.maxHeight = null; // Reset max height for next reveal
                          explanationDiv.removeEventListener('transitionend', handler);
                     });
                 }, 10); // Small delay
                toggleExplanationButton.textContent = 'הצג הסבר מלא';
            }
        });

        // Add CSS for smooth explanation toggle (requires CSS update too)
         explanationDiv.style.transition = 'max-height 0.5s ease-out';
         explanationDiv.style.overflow = 'hidden';


        // Initial reset to ensure correct state on load
        resetSimulation();
    });
</script>
```