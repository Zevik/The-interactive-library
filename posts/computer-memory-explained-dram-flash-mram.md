---
title: "זיכרון המחשב נחשף: מה ההבדל בין DRAM, Flash ו-MRAM?"
english_slug: computer-memory-explained-dram-flash-mram
category: "טכנולוגיה / מדעי המחשב"
tags: [זיכרון, DRAM, Flash, MRAM, חומרה, שבבים]
---
<div class="intro-section">
    <h1>זיכרון המחשב נחשף: מה ההבדל בין DRAM, Flash ו-MRAM?</h1>
    <p>הטלפון שלכם עולה תוך שניות, המחשב לוקח דקות. כשמכבים את המחשב, התוכנות שרצות נעלמות, אך התמונות בטלפון נשארות. מדוע יש הבדלים כאלה בהתנהגות ובמהירות של זכרונות דיגיטליים? בואו נצלול פנימה ונבין!</p>
</div>

<div id="memory-app" class="app-container">
    <div class="controls">
        <h3>בחר את סוג הזיכרון לחקר:</h3>
        <div class="memory-type-selection">
            <button class="memory-type-btn" data-type="DRAM">DRAM (זיכרון נדיף)</button>
            <button class="memory-type-btn" data-type="Flash">Flash (זיכרון בלתי נדיף)</button>
            <button class="memory-type-btn" data-type="MRAM">MRAM (בלתי נדיף, מהיר)</button>
        </div>

        <div class="memory-actions disabled-actions">
            <h3>מעבדה: בצע פעולה</h3>
            <div class="action-group">
                <label for="write-value">ערך לכתיבה (0 או 1):</label>
                <input type="number" id="write-value" min="0" max="1" value="1" disabled>
                <button id="write-btn" class="action-btn write-btn" disabled>כתוב</button>
            </div>
             <div class="action-group">
                 <button id="read-btn" class="action-btn read-btn" disabled>קרא</button>
            </div>
            <div class="action-group">
                 <button id="power-toggle-btn" class="action-btn power-toggle-btn" disabled>נתק חשמל 🔌</button>
            </div>
        </div>
    </div>

    <div class="visualization">
        <h3>תא הזיכרון (סימולציה):</h3>
        <div id="memory-cell" class="memory-cell">
            <div id="cell-representation" class="cell-representation">?</div>
            <div id="cell-value" class="cell-value">?</div>
             <div id="power-indicator" class="power-indicator">🔌</div>
             <!-- Visual elements for animations -->
             <div class="write-animation-effect"></div>
             <div class="read-animation-effect"></div>
             <div class="power-animation-effect"></div>
        </div>
        <p id="status-message" class="status-message">אנא בחר סוג זיכרון כדי להתחיל את הניסוי.</p>
    </div>
</div>

