---
title: "אמנות של החלטות: סימולטור אוצר מוזיאון"
english_slug: art-decision-making-museum-curator-simulator
category: "כלכלה התנהגותית"
tags:
  - קבלת החלטות
  - אומנות
  - מוזיאון
  - אוצרות
  - כלכלה התנהגותית
---
# אמנות של החלטות: סימולטור אוצר מוזיאון

ברוכים הבאים לתפקיד אוצר המוזיאון! בפניכם עומדת הזדמנות נדירה לגבש את אוסף האמנות העתידי של המוסד, אך התקציב מוגבל והבחירות רבות. איך תשקללו בין שם האמן הנוצץ למחיר הנגיש? בין חשיבות היסטורית פוטנציאלית למשיכת קהל ויראלית? צללו עמוק לתוך האתגר המרתק של קבלת החלטות בעולם האמנות, שבו כל בחירה מעצבת את עתיד המוזיאון.

<div id="app">
    <div class="app-header">
        <h2>אמנות של החלטות: גלריית רכישה</h2>
        <div id="budget-info" class="info-box">
            <p>💸 תקציב כולל: <span id="total-budget" class="budget-value"></span> ₪</p>
            <p>Remaining budget: <span id="remaining-budget" class="budget-value"></span> ₪</p>
            <p>סה"כ עלות בחירה: <span id="selected-cost" class="budget-value">0</span> ₪</p>
        </div>
    </div>

    <h3>מועמדות פוטנציאליות לאוסף:</h3>
    <div id="artwork-list">
        <!-- Artworks will be loaded here by JavaScript -->
    </div>

    <div id="selection-area">
        <h3>הבחירות שלכם לאוסף:</h3>
        <div id="selected-artworks" class="info-box">
            <p id="no-selection-message">עדיין לא הוספתם יצירות לאוסף.</p>
            <ul id="selection-list">
                <!-- Selected artworks will be listed here -->
            </ul>
        </div>
        <button id="submit-selection" class="action-button primary">סיימתי! הצג משוב אוצרותי</button>
    </div>


    <div id="results" class="hidden feedback-box">
        <h3>🔍 משוב על החלטות הרכישה שלכם:</h3>
        <div id="feedback-content">
            <!-- Feedback will be displayed here -->
        </div>
        <button id="restart-simulation" class="action-button secondary">התחילו סיבוב רכישה חדש</button>
    </div>
</div>

