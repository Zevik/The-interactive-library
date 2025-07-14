---
title: "הסוד המרתק של שווקי האספנות"
english_slug: the-secret-value-of-collectibles
category: "מדעי החברה / כלכלה התנהגותית"
tags: [אספנות, כלכלה, שווקים, הטיות קוגניטיביות, ערך, השקעה, פסיכולוגיה]
---
# הסוד המרתק של שווקי האספנות

למה חתיכת נייר ישנה או פיסת מתכת פשוטה יכולות להיות שוות הון? זה לא בגלל השימוש בהן היום, אלא בגלל סיפורים, נדירות... והפסיכולוגיה המורכבת שלנו. היכנסו לסימולטור ותתנסו בעצמכם: קנו, מכרו, והבינו איך עובד עולם שבו ערך נוצר מתוך תשוקה, היסטוריה, ולפעמים גם קצת הייפ פרוע. האם תצליחו להגדיל את ההון שלכם?

<div id="simulator" class="game-container">
    <h2 class="game-title">סימולטור אספנות: המסע אחר הערך</h2>
    <div class="controls-panel">
        <label for="item-type" class="control-label">בחר עולם אספנות:</label>
        <select id="item-type" class="control-select">
            <option value="stamps">בולים היסטוריים</option>
            <option value="coins">מטבעות עתיקים</option>
            <option value="cards">קלפי אספנות (טרנדיים)</option>
        </select>
        <button id="start-sim" class="control-button primary">התחל מסע</button>
        <button id="stop-sim" class="control-button secondary" disabled>עצור מסע</button>
         <span id="day-counter" class="day-counter">יום: 0</span>
    </div>
    <div class="stats-panel">
        <div class="stat-box">
            <h3>💰 תקציב</h3>
            <span id="budget" class="stat-value">0</span> ש"ח
        </div>
        <div class="stat-box">
            <h3>💎 שווי מלאי</h3>
            <span id="inventory-value" class="stat-value">0</span> ש"ח
        </div>
         <div class="stat-box goal-box">
            <h3>🎯 יעד</h3>
            <span id="goal-text">להגיע ל-10,000 ש"ח שווי כולל!</span>
        </div>
    </div>
     <div id="messages" class="messages-feed">
        <!-- Messages appear here -->
    </div>
    <div id="items-list" class="market-items-list">
        <h3>שוק האספנות פעיל!</h3>
        <p>בחר עולם אספנות והתחל את המסע כדי לראות פריטים.</p>
        <!-- Items will be rendered here -->
    </div>
    <div id="game-over-message" class="game-over-message"></div>
</div>

