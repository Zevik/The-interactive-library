---
title: "מסע וירטואלי באמנות הקדרות: מחימר ליצירה מוגמרת"
english_slug: virtual-pottery-simulator-design-fire-glaze
category: "אמנות ועיצוב / כללי"
tags: ["קדרות", "אובניים", "חרס", "אמנות", "יצירה", "סימולטור"]
---
<header class="page-header">
    <h1>מסע וירטואלי באמנות הקדרות: מחימר ליצירה מוגמרת</h1>
    <p class="intro-text">תמיד חלמתם לגעת בחימר, להרגיש את סיבוב האובניים וליצור כלי שכולו שלכם? ברוכים הבאים לסימולטור הקדרות הווירטואלי שלנו! כאן תוכלו לצלול לעולם הקסום של הקדרות, החל מהכנת גוש חימר חסר צורה, דרך העיצוב המרתק על האובניים, שלבי השרפה המכריעים ועד לבחירת הזיגוג המושלם שיעניק ליצירה שלכם את הגימור הסופי. התנסו, למדו, וגלו את הקדר שבכם!</p>
</header>

<div class="pottery-simulator">
    <div class="simulator-area">
        <div id="pottery-stage" class="stage-clay-prep">
            <div class="clay-mass"></div>
            <div class="pottery-wheel"></div>
        </div>
        <div id="simulation-controls" class="controls">
            <h2>מסלול היצירה:</h2>
            <button data-stage="clay-prep" class="stage-button">הכנת החימר ומרכוז</button>
            <button data-stage="shaping" class="stage-button" disabled>פיסול על האובניים</button>
            <button data-stage="drying" class="stage-button" disabled>ייבוש - שלב העור</button>
            <button data-stage="bisque" class="stage-button" disabled>שרפה ראשונה (ביסק)</button>
            <button data-stage="glazing" class="stage-button" disabled>שלב הזיגוג</button>
            <button data-stage="glaze-fire" class="stage-button" disabled>שרפת הגלייז הסופית</button>
            
            <div id="shaping-tools" class="tool-controls">
                <h3>הכלים שבידיים:</h3>
                <button data-tool="fingers">אצבעות</button>
                <button data-tool="metal-rib">כלי מתכת</button>
                <button data-tool="sponge">ספוג</button>
                <div class="control-group">
                    <label for="wheel-speed">מהירות אובניים:</label>
                    <input type="range" min="10" max="200" value="100" class="slider" id="wheel-speed">
                </div>
            </div>
            
            <div id="glazing-options" class="glazing-controls">
                <h3>צבע וברק:</h3>
                <button data-glaze="blue-glossy">כחול מבריק</button>
                <button data-glaze="white-matte">לבן מט</button>
                <button data-glaze="clear-satin">שקוף סאטן</button>
            </div>
            
            <button id="save-btn" disabled>שמור יצירה מוגמרת</button>
        </div>
    </div>
    <div id="simulation-feedback" class="feedback-area">
        <h2>מה קורה עכשיו:</h2>
        <p id="current-feedback">ברוכים הבאים! בחרו את השלב הראשון במסע הקדרות שלכם.</p>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצגת הסבר תיאורטי מעמיק</button>