<button id="toggle-explanation" class="toggle-explanation-btn">🤔 הסבר מורחב על סוגי הזיכרון</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>🚀 מבוא - מהו זיכרון במחשב ולמה יש סוגים שונים?</h2>
    <p>דמיינו את המחשב שלכם כמעין שולחן עבודה ענק עם מגירות רבות. המעבד הוא אתם, יושבים בשולחן וצריכים גישה מהירה לכלי העבודה (נתונים ופקודות) שעליהם אתם עובדים <strong>ברגע זה</strong>. זהו תפקיד הזיכרון הראשי (RAM). אבל אתם גם צריכים לשמור מסמכים חשובים (קבצים, תמונות, תוכנות) שיישארו במגירות גם כשאתם קמים מהשולחן (מכבים את המחשב). זהו תפקיד זיכרון האחסון לטווח ארוך (כמו דיסק קשיח או SSD).</p>
    <p>מכיוון שלדרישות האלה (מהירות גישה מיידית מול אחסון קבוע) יש אילוצים שונים (עלות, צריכת חשמל, גודל פיזי), פותחו סוגי זיכרון שונים. הסימולציה למעלה מראה תא יחיד מכל אחד משלושת הסוגים הנפוצים כדי לעזור לכם להבין את ההבדלים המהותיים בהתנהגותם.</p>

    <h2>✨ זיכרון נדיף (Volatile) לעומת זיכרון בלתי נדיף (Non-Volatile)</h2>
    <p>ההבדל המרכזי והדרמטי ביותר הוא בשאלה האם הזיכרון זוכר את המידע שלו כשהחשמל מנותק:</p>
    <ul>
        <li><b>זיכרון נדיף (Volatile Memory):</b> הוא כמו פתק שכתבתם בעיפרון על דף שולחן העבודה שלכם. כל עוד האור (חשמל) דולק, אתם רואים אותו בבירור. ברגע שהאור כבה, הוא נעלם! הזיכרון הזה דורש חשמל קבוע כדי לשמור על הנתונים. כבוי = נאבד. לרוב, זיכרונות נדיפים הם מהירים יותר. <strong>דוגמה: DRAM</strong> (ה-RAM במחשב).</li>
        <li><b>זיכרון בלתי נדיף (Non-Volatile Memory):</b> זהו מידע שנצרב בעט על דף קשיח במגירה. גם אם תכבו את האור ותלכו הביתה, כשתחזרו ותדליקו את האור, המידע יהיה שם! זיכרון כזה שומר את המידע גם ללא מתח חשמלי. הוא משמש לאחסון קבוע. <strong>דוגמאות: Flash</strong> (בטלפונים, דיסק און קי, SSDs), <strong>MRAM</strong> (טכנולוגיה חדשנית), דיסקים קשיחים מסורתיים (HDD).</li>
    </ul>

    <h2>⚛️ DRAM (Dynamic Random-Access Memory) - סוס העבודה הנדיף</h2>
    <p>ה-DRAM הוא ה-RAM הקלאסי שאתם מכירים מהמחשב השולחני או הנייד שלכם. הוא זז במהירות מסחררת, אבל הוא שכחן באופן קיצוני ברגע שהחשמל נעלם.</p>
    <h3>איך זה עובד בפשטות:</h3>
    <p>כל ביט ב-DRAM מאוחסן בקבל זעיר שמחזיק מטען חשמלי (1) או לא מחזיק מטען (0). הבעיה? הקבל הזה "דולף" את המטען שלו מהר מאוד. לכן, יש צורך ב"רענון" (Refresh) מתמיד - קריאת הערך וכתיבתו מחדש - אלפי פעמים בשנייה! זה דורש חשמל קבוע ומסביר למה הוא נדיף ("דינמי" מתייחס לצורך ברענון המתמיד).</p>
    <h3>מאפיינים מרכזיים:</h3>
    <ul>
        <li><b>מהירות:</b> מהיר מאוד לקריאה וכתיבה.</li>
        <li><b>נדיפות:</b> המידע אובד מיידית בהפסקת חשמל.</li>
        <li><b>צריכת חשמל:</b> גבוהה יחסית (דורש חשמל לרענון קבוע).</li>
        <li><b>אורך חיים:</b> אין שחיקה פיזית משמעותית בכתיבה.</li>
        <li><b>שימושים:</b> הזיכרון הראשי (RAM) במחשבים, קונסולות, שרתים.</li>
    </ul>

    <h2>💾 Flash Memory - הארכיון הנייד והעמיד</h2>
    <p>Flash הוא הזיכרון הבלתי-נדיף שמאפשר לכם לכבות את הטלפון ולהדליק אותו שוב מבלי לאבד את כל האפליקציות והתמונות. הוא קצת פחות מהיר מ-DRAM, ויש לו סוד אפל קטן...</p>
    <h3>איך זה עובד בפשטות:</h3>
    <p>Flash משתמש בטרנזיסטורים מיוחדים עם "שער צף" (Floating Gate) שכולא אלקטרונים. אפשר לכלוא אלקטרונים (לכתוב 1) או לשחרר אותם (לכתוב 0) על ידי הפעלת מתחים מסוימים. היתרון הגדול: האלקטרונים נשארים כלואים גם ללא חשמל חיצוני! החיסרון: תהליך הכתיבה והמחיקה דורש "ניקוי" של אזורים גדולים יחסית בזיכרון (בלוקים) לפני שניתן לכתוב מחדש, מה שהופך אותו לאיטי יותר לכתיבה מאשר לקריאה. וזה הסוד האפל: כל כתיבה/מחיקה שוחקת את התאים פיזית, ולכן לזיכרון Flash יש אורך חיים מוגבל מבחינת מספר הפעולות שניתן לבצע עליו (Endurance).</p>
    <h3>מאפיינים מרכזיים:</h3>
    <ul>
        <li><b>מהירות:</b> מהיר לקריאה, איטי יותר לכתיבה/מחיקה (דורש פעולות בלוק).</li>
        <li><b>בלתי נדיפות:</b> שומר מידע גם ללא חשמל.</li>
        <li><b>אורך חיים:</b> מוגבל יחסית (מיליונים בודדים של מחזורי כתיבה/מחיקה לתא).</li>
        <li><b>צפיפות:</b> מאפשר לארוז הרבה מידע בשטח קטן, ולכן מצוין לאחסון המוני.</li>
        <li><b>שימושים:</b> כונני SSD, אחסון בטלפונים/טאבלטים, כרטיסי זיכרון, דיסק און קי.</li>
    </ul>

    <h2>🧲 MRAM (Magnetoresistive Random-Access Memory) - העתיד המגנטי?</h2>
    <p>MRAM היא טכנולוגיה חדשה ומלהיבה שמנסה לשלב את הטוב שבשני העולמות: המהירות של DRAM עם הבלתי-נדיפות של Flash, ובלי בעיית השחיקה של Flash!</p>
    <h3>איך זה עובד בפשטות:</h3>
    <p>תא MRAM מאחסן מידע במצב מגנטי. הוא משתמש בחומרים שמגיבים לשדה מגנטי. שינוי כיוון המגנוט (כתיבה) משפיע על ההתנגדות החשמלית של התא. התנגדות נמוכה = 0, התנגדות גבוהה = 1. הנתון נשמר במצב המגנטי באופן קבוע, גם ללא חשמל! קריאה מתבצעת על ידי מדידת ההתנגדות, והיא מהירה כמו קריאה מ-DRAM.</p>
    <h3>מאפיינים מרכזיים:</h3>
    <ul>
        <li><b>מהירות:</b> מהיר מאוד גם לקריאה וגם לכתיבה (קרוב ל-DRAM).</li>
        <li><b>בלתי נדיפות:</b> שומר מידע גם ללא חשמל.</li>
        <li><b>אורך חיים:</b> גבוה מאוד (הרבה יותר מ-Flash). אין שחיקה פיזית משמעותית מכתיבה.</li>
        <li><b>צריכת חשמל:</b> נמוכה (אין צורך ברענון).</li>
        <li><b>שימושים:</b> עדיין יקר יותר ופחות נפוץ מ-DRAM ו-Flash. בשימוש ביישומים מיוחדים (מטמון מהיר, אחסון בבקרים תעשייתיים, IoT). נחשב מועמד פוטנציאלי להחליף סוגי זיכרון אחרים בעתיד.</li>
    </ul>

    <h2>📊 השוואה מסכמת - מי הטוב ביותר? (תלוי למה!)</h2>
    <p>הטבלה הבאה מסכמת את ההבדלים העיקריים:</p>
    <table>
        <thead>
            <tr>
                <th>מאפיין</th>
                <th>DRAM</th>
                <th>Flash</th>
                <th>MRAM</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>נדיפות (Volatility)</td>
                <td>נדיף (מאבד מידע ללא חשמל)</td>
                <td>בלתי נדיף (שומר מידע ללא חשמל)</td>
                <td>בלתי נדיף (שומר מידע ללא חשמל)</td>
            </tr>
            <tr>
                <td>מהירות קריאה</td>
                <td>🏃‍♂️ מהירה מאוד</td>
                <td>🏃 מהירה</td>
                <td>🏃‍♂️ מהירה מאוד</td>
            </tr>
            <tr>
                <td>מהירות כתיבה</td>
                <td>✍️ מהירה מאוד</td>
                <td>🐢 איטית יחסית (במיוחד מחיקה/כתיבה)</td>
                <td>✍️ מהירה מאוד / מהירה</td>
            </tr>
            <tr>
                <td>עקרון פעולה</td>
                <td>קבלים (דורש רענון)</td>
                <td>שער צף (מלכודת אלקטרונים)</td>
                <td>מגנטורזיסטיביות (מצב מגנטי)</td>
            </tr>
            <tr>
                <td>צריכת חשמל</td>
                <td>⚡ גבוהה יחסית</td>
                <td>🔋 נמוכה יחסית</td>
                <td>💡 נמוכה מאוד</td>
            </tr>
             <tr>
                <td>אורך חיים (מספר מחזורי כתיבה)</td>
                <td>♾️ גבוה מאוד</td>
                <td>⏳ מוגבל</td>
                <td>💪 גבוה מאוד</td>
            </tr>
            <tr>
                <td>שימושים נפוצים</td>
                <td>זיכרון RAM ראשי במחשב</td>
                <td>כונני SSD, USB, אחסון נייד</td>
                <td>יישומים תעשייתיים, מטמון מהיר, IoT (צומח)</td>
            </tr>
        </tbody>
    </table>

    <h2>🏗️ לסיכום: היררכיית הזיכרון</h2>
    <p>בגלל היתרונות והחסרונות השונים, מערכות מודרניות לא מסתמכות על סוג זיכרון אחד. הן משתמשות ב"היררכיית זיכרון": זיכרונות מהירים ויקרים (כמו מטמון במעבד ו-DRAM) נמצאים קרוב למעבד לגישה מיידית. זיכרונות איטיים וזולים יותר (כמו Flash ב-SSD) משמשים לאחסון כמויות גדולות לטווח ארוך. ה-MRAM, עם שילוב המהירות והעמידות שלו, עשוי למלא בעתיד נישות חשובות בהיררכיה הזו, או אפילו לשנות אותה.</p>