<style>
    /* כללי */
    :root {
        --primary-color: #4CAF50; /* ירוק - צמיחה */
        --secondary-color: #2196F3; /* כחול - יציבות */
        --accent-color: #FFC107; /* צהוב - זהב/נדירות */
        --danger-color: #F44336; /* אדום - ירידה */
        --background-color: #e8f5e9; /* ירוק בהיר רקע */
        --card-background: #ffffff;
        --border-color: #a5d6a7; /* ירוק בהיר גבול */
        --text-color: #333;
        --subtle-text-color: #555;
        --message-info-bg: #fff9c4; /* צהוב בהיר הודעות */
        --message-event-bg: #ffe0b2; /* כתום בהיר הודעות אירוע */
    }

    body {
        font-family: 'Arial', sans-serif;
        background-color: var(--background-color);
        color: var(--text-color);
        line-height: 1.6;
        padding-bottom: 40px; /* רווח למטה לפני ההסבר */
    }

    h1, h2, h3 {
        color: #1b5e20; /* ירוק כהה לכותרות */
    }

    /* מיכל הסימולטור הראשי */
    #simulator {
        max-width: 900px;
        margin: 30px auto;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--card-background);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        position: relative; /* להכיל הודעת סיום משחק */
    }

    .game-title {
        text-align: center;
        margin-top: 0;
        margin-bottom: 25px;
        font-size: 2em;
        color: #1b5e20;
    }

    /* פאנלים (פקדים, נתונים) */
    .controls-panel, .stats-panel {
        margin-bottom: 25px;
        padding: 15px 20px;
        border-bottom: 1px solid var(--border-color);
        background-color: #f1f8e9; /* ירוק בהיר עדין לרקע פאנל */
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    .controls-panel {
        display: flex;
        align-items: center;
        gap: 15px;
        flex-wrap: wrap; /* לאפשר מעבר שורה במסכים קטנים */
    }

    .control-label {
        font-weight: bold;
        color: var(--subtle-text-color);
    }

    .control-select, .control-button {
        padding: 10px 15px;
        border-radius: 5px;
        font-size: 1em;
        cursor: pointer;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

    .control-select {
        border: 1px solid var(--border-color);
        background-color: #ffffff;
    }

    .control-button {
        border: none;
        color: white;
        font-weight: bold;
    }

    .control-button.primary {
        background-color: var(--primary-color);
    }

    .control-button.primary:hover:not(:disabled) {
        background-color: #388E3C; /* ירוק כהה יותר בהובר */
         transform: translateY(-1px);
    }

     .control-button.secondary {
        background-color: var(--secondary-color);
    }

     .control-button.secondary:hover:not(:disabled) {
        background-color: #1976D2; /* כחול כהה יותר בהובר */
         transform: translateY(-1px);
    }

    .control-button:disabled {
        background-color: #bdbdbd; /* אפור ללחצנים לא פעילים */
        cursor: not-allowed;
    }

     .day-counter {
        margin-left: auto; /* דוחף את הדלפק לימין בפלקסבוקס */
        font-size: 1.1em;
        font-weight: bold;
        color: #004d40; /* ירוק-כחול כהה */
     }


    .stats-panel {
        display: flex;
        justify-content: space-around; /* רווח שווה בין תיבות הסטטיסטיקה */
        flex-wrap: wrap;
        gap: 15px;
    }

    .stat-box {
        text-align: center;
         flex-grow: 1; /* מאפשר להם לגדול */
        min-width: 150px; /* מונע התכווצות יתר */
    }

    .stat-box h3 {
        margin: 0 0 8px 0;
        font-size: 1em;
        color: var(--subtle-text-color);
    }

    .stat-value {
        font-size: 1.8em;
        font-weight: bold;
        color: var(--primary-color);
        transition: color 0.3s ease; /* אנימציה לצבע הנתון */
    }

     .stat-value.pulsing {
        animation: pulseEffect 0.5s ease-out;
     }


    /* עדכוני הודעות */
    .messages-feed {
        margin-top: 25px;
        padding: 15px;
        border: 2px dashed var(--accent-color); /* מסגרת צהובה מקווקוות */
        background-color: var(--message-info-bg);
        max-height: 150px; /* הגבלת גובה */
        overflow-y: auto; /* גלילה אם יש יותר מדי הודעות */
        font-size: 0.9em;
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    .message {
        margin-bottom: 10px;
        padding-bottom: 8px;
        border-bottom: 1px dotted #ccc; /* קו מפריד דק בין הודעות */
        opacity: 0; /* התחלה עם שקיפות 0 */
        animation: fadeInMessage 0.5s ease-out forwards; /* אנימציה להופעה */
        color: var(--subtle-text-color);
    }

     .message:last-child {
        border-bottom: none; /* אין קו אחרי ההודעה האחרונה */
     }

    /* רשימת פריטי השוק */
    .market-items-list {
        margin-top: 25px;
    }

     .market-items-list h3 {
        margin-bottom: 15px;
        color: #1b5e20;
     }

    .item {
        border: 1px solid var(--border-color);
        padding: 15px 20px;
        margin-bottom: 15px;
        border-radius: 8px;
        background-color: var(--card-background);
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap; /* לאפשר מעבר שורה במסכים קטנים */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
         transition: transform 0.2s ease; /* אנימציה קלה בהובר */
    }

     .item:hover {
        transform: translateY(-2px);
     }

    .item-details {
        flex-grow: 1;
        margin-right: 20px; /* רווח בין פרטים ולחצנים */
        min-width: 250px; /* מונע התכווצות יתר */
    }

    .item-details h4 {
        margin: 0 0 5px 0;
        font-size: 1.1em;
        color: #333;
    }

    .item-details p {
        margin: 3px 0;
        font-size: 0.9em;
        color: var(--subtle-text-color);
    }

    .item-actions {
        display: flex;
        align-items: center;
        gap: 10px;
         margin-top: 10px; /* רווח אם הפריטים עברו שורה */
    }

    .item-actions button {
        padding: 8px 12px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 0.9em;
        font-weight: bold;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

    .item-actions button:first-of-type { /* קנה */
        background-color: var(--primary-color);
        color: white;
    }
     .item-actions button:first-of-type:hover {
        background-color: #388E3C;
     }

    .item-actions button:last-of-type { /* מכור */
        background-color: var(--danger-color);
        color: white;
    }
     .item-actions button:last-of-type:hover {
        background-color: #D32F2F;
     }

     .item-actions button:disabled {
        background-color: #bdbdbd;
        cursor: not-allowed;
     }


    .value-info {
        display: flex;
        align-items: center;
        font-weight: bold;
        margin-top: 5px;
    }

    .value-change {
        font-weight: normal; /* עובי גופן רגיל לשינוי */
        margin-left: 8px;
        font-size: 0.85em;
         transition: color 0.3s ease; /* אנימציה לצבע השינוי */
    }

    .value-up {
        color: var(--primary-color); /* ירוק לעלייה */
    }

    .value-down {
        color: var(--danger-color); /* אדום לירידה */
    }

    /* אנימציות */
    @keyframes fadeInMessage {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

     @keyframes pulseEffect {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
     }


    /* לחצן והסבר */
    #explanation-button {
        display: block;
        margin: 40px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 8px;
        background-color: #0277bd; /* כחול כהה יותר */
        color: white;
        font-weight: bold;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
     #explanation-button:hover {
        background-color: #01579b;
        transform: translateY(-1px);
     }


    #explanation {
        margin-top: 20px;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--card-background);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        display: none; /* Hidden by default */
        transition: all 0.5s ease-in-out; /* אנימציה להופעה/הסתרה */
    }

    #explanation h2, #explanation h3 {
        color: #1b5e20;
    }

    #explanation p {
        line-height: 1.7;
        color: var(--text-color);
        margin-bottom: 15px;
    }

    #explanation ul {
        list-style-type: disc;
        margin-left: 30px;
        padding-left: 0;
    }

    #explanation li {
        margin-bottom: 12px;
        color: var(--text-color);
    }

     /* Game Over Overlay */
    .game-over-message {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.7);
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-size: 2em;
        font-weight: bold;
        z-index: 10;
        border-radius: 12px;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.5s ease-in-out, visibility 0.5s ease-in-out;
    }

     .game-over-message.visible {
        opacity: 1;
        visibility: visible;
     }

     .game-over-message p {
        margin: 10px 0;
     }

    /* רספונסיביות בסיסית */
    @media (max-width: 600px) {
        .controls-panel, .stats-panel, .item {
            flex-direction: column;
            align-items: stretch;
        }
        .controls-panel {
            gap: 10px;
        }
        .control-label {
            margin-bottom: 5px;
        }
         .day-counter {
            margin-left: 0; /* לבטל דחיפה לימין במסכים קטנים */
            text-align: center;
         }
        .stats-panel {
            gap: 10px;
        }
        .stat-box {
            min-width: unset;
        }
        .item-details {
            margin-right: 0;
            margin-bottom: 10px;
        }
        .item-actions {
             justify-content: center; /* מרכז את הלחצנים */
        }
    }