<div id="full-explanation" style="display: none;">
    <header>
        <h2>פותחים צוהר לעולם הקדרות: ידע תיאורטי מעמיק</h2>
    </header>

    <section>
        <h3>חימר: הקסם שמאחורי החומר הפלסטי</h3>
        <p>חימר הוא פלא טבעי! הוא מורכב ממינרלים זעירים ממשפחת הסיליקטים, בעיקר קאוליניט, בעלי מבנה לוחיות דקיקות. כשהוסיפים מים לחימר יבש, מולקולות המים חודרות בין הלוחיות ומאפשרות להן להחליק אחת על השנייה. זהו סוד הפלסטיות שלו – היכולת המופלאה לשנות צורה בקלות מבלי להיקרע. איכות הפלסטיות תלויה בסוג החימר, גודל חלקיקיו וכמות הלחות.</p>
    </section>

    <section>
        <h3>האובניים והמכניקה: לרקוד עם החומר</h3>
        <p>עבודה על אובניים היא אמנות של שליטה בכוחות. הכוח הצנטריפוגלי הנוצר מסיבוב המשטח דוחף את החימר החוצה. הקדר, בעזרת מים (כחומר סיכה הכרחי!) וידיים אמונות או כלים, מפעיל לחץ פנימי וחיצוני כדי לרכז את הגוש, "לעלות" את הדפנות ולפסל את הכלי לצורתו הסופית. מהירות האובניים משפיעה ישירות על עוצמת הכוח וקצב העיצוב – דורש דיוק ותרגול!</p>
    </section>

    <section>
        <h3>תהליך הייבוש: מסע ההתקשות של החימר</h3>
        <p>לאחר העיצוב, הכלי מתחיל לאבד מים ומתכווץ כשהלוחיות מתקרבות. ישנם שלושה שלבי ייבוש מרכזיים, כל אחד עם מאפיינים ויכולות שונות לעבודה:
        <ul>
            <li><strong>רטוב (Wet):</strong> מיד לאחר הפיסול, רך וגמיש, מושלם לשינויים גדולים.</li>
            <li><strong>שלב עור (Leather Hard):</strong> רוב המים התאדו, אך הוא עדיין מכיל לחות מסוימת. הכלי יציב אך ניתן עדיין לחתוך, לגלף, או להוסיף לו אלמנטים כמו ידיות. שלב קריטי לעיבודים עדינים.</li>
            <li><strong>יבש עצם (Bone Dry):</strong> כל המים התאדו. הכלי קל מאוד, שביר ביותר, והתכווצות הייבוש הסתיימה. מוכן לשרפה ראשונה!</li>
        </ul></p>
    </section>

    <section>
        <h3>שרפת הביסק: הפיכת החימר לחרס</h3>
        <p>השרפה הראשונה, בדרך כלל בטמפרטורות שבין 800 ל-1000 מעלות צלזיוס. כאן מתרחש שינוי בלתי הפיך:
        <ul>
            <li><strong>סילוק מים קשורים:</strong> מים המחוברים למבנה המולקולרי של החימר משתחררים.</li>
            <li><strong>התחלת סינטור:</strong> חלקיקי החימר מתחילים להתחבר זה לזה בנקודות המגע, תהליך של התמזגות בחום.</li>
            <li><strong>שינויים כימיים נוספים</strong> מתרחשים במינרלים השונים.</li>
        </ul>
        התוצר: חרס מוצק אך נקבובי (סופג נוזלים), שהפך מחומר גלם קרמי לחומר קרמי קבוע, מוכן לקליטת הזיגוג.</p>
    </section>

    <section>
        <h3>הרכב הזיגוג: המדע שמאחורי הציפוי</h3>
        <p>זיגוג הוא בעצם שכבת זכוכית המצפה את הכלי, ומורכב משלושה מרכיבים בסיסיים:
        <ul>
            <li><strong>סיליקה (SiO₂):</strong> עמוד השדרה הזכוכיתי. נמסה בחום גבוה ויוצרת את המבנה.</li>
            <li><strong>פלוקסים (Flaxes):</strong> כמו תחמוצות אלקליות (נתרן, אשלגן) או אלקליים עפרוריים (סידן, מגנזיום). הם מורידים את טמפרטורת ההתכה של הסיליקה ומאפשרים לה להפוך לזכוכית בטמפרטורות סבירות לתנור קדרות.</li>
            <li><strong>מייצבים (Stabilizers):</strong> בעיקר אלומינה (Al₂O₃). מונעים מהזיגוג "לנזול" מהכלי בזמן השרפה ומגבירים את עמידותו.</li>
        </ul>
        לכך מוספים צבענים (תחמוצות מתכת), חומרי עכירות (להפיכת הזיגוג לאטום), וחומרים אחרים לאפקטים מיוחדים.</p>
    </section>

    <section>
        <h3>שרפת הגלייז: הפיכת הציפוי לזכוכית</h3>
        <p>השרפה השנייה והחמה יותר (1000-1250 מעלות צלזיוס ויותר, תלוי בחומרים). בטמפרטורות אלו:
        <ul>
            <li>אבקת הזיגוג על פני הביסק מתחילה להתמוסס לנוזל צמיג.</li>
            <li>כשהחום עולה, הנוזל נעשה פחות צמיג, משתטח וממלא את הנקבוביות בחרס הביסק.</li>
            <li>נוצרת שכבת קישור כימית בין החרס לזיגוג, המבטיחה שהציפוי לא יתקלף.</li>
            <li>במהלך הקירור המבוקר, הזיגוג מתמצק למצב אמורפי (זכוכיתי), יוצר שכבה אטומה, קשה ועמידה, בגימור מבריק או מט לפי הרכבו.</li>
        </ul>
        שלב זה הופך את הכלי לשימושי, עמיד בפני נוזלים ומרהיב ביופיו.</p>
    </section>

    <section>
        <h3>טמפרטורה וזמן: המפתח לתוצאה מושלמת</h3>
        <p>עקומת השרפה (קצב עליית הטמפרטורה, זמן השהייה בחום המקסימלי וקצב הקירור) היא קריטית לתוצאה הסופית:
        <ul>
            <li><strong>חוזק:</strong> טמפרטורה גבוהה יותר מגבירה את הסינטור בתוך החרס והופכת אותו לצפוף וחזק יותר (למשל פורצלן).</li>
            <li><strong>צבע:</strong> טמפרטורות שונות או אטמוספרות שרפה שונות (מחזרת/מחמצנת) יכולות לשנות דרמטית את גוון הצבענים בזיגוג ובחימר.</li>
            <li><strong>טקסטורת הזיגוג:</strong> הגימור (מבריק, מט) והאפקטים המיוחדים נקבעים על ידי הרכב הזיגוג, טמפרטורת השיא וקצב הקירור (המשפיע על התגבשות). טמפרטורה לא מדויקת יכולה להרוס את הזיגוג.</li>
        </ul></p>
    </section>

    <section>
        <h3>מסע האש: סוגי תנורים ותהליכי שרפה בקדרות</h3>
        <p>עולם השרפה מגוון, וכל תנור ותהליך מוסיפים את ה"חתימה" שלהם ליצירה:
        <ul>
            <li><strong>תנורים חשמליים:</strong> נפוצים, מדויקים וקלים לשליטה, יוצרים לרוב אטמוספרה מחמצנת.</li>
            <li><strong>תנורי גז:</strong> מאפשרים בקרה על האטמוספרה וליצור שרפה מחזרת (פחות חמצן) לאפקטים מיוחדים בצבעים (למשל, ירוק נחושת הופך לאדום).</li>
            <li><strong>תנורי עץ:</strong> מסורתיים, יוצרים אפקטים פראיים וייחודיים מאפר ועשן הנוגעים בכלים.</li>
            <li><strong>ראקו (Raku):</strong> טכניקת שרפה מהירה ודרמטית שבה הכלים מוצאים מהתנור כשהם לוהטים ומוכנסים לחומרים דליקים, ליצירת פיח ואפקטים מתכתיים מדהימים בזיגוג.</li>
        </ul>
        הבנת התנור והתהליך היא חלק בלתי נפרד מאמנות הקדרות.</p>
    </section>

