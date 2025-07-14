---
title: "סוד הדיו: בריחה בצל הענן השחור (סימולטור דיונון)"
english_slug: secret-of-the-ink-squid-ink-production-simulator
category: "ביולוגיה ימית"
tags: [דיונונים, דיו, מנגנוני הגנה, ביולוגיה ימית, רכיכות, סימולציה]
---
<p>דמיינו לעצמכם שאתם צוללים במצולות הים, ולפתע - סכנה אורבת! מה עושה דיונון חכם כשהוא מרגיש מאוים? הוא לא נלחם חזיתית, אלא משתמש בטקטיקת הסוואה מדהימה. גלו בעצמכם את הכוח המסתורי של ענן הדיו השחור בסימולטור האינטראקטיבי הזה.</p>

<div id="simulation-area">
    <div id="water-environment">
         <div id="predator">🦈</div> <!-- Simple predator icon -->
        <div id="squid">
            <div id="ink-sac"></div>
            <div id="siphon"></div>
            <div id="squid-body">
                🦑
            </div>
             <div id="squid-eyes"></div> <!-- Added for potential animation -->
        </div>
        <div id="ink-cloud"></div>
    </div>
    <div id="controls">
        <label for="danger-level">עוצמת האיום:</label>
        <input type="range" id="danger-level" name="danger-level" min="1" max="10" value="3">
        <span id="danger-value">3</span>
        <button id="threaten-button">שחרר דיו!</button>
    </div>
</div>

<button id="toggleExplanation">הצג את סוד הדיו</button>

<div id="explanation" style="display: none;">
    <h2>הצצה עמוקה לסוד הדיו של הדיונון</h2>
    <p>ענן הדיו השחור שפולט דיונון הוא הרבה יותר מסתם "צבע". זהו כלי הישרדות אדיר, תערובת מורכבת של כימיקלים שמיועדת להטעות, לבלבל ולהרחיק טורפים.</p>

    <h3>מה מכיל הדיו?</h3>
    <p>המרכיב העיקרי ברוב סוגי הדיו של רכיכות ימיות הוא <strong>מֶלָנִין</strong> – כן, אותו פיגמנט שמקנה צבע לעור ולשיער שלנו! המלנין הוא שמקנה לדיו את צבעו הכהה והאטום. בנוסף למלנין, הדיו מכיל חלבונים, אנזימים, מוקוס (ריר) ותרכובות כימיות שונות שעשויות לגרות את חושיהם של טורפים או אפילו לדכא את חוש הריח שלהם, ובכך לפגוע ביכולתם לעקוב אחר הדיונון הנמלט.</p>

    <h3>מסע הדיו מבלוטה לענן</h3>
    <p>הדיו אינו נוצר בפתאומיות בעת סכנה, אלא מיוצר באופן שוטף וקבוע ב<strong>בלוטת דיו</strong> ייעודית (ink gland) הנמצאת בחלל הגוף של הדיונון. מבלוטת הדיו, הדיו הסמיך מועבר לאחסון ב<strong>שקית דיו</strong> גמישה (ink sac), מעין בלון קטן המלא בדיו מרוכז, הממוקמת בסמוך למערכת העיכול ולסיפון.</p>
    <p>כאשר הדיונון חש סכנה, הוא מפעיל שרירים מיוחדים סביב שקית הדיו. התכווצות השרירים דוחסת את השקית ומאלצת את הדיו לזרום במהירות דרך צינור קטן אל תוך ה<strong>סיפון</strong> (siphon). הסיפון הוא איבר שרירי המשמש את הדיונון בעיקר לתנועה מהירה: הדיונון שואף מים לחלל הגלימה ופולט אותם בחוזקה דרך הסיפון, מה שיוצר כוח דחף שמניע אותו אחורה (תנועת "ריאקטיבית"). כאשר הדיו משוחרר, הוא מתערבב עם זרם המים הנפלט מהסיפון, ונוצר ענן הדיו המוכר.</p>

    <h3>אמנות ההישרדות: מטרות שחרור הדיו</h3>
    <p>שחרור הדיו אינו אקראי, אלא טקטיקת הגנה מתוחכמת עם מספר מטרות עיקריות:</p>
    <ul>
        <li><b>מסך עשן ומיסוך ויזואלי:</b> ענן הדיו האפל מטשטש באופן מיידי את הראות בסביבת הדיונון, יוצר מסך המסתיר אותו ומאפשר לו לנצל את הרגע כדי לשנות כיוון או להגביר מהירות בריחה.</li>
        <li><b>בלבול והטעיה:</b> ענן הדיו הגדול והפתאומי יכול להלחיץ ולבלבל את הטורף, ואף לגרום לו לתקוף את הענן במקום את הדיונון עצמו. אצל מינים מסוימים, הדיו אף נשאר צפוף ויוצר צורה דמוית דיונון ('פסאודומורף' או 'כפיל'), מה שמושך את תשומת לב הטורף בזמן שהדיונון האמיתי נמלט בכיוון אחר.</li>
        <li><b>גירוי חושי:</b> כפי שצוין, חלק ממרכיבי הדיו יכולים לגרות את עיני הטורף, את חוש הריח שלו, או את מערכות חישה אחרות, ובכך להאט או להרתיע אותו.</li>
    </ul>

    <h3>הדיו משתנה ממין למין</h3>
    <p>לא כל הרכיכות הימיות בעלות דיו. נאוטילוס, למשל, נטול דיו. גם הרכב הדיו, צבעו המדויק וצורת ענן הדיו משתנים בין מיני דיונונים, תמנונים ודיואים שונים, בהתאם לצרכי ההגנה הספציפיים שלהם ולטורפים בסביבתם הטבעית.</p>

    <h3>מהדיו לכתיבה - וצלחת?</h3>
    <p>מעבר לתפקידו ההישרדותי, דיו דיונונים זכה לשימושים היסטוריים ומודרניים. בעבר, במיוחד דיו ממיני הספידה, עובד לדיו כתיבה וציור בצבע חום-שחור שנודע בשם "ספיה". כיום, הוא נפוץ בבישול, בעיקר במטבח הים תיכוני והאסייתי, ומוסיף צבע שחור עשיר וטעם ייחודי למנות פסטה, ריזוטו, פאייה ומאכלי ים אחרים. הוא נחשב גם למקור לחומרים בעלי עניין תזונתי או רפואי.</p>
