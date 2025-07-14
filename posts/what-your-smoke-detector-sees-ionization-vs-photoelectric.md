---
title: "הצצה לקרביים: כך גלאי העשן שלך 'רואה' שריפה"
english_slug: what-your-smoke-detector-sees-ionization-vs-photoelectric
category: "מדעים מדויקים / פיזיקה"
tags:
  - גלאי עשן
  - בטיחות אש
  - יוניזציה
  - פוטואלקטרי
  - פיזיקה של גלאים
  - סימולציה
---
# הצצה לקרביים: כך גלאי העשן שלך 'רואה' שריפה

נשימה עמוקה! רוב הזמן גלאי העשן שמעל ראשך יושב בשקט. אבל כשהסכנה אורבת, איך הוא יודע להזעיק עזרה? לא כל הגלאים זהים, והם מגיבים אחרת לסוגי אש שונים. בואו נצלול פנימה ונראה מה קורה באמת בתוך הקופסאות הקטנות האלה כשהעשן מגיע.

<div class="app-container">
    <h2>איך זה עובד? הדמיית גלאי עשן</h2>
    <div class="detectors-container">
        <div class="detector-panel ionization-detector">
            <h3>גלאי יוניזציה</h3>
            <div class="chamber" id="ionization-chamber">
                <div class="chamber-title">תא הגילוי</div>
                 <div class="ionization-source" title="מקור רדיואקטיבי">☢️</div>
                <div class="plate top-plate" title="אלקטרודה חיובית"></div>
                <div class="plate bottom-plate" title="אלקטרודה שלילית"></div>
                <div class="ions-container" id="ionization-ions">
                    <!-- Ions will be added here by JS -->
                </div>
                 <div class="current-flow" id="ionization-current-flow">
                    <div class="current-line"></div>
                    <div class="current-line"></div>
                    <div class="current-line"></div>
                </div>
                <div class="smoke-particles" id="ionization-smoke">
                    <!-- Smoke particles will be added here -->
                </div>
            </div>
            <div class="status" id="ionization-status"><span class="status-text">מוכן</span></div>
        </div>

        <div class="detector-panel photoelectric-detector">
            <h3>גלאי פוטואלקטרי</h3>
            <div class="chamber" id="photoelectric-chamber">
                 <div class="chamber-title">תא הגילוי</div>
                <div class="light-source" title="מקור אור (לד)">💡</div>
                <div class="light-beam" id="photoelectric-beam"></div>
                <div class="light-sensor" title="חיישן אור (פוטודיודה)">👁️</div>
                 <div class="scattered-light" id="photoelectric-scattered">
                    <!-- Scattered light lines will be added here -->
                 </div>
                <div class="smoke-particles" id="photoelectric-smoke">
                     <!-- Smoke particles will be added here -->
                </div>
            </div>
             <div class="status" id="photoelectric-status"><span class="status-text">מוכן</span></div>
        </div>
    </div>

    <div class="controls">
        <h4>בדוק את הגלאים עם:</h4>
        <button onclick="sendSmoke('small')">עשן מחלקיקים קטנים (שריפה מהירה ובוערת)</button>
        <button onclick="sendSmoke('large')">עשן מחלקיקים גדולים (שריפה איטית ועומדת)</button>
        <button onclick="resetSimulation()">נקה עשן</button>
    </div>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #28a745;
        --warning-color: #ffc107;
        --danger-color: #dc3545;
        --info-color: #17a2b8;
        --light-grey: #f8f9fa;
        --dark-grey: #343a40;
        --ionization-blue: #007bff;
        --photoelectric-yellow: #ffc107;
    }

    .app-container {
        font-family: 'Arial', sans-serif;
        max-width: 960px; /* Slightly wider */
        margin: 30px auto;
        padding: 30px;
        border: 1px solid #e0e0e0;
        border-radius: 12px; /* More rounded */
        background: linear-gradient(to bottom, #f9f9f9, #e9e9e9); /* Subtle gradient */
        text-align: center;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Deeper shadow */
    }

     h2 {
        color: var(--dark-grey);
        margin-bottom: 25px;
     }

    .detectors-container {
        display: flex;
        justify-content: space-around;
        margin-top: 25px;
        flex-wrap: wrap;
        gap: 20px; /* Space between items */
    }

    .detector-panel {
        background-color: #fff;
        border: 1px solid #d0d0d0;
        border-radius: 10px;
        padding: 20px;
        flex-basis: 48%; /* Flex basis for layout */
        min-width: 320px; /* Ensure minimum width */
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        display: flex;
        flex-direction: column;
        align-items: center;
        transition: transform 0.3s ease; /* Hover effect */
    }

    .detector-panel:hover {
         transform: translateY(-5px);
    }


    .detector-panel h3 {
        margin-top: 0;
        color: var(--dark-grey);
        font-size: 1.3em;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 8px;
        margin-bottom: 15px;
        width: 100%;
    }

    .chamber {
        width: 100%;
        height: 180px; /* Taller chamber */
        border: 2px dashed #b0b0b0; /* Stronger border */
        margin: 15px 0;
        position: relative;
        overflow: hidden;
        background-color: #e0e0e0; /* Light grey background */
        border-radius: 8px;
         box-shadow: inset 0 0 5px rgba(0,0,0,0.1);
    }

    .chamber-title {
        position: absolute;
        top: 5px;
        left: 10px;
        font-size: 0.9em;
        color: #666;
        z-index: 5; /* Above other elements */
    }


    .ionization-detector .chamber {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: #d0e0f0; /* Light blueish tint */
    }

    .ionization-source {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 1.5em; /* Slightly larger icon */
        z-index: 4;
        filter: drop-shadow(0 0 3px rgba(255, 0, 0, 0.5)); /* Subtle glow */
    }

     .plate {
        position: absolute;
        width: 80%;
        height: 12px; /* Thicker plates */
        background-color: var(--dark-grey);
        z-index: 3;
        border-radius: 3px;
     }

    .top-plate {
        top: 20px;
        box-shadow: 0 2px 3px rgba(0,0,0,0.1);
    }

    .bottom-plate {
        bottom: 20px;
        box-shadow: 0 -2px 3px rgba(0,0,0,0.1);
    }

     .ions-container {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 2;
        overflow: hidden;
     }

    .ion {
         position: absolute;
         width: 6px; /* Slightly larger ions */
         height: 6px;
         background-color: var(--ionization-blue); /* Blue ions */
         border-radius: 50%;
         animation: ion-drift 3s linear infinite; /* Slower drift */
         opacity: 0.8;
         transition: opacity 0.5s ease, transform 0.5s ease; /* Smooth fade */
         box-shadow: 0 0 3px rgba(0,0,255,0.5);
    }

    /* Adjust ion behavior based on smoke */
     .ionization-detector.smoke-small .ion {
         opacity: 0.1; /* Most ions blocked/captured */
     }

     .ionization-detector.smoke-large .ion {
         opacity: 0.6; /* Some ions blocked */
     }


    .current-flow {
        position: absolute;
        top: 32px; /* Between plates */
        bottom: 32px;
        left: 50%;
        width: 6px; /* Thicker current indicator */
        background-color: rgba(0, 128, 0, 0.8); /* Green current */
        z-index: 1;
        transition: height 0.5s ease, background-color 0.5s ease, width 0.5s ease;
        border-radius: 3px;
        overflow: hidden; /* Hide internal lines if current is low */
    }

    .current-line {
        width: 100%;
        height: 10px;
        background-color: rgba(255, 255, 255, 0.5); /* White lines for flow */
        margin-bottom: 5px;
        animation: current-flow-animation 1s linear infinite;
    }

    .ionization-detector .chamber .current-flow {
         height: calc(100% - 64px); /* Full height between plates */
         background-color: var(--secondary-color); /* Normal current color */
    }

    .ionization-detector.smoke-small .chamber .current-flow {
         height: 15px; /* Current significantly reduced */
         background-color: var(--danger-color); /* Red alarm */
         width: 8px;
         box-shadow: 0 0 10px var(--danger-color);
    }
    .ionization-detector.smoke-large .chamber .current-flow {
         height: calc(100% - 90px); /* Current slightly reduced */
         background-color: var(--warning-color); /* Orange warning */
         width: 6px;
         box-shadow: 0 0 5px var(--warning-color);
    }


    .photoelectric-detector .chamber {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 25px; /* More padding */
        background-color: #fff0d0; /* Light yellowish tint */
    }

    .light-source {
        font-size: 1.8em; /* Larger icon */
        z-index: 4;
        filter: drop-shadow(0 0 5px var(--photoelectric-yellow)); /* Glow */
    }

    .light-sensor {
        font-size: 1.8em; /* Larger icon */
        z-index: 4;
        color: #666; /* Darker grey */
    }

    .light-beam {
        position: absolute;
        left: 55px; /* Near source, slightly offset */
        top: 50%;
        transform: translateY(-50%);
        width: calc(100% - 110px); /* Spans across chamber */
        height: 4px; /* Thicker beam */
        background-color: var(--photoelectric-yellow);
        z-index: 1;
        opacity: 0.9;
        box-shadow: 0 0 8px var(--photoelectric-yellow);
        animation: light-pulse 1.5s ease-in-out infinite; /* Pulsing beam */
        border-radius: 2px;
    }

    .scattered-light {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 2;
        overflow: hidden;
        pointer-events: none; /* Don't block clicks */
    }

    .scattered-light-ray {
         position: absolute;
         width: 3px; /* Thicker rays */
         background-color: var(--photoelectric-yellow);
         transform-origin: 0 0;
         opacity: 0; /* Hidden by default */
         transition: opacity 0.5s ease;
         box-shadow: 0 0 5px rgba(255,193,7,0.7);
    }

     /* Scattered rays visible and animated when large smoke is present */
     .photoelectric-detector.smoke-large .scattered-light-ray {
         opacity: 0.9;
         animation: scattered-flicker 1s ease-out infinite alternate; /* Flicker effect */
     }

    .smoke-particles {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 5; /* Above internal components */
        pointer-events: none;
        opacity: 0; /* Hidden by default */
        transition: opacity 0.8s ease; /* Slower fade in */
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        align-content: space-around;
        animation: smoke-float 10s linear infinite; /* Subtle float animation */
    }

     .smoke-particles.visible {
         opacity: 0.95; /* More opaque when visible */
     }

    .smoke-particle {
        position: relative;
        border-radius: 50%;
        background-color: rgba(100, 100, 100, 0.8); /* Grey smoke */
        box-shadow: 0 0 2px rgba(0,0,0,0.5);
        animation: particle-wobble 3s ease-in-out infinite alternate; /* Individual particle movement */
    }

    .ionization-detector .smoke-particles .smoke-particle.small {
         width: 6px; /* Slightly larger */
         height: 6px;
         margin: 3px; /* More space */
    }
     .ionization-detector .smoke-particles .smoke-particle.large {
         width: 10px; /* Larger */
         height: 10px;
         margin: 5px;
     }

    .photoelectric-detector .smoke-particles .smoke-particle.small {
         width: 6px;
         height: 6px;
         margin: 3px;
    }
     .photoelectric-detector .smoke-particles .smoke-particle.large {
         width: 18px; /* Significantly larger */
         height: 18px;
         margin: 8px;
         box-shadow: 0 0 5px rgba(0,0,0,0.7); /* Stronger shadow for larger particles */
     }


    .status {
        margin-top: 15px;
        font-weight: bold;
        min-height: 1.5em; /* Reserve space */
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 8px;
        border-radius: 5px;
        width: 100%;
        text-align: center;
        transition: background-color 0.5s ease, color 0.5s ease;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }

    .status-text {
        flex-grow: 1; /* Make text span width */
    }

    .status.normal {
         color: var(--secondary-color);
         background-color: #e9f5ff;
         border: 1px solid var(--secondary-color);
    }
    .status.warning {
         color: var(--dark-grey);
         background-color: #fff3cd;
         border: 1px solid var(--warning-color);
    }
    .status.alarm {
         color: #fff;
         background-color: var(--danger-color);
         border: 1px solid var(--danger-color);
         animation: pulse-alarm 1s infinite alternate; /* Pulsing background */
    }

     /* Status icons (optional, can add via JS or data attributes) */
     .status.alarm::before { content: '🚨 '; }
     .status.warning::before { content: '⚠️ '; }
     .status.normal::before { content: '✅ '; }


    .controls {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px dashed #ccc;
    }

     .controls h4 {
         color: var(--dark-grey);
         margin-bottom: 15px;
     }

    .controls button {
        margin: 8px; /* More space */
        padding: 12px 20px; /* Larger padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* More rounded */
        background-color: var(--primary-color);
        color: white;
        transition: background-color 0.3s ease, transform 0.1s active;
        box-shadow: 0 3px 6px rgba(0,0,0,0.15);
    }

    .controls button:hover {
        background-color: #0056b3;
    }
     .controls button:active {
         transform: scale(0.98);
     }


    #explanation-button {
        display: block;
        width: fit-content;
        margin: 30px auto;
        padding: 12px 25px; /* Larger */
        font-size: 1.1em;
        cursor: pointer;
        border: 1px solid var(--primary-color);
        border-radius: 6px;
        background-color: #e9f5ff;
        color: var(--primary-color);
        transition: background-color 0.3s ease, color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    #explanation-button:hover {
        background-color: var(--primary-color);
        color: white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

    #explanation-content {
        max-width: 960px;
        margin: 30px auto;
        padding: 30px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: #fff;
        text-align: right;
        display: none; /* Hidden by default */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    }

    #explanation-content h2,
    #explanation-content h3,
    #explanation-content h4 {
        color: var(--dark-grey);
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
    }

     #explanation-content h2 { font-size: 1.8em; }
     #explanation-content h3 { font-size: 1.5em; }
     #explanation-content h4 { font-size: 1.2em; color: #555; }


    #explanation-content p,
    #explanation-content ul {
        line-height: 1.7; /* More space */
        margin-bottom: 15px;
        color: #555;
    }

     #explanation-content ul {
         padding-right: 20px;
     }
     #explanation-content li {
         margin-bottom: 8px;
     }


    /* Keyframe animation for ion movement */
    @keyframes ion-drift {
        0% { transform: translateY(0); }
        100% { transform: translateY(calc(100% - 40px)); } /* Drift towards bottom plate, relative to chamber height */
    }

     /* Keyframe animation for current flow lines */
     @keyframes current-flow-animation {
         0% { transform: translateY(0); }
         100% { transform: translateY(25px); /* Move lines down */ }
     }

     /* Keyframe animation for light beam pulse */
     @keyframes light-pulse {
         0% { transform: translateY(-50%) scaleX(1); opacity: 0.9; }
         50% { transform: translateY(-50%) scaleX(1.01); opacity: 1; }
         100% { transform: translateY(-50%) scaleX(1); opacity: 0.9; }
     }

     /* Keyframe animation for scattered light flicker */
     @keyframes scattered-flicker {
         0% { opacity: 0.8; }
         50% { opacity: 1; }
         100% { opacity: 0.8; }
     }

     /* Keyframe animation for overall smoke float */
     @keyframes smoke-float {
         0% { transform: translateY(0); }
         50% { transform: translateY(-5px); }
         100% { transform: translateY(0); }
     }

     /* Keyframe animation for individual particle wobble */
      @keyframes particle-wobble {
          0% { transform: translate(0, 0); }
          25% { transform: translate(1px, 1px); }
          50% { transform: translate(0, 0); }
          75% { transform: translate(-1px, 1px); }
          100% { transform: translate(0, 0); }
      }


     /* Keyframe animation for alarm pulse */
     @keyframes pulse-alarm {
         0% { box-shadow: 0 0 0 0 rgba(220, 53, 69, 0.7); }
         70% { box-shadow: 0 0 0 10px rgba(220, 53, 69, 0); }
         100% { box-shadow: 0 0 0 0 rgba(220, 53, 69, 0); }
     }


