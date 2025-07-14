---
title: "המסע הכחול: סימולטור אמנות יצירת הגבינה"
english_slug: blue-cheese-making-simulator
category: "מדעי המזון"
tags:
  - גבינה כחולה
  - יצירת גבינה
  - עובש אציל
  - מיקרואורגניזמים קסומים
  - הבשלת גבינה
---
<div id="cheese-simulator-container">
    <h1>המסע אל הוורידים הכחולים: סימולטור יצירת גבינה</h1>

    <p>כיצד מקבלת הגבינה הכחולה את אופייה המיוחד והוורידים המרהיבים שלה? בואו לצלול איתנו לתהליך קסום ואינטראקטיבי, ולגלות את הסודות המדעיים והמיקרוביאליים מאחורי אחת הגבינות המסתוריות והאהובות בעולם, כולל התפקיד המכריע של העובש האציל.</p>

    <div id="simulator-area">
        <div id="visual-display">
            <!-- States will be managed by JS/CSS opacity and position -->
            <div id="milk" class="state">
                 <div class="state-content">
                    <img src="https://via.placeholder.com/100x100?text=🥛" alt="חלב" class="state-icon">
                    <span class="state-label">חלב טרי</span>
                 </div>
            </div>
            <div id="curds" class="state">
                 <div class="state-content">
                     <img src="https://via.placeholder.com/100x100?text=🍮" alt="גבן ומי גבן" class="state-icon">
                     <span class="state-label">קרישת קסם: גבן ומי גבן</span>
                 </div>
            </div>
            <div id="cut-curds" class="state">
                 <div class="state-content">
                    <img src="https://via.placeholder.com/100x100?text=🔪" alt="גבן חתוך" class="state-icon">
                    <span class="state-label">הכנת הקוביות: חיתוך הגבן</span>
                 </div>
            </div>
            <div id="drained-curds" class="state">
                <div class="state-content">
                    <img src="https://via.placeholder.com/100x100?text=🧺" alt="גבן מנוקז" class="state-icon">
                    <span class="state-label">פרידה מנוזלים: גבן מנוקז</span>
                </div>
            </div>
            <div id="salted-cheese" class="state">
                 <div class="state-content">
                     <img src="https://via.placeholder.com/100x100?text=🧂" alt="גבינה מומלחת" class="state-icon">
                     <span class="state-label">נגיעת טעם: המלחה</span>
                 </div>
            </div>
            <div id="molded-cheese" class="state">
                 <div class="state-content">
                      <img src="https://via.placeholder.com/100x100?text=🍄" alt="הוספת עובש" class="state-icon">
                     <span class="state-label">הזרעת הקסם: הוספת עובש</span>
                 </div>
            </div>
            <div id="aging-cheese" class="state">
                <div id="cheese-block"></div>
                <div id="mold-growth"></div>
                 <div class="state-content aging-content">
                    <span class="state-label">הקסם קורה: הבשלה</span>
                 </div>
            </div>
            <div id="final-cheese" class="state">
                 <img src="https://via.placeholder.com/300x200?text=גבינה+כחולה+מוכנה!" alt="גבינה כחולה מוכנה" id="final-cheese-img">
            </div>
        </div>
        <div id="controls-area">
            <div id="step-text">לחץ על כפתור ההתחלה כדי לצאת למסע יצירת הגבינה הכחולה!</div>
            <button id="next-step-btn">התחל את המסע</button>

            <!-- Aging Controls (initially hidden) -->
            <div id="aging-controls">
                <h3>שלב ההבשלה: קסם הזמן והתנאים</h3>
                <p>כוונן את תנאי הסביבה כדי להשפיע על התפתחות העובש והטעמים:</p>
                <div class="control-group">
                    <label for="temp-slider">טמפרטורה (°C): <span id="temp-value">10</span></label>
                    <input type="range" id="temp-slider" min="5" max="15" value="10">
                </div>
                 <div class="control-group">
                    <label for="humidity-slider">לחות (%): <span id="humidity-value">90</span></label>
                    <input type="range" id="humidity-slider" min="85" max="95" value="90">
                </div>
                <button id="start-aging-btn">התחל הבשלה (1 "מחזור זמן")</button>
                <p id="aging-feedback" class="feedback"></p>
            </div>
        </div>
    </div>