<style>
    :root {
        --primary-color: #0056b3; /* Darker blue */
        --secondary-color: #6c757d; /* Grey */
        --accent-color: #28a745; /* Green */
        --warning-color: #dc3545; /* Red */
        --background-light: #f8f9fa; /* Light grey */
        --border-color: #dee2e6; /* Light grey border */
        --selected-bg: #e9f5ff; /* Very light blue */
        --card-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
        --card-hover-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
        --transition-speed: 0.3s;
    }

    #app {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        direction: rtl;
        text-align: right;
        max-width: 900px;
        margin: 20px auto;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--background-light);
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.05);
        line-height: 1.7;
    }

    .app-header {
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px solid var(--border-color);
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
    }
     .app-header h2 {
         margin: 0;
         color: var(--primary-color);
         font-size: 1.8em;
     }


    h3 {
        color: #333;
        margin-top: 25px;
        margin-bottom: 15px;
        border-bottom: 2px solid var(--primary-color);
        display: inline-block;
        padding-bottom: 5px;
    }

    .info-box {
        background-color: #eef7ff; /* Lighter blue background */
        padding: 15px 20px;
        margin-bottom: 20px;
        border-radius: 8px;
        border: 1px solid #cce5ff; /* Light blue border */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
         min-width: 250px; /* Ensure budget box doesn't get too small */
    }
     .info-box p {
         margin: 8px 0;
         font-size: 1em;
         display: flex;
         justify-content: space-between;
         align-items: center;
     }
     .info-box p strong {
         font-weight: normal; /* Make labels less bold */
         color: #555;
     }

     .budget-value {
         font-weight: bold;
         color: var(--accent-color);
         font-family: 'Consolas', 'Courier New', monospace; /* Monospaced for numbers */
         font-size: 1.1em;
     }

     #remaining-budget {
         color: var(--accent-color);
     }
     #remaining-budget.warning {
         color: #ffc107; /* Yellow */
     }
      #remaining-budget.danger {
          color: var(--warning-color);
          animation: pulse-danger 1s infinite;
      }

      #selected-cost.danger {
          color: var(--warning-color);
          animation: pulse-danger 1s infinite;
      }

      @keyframes pulse-danger {
          0% { transform: scale(1); opacity: 1; }
          50% { transform: scale(1.02); opacity: 0.9; }
          100% { transform: scale(1); opacity: 1; }
      }


    #artwork-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 25px;
        margin-bottom: 30px;
    }

    .artwork-item {
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 20px;
        background-color: #fff;
        cursor: pointer;
        transition: transform var(--transition-speed) ease-in-out, box-shadow var(--transition-speed) ease-in-out, border-color var(--transition-speed) ease-in-out;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 240px; /* Ensure cards have similar height */
        position: relative; /* For potential future overlays/icons */
        box-shadow: var(--card-shadow);
    }

    .artwork-item:hover {
        transform: translateY(-7px);
        box-shadow: var(--card-hover-shadow);
    }

    .artwork-item.selected {
        border-color: var(--primary-color);
        box-shadow: 0 0 15px rgba(0, 86, 179, 0.4); /* More prominent shadow */
        background-color: var(--selected-bg);
        transform: translateY(-3px); /* Keep slightly raised */
    }

    .artwork-item h4 {
        margin-top: 0;
        margin-bottom: 8px;
        color: var(--primary-color);
        font-size: 1.2em;
        border-bottom: 1px dashed var(--border-color);
        padding-bottom: 5px;
    }

    .artwork-item p {
        margin: 5px 0;
        font-size: 0.95em;
        color: #555;
    }
     .artwork-item p strong {
         color: #333;
     }

    .artwork-item .price {
        font-weight: bold;
        color: var(--accent-color);
        font-size: 1.1em;
        margin-top: auto; /* Push price to bottom */
        text-align: left; /* Price on the left */
        padding-top: 10px;
        border-top: 1px solid #eee;
    }
     .artwork-item .price::before {
         content: "מחיר: ";
         font-weight: normal;
         color: #555;
         font-size: 0.9em;
     }
     .artwork-item .price span {
         font-family: 'Consolas', 'Courier New', monospace;
     }


    #selection-area {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid var(--border-color);
    }

    #selected-artworks {
        margin-top: 15px;
        min-height: 80px; /* Give it some default height */
    }

    #no-selection-message {
        text-align: center;
        color: #777;
        font-style: italic;
    }

    #selection-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    #selection-list li {
        background-color: #ffffff;
        border: 1px solid #cce5ff; /* Match info box border */
        margin-bottom: 8px;
        padding: 10px 15px;
        border-radius: 5px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 1em;
        color: #333;
        opacity: 1;
        transition: opacity var(--transition-speed) ease-in-out, transform var(--transition-speed) ease-in-out;
    }

    #selection-list li.adding {
        opacity: 0;
        transform: translateX(-20px);
    }
    #selection-list li.removing {
         opacity: 0;
         transform: translateX(20px);
    }


    #selection-list li span {
        font-weight: bold;
        color: var(--primary-color);
         font-family: 'Consolas', 'Courier New', monospace;
    }

    .action-button {
        display: block;
        width: auto;
        margin: 30px auto 10px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        color: #fff;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color var(--transition-speed) ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .action-button.primary {
        background-color: var(--primary-color);
    }
    .action-button.primary:hover {
        background-color: #004085; /* Darker primary */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    .action-button.secondary {
        background-color: var(--secondary-color);
        margin-top: 15px;
    }
     .action-button.secondary:hover {
         background-color: #545b62; /* Darker secondary */
          box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
     }

     .action-button:active {
         transform: scale(0.98); /* Subtle press effect */
     }


    .feedback-box {
        margin-top: 30px;
        padding: 25px;
        border-radius: 8px;
        color: #155724; /* Dark green */
        background-color: #d4edda; /* Light green */
        border: 1px solid #c3e6cb; /* Green border */
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.08);
         transition: opacity var(--transition-speed) ease, transform var(--transition-speed) ease;
         opacity: 1;
         transform: translateY(0);
    }

    .feedback-box.hidden {
        opacity: 0;
        transform: translateY(20px);
        pointer-events: none; /* Prevent interaction when hidden */
        position: absolute; /* Or use display: none; if you prefer */
        left: -9999px; /* Hide effectively */
    }


    #results h3 {
        color: #155724; /* Dark green */
         border-bottom-color: #c3e6cb; /* Lighter green border */
         padding-bottom: 8px;
    }

    #feedback-content p {
        margin-bottom: 12px;
        line-height: 1.6;
         color: #333;
    }

     #feedback-content p strong {
         color: #000;
     }

    #feedback-content .warning {
        color: var(--warning-color);
        font-weight: bold;
    }
     #feedback-content .success {
         color: var(--accent-color);
         font-weight: bold;
     }


    #show-explanation {
         display: block;
         width: auto;
         margin: 20px auto;
         padding: 10px 20px;
         font-size: 1em;
         color: #fff;
         background-color: var(--secondary-color);
         border: none;
         border-radius: 5px;
         cursor: pointer;
         transition: background-color 0.3s ease, transform 0.1s ease;
          box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
     #show-explanation:hover {
         background-color: #5a6268;
     }
     #show-explanation:active {
         transform: scale(0.98);
     }

    #explanation {
        margin-top: 30px;
        padding: 25px;
        border-top: 1px solid #ccc;
        background-color: #f1f1f1;
        border-radius: 8px;
         transition: opacity var(--transition-speed) ease, transform var(--transition-speed) ease;
         opacity: 1;
         transform: translateY(0);
    }
     #explanation.hidden {
         opacity: 0;
         transform: translateY(20px);
          pointer-events: none;
          position: absolute;
          left: -9999px;
     }


    #explanation h2, #explanation h3 {
        color: #333;
        margin-top: 15px;
        margin-bottom: 10px;
         border-bottom-color: #ccc;
    }

     #explanation p, #explanation ul {
         line-height: 1.8;
         margin-bottom: 15px;
         color: #555;
     }
     #explanation ul {
         padding-right: 25px;
     }
     #explanation li {
         margin-bottom: 8px;
     }