</div>

<style>
    /* Custom Properties for easier theme changes */
    :root {
        --clay-dark: #6b3e26; /* Richer brown */
        --clay-medium: #8c5e3d; /* Earthy brown */
        --clay-light: #a87d5c; /* Lighter tan */
        --bisque-color: #e0b18a; /* Warm, fired bisque */
        --glaze-blue: #4682b4; /* SteelBlue */
        --glaze-white: #f5f5dc; /* Beige */
        --glaze-clear: rgba(255, 255, 255, 0.5); /* Semi-transparent */
        --background-light: #f8f4e3; /* Off-white/cream */
        --background-medium: #ece3d2; /* Light beige */
        --border-color: #d1c7b7; /* Soft border */
        --shadow-color: rgba(0, 0, 0, 0.1);
        --accent-color: #a0522d; /* Sienna/terracotta accent */
        --text-color: #333;
        --font-family-main: 'Arial', sans-serif; /* Replace with a nicer font if available */
    }

    body {
        font-family: var(--font-family-main);
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-medium);
        margin: 0;
        padding: 20px;
    }

    .page-header {
        text-align: center;
        margin-bottom: 30px;
    }

    .page-header h1 {
        color: var(--accent-color);
        margin-bottom: 10px;
        font-size: 2.2em;
        text-shadow: 1px 1px 2px var(--shadow-color);
    }

    .intro-text {
        max-width: 800px;
        margin: 0 auto;
        font-size: 1.1em;
        color: var(--text-color);
    }

    .pottery-simulator {
        display: flex;
        flex-direction: column;
        gap: 30px;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--background-light);
        box-shadow: 0 5px 15px var(--shadow-color);
        max-width: 900px;
        margin: 20px auto;
    }

    .simulator-area {
        display: flex;
        flex-direction: column; /* Stack on small screens */
        gap: 30px;
    }
     @media (min-width: 768px) {
        .simulator-area {
             flex-direction: row; /* Side-by-side on larger screens */
        }
     }


    /* Stage Area Styling */
    #pottery-stage {
        flex: 2; /* Give more space to the visual */
        min-height: 350px; /* Increased height */
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: center;
        background: linear-gradient(to bottom, #e0e0e0, #c0c0c0); /* Subtle gradient background */
        border: 1px solid var(--border-color);
        border-radius: 8px;
        position: relative; /* For potential absolute positioning of tools/effects */
        overflow: hidden; /* Hide potential overflow from animations */
    }

    .clay-mass {
        width: 120px; /* Larger visual elements */
        height: 100px;
        border-radius: 50% 50% 20% 20%;
        background-color: var(--clay-dark);
        margin: 0 auto;
        position: relative;
        bottom: 10px; /* Sit just above the wheel */
        transition: all 0.5s ease-in-out, background-color 0.3s ease; /* Smooth transitions */
        box-shadow: 0 5px 10px rgba(0,0,0,0.2);
        display: flex; /* Allow centering content inside */
        justify-content: center;
        align-items: center;
        color: white;
        font-weight: bold;
        font-size: 1.2em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    
    .stage-clay-prep .clay-mass {
        width: 140px;
        height: 100px;
        border-radius: 50%; /* Gump of clay */
        bottom: 5px;
         content: 'חימר'; /* Placeholder text */
    }

    .stage-shaping .clay-mass {
        width: 100px;
        height: 150px; /* Shaping into a taller form */
        border-radius: 10% 10% 5% 5%;
        background-color: var(--clay-medium);
         animation: rotate 0.5s infinite linear; /* Basic wheel rotation */
         box-shadow: 0 5px 10px rgba(0,0,0,0.3), inset 0 0 15px rgba(0,0,0,0.3); /* More depth */
         content: 'מעצבים';
    }

     .stage-drying .clay-mass {
        width: 100px;
        height: 150px;
        border-radius: 10% 10% 5% 5%;
        background-color: var(--clay-light);
        opacity: 0.9; /* Indicates slight dryness/opacity change */
         content: 'מתייבש';
    }

     .stage-bisque .clay-mass {
        width: 100px;
        height: 150px;
        border-radius: 10% 10% 5% 5%;
        background-color: var(--bisque-color);
        opacity: 1; /* Solid after firing */
         box-shadow: 0 5px 10px rgba(0,0,0,0.2); /* Lighter shadow for lighter color */
         content: 'ביסק';
         color: var(--text-color);
    }

     .stage-glazing .clay-mass {
        width: 100px;
        height: 150px;
        border-radius: 10% 10% 5% 5%;
        background-color: var(--bisque-color); /* Still bisque underneath */
        position: relative;
         content: 'מזגגים';
         color: var(--text-color);
    }

     /* Visual representation of glaze application - will be handled by JS adding classes */
     .clay-mass::before {
         content: attr(data-stage-text); /* Use data attribute for text */
         position: absolute;
         top: 50%;
         left: 50%;
         transform: translate(-50%, -50%);
         white-space: nowrap;
     }

     .stage-glaze-fire .clay-mass {
        width: 100px;
        height: 150px;
        border-radius: 10% 10% 5% 5%;
        background-color: var(--accent-color); /* Example final fired color */
        /* Glaze appearance added via JS/class */
        box-shadow: 0 5px 15px rgba(0,0,0,0.4); /* More pronounced shadow */
        border: 1px solid rgba(0,0,0,0.2); /* Subtle border */
         content: 'מוכן!';
         color: white;
    }


    .pottery-wheel {
        width: 200px; /* Wider wheel */
        height: 40px; /* Taller wheel */
        background: linear-gradient(to bottom, #444, #222); /* Darker gradient */
        border-radius: 50%;
        margin: 15px auto 0;
        box-shadow: inset 0 5px 10px rgba(0,0,0,0.5), 0 2px 5px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1; /* Ensure wheel is visually below clay edge */
        transform-origin: center;
        transition: transform 0.1s linear; /* Smooth transition for speed change */
    }

    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    .stage-shaping .pottery-wheel, .stage-glazing .pottery-wheel {
         /* Animation controlled by JS */
    }


    /* Controls and Feedback Styling */
    .simulator-area > .controls,
    .simulator-area > .feedback-area {
        flex: 1; /* Equal flex distribution on larger screens */
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 20px;
        background-color: #fff;
        box-shadow: 0 2px 8px var(--shadow-color);
    }


     .controls h2, .feedback-area h2 {
        color: var(--accent-color);
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.5em;
         text-align: center;
    }

    .controls button {
        display: block;
        width: 100%;
        margin-bottom: 12px;
        padding: 12px 15px;
        cursor: pointer;
        background-color: var(--accent-color);
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .controls button:hover:not(:disabled) {
        background-color: #8b4513; /* Slightly darker accent */
        transform: translateY(-2px);
    }

     .controls button:disabled {
         background-color: #ccc;
         cursor: not-allowed;
         opacity: 0.7;
     }

    .tool-controls, .glazing-controls {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px dashed var(--border-color);
    }
    .tool-controls h3, .glazing-controls h3 {
        color: var(--text-color);
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.2em;
         text-align: center;
    }

    .tool-controls button, .glazing-controls button {
        width: auto; /* Allow buttons to size to content */
        display: inline-block; /* Arrange in a row */
        margin: 0 5px 10px 5px;
        padding: 8px 15px;
        background-color: #eee;
        color: var(--text-color);
        border: 1px solid var(--border-color);
        font-size: 1em;
    }
     .tool-controls button:hover, .glazing-controls button:hover {
         background-color: #ddd;
         transform: translateY(-1px);
     }

     .control-group {
         margin-top: 15px;
         text-align: center;
     }
     .control-group label {
         display: block;
         margin-bottom: 5px;
         font-weight: bold;
     }
     .slider {
         width: 80%;
         -webkit-appearance: none;
         appearance: none;
         height: 8px;
         background: var(--border-color);
         outline: none;
         opacity: 0.7;
         transition: opacity .2s;
         border-radius: 4px;
     }
     .slider:hover {
         opacity: 1;
     }
     .slider::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px;
         height: 20px;
         background: var(--accent-color);
         cursor: pointer;
         border-radius: 50%;
         box-shadow: 0 2px 5px var(--shadow-color);
     }
      .slider::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: var(--accent-color);
         cursor: pointer;
         border-radius: 50%;
         box-shadow: 0 2px 5px var(--shadow-color);
     }


    .feedback-area {
        min-height: 200px; /* Ensure feedback area is visible */
        display: flex;
        flex-direction: column;
    }

    #current-feedback {
        flex-grow: 1; /* Push feedback text down */
        margin-top: 0;
        font-size: 1.2em;
        text-align: center;
        color: #555; /* Slightly muted text */
    }

    .toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        cursor: pointer;
        background-color: var(--text-color);
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 2px 5px var(--shadow-color);
    }
     .toggle-button:hover {
         background-color: #555;
         transform: translateY(-2px);
     }

    #full-explanation {
        margin-top: 20px;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #fff;
        box-shadow: 0 2px 8px var(--shadow-color);
        max-width: 900px;
        margin: 20px auto;
    }

    #full-explanation h2 {
        color: var(--accent-color);
        margin-top: 0;
        margin-bottom: 20px;
         font-size: 1.8em;
    }
     #full-explanation h3 {
        color: var(--text-color);
        margin-top: 1.5em;
        margin-bottom: 0.8em;
        font-size: 1.3em;
        border-bottom: 1px dashed var(--border-color);
        padding-bottom: 5px;
    }

    #full-explanation p, #full-explanation ul {
        line-height: 1.7;
        margin-bottom: 1em;
        color: #555;
    }

    #full-explanation ul {
        padding-left: 25px;
    }
     #full-explanation li {
        margin-bottom: 0.7em;
    }

     /* Glaze Visualizations (CSS classes added by JS) */
     .clay-mass.glazed-blue-glossy {
         background-color: var(--glaze-blue);
         box-shadow: inset 0 0 15px rgba(0,0,139,0.8); /* Deep blue glow */
         border: 2px solid var(--glaze-blue);
         content: ''; /* Remove text */
     }
      .clay-mass.glazed-white-matte {
         background-color: var(--glaze-white);
         box-shadow: inset 0 0 10px rgba(192,192,192,0.5); /* Subtle grey shadow */
         border: 2px solid var(--glaze-white);
          content: ''; /* Remove text */
     }
       .clay-mass.glazed-clear-satin {
         /* Keep bisque color or base color */
         box-shadow: inset 0 0 10px rgba(0,0,0,0.2), 0 0 15px rgba(0,0,0,0.1) ; /* Add a subtle shine/depth */
         border: 2px solid rgba(0,0,0,0.1);
           content: ''; /* Remove text */
      }


