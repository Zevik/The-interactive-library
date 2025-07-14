---
title: "קרב המנגנונים: הוכחת עבודה מול הוכחת החזקה – איך בלוקצ'יין מגיע להסכמה?"
english_slug: proof-of-work-vs-proof-of-stake-blockchain-validation
category: "מדעי המחשב"
tags:
  - בלוקצ'יין
  - Proof of Work
  - Proof of Stake
  - מנגנוני קונצנזוס
  - קריפטוגרפיה
---
<h1>קרב המנגנונים: הוכחת עבודה מול הוכחת החזקה</h1>
<p>איך רשתות מבוזרות וחסרות שליטה מרכזית כמו ביטקוין ואת'ריום מצליחות להגיע להסכמה על מצב הבלוקצ'יין, להוסיף בלוקים חדשים בבטחה ולמנוע רמאויות? הכל בזכות מנגנוני הקונצנזוס הגאוניים שמניעים אותן: הוכחת עבודה (Proof-of-Work) והוכחת החזקה (Proof-of-Stake).</p>

<div id="app-container">
    <h2>התנסו בעצמכם: סימולציית קונצנזוס</h2>
    <p>בואו נראה איך שני המנגנונים הללו עובדים בפועל.</p>

    <div class="controls">
        <button id="mode-pow" class="active">הוכחת עבודה (PoW)</button>
        <button id="mode-pos">הוכחת החזקה (PoS)</button>
    </div>

    <div id="pow-simulation" class="simulation-section">
        <h3>הוכחת עבודה (Proof-of-Work)</h3>
        <p><strong>המטרה:</strong> לפתור חידה קריפטוגרפית מורכבת באמצעות כוח חישוב. הראשון שמוצא פתרון זוכה להוסיף את הבלוק הבא ומקבל תגמול!</p>
        <div class="miners-container">
            <h4>הכורים המתחרים ברשת:</h4>
            <div class="miner user-miner" id="user-miner-pow">
                <img src="https://img.icons8.com/ios-filled/50/000000/computer--v1.png" alt="Miner Icon">
                <p class="miner-name">הכורה שלי</p>
                <div class="attempts-container">
                     <p>ניסיונות (Hash Attempts): <span class="attempts">0</span></p>
                     <div class="progress-bar"><div class="progress"></div></div>
                </div>
                <button class="mine-button">נסה לכרות בלוק!</button>
                <p class="reward">תגמול: 0 מטבעות</p>
            </div>
            <div class="miner" id="other-miner-pow-1">
                 <img src="https://img.icons8.com/ios-filled/50/000000/computer--v1.png" alt="Miner Icon">
                <p class="miner-name">כורה אחר #1</p>
                 <div class="attempts-container">
                     <p>ניסיונות (Hash Attempts): <span class="attempts">0</span></p>
                      <div class="progress-bar"><div class="progress"></div></div>
                 </div>
                 <p class="reward">תגמול: 0 מטבעות</p>
            </div>
             <div class="miner" id="other-miner-pow-2">
                 <img src="https://img.icons8.com/ios-filled/50/000000/computer--v1.png" alt="Miner Icon">
                <p class="miner-name">כורה אחר #2</p>
                 <div class="attempts-container">
                     <p>ניסיונות (Hash Attempts): <span class="attempts">0</span></p>
                      <div class="progress-bar"><div class="progress"></div></div>
                 </div>
                 <p class="reward">תגמול: 0 מטבעות</p>
            </div>
        </div>
         <button id="auto-mine" class="action-button auto-button">התחל כרייה אוטומטית!</button>
        <button id="stop-auto-mine" class="action-button auto-button stop-button" style="display: none;">עצור כרייה אוטומטית</button>

        <div class="blockchain-pow">
            <h4>הבלוקצ'יין (שרשרת הבלוקים):</h4>
            <div class="blockchain-display" id="pow-blockchain-display">
                <div class="block genesis-block">בלוק התחלה</div>
            </div>
        </div>
    </div>

    <div id="pos-simulation" class="simulation-section" style="display: none;">
        <h3>הוכחת החזקה (Proof-of-Stake)</h3>
        <p><strong>המטרה:</strong> להיבחר לאימות הבלוק הבא על בסיס כמות ה"החזקה" (Stake) שיש לך ברשת. המשאב: הון (מטבעות).</p>
         <div class="validators-container">
            <h4>המאמתים (Validators) ברשת:</h4>
            <div class="validator user-validator" id="user-validator-pos">
                 <img src="https://img.icons8.com/ios-filled/50/000000/wallet.png" alt="Wallet Icon">
                <p class="validator-name">המאמת שלי</p>
                <p>החזקה (Stake): <span class="stake-value">100</span> מטבעות</p>
                 <div class="stake-control">
                    <label for="user-stake-slider">שנה החזקה:</label>
                     <input type="range" id="user-stake-slider" min="10" max="500" value="100" class="stake-slider">
                 </div>
                 <p class="reward">סה"כ עמלות: 0 מטבעות</p>
            </div>
            <div class="validator" id="other-validator-pos-1">
                 <img src="https://img.icons8.com/ios-filled/50/000000/wallet.png" alt="Wallet Icon">
                <p class="validator-name">מאמת אחר #1</p>
                <p>החזקה (Stake): <span class="stake-value">200</span> מטבעות</p>
                 <p class="reward">סה"כ עמלות: 0 מטבעות</p>
            </div>
             <div class="validator" id="other-validator-pos-2">
                 <img src="https://img.icons8.com/ios-filled/50/000000/wallet.png" alt="Wallet Icon">
                <p class="validator-name">מאמת אחר #2</p>
                <p>החזקה (Stake): <span class="stake-value">50</span> מטבעות</p>
                 <p class="reward">סה"כ עמלות: 0 מטבעות</p>
            </div>
        </div>
        <button id="start-validation" class="action-button auto-button">התחל תהליך בחירת מאמת!</button>
        <div class="blockchain-pos">
            <h4>הבלוקצ'יין (שרשרת הבלוקים):</h4>
            <div class="blockchain-display" id="pos-blockchain-display">
                <div class="block genesis-block">בלוק התחלה</div>
            </div>
        </div>
    </div>
