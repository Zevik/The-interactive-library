---
title: "CRISPR: כך חותכים ועורכים DNA בדיוק מדהים"
english_slug: crispr-how-to-cut-and-edit-dna-with-precision
category: "מדעי החיים / ביולוגיה"
tags:
  - ביולוגיה מולקולרית
  - הנדסה גנטית
  - DNA
  - עריכת גנום
  - CRISPR-Cas9
---
# CRISPR: כך חותכים ועורכים DNA בדיוק מדהים

דמיינו לרגע שיש לכם את היכולת לערוך את ה'קוד' הגנטי שקובע מי אנחנו ואיך אנחנו נראים, ממש כמו לערוך מסמך טקסט במחשב. זה כבר לא מדע בדיוני! טכנולוגיית ה-CRISPR-Cas9 המדהימה מאפשרת לנו לעשות בדיוק את זה – לערוך DNA בדיוק חסר תקדים. הפוטנציאל שלה לחולל מהפכה ברפואה, בחקלאות ובהבנת החיים הוא עצום. אבל איך, לכל הרוחות, זה עובד? צאו למסע אינטראקטיבי ותגלו בעצמכם!

<div id="crispr-app">
    <h2>המשימה: מצא וחתך את רצף המטרה ב-DNA!</h2>
    <div class="app-container">
        <div class="dna-wrapper">
             <div class="dna-container">
                 <div class="dna-double-helix">
                     <div class="dna-strand top-strand">
                         <span class="nucleotide">A</span><span class="nucleotide">G</span><span class="nucleotide">G</span><span class="nucleotide">T</span><span class="nucleotide">C</span><span class="nucleotide">C</span><span class="nucleotide">A</span><span class="nucleotide">G</span><span class="nucleotide">T</span><span class="nucleotide nucleotide-pam">G</span><span class="nucleotide nucleotide-target">G</span><span class="nucleotide nucleotide-target">A</span><span class="nucleotide nucleotide-target">T</span><span class="nucleotide nucleotide-target">T</span><span class="nucleotide nucleotide-target">G</span><span class="nucleotide nucleotide-target">C</span><span class="nucleotide">T</span><span class="nucleotide">A</span><span class="nucleotide">G</span><span class="nucleotide">C</span><span class="nucleotide">T</span><span class="nucleotide">C</span><span class="nucleotide">A</span><span class="nucleotide">G</span>
                     </div>
                     <div class="dna-strand bottom-strand">
                         <span class="nucleotide">T</span><span class="nucleotide">C</span><span class="nucleotide">C</span><span class="nucleotide">A</span><span class="nucleotide">G</span><span class="nucleotide">G</span><span class="nucleotide">T</span><span class="nucleotide">C</span><span class="nucleotide">A</span><span class="nucleotide nucleotide-pam">C</span><span class="nucleotide nucleotide-target">C</span><span class="nucleotide nucleotide-target">T</span><span class="nucleotide nucleotide-target">A</span><span class="nucleotide nucleotide-target">A</span><span class="nucleotide nucleotide-target">C</span><span class="nucleotide nucleotide-target">G</span><span class="nucleotide">A</span><span class="nucleotide">T</span><span class="nucleotide">C</span><span class="nucleotide">G</span><span class="nucleotide">A</span><span class="nucleotide">G</span><span class="nucleotide">T</span><span class="nucleotide">C</span>
                     </div>
                 </div>
                 <div class="cut-line"></div>
                 <div class="dna-break-left"></div>
                 <div class="dna-break-right"></div>
             </div>
        </div>

        <div class="components-area">
            <div id="cas9" class="draggable component cas9-comp">
                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2IDYiPjxjaXJjbGUgc3R5bGU9ImZpbGw6I2U3NGMzcDsiIGN4PSIzIiBjY2U9IjMiIHI9IjIiLz48cGF0aCBzdHlsZT0iZmlsbDojZmZmO29wYWNpdHk6MC44OyIgZD0iTTIgMS41djNjMC41LS41IDEtMSAxLjUtMS41UzQgMSAyIDEuNXoiLz48cGF0aCBzdHlsZT0iZmlsbDojZmZmO29wYWNpdHk6MC44OyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNiA2KSByb3RhdGUoMTgwKSIgZD0iTTIgMS41djNjMC41LS41IDEtMSAxLjUtMS41UzQgMSAyIDEuNXoiLz48L3N2Zw==" alt="Cas9 Enzyme">
                <p>אנזים Cas9</p>
            </div>
            <div id="sgrna" class="draggable component sgrna-comp">
                 <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2IDYiPjxjaXJjbGUgc3R5bGU9ImZpbGw6IzM0OTgyZjtvcGFjaXR5OjAuODsiIGN4PSIzIiBjY2E9IjMiIHI9IjIiLz48cGF0aCBzdHlsZT0iZmlsbDpub25lO3N0cm9rZTojZmZmO3N0cm9rZS13aWR0aDowLjU7b3BhY2l0eTowLjg7IiBkPSJNMCAzaDNtMCAwYTQuOCA0LjggMCAwMTMgMHoiLz48L3N2Zw==" alt="sgRNA Molecule">
                <p>מולקולת sgRNA</p>
                <div class="target-sequence-label">רצף מטרה: <span class="target-sequence">GATTGC</span></div>
            </div>
        </div>

        <div id="complex-area" class="drop-zone">
            <p>גרור את ה-<span class="sgrna-label">sgRNA</span> לכאן<br>כדי לחבר אותו לאנזים <span class="cas9-label">Cas9</span></p>
        </div>
        <div id="dna-drop-zone" class="drop-zone">
            <p>גרור את קומפלקס<br><span class="cas9-label">Cas9</span> + <span class="sgrna-label">sgRNA</span><br>אל גדיל ה-DNA</p>
        </div>

         <div class="message-box"></div>
    </div>