</style>

<button id="explanation-button">רוצים לדעת עוד? לחצו להסבר המלא</button>

<div id="explanation-content">
    <h2>הבנת גלאי העשן שלך - לעומק</h2>
    <p>גלאי עשן אינם סתם "זיהוי עשן פשוט". הם מתוכננים להגיב לחלקיקים מסוימים באוויר המעידים על שריפה, אך השיטות לזיהוי החלקיקים הללו שונות משמעותית בין הסוגים העיקריים, ומשפיעות על מידת יעילותם מול סוגי אש שונים.</p>

    <h3>צמד הטכנולוגיות המובילות: יוניזציה מול פוטואלקטרי</h3>
    <p>עולם גלאי העשן הביתי נשלט בעיקר על ידי שני סוגי מנגנונים:</p>

    <h4>גלאי יוניזציה: כשחלקיקים קטנים שוברים את הזרם</h4>
    <ul>
        <li>**מנגנון פעולה:** דמיינו תא קטן עם שתי לוחיות מתכת (אלקטרודות) ומקור רדיואקטיבי זעיר ביניהן (בדרך כלל אמריציום-241). המקור פולט חלקיקי אלפא "בלתי מזיקים" (שנעצרים בקלות ע"י האוויר או הפלסטיק של הגלאי), שמייננים את מולקולות האוויר בתוך התא - כלומר, גורמים לאטומים או למולקולות לאבד או לקבל אלקטרון ולהפוך ליונים בעלי מטען חשמלי. נוצר "זרם" קבוע של יונים חיוביים ושליליים הנעים לעבר האלקטרודות בעלות המטען הנגדי, הודות למתח חשמלי קטן שמושרה עליהן.</li>
        <li>**כיצד עשן מפעיל את האזעקה?** כשהעשן נכנס לתא, בעיקר חלקיקי עשן קטנים מאוד שנוצרים בשריפות בוערות (כמו עץ או נייר), הם "נתקלים" ביונים הקטנים והניידים ו"מנטרלים" אותם. יונים שנקשרים לחלקיקי עשן גדולים פחות ויכולים לנוע בחופשיות. כתוצאה מכך, הזרם החשמלי החלש שזורם בתא פוחת בצורה משמעותית. ירידה זו מזוהה ע"י מעגל אלקטרוני, וכשהזרם יורד מתחת לסף קריטי, הוא מפעיל את האזעקה הקולנית.</li>
        <li>**רגישות וחסרונות:** גלאי יוניזציה מצטיינים בזיהוי מהיר של שריפות שמתפתחות במהירות עם להבות (Fast Flaming Fires) ופולטות חלקיקים קטנים. עם זאת, הם רגישים פחות לעשן סמיך מחלקיקים גדולים שמאפיין שריפות "עומדות" (Smoldering Fires). בנוסף, הם נוטים יותר לאזעקות שווא מאדים (כמו מאמבטיה) או עשן בישול קל, בשל רגישותם הגבוהה לכל שינוי במוליכות האוויר בתא.</li>
    </ul>

    <h4>גלאי פוטואלקטרי (אופטי): כשחלקיקים גדולים מפזרים את האור</h4>
    <ul>
        <li>**מנגנון פעולה:** תא הגילוי בגלאי פוטואלקטרי מכיל מקור אור (לרוב נורת LED קטנה הפולטת אור אינפרא אדום או אור נראה) וחיישן אור (פוטודיודה), אך הם ממוקמים בזווית - הקרן מהמקור אינה פוגעת ישירות בחיישן במצב רגיל.</li>
        <li>**כיצד עשן מפעיל את האזעקה?** כאשר חלקיקי עשן נכנסים לתא, במיוחד חלקיקים גדולים וכבדים יותר שנוצרים בשריפות עומדות (כמו שריפת פלסטיק, ריהוט מרופד, או כבלים חשמליים), הם "חוצים" את נתיב קרן האור וגורמים לה להתפזר לכל הכיוונים. חלק מהאור המפוזר הזה "מוסט" ומגיע לחיישן האור. כאשר כמות האור שמגיעה לחיישן עוברת סף מוגדר מראש, הגלאי מזהה זאת כאיתור עשן ומפעיל את האזעקה.</li>
        <li>**רגישות וחסרונות:** גלאי פוטואלקטרי רגישים במיוחד לשריפות עומדות ומעשנות (Smoldering Fires) הפולטות חלקיקים גדולים. הם פחות רגישים לאזעקות שווא מאדים או עשן בישול קל בהשוואה לגלאי יוניזציה. עם זאת, הם עשויים להיות איטיים יותר בזיהוי שריפות בוערות מהירות מאוד עם מעט עשן נראה לעין.</li>
    </ul>

    <h3>לסיכום: איזה גלאי עשן הכי טוב עבורי?</h3>
    <p>התשובה הפשוטה: אין גלאי אחד "הכי טוב" לכל סוגי השריפות. הדרך האפקטיבית ביותר להבטיח בטיחות מקסימלית היא לשלב בין הטכנולוגיות.</p>
    <ul>
        <li>**גלאים משולבים (Combination / Dual Sensor):** האפשרות המומלצת ביותר היא להתקין גלאים שמכילים את שני המנגנונים באותה יחידה. גלאים אלו מסוגלים להגיב במהירות למגוון רחב יותר של סוגי שריפות.</li>
        <li>**התקנת גלאים מסוגים שונים:** אם מתקינים גלאים נפרדים, מומלץ להתקין גלאים פוטואלקטריים באזורים בהם יש סיכון גבוה לשריפות עומדות ומעשנות (למשל, ליד מטבחים - אך לא קרוב מדי לכיריים! - ובמסדרונות), וגלאי יוניזציה באזורים אחרים בהם הסיכון גבוה יותר לשריפות בוערות (למשל, חדרי מגורים עם אלקטרוניקה).</li>
    </ul>
    <p>מעבר לסוג הגלאי, זכרו תמיד את כללי הבסיס: התקינו גלאים בכל קומה, במסדרונות המובילים לחדרי שינה, ובתוך חדרי שינה (בהתאם להמלצות תקן מקומי). בדקו אותם מדי חודש (לחיצה על כפתור הבדיקה), החליפו בטריות לפחות פעם בשנה, והחליפו את הגלאי כולו כל 10 שנים (בדקו את תאריך הייצור או התפוגה). גלאי תקין ומתוחזק הוא ההבדל הדק שבין סכנה לבטיחות.</p>
</div>

<script>
    const ionizationChamber = document.getElementById('ionization-chamber');
    const photoelectricChamber = document.getElementById('photoelectric-chamber');
    const ionizationStatus = document.getElementById('ionization-status');
    const photoelectricStatus = document.getElementById('photoelectric-status');
    const ionizationSmokeDiv = document.getElementById('ionization-smoke');
    const photoelectricSmokeDiv = document.getElementById('photoelectric-smoke');
    const ionizationDetectorPanel = document.querySelector('.ionization-detector');
    const photoelectricDetectorPanel = document.querySelector('.photoelectric-detector');
    const explanationButton = document.getElementById('explanation-button');
    const explanationContent = document.getElementById('explanation-content');
    const ionizationCurrentFlow = document.getElementById('ionization-current-flow');


    const numIons = 60; // More visible ions
    const numSmokeParticlesSmall = 100; // More particles for visual density
    const numSmokeParticlesLarge = 30; // More particles for visual density
    const numScatteredRays = 15; // More scattered light rays

    // Create initial ions
    function createIons() {
        const ionsContainer = document.getElementById('ionization-ions');
        ionsContainer.innerHTML = ''; // Clear existing
        const chamberHeight = ionizationChamber.offsetHeight;
        const platePadding = 40; // Space taken by plates

        for (let i = 0; i < numIons; i++) {
            const ion = document.createElement('div');
            ion.classList.add('ion');
            // Random initial position between plates
            const initialY = platePadding + Math.random() * (chamberHeight - 2 * platePadding);
            ion.style.top = `${initialY}px`;
            ion.style.left = `${Math.random() * 90 + 5}%`; // Stay within side boundaries
            // Stagger animation start
            ion.style.animationDelay = `-${Math.random() * 3}s`;
            ionsContainer.appendChild(ion);
        }
    }

    // Create scattered light rays for photoelectric
    function createScatteredRays() {
        const scatteredLightContainer = document.getElementById('photoelectric-scattered');
        scatteredLightContainer.innerHTML = ''; // Clear existing

        // Get relative positions within the chamber
        const chamberRect = photoelectricChamber.getBoundingClientRect();
        const sourceElement = photoelectricChamber.querySelector('.light-source');
        const sensorElement = photoelectricChamber.querySelector('.light-sensor');
        const lightBeamElement = photoelectricChamber.querySelector('.light-beam');

        if (!sourceElement || !sensorElement || !lightBeamElement) return;

        const sourceRect = sourceElement.getBoundingClientRect();
        const sensorRect = sensorElement.getBoundingClientRect();
        const beamRect = lightBeamElement.getBoundingClientRect();


        // Calculate source and sensor center relative to chamber
        const sourceX = sourceRect.left + sourceRect.width / 2 - chamberRect.left;
        const sourceY = sourceRect.top + sourceRect.height / 2 - chamberRect.top;
        const sensorX = sensorRect.left + sensorRect.width / 2 - chamberRect.left;
        const sensorY = sensorRect.top + sensorRect.height / 2 - chamberRect.top;

        // Approximate beam path center Y
        const beamY = beamRect.top + beamRect.height / 2 - chamberRect.top;


        for (let i = 0; i < numScatteredRays; i++) {
            const ray = document.createElement('div');
            ray.classList.add('scattered-light-ray');

             // Calculate a start point near the beam path
             // Add some randomness around the beam's vertical center
             const startY = beamY + (Math.random() - 0.5) * 20; // Vertical spread near beam
             // Add randomness along the beam's horizontal path (but not too close to source/sensor)
             const startX = sourceX + (chamberRect.width - sourceX - (chamberRect.width - sensorX)) * 0.3 + Math.random() * ((chamberRect.width - sourceX - (chamberRect.width - sensorX)) * 0.4); // Spread start points in the middle section


             // Calculate end point near the sensor area
             const endX = sensorX + (Math.random() - 0.5) * sensorRect.width * 0.5; // Random point within sensor horizontal bounds
             const endY = sensorY + (Math.random() - 0.5) * sensorRect.height * 0.5; // Random point within sensor vertical bounds


             const deltaX = endX - startX;
             const deltaY = endY - startY;
             const distance = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
             const angle = Math.atan2(deltaY, deltaX) * 180 / Math.PI;

             ray.style.width = `${distance}px`;
             // Position the ray using transform (more reliable)
             ray.style.transform = `translate(${startX}px, ${startY}px) rotate(${angle}deg)`;
             ray.style.transformOrigin = '0 0'; // Rotate from the start point
             ray.style.height = '3px'; // Thickness

            scatteredLightContainer.appendChild(ray);
        }
    }

     // Create smoke particles inside the smoke-particles div
    function createSmokeParticles(container, count, sizeClass) {
        container.innerHTML = ''; // Clear existing
        for (let i = 0; i < count; i++) {
            const particle = document.createElement('div');
            particle.classList.add('smoke-particle', sizeClass);
            // Position is handled by flexbox in CSS
            container.appendChild(particle);
        }
    }


    function sendSmoke(particleSize) {
        resetSimulation(false); // Clear previous state visuals, but keep elements like ions/rays

        // Add smoke particles
        const ionizationParticleCount = particleSize === 'small' ? numSmokeParticlesSmall : numSmokeParticlesLarge;
        const photoelectricParticleCount = particleSize === 'small' ? numSmokeParticlesSmall : numSmokeParticlesLarge;

        createSmokeParticles(ionizationSmokeDiv, ionizationParticleCount, particleSize);
        createSmokeParticles(photoelectricSmokeDiv, photoelectricParticleCount, particleSize);

        // Make smoke visible
        ionizationSmokeDiv.classList.add('visible');
        photoelectricSmokeDiv.classList.add('visible');

        // Apply smoke effect classes to detector panels
        ionizationDetectorPanel.classList.add(`smoke-${particleSize}`);
        photoelectricDetectorPanel.classList.add(`smoke-${particleSize}`);


        // Update detector states based on smoke and detector type
        // Ionization Detector
        if (particleSize === 'small') {
            ionizationStatus.querySelector('.status-text').textContent = "אזעקה! (שריפה בוערת)";
            ionizationStatus.className = 'status alarm';
        } else { // large particles
             ionizationStatus.querySelector('.status-text').textContent = "מזהה עשן (עשן גדול)"; // Less effective detection
             ionizationStatus.className = 'status warning';
        }

        // Photoelectric Detector
         if (particleSize === 'large') {
             photoelectricStatus.querySelector('.status-text').textContent = "אזעקה! (שריפה עומדת)";
             photoelectricStatus.className = 'status alarm';
         } else { // small particles
             photoelectricStatus.querySelector('.status-text').textContent = "מזהה עשן (עשן קטן)"; // Less effective detection
             photoelectricStatus.className = 'status warning';
         }
    }

    function resetSimulation(clearElements = true) {
        // Remove smoke classes from panels
        ionizationDetectorPanel.classList.remove('smoke-small', 'smoke-large');
        photoelectricDetectorPanel.classList.remove('smoke-small', 'smoke-large');

        // Hide and clear smoke particles
        ionizationSmokeDiv.classList.remove('visible');
        photoelectricSmokeDiv.classList.remove('visible');
        if (clearElements) {
             ionizationSmokeDiv.innerHTML = '';
             photoelectricSmokeDiv.innerHTML = '';
             // Recreate ions and rays as they might have been affected/removed visually
             createIons();
             createScatteredRays();
        }

        // Reset status texts and classes
        ionizationStatus.querySelector('.status-text').textContent = "מוכן";
        ionizationStatus.className = 'status normal';
        photoelectricStatus.querySelector('.status-text').textContent = "מוכן";
        photoelectricStatus.className = 'status normal';

        // Ensure current flow and scattered rays are visually reset via CSS transitions
        // This happens automatically when smoke-* classes are removed
    }

    // Toggle explanation visibility
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר' : 'רוצים לדעת עוד? לחצו להסבר המלא';
    });

    // Initial setup on page load
    document.addEventListener('DOMContentLoaded', () => {
        createIons();
        createScatteredRays(); // Create ray elements, CSS hides them by default
        // Ensure initial status is 'מוכן' and 'normal' class
        ionizationStatus.querySelector('.status-text').textContent = "מוכן";
        ionizationStatus.className = 'status normal';
        photoelectricStatus.querySelector('.status-text').textContent = "מוכן";
        photoelectricStatus.className = 'status normal';
    });


</script>
```