</div>

<button id="toggle-explanation">רוצים להבין לעומק? לחצו כאן להסבר מלא</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: הוכחת עבודה מול הוכחת החזקה</h2>

    <h3>מהו מנגנון קונצנזוס בבלוקצ'יין ולמה הוא נחוץ?</h3>
    <p>דמיינו ספר חשבונות ענק, שקוף ופומבי, שפרוס על פני אלפי מחשבים בעולם - זה בלוקצ'יין. כדי שכולם יסכימו על מה כתוב בספר הזה בכל רגע נתון, ומי רשאי להוסיף עסקאות חדשות, חייב להיות מנגנון שיאפשר להם להגיע ל"קונצנזוס" - הסכמה משותפת - ללא צורך בסמכות מרכזית שתקבע. זהו התפקיד של מנגנוני הקונצנזוס, והם קובעים את הכללים למניעת רמאויות והבטחת אבטחת הרשת.</p>

    <h3>הוכחת עבודה (Proof-of-Work - PoW)</h3>
    <p>המנגנון הוותיק והמפורסם, שהושק לראשונה עם ביטקוין. הוא מבוסס על עיקרון פשוט אך גאוני: כדי לקבל את הזכות להוסיף בלוק חדש לשרשרת, עליך להוכיח שהשקעת "עבודה" חישובית משמעותית.</p>
    <ul>
        <li><strong>כיצד עובד מנגנון הכרייה (Mining):</strong> משתתפים ברשת (ה'כורים') מפעילים מחשבים רבי עוצמה בתחרות. הם מנסים לפתור "חידה" מתמטית-קריפטוגרפית שדורשת ניסוי וטעייה אינסופיים (חישובים רבים של פונקציית גיבוב - Hash). הראשון שמוצא את הפתרון הנכון מודיע על כך לרשת.</li>
        <li><strong>תפקיד ה-Hash והקושי החישובי:</strong> החידה היא למצוא ערך מסוים (Nonce) כך שהגיבוב (Hash) של הבלוק החדש (שמכיל עסקאות) יתאים לקריטריון מסוים שנקבע מראש (למשל, יתחיל במספר רב של אפסים). מציאת ה-Nonce הנכון היא אקראית לחלוטין ודורשת כוח חישוב עצום. הקושי של החידה מתעדכן אוטומטית כדי לשמור על קצב הוספת בלוקים יציב (כ-10 דקות בביטקוין).</li>
        <li><strong>תגמול:</strong> הכורה שפתר את החידה ראשון מקבל תגמול כפול: מטבעות קריפטו חדשים שנוצרו (כחלק מאינפלציה מתוכננת) ועמלות העסקאות שהיו בבלוק שהוסיף.</li>
        <li><strong>יתרונות:</strong>
            <ul>
                <li><strong>אבטחה מוכחת לאורך זמן:</strong> המנגנון פועל בהצלחה כבר למעלה מעשור ברשתות ענק.</li>
                <li><strong>עמידות גבוהה להתקפות (במיוחד התקפת 51%):</strong> ניסיון להשתלט על הרשת דורש שליטה ברוב (51%) מכוח החישוב העולמי - דבר יקר ומורכב כיום באופן כמעט בלתי אפשרי.</li>
            </ul>
        </li>
        <li><strong>חסרונות:</strong>
            <ul>
                <li><strong>צריכת אנרגיה מטורפת:</strong> התחרות העולמית על פתרון החידה צורכת כמויות חשמל עצומות, המשתוות לצריכה של מדינות קטנות. זהו החיסרון המרכזי והשנוי ביותר במחלוקת.</li>
                <li><strong>פוטנציאל לריכוזיות:</strong> כרייה הפכה לתעשייה דורשת ציוד יקר וגישה לחשמל זול, מה שהוביל לריכוזיות של כוח הכרייה בידי גופים גדולים ("חוות כרייה").</li>
            </ul>
        </li>
    </ul>

    <h3>הוכחת החזקה (Proof-of-Stake - PoS)</h3>
    <p>מנגנון אלטרנטיבי ויעיל יותר אנרגטית, שנמצא בשימוש גובר (כמו באת'ריום 2.0, סולאנה, קרדנו ועוד). כאן, הזכות לאמת בלוקים ולהרוויח תגמולים נקבעת לא לפי כוח חישוב, אלא לפי כמות המטבעות שהמשתמש "הפקיד" או "נע" (Staked) ברשת כבטוחה.</p>
    <ul>
        <li><strong>כיצד עובד מנגנון האימות (Validation) וההחזקה (Staking):</strong> משתמשים המעוניינים להשתתף בתהליך נועלים כמות מסוימת ממטבעות הרשת בחשבון מיוחד. בכך הם הופכים ל'מאמתים' (Validators). ההפקדה משמשת כבטוחה להתנהגות ישרה - אם ינסו לרמות, הם עלולים לאבד חלק או את כל ההחזקה שלהם (Slashing).</li>
        <li><strong>תהליך בחירת המאמת:</strong> בכל פעם שיש להוסיף בלוק חדש, אלגוריתם בוחר באופן אקראי (אך עם סיכויים פרופורציונליים לגודל ההחזקה) את אחד המאמתים שיציע את הבלוק. המאמת שנבחר מציע בלוק חדש (עם עסקאות), ורוב המאמתים האחרים מאשרים את תקינותו.</li>
        <li><strong>תגמול:</strong> המאמת שנבחר לאשר את הבלוק מקבל עמלות מהעסקאות שנכללו בו. בחלק מהרשתות יש גם תגמול נוסף של מטבעות חדשים (בדומה ל-PoW).</li>
        <li><strong>יתרונות:</strong>
            <ul>
                <li><strong>יעילות אנרגטית מדהימה:</strong> צורך כמויות אנרגיה זניחות לעומת PoW, מה שהופך אותו לידידותי הרבה יותר לסביבה.</li>
                <li><strong>קלות השתתפות:</strong> כל מי שמחזיק כמות מינימלית של מטבעות יכול להפוך למאמת (או להצטרף למאגר Staking), ללא צורך בציוד יקר.</li>
                <li><strong>פוטנציאל הרחבה (Scalability):</strong> נחשב לארכיטקטורה שמאפשרת יותר בקלות לשפר את מספר העסקאות בשנייה.</li>
            </ul>
        </li>
        <li><strong>חסרונות:</strong>
            <ul>
                <li><strong>סיכון לריכוזיות הון:</strong> מי שמחזיק בהרבה מטבעות יכול, תיאורטית, להגדיל משמעותית את הסיכוי שלו להיבחר ולהשפיע. מנגנונים מתוחכמים ברשתות PoS מנסים למנוע זאת.</li>
                 <li><strong>חדש יחסית ברשתות ענק:</strong> למרות שהוא קיים שנים, השימוש בו ברשתות בקנה מידה של את'ריום הוא חדש יחסית (אחרי ה-Merge).</li>
            </ul>
        </li>
    </ul>

    <h3>השוואה ראש בראש: PoW מול PoS</h3>
    <p>ההבדל המהותי הוא סוג ה"משאב" המושקע כדי להגן על הרשת ולקבוע מי יאשר את הבלוק הבא:</p>
    <ul>
        <li><strong>PoW:</strong> משקיע כוח חישוב פיזי (ואנרגיה) כדי לפתור חידה.</li>
        <li><strong>PoS:</strong> משקיע הון (מטבעות) כבטוחה, והבחירה אקראית לפי ההון.</li>
    </ul>
    <p><strong>אבטחה ויעילות:</strong> שניהם נועדו לספק אבטחה חזקה, אך בדרכים שונות. PoW מוכח לאורך זמן, בעוד PoS יעיל בהרבה אנרגטית ופוטנציאלית מהיר יותר.</p>
    <p><strong>צריכת אנרגיה:</strong> PoS מנצח בנוקאאוט - הוא צורך שבריר זניח מהאנרגיה שדורש PoW.</p>
    <p><strong>סיכוני ריכוזיות:</strong> בשני המנגנונים קיים סיכון לריכוזיות - ב-PoW על בסיס כוח חישוב, וב-PoS על בסיס הון. עיצובי הרשתות השונות כוללים מנגנונים לצמצום סיכונים אלו.</p>
    <p><strong>הבחירה במנגנון:</strong> תלויה במטרות הפרויקט. ביטקוין, כ"זהב דיגיטלי", מעדיף את האבטחה המוכחת של PoW. רשתות אפליקציות מבוזרות כמו את'ריום מעדיפות את היעילות וההתפתחות של PoS.</p>
</div>

<style>
    /* General Styles */
    body {
        font-family: 'Arial', sans-serif; /* Using standard font */
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        direction: rtl; /* Right-to-left */
        text-align: right; /* Align text right */
        background-color: #f8f9fa; /* Light background */
        color: #343a40; /* Dark gray text */
    }

    h1 {
        color: #0056b3; /* Deep blue */
        text-align: center;
        margin-bottom: 10px;
        font-size: 2.5em;
        font-weight: bold;
    }
     h2 {
         color: #007bff; /* Medium blue */
         text-align: center;
         margin-bottom: 15px;
         font-size: 2em;
         border-bottom: 2px solid #007bff;
         padding-bottom: 10px;
         display: inline-block; /* Shrink border to content */
         margin-left: auto; /* Center block element */
         margin-right: auto; /* Center block element */
     }
    h3 {
        color: #007bff; /* Medium blue */
        margin-top: 30px;
        margin-bottom: 15px;
        font-size: 1.6em;
        border-bottom: 1px solid #dee2e6;
        padding-bottom: 5px;
        text-align: right;
    }
    p {
        margin-bottom: 15px;
        font-size: 1.1em;
    }
    ul {
        margin-bottom: 15px;
        padding-right: 20px; /* RTL padding */
    }
    li {
        margin-bottom: 8px;
    }

    /* App Container */
    #app-container {
        background-color: #e9ecef; /* Light grey */
        padding: 30px;
        border-radius: 12px;
        margin-bottom: 30px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: right;
    }

    /* Controls */
    .controls {
        text-align: center;
        margin-bottom: 30px;
        padding: 15px;
        background-color: #d1e7dd; /* Light green */
        border-radius: 8px;
    }
    .controls button {
        padding: 12px 20px;
        margin: 0 8px;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        background-color: #ced4da; /* Grey */
        color: #495057; /* Dark grey text */
        font-size: 1.1em;
        transition: all 0.3s ease;
        min-width: 150px; /* Ensure buttons are wide enough */
    }
    .controls button.active {
        background-color: #28a745; /* Green */
        color: white;
        box-shadow: 0 2px 5px rgba(40, 167, 69, 0.5);
    }
    .controls button:not(.active):hover {
         background-color: #adb5bd; /* Darker grey on hover */
    }

    /* Simulation Sections */
    .simulation-section {
        border: 1px solid #ced4da; /* Light grey border */
        padding: 25px;
        margin-top: 25px;
        background-color: #ffffff; /* White background */
        border-radius: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.08);
    }
     .simulation-section h3 {
         text-align: center;
         margin-bottom: 20px;
         color: #007bff;
         border-bottom: none;
         padding-bottom: 0;
     }
    .simulation-section p strong {
        color: #0056b3;
    }

    /* Miners & Validators Containers */
    .miners-container, .validators-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 25px; /* Increased gap */
        margin-bottom: 30px;
        padding-top: 10px; /* Space above cards */
    }

    /* Miner/Validator Cards */
    .miner, .validator {
        border: 1px solid #ddd;
        padding: 20px; /* Increased padding */
        border-radius: 10px; /* More rounded corners */
        text-align: center;
        width: 140px; /* Slightly wider cards */
        background-color: #f8f9fa; /* Very light grey */
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* Add transitions */
        position: relative; /* For animations */
         overflow: hidden; /* Hide animation overflow */
    }

    .user-miner, .user-validator {
         border-color: #28a745; /* Green border */
         background-color: #eaf7ea; /* Light green background */
         box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
         transform: scale(1.05); /* Slightly larger */
    }
     .miner img, .validator img {
         width: 45px; /* Slightly larger icons */
         height: 45px;
         margin-bottom: 10px;
     }
     .miner p, .validator p {
         font-size: 1em;
         margin: 5px 0; /* Adjust spacing */
     }
     .miner-name, .validator-name {
         font-weight: bold;
         color: #0056b3;
         margin-bottom: 10px;
     }


    /* PoW Specific Styles */
    .attempts-container {
        margin-bottom: 10px;
    }
     .progress-bar {
         width: 100%;
         height: 8px;
         background-color: #e9ecef;
         border-radius: 4px;
         overflow: hidden;
         margin-top: 5px;
     }
    .progress {
        height: 100%;
        width: 0%;
        background-color: #007bff; /* Blue progress */
        transition: width 0.1s linear; /* Smooth progress animation */
    }

    .mine-button {
        display: block;
        width: 100%;
        padding: 10px;
        background-color: #007bff; /* Blue */
        color: white;
        border: none;
        border-radius: 20px; /* Rounded button */
        cursor: pointer;
        margin-top: 15px;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }
    .mine-button:not(:disabled):hover {
        background-color: #0056b3; /* Darker blue */
        transform: translateY(-2px);
    }
    .mine-button:disabled {
         background-color: #aaa;
         cursor: not-allowed;
    }

     .action-button {
        display: block;
        width: 250px; /* Wider buttons */
        margin: 20px auto; /* Center button and add more space */
        padding: 12px;
        background-color: #ffc107; /* Yellow/Orange */
        color: #212529; /* Dark text */
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
         text-align: center;
         font-size: 1.1em;
         transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 2px 5px rgba(255, 193, 7, 0.5);
     }
     .action-button:hover {
        background-color: #e0a800; /* Darker yellow */
        transform: translateY(-2px);
     }
    .action-button.stop-button {
        background-color: #dc3545; /* Red */
        color: white;
        box-shadow: 0 2px 5px rgba(220, 53, 69, 0.5);
    }
     .action-button.stop-button:hover {
        background-color: #c82333; /* Darker red */
     }
    .action-button:disabled {
         background-color: #aaa;
         cursor: not-allowed;
         box-shadow: none;
         transform: none;
    }


    /* PoS Specific Styles */
    .stake-control label {
         display: block;
         margin-bottom: 5px;
         font-size: 0.9em;
         color: #555;
    }
    .stake-slider {
        width: 100%;
        margin-top: 5px;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #007bff; /* Blue slider track */
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .stake-slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #0056b3; /* Dark blue thumb */
        cursor: pointer;
        border-radius: 50%;
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .stake-slider::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #0056b3;
        cursor: pointer;
        border-radius: 50%;
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
     .validator .reward { /* Specific reward style for PoS */
         color: #17a2b8; /* Teal */
     }

     /* Blockchain Display */
    .blockchain-pow, .blockchain-pos {
        margin-top: 30px;
    }
    .blockchain-display {
        display: flex;
        overflow-x: auto; /* Allow horizontal scrolling */
        padding: 15px 0; /* Add vertical padding for arrows */
        gap: 25px; /* Space between blocks */
        align-items: center; /* Vertically align blocks and arrows */
        border-top: 1px solid #eee;
        border-bottom: 1px solid #eee;
    }
    .block {
        flex: 0 0 auto;
        background-color: #17a2b8; /* Teal block color */
        color: white;
        padding: 18px 25px; /* More padding */
        border-radius: 8px; /* More rounded */
        min-width: 150px; /* Minimum width */
        text-align: center;
        white-space: pre-wrap; /* Allow wrapping lines (for two lines of text) */
        border: 1px solid #138496;
         position: relative;
        font-size: 1em;
        line-height: 1.4;
         opacity: 0; /* Start hidden for animation */
         transform: translateX(20px); /* Start off-screen for animation */
         animation: slideInBlock 0.5s ease-out forwards; /* Animation on add */
         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }

    .block.genesis-block {
        background-color: #6c757d; /* Grey for genesis */
        border-color: #5a6268;
        opacity: 1; /* Genesis block is visible initially */
        transform: none; /* No animation for genesis */
        animation: none;
    }

    .block::before {
        content: '➔'; /* Better arrow */
        position: absolute;
        left: -20px; /* Position the arrow between blocks */
        top: 50%;
        transform: translateY(-50%);
        color: #6c757d; /* Grey arrow color */
        font-size: 1.5em; /* Larger arrow */
        font-weight: bold;
         display: none; /* Hide arrow for the first block */
    }
     .blockchain-display .block:not(:first-child)::before {
         display: block; /* Show arrow for subsequent blocks */
     }

    @keyframes slideInBlock {
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    /* Animation for selected validator (PoS) */
    @keyframes pulseHighlight {
        0% { box-shadow: 0 0 0 0 rgba(0, 123, 255, 0.7); }
        70% { box-shadow: 0 0 0 15px rgba(0, 123, 255, 0); }
        100% { box-shadow: 0 0 0 0 rgba(0, 123, 255, 0); }
    }
    .validator.highlight {
        animation: pulseHighlight 1s ease-out;
    }
    .validator.chosen {
         border-color: #007bff; /* Blue border for chosen */
         background-color: #e0f7ff; /* Light blue background */
         box-shadow: 0 0 15px rgba(0, 123, 255, 0.5); /* Stronger blue shadow */
         transform: scale(1.1); /* Scale up slightly */
    }


    /* Explanation Toggle Button */
     #toggle-explanation {
         display: block;
         width: 300px; /* Wider button */
         margin: 30px auto;
         padding: 15px; /* More padding */
         background-color: #17a2b8; /* Teal */
         color: white;
         border: none;
         border-radius: 25px; /* Pill shape */
         cursor: pointer;
         text-align: center;
         font-size: 1.2em; /* Larger font */
          transition: background-color 0.3s ease, transform 0.1s ease;
          box-shadow: 0 2px 5px rgba(23, 162, 184, 0.5);
     }
     #toggle-explanation:hover {
         background-color: #138496; /* Darker teal */
          transform: translateY(-2px);
     }

    /* Explanation Section */
     #explanation {
         border-top: 2px solid #007bff; /* Blue separator */
         padding-top: 30px;
         margin-top: 30px;
         background-color: #ffffff;
         padding: 25px;
         border-radius: 12px;
         box-shadow: 0 4px 8px rgba(0,0,0,0.05);
     }
     #explanation h3 {
         margin-top: 20px;
         border-bottom: 1px solid #eee;
         padding-bottom: 5px;
         text-align: right;
         color: #343a40; /* Dark grey for text headings */
     }
     #explanation ul {
         margin-bottom: 15px;
     }
     #explanation li {
         margin-bottom: 8px;
         font-size: 1.05em;
     }
     #explanation strong {
         color: #0056b3;
     }