</div>

<button id="toggle-explanation">הצג/הסתר הסבר מפורט</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מפורט: איך CRISPR עובד</h2>
    <p><strong>מהי מערכת CRISPR-Cas9?</strong></p>
    <p>מערכת CRISPR-Cas9 התגלתה לראשונה בחיידקים ובחיידקי-קשת (Archaea), שם היא משמשת כמנגנון הגנה נגד פלישת וירוסים (בקטריופאג'ים) ופלסמידים. היא מאפשרת לחיידק לזהות ולנטרל DNA זר על ידי חיתוכו.</p>

    <p><strong>המרכיבים העיקריים:</strong></p>
    <ul>
        <li><strong>אנזים Cas9:</strong> זהו מעין 'מספריים מולקולריות' שיכולות לחתוך את שני הגדילים של ה-DNA. האנזים הזה לא פועל לבד, אלא זקוק למכוון.</li>
        <li><strong>מולקולת sgRNA (single guide RNA):</strong> מולקולת RNA קצרה זו מורכבת משני חלקים עיקריים: חלק אחד נקשר לאנזים Cas9, וחלק שני (המכונה 'רצף המדריך' או Guide Sequence) מכיל רצף נוקלאוטידים התואם לרצף המטרה ב-DNA שאותו אנו רוצים לחתוך. ה-sgRNA הוא למעשה ה'מפתח' או ה'מצפן' שמכווין את Cas9 לנקודה המדויקת בגנום.</li>
        <li><strong>רצף PAM (Protospacer Adjacent Motif):</strong> רצף קצר (בדרך כלל 2-5 נוקלאוטידים) שנמצא בסמוך לרצף המטרה ב-DNA. אנזים Cas9 חייב לזהות את רצף ה-PAM בנוסף לרצף המטרה כדי להיקשר ביעילות ל-DNA ולבצע את החיתוך. הוא משמש כמעין 'חותמת' או 'סימן זיהוי' ל-Cas9, ומונע ממנו לחתוך בטעות את ה-DNA של החיידק עצמו (שאין לו PAM ליד רצפי ה-CRISPR הפנימיים שלו).</li>
    </ul>

    <p><strong>איך הקומפלקס 'מוצא' את רצף המטרה הספציפי?</strong></p>
    <p>לאחר שקומפלקס Cas9-sgRNA נוצר, הוא נקשר לגדיל ה-DNA הכפול ו'סורק' אותו. ה-sgRNA 'בודק' כל הזמן התאמה בין רצף המדריך שלו לבין רצפי ה-DNA שהוא פוגש (זיווג בסיסים: A עם T, G עם C). במקביל, אנזים Cas9 מחפש את רצף ה-PAM. רק כאשר הקומפלקס מזהה *גם* התאמה טובה לרצף המטרה על ידי ה-sgRNA *וגם* את רצף ה-PAM במיקום הנכון ליד רצף המטרה, הקומפלקס נקשר בחוזקה לאתר ומפעיל את פעולת החיתוך.</p>

    <p><strong>פעולת החיתוך הכפולה של Cas9 ב-DNA:</strong></p>
    <p>ברגע שהקומפלקס מקובע על רצף המטרה ב-DNA (בעזרת ה-sgRNA וזיהוי ה-PAM), אנזים Cas9 מפעיל את הפעילות האנזימטית שלו ויוצר חיתוך בשני גדילי ה-DNA. החיתוך מתרחש במרחק קצר מאתר ה-PAM, בתוך רצף המטרה שזוהה על ידי ה-sgRNA. חיתוך כפול גדילים זה (DSB - Double-Strand Break) הוא נקודת המפתח לתהליך העריכה, מכיוון שהוא 'שובר' למעשה את ה-DNA ומאלץ את התא להפעיל מנגנוני תיקון.</p>

    <p><strong>מנגנוני התיקון הטבעיים של התא:</strong></p>
    <p>התא מזהה את החיתוך הכפול ב-DNA כמצב חירום ומפעיל מיד מנגנוני תיקון טבעיים:</p>
    <ul>
        <li><strong>NHEJ (Non-Homologous End Joining):</strong> זהו המנגנון הנפוץ והראשון שמופעל. התא מנסה לחבר מחדש את קצוות ה-DNA החתוכים במהירות. תהליך זה נוטה להיות 'רשלני' ויכול להוביל להכנסה או הסרה של נוקלאוטידים בנקודת החיתוך. שינויים אלה (indels) יכולים לשבש את רצף הגן ולמעשה 'להשבית' אותו או ליצור שינויים קטנים. שיטה זו משמשת לעיתים קרובות כדי "לכבות" גן מסוים או לגרום למוטציה אקראית באתר החיתוך.</li>
        <li><strong>HDR (Homology-Directed Repair):</strong> מנגנון זה פעיל בעיקר בשלבים מסוימים של מחזור התא (כאשר יש עותק נוסף של ה-DNA, למשל אחרי שכפול). הוא משתמש בתבנית DNA (מולקולת DNA נוספת בעלת רצף דומה לאזור החיתוך) כדי לתקן את השבר בצורה מדויקת. בטכנולוגיית CRISPR, ניתן לספק לתא תבנית DNA חדשה המכילה את השינוי הרצוי (למשל, רצף נורמלי במקום פגם גנטי, או הוספת גן חדש). התא ישתמש בתבנית זו כדי לתקן את החיתוך ולהכניס את השינוי הרצוי באופן מדויק. מנגנון זה פחות יעיל מ-NHEJ ודורש תכנון נוסף, אך הוא המפתח לעריכה מדויקת.</li>
    </ul>
    <p>היכולת לנצל את מנגנוני התיקון של התא לאחר החיתוך שמבצע CRISPR היא מה שהופך את הטכנולוגיה לכלי עריכה גנטית כה עוצמתי – אנחנו לא רק חותכים, אנחנו מנצלים את ה"תיקונצ'יקים" הטבעיים של התא כדי לבצע את השינוי שרצינו.</p>

    <p><strong>יישומים פוטנציאליים:</strong></p>
    <p>טכנולוגיית CRISPR פותחת דלתות ליישומים רבים, כולל:</p>
    <ul>
        <li>ריפוי מחלות גנטיות על ידי תיקון המוטציה הגורמת למחלה (למשל, ציסטיק פיברוזיס, אנמיה חרמשית).</li>
        <li>פיתוח טיפולים לסרטן על ידי שיפור תאי מערכת החיסון או השבתת גנים בתאי גידול.</li>
        <li>יצירת זנים חקלאיים משופרים עם עמידות למחלות, יבול גדול יותר או ערך תזונתי משופר.</li>
        <li>הבנה מעמיקה יותר של תפקידי גנים שונים במחלות ובתהליכים ביולוגיים.</li>
    </ul>

    <p><strong>אתגרים וסוגיות אתיות:</strong></p>
    <p>למרות הפוטנציאל העצום, ישנם גם אתגרים וחששות. האתגרים כוללים דיוק (חיתוכים לא רצויים באזורים אחרים בגנום - off-target effects) ויעילות (הכנסת המערכת לתאים). סוגיות אתיות משמעותיות עולות לגבי עריכת גנום באמבריונים אנושיים (עריכת קו הנבט), מכיוון ששינויים כאלה עוברים בתורשה לדורות הבאים, ונדרש דיון ציבורי ורגולציה קפדנית.</p>
</div>

<style>
/* כללי */
#crispr-app {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin-top: 20px;
    border: 1px solid #d0d0d0;
    padding: 20px;
    border-radius: 12px;
    background-color: #eef5ff; /* רקע תכלת בהיר */
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    direction: rtl; /* תמיכה בעברית */
    text-align: right;
}