</style>

<script>
    const potteryStage = document.getElementById('pottery-stage');
    const simulationControls = document.getElementById('simulation-controls');
    const feedbackArea = document.getElementById('current-feedback');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const fullExplanationDiv = document.getElementById('full-explanation');
    const shapingTools = document.getElementById('shaping-tools');
    const glazingOptions = document.getElementById('glazing-options');
    const wheelSpeedSlider = document.getElementById('wheel-speed');
    const saveButton = document.getElementById('save-btn');
    const stageButtons = simulationControls.querySelectorAll('button[data-stage]');
    const clayMass = document.querySelector('.clay-mass'); // Select the clay element
    const potteryWheel = document.querySelector('.pottery-wheel'); // Select the wheel element

    let currentStage = 'clay-prep';
    let selectedGlaze = null; // Track selected glaze
    let wheelAnimation = null; // Store wheel animation instance
    let currentWheelSpeed = 100; // Store current wheel speed

    const stageDescriptions = {
        'clay-prep': { text: 'מוכנים להתחיל? בחרו את השלב הראשון במסע הקדרות שלכם!', stageText: 'חימר' },
        'shaping': { text: 'מפסלים ביד אמן! מעצבים את הכלי על האובניים. נסו כלים שונים!', stageText: 'מעצבים' },
        'drying': { text: 'הכלי מתייבש באוויר לשלב ה"עור". עכשיו ניתן לגלף או להוסיף לו אלמנטים.', stageText: 'מתייבש' },
        'bisque': { text: 'הכלי עבר שרפה ראשונה בתנור (ביסק)! הוא קשיח ומוכן לזיגוג.', stageText: 'ביסק' },
        'glazing': { text: 'שלב הזיגוג המרהיב! בחרו את הזיגוג שיעניק לכלי שלכם צבע וברק.', stageText: 'מזגגים' },
        'glaze-fire': { text: 'שרפת הגלייז הסופית הסתיימה! הזיגוג נמס והתמצק לגימור זכוכיתי. יצירתכם מוכנה!', stageText: 'מוכן!' }
    };

     // Define the flow logic: which stage can follow which
     const stageFlow = {
         'clay-prep': 'shaping',
         'shaping': 'drying',
         'drying': 'bisque',
         'bisque': 'glazing',
         'glazing': 'glaze-fire',
         'glaze-fire': null // End of process
     };

    function updateSimulation(stage) {
        // Disable current stage button after advancing
        const currentStageButton = simulationControls.querySelector(`button[data-stage="${currentStage}"]`);
        if (currentStageButton) {
             // currentStageButton.disabled = true; // Maybe better to just enable the *next* one
        }

        currentStage = stage;

        // Update stage visualization classes
        potteryStage.className = ''; // Clear existing classes
        potteryStage.classList.add('stage-' + stage);
        clayMass.classList.remove('glazed-blue-glossy', 'glazed-white-matte', 'glazed-clear-satin'); // Remove previous glaze classes

        // Update text content in clay mass
        clayMass.setAttribute('data-stage-text', stageDescriptions[stage].stageText);


        // Update feedback text
        feedbackArea.textContent = stageDescriptions[stage].text;

        // Show/hide specific controls based on stage
        shapingTools.style.display = stage === 'shaping' ? 'block' : 'none';
        glazingOptions.style.display = stage === 'glazing' ? 'block' : 'none';
        saveButton.style.display = stage === 'glaze-fire' ? 'block' : 'none';
        saveButton.disabled = stage !== 'glaze-fire'; // Only enable save button at the end

        // Manage stage button availability based on flow
        stageButtons.forEach(button => {
            button.disabled = true; // Disable all initially
        });
         let flowStage = 'clay-prep';
         while(flowStage && flowStage !== currentStage) {
             const btn = simulationControls.querySelector(`button[data-stage="${flowStage}"]`);
             if(btn) btn.disabled = true; // Keep previous stages disabled or mark them as 'done'
             flowStage = stageFlow[flowStage];
         }
         // Enable the current stage and the next one (if exists)
         const currentBtn = simulationControls.querySelector(`button[data-stage="${currentStage}"]`);
         if(currentBtn) {
             currentBtn.disabled = false; // Keep current stage button enabled
             // Maybe add a class to indicate current stage
             stageButtons.forEach(btn => btn.classList.remove('current-stage'));
             currentBtn.classList.add('current-stage');
         }
         const nextStage = stageFlow[currentStage];
         if(nextStage) {
             const nextBtn = simulationControls.querySelector(`button[data-stage="${nextStage}"]`);
             if(nextBtn) nextBtn.disabled = false;
         }


        // Handle wheel animation
        if (stage === 'shaping' || stage === 'glazing') {
             startWheelSpin(currentWheelSpeed);
        } else {
             stopWheelSpin();
        }

        console.log(`Changed to stage: ${stage}`);
    }

     function startWheelSpin(speed) {
         stopWheelSpin(); // Stop any existing animation first
         const duration = 200 / speed; // Faster speed = shorter duration
         potteryWheel.style.animation = `wheel-spin ${duration}s infinite linear`;
         clayMass.style.animation = `rotate ${duration}s infinite linear`;
     }

     function stopWheelSpin() {
         potteryWheel.style.animation = 'none';
         clayMass.style.animation = 'none';
     }


    // Event listeners for stage buttons
    stageButtons.forEach(button => {
        button.addEventListener('click', () => {
            if (!button.disabled) {
                 updateSimulation(button.dataset.stage);
            }
        });
    });

    // Event listeners for shaping tools (placeholder with feedback)
    shapingTools.querySelectorAll('button[data-tool]').forEach(button => {
        button.addEventListener('click', () => {
            feedbackArea.textContent = `מפסלים עם ה${button.textContent.toLowerCase()}. המשיכו לעצב!`;
             // Add a subtle visual effect on the clay mass temporarily
             clayMass.style.transition = 'none'; // Disable smooth transition for pulse
             clayMass.style.transform = 'scale(1.02)';
             setTimeout(() => {
                 clayMass.style.transform = 'scale(1)';
                  clayMass.style.transition = 'all 0.5s ease-in-out, background-color 0.3s ease'; // Re-enable transition
             }, 100);
        });
    });

    // Wheel speed slider
    wheelSpeedSlider.addEventListener('input', (event) => {
         currentWheelSpeed = event.target.value;
         feedbackArea.textContent = `מהירות אובניים: ${currentWheelSpeed}.`;
         if (currentStage === 'shaping' || currentStage === 'glazing') {
             startWheelSpin(currentWheelSpeed);
         }
    });

    // Event listeners for glazing options (placeholder with visual update)
    glazingOptions.querySelectorAll('button[data-glaze]').forEach(button => {
        button.addEventListener('click', () => {
            selectedGlaze = button.dataset.glaze;
            feedbackArea.textContent = `בחרתם בזיגוג: ${button.textContent}. דמיינו אותו על הכלי!`;
            // Apply temporary glaze class for visualization
            clayMass.classList.remove('glazed-blue-glossy', 'glazed-white-matte', 'glazed-clear-satin');
            clayMass.classList.add('glazed-' + selectedGlaze);
            clayMass.setAttribute('data-stage-text', ''); // Remove text when glazed
             // Add a subtle pulse or shine effect
             clayMass.style.transition = 'none';
             clayMass.style.boxShadow += ', 0 0 20px rgba(173, 216, 230, 0.5)'; // Example blue glow effect
             setTimeout(() => {
                  clayMass.style.transition = 'all 0.5s ease-in-out, background-color 0.3s ease';
                   clayMass.style.boxShadow = clayMass.style.boxShadow.replace(', 0 0 20px rgba(173, 216, 230, 0.5)', '');
             }, 300);
        });
    });

    // Save button (placeholder)
    saveButton.addEventListener('click', () => {
        feedbackArea.textContent = 'יצירתך המושלמת נשמרה (וירטואלית)! כל הכבוד על המסע המופלא!';
        // In a real app, this would trigger image export or final rendering
         saveButton.disabled = true; // Prevent saving multiple times
    });


    // Toggle explanation functionality
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = fullExplanationDiv.style.display === 'none';
        fullExplanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר תיאורטי מעמיק' : 'הצגת הסבר תיאורטי מעמיק';
         // Scroll to the explanation if showing it
         if (!isHidden) {
             fullExplanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    // Initialize the simulation display
    updateSimulation(currentStage);

</script>
```