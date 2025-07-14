---
title: "סימולטור ועדת חנינות: מאחורי ההחלטה הגורלית"
english_slug: pardon-committee-simulator-would-you-decide-differently
category: "מדעי החברה / פסיכולוגיה"
tags: ["קבלת החלטות", "הטיות קוגניטיביות", "פסיכולוגיה", "ועדה", "צדק", "סימולטור", "משחק"]
---
# סימולטור ועדת חנינות: מאחורי ההחלטה הגורלית

דמיינו שאתם חלק מוועדה גורלית, שבידיה הכוח להשפיע על חיי אדם. אילו שיקולים ינחו אתכם? האם תוכלו להישאר אובייקטיביים לחלוטין, או שהטיות נפוצות ומידע לא רלוונטי יחדרו לתהליך קבלת ההחלטות שלכם? הסימולטור הזה מזמין אתכם להיכנס לנעלי חברי הוועדה ולהתנסות במורכבות האנושית שמאחורי כל המלצה על חנינה.

<div id="simulator-app">
    <div id="case-presentation">
        <h2 id="case-title">טוען מקרה...</h2>
        <div id="case-details">
            <!-- Case details will be loaded here -->
        </div>
         <div id="bias-hint" class="hint" style="display: none;">
            <i class="info-icon"></i> <span id="bias-hint-text"></span>
        </div>
    </div>
    <div id="decision-buttons" class="actions" style="display: none;">
        <button id="approve-btn" class="decision-btn approve">להמליץ על חנינה</button>
        <button id="reject-btn" class="decision-btn reject">לדחות את הבקשה</button>
    </div>
    <div id="feedback-area" class="feedback" style="display: none;">
        <h3>המשוב על ההחלטה שלך:</h3>
        <p id="feedback-text"></p>
        <button id="next-case-btn" class="action-btn next-case" style="display: none;">למקרה הבא</button>
    </div>
    <div id="end-screen" class="end-game" style="display: none;">
        <h2>סיכום הסימולטור</h2>
        <p>סיימת לבחון את כל המקרים. מקרי החנינה אמיתיים ומורכבים, ומראים כיצד שיקולים שונים, כולל הטיות קוגניטיביות, יכולים להשפיע על החלטות משנות חיים. כעת, מומלץ לעיין בהסבר המורחב כדי להעמיק את הבנתכם בנוגע לדינמיקות בוועדות ולקבלת החלטות תחת השפעה.</p>
         <button id="restart-btn" class="action-btn restart">התחל סימולטור מחדש</button>
    </div>
</div>