</style>

<button id="show-explanation">על ההחלטות שמאחורי האמנות: הסבר תיאורטי</button>

<div id="explanation" class="hidden">
    <h2>על ההחלטות שמאחורי האמנות: הסבר תיאורטי</h2>

    <p>
        רכישת יצירות אמנות לאוסף מוזיאוני היא משימה הדורשת הרבה יותר מסתם "אהבה" ליצירה. זוהי החלטה מורכבת המשלבת שיקולים אסתטיים, היסטוריים, תרבותיים, כלכליים ואפילו חברתיים. תהליך זה, כמו תהליכי קבלת החלטות רבים בחיים ובעסקים, מתרחש לרוב תחת <strong>אי-ודאות</strong> ומאופיין בצורך לבצע <strong>פשרות</strong> (Trade-offs) בין מטרות מתנגשות.
    </p>

    <h3>אי-ודאות וקבלת החלטות</h3>
    <p>
        אי-ודאות קיימת כאשר איננו יודעים בוודאות את התוצאות העתידיות של בחירותינו. בשוק האמנות, אי-ודאות זו מתבטאת בהערכות שווי עתידיות שונות, מצב שימור היכול להשתנות, ואף שינויים עתידיים בטעם הקהל או במעמד של אמן מסוים בהיסטוריה. אוצר חייב להעריך סיכונים וסיכויים אלו, לרוב בהתבסס על מידע חלקי ומומחיות.
    </p>

    <h3>מודלים של קבלת החלטות: מרציונליות להטיות</h3>
    <ul>
        <li><strong>המודל ה"רציונלי" הקלאסי:</strong> מניח שיש לנו גישה לכל המידע, אנו מעבדים אותו בצורה מושלמת, ושואפים למקסם "תועלת" אחת (למשל, ערך כספי עתידי או היסטורי). מודל זה שימושי כנקודת ייחוס, אך הוא פשטני מדי עבור מציאות מורכבת כמו רכישת אמנות.</li>
        <li><strong>כלכלה התנהגותית:</strong> תחום זה, עליו מבוסס הסימולטור שלנו במידה רבה, מזהה שאנשים אינם פועלים תמיד בצורה רציונלית לחלוטין. תהליכי החשיבה שלנו מושפעים מקיצורי דרך מנטליים (היוריסטיקות) ו<strong>הטיות קוגניטיביות</strong> שגורמות לנו לסטות מהמודל הרציונלי.</li>
    </ul>

    <h3>הטיות קוגניטיביות נפוצות בעולם האמנות (ומחוצה לו):</h3>
    <p>
        שימו לב כיצד ההטיות הבאות עשויות להשפיע על הבחירות שלכם בסימולטור:
    </p>
    <ul>
        <li><strong>הטיית העוגן (Anchoring Bias):</strong> האם המחיר המבוקש הראשוני (ה"עוגן") השפיע עליכם יותר מדי בהערכת שווי היצירה, גם אם מידע אחר הצביע על הערכה שונה?</li>
        <li><strong>הטיית האישור (Confirmation Bias):</strong> האם חיפשתם באופן לא מודע מידע שתומך ברצונכם לרכוש יצירה מסוימת (כי אהבתם אותה, או כי אתם מכירים את האמן), והתעלמתם מנתונים פחות מחמיאים (מצב שימור, רלוונטיות נמוכה לאוסף)?</li>
        <li><strong>אפקט ההילה (Halo Effect):</strong> האם המוניטין של אמן "כוכב" (כמו אברהם כהן או דניאל שפירא בדוגמאות שלנו) גרם לכם להעריך את יצירותיו כטובות יותר בכל הקריטריונים, או להעדיף אותן על פני יצירות של אמנים פחות מוכרים אך בעלות פוטנציאל אחר?</li>
         <li><strong>שנאת הפסד (Loss Aversion):</strong> האם הנטייה להימנע מהפסד נתפש (למשל, לפספס הזדמנות על יצירה "בטוחה") השפיעה על ההחלטה שלכם יותר מאשר הרצון לזכות ברווח פוטנציאלי (למשל, להמר על יצירה פחות ידועה עם פוטנציאל עתידי גבוה)?</li>
    </ul>

    <h3>קריטריונים ופשרות: הדילמה האוצרותית</h3>
    <p>
        בפועל, אוצרים חייבים לשקלל מגוון קריטריונים:
    </p>
    <ul>
        <li><strong>ערך היסטורי ותרבותי:</strong> האם היצירה משלימה חוסר חשוב באוסף? האם היא מייצגת תקופה, זרם או אמן מרכזי?</li>
        <li><strong>פוטנציאל משיכת קהל:</strong> האם היצירה "מדברת" לקהל הרחב? האם היא ויראלית? אינטראקטיבית? מרשימה ויזואלית?</li>
        <li><strong>פוטנציאל השבחה עתידית:</strong> האם צפוי ששווי היצירה יעלה עם הזמן? האם זו "קנייה טובה" גם בהיבט הכלכלי ארוך הטווח? (קשור גם לאי-ודאות).</li>
        <li><strong>רלוונטיות לאוסף הקיים:</strong> כיצד היצירה החדשה משתלבת בנרטיב האוסף הקיים? האם היא מרחיבה אותו בצורה משמעותית?</li>
        <li><strong>עלות ותחזוקה:</strong> מעבר למחיר הרכישה, יש לשקול עלויות שימור, אחסון, ביטוח ואף עלויות תפעול (ביצירות דיגיטליות/אינטראקטיביות).</li>
    </ul>
    <p>
        המגבלה התקציבית מכריחה לבצע פשרות: רכישת יצירה יקרה אחת בעלת חשיבות רבה עשויה לבוא על חשבון רכישת מספר יצירות זולות יותר המגוונות את האוסף. בחירה ביצירה בעלת פוטנציאל קהל גבוה אך חשיבות היסטורית פחותה היא פשרה אחרת. המשוב בסימולטור נועד לעזור לכם לזהות אילו פשרות ביצעתם וכיצד הן משתלבות עם יעדים אוצרותיים שונים.
    </p>

    <h3>שקיפות ואחריות: קבלת החלטות במוסדות ציבוריים</h3>
    <p>
        במוזיאונים ציבוריים, קבלת החלטות רכישה היא תהליך בעל אחריות ציבורית. חשוב שהקריטריונים יהיו ברורים ושקופים ככל האפשר, שתהליך הבחירה יכלול מגוון מומחים (ועדות רכישה), ושייעשה תיעוד מפורט של השיקולים. שקיפות זו מסייעת להבטיח שהאוסף נבנה בצורה מושכלת ואחראית, למען הציבור ולמען הדורות הבאים. הסימולטור מאפשר לכם להתנסות באופן אישי במורכבות זו.
    </p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const totalBudget = 1000000; // 1,000,000 ₪
        let remainingBudget = totalBudget;
        let selectedArtworks = [];

        // DOM Elements
        const budgetInfoDiv = document.getElementById('budget-info');
        const totalBudgetSpan = document.getElementById('total-budget');
        const remainingBudgetSpan = document.getElementById('remaining-budget');
        const selectedCostSpan = document.getElementById('selected-cost');
        const artworkListDiv = document.getElementById('artwork-list');
        const selectedArtworksDiv = document.getElementById('selected-artworks');
        const noSelectionMessage = document.getElementById('no-selection-message');
        const selectionListUl = document.getElementById('selection-list');
        const submitButton = document.getElementById('submit-selection');
        const resultsDiv = document.getElementById('results');
        const feedbackContentDiv = document.getElementById('feedback-content');
        const restartButton = document.getElementById('restart-simulation');
        const showExplanationButton = document.getElementById('show-explanation');
        const explanationDiv = document.getElementById('explanation');

        // Initial Budget Display
        totalBudgetSpan.textContent = totalBudget.toLocaleString();
        remainingBudgetSpan.textContent = remainingBudget.toLocaleString();

        // Artwork Data (7 pieces) - Enhanced Descriptions
        const artworks = [
            {
                id: 1,
                title: "קומפוזיציה אבסטרקטית בכחול ואדום",
                artist: "לאה לוי",
                price: 150000,
                era: "מודרני (שנות ה-60)",
                subject: "אבסטרקט גיאומטרי",
                condition: "מצב טוב מאוד",
                history: "יצירה מרכזית מתערוכת היחיד המפורסמת של האמנית ב-1968. נרכש ישירות מאספן פרטי ידוע.",
                futureValueEst: { min: 180000, max: 250000, probability: "בינונית-גבוהה" },
                relevanceToCollection: "חיזוק משמעותי לאוסף הישראלי המודרני המוקדם, מילוי חוסר נקודתי בעבודותיה המוקדמות של לוי.",
                audienceAppeal: "בינוני (אמנות מופשטת דורשת עין מיומנת, אך הקומפוזיציה נעימה)",
                historicalSignificance: "גבוה (יצירה איקונית מאמנית מוכרת ומשפיעה בתקופתה)",
                internalScores: { historical: 5, audience: 3, futureValue: 4, relevance: 5 } // Scores 1-5
            },
            {
                id: 2,
                title: "דיוקן אישה בשדה פרגים",
                artist: "אברהם כהן",
                price: 280000,
                era: "אמנות ישראלית ראשית (שנות ה-20)",
                subject: "דיוקן/נוף ארץ ישראלי",
                condition: "זקוקה לשימור קל של המסגרת, הבד במצב טוב.",
                history: "אחת היצירות הידועות והאהובות ביותר של כהן מתקופת שהותו הראשונה בארץ. הייתה באוסף משפחתי דורות רבים.",
                futureValueEst: { min: 320000, max: 450000, probability: "גבוהה מאוד" },
                relevanceToCollection: "אבן יסוד חסרה באוסף האמנות הארץ-ישראלית המוקדמת, מייצגת תקופה וסגנון קריטיים.",
                audienceAppeal: "גבוה מאוד (סגנון קלאסי, נגיש רגשית, נושא מקומי פופולרי)",
                historicalSignificance: "גבוה מאוד (אמן מרכזי בתולדות האמנות הישראלית, יצירה מפורסמת)",
                internalScores: { historical: 5, audience: 5, futureValue: 5, relevance: 5 }
            },
            {
                id: 3,
                title: "נוף עירוני: לילה בעיר העתיקה",
                artist: "שרה בלום",
                price: 90000,
                era: "פוסט-מודרני (שנות ה-90)",
                subject: "אורבני/אקספרסיבי",
                condition: "מצב מצוין, צבעים עזים.",
                history: "נרכש ישירות מסטודיו האמנית. הוצג בתערוכה קבוצתית בגלריה מקומית.",
                futureValueEst: { min: 80000, max: 120000, probability: "בינונית" },
                relevanceToCollection: "הוספת ייצוג לזרם פחות מיוצג באוסף - הציור האקספרסיבי של שנות ה-90.",
                audienceAppeal: "בינוני-גבוה (נושא מוכר, סגנון דינמי)",
                historicalSignificance: "בינוני (אמנית מוכרת בקהילה המקומית, פחות בעלת שם לאומי רחב)",
                 internalScores: { historical: 3, audience: 4, futureValue: 2, relevance: 3 }
            },
            {
                id: 4,
                title: "צמיחה אורגנית #2: פסל חוץ",
                artist: "דניאל שפירא",
                price: 450000,
                era: "פיסול עכשווי (שנות ה-2000)",
                subject: "פיסול מופשט/סביבתי",
                condition: "מצב מצוין, עשוי מחומרים עמידים לחוץ.",
                history: "הוצג בהצלחה בפארק פסלים יוקרתי. דורש שטח תצוגה חיצוני מתאים ותשתית יציבה.",
                futureValueEst: { min: 480000, max: 600000, probability: "גבוהה" },
                relevanceToCollection: "הרחבה משמעותית של מדיום הפיסול באוסף, הוספת יצירת חוץ מרשימה.",
                audienceAppeal: "גבוה מאוד (מרשים בקנה מידה גדול, מושך תשומת לב)",
                historicalSignificance: "גבוה (אמן בעל מוניטין בינלאומי בתחום הפיסול הסביבתי)",
                 internalScores: { historical: 4, audience: 5, futureValue: 4, relevance: 3 }
            },
            {
                id: 5,
                title: "רגעים קטנים: סדרת צילומים מחיי יום יום",
                artist: "רות קליין",
                price: 60000, // For the series of 10 prints
                era: "צילום דוקומנטרי חברתי (שנות ה-70)",
                subject: "חברה/תיעוד",
                condition: "ההדפסים במצב טוב, אך המסגרות ישנות וזקוקות להחלפה מקצועית.",
                history: "סדרה קלאסית בז'אנר הצילום הדוקומנטרי בישראל. תיעוד רגיש של חיי היומיום בעיירת פיתוח.",
                futureValueEst: { min: 70000, max: 100000, probability: "גבוהה" },
                relevanceToCollection: "הוספת מדיום צילום חשוב, תיעוד היסטורי-חברתי בעל ערך.",
                audienceAppeal: "גבוה (נגיש, מעורר הזדהות, סיפורי)",
                historicalSignificance: "גבוה מאוד (קלאסיקה בז'אנר, תיעוד חברתי חשוב)",
                 internalScores: { historical: 5, audience: 5, futureValue: 4, relevance: 5 }
            },
             {
                id: 6,
                title: "מציאות רבודה: התערבות דיגיטלית #3",
                artist: "עידן גולן",
                price: 70000,
                era: "אמנות דיגיטלית/וידאו/אינטראקטיב (שנות ה-2010)",
                subject: "אינטראקטיבי/טכנולוגי",
                condition: "דורשת תחזוקה טכנולוגית שוטפת ועדכוני תוכנה. רישיונות שימוש סופיים.",
                history: "עבודה מוכרת שהוצגה בהצלחה בביאנלה הבינלאומית לאמנות דיגיטלית. מבוססת על תוכנה וטכנולוגיה שצפויות להשתנות.",
                futureValueEst: { min: 50000, max: 90000, probability: "לא וודאית (תלויה בהתפתחות טכנולוגית)" },
                relevanceToCollection: "כניסה הכרחית לעולם האמנות הדיגיטלית והמדיה החדשה - תחום חסר לחלוטין באוסף הקיים.",
                audienceAppeal: "גבוה מאוד (חוויתי, אינטראקטיבי, מדבר במיוחד לקהל צעיר וטכנולוגי)",
                historicalSignificance: "בינוני-גבוה (אמן עולה בתחום, יצירה נחשבת בתקופתה)",
                 internalScores: { historical: 3, audience: 5, futureValue: 3, relevance: 4 }
            },
            {
                id: 7,
                title: "נוף פנורמי מהכרמל עם דמויות",
                artist: "אלמוני (מיוחס ל...?)",
                price: 30000,
                era: "סוף המאה ה-19 / ראשית המאה ה-20",
                subject: "נוף היסטורי/ז'אנר",
                condition: "מצב פיזי בינוני, זקוק לשיקום וניקוי משמעותיים. נזקי לחות ובלאי.",
                history: "נמצא בשוק הפשפשים עם מסגרת מקורית. קיים פוטנציאל לזיהוי אמן משמעותי מתקופת היישוב הישן/תחילת העלייה הראשונה לאחר מחקר ושיקום.",
                futureValueEst: { min: 20000, max: 150000, probability: "נמוכה מאוד (תלויה באופן מוחלט בזיהוי האמן ושיקום)" },
                relevanceToCollection: "פוטנציאל להשלמת חוסר משמעותי באוסף ההיסטורי המוקדם מאוד, אך כרוך בסיכון ומחקר.",
                audienceAppeal: "בינוני (ציור נוף קלאסי, עשוי לעניין חובבי היסטוריה מקומית)",
                historicalSignificance: "נמוך (כל עוד האמן אלמוני); פוטנציאל גבוה אם יזוהה אמן משמעותי.",
                 internalScores: { historical: 2, audience: 3, futureValue: 1, relevance: 2 }
            }
        ];

        function renderArtworks() {
            artworkListDiv.innerHTML = '';
            artworks.forEach(artwork => {
                const isSelected = selectedArtworks.some(item => item.id === artwork.id);
                const artworkElement = document.createElement('div');
                artworkElement.classList.add('artwork-item');
                 if (isSelected) {
                    artworkElement.classList.add('selected');
                }
                artworkElement.setAttribute('data-id', artwork.id);
                artworkElement.innerHTML = `
                    <h4>${artwork.title} מאת ${artwork.artist}</h4>
                    <p><strong>תקופה:</strong> ${artwork.era}</p>
                    <p><strong>נושא:</strong> ${artwork.subject}</p>
                    <p><strong>מצב:</strong> ${artwork.condition}</p>
                    <p><strong>היסטוריה:</strong> ${artwork.history}</p>
                    <p><strong>פוטנציאל משיכת קהל:</strong> ${artwork.audienceAppeal}</p>
                    <p><strong>רלוונטיות לאוסף:</strong> ${artwork.relevanceToCollection}</p>
                    <p><strong>שווי עתידי מוערך:</strong> ${artwork.futureValueEst.min.toLocaleString()} - ${artwork.futureValueEst.max.toLocaleString()} ₪ (סבירות: ${artwork.futureValueEst.probability})</p>
                    <p class="price"><span>${artwork.price.toLocaleString()}</span> ₪</p>
                `;
                artworkElement.addEventListener('click', () => toggleArtworkSelection(artwork));
                artworkListDiv.appendChild(artworkElement);
            });
        }

        function updateBudgetDisplay() {
            const selectedCost = selectedArtworks.reduce((sum, artwork) => sum + artwork.price, 0);
            remainingBudget = totalBudget - selectedCost;

            selectedCostSpan.textContent = selectedCost.toLocaleString();
            remainingBudgetSpan.textContent = remainingBudget.toLocaleString();

            // Visual feedback for budget
            remainingBudgetSpan.classList.remove('warning', 'danger');
            selectedCostSpan.classList.remove('danger');

            if (remainingBudget < 0) {
                remainingBudgetSpan.classList.add('danger');
                 selectedCostSpan.classList.add('danger');
            } else if (remainingBudget < totalBudget * 0.1 && remainingBudget > 0) { // Less than 10% left
                 remainingBudgetSpan.classList.add('warning');
            }


            // Update selected items list
            selectionListUl.innerHTML = '';
            if (selectedArtworks.length === 0) {
                noSelectionMessage.style.display = 'block';
            } else {
                noSelectionMessage.style.display = 'none';
                selectedArtworks.forEach(artwork => {
                    const listItem = document.createElement('li');
                    // Use dataset for animation trigger
                    listItem.dataset.id = artwork.id;
                    listItem.innerHTML = `
                        ${artwork.title} <span>${artwork.price.toLocaleString()} ₪</span>
                    `;
                     // Trigger adding animation
                    requestAnimationFrame(() => {
                         requestAnimationFrame(() => {
                            // This double rAF trick helps ensure the transition runs
                            // if the item was just added to the DOM.
                            listItem.classList.remove('adding');
                        });
                    });

                    selectionListUl.appendChild(listItem);
                });
            }
        }

        function toggleArtworkSelection(artwork) {
            const isSelected = selectedArtworks.some(item => item.id === artwork.id);
            const artworkElement = document.querySelector(`.artwork-item[data-id='${artwork.id}']`);

            if (isSelected) {
                // Deselect
                selectedArtworks = selectedArtworks.filter(item => item.id !== artwork.id);
                artworkElement.classList.remove('selected');
                 // Find the corresponding list item and trigger removing animation
                const listItemToRemove = selectionListUl.querySelector(`li[data-id='${artwork.id}']`);
                if (listItemToRemove) {
                    listItemToRemove.classList.add('removing');
                    // Remove after animation
                    listItemToRemove.addEventListener('transitionend', () => {
                        listItemToRemove.remove();
                        updateBudgetDisplay(); // Update display *after* item is removed from list
                    }, { once: true }); // Ensure listener is removed after it fires
                } else {
                     updateBudgetDisplay(); // Fallback if list item not found
                }


            } else {
                // Select
                 selectedArtworks.push(artwork);
                 artworkElement.classList.add('selected');
                 // Add to selected list with adding animation
                 const listItem = document.createElement('li');
                 listItem.dataset.id = artwork.id;
                 listItem.innerHTML = `${artwork.title} <span>${artwork.price.toLocaleString()} ₪</span>`;
                 listItem.classList.add('adding'); // Start with adding class for animation
                 selectionListUl.appendChild(listItem);

                 updateBudgetDisplay(); // Update display immediately upon selection
            }
        }

        function submitSelection() {
            // Hide current content, show results
            document.getElementById('selection-area').classList.add('hidden'); // Hide list/selection area
            resultsDiv.classList.remove('hidden');

            feedbackContentDiv.innerHTML = '';

            const selectedCost = selectedArtworks.reduce((sum, artwork) => sum + artwork.price, 0);
            const budgetStatusClass = selectedCost > totalBudget ? 'warning' : 'success';

            feedbackContentDiv.innerHTML += `<h4>סיכום הרכישה:</h4>`;
            if (selectedArtworks.length === 0) {
                feedbackContentDiv.innerHTML += `<p> לא נבחרו יצירות לרכישה הפעם. אולי בחרוף הבא?</p>`;
            } else {
                 feedbackContentDiv.innerHTML += `<p>בחרתם <strong>${selectedArtworks.length}</strong> יצירות בעלות כוללת של <strong>${selectedCost.toLocaleString()} ₪</strong>.</p>`;
                 feedbackContentDiv.innerHTML += `<p class="${budgetStatusClass}"><strong>סטטוס תקציבי:</strong> ${selectedCost > totalBudget ? `<strong>חריגה מהתקציב!</strong> חרגתם ב- ${(selectedCost - totalBudget).toLocaleString()} ₪.` : `<strong>במסגרת התקציב.</strong> נותרה יתרה של ${remainingBudget.toLocaleString()} ₪.`}</p>`;


                feedbackContentDiv.innerHTML += `<h4>איזון אוצרותי: כיצד הבחירות שלכם משפיעות על האוסף?</h4>`;

                // Calculate scores based on selected items
                const totalHistoricalScore = selectedArtworks.reduce((sum, artwork) => sum + artwork.internalScores.historical, 0);
                const totalAudienceScore = selectedArtworks.reduce((sum, artwork) => sum + artwork.internalScores.audience, 0);
                const totalFutureValueScore = selectedArtworks.reduce((sum, artwork) => sum + artwork.internalScores.futureValue, 0);
                 const totalRelevanceScore = selectedArtworks.reduce((sum, artwork) => sum + artwork.internalScores.relevance, 0);

                 // Calculate potential maximum scores (if user bought everything)
                 const maxHistorical = artworks.reduce((sum, artwork) => sum + artwork.internalScores.historical, 0);
                 const maxAudience = artworks.reduce((sum, artwork) => sum + artwork.internalScores.audience, 0);
                 const maxFutureValue = artworks.reduce((sum, artwork) => sum + artwork.internalScores.futureValue, 0);
                 const maxRelevance = artworks.reduce((sum, artwork) => sum + artwork.internalScores.relevance, 0);

                 const formatScoreFeedback = (score, maxScore, goalName, highValueArtworks) => {
                     let feedback = `<p><strong>${goalName}:</strong> ציון ${score}/${maxScore}.`;
                     if (highValueArtworks.length > 0) {
                         const artworkTitles = highValueArtworks.map(a => `"${a.title}"`).join(', ');
                         feedback += ` היצירה${highValueArtworks.length > 1 ? 'ות' : ''} ${artworkTitles} תורמ${highValueArtworks.length > 1 ? 'ות' : 'ת'} במיוחד להיבט זה.`;
                     } else {
                         feedback += ` אף יצירה עם ציון גבוה במיוחד בקריטריון זה לא נבחרה הפעם.`;
                     }
                     feedback += '</p>';
                     return feedback;
                 };


                 feedbackContentDiv.innerHTML += formatScoreFeedback(totalHistoricalScore, maxHistorical, 'חיזוק היסטורי/תרבותי של האוסף', selectedArtworks.filter(a => a.internalScores.historical >= 4));
                 feedbackContentDiv.innerHTML += formatScoreFeedback(totalAudienceScore, maxAudience, 'פוטנציאל משיכת קהל והשפעה חברתית', selectedArtworks.filter(a => a.internalScores.audience >= 4));
                 feedbackContentDiv.innerHTML += formatScoreFeedback(totalFutureValueScore, maxFutureValue, 'פוטנציאל השבחה וערך עתידי', selectedArtworks.filter(a => a.internalScores.futureValue >= 4));
                 feedbackContentDiv.innerHTML += formatScoreFeedback(totalRelevanceScore, maxRelevance, 'התאמה ורלוונטיות לאוסף הקיים', selectedArtworks.filter(a => a.internalScores.relevance >= 4));


                 feedbackContentDiv.innerHTML += `<h4>מחשבות לסיום: פשרות והטיות אוצרותיות</h4>`;
                 feedbackContentDiv.innerHTML += `<p>האתגר האוצרותי הוא לאזן בין מטרות שונות תחת מגבלות תקציב. האם העדפתם "קניות בטוחות" של אמנים מוכרים (פוטנציאל היסטורי וקהל גבוה, אך יקרות), או נטלתם סיכונים על יצירות פחות ודאיות אך עם פוטנציאל מפתיע (כמו היצירה האלמונית או הדיגיטלית)? האם שיקולי המחיר או שם האמן השפיעו עליכם באופן בלתי מודע? כל בחירה משקפת סדרי עדיפויות שונים ומעצבת את אופי האוסף.</p>`;
            }

             // Scroll to results
             resultsDiv.scrollIntoView({ behavior: 'smooth' });
             submitButton.style.display = 'none'; // Use style to completely hide element and remove from flow
        }

        function restartSimulation() {
            selectedArtworks = [];
            remainingBudget = totalBudget;
            updateBudgetDisplay();
            renderArtworks(); // Re-render to remove 'selected' class and reset event listeners
            resultsDiv.classList.add('hidden');
            document.getElementById('selection-area').classList.remove('hidden'); // Show selection area
            feedbackContentDiv.innerHTML = '';
            submitButton.style.display = 'block'; // Show submit button
             // Scroll back to the top of the app
             document.getElementById('app').scrollIntoView({ behavior: 'smooth' });

        }

        // Toggle Explanation
        showExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.classList.contains('hidden');
            if (isHidden) {
                explanationDiv.classList.remove('hidden');
                showExplanationButton.textContent = 'הסתר הסבר תיאורטי';
                 // Scroll to explanation
                explanationDiv.scrollIntoView({ behavior: 'smooth' });

            } else {
                explanationDiv.classList.add('hidden');
                showExplanationButton.textContent = 'על ההחלטות שמאחורי האמנות: הסבר תיאורטי';
                 // Optional: scroll back up after hiding? Maybe not necessary.
            }
        });


        // Initial Render
        renderArtworks();
        updateBudgetDisplay();

        // Event Listeners
        submitButton.addEventListener('click', submitSelection);
        restartButton.addEventListener('click', restartSimulation);

    });
</script>
```