</div>

<style>
    :root {
        --primary-color: #4a90e2; /* Blue */
        --secondary-color: #50e3c2; /* Teal */
        --accent-color: #f5a623; /* Orange */
        --danger-color: #d0021b; /* Red */
        --success-color: #7bdc7f; /* Green */
        --background-color: #f7f9fb;
        --card-background: #ffffff;
        --text-color: #333;
        --border-color: #ddd;
        --shadow-color: rgba(0, 0, 0, 0.1);
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        direction: rtl;
        text-align: right;
        padding: 20px;
    }

    h1, h2, h3 {
        color: var(--primary-color);
        margin-bottom: 15px;
    }

    h1 { font-size: 2em; }
    h2 { font-size: 1.5em; margin-top: 30px; border-bottom: 2px solid var(--secondary-color); padding-bottom: 5px; }
    h3 { font-size: 1.2em; color: var(--accent-color); margin-top: 20px; }

    .intro-section p, .explanation-section p, .explanation-section ul {
         margin-bottom: 15px;
         line-height: 1.7;
     }

    .explanation-section ul {
         padding-right: 25px; /* Indent list for RTL */
     }
     .explanation-section li {
         margin-bottom: 8px;
     }
     .explanation-section b {
         color: var(--primary-color);
     }


    .app-container {
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 30px;
        margin: 40px auto;
        max-width: 800px;
        box-shadow: 0 5px 15px var(--shadow-color);
        display: flex;
        flex-direction: column;
        gap: 30px;
    }

    .controls, .visualization {
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #fdfdff; /* Slightly lighter background */
    }

    .controls {
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

     .memory-type-selection {
         display: flex;
         flex-wrap: wrap;
         gap: 10px;
     }

    .memory-type-btn, .action-btn, .toggle-explanation-btn {
        padding: 12px 20px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .memory-type-btn {
        background-color: #e9ecef; /* Light grey */
        color: var(--text-color);
    }
    .memory-type-btn.active {
        background-color: var(--primary-color);
        color: white;
        box-shadow: 0 3px 8px rgba(0,0,0,0.2);
    }
     .memory-type-btn:hover:not(:disabled):not(.active) {
         background-color: #dee2e6;
     }


    .memory-actions {
        display: flex;
        flex-direction: column;
        gap: 15px;
         padding-top: 15px;
         margin-top: 15px;
         border-top: 1px solid var(--border-color);
    }

     .memory-actions.disabled-actions {
         opacity: 0.6;
         pointer-events: none; /* Disable clicks */
     }


    .action-group {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap;
    }
    .action-group label {
        font-weight: bold;
         margin-left: 10px;
    }

    #write-value {
        width: 50px;
        padding: 8px;
        border: 1px solid var(--border-color);
        border-radius: 4px;
        text-align: center;
        font-size: 1rem;
    }

    .write-btn {
        background-color: var(--success-color);
        color: white;
    }
    .read-btn {
        background-color: var(--accent-color);
        color: white;
    }
    .power-toggle-btn {
        background-color: var(--danger-color);
        color: white;
    }

    .action-btn:hover:not(:disabled) {
         opacity: 0.9;
         transform: translateY(-1px);
         box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }

    .memory-type-btn:disabled, .action-btn:disabled {
        opacity: 0.4;
        cursor: not-allowed;
        box-shadow: none;
         transform: none;
    }

    .visualization {
        text-align: center;
        position: relative; /* Needed for absolute positioning of cell */
    }

    #memory-cell {
        width: 150px; /* Increased size */
        height: 100px;
        border: 3px solid var(--primary-color);
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        margin: 20px auto;
        background-color: var(--card-background);
        overflow: hidden;
        transition: all 0.5s ease-in-out; /* Smooth transitions on state change */
        box-shadow: 0 4px 12px var(--shadow-color);
    }

    #memory-cell.power-off {
        border-color: var(--danger-color);
        background-color: #fff0f0; /* Light red background */
        box-shadow: 0 4px 12px rgba(var(--danger-color), 0.3);
    }


    #cell-representation {
        font-size: 2em; /* Larger icon */
        position: absolute;
        top: 10px;
        right: 10px;
        color: var(--primary-color);
        transition: color 0.5s ease;
    }

    #memory-cell.power-off #cell-representation {
        color: var(--danger-color);
    }


    #cell-value {
        font-size: 4em; /* Very large value */
        font-weight: bold;
        color: var(--text-color);
        transition: color 0.3s ease;
    }

     #memory-cell.power-off #cell-value {
        color: var(--danger-color);
     }


    #power-indicator {
        position: absolute;
        bottom: 8px;
        left: 8px;
        font-size: 1.5em;
        color: var(--success-color); /* Green for powered */
        transition: color 0.5s ease;
    }

    #memory-cell.power-off #power-indicator {
        color: var(--danger-color); /* Red for power off */
    }

    /* Animation Effects Containers */
    .write-animation-effect, .read-animation-effect, .power-animation-effect {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none; /* Don't block clicks */
    }

    /* --- Specific Animations --- */

    /* Base Write Animation - Value Scale */
     @keyframes pulse-scale {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.3); opacity: 0.7; }
        100% { transform: scale(1); opacity: 1; }
    }

     #memory-cell.animating-write #cell-value {
         animation: pulse-scale 0.6s ease-out;
     }

    /* Base Read Animation - Cell Flash */
     @keyframes flash {
        0% { background-color: transparent; }
        50% { background-color: rgba(var(--primary-color), 0.2); } /* Light primary color flash */
        100% { background-color: transparent; }
    }
     #memory-cell.animating-read {
         animation: flash 0.5s ease;
     }

    /* DRAM Specifics */
    /* DRAM Refresh Animation (Subtle pulse when idle & powered) */
     @keyframes dram-refresh {
         0%, 100% { transform: scale(1); opacity: 1; }
         50% { transform: scale(1.02); opacity: 0.98; }
     }
     #memory-cell.dram.powered.idle {
         animation: dram-refresh 2s ease-in-out infinite;
     }

    /* Flash Specifics */
    /* Flash Write Animation (Slower, maybe blocky or 'burning' effect) */
     @keyframes flash-write-effect {
        0% { background: transparent; }
        20% { background: rgba(var(--accent-color), 0.1); }
        80% { background: rgba(var(--accent-color), 0.3); } /* Longer burn effect */
        100% { background: transparent; }
     }
     #memory-cell.flash.animating-write .write-animation-effect {
         animation: flash-write-effect 1s ease-out; /* Matches write speed */
     }

    /* Flash Read Animation (Similar to base, maybe slightly longer) */
     #memory-cell.flash.animating-read {
         animation: flash 0.6s ease;
     }


    /* MRAM Specifics */
     /* MRAM Write Animation (Quick magnetic flip - represent with scale/rotate?) */
     @keyframes mram-write-flip {
         0% { transform: scale(1) rotateY(0deg); }
         50% { transform: scale(1.1) rotateY(180deg); }
         100% { transform: scale(1) rotateY(360deg); }
     }
      #memory-cell.mram.animating-write #cell-value {
         animation: mram-write-flip 0.4s ease-out; /* Matches write speed */
     }
      /* MRAM Read Animation (Very quick, non-destructive pulse) */
      #memory-cell.mram.animating-read {
         animation: flash 0.4s ease;
      }


    /* Power Off Effect */
     @keyframes power-off-visual {
         0% { opacity: 1; }
         100% { opacity: 0.2; }
     }
     #memory-cell.animating-power-off {
         animation: power-off-visual 0.3s ease-out forwards;
     }
     /* Power On Effect */
      @keyframes power-on-visual {
         0% { opacity: 0.2; }
         100% { opacity: 1; }
     }
     #memory-cell.animating-power-on {
         animation: power-on-visual 0.3s ease-out forwards;
     }


    .status-message {
        margin-top: 20px;
        font-size: 1.1rem;
        color: var(--text-color);
        min-height: 1.5em; /* Prevent layout shift */
        font-weight: bold;
    }
    #memory-cell.power-off + .status-message {
         color: var(--danger-color);
    }


    .toggle-explanation-btn {
        display: block;
        margin: 40px auto;
        background-color: var(--secondary-color);
        color: var(--text-color);
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 0 3px 8px rgba(0,0,0,0.2);
    }

    .toggle-explanation-btn:hover {
         background-color: #40c9b4;
         transform: translateY(-2px);
    }

    .explanation-section {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--card-background);
        direction: rtl;
        text-align: right;
        box-shadow: 0 5px 15px var(--shadow-color);
    }

    .explanation-section h2:first-child {
        margin-top: 0;
    }

    /* Add a simple comparison table style */
    .explanation-section table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
        text-align: right;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .explanation-section th, .explanation-section td {
        border: 1px solid var(--border-color);
        padding: 12px;
    }
    .explanation-section th {
        background-color: #e9ecef;
        font-weight: bold;
        color: var(--primary-color);
    }
     .explanation-section tr:nth-child(even) {
         background-color: #f8f9fa; /* Zebra striping */
     }

    /* Responsive Adjustments */
    @media (max-width: 600px) {
        .app-container, .explanation-section {
            padding: 20px;
        }
        .controls h3, .visualization h3 {
            text-align: center;
        }
        .memory-type-selection {
             justify-content: center;
        }
        .action-group {
            justify-content: center;
        }
         .action-group label, .action-group input, .action-group button {
             margin-left: 0;
         }
        #memory-cell {
             width: 100px;
             height: 80px;
        }
        #cell-value {
             font-size: 3em;
        }
         #cell-representation {
             font-size: 1.5em;
         }
          #power-indicator {
              font-size: 1.2em;
          }

         .toggle-explanation-btn {
             padding: 10px 15px;
             font-size: 1rem;
         }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const memoryTypeBtns = document.querySelectorAll('.memory-type-btn');
        const writeValueInput = document.getElementById('write-value');
        const writeBtn = document.getElementById('write-btn');
        const readBtn = document.getElementById('read-btn');
        const powerToggleBtn = document.getElementById('power-toggle-btn');
        const memoryCell = document.getElementById('memory-cell');
        const cellRepresentation = document.getElementById('cell-representation');
        const cellValue = document.getElementById('cell-value');
        const powerIndicator = document.getElementById('power-indicator');
        const statusMessage = document.getElementById('status-message');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationBtn = document.getElementById('toggle-explanation');
        const memoryActionsDiv = document.querySelector('.memory-actions');


        let currentMemoryType = null;
        let storedValue = null; // null means no value/uninitialized/lost
        let isPowered = true;
        let isAnimating = false; // Prevent multiple animations at once

        // Configuration for each memory type
        const memoryProperties = {
            DRAM: {
                name: 'DRAM',
                representation: '⚛️', // Capacitor/Atom symbol idea
                writeSpeed: 600, // ms - simulating speed + animation time
                readSpeed: 500, // ms
                volatile: true,
                description: "זיכרון נדיף ומהיר במיוחד. דורש חשמל קבוע לרענון, אחרת המידע אובד.",
                writeAnimation: 'pulse-scale', // Use base animation on value
                readAnimation: 'flash', // Use base animation on cell
                cellClasses: ['dram']
            },
            Flash: {
                name: 'Flash',
                representation: '💾', // Disk/Storage symbol idea
                writeSpeed: 1500, // ms (significantly slower write)
                readSpeed: 600, // ms (slower read than DRAM/MRAM)
                volatile: false,
                description: "זיכרון בלתי נדיף, נפוץ לאחסון קבוע. מהיר לקריאה, אך איטי יותר לכתיבה ובעל אורך חיים מוגבל.",
                 writeAnimation: 'flash-write-effect', // Use specific effect layer animation
                readAnimation: 'flash', // Use base animation on cell, maybe slightly longer
                cellClasses: ['flash']
            },
            MRAM: {
                name: 'MRAM',
                representation: '🧲', // Magnet symbol idea
                writeSpeed: 700, // ms (fast write)
                readSpeed: 550, // ms (fast read)
                volatile: false,
                description: "זיכרון בלתי נדיף ומהיר (קרוב ל-DRAM), עם אורך חיים ארוך. טכנולוגיה חדשנית.",
                 writeAnimation: 'mram-write-flip', // Use specific animation on value
                 readAnimation: 'mram-read', // Use base flash animation, maybe quicker
                cellClasses: ['mram']
            }
        };

        // Helper to disable/enable buttons
        function setActionsEnabled(enabled) {
            const actionsContainer = document.querySelector('.memory-actions');
            actionsContainer.classList.toggle('disabled-actions', !enabled);

            // Explicitly set disabled state on buttons/input for screen readers etc.
            const actionElements = actionsContainer.querySelectorAll('button, input');
            actionElements.forEach(el => el.disabled = !enabled);
        }


        function updateUI() {
            // Update memory type buttons state
            memoryTypeBtns.forEach(btn => {
                if (btn.dataset.type === currentMemoryType) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });

            // Remove previous type classes and add current one
            Object.keys(memoryProperties).forEach(type => memoryCell.classList.remove(type.toLowerCase()));
             if (currentMemoryType) {
                memoryCell.classList.add(currentMemoryType.toLowerCase());
             }


            // Update action buttons enabled state (controlled by setActionsEnabled)
             // Let the animation state handle the actual disabling via setActionsEnabled calls

            // Update power button text and state
            powerToggleBtn.textContent = isPowered ? 'נתק חשמל 🔌' : 'חבר חשמל ⚡';
            memoryCell.classList.toggle('power-off', !isPowered);
            powerIndicator.style.color = isPowered ? 'var(--success-color)' : 'var(--danger-color)';


            // Update cell representation and border color based on power
            if (currentMemoryType && memoryProperties[currentMemoryType]) {
                 cellRepresentation.textContent = memoryProperties[currentMemoryType].representation;
                 // Border color is handled by .power-off class in CSS
            } else {
                 cellRepresentation.textContent = '?';
            }

            // Update cell value display based on power, volatility, and stored value
            const isVolatile = currentMemoryType && memoryProperties[currentMemoryType].volatile;

            // Handle DRAM refresh animation state
             if (currentMemoryType === 'DRAM' && isPowered && !isAnimating) {
                  memoryCell.classList.add('powered', 'idle');
             } else {
                 memoryCell.classList.remove('powered', 'idle');
             }


            if (!isPowered && isVolatile) {
                 cellValue.textContent = '⚡'; // Show lightning when volatile & no power
                 statusMessage.textContent = `🔋 החשמל מנותק. הזיכרון הנדיף (${currentMemoryType}) איבד את המידע.`;
                 storedValue = null; // Ensure storedValue is null when volatile and off
            } else if (storedValue !== null) {
                cellValue.textContent = storedValue;
                 if (!isAnimating) {
                     statusMessage.textContent = `💾 ערך נוכחי ב-${currentMemoryType}: ${storedValue}.`;
                 }
            } else if (currentMemoryType !== null) {
                 cellValue.textContent = '?'; // Show ? if no value is stored (e.g., after power loss on volatile, or initial state)
                 if (!isAnimating) {
                     statusMessage.textContent = `🤔 זיכרון מסוג ${currentMemoryType} נבחר. אנא בצע פעולה (כתוב/קרא).`;
                 }
            } else {
                 cellValue.textContent = '?';
                 statusMessage.textContent = `👋 בחר סוג זיכרון כדי להתחיל את הסימולציה.`;
            }

            // Actions are disabled/enabled externally by animation logic
        }

        function simulateWrite(value) {
            if (!currentMemoryType || isAnimating || !isPowered) return;

            isAnimating = true;
            setActionsEnabled(false); // Disable actions during animation
            const props = memoryProperties[currentMemoryType];

            statusMessage.textContent = `✍️ כותב ${value} לזיכרון ${currentMemoryType}... (אורך פעולה: ${props.writeSpeed}ms)`;

             // Apply animation classes
             if (props.writeAnimation) {
                 if (props.writeAnimation === 'pulse-scale' || props.writeAnimation === 'mram-write-flip') {
                      cellValue.classList.add('animating-write');
                 } else if (props.writeAnimation === 'flash-write-effect') {
                     const effectElement = memoryCell.querySelector('.write-animation-effect');
                     effectElement.classList.add('animating-write-effect'); // Use a distinct class for the effect layer animation
                 }
             }


            setTimeout(() => {
                storedValue = value; // Update the stored value
                cellValue.textContent = storedValue; // Update the display immediately after the conceptual write

                 // Clean up animation classes
                 cellValue.classList.remove('animating-write');
                 const effectElement = memoryCell.querySelector('.write-animation-effect');
                 effectElement.classList.remove('animating-write-effect');

                isAnimating = false;
                setActionsEnabled(true); // Re-enable actions
                statusMessage.textContent = `✅ הכתיבה לזיכרון ${currentMemoryType} הסתיימה בהצלחה.`;
                updateUI(); // Final UI update after state change
            }, props.writeSpeed);
        }

        function simulateRead() {
             if (!currentMemoryType || isAnimating || !isPowered) return;

            isAnimating = true;
            setActionsEnabled(false); // Disable actions during animation
            const props = memoryProperties[currentMemoryType];

            statusMessage.textContent = `👀 קורא מהזיכרון ${currentMemoryType}... (אורך פעולה: ${props.readSpeed}ms)`;

             // Apply animation classes
             if (props.readAnimation) {
                 memoryCell.classList.add('animating-read');
             }


            setTimeout(() => {
                 memoryCell.classList.remove('animating-read'); // Clean up animation

                 if (storedValue !== null) {
                     statusMessage.textContent = `✅ הקריאה מהזיכרון ${currentMemoryType} הסתיימה. הערך הוא: ${storedValue}.`;
                     cellValue.textContent = storedValue; // Ensure value is displayed clearly after read
                 } else {
                     statusMessage.textContent = `⚠️ הקריאה מהזיכרון ${currentMemoryType} הסתיימה. אין ערך זמין (תא ריק או נמחק).`;
                      cellValue.textContent = '?'; // Ensure ? is shown if value is null
                 }

                isAnimating = false;
                setActionsEnabled(true); // Re-enable actions
                updateUI(); // Final UI update
            }, props.readSpeed);
        }

        function togglePower() {
             if (!currentMemoryType || isAnimating) return;

            isAnimating = true;
            setActionsEnabled(false); // Disable actions during power transition

            const props = memoryProperties[currentMemoryType];
            const wasPowered = isPowered;
            isPowered = !isPowered;

             memoryCell.classList.add(wasPowered ? 'animating-power-off' : 'animating-power-on');

             if (!isPowered) { // Powering Off
                 statusMessage.textContent = `🔌 מנתק חשמל...`;
                 if (props.volatile) {
                    // Data loss happens immediately but we might delay the visual change slightly
                     // The updateUI already sets storedValue = null visually for volatile off state
                     // We'll add a slight delay before updating the final status message
                     setTimeout(() => {
                        statusMessage.textContent = `🔋 החשמל מנותק. המידע בזיכרון ${currentMemoryType} אבד (זיכרון נדיף).`;
                         isAnimating = false;
                         setActionsEnabled(true);
                         updateUI(); // Final UI update for power off state
                     }, 500); // Animation + small delay
                 } else {
                     // Non-volatile memory retains data - nothing happens to storedValue
                      setTimeout(() => {
                         statusMessage.textContent = `🔋 החשמל מנותק. המידע בזיכרון ${currentMemoryType} נשמר (זיכרון בלתי נדיף).`;
                          isAnimating = false;
                          setActionsEnabled(true);
                          updateUI(); // Final UI update for power off state
                      }, 500); // Animation + small delay
                 }
             } else { // Powering On
                 statusMessage.textContent = `⚡ מחבר חשמל...`;
                 // For non-volatile, storedValue is already correct. For volatile, it's null.
                 // The visual update happens via updateUI
                  setTimeout(() => {
                      if (props.volatile) {
                           statusMessage.textContent = `🔌 החשמל חובר. זיכרון נדיף (${currentMemoryType}) - המידע הקודם אבד. התא ריק.`;
                      } else {
                          statusMessage.textContent = `🔌 החשמל חובר. זיכרון בלתי נדיף (${currentMemoryType}) - המידע הקודם נשמר.`;
                      }
                      isAnimating = false;
                      setActionsEnabled(true);
                      updateUI(); // Final UI update for power on state
                  }, 500); // Animation + small delay
             }

        }

        // Event Listeners

        // Memory Type Selection
        memoryTypeBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                if (isAnimating) return; // Prevent changing type during animation or power toggle

                // Reset state
                currentMemoryType = btn.dataset.type;
                storedValue = null; // Reset value when changing memory type
                isPowered = true; // Assume power is on when selecting type

                 // Remove animation classes before starting
                 memoryCell.classList.remove('animating-write', 'animating-read', 'animating-power-off', 'animating-power-on');
                 cellValue.classList.remove('animating-write', 'mram-write-flip');
                 memoryCell.querySelector('.write-animation-effect').classList.remove('animating-write-effect');


                 // Add a slight delay before enabling actions to feel like initialization
                 setActionsEnabled(false);
                 statusMessage.textContent = `🛠️ מאתחל זיכרון מסוג ${currentMemoryType}...`;
                 setTimeout(() => {
                     setActionsEnabled(true); // Enable actions after initialization delay
                     updateUI(); // Initial UI update after selecting type
                     statusMessage.textContent = `✅ נבחר סוג זיכרון: ${memoryProperties[currentMemoryType].name}. המעבדה מוכנה!`;
                 }, 700); // Simulated initialization time


            });
        });

        // Write Button
        writeBtn.addEventListener('click', () => {
            const valueToWrite = writeValueInput.value;
             if (valueToWrite === '0' || valueToWrite === '1') {
                 simulateWrite(valueToWrite);
             } else {
                 statusMessage.textContent = '❌ אנא הזן 0 או 1 לכתיבה בלבד!';
             }
        });

        // Read Button
        readBtn.addEventListener('click', () => {
            simulateRead();
        });

        // Power Toggle Button
        powerToggleBtn.addEventListener('click', () => {
            togglePower();
        });

        // Listen for animation end events on the cell and value elements
        // Use these to clean up specific animation classes if needed,
        // but rely on the setTimeout in the simulate functions to manage `isAnimating`

         memoryCell.addEventListener('animationend', (event) => {
             // Clean up general animation classes if they finish
             if (event.animationName.startsWith('flash')) {
                 memoryCell.classList.remove('animating-read');
             } else if (event.animationName === 'power-off-visual') {
                 memoryCell.classList.remove('animating-power-off');
             } else if (event.animationName === 'power-on-visual') {
                  memoryCell.classList.remove('animating-power-on');
             }
              // Note: isAnimating is cleared in the setTimeout callback, not here
         });

        cellValue.addEventListener('animationend', (event) => {
             if (event.animationName === 'pulse-scale' || event.animationName === 'mram-write-flip') {
                  cellValue.classList.remove('animating-write', 'mram-write-flip');
             }
             // Note: isAnimating is cleared in the setTimeout callback, not here
        });

         // Listen for animation end on the effect layer for Flash write
         const writeEffectElement = memoryCell.querySelector('.write-animation-effect');
         writeEffectElement.addEventListener('animationend', (event) => {
             if (event.animationName === 'flash-write-effect') {
                  writeEffectElement.classList.remove('animating-write-effect');
             }
         });


        // Explanation toggle
        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationBtn.textContent = isHidden ? '◀️ הסתר הסבר מורחב' : '🤔 הסבר מורחב על סוגי הזיכרון';
             // Scroll to the explanation section if showing it
             if (isHidden) {
                 explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
             }
        });

        // Initial setup - clear the actions section until a memory type is selected
        setActionsEnabled(false);
        updateUI(); // Set initial status message and state
    });
</script>
```