#crispr-app h2 {
    text-align: center;
    color: #0056b3; /* כחול כהה */
    margin-bottom: 25px;
    font-size: 1.6em;
}

.app-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
}

/* אזור ה-DNA */
.dna-wrapper {
    width: 100%;
    max-width: 800px;
    overflow-x: auto; /* גלילה אופקית ל-DNA ארוך */
    padding-bottom: 10px; /* מקום לפס גלילה */
}

.dna-container {
    min-width: fit-content; /* מונע כיווץ ה-DNA */
    min-height: 100px; /* גובה מינימלי לאזור */
    border: 2px dashed #a0c4ff; /* קו מקווקו עדין */
    border-radius: 8px;
    padding: 20px 10px;
    position: relative;
    background: linear-gradient(to bottom, #ffffff, #f0f8ff); /* רקע עם גרדיאנט עדין */
    display: flex;
    align-items: center; /* מרכז אנכית את ההליקס */
    justify-content: flex-start; /* מתחיל את ה-DNA משמאל */
}

.dna-double-helix {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 60px; /* גובה ההליקס */
    white-space: nowrap; /* מונע גלישת שורות */
    position: relative;
}

.dna-strand {
    display: flex;
    height: 25px; /* גובה גדיל יחיד */
    line-height: 25px;
    font-size: 1.1em;
    font-weight: bold;
}

.top-strand {
    color: #333;
}

.bottom-strand {
    color: #333;
    transform: rotate(180deg); /* היפוך ויזואלי */
    direction: ltr; /* שומר על כיוון אותיות */
    margin-top: 10px; /* רווח קטן בין הגדילים */
}

.bottom-strand span {
     transform: rotate(180deg); /* היפוך נוקלאוטידים בחזרה */
     display: inline-block;
}

.nucleotide {
    display: inline-block;
    width: 25px; /* רוחב כל נוקלאוטיד */
    text-align: center;
    user-select: none;
    position: relative; /* למיקום אפשרי של אפקטים */
    transition: color 0.3s ease; /* אנימציית צבע עדינה */
}

/* הדגשת רצפים */
.nucleotide-target {
    color: #e74c3c; /* אדום - מטרה */
    font-weight: bold;
    text-shadow: 0 0 3px rgba(231, 76, 60, 0.5); /* צל עדין להדגשה */
}
.nucleotide-pam {
     color: #f39c12; /* כתום - PAM */
     font-weight: bold;
     text-shadow: 0 0 3px rgba(243, 156, 18, 0.5); /* צל עדין להדגשה */
}


/* קו חיתוך ואנימציית שבר */
.cut-line {
    position: absolute;
    top: 10px; /* aligns with DNA padding */
    bottom: 10px; /* aligns with DNA padding */
    width: 3px;
    background-color: #c0392b; /* אדום כהה */
    display: none; /* מוסתר בהתחלה */
    left: 0; /* ימוקם ע"י JS */
    z-index: 2; /* מעל ה-DNA */
    box-shadow: 0 0 8px rgba(192, 57, 43, 0.8);
}

.dna-break-left, .dna-break-right {
    position: absolute;
    top: 10px; /* aligns with DNA padding */
    bottom: 10px; /* aligns with DNA padding */
    width: 5px; /* רוחב השבר */
    background-color: rgba(192, 57, 43, 0.6); /* צבע שבר עדין */
    display: none; /* מוסתר בהתחלה */
    z-index: 1; /* מתחת לקו החיתוך */
    opacity: 0; /* שקוף בהתחלה */
}
.dna-break-left { left: 0; } /* ימוקם שמאלה מקו החיתוך */
.dna-break-right { left: 0; } /* ימוקם ימינה מקו החיתוך */


/* אזור רכיבים */
.components-area {
    display: flex;
    justify-content: center;
    gap: 40px; /* רווח גדול יותר */
    margin-bottom: 20px;
    padding: 15px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.component {
    text-align: center;
    cursor: grab;
    padding: 12px 15px; /* ריפוד מוגדל */
    border: 1px solid #ccc;
    border-radius: 8px; /* פינות מעוגלות יותר */
    background-color: #f8f8f8; /* רקע כמעט לבן */
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease;
    position: relative;
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.component:hover {
    transform: translateY(-5px); /* אפקט הרחפה בהוםר */
    box-shadow: 0 6px 15px rgba(0,0,0,0.15);
}

.component img {
    width: 55px; /* גודל אייקון מוגדל */
    height: 55px;
    display: block;
    margin: 0 auto 8px auto; /* רווח מתחת לתמונה */
    border-radius: 50%; /* אייקונים עגולים */
    padding: 6px; /* ריפוד פנימי לאייקון */
    box-shadow: inset 0 0 5px rgba(0,0,0,0.1);
}

.cas9-comp img { background-color: #e74c3c; } /* אדום ל-Cas9 */
.sgrna-comp img { background-color: #3498db; } /* כחול ל-sgRNA */

.component p {
    margin: 0; /* מנקה שוליים */
    font-size: 1em; /* גודל טקסט רגיל */
    font-weight: bold;
    color: #555;
}

.target-sequence-label {
    font-size: 0.9em;
    color: #333;
    margin-top: 8px;
    border-top: 1px dashed #eee;
    padding-top: 5px;
}
.target-sequence {
    font-family: 'Courier New', Courier, monospace; /* פונט מונטספייס לרצף */
    font-weight: bold;
    color: #e74c3c; /* צבע המטרה */
}


/* אזורי גרירה */
.drop-zone {
    width: 90%;
    max-width: 500px;
    min-height: 80px; /* גובה מינימלי לאזור */
    border: 3px dashed #007bff; /* קו כחול בולט יותר */
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #007bff;
    background-color: #e9f5ff; /* רקע בהיר יותר */
    margin-bottom: 20px;
    transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.2s ease;
    font-size: 1.1em;
    font-weight: bold;
}

.drop-zone p {
    margin: 0;
    line-height: 1.5;
}

.drop-zone .cas9-label { color: #e74c3c; font-weight: bold;}
.drop-zone .sgrna-label { color: #3498db; font-weight: bold;}


.drop-zone.hover {
    background-color: #cce5ff; /* רקע כחול בהיר יותר בהוםר */
    border-color: #0056b3; /* קו כחול כהה יותר */
    transform: scale(1.02); /* אפקט זום קטן בהוםר */
}

#complex-area {
    flex-direction: column;
}

#dna-drop-zone {
     min-height: 120px; /* גובה מוגדל */
     max-width: 95%;
}

/* קומפלקס מאוחד */
.cas9-complex {
    cursor: grab; /* קומפלקס גם ניתן לגרירה */
    background: linear-gradient(to right, #e74c3c 40%, #3498db 60%); /* גרדיאנט המשלב את הצבעים */
    border-color: #555;
    box-shadow: 0 6px 15px rgba(0,0,0,0.2);
    display: flex;
    align-items: center;
    justify-content: center; /* מרכוז תוכן הקומפלקס */
    padding: 10px 15px;
    gap: 15px; /* רווח בין הרכיבים בקומפלקס */
    min-height: 80px; /* גובה מינימלי לקומפלקס */
}

.cas9-complex img {
    width: 45px; /* גודל אייקון מופחת בתוך קומפלקס */
    height: 45px;
    padding: 5px;
    box-shadow: none; /* מנקה צל פנימי */
    background: rgba(255, 255, 255, 0.3); /* רקע שקוף עדין */
}

.cas9-complex p {
    color: #fff; /* טקסט לבן על רקע כהה */
    text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    font-size: 1em;
}

.cas9-complex .sgrna-comp {
     position: static; /* מבטל מיקום אבסולוטי אם היה */
     border: none;
     padding: 0;
     margin: 0;
     background: none;
     box-shadow: none;
     cursor: grab; /* עדיין ניתן לגרירה כחלק מהקומפלקס */
     transition: none;
     flex-direction: row; /* רכיבי sgRNA בשורה */
     align-items: center;
     gap: 5px; /* רווח בין האייקון לטקסט */
}
.cas9-complex .sgrna-comp img {
    width: 35px; /* גודל אייקון sgRNA בקומפלקס */
    height: 35px;
}
.cas9-complex .sgrna-comp p, .cas9-complex .target-sequence-label {
     color: #fff; /* טקסט לבן */
     font-size: 0.9em;
     margin: 0;
}
.cas9-complex .target-sequence-label {
     border-top: none;
     padding-top: 0;
}

.cas9-complex.ready-to-cut {
    cursor: pointer; /* הופך לסמן יד כשאפשר ללחוץ */
    animation: pulse-glow 1.5s infinite alternate; /* אנימציית פעימה כשהוא מוכן */
}

/* הודעות */
.message-box {
    min-height: 50px; /* גובה מינימלי להודעה */
    color: #333;
    font-weight: bold;
    text-align: center;
    margin-top: 15px;
    padding: 10px;
    background-color: #fffacd; /* רקע צהבהב עדין */
    border: 1px solid #ffebcd;
    border-radius: 8px;
    width: 90%;
    max-width: 600px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    line-height: 1.4;
}


/* כפתור הסבר */
#toggle-explanation {
    display: block;
    margin: 30px auto; /* מרווח גדול יותר */
    padding: 12px 25px; /* ריפוד מוגדל */
    font-size: 1.1em; /* גודל פונט מוגדל */
    cursor: pointer;
    border: none;
    border-radius: 25px; /* כפתור עגול יותר */
    background-color: #28a745; /* ירוק */
    color: white;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

#toggle-explanation:hover {
    background-color: #218838; /* ירוק כהה יותר בהוםר */
    transform: translateY(-2px); /* אפקט הרחפה קטן */
}

#toggle-explanation:active {
    transform: translateY(0); /* חוזר למקומו בלחיצה */
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}


/* אזור ההסבר */
#explanation {
    margin-top: 20px;
    padding: 25px; /* ריפוד מוגדל */
    border: 1px solid #d0d0d0;
    border-radius: 12px;
    background-color: #f9f9f9;
    line-height: 1.7; /* מרווח שורות גדול יותר */
    color: #333;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
}

#explanation h2, #explanation h3 {
    color: #0056b3;
    margin-top: 20px;
    margin-bottom: 12px;
    border-bottom: 1px solid #eee;
    padding-bottom: 5px;
}

#explanation p {
    margin-bottom: 15px;
}

#explanation strong {
    color: #0056b3;
}