</div>

<style>
    /* --- גלובליות ואזור סימולציה --- */
    #simulation-area {
        position: relative;
        width: 100%;
        max-width: 600px;
        height: 450px; /* הגדל גובה */
        border: 3px solid #005fa3; /* גבול מעט עמוק יותר */
        background: linear-gradient(to bottom, #e0f7ff 0%, #cceeff 100%); /* רקע מימי עדין */
        overflow: hidden;
        margin: 20px auto;
        border-radius: 12px; /* פינות מעוגלות יותר */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* צל עדין */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        padding: 15px; /* הגדל ריפוד */
        box-sizing: border-box;
    }

    #water-environment {
        position: relative;
        width: 100%;
        height: calc(100% - 80px); /* השאר מקום לבקרות וקצת שוליים */
        display: flex;
        justify-content: center; /* ממקם את הדיונון והטורף במרכז אופקית */
        align-items: flex-end; /* ממקם אותם בתחתית */
        perspective: 800px; /* הוסף פרספקטיבה לאפקט עומק קל */
    }

    /* --- דיונון --- */
    #squid {
        position: absolute;
        bottom: 20px; /* מיקום נמוך יותר במים */
        left: 50%;
        transform: translateX(-50%);
        width: 80px; /* קטן מעט */
        height: 120px; /* קטן מעט */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end;
        z-index: 2;
        transition: transform 0.6s cubic-bezier(0.25, 0.8, 0.25, 1), opacity 0.5s ease-out; /* אנימציה חלקה וטבעית יותר */
        transform-origin: bottom center; /* ציר סיבוב/קנה מידה */
    }

     #squid-body {
        font-size: 70px; /* קטן מעט בהתאם לגוף */
        line-height: 1;
        transform: rotate(90deg);
        filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.2)); /* צל עדין לדמות */
         transition: transform 0.3s ease-in-out; /* אנימציית גוף קלה */
    }

    #squid-eyes { /* אפקט עיניים קטן */
        position: absolute;
        top: 45px; /* מיקום על הגוף */
        width: 60%;
        height: 10px;
        /* background-color: rgba(0,0,0,0.1); */ /* הדמיית קו עיניים */
        /* border-radius: 50%; */
        z-index: 3;
        transition: opacity 0.3s ease-in-out;
        /* opacity: 0; /* חבוי עד למתח */
        color: #333; /* צבע עיניים */
        font-size: 10px;
        display: flex;
        justify-content: space-around;
        opacity: 0;
    }
     #squid-eyes:before, #squid-eyes:after {
        content: '•';
        display: inline-block;
     }


    #ink-sac {
        position: absolute;
        top: 25px; /* מיקום בתוך הגוף המשוער */
        width: 25px; /* קטן יותר */
        height: 35px; /* קטן יותר */
        background-color: #1a1a1a; /* צבע כהה יותר */
        border-radius: 50% 50% 40% 40%; /* צורה ריאליסטית יותר */
        opacity: 0.9;
        z-index: 1;
        transition: all 0.3s ease-in-out;
        transform-origin: bottom center;
    }

    #siphon {
        position: absolute;
        bottom: 10px; /* מיקום בתחתית הדיונון */
        width: 12px; /* רחב מעט */
        height: 30px; /* קצר יותר במנוחה */
        background-color: #333;
        border-radius: 6px 6px 0 0;
        opacity: 0; /* חבוי בהתחלה */
        transform-origin: bottom center;
        transition: height 0.2s ease-out, opacity 0.2s ease-out, transform 0.2s ease-out;
        z-index: 1;
    }

     #siphon.ejecting {
         height: 50px; /* מתארך בעת פליטה */
         opacity: 1;
         transform: scaleY(1.2); /* אפקט שחרור */
     }


    /* --- ענן דיו --- */
    #ink-cloud {
        position: absolute;
        bottom: 10px; /* מופיע ליד הסיפון */
        left: 50%;
        transform: translateX(-50%) scale(0);
        width: 60px; /* גודל התחלתי */
        height: 60px;
        background: radial-gradient(circle, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.7) 50%, rgba(0,0,0,0.4) 80%, rgba(0,0,0,0) 100%); /* מראה ענן מפוזר */
        border-radius: 50%;
        opacity: 0;
        z-index: 1;
        pointer-events: none;
        filter: blur(5px); /* טשטוש קל */
    }

    #ink-cloud.releasing {
        /* אנימציה נשלטת ע"י JS באמצעות CSS Variables */
        animation: releaseAndDissipate var(--ink-duration, 3s) forwards ease-out;
    }

    @keyframes releaseAndDissipate {
        0% {
            transform: translateX(-50%) scale(0.1);
            opacity: 1;
            filter: blur(3px);
        }
         10% { /* שיא הגודל והצפיפות מוקדם יותר */
             transform: translateX(-50%) scale(var(--ink-peak-scale, 2));
             opacity: 1;
             filter: blur(5px);
         }
        100% {
            transform: translateX(-50%) translateY(-50px) scale(var(--ink-final-scale, 4)); /* עולה מעט תוך התפזרות */
            opacity: 0;
             filter: blur(15px); /* טשטוש סופי */
        }
    }

    /* --- טורף --- */
    #predator {
        position: absolute;
        bottom: 50px; /* מיקום התחלתי רחוק יותר */
        left: 10%; /* מגיע מצד שמאל */
        font-size: 80px;
        transform: translateX(-200px) rotate(-20deg); /* מחוץ למסך, מסובב קלות */
        z-index: 2;
        opacity: 0; /* חבוי בהתחלה */
         transition: transform var(--predator-duration, 1s) ease-in-out, opacity 0.5s ease-in-out; /* אנימציית התקרבות */
         filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.2)); /* צל עדין */
    }

     #predator.approaching {
         opacity: 1;
     }


    /* --- בקרות --- */
    #controls {
        display: flex;
        align-items: center;
        gap: 20px; /* הגדל רווח */
        z-index: 3;
        background-color: rgba(255, 255, 255, 0.9); /* רקע שקוף למחצה */
        padding: 12px 20px; /* הגדל ריפוד */
        border-radius: 8px; /* פינות מעוגלות */
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
         width: calc(100% - 30px); /* רוחב מותאם */
         max-width: 400px;
         justify-content: center;
         flex-wrap: wrap; /* מאפשר מעבר שורה במסכים קטנים */
    }

    #controls label {
        font-weight: bold;
        color: #005fa3;
    }

    #controls input[type="range"] {
         flex-grow: 1; /* תופס כמה שיותר מקום */
         min-width: 100px; /* מונע התכווצות יתר */
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #ddd;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    #controls input[type="range"]:hover {
        opacity: 1;
    }

    #controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #0077cc;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
    }

    #controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #0077cc;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
    }

    #danger-value {
        font-weight: bold;
        color: #005fa3;
        min-width: 20px; /* מונע תזוזה בעת שינוי ערך */
        text-align: center;
    }


    #threaten-button {
        padding: 10px 20px; /* הגדל ריפוד */
        font-size: 1.1rem; /* הגדל פונט */
        cursor: pointer;
        background-color: #ff6666; /* צבע כפתור סכנה */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.2s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #threaten-button:hover {
        background-color: #ff4d4d;
    }

    #threaten-button:active {
         transform: scale(0.98); /* אפקט לחיצה */
    }

    /* --- כפתור הסבר ותוכן הסבר --- */
    #toggleExplanation {
        display: block;
        margin: 20px auto;
        padding: 12px 25px; /* הגדל ריפוד */
        font-size: 1.1rem; /* הגדל פונט */
        cursor: pointer;
        background-color: #0077cc;
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.2s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #toggleExplanation:hover {
        background-color: #005fa3;
    }
    #toggleExplanation:active {
         transform: scale(0.98);
    }


    #explanation {
        margin-top: 20px;
        padding: 20px; /* הגדל ריפוד */
        border: 1px solid #b0c4de; /* גבול עדין יותר */
        border-radius: 8px;
        background-color: #f0f8ff; /* רקע כחלחל בהיר */
        line-height: 1.7; /* רווח שורות נוח יותר לקריאה */
        color: #333;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    #explanation h2 {
        color: #005fa3;
        margin-top: 10px;
        margin-bottom: 10px;
        font-size: 1.5rem; /* הגדל כותרת */
        border-bottom: 2px solid #b0c4de; /* קו תחתון לכותרת ראשית */
        padding-bottom: 5px;
    }

    #explanation h3 {
         color: #0077cc;
         margin-top: 15px;
         margin-bottom: 5px;
         font-size: 1.2rem;
    }

     #explanation p {
        margin-bottom: 12px; /* רווח תחתון לפסקאות */
        text-align: justify; /* יישור דו-צדדי */
     }
     #explanation ul {
        margin-bottom: 12px;
        padding-left: 25px;
     }
     #explanation li {
        margin-bottom: 8px;
     }

