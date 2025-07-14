---
title: "סוד הפלדה הנעלם: מסע אל ליבת חרב דמשקאית"
english_slug: secret-of-lost-steel-journey-into-damascus-sword
category: "טכנולוגיה / הנדסת חומרים"
tags:
  - מטלורגיה
  - פלדה דמשקאית
  - ווטס
  - יצירת חרבות
  - היסטוריה של הטכנולוגיה
---
<h1>סוד הפלדה הנעלם: מסע אל ליבת חרב דמשקאית</h1>
<p class="intro-text">כיצד הצליחו נפחי העבר ליצור פלדה בעלת חוזק וגמישות יוצאי דופן, מעוטרת בדגמים מרהיבים, שסוד יצירתה אבד למאות שנים? אילו תהליכים כימיים ופיזיקליים התרחשו בתוך הכור העתיק כדי להפוך עפרה לפלדה מופלאה?</p>

<div class="app-container">
    <h2>יצירת פלדת ווטס: הסימולציה</h2>

    <div id="stage-intro" class="stage active">
        <p>ברוכים הבאים למסע אל ליבת הפלדה האגדית. נתחיל עם חומרי הגלם הנדירים.</p>
        <div class="ingredients-area">
            <div class="ingredient iron-ore">
                 <div class="icon ore-icon"></div>
                 <span>עפרת ברזל איכותית</span>
            </div>
            <div class="ingredient carbon-source">
                 <div class="icon carbon-icon"></div>
                 <span>פחם עץ וחומרים אורגניים</span>
            </div>
            <div class="ingredient flux">
                <div class="icon flux-icon"></div>
                <span>שטף (לניקוי סיגים)</span>
            </div>
        </div>
        <div class="crucible-area">
             <div class="crucible empty">
                 <div class="crucible-label">כור היתוך</div>
                 <div class="crucible-content"></div>
             </div>
        </div>
        <button id="next-button-1" class="action-button">הכנס מרכיבים לכור היתוך</button>
    </div>

    <div id="stage-crucible" class="stage">
        <p>חומרי הגלם הונחו בזהירות בתוך הכור האטום, מוכנים למסע האש.</p>
        <div class="crucible-area">
            <div class="crucible filled">
                <div class="crucible-label">כור היתוך</div>
                <div class="crucible-content">
                    <div class="ingredient-in-crucible ore-in"></div>
                    <div class="ingredient-in-crucible carbon-in"></div>
                    <div class="ingredient-in-crucible flux-in"></div>
                </div>
            </div>
        </div>
        <button id="next-button-2" class="action-button">התחל תהליך חימום ממושך</button>
    </div>

    <div id="stage-heating" class="stage">
        <p>הכור מחומם לאט ובבקרתיות. הברזל נמס, והפחמן מתחיל להתמוסס לתוכו, יוצר תערובת מותכת.</p>
        <div class="crucible-area">
            <div class="crucible heating">
                <div class="crucible-label">חימום הכור</div>
                <div class="crucible-content heating-animation">
                     <div class="molten-steel-visual"></div>
                </div>
                 <div class="temperature-gauge">
                     <div class="temp-bar"></div>
                 </div>
            </div>
        </div>
         <div class="progress-bar-container">
             <div class="progress-label">תהליך ההיתוך וספיחת הפחמן</div>
             <div id="heating-progress" class="progress-bar"></div>
         </div>
        <button id="next-button-3" class="action-button" disabled>סיים חימום והתחל קירור</button>
    </div>

     <div id="stage-cooling" class="stage">
        <p>שלב קריטי! קירור איטי ומבוקר מאפשר לפחמן ליצור את רשת הקרבידים הייחודית.</p>
         <div class="crucible-area">
            <div class="crucible cooling">
                <div class="crucible-label">קירור איטי</div>
                 <div class="crucible-content cooling-animation">
                      <div class="solidified-ingot-visual">
                           <span>מטיל פלדת ווטס</span>
                           <div class="microstructure-preview">מבנה רצועות</div>
                      </div>
                 </div>
                 <div class="temperature-gauge">
                     <div class="temp-bar cooling-temp"></div>
                 </div>
            </div>
        </div>
         <div class="progress-bar-container">
             <div class="progress-label">תהליך הקירור והתגבשות המבנה</div>
            <div id="cooling-progress" class="progress-bar"></div>
         </div>
        <button id="next-button-4" class="action-button" disabled>הוצא מטיל והתחל חישול</button>
    </div>

     <div id="stage-forging" class="stage">
        <p>חישול אמן בטמפרטורה מדויקת מעצב את הלהב וחושף את הדגם הסודי הטמון בפלדה.</p>
         <div class="forging-area">
             <div class="anvil">
                 <div class="ingot"></div>
             </div>
             <div class="hammer"></div>
         </div>
         <div class="progress-bar-container">
             <div class="progress-label">ריקוע ועיצוב הלהב</div>
            <div id="forging-progress" class="progress-bar"></div>
         </div>
        <button id="next-button-5" class="action-button" disabled>הלהב מוכן! צפה בתוצאה</button>
    </div>

     <div id="stage-result" class="stage">
        <p>מלאכת המחשבת הושלמה. חרב דמשקאית מפוארת עם הדגם המיתולוגי שלה.</p>
         <div class="result-area">
             <img src="https://via.placeholder.com/300x500/4a3c32/f0f0f0?text=חרב+דמשקאית" alt="חרב דמשקאית עם דגם ווטס" class="final-sword">
             <div class="micro-view">
                 <h4>מבט מיקרוסקופי</h4>
                 <img src="https://via.placeholder.com/250x150/6a5a50/ffffff?text=מבנה+רצועות+קרבידים" alt="מבנה מיקרוסקופי של ווטס" class="microstructure-img">
                 <p>רצועות כהות עשירות בקרבידים (סמנטיט) בתוך מטריצה בהירה (פרייט).</p>
             </div>
         </div>
         <button id="reset-button" class="action-button secondary">התחל מסע חדש</button>
    </div>