#explanation ul {
    margin-bottom: 15px;
    padding-right: 20px; /* ריפוד לרשימה */
    list-style-type: disc; /* נקודות לרשימה */
}

#explanation li {
    margin-bottom: 10px;
}


/* Dragula Styles - Minimal + custom */
.gu-mirror {
  position: fixed !important;
  margin: 0 !important;
  z-index: 9999 !important;
  opacity: 0.9; /* פחות שקוף */
  list-style-type: none;
  transform: rotate(3deg); /* הטיה קלה בגרירה */
  transition: none !important; /* מונע אנימציה בזמן גרירה */
}
.gu-hide {
  display: none !important;
}
.gu-unselectable {
  -webkit-user-select: none !important;
  -moz-user-select: none !important;
  -ms-user-select: none !important;
  user-select: none !important;
}
.gu-transit {
  opacity: 0.4; /* הרכיב המקורי שקוף יותר */
}

/* אנימציות */
@keyframes pulse-glow {
    from { box-shadow: 0 0 10px rgba(52, 152, 219, 0.7); } /* זוהר כחול */
    to { box-shadow: 0 0 20px rgba(231, 76, 60, 0.8), 0 0 25px rgba(52, 152, 219, 0.8); } /* זוהר אדום וכחול */
}

@keyframes dna-cut-pulse {
    from { transform: translateX(-50%) scaleY(1); opacity: 1; }
    to { transform: translateX(-50%) scaleY(1.1); opacity: 0.7; }
}

