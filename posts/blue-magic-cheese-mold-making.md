---
title: "הקסם הכחול: מסע מופלא אל לב גבינות העובש"
english_slug: blue-magic-cheese-mold-making
category: "ביולוגיה"
tags:
- גבינה
- עובש
- מיקרוביולוגיה
- התססה
- מדעי המזון
- סימולציה
- אינטראקטיבי
---
<div class="simulation-container">
    <h1>הקסם הכחול: מסע מופלא אל לב גבינות העובש</h1>
    <p>איך חתיכת גבינה לבנה תמימה הופכת, כבמטה קסם, למעדן פיקנטי מלא בעורקים כחולים עשירים? הסוד טמון לא רק בחלב המשובח ובחיידקים החרוצים, אלא בשחקן זעיר ובלתי צפוי שמשנה את כללי המשחק: עובש!</p>

    <div id="cheese-making-simulation" class="interactive-simulation">
        <h2>הסימולטור הקסום לייצור גבינה כחולה</h2>
        <div id="simulation-area" class="simulation-stages">
            <div id="stage-milk" class="stage active">
                <h3>שלב 1: הנוזל הלבן והזמנת החיידקים</h3>
                <p>התחילו את המסע. בחרו סוג חלב איכותי והוסיפו את מחמצות החיידקים שיחלו את תהליך הגיבון.</p>
                <div class="visual-area milk-visual">
                    <div class="milk-liquid"></div>
                    <div class="milk-vat-outline"></div>
                     <div class="cultures-add-point"></div>
                </div>
                <select id="milk-type" aria-label="בחירת סוג חלב">
                    <option value="cow">חלב בקר</option>
                    <option value="sheep">חלב צאן</option>
                </select>
                <button id="add-cultures" class="action-button">הוסף את צוות החיידקים!</button>
                <div class="status-message" aria-live="polite">בחר חלב והוסף מחמצות כדי להמשיך.</div>
            </div>

            <div id="stage-curd" class="stage">
                 <h3>שלב 2: קסם הגיבון והאורח המיוחד</h3>
                 <p>החלב מתחיל להתגבן ולהפוך למוצק. עכשיו הרגע הקריטי: בואו נפגוש את האורח הראשי שלנו - עובש ה-Penicillium roqueforti!</p>
                 <div class="visual-area curd-visual">
                      <div class="curd-block"></div>
                      <div class="mold-sprinkle-point"></div>
                 </div>
                 <button id="add-mold" class="action-button">פזר את אבקת העובש (Penicillium roqueforti)</button>
                 <div class="status-message" aria-live="polite">הוסף עובש כדי להבטיח את הצבע הכחול.</div>
            </div>

            <div id="stage-cut-drain" class="stage">
                <h3>שלב 3: פיצוח המוצק ושחרור הנוזלים</h3>
                <p>אנחנו חותכים את גוש הגבן בעדינות. הפעולה הזו מאפשרת למי הגבן המיותרים להתנקז ולהיפרד מהמוצק.</p>
                 <div class="visual-area cut-curd-visual">
                      <div class="curd-cut-grid"></div>
                 </div>
                 <div class="status-message" aria-live="polite">הגבן נחתך. המים מתנקזים...</div>
                 <button id="simulate-cut" class="action-button">חתוך את הגבן</button>
            </div>

            <div id="stage-mold-salt" class="stage">
                 <h3>שלב 4: בית חדש ונגיעת מלח קסומה</h3>
                 <p>הגבן המנוקז עובר לתבניות עגולות כדי לקבל את צורתו הסופית. כעת נוסיף מלח - לשמירה, לטעם ולעזרה בניקוז נוסף.</p>
                 <div class="visual-area molded-cheese-visual">
                      <div class="cheese-shape-initial"></div>
                 </div>
                  <div class="status-message" aria-live="polite">הגבן עבר לתבניות ועבר המלחה.</div>
                  <button id="simulate-mold-salt" class="action-button">העבר לתבניות והמלחה</button>
            </div>

            <div id="stage-needle" class="stage">
                <h3>שלב 5: המהלך הגאוני! הניקוב!</h3>
                <p>כאן הסוד הגדול של הגבינות הכחולות. נקבו את הגבינה שוב ושוב בעזרת הכלי הווירטואלי כדי ליצור תעלות אוויר חיוניות לעובש!</p>
                <div class="visual-area cheese-wheel-to-needle" tabindex="0" aria-label="לחץ על הגבינה לנקב">
                    <div class="cheese-base"></div>
                    <div class="needle-visual"></div>
                </div>
                <button id="finish-needling" class="action-button" style="display: none;">סיימתי לנקב, קדימה להבשלה!</button>
                 <div class="status-message" aria-live="polite">לחץ על הגבינה כדי לנקב! לפחות <span id="min-needles-count"></span> נקבים נדרשים.</div>
            </div>

            <div id="stage-ripening" class="stage">
                <h3>שלב 6: מסע ההבשלה והתפרצות הכחול!</h3>
                <p>הגבינה נחה בתנאים מבוקרים. צפה כיצד העובש הכחול, שקיבל גישה לחמצן דרך הנקבים, מתעורר לחיים ויוצר את הוורידים האייקונים!</p>
                <div class="visual-area ripening-visual">
                     <div class="cheese-base"></div>
                     <div class="mold-growth-area"></div>
                </div>
                 <div class="status-message" aria-live="polite">לחץ על "התחל הבשלה" כדי לראות את קסם התפתחות העובש.</div>
                <button id="start-ripening" class="action-button">התחל הבשלה מואצת!</button>
            </div>

             <div id="stage-finished" class="stage">
                <h3>ניצחון כחול! הגבינה מוכנה לטעימה!</h3>
                <p>התהליך המופלא הושלם בהצלחה! הגבינה הכחולה שלכם מוכנה להרשים בטעם ובמראה הייחודיים שלה.</p>
                <div class="visual-area finished-cheese-visual">
                     <div class="cheese-base"></div>
                     <div class="final-mold-display"></div>
                </div>
                 <div class="status-message" aria-live="polite">תהליך ייצור הגבינה הכחולה הושלם.</div>
                 <button id="reset-simulation" class="action-button">בנה גבינה כחולה נוספת!</button>
            </div>

        </div>
         <button id="next-step" class="navigate-button">קדימה לשלב הבא</button>
    </div>

    <button id="toggle-explanation" class="toggle-button" aria-expanded="false" aria-controls="explanation-section">הצג איך עשינו את זה? (הסבר מדעי)</button>

    <div id="explanation-section" class="explanation-section" style="display: none;" aria-hidden="true">
        <h2>הסבר מעמיק: מאחורי הקסם הכחול</h2>
        <p>גבינות כחולות אינן סתם גבינות, הן יצירות אמנות מיקרוביולוגיות! עורקי הצבע הכחולים-ירוקים המרהיבים, הטעם הפיקנטי המורכב והריח האופייני – כולם תוצר של פעילות משולבת של חיידקים, אנזימים ובעיקר זני עובש מיוחדים מהסוג <em>Penicillium roqueforti</em>.</p>

        <h3>הבסיס: מסע הגיבון</h3>
        <p>כמו רוב הגבינות, הכל מתחיל בחלב איכותי. אנו מוסיפים לו "מחמצות" – תרביות חיידקים מועילות. חיידקים אלו מפרקים את סוכר החלב (לקטוז) ומייצרים חומצה לקטית, שמורידה את רמת ה-pH של החלב. ירידה זו גורמת לחלבון העיקרי בחלב, הקזאין, להתגבן ולהתאחד ליצירת גוש רך שנקרא "גבן". לאחר הגיבון, הגבן נחתך לקוביות קטנות כדי להקל על ניקוז הנוזלים (מי הגבן) מהמוצק. לאחר מכן, הגבן מועבר לתבניות לעיצוב סופי ולניקוז נוסף, ולבסוף מומלח - המלח משפר את הטעם, מסייע בשימור ומעודד ניקוז נוזלים נוסף.</p>

        <h3>השחקן הסודי: עובש ה-Penicillium roqueforti</h3>
        <p>חשוב להבין: העובש שנמצא בגבינות כחולות הוא זן מיוחד ומבוית, השונה לחלוטין מהעובש שעלול לגדול על מזון מקולקל. זני ה-<em>Penicillium roqueforti</em> בטוחים לחלוטין למאכל ואינם מייצרים רעלנים מזיקים בסביבת הגבינה. תרביות של עובש זה מוספות בדרך כלל בשלב מוקדם של הייצור – לעיתים ישירות לחלב, ולעיתים מעורבבות עם הגבן החתוך לפני הכניסה לתבניות. פיזור מוקדם זה מבטיח שהנבגים יהיו נוכחים בכל רחבי הגבינה הפוטנציאלית.</p>

        <h3>מדוע הניקוב הוא מהלך גאוני?</h3>
        <p>גוף הגבינה לאחר הכניסה לתבניות וההמלחה הוא צפוף ואטום יחסית. עובש ה-<em>Penicillium roqueforti</em>, בדומה לרוב האורגניזמים החיים, הוא אירובי – הוא זקוק לחמצן כדי לנשום, לצמוח ולהתפתח ביעילות. בתוך הגבן הדחוס יש מעט מאוד כיסי אוויר. כאן נכנס לתמונה הניקוב! באמצעות מוטות דקים וארוכים (בסימולציה - הקליקים שלכם!), יוצרים תעלות אוויר שמחברות את פני שטח הגבינה אל ליבתה הפנימית. החמצן חודר דרך התעלות הללו ומגיע אל נבגי העובש שהיו רדומים בפנים.</p>

        <h3>התפרצות הצבע והטעם בהבשלה</h3>
        <p>שלב ההבשלה, הנמשך שבועות או חודשים בתנאי טמפרטורה (8-12 מעלות צלזיוס) ולחות (מעל 90%) מבוקרים, הוא זמן הקסם. עם אספקת החמצן דרך תעלות הניקוב, נבגי העובש מתעוררים, נובטים ומתחילים לצמוח במהירות לאורך תעלות האוויר. צמיחה זו, המורכבת ממבנים דמויי חוטים (היפות), היא שיוצרת את המראה הוורידי הכחול-ירוק המפורסם. מעבר למראה, העובש מייצר אנזימים רבי עוצמה (כמו ליפאזות ופרוטאזות) שמפרקים את השומנים והחלבונים בגבן. פירוק זה משחרר מגוון רחב של תרכובות ארומטיות (אלדהידים, קטונים, חומצות שומן) האחראיות לטעם הפיקנטי, הייחודי והעשיר של הגבינה הכחולה, וגם תורם למרקם רך וקרמי יותר ככל שההבשלה מתקדמת. ללא הניקוב הנכון ואספקת החמצן, צמיחת העובש תהיה מוגבלת מאוד, ולא תתקבל הגבינה הכחולה האופיינית.</p>
    </div>