</style>

<button id="explanation-button">לגלות את סוד הערך מאחורי הקלעים</button>

<div id="explanation">
    <h2>סוד הערך של האספנות: מסע אל מעבר לשימושיות</h2>

    <h3>איך מחיר "רגיל" עובד? עולם היצע וביקוש</h3>
    <p>ברוב השווקים שאנחנו מכירים - שוק ירקות, חנויות בגדים, שירותי תיקונים - המחיר של מוצר או שירות נקבע בעיקר על ידי שיווי משקל בין ההיצע (כמה יש מהמוצר או השירות) לביקוש (כמה אנשים רוצים ומוכנים לשלם עבורו). גורמים כמו עלות ייצור, זמינות חומרי גלם ויעילות תהליכים משפיעים על ההיצע. טרנדים, צרכים וחלופות משפיעים על הביקוש. זה בדרך כלל תהליך הגיוני למדי שמבוסס על שימושיות ויעילות.</p>

    <h3>ברוכים הבאים לעולם האספנות - חוקים שונים לחלוטין!</h3>
    <p>תשכחו משימושיות או עלות ייצור. בשוק האספנות, הערך נובע ממקורות אחרים, לעיתים קסומים יותר:</p>
    <ul>
        <li><strong>נדירות אולטימטיבית:</strong> הדבר החשוב ביותר! ככל שמפריט מסוים נוצר במספר קטן יותר של עותקים, או שמעט שרדו את מבחן הזמן - כך ערכו מזנק. פריט "אחד יחיד במינו" (1 of 1) יכול לשבור שיאי מחיר.</li>
        <li><strong>מצב פיזי (הקונדיציה קובעת):</strong> שריטה קטנה, קיפול או שינוי צבע יכולים להוריד את ערך הפריט בצורה דרסטית. אספנים מחפשים את המצב המושלם (Mint Condition), ומוכנים לשלם עליו פרמיה עצומה. דירוג מקצועי של מצב הפריט (Grading) הוא תעשייה בפני עצמה.</li>
        <li><strong>הסיפור שמאחוריו (הנרטיב):</strong> מי החזיק בפריט? לאיזה אירוע היסטורי הוא קשור? האם יש לו סיפור רקע ייחודי ומעניין? נרטיב חזק הופך פריט למבוקש ומעלה את מחירו, הרבה מעבר לנדירות או מצב בלבד. תחשבו על חפץ שהיה שייך למלך, לאומן מפורסם או קשור לרגע מכונן בהיסטוריה.</li>
        <li><strong>אותנטיות ומוניטין:</strong> בשוק שבו זיופים נפוצים, היכולת להוכיח שהפריט אמיתי (באמצעות תעודות, היסטוריית בעלים, בדיקות מומחים) חיונית. פריט עם מוניטין מוכח או שמקורו ידוע ואמין יהיה שווה יותר.</li>
    </ul>

    <h3>הביקוש הלא רציונלי: תשוקה, נוסטלגיה ופחד</h3>
    <p>היצע וביקוש עדיין פועלים, אבל הביקוש בשוק האספנות שונה. הוא מונע לא רק מצורך, אלא מתשוקה, נוסטלגיה, הרצון להשלים סדרה, להיות חלק מקהילה, או פשוט להחזיק במשהו מיוחד שאין לאחרים. זהו ביקוש רגשי, פסיכולוגי, שקל יותר להשפיע עליו על ידי "הייפ" (באז תקשורתי), טרנדים חולפים ורגשות כמו פחד מהחמצה (FOMO - Fear Of Missing Out) שדוחפים אנשים לקנות מהר ובכל מחיר.</p>

    <h3>השקעה או תחביב? לשניהם מקום</h3>
    <p>עבור רוב האספנים, מדובר קודם כל בתחביב מרתק – אהבה לפריטים, הנאה מהחיפוש, הסיפוק מהאוסף. אבל הפוטנציאל הכלכלי תמיד קיים. עבור אחרים, זו השקעה לכל דבר, עם מטרה ברורה של רווח. אספנים "חכמים" משלבים בין השניים: הם נהנים מהתחביב אבל גם לומדים את השוק, מבינים את גורמי הערך, ומנסים לקבל החלטות מושכלות של קנייה ומכירה, תוך מודעות להטיות הפסיכולוגיות שיכולות להשפיע עליהם ועל השוק כולו.</p>