</style>

<script>
    // --- Element References ---
    const modePoWButton = document.getElementById('mode-pow');
    const modePoSButton = document.getElementById('mode-pos');
    const powSimulationDiv = document.getElementById('pow-simulation');
    const posSimulationDiv = document.getElementById('pos-simulation');
    const powBlockchainDisplay = document.getElementById('pow-blockchain-display');
    const posBlockchainDisplay = document.getElementById('pos-blockchain-display');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // PoW Elements
    const userMinerPoW = document.getElementById('user-miner-pow');
    const otherMinersPoW = [
        document.getElementById('other-miner-pow-1'),
        document.getElementById('other-miner-pow-2')
    ];
    const allMinersPoW = [userMinerPoW, ...otherMinersPoW];
    const userMineButton = userMinerPoW.querySelector('.mine-button');
    const autoMineButton = document.getElementById('auto-mine');
    const stopAutoMineButton = document.getElementById('stop-auto-mine');
    let powAttempts = { 'user-miner-pow': 0, 'other-miner-pow-1': 0, 'other-miner-pow-2': 0 };
    let powRewards = { 'user-miner-pow': 0, 'other-miner-pow-1': 0, 'other-miner-pow-2': 0 };
    let powMinerInterval = null;
    let powProgressIntervals = {}; // Track progress bar intervals

    // PoS Elements
    const userValidatorPoS = document.getElementById('user-validator-pos');
    const otherValidatorsPoS = [
         document.getElementById('other-validator-pos-1'),
         document.getElementById('other-validator-pos-2')
    ];
    const allValidatorsPoS = [userValidatorPoS, ...otherValidatorsPoS];
    const userStakeSlider = userValidatorPoS.querySelector('.stake-slider');
    const userStakeValueSpan = userValidatorPoS.querySelector('.stake-value');
    const startValidationButton = document.getElementById('start-validation');
     let posStakes = {
        'user-validator-pos': 100,
        'other-validator-pos-1': 200,
        'other-validator-pos-2': 50
     };
      let posRewards = {
        'user-validator-pos': 0,
        'other-validator-pos-1': 0,
        'other-validator-pos-2': 0
     };
     let posValidatorInterval = null;


    // --- Helper Functions ---
    function addBlock(blockchainDisplay, participantElementId) {
        const blockCount = blockchainDisplay.children.length;
        const newBlock = document.createElement('div');
        newBlock.classList.add('block');
        const mode = blockchainDisplay.id.includes('pow') ? 'PoW' : 'PoS';
        const participantName = mode === 'PoW' ? getMinerName(participantElementId) : getValidatorName(participantElementId);
        // Adding block details (simplified)
        newBlock.innerHTML = `<strong>בלוק ${blockCount}</strong><br>אושר ע"י ${participantName}`; // Use innerHTML for line break

        blockchainDisplay.appendChild(newBlock);

        // Animate adding block (CSS handles the initial animation class)
        // Scroll to the new block with a slight delay to allow animation
         setTimeout(() => {
            blockchainDisplay.scrollLeft = blockchainDisplay.scrollWidth;
        }, 100); // Scroll slightly after block appears
    }

    function getMinerName(minerElementId) {
         const miner = document.getElementById(minerElementId);
         return miner ? miner.querySelector('.miner-name').textContent : 'אלמוני';
    }

     function getValidatorName(validatorElementId) {
         const validator = document.getElementById(validatorElementId);
         return validator ? validator.querySelector('.validator-name').textContent : 'אלמוני';
    }


    function updatePoWDisplay() {
        allMinersPoW.forEach(miner => {
             const id = miner.id;
             miner.querySelector('.attempts').textContent = powAttempts[id];
             miner.querySelector('.reward').textContent = `תגמול: ${powRewards[id]} מטבעות`;
        });
    }

    function animatePoWAttempt(minerElementId, attemptsDelta) {
        const miner = document.getElementById(minerElementId);
        if (!miner) return;

        const progressBar = miner.querySelector('.progress');
        // Simulate progress reset and increment
        progressBar.style.transition = 'none'; // Remove transition for instant reset
        progressBar.style.width = '0%';

        // Force reflow to apply reset before starting animation
        void progressBar.offsetWidth;

        progressBar.style.transition = 'width 0.1s linear'; // Add transition back
        const currentAttempts = powAttempts[minerElementId];
        // Simulate progress based on attempts within a hypothetical block cycle (e.g., 100 attempts for 100%)
        // This is simplified - real PoW difficulty means attempts are huge numbers.
        // Here, we just show *some* progress to make it visual.
        const maxVisualAttempts = 50; // Attempts to reach full visual bar
        const progress = Math.min(100, (currentAttempts % maxVisualAttempts) / maxVisualAttempts * 100);
        progressBar.style.width = `${progress}%`;

        // Basic card pulse animation on attempt (subtle)
        miner.classList.remove('pulse'); // Reset animation
        void miner.offsetWidth; // Trigger reflow
        // Add back class conditionally or use a different animation
        // Let's skip pulse on *every* attempt in auto-mode, maybe just on manual or successful mine.

    }


     function updatePoSDisplay() {
        const allStakeValues = Object.values(posStakes);
        const overallMaxStake = Math.max(...allStakeValues, 10); // Avoid division by zero if all stakes are 0

        allValidatorsPoS.forEach(validator => {
             const id = validator.id;
             const stake = posStakes[id];
             validator.querySelector('.stake-value').textContent = stake;
             validator.querySelector('.reward').textContent = `סה"כ עמלות: ${posRewards[id]} מטבעות`;

             // Visual scaling based on stake relative to max stake
             const baseSize = 140; // Base width/height (from CSS)
             const scaleFactor = stake / overallMaxStake;
             // Interpolate size between baseSize and baseSize * 1.5
             const scaledSize = baseSize + (baseSize * 0.5 * scaleFactor);
             validator.style.width = `${scaledSize}px`;
             validator.style.height = `${scaledSize}px`;
             // Adjust font size and icon size proportionally but within limits
             const scaledFontSize = Math.max(1, 1 + (0.3 * scaleFactor)); // Font 1em to 1.3em
             validator.style.fontSize = `${scaledFontSize}em`;
             validator.querySelector('img').style.width = `${45 * (1 + 0.5 * scaleFactor)}px`;
             validator.querySelector('img').style.height = `${45 * (1 + 0.5 * scaleFactor)}px`;
        });
    }


    // --- PoW Logic ---
    function attemptPoW(minerElementId) {
        powAttempts[minerElementId]++;
        animatePoWAttempt(minerElementId, 1); // Animate progress bar for this miner

        const successChance = 0.005; // Make it a bit harder to find manually initially
        if (minerElementId === 'user-miner-pow' && !powMinerInterval) {
            // Manual attempt - slightly lower chance to encourage auto? Or same? Let's keep same.
            // successChance = 0.01; // Or adjust if needed
        } else if (powMinerInterval) {
             // Auto mining attempts - maybe higher chance overall distributed among miners?
             // Or simulate more attempts per interval. Let's stick to attempts count.
        }


        if (Math.random() < successChance) {
            // Solution found!
            console.log(`${getMinerName(minerElementId)} מצא פתרון! מוסיף בלוק...`);
            // Stop auto mining briefly so user can see winner
            if (powMinerInterval) {
                 stopPoWSimulation(); // Stop auto mining
                 // Restart after a delay to allow viewing winner
                 setTimeout(runPoWSimulation, 3000); // Restart after 3 seconds
            }


            addBlock(powBlockchainDisplay, minerElementId);
             powRewards[minerElementId] += 10; // Simulate reward
             // Reset attempts for all miners after a block is found
             Object.keys(powAttempts).forEach(key => powAttempts[key] = 0);

             // Visual feedback for the winning miner
             const winnerMiner = document.getElementById(minerElementId);
             winnerMiner.classList.add('chosen'); // Add a class for highlight animation
             setTimeout(() => {
                 winnerMiner.classList.remove('chosen'); // Remove class after animation
             }, 1000);


            updatePoWDisplay(); // Update numbers
            return true; // Indicate success
        }
         updatePoWDisplay(); // Update numbers even on failure
        return false; // Indicate failure
    }

    function runPoWSimulation() {
         console.log('החלה כרייה אוטומטית...');
         stopPoWSimulation(); // Ensure no duplicate intervals

         // Simulate attempts for all miners
        powMinerInterval = setInterval(() => {
             const allMinerIds = Object.keys(powAttempts);
             let blockFound = false;
             allMinerIds.forEach(minerId => {
                 if (!blockFound) { // Stop simulating attempts once a block is found
                      // Simulate a batch of attempts per interval for smoother visual updates
                      const attemptsPerInterval = 10; // Simulate 10 hash attempts per miner per interval
                     for(let i = 0; i < attemptsPerInterval; i++) {
                         if (attemptPoW(minerId)) {
                            blockFound = true;
                            // attemptPoW already stops/restarts interval
                            return; // Exit inner loop
                         }
                     }
                     // Update progress bar visually based on accumulated attempts
                     animatePoWAttempt(minerId, attemptsPerInterval);
                 }
             });
             if (!blockFound) {
                 updatePoWDisplay(); // Update attempts count if no block found
             }

        }, 200); // Simulate batches of attempts faster
    }

    function stopPoWSimulation() {
         console.log('עצירת כרייה אוטומטית.');
         if (powMinerInterval) {
             clearInterval(powMinerInterval);
             powMinerInterval = null;
         }
          // Stop progress bar animations if they are running separately
          Object.values(powProgressIntervals).forEach(interval => clearInterval(interval));
          powProgressIntervals = {};
           // Reset progress bars visually
          allMinersPoW.forEach(miner => {
               const progressBar = miner.querySelector('.progress');
               progressBar.style.transition = 'none';
               progressBar.style.width = '0%';
          });
    }

    userMineButton.addEventListener('click', () => {
         if (!userMineButton.disabled) {
              attemptPoW('user-miner-pow');
         }
    });

    autoMineButton.addEventListener('click', () => {
        if (!powMinerInterval) {
            runPoWSimulation();
            autoMineButton.style.display = 'none';
            stopAutoMineButton.style.display = 'block';
            userMineButton.disabled = true;
        }
    });

     stopAutoMineButton.addEventListener('click', () => {
        stopPoWSimulation();
        autoMineButton.style.display = 'block';
        stopAutoMineButton.style.display = 'none';
        userMineButton.disabled = false;
     });


    // --- PoS Logic ---
    function runPoSSimulation() {
         console.log('התחיל תהליך אימות אוטומטי (בחירת מאמת).');
         stopPoSSimulation(); // Ensure no duplicate intervals

         posValidatorInterval = setInterval(() => {
             console.log('מנסה לבחור מאמת לבלוק הבא...');
             const totalStake = Object.values(posStakes).reduce((sum, stake) => sum + stake, 0);
             if (totalStake === 0) {
                 console.warn('סה"כ החזקה הוא 0. לא ניתן לבחור מאמת.');
                 return;
             }

             // Animate validators before selection
             allValidatorsPoS.forEach(validator => {
                 validator.classList.add('highlight'); // Add pulse animation class
             });

             let winningStake = Math.random() * totalStake;
             let chosenValidatorId = null;
             let cumulativeStake = 0;

             // Determine winner based on weighted random selection
             const allValidatorIds = Object.keys(posStakes);
             // Shuffle IDs to make the visual "spin" feel more random
             allValidatorIds.sort(() => Math.random() - 0.5); // Simple shuffle

             // Use a slight delay to show the pulse before selecting
             setTimeout(() => {
                 for (const validatorId of allValidatorIds) {
                     cumulativeStake += posStakes[validatorId];
                     if (winningStake <= cumulativeStake) {
                         chosenValidatorId = validatorId;
                         break;
                     }
                 }

                 // Remove highlight from all
                 allValidatorsPoS.forEach(validator => {
                     validator.classList.remove('highlight');
                 });


                 if (chosenValidatorId) {
                     console.log(`המאמת שנבחר: ${getValidatorName(chosenValidatorId)}`);
                     addBlock(posBlockchainDisplay, chosenValidatorId);
                     posRewards[chosenValidatorId] += 5; // Simulate reward (fees)

                     // Highlight the chosen validator
                     const chosenValidatorElement = document.getElementById(chosenValidatorId);
                      chosenValidatorElement.classList.add('chosen');
                      setTimeout(() => {
                           chosenValidatorElement.classList.remove('chosen');
                      }, 1000); // Remove highlight after 1 second


                     updatePoSDisplay(); // Update display after block added and reward given
                 } else {
                      console.log('לא נבחר מאמת בסיבוב זה.');
                 }
             }, 1000); // Delay selection by 1 second to see animation


         }, 4000); // Attempt to validate block every 4 seconds (slightly slower than PoW simulation pace)
    }

    function stopPoSSimulation() {
         console.log('עצירת תהליך אימות.');
         if (posValidatorInterval) {
             clearInterval(posValidatorInterval);
             posValidatorInterval = null;
         }
         // Ensure no validators are stuck in highlight state
         allValidatorsPoS.forEach(validator => {
             validator.classList.remove('highlight', 'chosen');
         });
    }


    userStakeSlider.addEventListener('input', (event) => {
        const newStake = parseInt(event.target.value);
        posStakes['user-validator-pos'] = newStake;
        userStakeValueSpan.textContent = newStake;
         updatePoSDisplay(); // Update visuals based on new stake immediately
    });
    // Also update display when slider changes *after* release (optional, input is enough)
    // userStakeSlider.addEventListener('change', updatePoSDisplay);


     startValidationButton.addEventListener('click', () => {
        if (!posValidatorInterval) {
             runPoSSimulation();
             startValidationButton.textContent = 'תהליך אימות אוטומטי פועל...';
             startValidationButton.disabled = true;
             userStakeSlider.disabled = true; // Disable slider while simulation runs
         } else {
             // Allow stopping? The prompt didn't ask for a separate stop button for PoS,
             // just switching modes stops it. Let's stick to that.
             console.log('תהליך האימות כבר פועל.');
         }
     });


    // --- Mode Switching ---
    function switchMode(mode) {
        if (mode === 'pow') {
            modePoWButton.classList.add('active');
            modePoSButton.classList.remove('active');
            powSimulationDiv.style.display = 'block';
            posSimulationDiv.style.display = 'none';

            // Stop PoS simulation and reset UI
            stopPoSSimulation();
            userStakeSlider.disabled = false;
            startValidationButton.textContent = 'התחל תהליך בחירת מאמת!';
            startValidationButton.disabled = false;
            startValidationButton.classList.remove('stop-button'); // Ensure correct class


             // Restore PoW UI state based on whether auto-mining was on or off
             if(powMinerInterval) {
                 autoMineButton.style.display = 'none';
                 stopAutoMineButton.style.display = 'block';
                 userMineButton.disabled = true;
             } else {
                 autoMineButton.style.display = 'block';
                 stopAutoMineButton.style.display = 'none';
                 userMineButton.disabled = false;
             }


        } else if (mode === 'pos') {
            modePoSButton.classList.add('active');
            modePoWButton.classList.remove('active');
            posSimulationDiv.style.display = 'block';
            powSimulationDiv.style.display = 'none';

            // Stop PoW simulation and reset UI
            stopPoWSimulation();
             autoMineButton.style.display = 'block';
             stopAutoMineButton.style.display = 'none';
             userMineButton.disabled = false;


            // Restore PoS UI state based on whether simulation was on or off
             if(posValidatorInterval) {
                 startValidationButton.textContent = 'תהליך אימות אוטומטי פועל...';
                 startValidationButton.disabled = true;
                 startValidationButton.classList.add('stop-button'); // Visually indicate running
                 userStakeSlider.disabled = true;
             } else {
                startValidationButton.textContent = 'התחל תהליך בחירת מאמת!';
                 startValidationButton.disabled = false;
                 startValidationButton.classList.remove('stop-button'); // Ensure correct class
                 userStakeSlider.disabled = false;
             }
        }
         // Update displays after switching
         updatePoWDisplay();
         updatePoSDisplay();
    }

    modePoWButton.addEventListener('click', () => switchMode('pow'));
    modePoSButton.addEventListener('click', () => switchMode('pos'));

    // --- Explanation Toggle ---
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        // Use transitions for smoother toggle (requires height/max-height animation in CSS if possible, or just fade/display)
        // Simple display toggle is kept for strict CSS separation
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'רוצים להבין לעומק? לחצו כאן להסבר מלא';
    });

    // Initial state setup (start in PoW mode, update displays)
    switchMode('pow'); // This also calls updatePoWDisplay and updatePoSDisplay
    // Initial PoS display update call is redundant if switchMode is called first.
    // Keeping it here just in case initial switchMode doesn't fully render everything before the call.
    updatePoSDisplay(); // Ensure PoS visual stake is set on load even if hidden
</script>
```