</div>

<style>
    /* Global Simulation Container */
    .simulation-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin-top: 20px;
        padding: 30px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: #fefefe;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        direction: rtl; /* RTL for Hebrew */
        text-align: right; /* Ensure text aligns right */
    }

    .simulation-container h1, .simulation-container h2, .simulation-container h3 {
        color: #0d47a1; /* Deep blue */
        margin-bottom: 15px;
        text-align: center; /* Center headings for better flow */
    }

     .simulation-container p {
         line-height: 1.7;
         margin-bottom: 15px;
         color: #333;
         text-align: right;
     }

    /* Simulation Area Styling */
    .interactive-simulation {
        margin-top: 25px;
        padding: 25px;
        border: 2px dashed #b0bec5; /* Light grey-blue dashed border */
        border-radius: 10px;
        background-color: #eceff1; /* Very light blue-grey */
        position: relative;
        overflow: hidden;
    }

     .simulation-stages {
         min-height: 350px; /* Give stages ample vertical space */
         margin-bottom: 20px;
         position: relative;
     }

    .stage {
        display: none;
        animation: fadeInScale 0.7s ease-in-out;
        width: 100%; /* Ensure stages take full width */
    }

    .stage.active {
        display: block;
    }

     @keyframes fadeInScale {
        from { opacity: 0; transform: scale(0.95); }
        to { opacity: 1; transform: scale(1); }
     }

    /* Buttons */
    .action-button, .navigate-button, .toggle-button {
        padding: 12px 20px;
        margin: 8px;
        background-color: #42a5f5; /* Medium blue */
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        font-weight: bold;
    }

    .action-button:hover, .navigate-button:hover, .toggle-button:hover {
        background-color: #2196f3; /* Darker blue on hover */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }

    .action-button:active, .navigate-button:active, .toggle-button:active {
        transform: scale(0.98);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }

     .action-button:disabled {
         background-color: #bbdefb; /* Lighter blue when disabled */
         cursor: not-allowed;
         box-shadow: none;
     }


    .navigate-button {
         background-color: #1e88e5; /* Slightly darker blue for navigation */
         margin-top: 20px;
    }

    .toggle-button {
         background-color: #7cb342; /* Green for toggle */
         margin-top: 20px;
    }

     .toggle-button:hover {
         background-color: #689f38; /* Darker green */
     }


    .status-message {
        margin-top: 20px;
        padding: 10px;
        background-color: #e1f5fe; /* Very light blue for info */
        border-left: 4px solid #29b6f6; /* Accent border */
        color: #01579b; /* Dark blue text */
        font-style: italic;
        min-height: 1.5em; /* Reserve space */
        text-align: center; /* Center status messages */
        border-radius: 4px;
        animation: pulseStatus 1.5s infinite alternate; /* Subtle pulse */
    }

    @keyframes pulseStatus {
        from { background-color: #e1f5fe; }
        to { background-color: #b3e5fc; }
    }


    /* Visual Elements Area */
    .visual-area {
        width: 220px; /* Increased size */
        height: 220px;
        margin: 30px auto;
        border: 2px solid #cfd8dc; /* Light grey border */
        border-radius: 15px; /* More rounded */
        background-color: #fff; /* White background */
        position: relative; /* For positioning children */
        overflow: hidden; /* Keep visual elements inside */
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
        display: flex; /* Use flexbox for internal centering/layout */
        justify-content: center; /* Center content */
        align-items: center; /* Center content */
    }

    /* Specific Stage Visuals */
    .milk-visual {
        background-color: #e0f7fa; /* Light cyan for milk vat */
        border-radius: 50%; /* Round like a vat */
        width: 250px; height: 250px; /* Larger vat */
         border-color: #b2ebf2;
    }
    .milk-vat-outline {
         position: absolute;
         width: 100%; height: 100%;
         border: 4px double #81d4fa; /* Double border for vat */
         border-radius: 50%;
         box-sizing: border-box;
    }
     .milk-liquid {
         position: absolute;
         width: 90%; height: 90%;
         background: linear-gradient(to bottom, #e1f5fe, #b3e5fc); /* Gradient fill */
         border-radius: 50%;
         animation: gentleWave 4s ease-in-out infinite alternate;
     }
     .cultures-add-point {
         position: absolute;
         top: 10%; left: 50%;
         width: 20px; height: 20px;
         background-color: #ff8a65; /* Orange dot */
         border-radius: 50%;
         transform: translate(-50%, -50%);
         opacity: 0;
         transition: opacity 0.5s ease;
     }
     .cultures-add-point.active {
         opacity: 1;
          animation: pulseDot 1s infinite;
     }
     @keyframes gentleWave {
         0% { transform: translateY(0); }
         100% { transform: translateY(5%); }
     }
     @keyframes pulseDot {
         0% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
         50% { transform: translate(-50%, -50%) scale(1.2); opacity: 0.7; }
         100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
     }


    .curd-visual {
        background-color: #ffecb3; /* Yellowish for curd block */
         border-color: #ffe082;
         width: 200px; height: 200px;
         border-radius: 8px; /* Block shape */
    }
     .curd-block {
         width: 90%; height: 90%;
         background: linear-gradient(to bottom right, #ffecb3, #ffcc80); /* Gradient */
         border-radius: 5px;
     }
     .mold-sprinkle-point {
          position: absolute;
          top: 20%; left: 50%;
          width: 30px; height: 30px;
          background-color: #a1887f; /* Brownish grey */
          border-radius: 50%;
          transform: translate(-50%, -50%);
          opacity: 0;
           transition: opacity 0.5s ease;
     }
      .mold-sprinkle-point.active {
          opacity: 1;
          animation: sprinkle 0.8s ease-out forwards;
      }
      @keyframes sprinkle {
           0% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
           100% { transform: translate(-50%, 50%) scale(0.5); opacity: 0; } /* Simulate falling */
      }


     .cut-curd-visual {
         background-color: #ffe082; /* Darker yellow */
         border-color: #ffb74d;
          width: 200px; height: 200px;
          border-radius: 8px;
          position: relative;
          overflow: hidden;
     }
      .curd-cut-grid {
          position: absolute;
          width: 100%; height: 100%;
          background-image: linear-gradient(0deg, transparent 50%, #ff9800 50%), linear-gradient(90deg, transparent 50%, #ff9800 50%);
          background-size: 25px 25px; /* Size of grid cells */
          opacity: 0;
          animation: showGrid 0.6s ease-out forwards;
      }
      @keyframes showGrid {
          0% { opacity: 0; transform: scale(0.8); }
          100% { opacity: 1; transform: scale(1); }
      }


      .molded-cheese-visual {
          background-color: #ffeb3b; /* More yellow */
          border-color: #ffca28;
          border-radius: 50%; /* Round cheese shape */
           width: 200px; height: 200px;
           position: relative;
      }
       .cheese-shape-initial {
            width: 90%; height: 90%;
            background: linear-gradient(to bottom, #fff9c4, #fff176); /* Soft yellow gradient */
            border-radius: 50%;
       }


    .cheese-wheel-to-needle, .ripening-visual, .finished-cheese-visual {
        width: 240px; /* Larger cheese wheel */
        height: 240px;
        background-color: #ffd54f; /* Cheese color */
        border-radius: 50%;
        cursor: crosshair; /* Indicate it's interactive */
        overflow: hidden; /* Hide mold outside the wheel */
        position: relative;
        border: 2px solid #ffc107; /* Amber border */
        box-shadow: 0 5px 10px rgba(0,0,0,0.1);
    }
    .cheese-base {
         width: 100%; height: 100%;
         background: radial-gradient(circle at 50% 50%, #ffecb3 0%, #ffd54f 60%, #ffc107 100%); /* Gradient */
         border-radius: 50%;
    }

    .needle-visual {
         position: absolute;
         width: 40px; /* Size of the needle icon/visual */
         height: 40px;
         top: 50%; left: 50%;
         transform: translate(-50%, -50%) scale(0);
         opacity: 0;
         transition: transform 0.3s ease-out, opacity 0.3s ease-out;
         /* Add needle icon/SVG or just a simple visual like a crosshair */
         border: 2px dashed #2196f3;
         border-radius: 50%;
         box-sizing: border-box;
         pointer-events: none; /* Don't block clicks */
    }
    .needle-hole {
        position: absolute;
        width: 6px; /* Slightly larger hole visual */
        height: 6px;
        background-color: #0d47a1; /* Dark blue dot */
        border-radius: 50%;
        pointer-events: none; /* Allow clicking through */
        transform: translate(-50%, -50%); /* Center dot on click */
        animation: holePop 0.3s ease-out; /* Animation on creation */
    }
    @keyframes holePop {
        0% { transform: translate(-50%, -50%) scale(0.5); opacity: 0.5; }
        100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
    }


     .mold-growth-area, .final-mold-display {
         position: absolute;
         top: 0; left: 0;
         width: 100%; height: 100%;
         border-radius: 50%;
         overflow: hidden;
         pointer-events: none;
         z-index: 1; /* Above cheese base */
     }


     .mold-line {
         position: absolute;
         background-color: #1a237e; /* Darker blue for mold */
         width: 0; /* Start with width 0 */
         height: 3px; /* Thickness */
         pointer-events: none;
         opacity: 0; /* Start hidden */
         transform-origin: 0 50%; /* Grow from the start point */
     }


    /* Explanation Styling */
    .explanation-section {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #b3e5fc; /* Light blue border */
        border-radius: 8px;
        background-color: #e1f5fe; /* Very light blue background */
        text-align: right; /* RTL */
        direction: rtl; /* RTL */
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
    }

    .explanation-section h2, .explanation-section h3 {
        color: #0d47a1; /* Dark blue heading */
        margin-bottom: 12px;
        text-align: right; /* Keep explanation headings right */
    }

    .explanation-section p {
        line-height: 1.7;
        margin-bottom: 15px;
        color: #263238; /* Dark grey text */
    }
</style>

<script>
    const simulationArea = document.getElementById('simulation-area');
    const stages = simulationArea.querySelectorAll('.stage');
    const nextButton = document.getElementById('next-step');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationSection = document.getElementById('explanation-section');

    // Stage specific elements
    const milkVisual = document.querySelector('#stage-milk .milk-visual');
    const culturesAddPoint = document.querySelector('#stage-milk .cultures-add-point');
    const addCulturesButton = document.getElementById('add-cultures');

    const curdVisual = document.querySelector('#stage-curd .curd-visual');
    const moldSprinklePoint = document.querySelector('#stage-curd .mold-sprinkle-point');
    const addMoldButton = document.getElementById('add-mold');

    const cutCurdVisual = document.querySelector('#stage-cut-drain .cut-curd-visual');
    const curdCutGrid = document.querySelector('#stage-cut-drain .curd-cut-grid');
    const simulateCutButton = document.getElementById('simulate-cut');

     const moldedCheeseVisual = document.querySelector('#stage-mold-salt .molded-cheese-visual');
     const simulateMoldSaltButton = document.getElementById('simulate-mold-salt');


    const needleCheeseVisual = document.querySelector('#stage-needle .cheese-wheel-to-needle');
    const needleVisual = document.querySelector('#stage-needle .needle-visual');
    const finishNeedlingButton = document.getElementById('finish-needling');
    const minNeedlesSpan = document.getElementById('min-needles-count');


    const ripeningVisual = document.querySelector('#stage-ripening .ripening-visual');
    const moldGrowthArea = document.querySelector('#stage-ripening .mold-growth-area');
    const startRipeningButton = document.getElementById('start-ripening');

    const finishedCheeseVisual = document.querySelector('#stage-finished .finished-cheese-visual');
     const finalMoldDisplay = document.querySelector('#stage-finished .final-mold-display');

    const resetButton = document.getElementById('reset-simulation');
    const statusMessage = simulationArea.querySelector('.status-message'); // Use a single status message element selector


    let currentStageIndex = 0;
    let moldAdded = false;
    let culturesAdded = false;
    let curdCut = false;
    let moldedAndSalted = false;
    let needlesCount = 0;
    const minNeedles = 15; // Increased minimum for more "gameplay"

    minNeedlesSpan.textContent = minNeedles; // Update the text in the HTML

    function updateStatus(message) {
        const currentStatusElement = stages[currentStageIndex].querySelector('.status-message');
         if (currentStatusElement) {
             currentStatusElement.textContent = message;
              currentStatusElement.classList.add('active'); // Add class for pulse animation
              setTimeout(() => currentStatusElement.classList.remove('active'), 1600); // Remove after pulse
         } else {
             console.warn("Status message element not found for current stage.");
         }
    }


    function showStage(index) {
        stages.forEach((stage, i) => {
            stage.classList.remove('active');
            if (i === index) {
                stage.classList.add('active');
                 stage.setAttribute('aria-hidden', 'false');
            } else {
                 stage.setAttribute('aria-hidden', 'true');
            }
        });

        // Reset buttons and visuals for the new stage
         nextButton.style.display = 'none'; // Hide next by default
         startRipeningButton.style.display = 'none';
         finishNeedlingButton.style.display = 'none';
         resetButton.style.display = 'none';
         addCulturesButton.style.display = 'none';
         addMoldButton.style.display = 'none';
         simulateCutButton.style.display = 'none';
         simulateMoldSaltButton.style.display = 'none';
         needleCheeseVisual.style.cursor = 'default'; // Reset cursor
         needleVisual.style.transform = 'translate(-50%, -50%) scale(0)'; // Hide needle visual


        // Configure stage based on index
        const currentStageId = stages[index].id;

        if (currentStageId === 'stage-milk') {
             addCulturesButton.style.display = 'inline-block';
             addCulturesButton.disabled = culturesAdded; // Disable if already done in this run
             updateStatus(culturesAdded ? 'מחמצות הוספו.' : 'בחר חלב והוסף מחמצות כדי להמשיך.');
              milkVisual.style.backgroundColor = '#e0f7fa'; // Ensure milk color
              milkVisual.querySelector('.milk-liquid').style.transform = 'translateY(0)'; // Reset animation

        } else if (currentStageId === 'stage-curd') {
            addMoldButton.style.display = 'inline-block';
            addMoldButton.disabled = moldAdded; // Disable if already done
            updateStatus(moldAdded ? 'עובש הוסף.' : 'החלב התגבן. הוסף את תרבית העובש.');
             curdVisual.style.backgroundColor = '#ffecb3'; // Ensure curd color
             curdVisual.querySelector('.curd-block').style.transform = 'scale(1)'; // Reset curd block state

             if (culturesAdded && !moldAdded) nextButton.style.display = 'inline-block'; // Allow skipping mold if wanted (will affect result)


        } else if (currentStageId === 'stage-cut-drain') {
             simulateCutButton.style.display = 'inline-block';
             simulateCutButton.disabled = curdCut;
             updateStatus(curdCut ? 'הגבן נחתך והמים מתנקזים.' : 'לחץ כדי לחתוך את הגבן ולהתחיל בניקוז.');
             curdCutGrid.style.opacity = 0; // Hide grid initially

             if ((culturesAdded || moldAdded) && !curdCut) nextButton.style.display = 'inline-block'; // Allow skipping if needed

        } else if (currentStageId === 'stage-mold-salt') {
             simulateMoldSaltButton.style.display = 'inline-block';
             simulateMoldSaltButton.disabled = moldedAndSalted;
             updateStatus(moldedAndSalted ? 'הגבן עבר לתבנית והומלח.' : 'העבר את הגבן המנוקז לתבניות והמלחהו.');
             moldedCheeseVisual.querySelector('.cheese-shape-initial').style.transform = 'scale(1)'; // Reset visual state

             if ((culturesAdded || moldAdded) && curdCut && !moldedAndSalted) nextButton.style.display = 'inline-block'; // Allow skipping

        } else if (currentStageId === 'stage-needle') {
            needleCheeseVisual.style.cursor = 'crosshair'; // Indicate interactivity
            needleCheeseVisual.innerHTML = '<div class="cheese-base"></div><div class="needle-visual"></div>'; // Reset holes and mold
             needlesCount = 0; // Reset count
             updateStatus(`לחץ על הגבינה לנקב! לפחות ${minNeedles} נקבים נדרשים.`);
             minNeedlesSpan.textContent = minNeedles;

             if ((culturesAdded || moldAdded) && moldedAndSalted) nextButton.style.display = 'inline-block'; // Allow skipping needling

        } else if (currentStageId === 'stage-ripening') {
             needleCheeseVisual.style.cursor = 'default'; // Remove crosshair
             moldGrowthArea.innerHTML = ''; // Clear mold growth area
             startRipeningButton.style.display = 'inline-block';
             startRipeningButton.disabled = false; // Enable button
             updateStatus('לחץ על "התחל הבשלה מואצת" כדי לראות את התפתחות העובש.');

        } else if (currentStageId === 'stage-finished') {
             finalMoldDisplay.innerHTML = ''; // Clear previous result
             resetButton.style.display = 'inline-block';
             nextButton.style.display = 'none'; // No next stage
             updateStatus('תהליך ייצור הגבינה הכחולה הושלם.');
             showFinalResult(); // Determine and display the final outcome
        }
    }

    function nextStage() {
         // Check prerequisites before moving
        if (currentStageIndex === stages.length - 1) {
             // Already at the end
             return;
        }

         const currentStageId = stages[currentStageIndex].id;
         let canAdvance = true;
         let statusOverride = null;

         if (currentStageId === 'stage-milk' && !culturesAdded) {
              canAdvance = false;
              statusOverride = 'אנא הוסף מחמצות קודם.';
         } else if (currentStageId === 'stage-curd' && !moldAdded && culturesAdded) { // Can skip mold if cultures were added
             canAdvance = true; // Allowed to skip mold, but result will differ
         } else if (currentStageId === 'stage-curd' && !moldAdded && !culturesAdded) { // Can't proceed without cultures OR mold
              canAdvance = false;
              statusOverride = 'אנא הוסף מחמצות ו/או עובש כדי להמשיך.';
         }
          else if (currentStageId === 'stage-cut-drain' && !curdCut && (culturesAdded || moldAdded)) {
              canAdvance = false;
              statusOverride = 'אנא חתוך את הגבן קודם.';
          } else if (currentStageId === 'stage-mold-salt' && !moldedAndSalted && (culturesAdded || moldAdded) && curdCut) {
               canAdvance = false;
               statusOverride = 'אנא העבר לתבנית והמלחה קודם.';
          }
           else if (currentStageId === 'stage-needle' && needlesCount < minNeedles && moldAdded && moldedAndSalted) {
                // If mold was added, needling is crucial
                canAdvance = false;
                statusOverride = `עליך לנקב את הגבינה לפחות ${minNeedles} פעמים לפני המעבר לשלב ההבשלה.`;
           }
            else if (currentStageId === 'stage-needle' && moldedAndSalted && !moldAdded) {
                 // If mold wasn't added, needling isn't critical for *blue* cheese, can advance
                 canAdvance = true;
            }
            else if (currentStageId === 'stage-ripening' && startRipeningButton.disabled) {
                 // Must start ripening simulation
                 canAdvance = false;
                 statusOverride = 'אנא התחל את תהליך ההבשלה כדי לראות את התוצאה.';
            }


        if (canAdvance) {
            currentStageIndex++;
            showStage(currentStageIndex);
        } else if (statusOverride) {
             updateStatus(statusOverride);
        }
    }

    function toggleExplanation() {
        const isHidden = explanationSection.style.display === 'none';
        explanationSection.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג איך עשינו את זה? (הסבר מדעי)';
        toggleExplanationButton.setAttribute('aria-expanded', !isHidden);
        explanationSection.setAttribute('aria-hidden', isHidden);
    }

    // --- Interaction Event Listeners ---

    // Stage 1: Add Cultures
    addCulturesButton.addEventListener('click', () => {
        culturesAdded = true;
        addCulturesButton.disabled = true;
        culturesAddPoint.classList.add('active'); // Show sprinkle animation
        updateStatus('מחמצות הוספו! החלב מתחיל להתגבן לאט...');
         nextButton.style.display = 'inline-block'; // Allow moving on
         setTimeout(() => {
              culturesAddPoint.classList.remove('active');
               milkVisual.querySelector('.milk-liquid').style.transform = 'translateY(5%)'; // Simulate slight change
         }, 1000); // Animation duration
    });

    // Stage 2: Add Mold
    addMoldButton.addEventListener('click', () => {
        moldAdded = true;
        addMoldButton.disabled = true;
         moldSprinklePoint.classList.add('active'); // Show sprinkle animation
        updateStatus('קסם כחול הוסף! נבגי העובש ממתינים לרגע הנכון...');
         nextButton.style.display = 'inline-block'; // Allow moving on
          setTimeout(() => {
               moldSprinklePoint.classList.remove('active');
               curdVisual.querySelector('.curd-block').style.transform = 'scale(0.98)'; // Simulate slight change
          }, 1000); // Animation duration
    });

     // Stage 3: Cut Curd
     simulateCutButton.addEventListener('click', () => {
         curdCut = true;
         simulateCutButton.disabled = true;
         curdCutGrid.style.opacity = 1; // Show cut grid visual
         updateStatus('הגבן נחתך לקוביות! מי הגבן מתחילים לזרום החוצה.');
          nextButton.style.display = 'inline-block'; // Allow moving on
     });

     // Stage 4: Mold and Salt
      simulateMoldSaltButton.addEventListener('click', () => {
          moldedAndSalted = true;
          simulateMoldSaltButton.disabled = true;
          moldedCheeseVisual.querySelector('.cheese-shape-initial').style.transform = 'scale(0.95)'; // Simulate compaction
          updateStatus('הגבן עבר לתבנית ועבר טיפול מלכה עשיר.');
           nextButton.style.display = 'inline-block'; // Allow moving on
      });


    // Stage 5: Needling interaction
    needleCheeseVisual.addEventListener('click', (event) => {
        if (stages[currentStageIndex].id === 'stage-needle' && moldedAndSalted) { // Only interactive if in this stage AND prior step done
            const rect = needleCheeseVisual.getBoundingClientRect();
            // Get click position relative to the visual element, accounting for padding/border
            const x = event.clientX - rect.left - parseFloat(getComputedStyle(needleCheeseVisual).borderLeftWidth);
            const y = event.clientY - rect.top - parseFloat(getComputedStyle(needleCheeseVisual).borderTopWidth);

             // Check if click is within the circular cheese area (approx)
             const centerX = rect.width / 2;
             const centerY = rect.height / 2;
             const radius = Math.min(centerX, centerY); // Approx radius
             const distance = Math.sqrt(Math.pow(x - centerX, 2) + Math.pow(y - centerY, 2));

             if (distance > radius) {
                 // Click was outside the circle, ignore
                 updateStatus('אנא לחץ בתוך מעגל הגבינה!');
                 return;
             }


            const hole = document.createElement('div');
            hole.classList.add('needle-hole');
            hole.style.left = `${x}px`;
            hole.style.top = `${y}px`;
            needleCheeseVisual.appendChild(hole);

            needlesCount++;
            updateStatus(`נקבת את הגבינה! סך הכל נקבים: ${needlesCount}. נדרשים לפחות ${minNeedles}.`);

             // Animate a temporary needle visual near the click
             needleVisual.style.left = `${x}px`;
             needleVisual.style.top = `${y}px`;
             needleVisual.style.transform = 'translate(-50%, -50%) scale(1)';
             needleVisual.style.opacity = 1;
             setTimeout(() => {
                  needleVisual.style.transform = 'translate(-50%, -50%) scale(0)';
                  needleVisual.style.opacity = 0;
             }, 300); // Quick animation

            if (needlesCount >= minNeedles) {
                 finishNeedlingButton.style.display = 'inline-block';
                 updateStatus(`מעולה! יש לך ${needlesCount} נקבים. סיימת לנקב?`);
            }
        } else if (stages[currentStageIndex].id === 'stage-needle' && !moldedAndSalted) {
             updateStatus('עליך לעבור את שלב התבניות וההמלחה קודם.');
        }
    });

    // Stage 5: Finish Needling Button
    finishNeedlingButton.addEventListener('click', () => {
         if (needlesCount >= minNeedles) {
             updateStatus('הניקוב הושלם! עכשיו הגבינה נושמת ומוכנה להבשלה!');
             finishNeedlingButton.disabled = true; // Disable button after click
             nextButton.style.display = 'inline-block'; // Allow moving on
             nextButton.textContent = 'קדימה להבשלה'; // Change button text
         } else {
              updateStatus(`עליך לנקב לפחות ${minNeedles} פעמים.`);
         }
    });


    // Stage 6: Start Ripening
    startRipeningButton.addEventListener('click', () => {
         startRipeningButton.disabled = true;
         let ripeningMessage = '';
         let moldPotential = 0; // 0: none, 1: limited, 2: full

         if (!moldAdded) {
              ripeningMessage = 'לא הוספת עובש! הגבינה תבשיל, אך לא תפתח עורקים כחולים אופייניים.';
              moldPotential = 0;
         } else if (needlesCount < minNeedles) {
              ripeningMessage = `ניקבת רק ${needlesCount} פעמים (פחות מהמומלץ ${minNeedles}). צמיחת העובש תהיה מוגבלת מאוד בגלל מחסור בחמצן.`;
              moldPotential = 1;
         } else {
             ripeningMessage = `מעולה! עם ${needlesCount} נקבים, לעובש יש די חמצן לצמוח! צפה בהתפתחות...`;
             moldPotential = 2;
         }
         updateStatus(ripeningMessage);


        // Simulate mold growth animation based on moldPotential and needle locations
        moldGrowthArea.innerHTML = ''; // Clear previous
         const holes = needleCheeseVisual.querySelectorAll('.needle-hole');

         if (moldPotential > 0) {
             holes.forEach(hole => {
                  const holePos = {
                      x: parseFloat(hole.style.left),
                      y: parseFloat(hole.style.top)
                  };

                  const linesPerHole = moldPotential === 2 ? 4 : 1; // More lines if proper needling

                  for(let i=0; i < linesPerHole; i++) {
                       const moldLine = document.createElement('div');
                       moldLine.classList.add('mold-line');
                       moldGrowthArea.appendChild(moldLine);

                       // Position at the hole
                       moldLine.style.left = `${holePos.x}px`;
                       moldLine.style.top = `${holePos.y}px`;

                       // Calculate direction randomly or towards center/edge
                        const angle = Math.random() * 360; // Random direction
                        const length = (moldPotential === 2 ? Math.random() * 120 + 40 : Math.random() * 40 + 20); // Longer lines if full potential


                        moldLine.style.transform = `rotate(${angle}deg)`;
                        moldLine.style.width = '0'; // Start thin/short
                        moldLine.style.opacity = 0;

                        // Animate width and opacity
                        setTimeout(() => {
                            moldLine.style.width = `${length}px`;
                            moldLine.style.opacity = 1;
                        }, 100 + i * 50); // Stagger animation slightly
                  }
             });
         }


        // Allow moving to the finished stage after a delay simulating the ripening time
        setTimeout(() => {
             updateStatus('ההבשלה הסתיימה!');
             nextButton.textContent = 'סיים תהליך ייצור';
             nextButton.style.display = 'inline-block';
        }, 4000); // Simulate ripening takes 4 seconds with animation
    });

    // Stage 7: Show Final Result
    function showFinalResult() {
         finalMoldDisplay.innerHTML = ''; // Clear visual
         finishedCheeseVisual.style.backgroundColor = '#ffd54f'; // Default cheese color

         if (!culturesAdded) {
             finalMoldDisplay.textContent = 'תהליך הגיבון לא התחיל! אין גבינה בכלל.';
             finishedCheeseVisual.style.backgroundColor = '#f0f0f0'; // Grey background
             finishedCheeseVisual.style.color = '#c62828';
         } else if (!moldAdded) {
             finalMoldDisplay.textContent = 'הגבינה מוכנה, אך ללא עובש כחול (עובש לא הוסף).';
             finishedCheeseVisual.style.backgroundColor = '#fff9c4'; // Light yellow
             finishedCheeseVisual.style.color = '#333';
         } else if (needlesCount < minNeedles) {
             finalMoldDisplay.textContent = `הגבינה פיתחה מעט עורקים כחולים, אך לא מספיק בגלל חוסר חמצן (רק ${needlesCount} נקבים).`;
              finishedCheeseVisual.style.backgroundColor = '#ffeb3b'; // Yellowish
              finishedCheeseVisual.style.color = '#333';
              // Add some limited mold lines
               const holes = needleCheeseVisual.querySelectorAll('.needle-hole'); // Use holes from stage 5
               holes.forEach(hole => {
                    const holePos = { x: parseFloat(hole.style.left), y: parseFloat(hole.style.top) };
                    const moldLine = document.createElement('div');
                    moldLine.classList.add('mold-line');
                     moldLine.style.backgroundColor = '#4a148c'; // Darker blue
                    finalMoldDisplay.appendChild(moldLine);

                    const angle = Math.random() * 360;
                    const length = Math.random() * 60 + 10;
                    moldLine.style.left = `${holePos.x}px`;
                    moldLine.style.top = `${holePos.y}px`;
                    moldLine.style.width = `${length}px`;
                    moldLine.style.height = '4px';
                    moldLine.style.transform = `rotate(${angle}deg)`;
                    moldLine.style.opacity = 0.8; // Partial visibility
               });

         } else {
             finalMoldDisplay.textContent = `מזל טוב! יצרת בהצלחה גבינה כחולה עשירה עם עורקים מרשימים (${needlesCount} נקבים)!`;
              finishedCheeseVisual.style.backgroundColor = '#ffc107'; // Amber
              finishedCheeseVisual.style.color = '#0d47a1'; // Blue text
              // Add full mold lines (replicate ripening animation outcome)
              const holes = needleCheeseVisual.querySelectorAll('.needle-hole'); // Use holes from stage 5
              holes.forEach(hole => {
                   const holePos = { x: parseFloat(hole.style.left), y: parseFloat(hole.style.top) };
                   const linesPerHole = 4; // Same as ripening

                   for(let i=0; i < linesPerHole; i++) {
                       const moldLine = document.createElement('div');
                       moldLine.classList.add('mold-line');
                        moldLine.style.backgroundColor = '#1a237e'; // Full blue color
                       finalMoldDisplay.appendChild(moldLine);

                       const angle = Math.random() * 360;
                       const length = Math.random() * 120 + 40;
                       moldLine.style.left = `${holePos.x}px`;
                       moldLine.style.top = `${holePos.y}px`;
                       moldLine.style.width = `${length}px`;
                       moldLine.style.height = '4px';
                       moldLine.style.transform = `rotate(${angle}deg)`;
                       moldLine.style.opacity = 1; // Fully visible
                   }
              });
         }
    }


    // Reset Simulation
    resetButton.addEventListener('click', () => {
        currentStageIndex = 0;
        moldAdded = false;
        culturesAdded = false;
        curdCut = false;
        moldedAndSalted = false;
        needlesCount = 0;

        // Reset specific visuals and buttons
         culturesAddPoint.classList.remove('active');
         moldSprinklePoint.classList.remove('active');
         curdCutGrid.style.opacity = 0;
         needleCheeseVisual.innerHTML = '<div class="cheese-base"></div><div class="needle-visual"></div>';
         moldGrowthArea.innerHTML = '';
         finalMoldDisplay.innerHTML = ''; // Clear final result display
         finishedCheeseVisual.style.backgroundColor = ''; // Reset background
         finishedCheeseVisual.style.color = ''; // Reset text color


        showStage(currentStageIndex);
    });


    // Event Listeners
    nextButton.addEventListener('click', nextStage);
    toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Initialize the simulation
    showStage(currentStageIndex);

</script>