</div>

<button id="toggle-explanation" class="toggle-button">הצג/הסתר הסבר מורחב על פלדת ווטס</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מורחב על פלדת ווטס וחרבות דמשקאיות</h2>

    <h3>מהי פלדת ווטס (Wootz Steel)?</h3>
    <p>פלדת ווטס היא סוג נדיר והיסטורי של פלדת כור היתוך (crucible steel) שמוצאה מדרום הודו, אלף שנים ויותר לפני זמננו. היא נודעה בתכונותיה העל-טבעיות כמעט: חוזק בלתי רגיל, גמישות מפתיעה ויכולת לשמור על חדות להב יוצאת דופן, כל זאת מעוטר בדגם גלי ומרשים המכונה "דמשקאי" (על שם דמשק, שהייתה מרכז סחר ויצירת חרבות מפורסם מפלדה זו).</p>

    <h3>האלכימיה של ההרכב הכימי</h3>
    <p>סוד ווטס טמון, בין השאר, בהרכב הכימי שלה. היא מכילה ריכוז פחמן גבוה במיוחד (בין 1.5% ל-2%, ולעיתים אף יותר) ביחס לפלדות רוב העידנים. ריכוז פחמן זה, בשילוב עם יסודות קורט מסוימים שמקורם בעפרת הברזל ההודית הייחודית (כמו ונדיום), הוא המפתח ליצירת המבנה הפלאי שלה.</p>

    <h3>מסע האש בכור ההיתוך</h3>
    <p>יצירת מטיל ווטס הייתה תהליך קפדני ומיסטי כמעט, שדרש הבנה עמוקה של החומרים והאש:</p>
    <ul>
        <li><strong>התערובת הקסומה:</strong> שילוב מדויק של עפרת ברזל נקייה במיוחד, פחם עץ איכותי או חומרים אורגניים אחרים (כמו עלים וגבעולים צמחיים עשירים בפחמן), ולעיתים גם "שטף" (כמו זכוכית או סיליקה) שסייע לסלק זיהומים ולקדם את ספיחת הפחמן.</li>
        <li><strong>כור אטום ולב תנור לוהט:</strong> התערובת הונחה בכורי חרס קטנים שנאטמו הרמטית. הכורים חוממו בתנורים מיוחדים לטמפרטורות גבוהות מאוד (לרוב מעל 1200°C) למשך ימים ארוכים. בתנאים אלו, הברזל התכה וספח את הפחמן מהחומר האורגני. האטימה מנעה כניסת חמצן שעלול היה לפגוע בתהליך.</li>
    </ul>

    <h3>סוד ההתגבשות: הקירור האיטי</h3>
    <p>אחד השלבים הקריטיים ביותר, שאבד ושוחזר בקושי רב, היה תהליך הקירור. לאחר ההיתוך, הכורים הוצאו מהתנור וקיררו לאט מאוד, לפעמים על ידי קבורה בחול או אפר. קצב הקירור המבוקר הזה, בטמפרטורות הנכונות, איפשר לפחמן העודף להתפזר ולהתגבש בצורה מיוחדת ביותר.</p>

    <h3>המבנה המיקרוסקופי: רשת הקרבידים</h3>
    <p>הקירור האיטי יוצר בפלדת ווטס מבנה פנימי מדהים: רשת מסועפת של "חוטים" או "רצועות" עשירות בקרבידים קשים (בעיקר סמנטיט, Fe₃C), המוטמעות בתוך מטריצה רכה וגמישה יותר של פלדה דלה בפחמן (פרייט). הקרבידים הם נקודות קשיחות במיוחד, בעוד שהפרייט מעניק לפלדה את גמישותה. שילוב זה הוא מפתח לתכונותיה הייחודיות.</p>

    <h3>מקסם הנפחות: חישול אמן</h3>
    <p>מטיל ווטס, לרוב בצורת "עוגה", עובד לצורת חרב בתהליך חישול ייחודי. החישול בוצע בטמפרטורות נמוכות יחסית (בסביבות 700-900°C) בסדרת חימומים וריקועים עדינים. טווח טמפרטורות זה חיוני כדי למנוע "שבירה" או המסה מחדש של רשת הקרבידים. תהליך הריקוע בפטיש "מותח" ומסדר את רשת הקרבידים בתוך הלהב, וליטוש וחריטה חושפים אותם לפני השטח כדגם גלי ומרשים.</p>

    <h3>הקשר בין מבנה לתכונות: הגאונות ההנדסית הטמונה</h3>
    <p>המבנה המיקרוסקופי של רצועות קרבידים קשים בתוך מטריצה גמישה מספק את השילוב המנצח:</p>
    <ul>
        <li><strong>חוזק וקשיחות:</strong> הקרבידים מספקים עמידות מירבית בפני שחיקה ודפורמציה.</li>
        <li><strong>גמישות וקשיחות לשבר:</strong> המטריצה הרכה יותר עוצרת סדקים ומונעת שבר פתאומי, תכונה נדירה בפלדות קשות.</li>
        <li><strong>חדות קצה יוצאת דופן:</strong> הקרבידים בקצה הלהב מספקים "מיקרו-סרטונים" קשים השומרים על חדות לאורך זמן, כמעט כמו להב משונן טבעי ברמה המיקרוסקופית.</li>
    </ul>

    <h3>אובדן הסוד ושחזורו</h3>
    <p>סוד יצירת ווטס אבד במאות 17-18, כנראה עקב שילוב של גורמים: דעיכת סחר הברזל מהודו, שינויים פוליטיים וחברתיים, ואובדן ידע שעבר בעל פה. שחזור התהליך במאות 20-21 היה אתגר מדעי עצום, שדרש מחקר מטלורגי מעמיק וניסויים רבים כדי להבין את הקשר המורכב בין חומרי גלם, תהליכי חימום וקירור, וטכניקות חישול - למבנה המיקרוסקופי הסופי ולתכונות האגדיות.</p>

    <h3>ווטס עתיקה מול "דמשקאית" מודרנית</h3>
    <p>חשוב להבדיל בין פלדת ווטס ההיסטורית (crucible wootz) לבין "פלדה דמשקאית" מודרנית (pattern welded steel). הדמשקאית המודרנית נוצרת על ידי ריתוך שכבות של פלדות שונות זו על גבי זו. הדגם הוא תוצאה של שכבות מתקפלות והבדלים כימיים ביניהן. בעוד שזוהי אמנות נפחות מרשימה ביותר, המבנה המיקרוסקופי והמנגנונים המעניקים תכונות שונים לחלוטין מאלו של פלדת ווטס האותנטית, בה הדגם נובע מהתגבשות מיוחדת של קרבידים בתוך המטיל עצמו.</p>
