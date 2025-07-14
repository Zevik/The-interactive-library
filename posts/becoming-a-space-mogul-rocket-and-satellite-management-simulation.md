---
title: "להיות איל חלל: מאסטרטגיה על הקרקע להצלחה במסלול"
english_slug: becoming-a-space-mogul-rocket-and-satellite-management-simulation
category: "כלכלה"
tags:
  - חלל
  - יזמות
  - ניהול אסטרטגי
  - כלכלה טכנולוגית
  - סימולציה עסקית
---
# להיות איל חלל: מאסטרטגיה על הקרקע להצלחה במסלול

החלל הוא גבול חדש, ומגרש משחקים למעצמות ויזמים כאחד. אבל מה באמת נדרש כדי להפוך חזון אסטרונאוטי לחברת ענק משגשגת? האם פריצת דרך טכנולוגית מספיקה, או שמא מדובר במשחק סבוך של ניהול משאבים, לכידת שווקים, תמחור חכם וניווט בין סיכונים תהומיים? צלול לעולם המרתק של יזמות החלל וגלה בעצמך.

<div id="space-sim-container">
    <header class="sim-header">
        <h2>סימולציית חברת חלל: מרכז פיקוד (<span id="turn-label">תור</span> <span id="turn-counter" class="counter-value">1</span>)</h2>
        <p class="tagline">בנה, שגר, כבוש את המסלול!</p>
    </header>

    <section class="sim-dashboard card">
        <h3 class="card-title">לוח בקרה כללי</h3>
        <div class="dashboard-grid">
            <div class="dashboard-item">
                <span class="item-label">מאזן מצטבר:</span>
                <span id="total-profit" class="item-value profit">$0M</span>
            </div>
            <div class="dashboard-item">
                 <span class="item-label">תזרים מזומנים (תור נוכחי):</span>
                <span id="cash-flow" class="item-value cash">$10M</span>
            </div>
             <div class="dashboard-item">
                <span class="item-label">מלאי רקטות:</span>
                <span id="rockets-available" class="item-value inventory">0</span>
            </div>
            <div class="dashboard-item">
                <span class="item-label">מלאי לוויינים:</span>
                <span id="satellites-available" class="item-value inventory">0</span>
            </div>
            <div class="dashboard-item">
                <span class="item-label">מו"פ פעיל:</span>
                <span id="active-rd" class="item-value rd-status">אין פרויקט</span>
            </div>
             <div class="dashboard-item">
                <span class="item-label">חוזים פוטנציאליים:</span>
                <span id="open-contracts-count" class="item-value contracts-count">3</span>
            </div>
            <div class="dashboard-item">
                <span class="item-label">שיגורים מתוכננים:</span>
                <span id="scheduled-launches-count" class="item-value launches-count">0</span>
            </div>
             <div class="dashboard-item">
                <span class="item-label">שיגורים מוצלחים:</span>
                <span id="successful-launches" class="item-value success-count">0</span>
            </div>
            <div class="dashboard-item">
                <span class="item-label">כישלונות שיגור:</span>
                <span id="failed-launches" class="item-value failure-count">0</span>
            </div>
        </div>
    </section>

    <section class="sim-actions card">
        <h3 class="card-title">קבלת החלטות לתור זה</h3>

        <div class="action-section">
            <h4 class="action-title">חדשנות פורצת דרך (מו"פ) <span class="icon">🔬</span></h4>
            <p class="action-description">השקע בפיתוח טכנולוגיות עתידיות שיעניקו לך יתרון תחרותי.</p>
            <div class="action-controls">
                <select id="rd-choice" class="action-select">
                    <option value="none">-- בחר פרויקט לפיתוח --</option>
                    <option value="advanced-rocket">רקטה דור 2 (יעילות משופרת, עלות שיגור מופחתת)</option>
                    <option value="communication-sat">לוויין תקשורת מהיר (מאפשר חוזים רווחיים יותר)</option>
                    <option value="remote-sensing-sat">לוויין חישה מרחוק (פותח סוגי חוזים חדשים)</option>
                </select>
                <button class="action-button primary-button">התחל מו"פ</button>
            </div>
        </div>

        <div class="action-section">
            <h4 class="action-title">פס ייצור לחלל <span class="icon">🏭</span></h4>
            <p class="action-description">בנה רקטות ולוויינים שישמשו אותך בחוזים עתידיים. זכור, ייצור לוקח זמן ומשאבים!</p>
            <div class="action-controls">
                <input type="number" id="production-amount" value="0" min="0" class="action-input">
                <select id="production-type" class="action-select">
                    <option value="rocket">רקטה</option>
                    <option value="satellite">לוויין</option>
                </select>
                <button class="action-button primary-button">התחל ייצור</button>
            </div>
        </div>

        <div class="action-section">
            <h4 class="action-title">לכידת שוק (חוזים פתוחים) <span class="icon">💼</span></h4>
            <p class="action-description">עיין בחוזים הקיימים בשוק והצע מחיר. כל חוזה דורש ציוד ספציפי ודדליין!</p>
            <div id="open-contracts-list" class="contract-list">
                <!-- Example contract items - JS will populate -->
                <div class="contract-item">
                    <p class="contract-details"><strong>חוזה #1:</strong> לוויין קטן, מסלול LEO, דדליין: תור 4, תשלום מוצע: $20M</p>
                    <button class="action-button secondary-button offer-bid-button">הצע מחיר</button>
                </div>
                <div class="contract-item">
                    <p class="contract-details"><strong>חוזה #2:</strong> לוויין בינוני, מסלול MEO, דדליין: תור 5, תשלום מוצע: $50M</p>
                    <button class="action-button secondary-button offer-bid-button">הצע מחיר</button>
                </div>
                 <div class="contract-item">
                    <p class="contract-details"><strong>חוזה #3:</strong> קבוצת לוויינים, מסלול LEO, דדליין: תור 6, תשלום מוצע: $80M</p>
                    <button class="action-button secondary-button offer-bid-button">הצע מחיר</button>
                </div>
            </div>
        </div>

         <div class="action-section">
            <h4 class="action-title">אל המסלול (שיגורים) <span class="icon">🚀</span></h4>
            <p class="action-description">נהל את החוזים שזכית בהם והקצה להם רקטות ולוויינים מהמלאי.</p>
            <div id="won-contracts-list" class="contract-list">
                 <!-- Example won contract items - JS will populate -->
                 <div class="contract-item">
                     <p class="contract-details">אין חוזים ממתינים לשיגור... צא לזכות בכאלה!</p>
                 </div>
            </div>
            <!-- This could open a modal or reveal more controls in a real sim -->
            <button class="action-button primary-button schedule-launch-button">קבע לוח זמנים לשיגורים</button>
        </div>

        <div class="action-section">
            <h4 class="action-title">ניהול פיננסי <span class="icon">💰</span></h4>
            <p class="action-description">חזק את הקופה לצמיחה עתידית או התמודדות עם קשיים זמניים.</p>
             <button class="action-button secondary-button finance-button">בצע גיוס הון</button>
             <button class="action-button secondary-button finance-button">קח הלוואה</button>
        </div>
    </section>

    <section class="sim-events card">
        <h3 class="card-title">ערוץ עדכונים ואירועים <span class="icon">📰</span></h3>
        <ul id="events-list" class="event-list">
            <!-- Events appear here -->
             <li class="event-item">אין אירועים חדשים בתור זה.</li>
        </ul>
    </section>

    <button id="end-turn-button" class="large-button success-button">סיים תור ועבור לתור הבא <span class="icon">▶️</span></button>
</div>

<style>
    /* גופנים ועיצוב בסיסי */
    #space-sim-container {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        max-width: 960px; /* קצת יותר רחב */
        margin: 30px auto; /* רווח למעלה ולמטה */
        padding: 30px;
        border: none; /* מוסר גבול כללי */
        border-radius: 12px; /* פינות מעוגלות יותר */
        background: linear-gradient(to bottom, #f0f4f8, #d9e2ec); /* רקע עדין */
        color: #333;
        direction: rtl;
        text-align: right;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* צל עדין לאפליקציה */
        position: relative; /* להכנה לאנימציות/אלמנטים ממוקמים */
    }

    .sim-header {
        text-align: center;
        margin-bottom: 30px;
        position: relative;
        padding-bottom: 15px;
    }

     .sim-header h2 {
        color: #0d47a1; /* כחול עמוק */
        margin: 0;
        font-size: 2em;
        font-weight: bold;
    }

    .sim-header .tagline {
        color: #555;
        font-size: 1.1em;
        margin-top: 5px;
    }

     .card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        border-top: 5px solid #0d47a1; /* פס כחול עליון בכרטיסים */
        transition: transform 0.3s ease, box-shadow 0.3s ease; /* אנימציית ריחוף עדינה */
     }

     .card:hover {
         transform: translateY(-5px);
         box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
     }


    .card-title {
        color: #1a237e; /* כחול כהה עוד יותר */
        border-bottom: 2px solid #e3f2fd; /* קו הפרדה עדין */
        padding-bottom: 10px;
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.5em;
    }

    .dashboard-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); /* רשת גמישה */
        gap: 15px; /* מרווח בין פריטים */
    }

    .dashboard-item {
        background-color: #e3f2fd; /* רקע תכלת בהיר */
        padding: 15px;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        align-items: flex-end; /* יישור לימין בתוך הפריט */
        text-align: right;
    }

    .dashboard-item .item-label {
        font-size: 0.9em;
        color: #555;
        margin-bottom: 5px;
    }

    .dashboard-item .item-value {
        font-size: 1.3em;
        font-weight: bold;
        color: #0d47a1; /* כחול */
    }

    /* צבעים ספציפיים למחוונים */
    .item-value.profit { color: #2e7d32; } /* ירוק */
    .item-value.cash { color: #fbc02d; } /* צהוב עמוק */
    .item-value.inventory { color: #0277bd; } /* כחול ים */
    .item-value.rd-status { color: #5e35b1; } /* סגול */
    .item-value.contracts-count { color: #d84315; } /* כתום */
    .item-value.launches-count { color: #004d40; } /* ירוק כהה-טורקיז */
    .item-value.success-count { color: #388e3c; } /* ירוק הצלחה */
    .item-value.failure-count { color: #c62828; } /* אדום כישלון */
     .counter-value { /* מונה תור */
        color: #e65100; /* כתום חזק */
     }


    .action-section {
        margin-bottom: 25px;
        padding-bottom: 15px;
        border-bottom: 1px dashed #b0bec5; /* קו מקווקו עדין */
    }

    .action-section:last-child {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
    }

    .action-title {
        font-size: 1.3em;
        color: #1a237e;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
    }

    .action-title .icon {
        margin-right: 8px;
        font-size: 1.2em;
    }

    .action-description {
        color: #555;
        margin-bottom: 15px;
        font-size: 0.95em;
    }

    .action-controls {
        display: flex;
        flex-wrap: wrap; /* עטיפה למסכים קטנים */
        gap: 10px; /* מרווח בין אלמנטים */
        align-items: center;
    }

     .action-select, .action-input {
        padding: 10px 12px;
        border: 1px solid #b0bec5;
        border-radius: 5px;
        font-size: 1em;
        flex-grow: 1; /* מאפשר התרחבות */
        min-width: 150px; /* רוחב מינימלי */
     }

    /* עיצוב כפתורים - כללי */
    button {
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

    button:active {
        transform: translateY(0);
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }

    /* סוגי כפתורים */
    .primary-button {
        background-color: #1e88e5; /* כחול */
        color: white;
    }

    .primary-button:hover {
        background-color: #1565c0; /* כחול כהה יותר */
    }

    .secondary-button {
        background-color: #e0e0e0; /* אפור בהיר */
        color: #333;
    }

    .secondary-button:hover {
        background-color: #bdbdbd; /* אפור כהה יותר */
    }

    .success-button {
         background-color: #43a047; /* ירוק */
         color: white;
     }

    .success-button:hover {
        background-color: #388e3c; /* ירוק כהה יותר */
    }

    .large-button {
        display: block;
        width: 100%;
        padding: 15px;
        font-size: 1.2em;
        margin-top: 30px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

    .large-button .icon {
        margin-right: 8px;
    }


    .contract-list, .event-list {
        list-style: none;
        padding: 0;
        margin-top: 15px;
    }

    .contract-item, .event-item {
        background-color: #f5f5f5; /* רקע אפור בהיר לפריטים */
        margin-bottom: 10px;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #eee;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

     .contract-item .contract-details {
        margin: 0;
        flex-grow: 1; /* מאפשר לטקסט לתפוס מקום */
        margin-left: 15px; /* רווח בין הטקסט לכפתור */
     }

     .contract-item .action-button {
        flex-shrink: 0; /* מונע כיווץ כפתור */
     }

    .event-item {
        background-color: #e1f5fe; /* רקע תכלת לאירועים */
         border-color: #b3e5fc;
         color: #0277bd;
         justify-content: flex-start; /* אירועים לא צריכים כפתור בדר"כ */
    }

    /* הסבר נפרד */
    #explanation-section {
        margin-top: 30px;
        padding: 25px;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        border-top: 5px solid #e65100; /* פס כתום */
        display: none; /* מוסתר כברירת מחדל */
    }

    #explanation-section h3 {
        color: #e65100; /* כתום חזק */
        border-bottom: 2px solid #ffccbc; /* קו הפרדה כתום עדין */
        padding-bottom: 10px;
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.5em;
    }

    #explanation-section h4 {
        color: #d84315; /* כתום כהה יותר */
        margin-top: 20px;
        margin-bottom: 10px;
    }


    #explanation-section p {
        color: #555;
        margin-bottom: 15px;
    }

    #explanation-section ul {
         list-style: disc;
         padding-right: 20px;
         margin-bottom: 15px;
    }

     #explanation-section ul ul {
        list-style: circle;
        margin-top: 8px;
     }

    #explanation-section li {
        background-color: transparent;
        border: none;
        margin-bottom: 8px;
        padding: 0;
        display: list-item;
        box-shadow: none;
    }

    /* כפתור הצג/הסתר הסבר */
    #toggle-explanation {
        display: block;
        width: fit-content; /* רוחב לפי תוכן */
        margin: 20px auto; /* ממורכז */
        background-color: #546e7a; /* אפור כחלחל */
        color: white;
    }

     #toggle-explanation:hover {
        background-color: #455a64;
     }

     /* אנימציות עדינות */
     @keyframes pulse {
         0% { transform: scale(1); }
         50% { transform: scale(1.02); }
         100% { transform: scale(1); }
     }

    .large-button:hover {
        animation: pulse 0.5s ease-in-out infinite alternate;
    }

    /* פייד אין לתוכן (אם היה טוען דינמית) - כאן רק לצורך דוגמה */
    /* .sim-dashboard, .sim-actions, .sim-events { opacity: 0; animation: fadeIn 0.8s ease forwards; } */
    /* @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } } */


</style>

<button id="toggle-explanation">מה עומד מאחורי המשחק? (הסבר)</button>

<div id="explanation-section">
    <h3>מאחורי הקלעים: הכלכלה והטכנולוגיה של עידן החלל החדש</h3>

    <p>סימולציית "להיות איל חלל" היא מודל פשוט שמטרתו לחשוף אתכם לאתגרים המרכזיים והמורכבות הניהולית של חברה הפועלת בתעשייה שעד לא מזמן הייתה נחלתם הבלעדית של ממשלות. היא ממחישה שהצלחה לא נובעת רק מיכולת טכנית מבריקה, אלא בראש ובראשונה מניהול עסקי, אסטרטגי ופיננסי חכם בסביבה עתירת סיכונים ומשאבים.</p>

    <h4>נושאים מרכזיים שהסימולציה נוגעת בהם:</h4>
    <ul>
        <li><strong>"New Space" - המהפכה הפרטית בחלל:</strong> העידן הנוכחי מאופיין במעבר הדרגתי מדומיננטיות ממשלתית לתפקיד גובר של חברות פרטיות. חברות אלו מביאות חדשנות, יעילות, ומודלים עסקיים חדשים (שיגורים בעלות נמוכה, קונסטלציות לוויינים ענקיות), ופותחות את החלל ליישומים מסחריים רבים יותר.</li>
        <li><strong>מודלים עסקיים עיקריים:</strong> תעשיית החלל מגוונת. שירותי שיגור (הקפצת מטען למסלול), ייצור ומכירת לוויינים (לצרכי תקשורת, צילום, ניווט ועוד), ואספקת שירותים מבוססי-לוויינים (אינטרנט, ניטור סביבתי, ניתוח נתונים) הם רק חלק מהאפשרויות. כל מודל דורש אסטרטגיה שונה וניהול משאבים ייחודי.</li>
        <li><strong>אתגרי ענק בדרך לכוכבים:</strong>
            <ul>
                <li><strong>הון עתק וסיכונים:</strong> פיתוח ובנייה של רקטות ולוויינים דורשים השקעות ראשוניות אדירות. טעות אחת קטנה יכולה להוביל לאסון שיגור - אובדן מידי של מאות מיליוני דולרים, פגיעה במוניטין, ואף קריסה פיננסית.</li>
                <li><strong>זמני פיתוח ארוכים:</strong> מפיתוח טכנולוגיה חדשה ועד למוצר מוכן לשיגור יכולות לעבור שנים רבות. זה דורש סבלנות, ניהול פרויקטים הדוק, ויכולת לשרוף מזומנים לאורך זמן ללא הכנסות מיידיות.</li>
                <li><strong>שוק תחרותי:</strong> מספר השחקנים בשוק גדל, ויש צורך מתמיד לחדש, לייעל ולמצוא נישות ייחודיות כדי לשרוד ולהצליח.</li>
                <li><strong>רגולציה:</strong> תעשיית החלל כפופה לחוקים ותקנות בינלאומיים ומקומיים נוקשים (רישוי, בטיחות, שימוש בתדרים) שיכולים להאט תהליכים ולהוסיף עלויות.</li>
            </ul>
        </li>
        <li><strong>החשיבות הקריטית של ניהול:</strong> ההישרדות והצמיחה של חברת חלל תלויות ביכולת:
            <ul>
                <li><strong>לאזן השקעות:</strong> כמה להקצות למו"פ ארוך טווח לעומת ייצור ומכירות לטווח הקצר?</li>
                <li><strong>לנהל תזרים מזומנים:</strong> כיצד לממן פעילות שוטפת כששיגורים גדולים מניבים הכנסה רק לאחר חודשים או שנים?</li>
                <li><strong>לתמחר נכון:</strong> מהו המחיר האופטימלי לשיגור או לוויין שיאפשר רווח אך גם ימשוך לקוחות?</li>
                <li><strong>לנהל סיכונים:</strong> כיצד להתכונן לכישלונות אפשריים ולהפחית את השפעתם?</li>
            </ul>
        </li>
    </ul>
    <p>הסימולציה מעניקה הצצה זעירה למורכבות העצומה הזו ומזמינה אתכם לחוות, לקבל החלטות ולראות את ההשלכות שלהן על עתיד אימפריית החלל שלכם.</p>
</div>


<script>
    // הגדרת משתנים ראשוניים - אלו הערכים ההתחלתיים של הסימולציה.
    let currentTurn = 1;
    let cashFlow = 10; // תזרים מזומנים נוכחי (במיליוני $)
    let totalProfit = 0; // רווח מצטבר (במיליוני $)
    let rockets = 0; // מלאי רקטות
    let satellites = 0; // מלאי לוויינים
    let activeRD = "אין פרויקט"; // פרויקט מו"פ פעיל
    let successfulLaunches = 0; // מונה שיגורים מוצלחים
    let failedLaunches = 0; // מונה שיגורים כושלים
    let openContractsCount = 3; // מספר חוזים פוטנציאליים בשוק
    let scheduledLaunchesCount = 0; // מספר שיגורים שמחכים לביצוע

    // אלמנטים בממשק שצריך לעדכן
    const turnCounterElement = document.getElementById('turn-counter');
    const cashFlowElement = document.getElementById('cash-flow');
    const totalProfitElement = document.getElementById('total-profit');
    const rocketsAvailableElement = document.getElementById('rockets-available');
    const satellitesAvailableElement = document.getElementById('satellites-available');
    const activeRDElement = document.getElementById('active-rd');
    const successfulLaunchesElement = document.getElementById('successful-launches');
    const failedLaunchesElement = document.getElementById('failed-launches');
    const openContractsCountElement = document.getElementById('open-contracts-count');
    const scheduledLaunchesCountElement = document.getElementById('scheduled-launches-count');
    const eventsListElement = document.getElementById('events-list'); // רשימת אירועים

    // פונקציה לעדכון לוח המחוונים
    function updateDashboard() {
        turnCounterElement.innerText = currentTurn;
        cashFlowElement.innerText = '$' + cashFlow.toFixed(1) + 'M'; // הצגת עשרוני אחד
        // הוספת צבע לפי מצב פיננסי
        if (totalProfit < 0) {
             totalProfitElement.classList.add('failure-count'); // אדום
             totalProfitElement.classList.remove('profit');
        } else {
             totalProfitElement.classList.add('profit'); // ירוק
             totalProfitElement.classList.remove('failure-count');
        }
         if (cashFlow < 0) {
             cashFlowElement.classList.add('failure-count'); // אדום
             cashFlowElement.classList.remove('cash');
        } else {
             cashFlowElement.classList.add('cash'); // צהוב
             cashFlowElement.classList.remove('failure-count');
        }


        totalProfitElement.innerText = '$' + totalProfit.toFixed(1) + 'M';
        rocketsAvailableElement.innerText = rockets;
        satellitesAvailableElement.innerText = satellites;
        activeRDElement.innerText = activeRD;
        successfulLaunchesElement.innerText = successfulLaunches;
        failedLaunchesElement.innerText = failedLaunches;
        openContractsCountElement.innerText = openContractsCount;
        scheduledLaunchesCountElement.innerText = scheduledLaunchesCount;

         // עדכון מצב המו"פ (לצורך הדגמה בלבד, ללא לוגיקה אמיתית)
         if (activeRD !== "אין פרויקט" && currentTurn % 3 === 0) { // נניח שמו"פ לוקח 3 תורות
             addEvent(`🎉 פרויקט המו"פ "${activeRD}" הושלם בהצלחה!`);
             activeRD = "אין פרויקט"; // איפוס לאחר השלמה
         } else if (activeRD !== "אין פרויקט") {
             // עדכון ויזואלי כלשהו על התקדמות (למשל שינוי צבע או טקסט עדין)
             activeRDElement.innerText = `${activeRD} (תור ${currentTurn % 3} מתוך 3)`;
         }

    }

     // פונקציה להוספת אירוע לערוץ העדכונים
     function addEvent(text, isCritical = false) {
         const listItem = document.createElement('li');
         listItem.classList.add('event-item');
          if (isCritical) {
             listItem.style.backgroundColor = '#ffcdd2'; /* רקע אדום בהיר לכישלונות */
             listItem.style.borderColor = '#ef9a9a';
             listItem.style.color = '#c62828';
         }
         listItem.innerText = `[תור ${currentTurn}] ${text}`;
         // הוספה לראש הרשימה (האירועים החדשים למעלה)
         if (eventsListElement.firstChild && eventsListElement.firstChild.innerText === '[אירועים מיוחדים יופיעו כאן]' || eventsListElement.firstChild.innerText === 'אין אירועים חדשים בתור זה.') {
              eventsListElement.innerHTML = ''; // ניקוי הטקסט הראשוני
         }
         eventsListElement.prepend(listItem);

         // אנימציית פייד אין לאירוע חדש (אופציונלי)
          listItem.style.opacity = 0;
          setTimeout(() => { listItem.style.opacity = 1; }, 50); // השהיה קלה לאפשר ל DOM להתעדכן
          listItem.style.transition = 'opacity 0.5s ease-in';
     }


    // הפעלה ראשונית של עדכון המחוונים
    updateDashboard();

    // לוגיקה של הצג/הסתר הסבר
    const toggleButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation-section'); // שיניתי ID

    toggleButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
            toggleButton.innerText = 'הסתר הסבר';
        } else {
            explanationDiv.style.display = 'none';
            toggleButton.innerText = 'מה עומד מאחורי המשחק? (הסבר)';
        }
    });

    // לוגיקה בסיסית של סיום תור (דוגמה בלבד, ללא סימולציה מלאה)
    const endTurnButton = document.getElementById('end-turn-button');
    endTurnButton.addEventListener('click', () => {
        // ניקוי רשימת אירועים לפני התור הבא, הוספת הודעת "אין אירועים" אם אין חדשים
         eventsListElement.innerHTML = '';
          addEvent('מתחילים תור חדש...', false); // הוספת הודעת התחלת תור


        // סימולציה של פעולות אוטומטיות בתחילת תור (מאוד פשטני!)
        let turnEvents = [];
        let turnCashChange = 0;

        // 1. הוצאות קבועות (מו"פ, ייצור, תפעול)
        let operatingCosts = 5; // עלות תפעול בסיסית
        turnCashChange -= operatingCosts;
        turnEvents.push(`הוצאות תפעול ותחזוקה: -$${operatingCosts}M`);

        if (activeRD !== "אין פרויקט") {
            let rdCost = 2; // עלות מו"פ לתור
            turnCashChange -= rdCost;
            turnEvents.push(`עלויות מו"פ לפרויקט "${activeRD}": -$${rdCost}M`);
        }

        // 2. ייצור מסתיים
        // במערכת מלאה, הייצור היה לוקח מספר תורות
        // כאן נניח שייצור שהוזמן בתור קודם מסתיים בהסתברות מסוימת
        // (אין כאן שמירת מצב הזמנות ייצור בפועל, רק הדגמה)
        if (Math.random() > 0.6) { // 40% סיכוי לייצור שהוזמן בעבר להסתיים (הדגמה)
             let producedRockets = Math.floor(Math.random() * 1); // 0 או 1 רקטה
             let producedSats = Math.floor(Math.random() * 2); // 0, 1 או 2 לוויינים
              if (producedRockets > 0 || producedSats > 0) {
                rockets += producedRockets;
                satellites += producedSats;
                turnEvents.push(`🎉 סיום ייצור: ${producedRockets} רקטה, ${producedSats} לוויינים נוספו למלאי!`);
              }
         }


        // 3. שיגורים מתוכננים מתבצעים
        if (scheduledLaunchesCount > 0) {
            for (let i = 0; i < scheduledLaunchesCount; i++) {
                if (Math.random() < 0.9) { // 90% סיכוי להצלחה (דוגמה)
                    successfulLaunches++;
                    let revenue = 40 + Math.random() * 30; // הכנסה מדוגמת
                    turnCashChange += revenue;
                    totalProfit += (revenue * 0.8 - 10); // רווח לאחר עלויות שיגור קבועות
                    turnEvents.push(`✅ שיגור מוצלח! הכנסות: +$${revenue.toFixed(1)}M`);
                } else {
                    failedLaunches++;
                    let penalty = 20 + Math.random() * 30; // קנס מדוגם
                    turnCashChange -= penalty;
                     totalProfit -= (penalty + 50); // עלות כישלון גבוהה יותר
                    turnEvents.push(`💥 כישלון שיגור! הפסד וקנסות: -$${penalty.toFixed(1)}M`, true); // אירוע קריטי
                }
            }
            scheduledLaunchesCount = 0; // כל השיגורים המתוכננים בוצעו
        }


        // 4. חוזים חדשים נפתחים בשוק
         openContractsCount = Math.floor(Math.random() * 4) + 2; // בין 2 ל-5 חוזים חדשים

        // 5. עדכון תזרים מזומנים
        cashFlow += turnCashChange;
        // Total profit כבר מעודכן בהצלחות/כישלונות

        // הוספת אירועים לרשימה
        if (turnEvents.length === 1 && turnEvents[0].includes('מתחילים תור חדש')) {
            addEvent('אין אירועים מיוחדים נוספים בתור זה.');
        } else {
             // האירוע הראשון (התחלת תור) כבר נוסף, מוסיפים את השאר
            for (let i = 1; i < turnEvents.length; i++) {
                 // צריך לטפל גם באירועים קריטיים אם רוצים להוסיף כאן
                addEvent(turnEvents[i]);
            }
        }


        // מעבר לתור הבא
        currentTurn++;

        // עדכון הממשק
        updateDashboard();

        // הודעת סיום תור (ניתן להפוך למשהו ויזואלי יותר)
        // alert('התור הסתיים! עברנו לתור #' + currentTurn);
         // אפשר להציג סיכום תור בכרטיס האירועים

         // בדיקת תנאי סיום משחק פשוט (הפסד)
         if (totalProfit < -100 || cashFlow < -50) { // דוגמה לתנאי כשל
            endTurnButton.disabled = true; // השבתת כפתור
            addEvent("☠️ חברת החלל קרסה! לא הצלחת לשמור על איתנות פיננסית. המשחק הסתיים.", true);
            endTurnButton.innerText = "המשחק הסתיים...";
            endTurnButton.style.backgroundColor = '#c62828';
         }

    });

    // הוספת event listeners לכפתורי פעולה - מקום להוסיף לוגיקה עתידית
    // כרגע הם מציגים הודעת התראה בלבד
    document.querySelectorAll('.action-section button:not(#end-turn-button)').forEach(button => {
        button.addEventListener('click', () => {
            const actionText = button.innerText;
             // לדוגמה, אם לחץ על "התחל מו"פ"
            if (actionText === "התחל מו"פ") {
                 const selectedRD = document.getElementById('rd-choice').value;
                 if (selectedRD !== "none" && activeRD === "אין פרויקט") {
                     activeRD = document.getElementById('rd-choice').options[document.getElementById('rd-choice').selectedIndex].text; // קבל את הטקסט מהאופציה
                     addEvent(`✅ התחלת בפרויקט המו"פ: "${activeRD}". עלויות יקוזזו בתורות הבאים.`);
                     updateDashboard(); // עדכן מיד את המחוון
                 } else if (activeRD !== "אין פרויקט") {
                      alert('כבר קיים פרויקט מו"פ פעיל. המתן לסיומו.');
                 } else {
                     alert('בחר פרויקט מו"פ לפני הלחיצה.');
                 }
            }
            // לדוגמה, אם לחץ על "התחל ייצור"
            else if (actionText === "התחל ייצור") {
                 const amount = parseInt(document.getElementById('production-amount').value);
                 const type = document.getElementById('production-type').value;
                 if (amount > 0) {
                     // במערכת מלאה, זה היה עולה כסף ונכנס לתור ייצור
                     addEvent(`🏗️ הוזמן ייצור של ${amount} יחידות מסוג ${type === 'rocket' ? 'רקטה' : 'לוויין'}. העלות והזמן יתעדכנו.`);
                     // פה היינו מקזזים עלות ייצור והכניסים למצב ייצור
                     updateDashboard();
                 } else {
                     alert('הזן כמות גדולה מ-0 לייצור.');
                 }
            }
             // לדוגמה, אם לחץ על "הצע מחיר"
            else if (button.classList.contains('offer-bid-button')) {
                 const contractDetails = button.parentElement.querySelector('.contract-details').innerText;
                 addEvent(`🤝 הצעת מחיר עבור ${contractDetails.split(':')[1].trim()}. במערכת מלאה, הייתה נדרשת הגשת הצעה ותיתכן זכייה.`);
                  // במערכת מלאה, זה היה פותח ממשק הגשת הצעה
             }
              // לדוגמה, אם לחץ על "קבע לוח זמנים לשיגורים"
            else if (button.classList.contains('schedule-launch-button')) {
                 // במערכת מלאה, זה היה פותח ממשק הקצאת נכסים לשיגורים
                 if (rockets > 0 && satellites > 0 && openContractsCount > 0) { // תנאי הדגמה פשוט
                     let numToSchedule = Math.min(rockets, satellites, Math.floor(openContractsCount/2)); // הדגמה פשוטה
                      if (numToSchedule > 0) {
                        scheduledLaunchesCount += numToSchedule;
                        rockets -= numToSchedule; // קיזוז מהמלאי
                        satellites -= numToSchedule;
                        addEvent(`📅 נקבעו ${numToSchedule} שיגורים לביצוע בתור הבא!`);
                         updateDashboard(); // עדכן מיד את המחוון
                      } else {
                          alert('אין מספיק רקטות/לוויינים או חוזים פוטנציאליים שניתן להקצות לשיגור כרגע.');
                      }

                 } else {
                      alert('ודא שיש לך רקטות ולוויינים במלאי ושיש חוזים פתוחים או זוכים שניתן לשגר.');
                 }
             }
             // לדוגמה, אם לחץ על כפתור פיננסי
             else if (button.classList.contains('finance-button')) {
                 const financeAction = button.innerText;
                 addEvent(`📊 פעלת לביצוע פעולה פיננסית: "${financeAction}". במערכת מלאה, פעולה זו הייתה משפיעה על המאזן.`);
                  // במערכת מלאה, זה היה מניב מזומנים בעלות (ריבית/אחזקות מניות)
             }

             // Fallback for other buttons (if any are added later)
            // else {
            //     alert('לחצת על: ' + button.innerText + '. במערכת מלאה, פעולה זו הייתה מבוצעת/נכנסת לתכנון.');
            // }
        });
    });


</script>