<style>
    :root {
        --primary-color: #0056b3; /* Darker Blue */
        --secondary-color: #e0e0e0; /* Light Gray */
        --approve-color: #28a745; /* Green */
        --reject-color: #dc3545; /* Red */
        --warning-color: #ffc107; /* Yellow/Orange for hints */
        --bg-color: #f4f7f6; /* Very Light Gray/Blue background */
        --card-bg-color: #ffffff; /* White for cards */
        --text-color: #333; /* Dark Gray text */
        --border-color: #cce5ff; /* Light Blue border */
        --border-radius: 10px;
        --box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --transition-speed: 0.4s ease-in-out;
    }

    #simulator-app {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        max-width: 700px;
        margin: 30px auto;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--bg-color);
        line-height: 1.7;
        color: var(--text-color);
        box-shadow: var(--box-shadow);
        overflow: hidden; /* To contain animations */
    }

    #case-presentation, .feedback, .end-game {
        margin-bottom: 20px;
        padding: 20px;
        border: 1px solid var(--secondary-color);
        border-radius: var(--border-radius);
        background-color: var(--card-bg-color);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        opacity: 1;
        transform: translateY(0);
        transition: opacity var(--transition-speed), transform var(--transition-speed);
    }

     .fade-out {
         opacity: 0;
         transform: translateY(20px);
     }

     .fade-in {
         opacity: 1;
         transform: translateY(0);
     }


    #case-title {
        text-align: center;
        color: var(--primary-color);
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.6em;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
    }

    #case-details p {
        margin-bottom: 12px;
        padding-bottom: 12px;
        border-bottom: 1px dashed var(--secondary-color);
        font-size: 1.05em;
    }
     #case-details p:last-child {
        border-bottom: none;
        padding-bottom: 0;
        margin-bottom: 0;
    }

    #case-details strong {
        color: var(--primary-color);
    }

    #bias-hint {
        margin-top: 20px;
        padding: 10px;
        background-color: #fff3cd; /* Light yellow */
        border: 1px solid #ffeeba; /* Yellow border */
        border-radius: 5px;
        color: #856404; /* Dark yellow text */
        font-size: 0.95em;
        display: flex;
        align-items: center;
    }

    .info-icon {
        display: inline-block;
        width: 20px;
        height: 20px;
        background-color: #856404;
        color: #fff3cd;
        border-radius: 50%;
        text-align: center;
        line-height: 20px;
        font-weight: bold;
        margin-left: 8px;
        flex-shrink: 0;
    }
     .info-icon::before {
         content: 'i';
         font-style: normal;
     }


    .actions {
        text-align: center;
        margin-bottom: 20px;
        display: flex; /* Use flexbox for buttons */
        justify-content: center;
        gap: 20px; /* Space between buttons */
        opacity: 1;
        transition: opacity var(--transition-speed);
    }

     .actions.fade-out {
         opacity: 0;
         pointer-events: none; /* Disable clicks while fading */
     }

    .decision-btn, .action-btn {
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* Pill shape */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .decision-btn.approve {
        background-color: var(--approve-color);
        color: white;
    }

    .decision-btn.approve:hover {
        background-color: #218838; /* Darker Green */
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
     .decision-btn.approve:active {
         transform: translateY(0);
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
     }


    .decision-btn.reject {
        background-color: var(--reject-color);
        color: white;
    }

    .decision-btn.reject:hover {
        background-color: #c82333; /* Darker Red */
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
     .decision-btn.reject:active {
         transform: translateY(0);
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
     }

    .feedback {
        margin-top: 20px;
        padding: 20px;
        border-radius: var(--border-radius);
        background-color: var(--card-bg-color);
        /* Feedback background will be set by JS based on decision */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
     .feedback h3 {
         margin-top: 0;
         color: var(--primary-color);
         border-bottom: 1px solid var(--secondary-color);
         padding-bottom: 10px;
         margin-bottom: 15px;
     }
     .feedback p {
         margin-bottom: 15px;
         font-size: 1.05em;
     }

    .action-btn {
        display: block;
        width: fit-content;
        margin: 20px auto 0;
        background-color: var(--primary-color);
        color: white;
    }

     .action-btn.restart {
         background-color: var(--warning-color);
         color: var(--text-color);
         font-weight: bold;
     }


    .action-btn:hover {
        background-color: #004085; /* Even Darker Blue */
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
     .action-btn:active {
         transform: translateY(0);
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
     }

    .action-btn.restart:hover {
        background-color: #ffaa00; /* Darker Orange */
    }


    .end-game {
         text-align: center;
         padding: 30px;
         background-color: var(--card-bg-color);
    }

    .end-game h2 {
        color: var(--primary-color);
        font-size: 2em;
        margin-bottom: 15px;
    }
     .end-game p {
         font-size: 1.1em;
         margin-bottom: 25px;
         color: #555;
     }


    #toggle-explanation {
        display: block;
        width: fit-content;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        border: 1px solid var(--primary-color);
        border-radius: 25px;
        background-color: var(--card-bg-color);
        color: var(--primary-color);
        transition: background-color 0.3s ease, color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        font-weight: bold;
    }
     #toggle-explanation:hover {
         background-color: var(--primary-color);
         color: white;
         transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
     }
     #toggle-explanation:active {
         transform: translateY(0);
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
     }


    #explanation {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--bg-color);
        direction: rtl;
        text-align: right;
        box-shadow: var(--box-shadow);
    }

    #explanation h2, #explanation h3 {
        color: var(--primary-color);
        border-bottom: 2px solid var(--secondary-color);
        padding-bottom: 8px;
        margin-bottom: 20px;
    }

    #explanation h2 {
        font-size: 1.8em;
    }
     #explanation h3 {
         font-size: 1.4em;
     }

    #explanation p {
        margin-bottom: 18px;
        font-size: 1.05em;
        color: #555;
    }

    #explanation ul {
        list-style-type: disc;
        margin-right: 25px;
        margin-bottom: 18px;
        color: #555;
    }

    #explanation li {
        margin-bottom: 10px;
        line-height: 1.6;
    }

     /* Add some keyframe animations */
     @keyframes fadeIn {
         from { opacity: 0; transform: translateY(20px); }
         to { opacity: 1; transform: translateY(0); }
     }

     @keyframes fadeOut {
         from { opacity: 1; transform: translateY(0); }
         to { opacity: 0; transform: translateY(-20px); }
     }

     .animated.fade-in { animation: fadeIn var(--transition-speed) forwards; }
     .animated.fade-out { animation: fadeOut var(--transition-speed) forwards; }