</style>

<script>
    const threatenButton = document.getElementById('threaten-button');
    const dangerLevelInput = document.getElementById('danger-level');
    const dangerValueSpan = document.getElementById('danger-value');
    const inkCloud = document.getElementById('ink-cloud');
    const inkSac = document.getElementById('ink-sac');
    const siphon = document.getElementById('siphon');
    const squid = document.getElementById('squid');
    const squidBody = document.getElementById('squid-body');
    const squidEyes = document.getElementById('squid-eyes');
    const predator = document.getElementById('predator');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    let isInkReleasing = false;

    // --- פונקציות עזר ---

    // מעדכן את מראה הדיונון והטורף לפי רמת הסכנה
    function updateDangerDisplay(level) {
        dangerValueSpan.textContent = level;

        // ככל שהסכנה גדולה יותר, הטורף קרוב יותר והדיונון מתוח יותר
        const predatorDistance = 200 - (level - 1) * 15; // קרוב יותר ל-100px ברמה 10
        const predatorOpacity = Math.min(1, (level - 1) / 5); // נהיה גלוי לחלוטין מרמה 6
        const squidTensionScale = 1 + (level - 1) * 0.01; // גדל מעט מאוד
        const squidRecoilPotential = (level - 1) * 5; // פוטנציאל ריבאונד גדול יותר

        predator.style.setProperty('--predator-duration', '0.5s'); // אנימציה מהירה של התקרבות טורף איטית
        predator.style.transform = `translateX(${predatorDistance}px) rotate(-20deg)`; // Adjust X position based on distance
        predator.style.opacity = predatorOpacity;
        if (predatorOpacity > 0) {
             predator.classList.add('approaching');
        } else {
             predator.classList.remove('approaching');
        }


        // אפקט מתח על הדיונון (קנה מידה קל ועיניים)
        squid.style.transform = `translateX(-50%) scale(${squidTensionScale})`;
        squidEyes.style.opacity = Math.min(1, (level - 1) / 3); // עיניים נפתחות מרמה 4
         squidBody.style.transform = `rotate(90deg) translateY(-${(level - 1) * 0.5}px)`; // גוף נדרך קלות
    }

    // מפעיל את רצף שחרור הדיו
    function releaseInk(dangerLevel) {
        if (isInkReleasing) {
            return; // מונע הפעלה כפולה
        }
        isInkReleasing = true;

        // חישוב פרמטרים לאנימציה לפי רמת סכנה
        const duration = 3.5 - (dangerLevel - 1) * 0.25; // מהיר יותר לסכנה גבוהה (4.5s עד 1s)
        const inkPeakScale = 1.5 + (dangerLevel - 1) * 0.3; // ענן גדול יותר לסכנה גבוהה (פי 1.5 עד פי 4)
        const inkFinalScale = inkPeakScale * 1.5; // ממשיך להתפשט
        const squidRecoil = 20 + (dangerLevel - 1) * 5; // נסיגה חזקה יותר

        // הגדרת CSS Variables לאנימציית הדיו
        inkCloud.style.setProperty('--ink-duration', `${duration}s`);
        inkCloud.style.setProperty('--ink-peak-scale', inkPeakScale);
         inkCloud.style.setProperty('--ink-final-scale', inkFinalScale);

        // רצף אנימציות:
        // 1. הדיונון נסוג במהירות
        squid.style.transition = 'transform 0.3s ease-out, opacity 0.5s ease-out';
        squid.style.transform = `translateX(-50%) translateY(-${squidRecoil}px) scale(${1 + (dangerLevel-1)*0.02})`; // נסיגה כלפי מעלה וקנה מידה קל

        // 2. שק הדיו מתכווץ (ויזואלי)
        inkSac.style.transition = 'all 0.3s ease-in';
        inkSac.style.transform = 'scale(0.5)';
        inkSac.style.opacity = 0.3;

        // 3. הסיפון נפתח ופולט (אנימציה)
        setTimeout(() => {
            siphon.classList.add('ejecting');
        }, 150); // התחל סיפון קצת אחרי תחילת הנסיגה

        // 4. שחרור ענן הדיו (אנימציה)
         setTimeout(() => {
             inkCloud.classList.add('releasing');
             inkCloud.style.opacity = 1; // ודא שהוא גלוי
         }, 300); // התחל ענן אחרי שהסיפון התחיל לפלוט


        // 5. הטורף "נבלע" בענן ומתבלבל
         predator.style.transition = 'transform 1s ease-out, opacity 1s ease-out';
         predator.style.transform = `translateX(${inkCloud.offsetLeft - predator.offsetWidth/2}px) rotate(-10deg)`; // זז לכיוון הענן
         predator.style.opacity = 0.2; // נהיה פחות גלוי

        // 6. איפוס בסוף האנימציה (של הענן)
        inkCloud.addEventListener('animationend', handleInkReleaseEnd, { once: true });
    }

    // מטפל בסיום אנימציית ענן הדיו
    function handleInkReleaseEnd() {
        inkCloud.classList.remove('releasing');
        inkCloud.style.opacity = 0; // הסתר ענן
        inkCloud.style.transform = 'translateX(-50%) scale(0)'; // אפס גודל ומיקום התחלתי

        siphon.classList.remove('ejecting'); // אפס סיפון

        // אפס דיונון ושק דיו למצב רגיל (או מצב לפי הסליידר העדכני)
        squid.style.transition = 'transform 0.6s cubic-bezier(0.25, 0.8, 0.25, 1)'; // החזר אנימציית רגילה
        // הדיונון יחזור למצב סליידר באנימציה נפרדת או עם עדכון הסליידר
        // Temporarily reset squid to center, then let updateDangerDisplay handle its final position
        squid.style.transform = 'translateX(-50%) translateY(0) scale(1)'; // Reset position first

        inkSac.style.transition = 'all 0.5s ease-out';
        inkSac.style.transform = 'scale(1)'; // שק הדיו מתמלא מחדש (ויזואלי)
        inkSac.style.opacity = 0.9;

        // הטורף "מאבד עניין" או מתרחק (חוזר למצב סליידר)
        predator.style.transition = 'transform 1s ease-out, opacity 1s ease-out';
        // הטורף יחזור למצב סליידר באנימציה נפרדת או עם עדכון הסליידר

        // השהייה קלה לפני שמאפשרים שחרור דיו נוסף ועדכון תצוגה
        setTimeout(() => {
             isInkReleasing = false;
             // ודא שהתצוגה (דיונון, טורף) חוזרת למצב המתאים לרמת הסכנה הנוכחית בסליידר
             updateDangerDisplay(parseInt(dangerLevelInput.value));
        }, 500); // השהייה קצרה
    }


    // --- Event Listeners ---

    // עדכון תצוגת רמת סכנה ואפקטים ויזואליים בסליידר
    dangerLevelInput.addEventListener('input', () => {
        const level = parseInt(dangerLevelInput.value);
        updateDangerDisplay(level);
    });

    // לחיצה על כפתור "שחרר דיו!"
    threatenButton.addEventListener('click', () => {
        const dangerLevel = parseInt(dangerLevelInput.value);
        releaseInk(dangerLevel);
    });

    // הצגה/הסתרה של ההסבר
    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר את סוד הדיו';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג את סוד הדיו';
        }
    });

    // --- אתחול ---
    // הגדר מצב התחלתי של התצוגה לפי ערך הסליידר ההתחלתי
    updateDangerDisplay(parseInt(dangerLevelInput.value));
</script>
```