</div>

<style>
    /* General Styles */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f2ed; /* Soft background */
        margin: 0;
        padding: 20px;
    }

    h1, h2, h3, h4 {
        color: #3a2e2a; /* Dark brown/steel color */
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2.2em;
        margin-bottom: 20px;
        border-bottom: 2px solid #c2b280; /* Clay color underline */
        padding-bottom: 10px;
        display: inline-block;
        width: 100%;
    }

     .intro-text {
         text-align: center;
         margin-bottom: 30px;
         font-size: 1.1em;
         color: #555;
     }

    .app-container {
        border: 2px solid #c2b280; /* Clay border */
        padding: 25px;
        margin: 20px auto; /* Center container */
        border-radius: 12px; /* More rounded */
        background: linear-gradient(to bottom, #ffffff, #f0f0f0); /* Subtle gradient */
        min-height: 500px; /* Increased height */
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2); /* More prominent shadow */
        max-width: 700px; /* Max width for larger screens */
        width: 100%; /* Ensure it takes full width on smaller screens */
    }

    .app-container h2 {
        font-size: 1.8em;
        margin-top: 0;
        margin-bottom: 25px;
        color: #5a3f3f; /* Darker clay */
    }

    /* Stage Styling and Transitions */
    .stage {
        display: none;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        padding: 25px; /* Match container padding */
        text-align: center;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 25px; /* Increased space */
        background-color: rgba(255,255,255,0.95); /* Slightly transparent white */
        transition: opacity 0.6s ease-in-out; /* Slower transition */
        opacity: 0;
        pointer-events: none;
    }

    .stage.active {
        display: flex;
        opacity: 1;
        pointer-events: auto;
    }

    /* Common Area Styles */
    .ingredients-area, .crucible-area, .forging-area, .result-area {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 30px; /* More space */
        flex-wrap: wrap;
        margin-bottom: 30px; /* More space before button/progress */
        width: 100%; /* Take full width */
    }

    /* Ingredient Styles */
    .ingredient {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 15px 20px; /* Larger padding */
        border: 1px solid #b8a79d; /* Softer border */
        border-radius: 8px; /* More rounded */
        background-color: #edece8; /* Light background */
        font-size: 1em; /* Slightly larger font */
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        min-width: 120px; /* Ensure minimum width */
        text-align: center;
    }

    .ingredient span {
        margin-top: 8px;
        color: #444;
    }

    /* Icons */
    .icon {
         width: 40px;
         height: 40px;
         background-size: cover;
         background-position: center;
         border-radius: 50%;
         border: 2px solid rgba(255,255,255,0.8);
         box-shadow: inset 0 0 5px rgba(0,0,0,0.3);
    }

    .ore-icon { background-color: #a0522d; background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="white" d="M12 2a10 10 0 0 0-9.95 9.05l-1.05.21a12 12 0 0 1 23.99 0l-1.05-.21A10 10 0 0 0 12 2m-1 4h2v5h-2V6m0 6h2v6h-2v-6"/></svg>'); } /* Simplified ore icon */
    .carbon-icon { background-color: #444; background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="white" d="M12 2a10 10 0 0 0-10 10c0 5.52 4.48 10 10 10s10-4.48 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8 8 8 0 0 1-8-8 8 8 0 0 1 8-8"/></svg>'); } /* Simplified carbon icon */
    .flux-icon { background-color: #add8e6; background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="#444" d="M12 2c-.58 0-1.1.27-1.4.69L3.42 14.75c-.37.5-.31 1.17.15 1.63a1.18 1.18 0 0 0 .87.36H19.56c.42 0 .8-.18 1.06-.51.26-.33.35-.77.25-1.2l-7.17-12c-.29-.47-.8-.73-1.35-.73m0 2a.74.74 0 0 1 .67.38l7.17 12a.33.33 0 0 1-.08.4c-.07.09-.18.13-.3.13h-16.1a.35.35 0 0 1-.3-.13c-.07-.09-.1-.2-.06-.31l7.17-12c.13-.22.36-.38.6-.38m0 3a2 2 0 0 0-2 2v4c0 1.1.9 2 2 2s2-.9 2-2V9a2 2 0 0 0-2-2m0 2a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5.5.5 0 0 1-.5-.5v-4a.5.5 0 0 1 .5-.5"/></svg>'); } /* Simplified crystal/glass icon */

    /* Crucible Styles */
    .crucible-area {
        position: relative; /* For placing crucible */
        width: 100%;
        min-height: 250px; /* Space for crucible */
    }

    .crucible {
        width: 180px; /* Larger */
        height: 250px; /* Taller */
        border: 3px solid #5a3f3f; /* Darker clay */
        border-bottom-left-radius: 90px; /* More rounded base */
        border-bottom-right-radius: 90px;
        background-color: #d4c0a8; /* Lighter clay color */
        position: absolute; /* Position within area */
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        overflow: hidden;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.4); /* More pronounced shadow */
        transition: transform 0.5s ease-in-out; /* Smooth movement */
    }

     .crucible-label {
         position: absolute;
         top: 15px;
         left: 0;
         right: 0;
         text-align: center;
         font-size: 1em;
         color: #3a2e2a;
         font-weight: bold;
     }

    .crucible.empty .crucible-content {
         position: absolute;
         top: 50%;
         left: 50%;
         transform: translate(-50%, -50%);
         font-size: 1.1em;
         color: #5a3f3f;
         font-weight: bold;
    }
    .crucible.empty .crucible-content::before {
         content: "ריק";
    }


    .crucible.filled .crucible-content {
        height: 70%;
        background-color: #6b4f4f; /* Represents the mix */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 5px;
        padding-bottom: 15px; /* More space from bottom */
        font-size: 0.8em;
        color: white;
        transition: height 0.5s ease-in-out;
    }

    .ingredient-in-crucible {
         width: 40px;
         height: 20px;
         border-radius: 5px;
         opacity: 0.8;
         box-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    }
     .ore-in { background-color: #a0522d; }
     .carbon-in { background-color: #444; }
     .flux-in { background-color: #add8e6; }


    .crucible.heating .crucible-content {
        height: 85%; /* Fill more for liquid */
        background: radial-gradient(circle at bottom center, #ff4500 0%, #ffa500 40%, #ffd700 80%, rgba(255,215,0,0) 100%); /* More dynamic gradient */
        animation: heat-pulse 1.5s infinite alternate ease-in-out, heat-shimmer 2s infinite linear; /* Enhanced animation */
         display: flex;
         align-items: center;
         justify-content: center;
         color: white;
         font-size: 1.2em;
         font-weight: bold;
         text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
         position: relative; /* For liquid movement */
         overflow: hidden;
    }

    .molten-steel-visual {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="10" fill="rgba(255,255,255,0.3)"/><circle cx="80" cy="40" r="12" fill="rgba(255,255,255,0.4)"/><circle cx="40" cy="80" r="8" fill="rgba(255,255,255,0.2)"/></svg>') repeat; /* Simple bubbly pattern */
        background-size: 20px 20px;
        animation: liquid-flow 5s infinite linear; /* Animation for liquid movement */
    }

     .temperature-gauge {
         position: absolute;
         top: 10%;
         right: 10%;
         width: 20px;
         height: 70%;
         border: 1px solid #333;
         border-radius: 10px;
         overflow: hidden;
         background-color: #eee;
     }
    .temp-bar {
        width: 100%;
        height: 0%; /* Start empty */
        background: linear-gradient(to top, #4CAF50, #ff4500); /* Green to red */
        position: absolute;
        bottom: 0;
        left: 0;
        transition: height 0.5s ease-in-out;
    }
     .cooling-temp {
         height: 100%; /* Start full for cooling */
         background: linear-gradient(to bottom, #4682b4, #4CAF50); /* Blue to green */
         transition: height 6s linear; /* Slower transition for cooling */
     }


     @keyframes heat-pulse {
        from { transform: scale(1); opacity: 0.9; }
        to { transform: scale(1.01); opacity: 1; }
    }
     @keyframes heat-shimmer {
         from { background-position: 0 0; }
         to { background-position: 100px 100px; }
     }
     @keyframes liquid-flow {
         from { background-position: 0 0; }
         to { background-position: 200px 200px; }
     }


     .crucible.cooling .crucible-content {
         height: 85%; /* Match heating start */
         background: linear-gradient(to bottom, #888, #bbb, #eee); /* Gray to lighter gray */
         transition: background 6s ease-in-out; /* Animate background change over cooling time */
         display: flex;
         flex-direction: column;
         align-items: center;
         justify-content: center;
          color: #333;
          font-size: 1em;
          font-weight: bold;
          position: relative;
     }

      .solidified-ingot-visual {
         width: 150px; /* Size matching solidified ingredient */
         height: 100px;
         background-color: #777;
         border: 2px solid #5a3f3f;
         box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
         display: flex;
         flex-direction: column;
         align-items: center;
         justify-content: center;
         gap: 10px;
         color: white;
         font-size: 0.9em;
         font-weight: bold;
         position: absolute; /* Position over cooling content */
         bottom: 15%; /* Adjust position */
         left: 50%;
         transform: translateX(-50%);
         opacity: 0; /* Start hidden */
         animation: solidify 1s forwards 5s; /* Appear after cooling */
      }

     @keyframes solidify {
         to { opacity: 1; }
     }


     .microstructure-preview {
         width: 120px; /* Increased size */
         height: 70px;
         background-image: repeating-linear-gradient(45deg, #bbb 0px, #bbb 8px, #444 8px, #444 16px); /* More visible bands */
         background-size: 16px 16px;
         border: 1px solid #333;
         margin-top: 10px; /* Space below text */
         font-size: 0.7em;
         color: #eee;
         display: flex;
         align-items: center;
         justify-content: center;
         text-shadow: 1px 1px 1px rgba(0,0,0,0.5);
          opacity: 0; /* Start hidden */
          animation: show-structure 1.5s forwards 6s; /* Appear after solidification/cooling */
     }

     @keyframes show-structure {
         to { opacity: 1; }
     }


    /* Forging Styles */
    .forging-area {
        display: flex;
        justify-content: center;
        align-items: flex-end; /* Align to bottom of anvil */
        position: relative;
        width: 100%;
        min-height: 250px; /* Space for forging */
    }

     .anvil {
         width: 250px;
         height: 150px;
         background-color: #333;
         border-radius: 10px 10px 50px 50px; /* Rounded base */
         position: relative;
         display: flex;
         justify-content: center;
         align-items: flex-start; /* Align ingot to top */
         padding-top: 20px;
         box-shadow: 5px 5px 10px rgba(0,0,0,0.5);
     }

    .ingot {
        width: 180px; /* Size relative to anvil */
        height: 50px;
        background-color: #777;
        border: 1px solid #333;
         box-shadow: inset 0 0 5px rgba(0,0,0,0.5);
         position: absolute;
         top: 10px; /* Position on anvil */
         left: 50%;
         transform: translateX(-50%);
         transition: transform 0.1s ease-in-out; /* For slight squash/stretch */
    }

    .hammer {
         width: 80px; /* Larger hammer */
         height: 80px;
         background-color: #555;
         border-radius: 15px;
         position: absolute;
         top: -40px; /* Position above anvil */
         left: 50%;
         transform: translateX(-50%) rotate(-30deg); /* Start angle */
         animation: hammer-strike 0.8s infinite alternate ease-in-out;
          transform-origin: bottom center; /* Rotate from the bottom */
         box-shadow: 3px 3px 8px rgba(0,0,0,0.4);
    }

     @keyframes hammer-strike {
         0% { transform: translateX(-50%) rotate(-30deg); } /* Angle up */
         50% { transform: translateX(-50%) rotate(5deg) translateY(5px); } /* Move down slightly past horizontal */
         100% { transform: translateX(-50%) rotate(-30deg); } /* Return up */
     }

     /* Result Styles */
    .result-area {
        flex-direction: row; /* Side by side layout */
        gap: 40px; /* More space */
        align-items: flex-start; /* Align tops */
        flex-wrap: wrap; /* Wrap on small screens */
        justify-content: center; /* Center when wrapped */
    }

    .final-sword {
        max-width: 300px; /* Larger sword */
        height: auto;
        border: 2px solid #888;
        box-shadow: 8px 8px 15px rgba(0,0,0,0.4);
        content: url('https://via.placeholder.com/300x500/4a3c32/f0f0f0?text=חרב+דמשקאית'); /* Placeholder image */
        border-radius: 5px;
        transition: transform 0.5s ease-out;
    }
     .final-sword:hover {
         transform: translateY(-5px);
     }


    .micro-view {
        border: 1px solid #888;
        padding: 20px; /* More padding */
        background-color: #f8f8f8;
        text-align: center;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.3);
        border-radius: 8px;
    }
     .micro-view h4 {
         margin-top: 0;
         margin-bottom: 10px; /* More space below heading */
         color: #555;
         font-size: 1.1em;
     }

    .microstructure-img {
         max-width: 250px; /* Larger microstructure image */
         height: auto;
          content: url('https://via.placeholder.com/250x150/6a5a50/ffffff?text=מבנה+רצועות+קרבידים'); /* Placeholder image */
          border: 1px solid #555;
          border-radius: 4px;
    }
     .micro-view p {
         margin-top: 10px;
         font-size: 0.9em;
         color: #666;
         max-width: 250px; /* Control width */
         margin-left: auto;
         margin-right: auto;
     }


    /* Progress Bar Styling */
    .progress-bar-container {
        width: 90%; /* Wider */
        max-width: 500px; /* Increased max width */
        height: 25px; /* Taller */
        border: 1px solid #5a3f3f;
        border-radius: 12px;
        overflow: hidden;
        margin: 25px auto;
        background-color: #eee;
        box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
        position: relative;
    }

     .progress-label {
         position: absolute;
         top: -25px;
         left: 0;
         right: 0;
         text-align: center;
         font-size: 0.9em;
         color: #3a2e2a;
         font-weight: bold;
     }

    .progress-bar {
        width: 0%;
        height: 100%;
        background-color: #4CAF50; /* Green default */
        transition: width 0.5s ease-in-out; /* Keep smooth transition */
        background: linear-gradient(45deg, #4CAF50, #8bc34a); /* Gradient */
        position: relative;
        overflow: hidden;
    }

    .progress-bar::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: repeating-linear-gradient(45deg, rgba(255,255,255,0.2) 0px, rgba(255,255,255,0.2) 10px, rgba(255,255,255,0) 10px, rgba(255,255,255,0) 20px);
        animation: progress-stripes 1s linear infinite;
    }
     @keyframes progress-stripes {
         from { background-position: 0 0; }
         to { background-position: 20px 20px; }
     }


     #heating-progress { background: linear-gradient(45deg, #ff6347, #ffb5a0); } /* Tomato gradient */
     #cooling-progress { background: linear-gradient(45deg, #4682b4, #87cefa); } /* Steelblue gradient */
     #forging-progress { background: linear-gradient(45deg, #a0522d, #d2b48c); } /* Sienna gradient */


    /* Button Styling */
    button {
        padding: 14px 30px; /* Larger buttons */
        font-size: 1.2em; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 8px; /* More rounded */
        background: linear-gradient(to bottom, #007bff, #0056b3); /* Gradient */
        color: white;
        transition: all 0.3s ease; /* Smooth transitions for all changes */
        margin-top: 20px; /* More space */
        box-shadow: 3px 3px 8px rgba(0,0,0,0.3); /* More prominent shadow */
        font-weight: bold;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    button.secondary {
         background: linear-gradient(to bottom, #6c757d, #545b62);
         box-shadow: 3px 3px 8px rgba(0,0,0,0.2);
    }
     button.secondary:hover:not(:disabled) {
         background: linear-gradient(to bottom, #545b62, #343a40);
     }
     button.toggle-button {
          background: linear-gradient(to bottom, #28a745, #218838);
          margin: 40px auto 20px; /* More space around toggle */
          display: block; /* Make it a block element */
          font-size: 1.1em;
          box-shadow: 3px 3px 8px rgba(0,0,0,0.2);
     }
     button.toggle-button:hover:not(:disabled) {
         background: linear-gradient(to bottom, #218838, #1e7e34);
     }


    button:hover:not(:disabled) {
        background: linear-gradient(to bottom, #0056b3, #003f7f); /* Darker gradient on hover */
         transform: translateY(-2px); /* Lift effect */
         box-shadow: 5px 5px 10px rgba(0,0,0,0.4);
    }

     button:active:not(:disabled) {
         transform: translateY(1px); /* Press effect */
         box-shadow: 1px 1px 3px rgba(0,0,0,0.4);
     }


    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
        opacity: 0.7;
     }

    /* Explanation Section */
    #explanation {
        border-top: 2px solid #c2b280;
        margin-top: 40px; /* More space */
        padding-top: 30px; /* More padding */
        background-color: #fefefe;
        padding: 25px;
        border-radius: 12px;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.1);
        line-height: 1.7; /* More comfortable reading */
    }

    #explanation h2, #explanation h3 {
        color: #3a2e2a;
        border-bottom: 1px dashed #ddd; /* Lighter dashed border */
        padding-bottom: 8px;
        margin-top: 25px; /* More space above headings */
    }
     #explanation h2 { margin-top: 0; }


    #explanation ul {
        list-style-type: square; /* Different bullet */
        margin-left: 35px; /* More indent */
        padding-left: 0;
         margin-bottom: 15px;
    }

    #explanation li {
        margin-bottom: 10px; /* More space between list items */
        line-height: 1.6;
        color: #555;
    }

     #explanation p {
         margin-bottom: 15px; /* Space between paragraphs */
         color: #555;
     }

</style>

<script>
    const stages = [
        'stage-intro',
        'stage-crucible',
        'stage-heating',
        'stage-cooling',
        'stage-forging',
        'stage-result'
    ];
    let currentStageIndex = 0;
    let simulationTimer = null; // Variable to hold the interval timer
    let temperatureTimer = null; // Variable to hold temperature timer

    const nextButton1 = document.getElementById('next-button-1');
    const nextButton2 = document.getElementById('next-button-2');
    const nextButton3 = document.getElementById('next-button-3');
    const nextButton4 = document.getElementById('next-button-4');
    const nextButton5 = document.getElementById('next-button-5');
    const resetButton = document.getElementById('reset-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    const heatingProgressBar = document.getElementById('heating-progress');
    const coolingProgressBar = document.getElementById('cooling-progress');
    const forgingProgressBar = document.getElementById('forging-progress');

    const tempBarHeating = document.querySelector('#stage-heating .temp-bar');
    const tempBarCooling = document.querySelector('#stage-cooling .temp-bar');
    const ingotVisual = document.querySelector('#stage-forging .ingot');


    function showStage(index) {
        stages.forEach((stageId, i) => {
            const stageElement = document.getElementById(stageId);
            if (i === index) {
                stageElement.classList.add('active');
            } else {
                stageElement.classList.remove('active');
            }
        });
        currentStageIndex = index;
    }

    function simulateProcess(progressBar, duration, nextButton, onComplete = null) {
        clearInterval(simulationTimer); // Clear any existing timer
        progressBar.style.width = '0%';
        nextButton.disabled = true;
        let width = 0;
        const interval = 50; // Update every 50ms
        const totalSteps = duration / interval;
        const increment = 100 / totalSteps; // Percentage to increment per step

        simulationTimer = setInterval(() => {
            if (width >= 100) {
                clearInterval(simulationTimer);
                simulationTimer = null;
                progressBar.style.width = '100%'; // Ensure it reaches 100%
                nextButton.disabled = false;
                if (onComplete) {
                    onComplete();
                }
            } else {
                width += increment;
                progressBar.style.width = width + '%';
            }
        }, interval);
    }

     function animateTemperature(tempBarElement, startHeight, endHeight, duration) {
         clearInterval(temperatureTimer);
         let currentHeight = startHeight;
         const interval = 50;
         const totalSteps = duration / interval;
         const increment = (endHeight - startHeight) / totalSteps;

         tempBarElement.style.height = startHeight + '%';

         temperatureTimer = setInterval(() => {
             if ((increment > 0 && currentHeight >= endHeight) || (increment < 0 && currentHeight <= endHeight)) {
                 clearInterval(temperatureTimer);
                 temperatureTimer = null;
                 tempBarElement.style.height = endHeight + '%';
             } else {
                 currentHeight += increment;
                 tempBarElement.style.height = currentHeight + '%';
             }
         }, interval);
     }


    nextButton1.addEventListener('click', () => {
        showStage(1);
    });

    nextButton2.addEventListener('click', () => {
        showStage(2);
        // Simulate heating for 5 seconds (5000ms)
        simulateProcess(heatingProgressBar, 5000, nextButton3);
        // Animate temperature bar up
        animateTemperature(tempBarHeating, 0, 100, 4500); // Finish temp animation slightly before process
    });

    nextButton3.addEventListener('click', () => {
        showStage(3);
        // Simulate cooling for 6 seconds (6000ms)
        simulateProcess(coolingProgressBar, 6000, nextButton4);
        // Animate temperature bar down
         animateTemperature(tempBarCooling, 100, 0, 5500); // Finish temp animation slightly before process
    });

    nextButton4.addEventListener('click', () => {
        showStage(4);
         // Simulate forging for 5 seconds (5000ms)
         simulateProcess(forgingProgressBar, 5000, nextButton5, () => {
             // Stop hammer animation on completion
             document.querySelector('#stage-forging .hammer').style.animation = 'none';
              // Optional: Add final strike visual
              ingotVisual.style.transform = 'translateX(-50%) scaleY(0.95)';
              setTimeout(() => { ingotVisual.style.transform = 'translateX(-50%) scaleY(1)'; }, 100);
         });
         // Start hammer animation
         document.querySelector('#stage-forging .hammer').style.animation = 'hammer-strike 0.8s infinite alternate ease-in-out';
          // Add slight ingot squash/stretch on hammer strike (needs more complex JS or synchronized CSS animation) - Basic version for now:
           // This requires tracking the animation time, maybe skip for now or do a simpler visual cue
    });

    nextButton5.addEventListener('click', () => {
        showStage(5);
         clearInterval(simulationTimer);
         simulationTimer = null;
         clearInterval(temperatureTimer);
         temperatureTimer = null;
         // Ensure hammer animation is stopped
         document.querySelector('#stage-forging .hammer').style.animation = 'none';
    });

    resetButton.addEventListener('click', () => {
        clearInterval(simulationTimer);
        simulationTimer = null;
        clearInterval(temperatureTimer);
        temperatureTimer = null;

        // Reset visuals
        heatingProgressBar.style.width = '0%';
        coolingProgressBar.style.width = '0%';
        forgingProgressBar.style.width = '0%';
        if (tempBarHeating) tempBarHeating.style.height = '0%';
        if (tempBarCooling) tempBarCooling.style.height = '100%'; // Start cooling temp at max
        if (ingotVisual) ingotVisual.style.transform = 'translateX(-50%) scaleY(1)';
         // Ensure hammer animation is stopped
         document.querySelector('#stage-forging .hammer').style.animation = 'none';

        // Reset button states
        nextButton3.disabled = true;
        nextButton4.disabled = true;
        nextButton5.disabled = true;


        showStage(0); // Start with the intro stage
    });


    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר מורחב';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג/הסתר הסבר מורחב על פלדת ווטס';
        }
    });

    // Initial setup
    showStage(0); // Start with the intro stage

</script>
```