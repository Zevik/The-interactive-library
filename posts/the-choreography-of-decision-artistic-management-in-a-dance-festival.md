---
title: "הכוראוגרפיה של ההחלטה: בניית פסטיבל מחול תחת אילוצים"
english_slug: the-choreography-of-decision-artistic-management-in-a-dance-festival
category: "ניהול תרבות ואמנות"
tags: ["ניהול אמנותי", "פסטיבל מחול", "קבלת החלטות", "אילוצים", "תקציב", "סימולציה"]
---
# הכוראוגרפיה של ההחלטה: בניית פסטיבל מחול תחת אילוצים

דמיינו את עצמכם בלב סערה יצירתית ותקציבית: אתם המנהלים האמנותיים של פסטיבל מחול יוקרתי, יש לכם תקציב וזמן מוגבלים, אבל עולם שלם של אמנים מופלאים מחכה להופיע על הבמה שלכם. כל בחירה היא צעד בכוריאוגרפיה מורכבת. אילו מופעים תעלו? על מה תיאלצו לוותר? איך תאזנו בין חזון, תקציב ולוח זמנים כדי ליצור חוויה בלתי נשכחת?

הסימולטור שלפניכם מזמין אתכם לנעליים של המנהל האמנותי. שחקו, החליטו, התמודדו עם האילוצים - ובנו את הפסטיבל שלכם.

## הסימולטור: האתגר האמנותי והניהולי

<div id="app">
    <div class="constraints-panel">
        <h2>המשאבים שלך: הכלים לבנות את החלום</h2>
        <div class="constraint-item">
            <span class="constraint-label">תקציב כולל:</span>
            <span class="constraint-value" id="total-budget"></span> ₪
        </div>
        <div class="constraint-item">
            <span class="constraint-label">סלוטים זמינים:</span>
            <span class="constraint-value" id="total-slots"></span>
        </div>
        <div class="constraint-item">
            <span class="constraint-label">תקציב שנותר:</span>
            <span class="constraint-value" id="remaining-budget"></span> ₪
        </div>
        <div class="constraint-item">
            <span class="constraint-label">סלוטים בשימוש:</span>
            <span class="constraint-value" id="used-slots"></span> / <span id="total-slots-used-display"></span>
        </div>
    </div>

    <div class="performances-container">
        <div class="available-performances">
            <h2>מאגר האמנים: מי ממתין לבמה?</h2>
            <div id="available-list" class="performance-list">
                <!-- Performance items will be loaded here by JS -->
            </div>
        </div>

        <div class="selected-program">
            <h2>הפסטיבל שלך: התוכנית האמנותית</h2>
            <div id="selected-list" class="performance-list">
                <p id="no-selection-message">רשימת ההמתנה ריקה... התחילו לצרף מופעים מהרשימה משמאל!</p>
            </div>
        </div>
    </div>

    <button id="finish-button" class="action-button primary">סיימתי לבחור! בוא נראה את הפסטיבל שבניתי</button>

    <div id="results" class="results" style="display: none;">
        <h2>סיכום הפסטיבל שבנית: הצלחות ואתגרים</h2>
        <div id="results-content">
            <!-- Results will be loaded here by JS -->
        </div>
        <button id="restart-button" class="action-button secondary">בנו פסטיבל חדש! (התחילו מחדש)</button>
    </div>
</div>

<button id="toggle-explanation" class="action-button outline">למה כל זה חשוב? הצגת ההסבר המלא</button>

