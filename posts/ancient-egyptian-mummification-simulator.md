---
title: "מסע אל הנצח: סימולטור טקס החניטה המצרי"
english_slug: ancient-egyptian-mummification-simulator
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags:
  - מצרים העתיקה
  - חניטה
  - מומיפיקציה
  - טקסי קבורה
  - היסטוריה עתיקה
  - אינטראקטיבי
---
<!DOCTYPE html>
<html lang="he">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>מסע אל הנצח: סימולטור טקס החניטה המצרי</title>
    <link href="https://fonts.googleapis.com/css2?family=Ariel&display=swap" rel="stylesheet"> <!-- Using a common Hebrew font -->
    <style>
        :root {
            --egyptian-sand: #e0c9a7;
            --egyptian-gold: #b8860b; /* DarkGoldenRod */
            --egyptian-terracotta: #c06c4a;
            --egyptian-blue: #4a6a8f;
            --egyptian-dark: #3a2b1a;
            --egyptian-light: #fcf8f3;
        }

        body {
            font-family: 'Ariel', sans-serif;
            line-height: 1.8;
            margin: 0;
            padding: 0;
            background: linear-gradient(to bottom, var(--egyptian-light), var(--egyptian-sand));
            color: var(--egyptian-dark);
            direction: rtl;
            text-align: right;
            min-height: 100vh;
            padding-bottom: 40px; /* Space for button/explanation */
        }

        .container {
            max-width: 900px;
            margin: 30px auto;
            background: var(--egyptian-light);
            padding: 30px 40px;
            border-radius: 12px;
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
            border: 2px solid var(--egyptian-gold);
        }

        h1, h2 {
            color: var(--egyptian-terracotta);
            text-align: center;
            font-weight: bold;
            margin-bottom: 20px;
        }

        p {
            margin-bottom: 15px;
            line-height: 1.7;
        }

        .simulator-area {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 30px;
            padding: 30px;
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.7); /* Semi-transparent white */
            box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1);
            position: relative; /* Needed for absolute positioning of body and targets */
        }

        .instruction, .step-explanation {
            margin-bottom: 20px;
            padding: 15px;
            border: 2px dashed var(--egyptian-blue);
            border-radius: 8px;
            min-height: 40px;
            text-align: center;
            font-size: 1.1em;
            font-weight: bold;
            color: var(--egyptian-dark);
            background-color: rgba(255, 255, 255, 0.9);
            width: 90%;
            max-width: 600px;
        }

        .step-explanation {
            background-color: rgba(144, 238, 144, 0.5); /* Light green semi-transparent */
            border-color: var(--egyptian-gold);
            color: var(--egyptian-dark);
            display: none;
            transition: opacity 0.5s ease-in-out;
            opacity: 0;
        }
        .step-explanation.visible {
             opacity: 1;
        }
         .error-message {
            background-color: rgba(255, 99, 71, 0.5); /* Tomato semi-transparent */
            border-color: red;
            color: var(--egyptian-dark);
         }


        .body-illustration-container {
            position: relative;
            width: 250px; /* Slightly larger */
            height: 500px; /* Slightly larger */
            margin-bottom: 30px;
            background-color: rgba(255, 255, 255, 0.3);
            border-radius: 10px;
        }

        .body-illustration {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/social/person_outline/2x_web/ic_person_outline_black_48dp.png'); /* A simple person outline icon as placeholder */
             background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
             transition: background-image 0.5s ease-in-out;
        }

        /* Visual Overlays for Body Illustration */
        .body-illustration::before, .body-illustration::after {
             content: '';
             position: absolute;
             top: 0;
             left: 0;
             width: 100%;
             height: 100%;
             background-size: contain;
             background-repeat: no-repeat;
             background-position: center;
             opacity: 0;
             transition: opacity 0.5s ease-in-out;
        }

        .body-illustration.cut-made::before {
            content: ''; /* Or a specific cut mark image */
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><line x1="75" y1="45" x2="85" y2="55" stroke="red" stroke-width="3"/></svg>'); /* Simple red line */
            opacity: 1;
        }

        .body-illustration.natron-applied {
            background-image: url('https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/social/person_outline/2x_web/ic_person_outline_black_48dp.png'), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="0" y="0" width="100" height="100" fill="%23e0c9a7" opacity="0.7"/></svg>'); /* Base + Natron overlay */
             background-size: contain, cover;
             background-repeat: no-repeat, no-repeat;
             background-position: center, center;
        }

         .body-illustration.oiled {
            background-image: url('https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/social/person_outline/2x_web/ic_person_outline_black_48dp.png'), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="0" y="0" width="100" height="100" fill="%23b8860b" opacity="0.3"/></svg>'); /* Base + Oil sheen overlay */
             background-size: contain, cover;
             background-repeat: no-repeat, no-repeat;
             background-position: center, center;
        }

        .body-illustration.bandages-start {
             background-image: url('https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/social/person_outline/2x_web/ic_person_outline_black_48dp.png'), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="0" y="0" width="100" height="100" fill="%23fcf8f3" opacity="0.8"/></svg>'); /* Base + light bandage */
             background-size: contain, cover;
             background-repeat: no-repeat, no-repeat;
             background-position: center, center;
        }
         .body-illustration.bandages-complete {
             background-image: url('https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/social/person_outline/2x_web/ic_person_outline_black_48dp.png'), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="0" y="0" width="100" height="100" fill="%23fcf8f3" opacity="0.95"/></svg>'); /* Base + dense bandage */
             background-size: contain, cover;
             background-repeat: no-repeat, no-repeat;
             background-position: center, center;
        }
        /* Add more classes for specific steps like amulets visible under bandages */


        .tool, .material, .amulet {
            width: 60px; /* Slightly larger */
            height: 60px;
            margin: 8px;
            cursor: grab;
            border: 2px solid var(--egyptian-terracotta);
            border-radius: 8px;
            display: flex;
            flex-direction: column; /* Stack icon and text */
            justify-content: center;
            align-items: center;
            background-color: var(--egyptian-light);
            font-size: 11px; /* Adjust font size */
            text-align: center;
            user-select: none;
            transition: transform 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
            position: relative; /* Needed for icons */
        }

        .tool img, .material img, .amulet img {
            width: 30px; /* Icon size */
            height: 30px;
            margin-bottom: 3px; /* Space between icon and text */
        }

        .tools-materials {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            margin-bottom: 30px;
            min-height: 80px; /* Ensure space even when empty */
        }

        .target-area {
            position: absolute;
            border: 3px dashed var(--egyptian-blue);
            background-color: rgba(74, 106, 143, 0.2); /* Egyptian blue semi-transparent */
            z-index: 10; /* Above body illustration */
            opacity: 0;
            transition: opacity 0.4s ease, border-color 0.4s ease, background-color 0.4s ease;
            pointer-events: none; /* Don't block clicks when not highlighted */
            border-radius: 8px;
        }

        .target-area.highlight {
            opacity: 1;
            pointer-events: auto; /* Enable clicks/drops when highlighted */
        }
        .target-area.active {
            border-color: var(--egyptian-gold);
            background-color: rgba(184, 134, 11, 0.3); /* Gold semi-transparent */
        }

        /* Specific target areas - adjust positions based on body image */
        /* These positions are relative to the .body-illustration-container */
        #target-brain { top: 8%; left: 25%; width: 50%; height: 10%; }
        #target-side { top: 40%; left: 70%; width: 20%; height: 15%; }
        #target-organs { top: 65%; left: 20%; width: 60%; height: 15%; } /* Area representing Canopic jars location */
        #target-body { top: 20%; left: 15%; width: 70%; height: 60%; } /* General body area for natron/oils/bandages */
        #target-amulets { top: 50%; left: 30%; width: 40%; height: 20%; } /* Area under bandages */


        button {
            display: block;
            margin: 30px auto;
            padding: 12px 25px;
            background-color: var(--egyptian-terracotta);
            color: var(--egyptian-light);
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 1em;
            transition: background-color 0.3s ease, transform 0.1s ease;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        button:hover {
            background-color: var(--egyptian-dark);
        }
         button:active {
            transform: scale(0.98);
        }

        .explanation {
            margin-top: 40px;
            padding: 30px;
            border: 2px solid var(--egyptian-blue);
            border-radius: 10px;
            background-color: var(--egyptian-light);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            display: none;
            transition: opacity 0.5s ease-in-out;
        }
         .explanation.visible {
            opacity: 1;
         }

        .explanation h3 {
             color: var(--egyptian-gold);
             margin-top: 20px;
             margin-bottom: 10px;
             font-weight: bold;
        }
        .explanation ul {
            list-style: disc inside;
            padding-right: 20px;
        }
        .explanation li {
            margin-bottom: 10px;
            line-height: 1.6;
        }

         /* Visual feedback for drag/drop */
        .tool.dragging, .material.dragging, .amulet.dragging {
            opacity: 0.8;
            transform: scale(1.1);
            box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
            cursor: grabbing;
        }

        .item-used {
            opacity: 0.4;
            cursor: default;
            transform: scale(0.9);
            pointer-events: none; /* Prevent dragging after use */
        }

         .final-mummy {
            width: 250px;
            height: 500px;
            background-image: url('https://via.placeholder.com/250x500?text=מומיה+מוכנה'); /* Placeholder for final mummy */
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            margin-bottom: 30px;
            transition: opacity 1s ease-in-out;
            opacity: 0; /* Start hidden */
         }
         .final-mummy.visible {
            opacity: 1;
         }

    </style>
</head>
<body>
    <div class="container">
        <h1>מסע אל הנצח: סימולטור טקס החניטה המצרי</h1>
        <p>הצטרפו אלינו למסע בזמן אל מצרים העתיקה, וגלו את סודות אחד הטקסים המסתוריים והחשובים ביותר: החניטה. תהליך זה, שנועד להבטיח חיי נצח לנפטר, דרש מיומנות, ידע עמוק ושימוש בחומרים מיוחדים. כעת, בתור חונטים מצריים מיומנים, תוכלו לבצע את השלבים הקריטיים בעצמכם.</p>
        <p>עקבו אחר ההוראות, בחרו את הכלי או החומר הנכון, וגררו אותו לאזור המתאים על הגופה כדי להשלים את הטקס הקדוש.</p>

        <div class="simulator-area" id="simulator-area">
            <div class="instruction">הטקס מתחיל... עקוב אחר ההוראות.</div>

            <div class="body-illustration-container">
                 <div class="body-illustration" id="body-illustration">
                    <!-- Target areas are absolutely positioned relative to this container -->
                    <div class="target-area" id="target-brain" data-target="brain"></div>
                    <div class="target-area" id="target-side" data-target="side"></div>
                    <div class="target-area" id="target-organs" data-target="organs"></div>
                    <div class="target-area" id="target-body" data-target="body"></div>
                    <div class="target-area" id="target-amulets" data-target="amulets"></div>
                 </div>
            </div>

             <div class="step-explanation"></div>

            <div class="tools-materials">
                <!-- Tools and Materials - Use icons or better visuals -->
                <div class="tool" data-item="hook" draggable="true"><img src="https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/hardware/memory/2x_web/ic_memory_black_48dp.png" alt="וו"> וו (מוח)</div>
                <div class="tool" data-item="knife" draggable="true"><img src="https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/editor/cut/2x_web/ic_cut_black_48dp.png" alt="סכין"> סכין (איברים)</div>
                 <div class="material" data-item="organs" draggable="true"><img src="https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/social/sentiment_dissatisfied/2x_web/ic_sentiment_dissatisfied_black_48dp.png" alt="איברים"> איברים פנימיים</div> <!-- Representing the removed organs -->
                <div class="material" data-item="natron" draggable="true"><img src="https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/file/folder_special/2x_web/ic_folder_special_black_48dp.png" alt="נטרון"> נטרון</div>
                <div class="material" data-item="oils-resins" draggable="true"><img src="https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/image/grain/2x_web/ic_grain_black_48dp.png" alt="שמנים"> שמנים ושרפים</div>
                <div class="material" data-item="bandages" draggable="true"><img src="https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/action/lock/2x_web/ic_lock_black_48dp.png" alt="בנדאז'ים"> בנדאז'ים</div> <!-- Lock icon symbolic of sealing -->
                <div class="amulet" data-item="heart-scarab" draggable="true"><img src="https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/action/favorite/2x_web/ic_favorite_black_48dp.png" alt="קמע לב"> קמע לב</div>
                 <div class="amulet" data-item="amulet-protection" draggable="true"><img src="https://cdn.jsdelivr.net/gh/google/material-design-icons@master/png/action/verified_user/2x_web/ic_verified_user_black_48dp.png" alt="קמע הגנה"> קמעות הגנה</div>
                 <!-- Add more amulets as needed -->
            </div>
             <!-- Final mummy visual - initially hidden -->
            <div class="final-mummy" id="final-mummy"></div>
        </div>

        <button id="toggle-explanation">הצג הסבר מורחב על החניטה</button>

        <div class="explanation" id="full-explanation">
            <h2>על טקס החניטה במצרים העתיקה: מסע אל הנצח</h2>
            <p>החניטה לא הייתה סתם שימור גופה, אלא טקס דתי מורכב וחיוני להבטחת חיי הנצח. המצרים האמינו שה-Ka (כוח החיים) וה-Ba (האישיות/נשמה) זקוקים לגוף פיזי שלם כדי לשוב אליו ולהתקיים בעולם הבא. תהליך זה, שנמשך כ-70 יום, דרש מיומנות רבה מצד הכוהנים והחונטים.</p>
            <h3>השלבים המרכזיים במסע:</h3>
            <ul>
                <li>**טיהור ראשוני:** הגופה נוקתה בקפידה במים קדושים מהנילוס וביינות תמרים, כהכנה לטקס.</li>
                <li>**הוצאת המוח:** באמצעות וו ארוך ודק, המוח הוצא דרך הנחיריים. המצרים לא ייחסו למוח חשיבות רבה כמו ללב.</li>
                <li>**הוצאת איברים פנימיים:** חתך יזום נעשה בצד שמאל של הבטן. הריאות, הקיבה, המעיים והכבד הוצאו, נוקו, יובשו בנטרון והונחו בצנצנות קנופיות - כל אחת תחת הגנתו של אחד מבני הורוס. הלב, שנחשב למרכז האינטליגנציה והרגשות, הושאר במקומו.</li>
                <li>**ייבוש הגופה:** הגופה כוסתה ומולאה באלפי קילוגרמים של מלח נטרון (תערובת טבעית של סודה לשתייה ומלח). הנטרון ספג את כל הנוזלים, תהליך שלקח כ-40 יום ומנע ריקבון.</li>
                <li>**שטיפה ומילוי:** לאחר הייבוש, הנטרון הוצא. הגופה נשטפה שוב, ולעתים מולאה בחומרים כמו פשתן, נסורת או בוץ כדי לשמור על צורתה.</li>
                <li>**שימון ובישום:** הגופה נמשחה בשמנים ארומטיים ושרפים (כמו שרף ארז) - גם לשימור, גם לריח טוב וגם כדי לרכך את העור לפני העטיפה.</li>
                <li>**העטיפה הקדושה:** זה היה שלב ארוך ומורכב. הגופה עוטפה באלפי מטרים של רצועות פשתן, שכבה אחר שכבה. כל שכבה נמשחה בשרפים. בין השכבות הונחו קמעות קדושים.</li>
                <li>**הנחת קמעות:** קמעות רבים הונחו בין רצועות הפשתן, כל אחד עם תפקיד מגן או מסייע במסע לעולם הבא. קמע הלב (חיפושית גדולה) היה החשוב ביותר, והונח ישירות על הלב כדי להבטיח שהוא לא יעיד נגד הנפטר במשפט המתים. קמעות נפוצים נוספים כללו את עין הורוס להגנה, קשר איזיס לחיים, ועוד.</li>
                <li>**טקס פתיחת הפה:** טקס זה, שהתבצע על המומיה או על ארון הקבורה/מסכה, היה קריטי. הוא נועד "להחזיר" לנפטר את היכולת לאכול, לדבר, לראות ולשמוע בעולם הבא, ובכך להשלים את הפיכתו לישות נצחית.</li>
            </ul>
            <p>לאחר השלמת הטקס, המומיה הונחה בארון קבורה, לעתים קרובות בתוך סרקופג מפואר, מוכנה למסע המכריע לעולם הבא ולמשפט המתים.</p>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const instructionDiv = document.querySelector('.instruction');
            const stepExplanationDiv = document.querySelector('.step-explanation');
            const toolsMaterialsArea = document.querySelector('.tools-materials');
            const bodyIllustration = document.getElementById('body-illustration');
            const targetAreas = document.querySelectorAll('.target-area');
            const toggleExplanationButton = document.getElementById('toggle-explanation');
            const fullExplanationDiv = document.getElementById('full-explanation');
             const finalMummyDiv = document.getElementById('final-mummy');
             const simulatorArea = document.getElementById('simulator-area');


            let currentStep = 0;
            const steps = [
                {
                    instruction: 'שלב 1: טיהור הגופה. דמיינו שהגופה טוהרה במי הנילוס ויינות תמרים.',
                    explanation: 'הטקס מתחיל בטיהור הגוף לקראת המסע הגדול.',
                    requiredItem: null,
                    targetArea: null,
                    visualChange: () => {
                        // No strong visual change, maybe a subtle glow or ripple effect if possible
                        // For now, just acknowledge the step
                    },
                    autoAdvance: true
                },
                {
                    instruction: 'שלב 2: הוצאת המוח. גרור את הוו אל אזור הראש/אף.',
                    explanation: 'המוח הוצא דרך הנחיריים, כיוון שלא נחשב חיוני לחיים שלאחר המוות.',
                    requiredItem: 'hook',
                    targetArea: 'brain',
                    visualChange: () => {
                         // Add a small visual cue for brain removal (difficult without complex SVG/canvas)
                         // Maybe change the body opacity slightly or add a specific small icon near the nose
                         // For simplicity, we'll rely on the explanation and target highlight
                    }
                },
                 {
                    instruction: 'שלב 3: פתיחת הגוף. גרור את הסכין לצד שמאל של הבטן כדי ליצור חתך.',
                    explanation: 'חתך יזום בצד שמאל אפשר גישה לאיברים הפנימיים.',
                    requiredItem: 'knife',
                    targetArea: 'side',
                    visualChange: () => {
                         bodyIllustration.classList.add('cut-made'); // Add a class to show the cut
                    }
                },
                 {
                    instruction: 'שלב 4: הנחת האיברים הפנימיים בצנצנות הקנופיות. גרור את "האיברים הפנימיים" לאזור המיועד לצנצנות.',
                    explanation: 'האיברים (למעט הלב) נוקו, יובשו והונחו בצנצנות קנופיות לשמירה.',
                    requiredItem: 'organs',
                    targetArea: 'organs',
                    visualChange: () => {
                        // Add a visual cue for canopic jars appearing (difficult without complex SVG/canvas)
                        // Maybe change the background of the target area permanently or add icons there
                    }
                },
                {
                    instruction: 'שלב 5: ייבוש הגופה. גרור את הנטרון על הגוף כולו.',
                    explanation: 'נטרון ספג את כל הלחות מהגופה, תהליך חיוני לשימור.',
                    requiredItem: 'natron',
                    targetArea: 'body',
                    visualChange: () => {
                         bodyIllustration.classList.add('natron-applied'); // Add class for natron visual
                    }
                },
                 {
                    instruction: 'שלב 6: ניקוי ומילוי. דמיינו שהנטרון הוסר והגופה מולאה מחדש.',
                    explanation: 'הגופה נוקתה מהנטרון ומולאה בחומרים לשמירת צורתה.',
                    requiredItem: null,
                    targetArea: null,
                     visualChange: () => {
                         bodyIllustration.classList.remove('natron-applied'); // Remove natron visual
                         // Maybe add a class for 'filled' state, but visually similar to base for now
                     },
                    autoAdvance: true
                },
                {
                    instruction: 'שלב 7: שימון ובישום. גרור את השמנים והשרפים על הגוף.',
                    explanation: 'שמנים ושרפים שימרו, בישמו וריככו את העור לקראת העטיפה.',
                    requiredItem: 'oils-resins',
                    targetArea: 'body',
                    visualChange: () => {
                         bodyIllustration.classList.add('oiled'); // Add class for oily sheen
                    }
                },
                {
                    instruction: 'שלב 8: תחילת העטיפה. גרור את הבנדאז\'ים על הגוף.',
                    explanation: 'אלפי מטרים של פשתן עוטפים את הגופה בקפידה.',
                    requiredItem: 'bandages',
                    targetArea: 'body',
                    visualChange: () => {
                         bodyIllustration.classList.remove('oiled'); // Remove oil visual
                         bodyIllustration.classList.add('bandages-start'); // Add initial bandage layer
                    }
                },
                 {
                    instruction: 'שלב 9: הנחת קמעות. גרור קמע לב (חיפושית) על אזור החזה.',
                    explanation: 'קמע הלב היה החשוב ביותר, נועד למנוע מהלב להעיד נגד הנפטר.',
                    requiredItem: 'heart-scarab',
                    targetArea: 'amulets',
                    visualChange: () => {
                         // Add a visual cue for the amulet under bandages (difficult)
                         // Maybe a subtle sparkle effect on the body illustration
                    }
                },
                 {
                    instruction: 'שלב 10: סיום העטיפה והנחת קמעות נוספים. גרור קמעות הגנה על הגוף.',
                    explanation: 'קמעות נוספים הונחו בין שכבות הפשתן להגנה וסיוע במסע.',
                    requiredItem: 'amulet-protection',
                    targetArea: 'body', // Can target the body again for general amulet placement
                    visualChange: () => {
                         bodyIllustration.classList.add('bandages-complete'); // Show more complete wrapping
                         // Maybe add visual cue for general amulets
                    }
                },
                 {
                    instruction: 'שלב 11: טקס פתיחת הפה. דמיינו שהטקס הקריטי הזה בוצע.',
                    explanation: 'טקס זה החזיר לנפטר את חושיו לצורך קיום בעולם הבא.',
                    requiredItem: null,
                    targetArea: null,
                     visualChange: () => {
                         // Add a final symbolic visual? Maybe a glow effect or transition
                     },
                    autoAdvance: true
                },
                 {
                    instruction: 'התהליך הושלם! המומיה מוכנה למסע אל הנצח.',
                    explanation: 'כל שלבי החניטה הושלמו בהצלחה. הנפטר מוכן כעת למשפט המתים ולחיים בעולם הבא.',
                    requiredItem: null,
                    targetArea: null,
                    visualChange: () => {
                         bodyIllustration.style.display = 'none'; // Hide the interactive body
                         finalMummyDiv.classList.add('visible'); // Show the final mummy image
                         toolsMaterialsArea.style.display = 'none'; // Hide tools
                         targetAreas.forEach(area => area.style.display = 'none'); // Hide targets
                    },
                    isLastStep: true
                }
            ];

            let draggedItem = null;
            let isProcessingStep = false; // Flag to prevent rapid drops

            function updateSimulator() {
                if (currentStep >= steps.length) {
                    endSimulation();
                    return;
                }

                const step = steps[currentStep];
                instructionDiv.textContent = step.instruction;
                hideExplanation(); // Hide previous explanation immediately

                // Hide all target areas
                targetAreas.forEach(area => {
                    area.classList.remove('highlight', 'active');
                    area.style.display = 'none';
                    area.style.pointerEvents = 'none'; // Ensure not interactive when hidden
                });

                 // Hide all tools/materials/amulets initially
                 document.querySelectorAll('.tool, .material, .amulet').forEach(item => {
                    item.style.display = 'none';
                    item.classList.remove('item-used'); // Reset used state
                    item.draggable = true; // Make draggable again if needed in a later step (though not in this flow)
                    item.style.opacity = 1; // Reset opacity
                    item.style.transform = 'scale(1)'; // Reset scale
                 });


                // Show only the relevant target area and item for the current step
                if (step.targetArea) {
                    const targetElement = document.getElementById(`target-${step.targetArea}`);
                    if (targetElement) {
                        targetElement.style.display = 'block'; // Show the target area container
                        // Use a timeout to allow display:block to apply before transition
                        setTimeout(() => {
                             targetElement.classList.add('highlight');
                             targetElement.style.pointerEvents = 'auto'; // Make interactive
                        }, 10);
                    }
                }

                if (step.requiredItem) {
                     const requiredItemElement = document.querySelector(`[data-item="${step.requiredItem}"]`);
                     if(requiredItemElement) {
                         requiredItemElement.style.display = 'flex'; // Show the required item
                         requiredItemElement.classList.remove('item-used'); // Ensure it's not marked as used
                         requiredItemElement.draggable = true;
                         requiredItemElement.style.opacity = 1;
                         requiredItemElement.style.transform = 'scale(1)';
                     }
                }

                // Handle auto-advance steps
                if (step.autoAdvance && !isProcessingStep) {
                    isProcessingStep = true; // Prevent re-triggering
                     setTimeout(() => {
                        showExplanation(step.explanation);
                         // Auto-advance after showing explanation for a brief moment
                         setTimeout(() => {
                             hideExplanation();
                             isProcessingStep = false; // Reset flag
                             advanceStep();
                         }, 3500); // Adjust time as needed for reading
                    }, 500); // Short delay before showing explanation
                } else if (!step.requiredItem && !step.autoAdvance && !step.isLastStep) {
                     // Step requires no item but is not auto-advance or last step - this shouldn't happen in this flow, but good to handle
                     console.warn("Step requires no item and is not auto-advance:", step);
                      setTimeout(advanceStep, 1000); // Auto-advance as nothing to do
                }
            }

            function showExplanation(text, isError = false) {
                stepExplanationDiv.textContent = text;
                stepExplanationDiv.classList.remove('error-message');
                if (isError) {
                     stepExplanationDiv.classList.add('error-message');
                }
                stepExplanationDiv.style.display = 'block';
                 setTimeout(() => { stepExplanationDiv.classList.add('visible'); }, 10); // Fade in
            }

             function hideExplanation() {
                 stepExplanationDiv.classList.remove('visible');
                 // Wait for fade out before hiding display
                 setTimeout(() => { stepExplanationDiv.style.display = 'none'; }, 500); // Match CSS transition duration
             }

            function advanceStep() {
                currentStep++;
                updateSimulator();
            }

            function endSimulation() {
                 instructionDiv.textContent = steps[steps.length - 1].instruction;
                 showExplanation(steps[steps.length - 1].explanation);
                 steps[steps.length - 1].visualChange(); // Apply final visual change
                 // Hide interactive elements
                 toolsMaterialsArea.style.display = 'none';
                 targetAreas.forEach(area => area.style.display = 'none');
                 bodyIllustration.style.display = 'none';
                 finalMummyDiv.classList.add('visible'); // Ensure final mummy is visible
                 // Optionally add a "Restart" button
                 // let restartButton = document.createElement('button');
                 // restartButton.textContent = 'התחל מחדש';
                 // restartButton.addEventListener('click', () => { location.reload(); });
                 // simulatorArea.appendChild(restartButton);
            }


            // Drag and Drop Logic
            toolsMaterialsArea.addEventListener('dragstart', (event) => {
                const itemElement = event.target.closest('.tool, .material, .amulet');
                if (itemElement && !itemElement.classList.contains('item-used')) {
                     const item = itemElement.dataset.item;
                     const step = steps[currentStep];
                     // Only allow dragging the correct item for the current step
                     if (step.requiredItem === item && !isProcessingStep) {
                        draggedItem = item;
                        event.dataTransfer.setData('text/plain', item);
                        itemElement.classList.add('dragging');
                        // Highlight the correct target area
                        if (step.targetArea) {
                            const targetElement = document.getElementById(`target-${step.targetArea}`);
                            if (targetElement) {
                                targetElement.classList.add('active'); // Visual feedback for active target
                            }
                        }
                     } else {
                         event.preventDefault(); // Prevent dragging the wrong item or if processing
                         if (!isProcessingStep) {
                              showExplanation('זה לא הכלי או החומר המתאים לשלב זה.', true);
                             setTimeout(hideExplanation, 2000);
                         }
                     }
                } else {
                     event.preventDefault(); // Prevent dragging used items
                }
            });

             toolsMaterialsArea.addEventListener('dragend', (event) => {
                 const itemElement = event.target.closest('.tool, .material, .amulet');
                 if (itemElement) {
                     itemElement.classList.remove('dragging');
                      // Remove active highlight from target areas
                     targetAreas.forEach(area => area.classList.remove('active'));
                     draggedItem = null; // Reset dragged item
                 }
            });

            targetAreas.forEach(area => {
                area.addEventListener('dragover', (event) => {
                    event.preventDefault(); // Necessary to allow dropping
                     const step = steps[currentStep];
                     // Only allow dragover on the correct target area and if the correct item is dragged
                     if (area.dataset.target === step.targetArea && draggedItem === step.requiredItem && !isProcessingStep) {
                         event.dataTransfer.dropEffect = 'move'; // Visual feedback
                         area.classList.add('active'); // Ensure target is active while item is over it
                     } else {
                          event.dataTransfer.dropEffect = 'none';
                          area.classList.remove('active');
                     }
                });

                 area.addEventListener('dragleave', (event) => {
                     // Remove active highlight when item leaves the target area
                     event.target.classList.remove('active');
                 });


                area.addEventListener('drop', (event) => {
                    event.preventDefault();
                    const droppedItem = event.dataTransfer.getData('text/plain');
                    const targetArea = event.target.dataset.target;
                    const step = steps[currentStep];

                    // Check if the dropped item and target area match the current step's requirements and not processing
                    if (step.requiredItem === droppedItem && step.targetArea === targetArea && !isProcessingStep) {
                        isProcessingStep = true; // Set flag
                        // Correct drop!
                        showExplanation(step.explanation);
                        step.visualChange(); // Apply visual change if defined

                        // Mark the used item
                        const usedItemElement = document.querySelector(`[data-item="${droppedItem}"]`);
                        if(usedItemElement) {
                           usedItemElement.classList.add('item-used');
                           usedItemElement.draggable = false;
                        }

                        // Hide the target area immediately or after transition
                        event.target.classList.remove('highlight', 'active'); // Remove highlights
                        // Use opacity transition then hide display
                        event.target.style.opacity = 0;
                        setTimeout(() => { event.target.style.display = 'none'; event.target.style.opacity = 1; }, 500); // Hide after transition


                        // Advance to the next step after explanation is shown
                        setTimeout(() => {
                            hideExplanation();
                            isProcessingStep = false; // Reset flag
                            advanceStep();
                        }, 4000); // Show explanation for 4 seconds

                    } else {
                        // Incorrect drop (This case should be mostly prevented by dragover/dragstart checks, but good fallback)
                        console.log('Incorrect item or target on drop!');
                         if (!isProcessingStep) {
                             showExplanation('שגיאה: זה לא הצעד הנכון כעת או שהשתמשת בכלי הלא נכון.', true);
                             setTimeout(hideExplanation, 2000);
                         }
                    }
                     // Remove active highlight after drop attempt
                     targetAreas.forEach(area => area.classList.remove('active'));
                     draggedItem = null; // Reset dragged item
                });
            });


            // Toggle explanation button
            toggleExplanationButton.addEventListener('click', () => {
                const isHidden = fullExplanationDiv.style.display === 'none' || fullExplanationDiv.style.display === '';
                if (isHidden) {
                     fullExplanationDiv.style.display = 'block';
                     setTimeout(() => { fullExplanationDiv.classList.add('visible'); }, 10); // Fade in
                } else {
                     fullExplanationDiv.classList.remove('visible');
                     setTimeout(() => { fullExplanationDiv.style.display = 'none'; }, 500); // Fade out then hide
                }
                toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצג הסבר מורחב על החניטה';
            });

            // Initialize the simulator
            updateSimulator();
        });
    </script>
</body>
</html>
```