</div>

<button id="toggle-explanation">הצג/הסתר את הסיפור המלא מאחורי הגבינה הכחולה</button>

<div id="explanation">
    <h2>הסיפור המלא: הסודות המרתקים מאחורי הגבינה הכחולה</h2>

    <section>
        <h3>מבוא: מהי גבינה כחולה ומה הופך אותה למיוחדת כל כך?</h3>
        <p>גבינה כחולה היא משפחה עשירה ומגוונת של גבינות בעלות אופי דרמטי. היא נוצרת מחלב בקר, כבשים או עזים, ומאופיינת בוורידים ירוקים-כחולים עזים המפוזרים בתוכה. ורידים אלו הם יצירתו של עובש אציל, לרוב מזן <em>Penicillium roqueforti</em>, והוא שמעניק לגבינה את טעמה העמוק, המלוח והמעט חריף, ואת ריחה האופייני והבלתי נשכח. הצטרפו אלינו למסע אל עולם המיקרואורגניזמים הנהדרים שיוצרים את הקסם הזה.</p>
    </section>

    <section>
        <h3>חומרי הגלם: בסיס הקסם</h3>
        <ul>
            <li><strong>חלב טרי:</strong> הבסיס לכל גבינה מצוינת. סוג החלב (בקר, כבשים, עזים) והרכבו (שומן, חלבון, לקטוז) ישפיעו דרמטית על הטעם והמרקם הסופיים. לרוב עובר החלב פסטור עדין כדי לשמור על חיידקים מועילים טבעיים ובו זמנית להגן מפני פתוגנים.</li>
            <li><strong>תרביות סטארטר (חיידקים מועילים):</strong> גיבורים זעירים שמתחילים את המסיבה! אלו לרוב חיידקי חומצת חלב שצורך מהלקטוז בחלב ומייצרים חומצה לקטית. ירידת ה-pH חיונית לקרישת החלב, לפיתוח טעמים ראשוניים, ולבלימת חיידקים לא רצויים בשלבים הראשונים.</li>
            <li><strong>אנזים הגבנה (רנט):</strong> המפתח שמפעיל את תהליך הקרישה. אנזים זה, שמקורו יכול להיות חי (מקיבת יונקים צעירים), צמחי או מיקרוביאלי, גורם לחלבון העיקרי בחלב, הקזאין, להתלכד וליצור רשת מוצקה – הגבן, תוך כדי שחרור הנוזל שנקרא מי גבן.</li>
            <li><strong>נבגי עובש אציל (Penicillium roqueforti):</strong> הנשמה הכחולה של הגבינה. אלו הם נבגי פטרייה מיוחדת שיש לה יכולת מדהימה לגדול בתנאים שמייבשים ומקשים על מיקרואורגניזמים אחרים לשרוד (סביבה חומצית ומלוחה יחסית).</li>
        </ul>
    </section>

    <section>
        <h3>שלבי היצירה הבסיסיים: המסע של החלב לגבן</h3>
        <p>יצירת גבינה כחולה מתחילה בתהליך דומה לגבינות רבות אחרות, אך עם תוספת קריטית אחת:</p>
        <ul>
            <li><strong>הכנת החלב והוספת הסטארטר:</strong> חימום עדין של החלב ולאחר מכן קירור לטמפרטורה המתאימה לפעילות חיידקי הסטארטר. החיידקים מתחילים לעבוד, מורידים את ה-pH ומכינים את הקרקע לקרישה.</li>
            <li><strong>הוספת הרנט וקרישת החלב:</strong> הוספת אנזים הגבנה גורמת לחלבון הקזאין להתקרש תוך 30-60 דקות, ויוצר מסה מוצקה ורכה - הגבן.</li>
            <li><strong>חיתוך הגבן וניקוז מי הגבן:</strong> הגבן המוצק נחתך לקוביות קטנות באמצעות סכינים מיוחדות או גידים. החיתוך מגדיל את שטח הפנים ומאפשר למי הגבן הנוזליים לצאת בקלות מהגבן. גודל הקוביות ישפיע על כמות הלחות שתישאר בגבינה הסופית.</li>
            <li><strong>ניקוז נוסף ועיצוב:</strong> הגבן החתוך מעורבב בעדינות ומועבר לתבניות. בשלב זה ממשיכים מי הגבן להתנקז באופן פסיבי מכוח הכבידה. הגבן מקבל את צורתו הסופית.</li>
            <li><strong>המלחה:</strong> המלח מוסף לגבן או לגבינה הצעירה. הוא לא רק מוסיף טעם חיוני, אלא גם עוזר להוציא לחות נוספת, בולם התפתחות חיידקים לא רצויים, ומהווה תנאי סביבה מועדפים עבור העובש הכחול.</li>
        </ul>
    </section>

    <section>
        <h3>התפקיד הראשי: העובש Penicillium roqueforti</h3>
        <p>זהו השלב בו הגבינה הכחולה מקבלת את זהותה הייחודית.</p>
        <ul>
            <li><strong>הוספת העובש:</strong> נבגי העובש מוספים לגבינה באחת מכמה דרכים: או שהם מעורבבים ישירות עם החלב בתחילת התהליך, או שהם מפוזרים על הגבן המנוקז לפני העיצוב, או (בטכניקה נפוצה לגבינות גדולות) שהם מוזרקים לגבינה הצעירה לאחר המלחתה באמצעות מחטים ארוכות. הזרקת הנבגים יוצרת "ערוצים" פנימיים שיאפשרו בהמשך כניסת חמצן לגוף הגבינה, חיוני להתפתחות העובש בפנים.</li>
            <li><strong>הפעלת העובש:</strong> הנבגים "מתעוררים לחיים" ומחלים לגדול כחוטי קור עדינים בתוך הגבינה, מוכנים לשלב הבא.</li>
        </ul>
    </section>

    <section>
        <h3>שלב ההבשלה: קסם הטרנספורמציה האיטית</h3>
        <p>זהו שיא המסע! חודשים ארוכים (ולפעמים אף יותר) במרתפים קרירים ולחים, בהם מתרחשים תהליכים ביוכימיים מורכבים וקסומים.</p>
        <ul>
            <li><strong>תנאי סביבה קסומים:</strong> ההבשלה מתרחשת בסביבה מבוקרת קפדנית: טמפרטורה נמוכה יחסית (5-15°C) ולחות גבוהה מאוד (85-95%). לעיתים קרובות, הגבינות מחוררות לאחר העיצוב וההמלחה. חירור זה יוצר את אותם "ערוצים" המאפשרים לחמצן לחדור לעומק הגבינה, שם יכול העובש האציל לשגשג ולהתפתח.</li>
            <li><strong>ריקוד האנזימים:</strong> העובש <em>Penicillium roqueforti</em> וגם חיידקי הסטארטר מייצרים אנזימים רבי עוצמה: פרוטאזות שמפרקות את החלבונים לחומצות אמינו ותרכובות קטנות יותר, וליפאזות שמפרקות את השומנים לחומצות שומן ותרכובות נדיפות.</li>
            <li><strong>פיתוח הטעם, הריח והמרקם:</strong> פירוק החלבונים (פרוטאוליזה) תורם לטעם אומאמי עשיר, לריכוך המרקם, ולייצור תרכובות המשפיעות על הריח. פירוק השומנים (ליפוליזה), בעיקר על ידי הליפאזות של העובש, מייצר תרכובות ארומטיות עוצמתיות כמו מתיל קטונים, האחראיות לריח ה"עובשי" האופייני ולטעם הפיקנטי-חריף של הגבינה הכחולה.</li>
            <li><strong>התגלות הוורידים הכחולים:</strong> העובש <em>Penicillium roqueforti</em> מייצר את הפיגמנט הכחול-ירוק האופייני רק בנוכחות חמצן. לכן, העובש מתפתח ויוצר את הוורידים המרהיבים בעיקר לאורך סדקים טבעיים בגבן או בתוך התעלות שנוצרו באמצעות החירור – בכל מקום אליו חודר האוויר.</li>
        </ul>
    </section>

     <section>
        <h3>בקרת איכות ואמנות הייצור</h3>
        <p>יצירת גבינה כחולה ברמה גבוהה דורשת מיומנות, ניטור קפדני של כל שלב, ובקרת תנאי סביבה מדויקים בשלב ההבשלה. טעויות בתהליך או תנאים לא מתאימים יכולים להוביל לפגמים כמו טעמי לוואי (מרירות, אמוניאק), מרקם לא אחיד, או התפתחות לא מספקת (או מוגזמת) של העובש הכחול. זהו שילוב אמיתי של מדע ואמנות.</p>
    </section>

     <section>
        <h3>גבינות כחולות מפורסמות מסביב לעולם</h3>
        <p>לכל גבינה כחולה סיפור משלה! המאפיינים הייחודיים של כל סוג נובעים משילוב של סוג החלב, שיטות הייצור הספציפיות לאזור (לעיתים עוברות מדור לדור), ותרביות העובש והחיידקים המקומיות. דוגמאות מפורסמות כוללות את הרוקפור (Roquefort) האלגנטית מחלב כבשים מצרפת, הגורגונזולה (Gorgonzola) הקרמית והאיטלקית מחלב בקר, הסטילטון (Stilton) האנגלית והעשירה, והדניש בלו (Danish Blue) הנגישה והפופולרית מדנמרק.</p>
    </section>