<div id="explanation" style="display: none;">
    <h2>מאחורי הקלעים: הכוראוגרפיה של ניהול אמנותי בפסטיבל מחול</h2>
    <p>ניהול אמנותי של פסטיבל אינו רק בחירת יצירות 'יפות'. זהו תפקיד אסטרטגי הדורש ניווט מורכב בין עולם של רעיונות ויצירה לבין אילוצים פרקטיים של תקציב, זמן ולוגיסטיקה. המנהל האמנותי הוא האדריכל של החוויה הכוללת שהקהל יפגוש.</p>

    <h3>מה באמת עושה מנהל אמנותי של פסטיבל?</h3>
    <p>הוא זה שמכתיב את הטון, מגבש את החזון, ואורג את התוכנית האמנותית לכדי שטיח רבגוני ובעל משמעות. זה כולל סקאוטינג (חיפוש וגילוי) אחר אמנים ומופעים, התאמתם לתמה או קו אמנותי מוגדר, ובעיקר - קבלת החלטות קשות לגבי מי נכנס לתוכנית הסופית ומי לא.</p>

    <h3>חזון אמנותי פוגש את המציאות: משאבים ואילוצים</h3>
    <p>לכל פסטיבל יש גבולות. התקציב הוא לרוב המגבלה המשמעותית ביותר - כמה אפשר לשלם לאמנים? כמה עולה שכירות הבמה? כמה עולה טכנולוגיה? מעבר לכסף, יש מגבלות של זמן (כמה ימים הפסטיבל נמשך?) ומרחב (כמה במות זמינות וכמה זמן כל מופע יכול לתפוס? - אלו הם "הסלוטים"). אילוצים אלו הם לא רק מכשולים, אלא גם נקודת מוצא ליצירתיות. עליהם לבחור את השילוב האופטימלי שיניב את הערך האמנותי הגבוה ביותר בתוך המגבלות הנתונות.</p>

    <h3>אמנות הוויתור: הגיבור הבלתי נראה של הניהול האמנותי</h3>
    <p>כמעט תמיד יהיו יותר מופעים ראויים ומרגשים מאשר המשאבים מאפשרים להכיל. היכולת לוותר על אופציות מצוינות היא אולי המיומנות החשובה ביותר. ויתור אסטרטגי על מופע יקר יכול לפנות תקציב וסלוטים למספר מופעים קטנים יותר, להרחיב את מגוון הסגנונות או לאפשר שילוב אמנים צעירים. ניהול אמנותי אינו רק להגיד "כן" למה שטוב, אלא לדעת להגיד "לא" כשהדבר משרת את התמונה הכוללת.</p>

    <h3>לבנות פאזל מושלם: איזון, גיוון וחיבור</h3>
    <p>תוכנית פסטיבל מוצלחת היא יותר מסכום חלקיה. היא יצירה בפני עצמה. המנהל האמנותי שואף ליצור איזון בין סגנונות מחול שונים (קלאסי, עכשווי, רחוב, ניסיוני), לשלב אמנים בעלי שם לצד קולות חדשים, ולעיתים גם לפנות לקהלים מגוונים (מופעי ילדים, סדנאות אינטראקטיביות). המטרה היא ליצור חוויה רצופה, מפתיעה ומעשירה שתשאיר חותם על הקהל.</p>

    <h3>הקשר בין בחירה בודדת למכלול התוכנית</h3>
    <p>כפי שחוויתם בסימולטור, הוספת מופע אחד מיד משפיעה על המשאבים הזמינים ומכתיבה את הבחירות הבאות. בחירה במופע ארוך ויקר פירושה פחות תקציב ופחות סלוטים למופעים אחרים. בחירה בסגנון מסוים עשויה להשפיע על אופי הפסטיבל כולו. זהו משחק שחמט תלת-ממדי, שבו כל מהלך צריך לקחת בחשבון את ההשלכות על כל שאר חלקי הלוח.</p>

    <h3>כיצד הסימולטור האינטראקטיבי ממחיש את כל זה?</h3>
    <p>הסימולטור אפשר לכם להתנסות באופן ישיר באתגרים אלו. הייתם חייבים לקבל החלטות תחת מגבלות ברורות (התקציב והסלוטים). ראיתם בזמן אמת כיצד כל הוספת מופע משפיעה על המשאבים שנותרו. נאלצתם להתמודד עם הפיתוי לצרף את כל המופעים ה'שווים' ביותר, ולהבין שלעיתים זה בא על חשבון הגיוון או ניצול המשאבים. בסיום, הסיכום שהוצג לכם שיקף את התוצאה של הבחירות הניהוליות-אמנותיות שלכם, ואת הוויתורים (הגלויים והסמויים) שהיו כרוכים בתהליך. זוהי טעימה קטנה מעולם מורכב ומרתק, שבו יצירתיות ופרגמטיות רוקדות יחד.</p>
</div>