</style>

<button id="toggle-explanation">הצגת/הסתרת ההסבר המורחב</button>

<div id="explanation" style="display: none;">
    <h2>ועדת חנינות וקבלת החלטות: מבט מעמיק</h2>

    <h3>תפקידה של ועדת חנינות נשיאותית</h3>
    <p>ועדת החנינות משמשת כגוף מייעץ לנשיא המדינה, בוחנת בקשות חנינה מאסירים ומורשעים, וממליצה אם להיענות לבקשה (למשל, קיצור עונש או מחיקת רישום פלילי) או לדחותה. עבודת הוועדה דורשת איזון עדין בין עקרונות צדק, שיקום, בטחון הציבור, והתחשבות בנסיבות אנושיות ייחודיות.</p>

    <h3>המורכבות האנושית שמאחורי ההחלטה</h3>
    <p>ההחלטה על חנינה אינה תהליך משפטי יבש בלבד. היא רוויה בהיבטים מוסריים, חברתיים ורגשיים. כיצד שוקלים את סיכויי השיקום מול חומרת העבירה המקורית? מתי החברה סלחה? וכיצד מתייחסים להשפעת המאסר על משפחת האסיר מול סבל קורבנות העבירה? חברי הוועדה ניצבים בפני דילמות אמיתיות, לעיתים ללא תשובות חד-משמעיות.</p>

    <h3>דינמיקות קבוצתיות בוועדה: לא רק דעות אישיות</h3>
    <p>קבלת החלטות בוועדה מושפעת לא רק משיקול דעתם האישי של החברים, אלא גם מדינמיקות חברתיות. לחצים נורמטיביים, הרצון להגיע לקונצנזוס במהירות (לפעמים על חשבון דיון מעמיק - "חשיבת יחד" או Groupthink), והשפעת חברים דומיננטיים יכולים כולם להטות את כף המאזניים.</p>

    <h3>הטיות קוגניטיביות: מלכודות החשיבה האנושית</h3>
    <p>הטיות קוגניטיביות הן דפוסי חשיבה אוטומטיים, שאינם בהכרח רציונליים, המשפיעים על האופן בו אנו קולטים ומעבדים מידע, ובכך מעוותים את שיקול דעתנו. הן נפוצות גם אצל מקבלי החלטות מנוסים:</p>
    <ul>
        <li>**הטיית העיגון (Anchoring Bias):** הנטייה להיתפס למידע הראשוני המוצג (ה"עוגן") ולהתבסס עליו יתר על המידה בהמשך קבלת ההחלטה, גם כשהוא אינו בהכרח הרלוונטי ביותר. לדוגמה, חומרת העבירה המקורית או אורך העונש יכולים להוות עוגן שמשפיע על הערכת סיכויי שיקום עתידיים.</li>
        <li>**הטיית האישור (Confirmation Bias):** הנטייה לחפש, לפרש ולזכור מידע שמאשר אמונות או דעות קיימות, ולהתעלם ממידע שסותר אותן. אם חבר ועדה מאמין שאסיר מסוים ראוי לחנינה (או שלא), הוא יחפש עדויות שיחזקו דעה זו ויתעלם מהשאר.</li>
        <li>**הטיית ההילה (Halo Effect):** הנטייה להרחיב תכונה חיובית אחת (או שלילית אחת) של אדם, ולהסיק ממנה לגבי תכונות נוספות שאינן קשורות אליה ישירות. סיפור אישי מרגש או מראה חיצוני מסודר יכולים ליצור 'הילה' שתגרום להערכת יתר של אמינות האסיר או סיכויי שיקומו.</li>
        <li>**אפקט המסגור (Framing Effect):** האופן בו מוצג המידע משפיע על ההחלטה, גם אם המידע המהותי זהה. הדגשת סבל משפחת האסיר לעומת הדגשת פגיעת הקורבן יכולה להוביל להחלטות שונות לחלוטין, פשוט בגלל ה"מסגרת" השונה בה הוצג המקרה.</li>
    </ul>

    <h3>השפעת מידע לא רלוונטי</h3>
    <p>ועדות חנינה נחשפות לעיתים קרובות למידע אישי, רגשי או חברתי שאינו קשור ישירות לעבירה, לעונש או לתהליך השיקום המקצועי של האסיר (כמו מצב משפחתי ייחודי, קשרים חיצוניים, או עדויות אופי שאינן מבתי הכלא). מידע זה, אף שהוא אנושי ומעורר אמפתיה, עלול להכניס אלמנטים סובייקטיביים ולהגביר את הסיכון להטיות, על חשבון בחינה עניינית ומבוססת קריטריונים אחידים.</p>

    <h3>האיזון העדין: רציונל מול רגש</h3>
    <p>ההחלטה על חנינה דורשת שילוב של חשיבה רציונלית (בחינת עובדות, חוקים, נהלים) וחמלה אנושית (התחשבות בנסיבות, פוטנציאל שיקום). האתגר המרכזי הוא למצוא את האיזון הנכון: להכיר בהיבטים האנושיים מבלי לאפשר להטיות ולמידע לא רלוונטי להאפיל על הצורך באובייקטיביות, שקיפות ושוויון בפני החוק.</p>

    <h3>זיהוי הטיות והתמודדות איתן</h3>
    <p>הצעד הראשון הוא מודעות לקיומן של הטיות אלו והכרה בכך שכולנו חשופים להן. דיון פתוח, ביקורתי ורב-קולי בוועדה, שימוש בכלי עזר מסודרים, קביעת קריטריונים ברורים ככל הניתן, והתייעצות עם גורמים מקצועיים בלתי תלויים יכולים לסייע בצמצום השפעתן של הטיות ובקבלת החלטות מבוססות ומאוזנות יותר.</p>