@keyframes dna-break-out {
     from { opacity: 0; }
     to { opacity: 1; }
}


</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/dragula/3.7.2/dragula.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/dragula/3.7.2/dragula.min.css">

<script>
document.addEventListener('DOMContentLoaded', () => {
    const cas9 = document.getElementById('cas9');
    const sgrna = document.getElementById('sgrna');
    const complexArea = document.getElementById('complex-area');
    const dnaDropZone = document.getElementById('dna-drop-zone');
    const dnaContainer = document.querySelector('.dna-container');
    const dnaDoubleHelix = document.querySelector('.dna-double-helix');
    const messageBox = document.querySelector('.message-box');
    const cutLine = document.querySelector('.cut-line');
    const dnaBreakLeft = document.querySelector('.dna-break-left');
    const dnaBreakRight = document.querySelector('.dna-break-right');
    const componentsArea = document.querySelector('.components-area'); // To hide components later

    let isComplexFormed = false;
    let complexElement = null; // To store the complex element

    messageBox.innerHTML = "שלום! בואו נלמד איך CRISPR-Cas9 עובד. <br> <strong>המשימה הראשונה:</strong> חברו את אנזים <span class='cas9-label'>Cas9</span> עם מולקולת ה-<span class='sgrna-label'>sgRNA</span>. גררו את ה-<span class='sgrna-label'>sgRNA</span> לאזור החיבור.";

    // Initialize Dragula
    const drake = dragula([componentsArea, complexArea, dnaDropZone], {
        accepts: function (el, target, source, sibling) {
            // Rule 1: Only sgRNA can be dropped into complexArea initially
            if (target === complexArea) {
                return el === sgrna && !isComplexFormed;
            }
            // Rule 2: Only the complex can be dropped into dnaDropZone
            if (target === dnaDropZone) {
                 // Check if the element being dragged is the complex and complex is formed
                 return el.classList.contains('cas9-complex') && isComplexFormed;
            }
             // Prevent dropping components anywhere else if not the correct target
             if (el === sgrna && target !== complexArea && source === componentsArea) {
                 return false; // sgRNA can only go to complexArea
             }
             if (el === cas9 && source === componentsArea) {
                  return false; // Cas9 cannot be moved individually after start
             }
             if (el.classList.contains('cas9-complex') && target !== dnaDropZone && source === complexArea) {
                  return false; // Complex can only go to dnaDropZone
             }

            return true; // Default acceptance (shouldn't be reached with above rules)
        },
        moves: function (el, source, handle, sibling) {
             // Only allow dragging initial components from componentsArea or the formed complex from complexArea
            if (source === componentsArea) {
                return el === sgrna || el === cas9; // Allow dragging sgrna or cas9 initially
            }
            if (source === complexArea) {
                 return el === complexElement; // Allow dragging the complex element
            }
             // Prevent dragging from dnaDropZone after complex is placed
            if (source === dnaDropZone) {
                 return false;
            }
            return true; // Allow dragging from other places if needed (but controlled by accepts)
        }
    });

    drake.on('drag', function(el, source) {
         // Add hover class to potential drop targets
        if (el === sgrna && !isComplexFormed) {
            complexArea.classList.add('hover');
        } else if (el.classList.contains('cas9-complex') && isComplexFormed) {
             dnaDropZone.classList.add('hover');
        }
         el.classList.add('is-dragging'); // Add class for drag animation
    });

    drake.on('dragend', function(el) {
         // Remove hover classes from all drop targets
         complexArea.classList.remove('hover');
         dnaDropZone.classList.remove('hover');
         el.classList.remove('is-dragging'); // Remove drag animation class
    });


    drake.on('drop', function (el, target, source, sibling) {
        // sgRNA dropped into complexArea
        if (el === sgrna && target === complexArea && !isComplexFormed) {
            // Create the complex element
            complexElement = document.createElement('div');
            complexElement.classList.add('component', 'cas9-complex');

            // Move Cas9 img and text into the complex element
            const cas9Img = cas9.querySelector('img').cloneNode(true); // Clone to preserve original if needed later, though we remove the parent
            const cas9P = cas9.querySelector('p').cloneNode(true);
            complexElement.appendChild(cas9Img);
            complexElement.appendChild(cas9P);
            // cas9.remove(); // Removed by dragula

            // Move sgRNA img and text into the complex element
            const sgrnaImg = sgrna.querySelector('img').cloneNode(true);
            const sgrnaP = sgrna.querySelector('p').cloneNode(true);
            const targetSeqLabel = sgrna.querySelector('.target-sequence-label').cloneNode(true);
            // sgrna.remove(); // Removed by dragula

            const sgRNAComponentDiv = document.createElement('div'); // Wrap sgRNA parts for layout
            sgRNAComponentDiv.classList.add('sgrna-comp');
            sgRNAComponentDiv.appendChild(sgrnaImg);
            sgRNAComponentDiv.appendChild(sgrnaP);
            sgRNAComponentDiv.appendChild(targetSeqLabel); // Add target sequence label

            complexElement.appendChild(sgRNAComponentDiv);

            // Remove original components visually and from dragula sources
            componentsArea.style.display = 'none'; // Hide the initial components area

            // Add the complex to the complex area
            target.innerHTML = ''; // Clear the area text
            target.appendChild(complexElement);
            isComplexFormed = true;

            messageBox.innerHTML = "קומפלקס <span class='cas9-label'>Cas9</span> + <span class='sgrna-label'>sgRNA</span> נוצר בהצלחה! <br> <strong>המשימה הבאה:</strong> גרור/י את הקומפלקס החדש אל גדיל ה-DNA.";
            complexArea.classList.remove('drop-zone'); // It's no longer just a drop zone for sgRNA
            complexArea.style.border = 'none'; // Remove drop zone styling
            complexArea.style.backgroundColor = 'transparent'; // Remove background
            complexArea.style.minHeight = 'auto'; // Adjust height


            // Update dragula containers and moves rules for the next step
            drake.containers = [complexArea, dnaDropZone]; // Now only complexArea is a source for complex
            drake.options.moves = function (el, source, handle, sibling) {
                // Allow dragging the complex from complexArea
                 return source === complexArea && el === complexElement;
             };
             drake.options.accepts = function (el, target, source, sibling) {
                 // Only accept complex in dnaDropZone now
                 return target === dnaDropZone && el === complexElement;
             }


        }
        // Complex dropped onto dnaDropZone
        else if (el === complexElement && target === dnaDropZone && isComplexFormed) {
            messageBox.innerHTML = "קומפלקס <span class='cas9-label'>Cas9</span> + <span class='sgrna-label'>sgRNA</span> נקשר ל-DNA ומתחיל לסרוק בחיפוש אחר רצף המטרה (<span class='target-sequence'>GATTGC</span>) וה-PAM (<span class='nucleotide-pam'>G</span>)...";

            // Position the complex relative to the DNA container for animation
            const dnaContainerRect = dnaContainer.getBoundingClientRect();
            const dropZoneRect = dnaDropZone.getBoundingClientRect();
            const complexRect = complexElement.getBoundingClientRect();

            // Calculate initial position (centered within the drop zone, relative to dnaContainer)
            // Needs to account for dnaContainer's scroll position if any, but simplified here.
            // Let's position it just before the DNA starts visually within the container
             const initialLeft = 10; // Start near the left padding of dnaContainer
             const initialTop = (dnaContainer.offsetHeight / 2) - (complexRect.height / 2); // Center vertically

            complexElement.style.position = 'absolute';
            complexElement.style.left = initialLeft + 'px';
            complexElement.style.top = initialTop + 'px';

             // Move complex element from its current parent (complexArea) to dnaContainer
             // source.removeChild(el); // Dragula handles this
             dnaContainer.appendChild(complexElement); // Append to DNA container for relative positioning

            dnaDropZone.style.display = 'none'; // Hide the drop zone after drop
            complexArea.style.display = 'none'; // Hide complex area as well


            // --- Find the target sequence position and Animate Scanning ---
            const targetSequence = "GATTGC"; // From sgRNA target sequence label
            const pamSequence = "G"; // The PAM sequence *preceding* the target in this visualization
            // Get all nucleotide spans in the top strand
            const dnaNucleotides = dnaDoubleHelix.querySelector('.top-strand').querySelectorAll('.nucleotide');
            let dnaSequenceText = '';
            let targetStartIndex = -1;
            let pamStartIndex = -1;

            // Reconstruct the full DNA sequence string and find indices
            dnaNucleotides.forEach((span, index) => {
                dnaSequenceText += span.textContent.trim();
                 // Find the START index of the target sequence and PAM sequence
                 // Assuming PAM is directly before the target
                 const fullMatchSequence = pamSequence + targetSequence;
                 if (dnaSequenceText.endsWith(fullMatchSequence)) {
                      pamStartIndex = index - (fullMatchSequence.length -1) + (pamSequence.length -1) ; // Index of the start of PAM
                     targetStartIndex = index - (fullMatchSequence.length -1) + fullMatchSequence.length - targetSequence.length; // Index of the start of target
                 }
            });

            console.log("DNA Sequence:", dnaSequenceText);
            console.log("Target Sequence:", targetSequence, "found at index:", targetStartIndex);
            console.log("PAM Sequence:", pamSequence, "found at index:", pamStartIndex);


            if (targetStartIndex === -1 || pamStartIndex === -1 || pamStartIndex !== targetStartIndex - pamSequence.length) {
                messageBox.innerHTML = "אופס! משהו השתבש במציאת הרצף. אנא רענן/י את העמוד ונסה/י שוב.";
                console.error("Target or PAM sequence not found correctly.");
                return; // Stop if target/PAM not found correctly
            }

            // Calculate the target position in pixels
            // Position should be at the START of the PAM sequence visualization area
            const nucleotideWidth = dnaNucleotides[0] ? dnaNucleotides[0].offsetWidth : 25; // Get actual width or use default
            const targetPixelPosition = pamStartIndex * nucleotideWidth; // Position the complex at the start of the PAM


            // Animate the complex moving to the target position
            const scanDuration = 4; // seconds
            complexElement.style.transition = `left ${scanDuration}s linear`;
            complexElement.style.left = targetPixelPosition + 'px';


            complexElement.addEventListener('transitionend', () => {
                messageBox.innerHTML = "קומפלקס <span class='cas9-label'>Cas9</span> + <span class='sgrna-label'>sgRNA</span> מצא את רצף ה-PAM והמטרה! <br> <strong>המשימה האחרונה:</strong> לחץ/י על הקומפלקס כדי לבצע את החיתוך!";

                // Add visual cue for binding - maybe scale up slightly?
                complexElement.style.transition = 'none'; // Stop scanning transition
                complexElement.style.transform = 'scale(1.05)';
                complexElement.style.boxShadow = '0 0 20px rgba(0, 123, 255, 0.8)'; // Add a binding glow

                // Position cut line - it should be after the target sequence, typically 3-4 bases after PAM.
                // In our simple visual model, let's place it after the target sequence ends.
                 // Position the cut line after the target sequence + PAM sequence
                 const cutLineOffset = nucleotideWidth * (pamSequence.length + targetSequence.length);
                const cutLinePosition = pamStartIndex * nucleotideWidth + cutLineOffset - (nucleotideWidth / 2); // Adjust to be somewhat centered after the target sequence

                cutLine.style.left = cutLinePosition + 'px';
                cutLine.style.display = 'block';
                cutLine.style.height = '100%'; // Extend full height of dnaContainer padding
                 cutLine.style.animation = 'dna-cut-pulse 1s infinite alternate'; // Pulse while waiting for click

                // Make the complex clickable to trigger the cut
                complexElement.classList.add('ready-to-cut');
                complexElement.onclick = handleCutAction;


            }, { once: true }); // Ensure the event listener is called only once

             // Disable further dragging of the complex after it's placed on DNA
             drake.options.moves = function (el, source, handle, sibling) {
                  return false; // Cannot drag the complex after it's on the DNA
             };
             drake.options.accepts = function (el, target, source, sibling) {
                 return false; // Cannot drop anything anywhere after complex is on DNA
             }
        }
    });

    function handleCutAction() {
        if (!isComplexFormed || !complexElement || !complexElement.classList.contains('ready-to-cut')) return;

        messageBox.innerHTML = "<span class='cas9-label'>Cas9</span> מבצע את החיתוך! ה-DNA נחתך בהצלחה.<br>(כעת מנגנוני התיקון של התא יפעלו - NHEJ או HDR)";

        // Animation for cutting
        complexElement.style.animation = 'none'; // Stop pulse glow
        complexElement.style.transform = 'scale(1)'; // Return to normal size
        complexElement.style.boxShadow = '0 0 10px rgba(0,0,0,0.2)'; // Less prominent shadow

        cutLine.style.animation = 'none'; // Stop cut line pulse animation
        cutLine.style.backgroundColor = '#c0392b'; // Ensure color is set
        cutLine.style.width = '4px'; // Make cut line thicker temporarily
        cutLine.style.height = 'calc(100% + 20px)'; // Extend beyond padding slightly
         cutLine.style.top = '-10px'; // Adjust position

        // Simple DNA break visualization: Move parts slightly apart
        const cutPositionX = parseFloat(cutLine.style.left); // Get the position of the cut line

        dnaBreakLeft.style.display = 'block';
        dnaBreakRight.style.display = 'block';
        dnaBreakLeft.style.left = cutPositionX - 10 + 'px'; // Position left break piece left of cut
        dnaBreakRight.style.left = cutPositionX + 10 + 'px'; // Position right break piece right of cut
        dnaBreakLeft.style.width = '15px'; // Width of break effect
        dnaBreakRight.style.width = '15px';

        // Animate the break pieces fading in and moving slightly apart
        dnaBreakLeft.style.transition = 'left 1s ease-out, opacity 1s ease-out';
        dnaBreakRight.style.transition = 'left 1s ease-out, opacity 1s ease-out';
        dnaBreakLeft.style.left = cutPositionX - 25 + 'px'; // Move further left
        dnaBreakRight.style.left = cutPositionX + 25 + 'px'; // Move further right
        dnaBreakLeft.style.opacity = 1;
        dnaBreakRight.style.opacity = 1;

         // Animate complex moving away slightly after cutting
         complexElement.style.transition = 'transform 0.5s ease-out';
         complexElement.style.transform = 'scale(0.9) translateY(-10px)'; // Shrink and move up

        // Disable clicking the complex after cut is initiated
        complexElement.onclick = null;
        complexElement.classList.remove('ready-to-cut');
        complexElement.style.cursor = 'default';

        // Optionally, after a delay, fade out complex and cut line
        setTimeout(() => {
             complexElement.style.transition = 'opacity 1s ease-out';
             complexElement.style.opacity = 0;
             cutLine.style.transition = 'opacity 1s ease-out';
             cutLine.style.opacity = 0;
             // Hide break lines after a bit
             setTimeout(() => {
                  dnaBreakLeft.style.display = 'none';
                  dnaBreakRight.style.display = 'none';
             }, 1000); // Match fade out duration

             messageBox.innerHTML += "<br>הסימולציה הסתיימה. קראו את ההסבר למטה להבנה מעמיקה יותר!";

        }, 2000); // 2 seconds after cut message

    }


     // Explanation Toggle
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    toggleButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            explanationDiv.style.maxHeight = explanationDiv.scrollHeight + "px"; // Animate opening (simple)
            toggleButton.textContent = 'הסתר הסבר מפורט';
        } else {
            explanationDiv.style.display = 'none'; // Close instantly
            explanationDiv.style.maxHeight = "0"; // For potential future animation back
            toggleButton.textContent = 'הצג/הסתר הסבר מפורט';
        }
    });

    // Initial state for explanation animation
     explanationDiv.style.maxHeight = "0";
     explanationDiv.style.overflow = "hidden";
     explanationDiv.style.transition = "max-height 0.5s ease-out";

});
</script>
```