</div>

<style>
    /* General Body & Layout */
    body {
        font-family: 'Arial', sans-serif; /* Using a common font family */
        line-height: 1.6;
        background-color: #f8f4e6; /* Warm, creamy background */
        color: #333;
        direction: rtl; /* Hebrew support */
        text-align: right;
        padding: 20px;
    }

    h1, h2, h3 {
        color: #5a3e2b; /* Warm brown for headings */
        font-weight: bold;
        margin-top: 0;
    }

    h1 {
        text-align: center;
        margin-bottom: 20px;
        color: #0e4a5a; /* Deep blue-green */
    }

    p {
        margin-bottom: 15px;
    }

    #cheese-simulator-container {
        max-width: 800px;
        margin: 20px auto;
        background-color: #ffffff; /* Clean white for the simulator */
        border: 1px solid #dcdcdc;
        border-radius: 12px; /* More rounded corners */
        padding: 30px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Softer shadow */
    }

    #simulator-area {
        display: flex;
        flex-direction: column;
        gap: 25px;
        align-items: center;
    }

    /* Visual Display Area */
    #visual-display {
        position: relative;
        width: 100%;
        height: 220px; /* Slightly taller */
        border: 2px dashed #c0b2a0; /* Rustic dashed border */
        background-color: #edece0; /* Light parchment color */
        overflow: hidden;
        border-radius: 8px;
        display: flex; /* Use flex for centering state content */
        justify-content: center;
        align-items: center;
    }

    .state {
        position: absolute;
        width: 100%;
        height: 100%;
        display: flex; /* Use flex for centering content inside state */
        justify-content: center;
        align-items: center;
        transition: opacity 0.7s ease-in-out, transform 0.7s ease; /* Smooth transitions */
        opacity: 0; /* Hidden by default */
        pointer-events: none; /* Don't block clicks when hidden */
         background-size: cover;
         background-position: center;
         border-radius: 8px; /* Match container */
    }

    .state.active {
        opacity: 1; /* Active state is visible */
        pointer-events: auto; /* Allow interaction */
    }

    /* State Specific Styling - More evocative colors/textures */
    #milk { background-color: #fffacd; /* Lemon chiffon */ }
    #curds { background-color: #ffecb3; /* Light yellow */ }
    #cut-curds { background-color: #ffe082; /* Amber 200 */ }
    #drained-curds { background-color: #ffd54f; /* Amber 300 */ }
    #salted-cheese { background-color: #ffb300; /* Amber 600 */ }
    #molded-cheese {
         background-color: #ffa000; /* Amber 700 */
         /* Optional: Add subtle mold spots hint */
         background-image: radial-gradient(circle, rgba(14, 74, 90, 0.2) 10%, transparent 10%),
                           radial-gradient(circle, rgba(14, 74, 90, 0.15) 15%, transparent 15%);
        background-size: 20px 20px, 30px 30px;
        background-position: 0 0, 10px 10px;
         background-repeat: repeat;
    }


    /* Content within states (icon + label) */
    .state-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        color: #333;
        text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.8); /* White shadow for readability */
        font-weight: bold;
        font-size: 1.3em;
        z-index: 2; /* Above background layers */
    }

    .state-icon {
        width: 80px; /* Icon size */
        height: 80px;
        margin-bottom: 10px;
        border-radius: 50%; /* Make icons round placeholders */
        background-color: rgba(255, 255, 255, 0.7); /* Semi-transparent white background for icons */
        padding: 10px;
    }

     /* Special styling for aging state */
    #aging-cheese {
        background-color: #e0e0e0; /* Base cheese color for aging block */
        position: relative; /* Important for children positioning */
         opacity: 0; /* Starts hidden */
         pointer-events: none;
         /* Transition for aging state itself */
        transition: opacity 0.7s ease-in-out;
    }

     #aging-cheese.active {
         opacity: 1;
         pointer-events: auto;
     }

    #cheese-block {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: #e0e0e0; /* Base color */
        z-index: 0; /* Below mold */
        border-radius: 8px;
    }

    #mold-growth {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: none; /* Populated by JS */
        background-size: cover; /* Adjust as needed by JS */
        background-position: center;
        opacity: 1; /* Mold itself is opaque */
        z-index: 1; /* Above cheese block */
         border-radius: 8px;
    }

    .aging-content {
        /* Specific styling for text/icons during aging */
        color: #1a2e35; /* Darker text for contrast */
        text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.5);
    }


    #final-cheese {
         background-color: transparent; /* Container itself is transparent */
          opacity: 0; /* Starts hidden */
         pointer-events: none;
         /* Transition for final state itself */
        transition: opacity 0.7s ease-in-out;
    }
     #final-cheese.active {
         opacity: 1;
         pointer-events: auto;
     }

    #final-cheese-img {
         max-width: 90%; /* Ensure image fits */
         max-height: 90%;
         border: 4px solid #5a3e2b; /* Frame the final cheese */
         border-radius: 8px;
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }


    /* Controls Area */
    #controls-area {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
        width: 100%; /* Take full width */
        text-align: center;
    }

    #step-text {
        font-size: 1.2em;
        min-height: 2.5em; /* Reserve more space for text */
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-weight: bold;
        color: #0e4a5a; /* Deep blue-green */
    }

    button {
        padding: 12px 25px; /* More generous padding */
        font-size: 1.1em;
        cursor: pointer;
        background: linear-gradient(to bottom, #4CAF50, #45a049); /* Gradient green */
        color: white;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        transition: all 0.3s ease; /* Smooth transition for hover */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        font-weight: bold;
    }

    button:hover {
        background: linear-gradient(to bottom, #45a049, #39843c); /* Darker green on hover */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        transform: translateY(-2px); /* Lift button slightly */
    }

     #toggle-explanation {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        background: linear-gradient(to bottom, #007bff, #0056b3); /* Gradient blue */
        color: white;
        border: none;
        border-radius: 6px;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
         font-weight: bold;
    }

    #toggle-explanation:hover {
        background: linear-gradient(to bottom, #0056b3, #004085); /* Darker blue */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        transform: translateY(-2px);
    }


    /* Aging Controls */
    #aging-controls {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        padding: 20px;
        border: 2px dashed #c0b2a0;
        border-radius: 8px;
        background-color: #f0eadd; /* Lighter parchment */
        width: 90%;
        max-width: 400px; /* Limit width */
        margin-top: 15px;
         box-shadow: inset 0 1px 4px rgba(0,0,0,0.1);
         display: none; /* Hidden by default */
    }

    #aging-controls h3 {
        margin-top: 0;
        color: #5a3e2b;
         border-bottom: 1px solid #c0b2a0;
        padding-bottom: 5px;
        width: 100%;
        text-align: center;
    }

    #aging-controls p {
        text-align: center;
         font-size: 0.95em;
         color: #555;
    }

    .control-group {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: flex-end; /* Align labels right */
        gap: 5px;
    }


    #aging-controls label {
        font-weight: bold;
        color: #333;
        text-align: right;
        width: auto; /* Adjust width */
    }

     #aging-controls input[type="range"] {
         width: 100%;
         direction: ltr; /* Sliders are left-to-right controls */
         -webkit-appearance: none;
         appearance: none;
         height: 8px;
         background: #d3d3d3;
         outline: none;
         opacity: 0.7;
         -webkit-transition: .2s;
         transition: opacity .2s;
         border-radius: 4px;
     }

    #aging-controls input[type="range"]:hover {
         opacity: 1;
    }

    #aging-controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        background: #0e4a5a; /* Deep blue-green thumb */
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.4);
    }

    #aging-controls input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        background: #0e4a5a;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
         box-shadow: 0 1px 3px rgba(0,0,0,0.4);
    }

    #start-aging-btn {
         background: linear-gradient(to bottom, #8bc34a, #689f38); /* Greenish for aging */
         margin-top: 10px;
    }
     #start-aging-btn:hover {
         background: linear-gradient(to bottom, #689f38, #558b2f);
     }

     .feedback {
        min-height: 1.2em;
        font-size: 0.9em;
        color: #d32f2f; /* Red for feedback, adjust if needed */
        margin-top: 5px;
     }


    /* Explanation Section */
    #explanation {
        max-width: 800px;
        margin: 30px auto; /* More space */
        padding: 30px;
        border: 1px solid #dcdcdc;
        border-radius: 12px;
        background-color: #ffffff;
        direction: rtl;
        text-align: right;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
         display: none; /* Hidden by default */
    }

    #explanation h2 {
        color: #0e4a5a;
        border-bottom: 2px solid #c0b2a0; /* Rustic border */
        padding-bottom: 8px;
        margin-bottom: 20px;
         text-align: center;
    }

     #explanation h3 {
        color: #5a3e2b;
        border-bottom: 1px dashed #eee;
        padding-bottom: 4px;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    #explanation ul {
        padding-right: 25px; /* More padding for RTL list */
         margin-bottom: 15px;
    }

    #explanation li {
        margin-bottom: 12px;
        line-height: 1.5;
    }

    #explanation strong {
        color: #5a3e2b; /* Match headings */
    }