</div>


<script>
    const cases = [
        {
            title: "מקרה 1: גניבה לצורך רפואה דחופה",
            details: [
                "**האסיר:** דוד כהן, בן 55.",
                "**העבירה:** גניבת סכום כסף גדול ממעסיקו לצורך מימון טיפול רפואי דחוף ויקר לבתו הקטנה שהייתה בסכנת חיים. אין לו עבר פלילי קודם.",
                "**העונש שנגזר:** 3 שנות מאסר בפועל.",
                "**התנהגות בכלא:** התנהגות מופתית, השתתף בתוכניות שיקום רבות, עובד במפעל הכלא ונחשב לאסיר למופת. מקבל דו"חות חיוביים מהסגל.",
                "**נסיבות אישיות נוספות:** בתו החלימה אך נותרה נכה חלקית ותלויה בטיפול יקר מתמשך. אשתו התקשתה לפרנס את המשפחה בלעדיו והמשפחה נקלעה לחובות כבדים. מעסיקו לשעבר הביע צער על המצב אך התעקש על העונש כאות אזהרה.",
                "**התרשמות משימוע קודם:** אסיר שקט, שומר על מראה מסודר ונקי. במהלך שימוע קודם בפני גורם אחר, סיפורו האישי והמצוקה ששידר גרמו לרגש רב אצל השומעים ונרשמה הערה על כך בפרוטוקול."
            ],
            biasHint: "שימו לב כיצד המצוקה האישית והסיפור הרגשי העוצמתי 'ממסגרים' את המעשה, והאם ההתרשמות החיובית מהאסיר יוצרת 'הילה' המשפיעה על שיקול הדעת, על חשבון חומרת העבירה והצורך בצדק ציבורי (הטיית ההילה, אפקט המסגור).",
            feedback: {
                approve: "**החלטה להמליץ על חנינה:** החלטה זו הושפעה, ככל הנראה, מהכוח הרגשי העצום של סיפורו האישי של האסיר ונסיבות ביצוע העבירה. חברי ועדה רבים התקשו להתעלם מהמצוקה הנוראה בה היה נתון ומהעובדה שהמעשה הציל חיים (למרות שהיה פלילי). זוהי דוגמה לאפקט המסגור - המקרה 'מסוגר' כמעשה נואש ממצוקה ולא כעבירה פלילית רגילה. התנהגותו הטובה בכלא מוסיפה ל'הילת' האסיר הטוב. ההתמקדות היא בצד האנושי ופוטנציאל השיקום, לעיתים על חשבון הצורך להרתיע מעבירות חמורות כאלו.",
                reject: "**החלטה לדחות את הבקשה:** דחיית הבקשה מתמקדת לרוב בחומרת העבירה המקורית, בגובה הסכום שנגנב ובהשלכותיה על הקורבן (המעסיק). גישה זו נוטה להפריד בין נסיבות אישיות קשות ובין חומרת המעשה הפלילי עצמו, ומתמקדת בצורך לשמור על שלטון החוק ולהרתיע. זוהי גישה המבוססת על היגיון 'קר' יותר, אך היא עלולה להתעלם מהקשר הייחודי שאיפשר את ביצוע העבירה. היא שמה דגש על עקרונות משפטיים וציבוריים מעל גורמים רגשיים ואישיים."
            }
        },
        {
            title: "מקרה 2: הונאה פיננסית רחבת היקף",
            details: [
                "**האסיר:** אלי שקד, בן 48.",
                "**העבירה:** הונאה פיננסית מתוחכמת ורחבת היקף שגרמה הפסדים של מיליוני שקלים לחברה ציבורית ולמשקיעים קטנים רבים, חלקם איבדו את כל חסכונותיהם.",
                "**העונש שנגזר:** 7 שנות מאסר בפועל.",
                "**התנהגות בכלא:** התנהגות שגרתית, לא יצר בעיות מיוחדות אך גם לא גילה עניין מיוחד בתוכניות שיקום מעבר למינימום הפורמלי. מתלונן תדיר על התנאים בכלא ועל יחס הסגל.",
                "**נסיבות אישיות נוספות:** בא ממשפחה מבוססת ובעלת קשרים חברתיים ופוליטיים. סנגורו, עורך דין ידוע, טוען שנעשה לו עוול ושהוא 'שעיר לעזאזל' למחדלי רשויות הפיקוח. האסיר עצמו ממעיט בחומרת מעשיו ואינו מביע חרטה אמיתית. נשוי ואב לשניים. אשתו פעילה ציבורית בולטת ומפעילה לחץ לקבלת החנינה.",
                "**השוואה לתיק אחר:** הוצג לוועדה נתון השוואתי (שאינו קשור ישירות לתיק) של אסיר אחר שהורשע בעבירת הונאה דומה, אך בסכום נמוך בהרבה, וקיבל עונש קל משמעותית."
            ],
            biasHint: "שקלו כיצד גובה הסכום שנגנב (וההפסדים העצומים) יכולים 'לעגן' את תפיסת חומרת העבירה. האם מעמדו החברתי, קשריו, או הלחץ החיצוני שהופעל משפיעים על ההחלטה? האם ההשוואה לתיק אחר, פחות חמור, מהווה 'עוגן' נוסף? (הטיית העיגון, השפעת מידע לא רלוונטי/לחצים חיצוניים).",
            feedback: {
                approve: "**החלטה להמליץ על חנינה:** אישור חנינה במקרה זה עלול לנבוע מהשפעת גורמים חיצוניים ומידע שאינו רלוונטי עניינית, כמו מעמד חברתי, קשרים חזקים, או לחץ המופעל מבחוץ. ייתכן גם שההשוואה למקרה אחר, עם עונש קל יותר, משמשת כ'עוגן' שממנו נגזר הצורך לסטות מהעונש המקורי (שהפך ל'עוגן' הנגדי). החלטה כזו עלולה להתפרש כהעדפה פסולה לבעלי אמצעים וקשרים, תוך התעלמות מחומרת העבירה, היעדר חרטה, והנזק הרב שנגרם לקורבנות רבים.",
                reject: "**החלטה לדחות את הבקשה:** דחיית החנינה במקרה זה מתבססת לרוב באופן מובהק על חומרת ההונאה הפיננסית, היקף הנזק שנגרם למשקיעים, והמסר הציבורי בדבר חומרת עבירות 'צווארון לבן'. גובה הסכום שנגנב משמש כ'עוגן' מרכזי בהערכת המקרה. גישה זו מתייחסת מעט יחסית לנסיבות אישיות שאינן מעידות על שיקום, ומסרבת להיכנע ללחצים חיצוניים או להשוואות לא רלוונטיות. ההתמקדות היא בענישה, הרתעה והגנה על הציבור."
            }
        },
         {
            title: "מקרה 3: אלימות בנסיבות מצוקה קשה",
            details: [
                "**האסירה:** רותי לוי, בת 38.",
                "**העבירה:** תקיפה אלימה וקשה שגרמה לפציעה חמורה לבן זוגה, במהלך ויכוח שהתדרדר לאלימות מצידו. הוגדרה בבית המשפט כהגנה עצמית שחרגה מהסביר בנסיבות המקרה.",
                "**העונש שנגזר:** 5 שנות מאסר בפועל.",
                "**התנהגות בכלא:** התנהגות טובה ושקטה מאוד, מופנמת. סבלה מדיכאון קליני קשה שהוביל להתערבות פסיכיאטרית בכלא. למדה מקצוע טיפולי במסגרת תוכניות השיקום בכלא ומגלה אחריות.",
                "**נסיבות אישיות נוספות:** היסטוריה מתועדת ארוכה של התעללות פיזית, מינית ונפשית קשה מצד בן הזוג, שכללה איומים ופגיעות חוזרות ונשנות. בזמן התקיפה הייתה במצב מצוקה נפשית קיצוני. ללא תמיכה משפחתית חיצונית משמעותית. יש לה שני ילדים קטינים המטופלים אצל קרובי משפחה מרוחקים בתנאים קשים.",
                "**ראיות נוספות שהוצגו:** הסנגור הציג לוועדה תמונות רפואיות קשות שתיעדו פגיעות פיזיות קודמות שסבלה מהן האסירה מידי בן הזוג. עובדת סוציאלית מטעם שירות בתי הסוהר המליצה בחום על שחרורה לחלופת מעצר טיפולית, והעידה על תהליך שיקום משמעותי שעברה."
            ],
            biasHint: "האם הנסיבות הקשות (התעללות, מצוקה נפשית, היסטוריה של פגיעות) יוצרות 'הילה' של קורבן וממסגרות את המעשה ככורח מצער? כיצד ראיות ויזואליות קשות משפיעות על הרגש ועל שיקול הדעת? האם הן גורמות להתעלמות מחומרת הפציעה שנגרמה לקורבן? (הטיית ההילה, אפקט המסגור, השפעת מידע רגשי/ויזואלי, התעלמות מהקורבן).",
            feedback: {
                approve: "**החלטה להמליץ על חנינה:** המלצה זו מושפעת עמוקות מאפקט המסגור ומ'הטיית ההילה'. הנסיבות הקיצוניות בהן בוצעה העבירה (שנים של התעללות) והצגת העדויות המצולמות 'ממסגרות' את האסירה כקורבן ואת המעשה כמעשה נואש הנובע ממצוקה קיצונית. האמפתיה העצומה שהמקרה מעורר יוצרת 'הילה' חיובית סביב האסירה, ומטה את ההחלטה לכיוון החנינה, לעיתים תוך הפחתה ממשקל חומרת הפציעה שנגרמה לבן הזוג (הקורבן). ההתמקדות היא בגורלה של האסירה ובפוטנציאל השיקום שלה נוכח מצבה הנפשי וההיסטוריה שלה.",
                reject: "**החלטה לדחות את הבקשה:** דחיית החנינה במקרה זה שמה את הדגש המרכזי על תוצאת המעשה האלים - הפציעה הקשה שנגרמה לקורבן - ועל הצורך הציבורי להרתיע מפני אלימות, גם אם היא מבוצעת בנסיבות קשות. גישה זו נוטה 'להתעלם' מהנסיבות האישיות המקלות או להפחית ממשקלן, ומתמקדת בהיבט הפלילי והמשפטי היבש של התקיפה והתוצאה. היא עלולה להיות מושפעת מ'הטיית העיגון' על בסיס חומרת הפציעה, ולעיתים מתקשה לשקלל כראוי את ההקשר המורכב של אלימות בתוך המשפחה."
            }
        }
    ];

    let currentCaseIndex = 0;

    const simulatorApp = document.getElementById('simulator-app');
    const casePresentationDiv = document.getElementById('case-presentation');
    const caseTitle = document.getElementById('case-title');
    const caseDetails = document.getElementById('case-details');
    const biasHintDiv = document.getElementById('bias-hint');
    const biasHintTextSpan = document.getElementById('bias-hint-text');
    const decisionButtonsDiv = document.getElementById('decision-buttons');
    const approveBtn = document.getElementById('approve-btn');
    const rejectBtn = document.getElementById('reject-btn');
    const feedbackAreaDiv = document.getElementById('feedback-area');
    const feedbackText = document.getElementById('feedback-text');
    const nextCaseBtn = document.getElementById('next-case-btn');
    const endScreenDiv = document.getElementById('end-screen');
    const restartBtn = document.getElementById('restart-btn');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    function animateElement(element, animationClass, duration = 500) {
        return new Promise(resolve => {
            element.classList.add('animated', animationClass);
            const animationEndHandler = () => {
                element.classList.remove('animated', animationClass);
                 // Ensure display is correctly set after fade-out
                 if (animationClass === 'fade-out') {
                     element.style.display = 'none';
                 }
                element.removeEventListener('animationend', animationEndHandler);
                resolve();
            };
            element.addEventListener('animationend', animationEndHandler);
             // Fallback in case animationend doesn't fire
            setTimeout(resolve, duration + 50);
        });
    }

    async function loadCase(index) {
        if (index >= cases.length) {
            endSimulator();
            return;
        }

        // If not the first case, fade out current content
        if (currentCaseIndex > 0) {
           await animateElement(casePresentationDiv, 'fade-out', 300);
           biasHintDiv.style.display = 'none'; // Ensure hint is hidden during transition
           decisionButtonsDiv.classList.remove('fade-in'); // Remove incoming animation class if exists
           decisionButtonsDiv.style.display = 'none'; // Hide buttons
        }


        const currentCase = cases[index];
        caseTitle.textContent = currentCase.title;
        caseDetails.innerHTML = '';
        currentCase.details.forEach(detail => {
            const p = document.createElement('p');
            p.innerHTML = detail; // Use innerHTML to support bold tags
            caseDetails.appendChild(p);
        });
        biasHintTextSpan.textContent = currentCase.biasHint;


        // Reset and prepare for fade-in
        feedbackAreaDiv.style.display = 'none';
        nextCaseBtn.style.display = 'none';
        endScreenDiv.style.display = 'none';

        casePresentationDiv.classList.remove('fade-out'); // Remove outgoing animation class if exists
        casePresentationDiv.style.display = 'block'; // Make sure it's block before fading in
        await animateElement(casePresentationDiv, 'fade-in', 500); // Fade in the new case details

        biasHintDiv.style.display = 'flex'; // Show hint
        decisionButtonsDiv.style.display = 'flex'; // Show buttons
        animateElement(decisionButtonsDiv, 'fade-in', 300); // Fade in buttons


        currentCaseIndex = index; // Update index *after* loading
    }

    async function showFeedback(decision) {
         // Disable buttons during transition
         approveBtn.disabled = true;
         rejectBtn.disabled = true;
         decisionButtonsDiv.classList.add('fade-out'); // Start fading out buttons

         // Fade out case details
         await animateElement(casePresentationDiv, 'fade-out', 300);
         biasHintDiv.style.display = 'none'; // Hide hint

         const currentCase = cases[currentCaseIndex];
        feedbackText.innerHTML = `**ההחלטה שלך:** ${decision === 'approve' ? 'להמליץ על חנינה' : 'לדחות את הבקשה'}.`; // Basic decision
        feedbackText.innerHTML += `<br><br>${currentCase.feedback[decision]}`; // Detailed feedback

         // Add visual cue to feedback area based on decision (optional, but adds flair)
         feedbackAreaDiv.style.borderColor = decision === 'approve' ? var_approve_color : var_reject_color; // This won't work directly with CSS vars in JS style property. Need to get computed style or define colors in JS. Let's use classes instead.
         feedbackAreaDiv.classList.remove('approve-feedback', 'reject-feedback'); // Clean previous classes
         feedbackAreaDiv.classList.add(decision + '-feedback'); // Add new class for styling


         // Fade in feedback
         feedbackAreaDiv.classList.remove('fade-out'); // Ensure no outgoing class
         feedbackAreaDiv.style.display = 'block'; // Make sure it's block before fading in
         await animateElement(feedbackAreaDiv, 'fade-in', 500);

        // Show next/end button
         nextCaseBtn.style.display = 'block';
         if (currentCaseIndex + 1 >= cases.length) {
             nextCaseBtn.textContent = 'סיים סימולטור';
         } else {
             nextCaseBtn.textContent = 'למקרה הבא';
         }


         // Re-enable buttons after transition (though they are hidden now)
         approveBtn.disabled = false;
         rejectBtn.disabled = false;
    }

    async function endSimulator() {
        // Fade out existing content if any
        if (feedbackAreaDiv.style.display !== 'none') {
             await animateElement(feedbackAreaDiv, 'fade-out', 300);
        } else if (casePresentationDiv.style.display !== 'none') {
             await animateElement(casePresentationDiv, 'fade-out', 300);
        }
         decisionButtonsDiv.style.display = 'none'; // Ensure buttons are hidden
         biasHintDiv.style.display = 'none'; // Ensure hint is hidden


        // Fade in end screen
        endScreenDiv.classList.remove('fade-out');
        endScreenDiv.style.display = 'block';
        animateElement(endScreenDiv, 'fade-in', 500);
    }

    async function restartSimulator() {
        // Fade out end screen
         await animateElement(endScreenDiv, 'fade-out', 300);

        // Reset index and load first case
        currentCaseIndex = 0;
        loadCase(currentCaseIndex);
    }

    // Event Listeners
    approveBtn.addEventListener('click', () => showFeedback('approve'));
    rejectBtn.addEventListener('click', () => showFeedback('reject'));
    nextCaseBtn.addEventListener('click', () => loadCase(currentCaseIndex)); // currentCaseIndex was incremented in showFeedback
    restartBtn.addEventListener('click', restartSimulator);

    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        if (isHidden) {
             explanationDiv.style.display = 'block';
             toggleExplanationBtn.textContent = 'הסתרת ההסבר המורחב';
             animateElement(explanationDiv, 'fade-in', 300);
        } else {
             animateElement(explanationDiv, 'fade-out', 300).then(() => {
                  explanationDiv.style.display = 'none';
                   toggleExplanationBtn.textContent = 'הצגת/הסתרת ההסבר המורחב';
             });
        }
    });

    // Add classes for feedback background based on decision (CSS handles colors)
     const styleSheet = document.styleSheets[document.styleSheets.length - 1];
     styleSheet.insertRule('.feedback.approve-feedback { border-color: var(--approve-color); background-color: #e9f7ef; }', styleSheet.cssRules.length);
     styleSheet.insertRule('.feedback.reject-feedback { border-color: var(--reject-color); background-color: #fdedee; }', styleSheet.cssRules.length);


    // Initialize the simulator
    loadCase(currentCaseIndex);

</script>
```