</div>

<script>
    const state = {
        initialBudget: 5000,
        budget: 0,
        inventory: [], // { id: 'item-id', boughtValue: price }
        availableItems: [],
        time: 0,
        intervalId: null,
        simulationRunning: false,
        itemTypesData: {
            stamps: [
                { id: 's001', name: 'בול דואר 1948 (מדינה בדרך)', rarity: 'rare', condition: 'mint', baseValue: 500, trend: 'stable', description: 'הבול הראשון של המדינה הצעירה, סמל היסטורי.' },
                { id: 's002', name: 'בול קק"ל היסטורי (שימוש יומיומי)', rarity: 'uncommon', condition: 'used', baseValue: 150, trend: 'up', description: 'שימש לתשלום על אדמות, נושא ניחוח תקופתי.' },
                { id: 's003', name: 'גיליון בולים יום העצמאות (שנות ה-60)', rarity: 'common', condition: 'mint', baseValue: 50, trend: 'stable', description: 'גיליון שלם וחגיגי, נפוץ אך אהוב.' },
                { id: 's004', name: 'בול שגיאת צבע נדירה (1 מ-1000)', rarity: 'very rare', condition: 'fine', baseValue: 2500, trend: 'stable', description: 'פספוס של המדפיס שהפך ללהיט אספנות.' },
                { id: 's005', name: 'סדרת בולים זואולוגיה (פשוטה)', rarity: 'common', condition: 'mint', baseValue: 80, trend: 'down', description: 'סדרה מקסימה, אבל הודפסה בכמויות אדירות.' },
                { id: 's006', name: 'בול תקופת המנדט (פגום קלות)', rarity: 'rare', condition: 'used', baseValue: 300, trend: 'stable', description: 'שריד לתקופה קודמת, מעניין היסטורית.' },
                 { id: 's007', name: 'בול זיכרון אירוע מיוחד', rarity: 'uncommon', condition: 'mint', baseValue: 180, trend: 'up', description: 'יצא לרגל אירוע נשכח, מתחיל לצבור עניין מחדש.' },
            ],
            coins: [
                { id: 'c001', name: 'מטבע 10 לירות 1970 (שימוש רגיל)', rarity: 'uncommon', condition: 'circulated', baseValue: 200, trend: 'stable', description: 'מטבע ששימש ביום יום, עם ערך נוסטלגי.' },
                { id: 'c002', name: 'פרוטה ארץ ישראלית (מנדט) (שמור היטב)', rarity: 'rare', condition: 'very fine', baseValue: 800, trend: 'up', description: 'פיסת היסטוריה קטנה מתקופת המנדט הבריטי.' },
                { id: 'c003', name: 'אגורה ישראלית מוקדמת (שחוקה)', rarity: 'common', condition: 'damaged', baseValue: 30, trend: 'stable', description: 'האגורה הראשונה, שחוקה מרוב שימוש.' },
                { id: 'c004', name: 'מטבע זיכרון מיוחד (יציאה לגימלאות)', rarity: 'uncommon', condition: 'mint', baseValue: 120, trend: 'down', description: 'הונפק לאירוע ספציפי, לא נדיר במיוחד.' },
                { id: 'c005', name: 'לירה ישראלית כסף (מהדורה מוגבלת)', rarity: 'very rare', condition: 'mint', baseValue: 3000, trend: 'stable', description: 'מטבע יפהפה מכסף טהור, נדיר ומבוקש.' },
                 { id: 'c006', name: 'שקל ישן נדיר (טעות הטבעה)', rarity: 'rare', condition: 'fine', baseValue: 600, trend: 'up', description: 'טעות קטנה בהטבעה יצרה פריט אספנות יקר ערך.' },
                 { id: 'c007', name: '5 לירות כסף (שנות ה-50)', rarity: 'rare', condition: 'very fine', baseValue: 900, trend: 'stable', description: 'מטבע גדול וכבד מתקופה מוקדמת.' },
            ],
            cards: [
                { id: 'k001', name: 'קלף פוקימון הולוגרפי נדיר (דור ראשון)', rarity: 'rare', condition: 'mint', baseValue: 700, trend: 'stable', description: 'קלף מיתולוגי ששיגע את העולם, במצב מושלם.' },
                { id: 'k002', name: 'קלף קסם: סדרה מוקדמת (משוחק)', rarity: 'uncommon', condition: 'played', baseValue: 180, trend: 'up', description: 'קלף משחק עם היסטוריה, מתחיל לצבור ערך.' },
                { id: 'k003', name: 'קלף ספורט שחקן ידוע (נפוץ)', rarity: 'common', condition: 'mint', baseValue: 60, trend: 'stable', description: 'קלף של שחקן פופולרי, הודפס הרבה ממנו.' },
                { id: 'k004', name: 'קלף אספנות אומנותי (יצירת מופת)', rarity: 'very rare', condition: 'mint', baseValue: 4000, trend: 'stable', description: 'קלף מעוצב להפליא במהדורה מוגבלת ביותר.' },
                { id: 'k005', name: 'קלף מסדרה ישנה (פגום קשות)', rarity: 'uncommon', condition: 'damaged', baseValue: 50, trend: 'down', description: 'שרוט, מקופל, אך עדיין פריט היסטורי למי שלא מבריר.' },
                 { id: 'k006', name: 'קלף פרומו מיוחד (מהדורה ראשונה)', rarity: 'rare', condition: 'mint', baseValue: 900, trend: 'up', description: 'קלף שחולק באירוע נדיר, מבוקש בקרב אספנים.' },
                 { id: 'k007', name: 'קלף של יוטיובר מפורסם (הייפ)', rarity: 'rare', condition: 'mint', baseValue: 1500, trend: 'up', description: 'טרנד חדש שהפך קלף פשוט ליקר בטירוף! כמה זמן זה יחזיק?' },
            ]
        },
        rarityMultipliers: { 'common': 1, 'uncommon': 1.5, 'rare': 3, 'very rare': 6 },
        conditionMultipliers: { 'damaged': 0.5, 'played': 0.8, 'circulated': 0.9, 'fine': 1.2, 'very fine': 1.5, 'mint': 2 },
        trendEffects: { 'up': 1.02, 'stable': 1.00, 'down': 0.99 }, // Daily multiplier
        trendChangeChance: 0.07, // 7% chance for a random item's trend to change each cycle
        eventChance: 0.12, // 12% chance for a random event each cycle
        gameOverGoal: 10000,
        maxDays: 50, // Limit simulation duration
    };

    const dom = {
        budgetSpan: document.getElementById('budget'),
        inventoryValueSpan: document.getElementById('inventory-value'),
        itemsListDiv: document.getElementById('items-list'),
        messagesDiv: document.getElementById('messages'),
        itemTypeSelect: document.getElementById('item-type'),
        startSimButton: document.getElementById('start-sim'),
        stopSimButton: document.getElementById('stop-sim'),
        explanationButton: document.getElementById('explanation-button'),
        explanationDiv: document.getElementById('explanation'),
        dayCounterSpan: document.getElementById('day-counter'),
        gameOverMessageDiv: document.getElementById('game-over-message'),
        goalTextSpan: document.getElementById('goal-text'),
    };

    function calculateCurrentValue(item) {
        let value = item.baseValue * state.rarityMultipliers[item.rarity] * state.conditionMultipliers[item.condition];
        // Apply trend effect over time
        value *= Math.pow(state.trendEffects[item.trend], state.time / 5); // Scale trend effect by time progression

        // Add random fluctuation (up to +/- 4%)
        value *= (1 + (Math.random() - 0.5) * 0.08);

         // Apply and fade event effect
        if (item.eventEffect) {
             value *= item.eventEffect;
             // Fade effect gradually
             item.eventEffect = item.eventEffect > 1 ? Math.max(1, item.eventEffect * 0.95) : Math.min(1, item.eventEffect * 1.05); // Fade towards 1
             if (Math.abs(item.eventEffect - 1) < 0.01) {
                 delete item.eventEffect; // Remove effect if close to 1
             }
        }
        return Math.max(1, Math.round(value)); // Ensure value is at least 1
    }

    function updateItemValues() {
        state.availableItems.forEach(item => {
            item.previousValue = item.currentValue || calculateCurrentValue(item);
            item.currentValue = calculateCurrentValue(item);
        });

        // Occasional random trend change
        if (Math.random() < state.trendChangeChance) {
            const randomItem = state.availableItems[Math.floor(Math.random() * state.availableItems.length)];
            const trends = Object.keys(state.trendEffects);
            const oldTrend = randomItem.trend;
            randomItem.trend = trends[Math.floor(Math.random() * trends.length)];
             addMessage(`📈 שוק משתנה: הטרנד עבור "${randomItem.name}" השתנה מ"${oldTrend}" ל"${randomItem.trend}"!`, 'event');
        }
    }

     function triggerRandomEvent() {
        if (Math.random() < state.eventChance) {
            const randomItem = state.availableItems[Math.floor(Math.random() * state.availableItems.length)];
            const eventType = Math.random();
            let effect = 1;
            let message = `📰 חדשות מהשוק: `;
            let messageType = 'event';

            if (eventType < 0.25) { // Negative event (25%)
                effect = 0.6 + Math.random() * 0.3; // Value drops 10-40%
                message += `נגלו זיופים רבים של פריטים דומים ל"${randomItem.name}". האמון צונח! הערך יורד!`;
            } else if (eventType < 0.55) { // Positive event (30%)
                effect = 1.25 + Math.random() * 0.5; // Value jumps 25-75%
                message += `פריט "${randomItem.name}" הוצג בתוכנית טלוויזיה פופולרית! הביקוש מזנק!`;
            } else if (eventType < 0.75) { // Mild positive event (20%)
                 effect = 1.1 + Math.random() * 0.2; // Value jumps 10-20%
                 message += `אספן מפורסם רכש פריט "${randomItem.name}" במכירה פומבית! עניין גובר בשוק!`;
             } else { // Mild negative event (25%)
                 effect = 0.8 + Math.random() * 0.15; // Value drops 5-20%
                 message += `פורסמה הערכת שווי נמוכה מהצפוי עבור פריטים מסוג "${randomItem.name}". הערך יורד מעט.`;
             }
             randomItem.eventEffect = effect;
             addMessage(message, messageType);
        }
     }


    function renderItems() {
        const itemsListHtml = state.availableItems.map(item => {
            const change = item.currentValue - (item.previousValue || item.currentValue);
            const valueChangeClass = change > 0 ? 'value-up' : (change < 0 ? 'value-down' : '');
            const valueChangeText = change > 0 ? `(+${change} ש"ח)` : (change < 0 ? `(${change} ש"ח)` : '');
            const inventoryCount = state.inventory.filter(invItem => invItem.id === item.id).length;

            return `
                <div class="item" data-item-id="${item.id}">
                    <div class="item-details">
                        <h4>${item.name}</h4>
                        <p>${item.description}</p>
                        <p><strong>נדירות:</strong> ${item.rarity}, <strong>מצב:</strong> ${item.condition}</p>
                         <div class="value-info">
                            <span><strong>ערך נוכחי:</strong> ${item.currentValue} ש"ח</span>
                             <span class="value-change ${valueChangeClass}">${valueChangeText}</span>
                         </div>
                    </div>
                    <div class="item-actions">
                        <button onclick="buyItem('${item.id}')" ${state.budget < item.currentValue ? 'disabled' : ''}>קנה (${item.currentValue} ש"ח)</button>
                        <button onclick="sellItem('${item.id}')" ${inventoryCount === 0 ? 'disabled' : ''}>מכור (${item.currentValue} ש"ח)</button>
                        <span>במלאי: ${inventoryCount}</span>
                    </div>
                </div>
            `;
        }).join('');
        dom.itemsListDiv.innerHTML = `<h3>פריטים זמינים בשוק:</h3>${itemsListHtml}`;

         // Trigger animation for value changes
        state.availableItems.forEach(item => {
            const itemElement = dom.itemsListDiv.querySelector(`.item[data-item-id="${item.id}"]`);
            if (itemElement) {
                const valueSpan = itemElement.querySelector('.value-info span:first-child');
                 const changeSpan = itemElement.querySelector('.value-change');
                if (item.previousValue && item.currentValue !== item.previousValue) {
                     // Add a temporary class to trigger CSS animation/transition
                     valueSpan.style.transition = 'color 0.3s ease';
                     if (item.currentValue > item.previousValue) {
                         valueSpan.style.color = var_primary_color; /* ירוק */
                     } else {
                          valueSpan.style.color = var_danger_color; /* אדום */
                     }

                    // Reset color after animation
                    setTimeout(() => {
                         valueSpan.style.color = ''; // Reset to default text color
                         valueSpan.style.transition = ''; // Remove transition after effect
                    }, 500); // Match CSS transition duration
                }
            }
        });
    }

    function renderStats() {
        dom.budgetSpan.textContent = state.budget.toFixed(0);
        const inventoryValue = state.inventory.reduce((sum, item) => {
            const currentItemData = state.availableItems.find(availItem => availItem.id === item.id);
            return sum + (currentItemData ? currentItemData.currentValue : 0);
        }, 0);
        dom.inventoryValueSpan.textContent = inventoryValue.toFixed(0);
        dom.dayCounterSpan.textContent = `יום: ${state.time}`;

        // Simple pulsing effect for stats on change (optional, requires CSS animation class)
        // dom.budgetSpan.classList.add('pulsing');
        // dom.inventoryValueSpan.classList.add('pulsing');
        // setTimeout(() => {
        //      dom.budgetSpan.classList.remove('pulsing');
        //      dom.inventoryValueSpan.classList.remove('pulsing');
        // }, 500);
    }

     function addMessage(msg, type = 'info') {
        const msgElement = document.createElement('p');
        msgElement.classList.add('message');
         msgElement.classList.add(type); // Add type class for potential styling
        msgElement.textContent = `[יום ${state.time}] ${msg}`;
        dom.messagesDiv.prepend(msgElement); // Add to top

         // Limit message count
        while (dom.messagesDiv.children.length > 15) {
            dom.messagesDiv.removeChild(dom.messagesDiv.lastChild);
        }
    }

    function buyItem(itemId) {
        const itemToBuy = state.availableItems.find(item => item.id === itemId);
        if (!itemToBuy) return;

        const price = itemToBuy.currentValue;
        if (state.budget >= price) {
            state.budget -= price;
            state.inventory.push({ id: itemToBuy.id, boughtValue: price });
            addMessage(`✅ קנית "${itemToBuy.name}" ב-${price} ש"ח. נשאר לך ${state.budget} ש"ח.`, 'info');
            renderStats();
            renderItems(); // Update inventory count and button state
             checkGameOver();
        } else {
            addMessage(`❌ אין מספיק כסף כדי לקנות "${itemToBuy.name}". נדרש: ${price} ש"ח.`, 'error');
        }
    }

    function sellItem(itemId) {
        const itemIndex = state.inventory.findIndex(item => item.id === itemId);
        if (itemIndex !== -1) {
             const itemToSell = state.inventory[itemIndex];
            const currentItemData = state.availableItems.find(availItem => availItem.id === itemToSell.id);
            if (!currentItemData) return;

            const price = currentItemData.currentValue;
            state.budget += price;
            state.inventory.splice(itemIndex, 1);
            addMessage(`📈 מכרת "${currentItemData.name}" ב-${price} ש"ח. יש לך עכשיו ${state.budget} ש"ח.`, 'info');
            renderStats();
            renderItems(); // Update inventory count and button state
             checkGameOver();
        } else {
            // This case should be prevented by disabling the button, but good for debug
            addMessage(`⚠ אין לך פריט כזה במלאי למכירה.`, 'warning');
        }
    }

    function advanceTime() {
        state.time++;
        updateItemValues();
        triggerRandomEvent();
        renderItems();
        renderStats();
        // addMessage(`יום ${state.time} מתחיל בשוק...`); // Too chatty

         checkGameOver();

         if (state.simulationRunning && state.time >= state.maxDays) {
             stopSimulation('time_limit');
         }
    }

    function startSimulation() {
        if (state.simulationRunning) return;

        const selectedType = dom.itemTypeSelect.value;
        state.availableItems = JSON.parse(JSON.stringify(state.itemTypesData[selectedType])); // Deep copy
        state.budget = state.initialBudget; // Reset budget
        state.inventory = []; // Reset inventory
        state.time = 0; // Reset time
        dom.gameOverMessageDiv.classList.remove('visible'); // Hide game over message

        state.availableItems.forEach(item => {
             item.currentValue = calculateCurrentValue(item); // Set initial values
             item.previousValue = item.currentValue; // Set previous to current initially
         });


        renderStats();
        renderItems();
        dom.messagesDiv.innerHTML = ''; // Clear messages
        addMessage(`🎉 המסע בשוק ה${selectedType === 'stamps' ? 'בולים' : selectedType === 'coins' ? 'מטבעות' : 'קלפים'} החל! יש לך ${state.budget} ש"ח להתחלה. המטרה: להגיע לשווי כולל של ${state.gameOverGoal} ש"ח לפני שיגמרו ${state.maxDays} ימים!`, 'info');

        state.simulationRunning = true;
        dom.startSimButton.disabled = true;
        dom.stopSimButton.disabled = false;
        dom.itemTypeSelect.disabled = true;

        state.intervalId = setInterval(advanceTime, 1200); // Advance time slightly faster - 1.2 seconds
    }

    function stopSimulation(reason = 'user') {
        if (!state.simulationRunning) return;

        clearInterval(state.intervalId);
        state.simulationRunning = false;
        dom.startSimButton.disabled = false;
        dom.stopSimButton.disabled = true;
         dom.itemTypeSelect.disabled = false;


         const finalValue = state.budget + state.inventory.reduce((sum, item) => {
            const currentItemData = state.availableItems.find(availItem => availItem.id === item.id);
            return sum + (currentItemData ? currentItemData.currentValue : 0);
        }, 0);

        let message = '';
        let isWin = false;

        if (reason === 'win') {
             message = `🎉 ניצחון מדהים! 🎉<br>הגעת לשווי כולל של ${finalValue.toFixed(0)} ש"ח ביום ${state.time}.<br>הפכת לאספן/ית מומחה/ית!`;
             isWin = true;
        } else if (reason === 'time_limit') {
             message = `⏰ נגמר הזמן! ⏰<br>המסע הסתיים לאחר ${state.maxDays} ימים. שווי כולל סופי: ${finalValue.toFixed(0)} ש"ח.<br>נסה שוב להשיג את היעד!`;
        } else { // user stopped
             message = `⏹ הסימולציה הסתיימה. ⏹<br>שווי כולל סופי: ${finalValue.toFixed(0)} ש"ח (תקציב: ${state.budget.toFixed(0)}, מלאי: ${state.inventoryValueSpan.textContent}).<br>יכול להיות שהפסדת הזדמנויות...`;
        }

        dom.gameOverMessageDiv.innerHTML = `<p>${message}</p><button onclick="startSimulation()">התחל מסע חדש</button>`;
        dom.gameOverMessageDiv.classList.add('visible');

         addMessage(`🎮 המשחק הסתיים! שווי כולל סופי: ${finalValue.toFixed(0)} ש"ח.`, 'info'); // Also add to message feed
    }

     function checkGameOver() {
         const totalValue = state.budget + state.inventory.reduce((sum, item) => {
            const currentItemData = state.availableItems.find(availItem => availItem.id === item.id);
            return sum + (currentItemData ? currentItemData.currentValue : 0);
        }, 0);

         if (totalValue >= state.gameOverGoal) {
             stopSimulation('win');
         }
     }


    function toggleExplanation() {
        const isHidden = dom.explanationDiv.style.display === 'none' || dom.explanationDiv.style.display === '';
        if (isHidden) {
            dom.explanationDiv.style.display = 'block';
            dom.explanationButton.textContent = 'הסתר את הסודות';
        } else {
            dom.explanationDiv.style.display = 'none';
            dom.explanationButton.textContent = 'לגלות את סוד הערך מאחורי הקלעים';
        }
    }

    // Event Listeners
    dom.startSimButton.addEventListener('click', startSimulation);
    dom.stopSimButton.addEventListener('click', stopSimulation);
    dom.explanationButton.addEventListener('click', toggleExplanation);

    // Initial render state
    renderStats();
     dom.dayCounterSpan.textContent = `יום: 0`; // Initialize day counter display
</script>
```