</style>

<script>
    const states = ['milk', 'curds', 'cut-curds', 'drained-curds', 'salted-cheese', 'molded-cheese', 'aging-cheese', 'final-cheese'];
    let currentStep = 0;

    const visualDisplay = document.getElementById('visual-display');
    const stepText = document.getElementById('step-text');
    const nextStepBtn = document.getElementById('next-step-btn');
    const agingControls = document.getElementById('aging-controls');
    const startAgingBtn = document.getElementById('start-aging-btn');
    const tempSlider = document.getElementById('temp-slider');
    const humiditySlider = document.getElementById('humidity-slider');
    const tempValueSpan = document.getElementById('temp-value');
    const humidityValueSpan = document.getElementById('humidity-value');
    const moldGrowthDiv = document.getElementById('mold-growth');
    const agingFeedback = document.getElementById('aging-feedback');

    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // More engaging state descriptions
     const stateDescriptions = [
        "לחץ על כפתור ההתחלה כדי לצאת למסע יצירת הגבינה הכחולה!", // Initial (state 0: milk)
        "שלב 1: מכינים את החלב ומוסיפים את הגיבורים הזעירים (סטארטר).", // After first click (state 1: curds)
        "שלב 2: הרנט מצטרף והחלב מתחיל להתגבש לקריש גבן קסום.", // After second click (state 2: cut-curds)
        "שלב 3: חותכים את קריש הגבן לקוביות קטנות לשחרור מי גבן.", // After third click (state 3: drained-curds)
        "שלב 4: מניחים לגבן להתנקז ולהתגבש לצורתו הצעירה.", // After fourth click (state 4: salted-cheese)
        "שלב 5: מוסיפים מלח לטעם, שימור, וסיוע בהמשך הדרך.", // After fifth click (state 5: molded-cheese)
        "שלב 6: מזרעים את הגבינה הצעירה בנבגי העובש האציל Penicillium roqueforti.", // After sixth click (state 6: aging-cheese setup)
        "שלב 7: הגבינה נחה במרתף ההבשלה. הזמן, הטמפרטורה והלחות יעשו את שלהם!", // After aging simulation (state 7: final-cheese)
     ];


    function updateSimulator(stepIndex) {
        // Hide all states visually and pointer-events
        states.forEach((stateId) => {
            const stateElement = document.getElementById(stateId);
            stateElement.classList.remove('active');
             stateElement.style.opacity = 0;
             stateElement.style.pointerEvents = 'none';
        });

        // Show the active state with transition
        const activeStateElement = document.getElementById(states[stepIndex]);
        activeStateElement.classList.add('active');
        // Set display block briefly to allow transition from opacity 0
         activeStateElement.style.display = 'flex'; // or 'block' depending on internal layout
         // RequestAnimationFrame helps ensure the display change is processed before opacity change
         requestAnimationFrame(() => {
             activeStateElement.style.opacity = 1;
             activeStateElement.style.pointerEvents = 'auto';
         });


        // Update step description
         stepText.textContent = stateDescriptions[stepIndex];


        // Handle button visibility and text, and control areas
        nextStepBtn.style.display = 'block';
        agingControls.style.display = 'none'; // Hide aging controls by default
        agingFeedback.textContent = ''; // Clear feedback
        nextStepBtn.textContent = "המשך לתהליך הבא";
        nextStepBtn.onclick = handleNextStep; // Reset to default handler

        // Specific state adjustments
        if (states[stepIndex] === 'milk') {
             stepText.textContent = stateDescriptions[0]; // Initial text
             nextStepBtn.textContent = "התחל את המסע";
        } else if (states[stepIndex] === 'molded-cheese') {
             nextStepBtn.textContent = "הכנה לשלב ההבשלה";
             stepText.textContent = stateDescriptions[5];
        }
        else if (states[stepIndex] === 'aging-cheese') {
            nextStepBtn.style.display = 'none'; // Hide next step button during aging setup
            agingControls.style.display = 'flex'; // Show aging controls
            stepText.textContent = stateDescriptions[6]; // Aging description

             // Reset mold growth visual for the start of aging
            moldGrowthDiv.style.backgroundImage = 'none';
            moldGrowthDiv.style.opacity = 1; // Mold layer is opaque when active

        } else if (states[stepIndex] === 'final-cheese') {
            nextStepBtn.style.display = 'none'; // Hide at the end
            agingControls.style.display = 'none'; // Ensure hidden at the end
            stepText.textContent = stateDescriptions[7]; // Final description
        }
    }

    function simulateAging() {
        const temp = parseInt(tempSlider.value, 10);
        const humidity = parseInt(humiditySlider.value, 10);

        // Simple simulation logic for visual effect:
        // Higher temp and humidity lead to more visible/intense mold growth
        // Let's scale factors from 0 to 1 based on the slider ranges
        const tempFactor = (temp - 5) / (15 - 5); // Scale 5-15 to 0-1
        const humidityFactor = (humidity - 85) / (95 - 85); // Scale 85-95 to 0-1

        // Combined factor influencing intensity and coverage
        const growthIntensity = (tempFactor + humidityFactor) / 2; // Simple average
        const scaledIntensity = Math.min(Math.max(growthIntensity, 0.2), 1); // Ensure min growth visible, cap at 1


        let veins = '';
        const numVeins = Math.floor(7 + scaledIntensity * 25); // More veins with higher intensity
        const baseColor = `rgba(14, 74, 90, ${0.4 + scaledIntensity * 0.5})`; // Darker/more opaque blue-green

        // Generate a pattern of blue "veins" using multiple linear gradients
        for(let i = 0; i < numVeins; i++) {
            const angle = Math.random() * 360;
            // Vary size and spread based on intensity
            const size = 1 + scaledIntensity * 3; // Thicker veins with intensity
            const spread = 40 + scaledIntensity * 60; // Longer veins with intensity

             veins += `linear-gradient(${angle}deg, transparent 0%, transparent ${spread - size*0.8}%, ${baseColor} ${spread}%, transparent ${spread + size*0.8}%, transparent 100%),`;
        }

        // Add some patchy mold growth using radial gradients
        const numPatches = Math.floor(3 + scaledIntensity * 10);
         const patchColor = `rgba(24, 104, 120, ${0.3 + scaledIntensity * 0.4})`; // Slightly lighter blue-green
        for(let i = 0; i < numPatches; i++) {
            const x = Math.random() * 100;
            const y = Math.random() * 100;
            const radius = 10 + scaledIntensity * 30; // Larger patches with intensity
             veins += `radial-gradient(circle at ${x}% ${y}%, ${patchColor} 0%, transparent ${radius}%),`;
        }


        // Remove trailing comma
        veins = veins.slice(0, -1);

        moldGrowthDiv.style.backgroundImage = veins;
        // You could also adjust moldGrowthDiv.style.opacity here if needed, but 1 is fine over the cheese block

        // Provide feedback based on conditions (simplified)
        if (scaledIntensity > 0.8) {
            agingFeedback.textContent = "תנאים מצוינים! העובש שגשג בהצלחה ויצר ורידים עשירים.";
            agingFeedback.style.color = '#388e3c'; // Green for success
        } else if (scaledIntensity < 0.4) {
             agingFeedback.textContent = "התנאים לא היו אידיאליים. התפתחות העובש חלשה יותר.";
             agingFeedback.style.color = '#fbc02d'; // Yellow/Orange for warning
        } else {
             agingFeedback.textContent = "ההבשלה התקדמה היטב.";
             agingFeedback.style.color = '#1976d2'; // Blue for standard
        }


        // After one "aging tick", allow moving to the final step
        nextStepBtn.style.display = 'block';
        nextStepBtn.textContent = "סיום הבשלה (הגבינה מוכנה!)";
        nextStepBtn.onclick = () => {
            // Move from aging state (index 6) to final state (index 7)
            currentStep = states.indexOf('final-cheese');
            updateSimulator(currentStep);
            // Note: No further steps after final, so no need to reset handler.
        };
    }


    function handleNextStep() {
        // Prevent moving forward from the final state
        if (currentStep >= states.length - 1) {
            return;
        }

        // Special handling: If currently at the molded-cheese state (index 5),
        // the *next* step is the aging-cheese state setup (index 6).
        if (states[currentStep] === 'molded-cheese') {
             currentStep++; // Move to aging setup state
             updateSimulator(currentStep);
        } else {
            // For all other states, just increment and update
            currentStep++;
             updateSimulator(currentStep);
        }
    }

    // Initial state setup
    updateSimulator(currentStep);

    // Event Listeners
    // nextStepBtn listener is set/reset within updateSimulator and simulateAging

    tempSlider.addEventListener('input', (event) => {
        tempValueSpan.textContent = event.target.value;
         // Optional: Live update of aging feedback or visual hint while adjusting sliders?
         // For simplicity, let's keep simulation only on button click.
    });

    humiditySlider.addEventListener('input', (event) => {
        humidityValueSpan.textContent = event.target.value;
        // Optional: Live update?
    });

    startAgingBtn.addEventListener('click', simulateAging);

     toggleExplanationBtn.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
            toggleExplanationBtn.textContent = 'הסתר את הסיפור המלא';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationBtn.textContent = 'הצג את הסיפור המלא מאחורי הגבינה הכחולה';
        }
    });

    // Add initial button click listener
    nextStepBtn.addEventListener('click', handleNextStep);


</script>
```