<style>
    /* Enhanced Styles for a modern, game-like feel */
    :root {
        --primary-color: #0056b3; /* Dark blue */
        --secondary-color: #007bff; /* Blue */
        --accent-color: #28a745; /* Green */
        --danger-color: #dc3545; /* Red */
        --warning-color: #ffc107; /* Yellow */
        --background-color: #f4f7f6; /* Light grey-blue */
        --card-background: #ffffff;
        --border-color: #dee2e6;
        --text-color: #343a40; /* Dark grey */
        --light-text-color: #6c757d; /* Medium grey */
        --hover-transition: all 0.3s ease;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        background-color: var(--background-color);
        color: var(--text-color);
        direction: rtl;
        text-align: right;
        transition: background-color 0.5s ease;
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 20px;
    }
     h2 { margin-top: 25px; }
     h3 { margin-top: 20px; }

    #app {
        background-color: var(--card-background);
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
        overflow: hidden; /* For animations */
    }

    .constraints-panel {
        background-color: #e9ecef;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 30px;
        text-align: center;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }

    .constraint-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-size: 1.1em;
    }

    .constraint-label {
        font-weight: bold;
        color: var(--primary-color);
        margin-bottom: 5px;
    }

    .constraint-value {
        font-size: 1.2em;
        font-weight: bold;
        color: var(--accent-color); /* Default green for good state */
        transition: color 0.3s ease;
    }
     /* Dynamic colors applied by JS for remaining/used */


    .performances-container {
        display: flex;
        gap: 30px;
        flex-wrap: wrap;
    }

    .available-performances, .selected-program {
        flex: 1;
        min-width: 320px; /* Slightly increased min-width */
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        display: flex;
        flex-direction: column;
    }
    .available-performances h2, .selected-program h2 {
         text-align: right; /* Align list titles to the right */
         margin-top: 0;
         margin-bottom: 15px;
         color: var(--text-color);
         font-size: 1.4em;
         border-bottom: 2px solid var(--secondary-color);
         padding-bottom: 10px;
    }


    .performance-list {
        flex-grow: 1;
        max-height: 450px; /* Slightly increased height */
        overflow-y: auto;
        padding-left: 0;
        list-style: none; /* Ensure no bullets if list items were <li> */
         padding-inline-start: 0;
    }

     /* Custom Scrollbar */
    .performance-list::-webkit-scrollbar {
      width: 8px;
    }

    .performance-list::-webkit-scrollbar-track {
      background: #f8f9fa;
      border-radius: 10px;
    }

    .performance-list::-webkit-scrollbar-thumb {
      background: var(--border-color);
      border-radius: 10px;
    }

    .performance-list::-webkit-scrollbar-thumb:hover {
      background: #ced4da;
    }


    .performance-item {
        background-color: var(--card-background);
        border: 1px solid #e0e0e0;
        margin-bottom: 15px;
        padding: 15px;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        gap: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease; /* Add hover transition */
        opacity: 1; /* Base opacity for animation */
        transform: translateY(0); /* Base transform for animation */
    }

    .performance-item:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

     .performance-item strong {
        color: var(--primary-color);
        font-size: 1.1em;
        margin-bottom: 5px;
    }

    .performance-item .details {
        font-size: 0.9em;
        color: var(--light-text-color);
        margin-bottom: 10px;
    }

    .performance-item button {
        align-self: flex-start;
        padding: 8px 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 0.9em;
        font-weight: bold;
        transition: var(--hover-transition);
        min-width: 120px; /* Give buttons a minimum width */
        text-align: center;
    }

    .add-button {
        background-color: var(--accent-color); /* Green */
        color: white;
    }
    .add-button:hover {
        background-color: #218838;
        box-shadow: 0 2px 5px rgba(40, 167, 69, 0.3);
    }

    .remove-button {
        background-color: var(--danger-color); /* Red */
        color: white;
    }
     .remove-button:hover {
        background-color: #c82333;
         box-shadow: 0 2px 5px rgba(220, 53, 69, 0.3);
    }

    #no-selection-message {
        color: var(--light-text-color);
        text-align: center;
        margin-top: 30px;
        font-style: italic;
    }

    .action-button {
        display: block;
        width: auto;
        margin: 25px auto;
        padding: 12px 25px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: var(--hover-transition);
        text-decoration: none; /* In case it's an anchor */
        text-align: center;
    }

    .action-button.primary {
        background-color: var(--secondary-color); /* Blue */
        color: white;
    }
    .action-button.primary:hover {
        background-color: var(--primary-color);
         box-shadow: 0 3px 8px rgba(0, 123, 255, 0.3);
    }

    .action-button.secondary {
        background-color: var(--warning-color); /* Yellow */
        color: var(--text-color);
    }
    .action-button.secondary:hover {
        background-color: #ffae00;
         box-shadow: 0 3px 8px rgba(255, 193, 7, 0.3);
    }

     .action-button.outline {
        background-color: transparent;
        color: var(--light-text-color);
        border: 1px solid var(--light-text-color);
     }
     .action-button.outline:hover {
         color: var(--text-color);
         border-color: var(--text-color);
         background-color: #e9ecef;
     }


    .results {
        background-color: #d4edda; /* Light green background for success/results */
        border: 1px solid #c3e6cb;
        color: #155724; /* Dark green text */
        padding: 30px;
        border-radius: 12px;
        margin-top: 30px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        opacity: 0; /* Start hidden for fade-in */
        transform: translateY(20px); /* Start slightly below for slide-up fade-in */
        transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    }
    .results.visible {
        opacity: 1;
        transform: translateY(0);
    }


    .results h2 {
        color: #0d3b18; /* Darker green */
        text-align: center;
        margin-bottom: 20px;
    }

    .results h3 {
        color: #1a6b2d; /* Mid green */
        margin-top: 25px;
        margin-bottom: 10px;
         text-align: right;
         border-bottom: 1px dashed #a7c7b1;
         padding-bottom: 5px;
    }

    .results p, .results ul {
        margin-bottom: 15px;
        font-size: 1.1em;
        text-align: right;
    }

    .results ul {
        list-style-type: disc;
        padding-right: 25px; /* Indent list items */
    }

    .results li strong {
        color: #0f5132; /* Even darker green */
    }

     .score {
         font-size: 1.8em;
         font-weight: bold;
         color: var(--primary-color);
         text-align: center;
         margin: 20px 0;
         padding: 15px;
         background-color: #fff;
         border-radius: 8px;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
     }
     .score span {
         color: var(--accent-color);
     }


    #toggle-explanation {
        /* Already styled by .action-button.outline */
    }

    #explanation {
        background-color: var(--card-background);
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin-top: 30px;
        opacity: 0; /* Start hidden for fade-in/slide */
        transform: translateY(20px);
        transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    }
     #explanation.visible {
         opacity: 1;
         transform: translateY(0);
     }


    #explanation h2 {
         color: var(--primary-color);
         text-align: right;
         margin-bottom: 20px;
    }
    #explanation h3 {
        color: var(--secondary-color);
        margin-top: 25px;
        margin-bottom: 10px;
        text-align: right;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
    }
    #explanation p {
        margin-bottom: 15px;
        text-align: right;
        color: var(--text-color);
    }


    /* Responsive adjustments */
    @media (max-width: 768px) {
        .performances-container {
            flex-direction: column;
            gap: 20px;
        }
        .available-performances, .selected-program {
            min-width: 100%;
            padding: 15px;
        }
         #app {
             padding: 20px;
         }
         .constraints-panel {
             gap: 10px;
         }
         .constraint-item {
             flex-direction: row;
             gap: 5px;
             font-size: 1em;
         }
         .constraint-label {
             margin-bottom: 0;
         }
         .performance-item {
             padding: 10px;
         }
         .performance-item button {
             width: 100%;
             text-align: center;
             min-width: auto;
         }
         .action-button {
             width: 95%;
             padding: 10px 15px;
             font-size: 1em;
         }
         .results, #explanation {
             padding: 20px;
         }
    }

    @media (max-width: 480px) {
        h1 { font-size: 1.8em; }
        h2 { font-size: 1.5em; }
        h3 { font-size: 1.2em; }
         .performance-item .details { font-size: 0.85em; }
         .score { font-size: 1.5em; }
         body { padding: 10px; }
         #app { padding: 15px; }
         .results, #explanation { padding: 15px; }
    }


     /* Animation for adding/removing items */
     @keyframes fadeIn {
         from { opacity: 0; transform: translateY(10px); }
         to { opacity: 1; transform: translateY(0); }
     }

    @keyframes fadeOut {
        from { opacity: 1; transform: translateY(0); }
        to { opacity: 0; transform: translateY(10px); }
    }

    .performance-item.adding {
         animation: fadeIn 0.5s ease-out;
    }
     .performance-item.removing {
         animation: fadeOut 0.5s ease-out forwards; /* forwards keeps final state */
     }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const totalBudget = 50000; // Total budget in ₪
        const totalSlots = 10; // Total available time slots

        let currentBudgetUsed = 0;
        let currentSlotsUsed = 0;
        let selectedPerformanceIds = [];

        // Performance Data - Added more descriptive text
        const performances = [
            { id: 1, title: 'סולו עכשווי: "נשימה"', artist: 'אורי כהן', cost: 8000, slots: 1, style: 'עכשווי', level: 'Established', description: 'סולו עוצר נשימה, חקירה פיזית ורגשית של גבולות הגוף.', tech: 'במה מינימליסטית, תאורת אווירה.' },
            { id: 2, title: 'דואט: "נקודת מפגש"', artist: 'דניאל ונועה', cost: 12000, slots: 2, style: 'עכשווי', level: 'Established', description: 'דיאלוג תנועתי עוצמתי המבטא חיבור וריחוק.', tech: 'דגש על תאורה דינמית, שטח במה בינוני.' },
            { id: 3, title: 'קבוצה: "פולחן האביב" (קטעים נבחרים)', artist: 'להקת המחול הירושלמית', cost: 25000, slots: 3, style: 'מודרני/קלאסי', level: 'Renowned', description: 'ביצוע מרהיב לאבן דרך היסטורית במחול, בקנה מידה גדול.', tech: 'דורש במה רחבה, תפאורה ותלבושות.' },
            { id: 4, title: 'פרויקט קהילתי: "קולות שכונה"', artist: 'מרכז המחול העירוני', cost: 7000, slots: 1, style: 'קהילתי/מעורב', level: 'Emerging', description: 'מופע סוחף הנוצר בשיתוף תושבי העיר, מלא חיים וצבע.', tech: 'ניתן להופיע בחללים לא קונבנציונליים, גמיש טכנית.' },
            { id: 5, title: 'פלמנקו: "שורשים בוערים"', artist: 'מריה גارسיה ולהקתה', cost: 15000, slots: 2, style: 'פלמנקו', level: 'Established', description: 'ערב פלמנקו אותנטי ומרגש, עם רקדנים ונגנים מהשורה הראשונה.', tech: 'דורש רצפת עץ קשיחה, מערכת סאונד איכותית.' },
            { id: 6, title: 'היפ הופ: "הביט ברחוב"', artist: 'סטודיו ביט', cost: 9000, slots: 1, style: 'היפ הופ/ברייקדאנס', level: 'Emerging', description: 'מופע קצבי ואנרגטי שסוחף את הקהל, מציג את הטופ של תרבות ההיפ הופ המקומית.', tech: 'דורש רצפה חלקה, מערכת הגברה חזקה.' },
            { id: 7, title: 'מחול תיאטרון: "הצל העצמי"', artist: 'קבוצת אלטרנטיבה', cost: 18000, slots: 3, style: 'מחול תיאטרון', level: 'Established', description: 'יצירה בימתית נועזת המשלבת תנועה, טקסט ו-וידאו ארט בנושא זהות.', tech: 'דורש ציוד הקרנה מתקדם, סאונד מדויק.' },
            { id: 8, title: 'סולו מינימליסטי: "ריחוף"', artist: 'אלה שלו', cost: 6000, slots: 1, style: 'עכשווי/מינימליסטי', level: 'Emerging', description: 'מדיטציה תנועתית על הבמה, חוקרת עדינות ונוכחות בחלל.', tech: 'במה נקייה, תאורה סופר-עדינה.' },
            { id: 9, title: 'אנסמבל: "רסיסי זיכרון"', artist: 'סטודיו דגש', cost: 14000, slots: 2, style: 'עכשווי', level: 'Established', description: 'יצירה קבוצתית מרשימה המשלבת קומפוזיציה מורכבת וטכניקה וירטואוזית.', tech: 'דורש שטח במה בינוני.' },
            { id: 10, title: 'מחול לילדים: "הרפתקה בארץ הדמיון"', artist: 'תיאטרון תנועה לילדים', cost: 10000, slots: 1, style: 'מחול לילדים', level: 'Established', description: 'מופע קסום ואינטראקטיבי שסוחף את הילדים וההורים למסע בעולם המחול.', tech: 'תפאורה קלה וצבעונית.' },
             { id: 11, title: 'כיתת אמן + הדגמה', artist: 'אמן אורח בינלאומי: ז׳אן-פול דובואה', cost: 20000, slots: 1, style: 'סדנה/הדגמה', level: 'Renowned', description: 'הזדמנות נדירה ללמוד ולצפות בעבודה של אמן בעל שם עולמי.', tech: 'סטודיו מרווח או במה, מערכת הגברה.' },
             { id: 12, title: 'דואט קצר: "מבט בעיניים"', artist: 'ליאור ורום', cost: 5000, slots: 1, style: 'עכשווי', level: 'Emerging', description: 'עבודה אינטימית ומרגשת החוקרת את כוחו של קשר אנושי.', tech: 'במה קטנה, תאורה נקודתית פשוטה.' }
        ];

        // DOM Elements
        const totalBudgetEl = document.getElementById('total-budget');
        const totalSlotsEl = document.getElementById('total-slots');
        const remainingBudgetEl = document.getElementById('remaining-budget');
        const usedSlotsEl = document.getElementById('used-slots');
        const totalSlotsUsedDisplayEl = document.getElementById('total-slots-used-display');
        const availableListEl = document.getElementById('available-list');
        const selectedListEl = document.getElementById('selected-list');
        const noSelectionMessageEl = document.getElementById('no-selection-message');
        const finishButton = document.getElementById('finish-button');
        const resultsEl = document.getElementById('results');
        const resultsContentEl = document.getElementById('results-content');
        const restartButton = document.getElementById('restart-button');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationEl = document.getElementById('explanation');

        // Initial Display Setup
        totalBudgetEl.textContent = totalBudget.toLocaleString();
        totalSlotsEl.textContent = totalSlots;
        totalSlotsUsedDisplayEl.textContent = totalSlots;

        // Function to update budget and slots display
        function updateConstraintsDisplay() {
            const remaining = totalBudget - currentBudgetUsed;
            const used = currentSlotsUsed;

            remainingBudgetEl.textContent = remaining.toLocaleString();
            usedSlotsEl.textContent = used;

            // Update colors based on state
            remainingBudgetEl.style.color = (remaining < 0) ? varExists('--danger-color') : (remaining < totalBudget * 0.2 ? varExists('--warning-color') : varExists('--accent-color'));
            usedSlotsEl.style.color = (used > totalSlots) ? varExists('--danger-color') : (used > totalSlots * 0.8 ? varExists('--warning-color') : varExists('--accent-color'));
        }

        // Helper to get CSS variable or fallback
        function varExists(name, fallback = '#000') {
            const style = getComputedStyle(document.documentElement);
            return style.getPropertyValue(name) || fallback;
        }


        // Function to render the list of available performances
        function renderAvailablePerformances() {
            availableListEl.innerHTML = '';
            performances.forEach(perf => {
                const isSelected = selectedPerformanceIds.includes(perf.id);
                 // Check if adding this performance exceeds limits
                 const canAdd = !isSelected && (currentBudgetUsed + perf.cost <= totalBudget) && (currentSlotsUsed + perf.slots <= totalSlots);

                const itemEl = document.createElement('div');
                itemEl.classList.add('performance-item');
                 if (!canAdd && !isSelected) {
                    itemEl.classList.add('cannot-add'); // Optional: add a class for styling unavailable items
                    // itemEl.style.opacity = 0.5; // Visual hint that it cannot be added
                    // itemEl.style.pointerEvents = 'none'; // Disable clicks? Maybe too harsh.
                 }

                itemEl.innerHTML = `
                    <strong>${perf.title}</strong> (${perf.artist})
                    <div class="details">
                        עלות: ${perf.cost.toLocaleString()} ₪ | סלוטים: ${perf.slots} | סגנון: ${perf.style} | רמה: ${perf.level}
                        <br><strong>תיאור:</strong> ${perf.description}
                        <br><strong>הערות טכניות:</strong> ${perf.tech}
                    </div>
                    <button class="${isSelected ? 'remove-button' : 'add-button'}" data-id="${perf.id}" ${!canAdd && !isSelected ? 'disabled' : ''}>
                        ${isSelected ? 'הסר מהתוכנית' : 'צרף לתוכנית'}
                    </button>
                `;
                 const button = itemEl.querySelector('button');
                 if (button) {
                     button.addEventListener('click', handleItemButtonClick);
                 }
                availableListEl.appendChild(itemEl);
            });
        }

        // Function to render the list of selected performances
        function renderSelectedProgram() {
            selectedListEl.innerHTML = '';
            if (selectedPerformanceIds.length === 0) {
                noSelectionMessageEl.style.display = 'block';
            } else {
                noSelectionMessageEl.style.display = 'none';
                selectedPerformanceIds.forEach(id => {
                    const perf = performances.find(p => p.id === id);
                     if (!perf) return;
                    const itemEl = document.createElement('div');
                    itemEl.classList.add('performance-item');
                     itemEl.innerHTML = `
                        <strong>${perf.title}</strong> (${perf.artist})
                        <div class="details">
                            עלות: ${perf.cost.toLocaleString()} ₪ | סלוטים: ${perf.slots} | סגנון: ${perf.style} | רמה: ${perf.level}
                        </div>
                         <button class="remove-button" data-id="${perf.id}">הסר מהתוכנית</button>
                    `;
                     const button = itemEl.querySelector('button');
                     if (button) {
                         button.addEventListener('click', handleItemButtonClick);
                     }
                    selectedListEl.appendChild(itemEl);
                });
            }
        }

        // Handler for add/remove button clicks
        function handleItemButtonClick(event) {
            const button = event.target;
            const performanceId = parseInt(button.dataset.id);
            const performance = performances.find(p => p.id === performanceId);

            if (!performance) return;

            const isCurrentlySelected = selectedPerformanceIds.includes(performanceId);
            const itemElement = button.closest('.performance-item'); // Get the parent item for animation

            if (isCurrentlySelected) {
                // Remove performance
                 itemElement.classList.add('removing'); // Add animation class
                 // Wait for animation to finish before removing from DOM and data
                 itemElement.addEventListener('animationend', () => {
                    selectedPerformanceIds = selectedPerformanceIds.filter(id => id !== performanceId);
                    currentBudgetUsed -= performance.cost;
                    currentSlotsUsed -= performance.slots;
                    updateConstraintsDisplay();
                    renderAvailablePerformances(); // Update available list buttons
                    renderSelectedProgram(); // Re-render selected list (or just remove the item)
                 }, { once: true }); // Run event listener only once

            } else {
                // Add performance - check constraints first
                if (currentBudgetUsed + performance.cost <= totalBudget && currentSlotsUsed + performance.slots <= totalSlots) {
                    selectedPerformanceIds.push(performanceId);
                    currentBudgetUsed += performance.cost;
                    currentSlotsUsed += performance.slots;
                    updateConstraintsDisplay();
                    renderAvailablePerformances(); // Update available list buttons
                    renderSelectedProgram(); // Re-render selected list
                     // itemElement.classList.add('adding'); // Add animation class (Might need to add to the new item in selected list)
                } else {
                     let message = 'לא ניתן לצרף מופע זה:';
                     if (currentBudgetUsed + performance.cost > totalBudget) {
                         message += '\n- חורג מהתקציב הזמין.';
                     }
                     if (currentSlotsUsed + performance.slots > totalSlots) {
                         message += '\n- חורג ממספר הסלוטים הזמינים.';
                     }
                     alert(message); // Use a more specific alert
                    // Add visual feedback to constraints display? (Advanced - skip for now)
                }
            }
        }

        // Function to evaluate the selected program and calculate a score
        function evaluateProgram() {
            const selected = performances.filter(p => selectedPerformanceIds.includes(p.id));
            const evaluation = {};

            // Basic Metrics
            evaluation.budgetUsed = currentBudgetUsed;
            evaluation.slotsUsed = currentSlotsUsed;
            evaluation.budgetUtilization = (currentBudgetUsed / totalBudget) * 100;
            evaluation.slotUtilization = (currentSlotsUsed / totalSlots) * 100;
            evaluation.numPerformances = selected.length;

            // Artistic Diversity
            const uniqueStyles = new Set(selected.map(p => p.style));
            const uniqueLevels = new Set(selected.map(p => p.level));
            evaluation.styleDiversity = uniqueStyles.size;
            evaluation.levelDiversity = uniqueLevels.size;
            const totalUniqueStylesAvailable = new Set(performances.map(p => p.style)).size;
            const totalUniqueLevelsAvailable = new Set(performances.map(p => p.level)).size;
            const renownedArtistsSelected = selected.filter(p => p.level === 'Renowned').length;
            const emergingArtistsSelected = selected.filter(p => p.level === 'Emerging').length;


            // Score Calculation (Simple Logic)
            let score = 0;
             score += selected.length * 200; // Base points per performance
             score += evaluation.budgetUsed / 50; // Points for using budget
             score += evaluation.slotsUsed * 100; // Points for using slots

            score += evaluation.styleDiversity * 500; // Bonus for style diversity
            score += evaluation.levelDiversity * 500; // Bonus for level diversity

            score += renownedArtistsSelected * 1000; // Bonus for renowned artists
            score += emergingArtistsSelected * 300; // Bonus for emerging artists

            // Utilization Bonuses
            if (evaluation.budgetUtilization > 90) score += 1500;
             else if (evaluation.budgetUtilization > 70) score += 750;
             if (evaluation.slotUtilization > 90) score += 1500;
             else if (evaluation.slotUtilization > 70) score += 750;

            // Penalties (shouldn't happen with current add logic, but good practice)
            if (evaluation.budgetUsed > totalBudget) score -= (evaluation.budgetUsed - totalBudget) * 10;
            if (evaluation.slotsUsed > totalSlots) score -= (evaluation.slotsUsed - totalSlots) * 500;

             score = Math.max(0, score); // Score cannot be negative
             evaluation.score = Math.round(score); // Round for cleaner display


            // Strategic Choices / Challenges Faced (Rephrased from Compromises)
            evaluation.strategicChoices = [];
            const remainingBudget = totalBudget - evaluation.budgetUsed;
            const remainingSlots = totalSlots - evaluation.slotsUsed;

            if (remainingBudget > totalBudget * 0.2 && evaluation.numPerformances < performances.length) {
                evaluation.strategicChoices.push('נותר תקציב משמעותי שלא נוצל. ייתכן שיכולתם לשלב מופעים יקרים יותר, או פשוט בחרתם בתוכנית חסכונית יותר.');
            } else if (remainingBudget < 1000 && evaluation.budgetUsed > totalBudget * 0.8) {
                 evaluation.strategicChoices.push('ניצלתם את התקציב ביעילות רבה! סביר להניח שהייתם צריכים לשקול היטב כל שקל.');
            }

             if (remainingSlots > totalSlots * 0.2 && evaluation.numPerformances < performances.length) {
                evaluation.strategicChoices.push('נותרו סלוטים פנויים. אולי יכולתם להכניס מופעים נוספים או להאריך חלק מהקיימים? לחלופין, אולי בחרתם בכוונה בתוכנית קצרה וממוקדת יותר.');
             } else if (remainingSlots === 0 && evaluation.slotsUsed > totalSlots * 0.8) {
                evaluation.strategicChoices.push('ניצלתם את כל הסלוטים הזמינים. האם מגבלת הזמן השפיעה על הבחירות שלכם?');
             }


            const stylesCoveredRatio = evaluation.styleDiversity / totalUniqueStylesAvailable;
             const levelsCoveredRatio = evaluation.levelDiversity / totalUniqueLevelsAvailable;

             if (stylesCoveredRatio < 0.5) {
                 evaluation.strategicChoices.push(`התוכנית מציגה רק ${evaluation.styleDiversity} סגנונות מתוך ${totalUniqueStylesAvailable} אפשריים. ייתכן שהגיוון הסגנוני נפגע כדי לעמוד באילוצים או להעדיף סגנונות מסוימים.`);
             } else if (stylesCoveredRatio >= 0.8) {
                 evaluation.strategicChoices.push('הצלחתם לכלול מגוון רחב מאוד של סגנונות מחול!');
             }

            if (levelsCoveredRatio < 0.5) {
                 evaluation.strategicChoices.push(`התוכנית כוללת אמנים רק מ-${evaluation.levelDiversity} רמות מתוך ${totalUniqueLevelsAvailable} אפשריות. אולי היה קשה לאזן בין אמנים מבוססים לצעירים בתקציב הנתון?`);
             } else if (levelsCoveredRatio >= 0.8) {
                evaluation.strategicChoices.push('יצרתם שילוב מאוזן בין אמנים ברמות שונות.');
            }


             // Check for specific high-impact items not selected
             const highImpactItems = performances.filter(p => p.cost >= 15000 || p.slots >= 3);
             const highImpactSelected = selected.filter(p => p.cost >= 15000 || p.slots >= 3);
             if (highImpactItems.length > 0 && highImpactSelected.length < highImpactItems.length / 2) {
                 evaluation.strategicChoices.push(`היו מופעים "כבדים" יותר (יקרים או ארוכים) שלא נכללו בתוכנית. האם נאלצתם לוותר עליהם כדי לפנות מקום או תקציב למופעים אחרים?`);
             } else if (highImpactSelected.length > 0) {
                evaluation.strategicChoices.push(`שילבתם מופעים בעלי עלות או משך גבוהים בתוכנית - דורש ניהול משאבים קפדני!`);
             }


            if (evaluation.strategicChoices.length === 0 && evaluation.budgetUtilization > 70 && evaluation.slotUtilization > 70 && evaluation.numPerformances > 3) {
                 evaluation.strategicChoices.push('נראה שבניתם תוכנית מאוזנת ויעילה ללא התנגשויות או ויתורים משמעותיים בולטים. עבודה מצוינת!');
             }


            return evaluation;
        }

        // Function to display the results
        function displayResults() {
            const evaluation = evaluateProgram();
            resultsContentEl.innerHTML = `
                <div class="score">הציון שלך: <span>${evaluation.score.toLocaleString()}</span></div>

                <h3>התוכנית שבניתם:</h3>
                <ul>
                    ${selectedPerformanceIds.length > 0 ?
                     selectedPerformanceIds.map(id => {
                        const perf = performances.find(p => p.id === id);
                        return perf ? `<li><strong>${perf.title}</strong> (${perf.artist}) - ${perf.cost.toLocaleString()} ₪, ${perf.slots} סלוטים, סגנון: ${perf.style}</li>` : '';
                    }).join('')
                    : '<li>לא נבחרו מופעים לתוכנית.</li>'
                    }
                </ul>
                <h3>ניתוח ביצועים:</h3>
                <p><strong>ניצול תקציב:</strong> ${evaluation.budgetUsed.toLocaleString()} ₪ מתוך ${totalBudget.toLocaleString()} ₪ (${evaluation.budgetUtilization.toFixed(1)}%)</p>
                <p><strong>ניצול סלוטים:</strong> ${evaluation.slotsUsed} מתוך ${totalSlots} (${evaluation.slotUtilization.toFixed(1)}%)</p>
                 <p><strong>מספר מופעים בתוכנית:</strong> ${evaluation.numPerformances}</p>
                <p><strong>גיוון אמנותי:</strong> התוכנית כוללת ${evaluation.styleDiversity} סגנונות מחול שונים ומשלבת אמנים מ-${evaluation.levelDiversity} רמות שונות.</p>

                <h3>נקודות למחשבה אסטרטגית:</h3>
                <p>תהליך הבנייה של פסטיבל הוא תמיד סיפור של קבלת החלטות תחת מגבלות. הבחירות שעשיתם הובילו לתוצאות הבאות:</p>
                <ul>
                    ${evaluation.strategicChoices.length > 0 ? evaluation.strategicChoices.map(comp => `<li>${comp}</li>`).join('') : '<li>ניתוח הבחירות מראה שהתוכנית יעילה ומאוזנת מאוד ביחס למשאבים!</li>'}
                </ul>

                 <p>כפי שראיתם, כל מופע שצורף או הוסר השפיע על הפאזל כולו. ניהול אמנותי מוצלח דורש יכולת ראייה מערכתית, לצד אומץ לב אמנותי והבנה מעשית של המגבלות בשטח.</p>

            `;
            resultsEl.style.display = 'block';
            // Add visible class for animation
             setTimeout(() => resultsEl.classList.add('visible'), 10); // Small delay to allow display change

             // Hide simulation elements
             finishButton.style.display = 'none';
             availableListEl.parentElement.style.display = 'none';
             selectedListEl.parentElement.style.display = 'none';
             document.querySelector('.constraints-panel').style.display = 'none';
             toggleExplanationButton.style.display = 'block'; // Ensure toggle button is visible
        }

        // Function to restart the simulation
        function restartSimulation() {
            currentBudgetUsed = 0;
            currentSlotsUsed = 0;
            selectedPerformanceIds = [];

            updateConstraintsDisplay();
            renderAvailablePerformances();
            renderSelectedProgram();

            // Hide results and show simulation elements
            resultsEl.classList.remove('visible'); // Remove class to reset animation
            resultsEl.style.display = 'none'; // Hide it fully after animation potential

            finishButton.style.display = 'block';
            availableListEl.parentElement.style.display = 'block';
            selectedListEl.parentElement.style.display = 'block';
            document.querySelector('.constraints-panel').style.display = 'flex'; // Restore flex display
             toggleExplanationButton.style.display = 'block'; // Ensure toggle button is visible
             explanationEl.classList.remove('visible');
             explanationEl.style.display = 'none';
             toggleExplanationButton.textContent = 'למה כל זה חשוב? הצגת ההסבר המלא';
        }

         // Function to toggle explanation visibility
         function toggleExplanation() {
             const isHidden = explanationEl.style.display === 'none';
             if (isHidden) {
                explanationEl.style.display = 'block';
                 setTimeout(() => explanationEl.classList.add('visible'), 10);
                 toggleExplanationButton.textContent = 'הסתר הסבר מלא';
             } else {
                 explanationEl.classList.remove('visible');
                 explanationEl.addEventListener('transitionend', () => {
                     explanationEl.style.display = 'none';
                 }, { once: true });
                 toggleExplanationButton.textContent = 'למה כל זה חשוב? הצגת ההסבר המלא';
             }
         }


        // Event Listeners
        finishButton.addEventListener('click', displayResults);
        restartButton.addEventListener('click', restartSimulation);
        toggleExplanationButton.addEventListener('click', toggleExplanation);

        // Initial Render
        updateConstraintsDisplay();
        renderAvailablePerformances();
        renderSelectedProgram();
    });
</script>
```