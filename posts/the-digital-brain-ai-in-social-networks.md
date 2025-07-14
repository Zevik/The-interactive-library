---
title: "המוח הדיגיטלי: AI ברשתות חברתיות"
english_slug: the-digital-brain-ai-in-social-networks
category: "טכנולוגיה / מדעי המחשב"
tags:
  - בינה מלאכותית
  - רשתות חברתיות
  - אלגוריתמים
  - למידת מכונה
  - ניתוח נתונים
---

# המוח הדיגיטלי: AI ברשתות חברתיות

האם אי פעם עצרתם לחשוב למה הפיד שלכם נראה בדיוק כפי שהוא? למה דווקא התוכן הזה קופץ לכם מול העיניים, ולמה פוסט מסוים נהפך לוויראלי בטירוף, בעוד אחר נבלע בתהום הנשייה? מאחורי הקלעים, מנועים בלתי נראים - מוחות דיגיטליים מבוססי בינה מלאכותית - פועלים ללא הרף, מנתחים מידע, מזהים דפוסים ומקבלים החלטות בזק כדי לעצב את החוויה הדיגיטלית שלכם. בואו נצלול פנימה ונראה איך זה עובד!

<div id="social-sim-app">
  <h2>המעבדה הדיגיטלית: בחן את אלגוריתם ה-AI</h2>
  <p>בחר באחד התכנים הבאים וצפה כיצד המוח הדיגיטלי של הרשת החברתית מנתח אותו ומעריך את פוטנציאל ההצלחה שלו:</p>

  <div id="content-selection">
    <button class="content-option" data-content-id="cat-video">
      <img src="https://via.placeholder.com/120x80/a8dadc/1d3557?text=סרטון+חתולים" alt="אייקון: סרטון חתולים מצחיקים">
      <span>סרטון מצחיק<br>של חתולים</span>
    </button>
    <button class="content-option" data-content-id="ai-ethics">
      <img src="https://via.placeholder.com/120x80/457b9d/1d3557?text=דו%22ח+AI" alt="אייקון: דו"ח על אתיקה ב-AI">
      <span>מאמר מעמיק<br>על אתיקה ב-AI</span>
    </button>
    <button class="content-option" data-content-id="sunset-photo">
      <img src="https://via.placeholder.com/120x80/e63946/1d3557?text=שקיעת+ים" alt="אייקון: תמונת שקיעה">
      <span>תמונת שקיעה<br>אמנותית</span>
     </button>
     <button class="content-option" data-content-id="soup-recipe">
      <img src="https://via.placeholder.com/120x80/f1faee/1d3557?text=מרק+עדשים" alt="אייקון: קערת מרק">
      <span>מתכון קל ומהיר<br>למרק עדשים</span>
    </button>
  </div>

  <div id="ai-analysis-section" class="analysis-process" style="display: none;">
    <h3>תהליך ניתוח ה-AI בעיצומן:</h3>
    <div id="analysis-steps">
      <div class="analysis-step">
        <span class="step-icon">🔬</span>
        <p class="step-title">שלב 1: סריקה וניתוח תוכן</p>
        <div id="step-analysis" class="analysis-step-output loading"></div>
      </div>
      <div class="analysis-step">
        <span class="step-icon">📊</span>
        <p class="step-title">שלב 2: הערכת פוטנציאל מעורבות</p>
        <div id="step-prediction" class="analysis-step-output loading"></div>
      </div>
      <div class="analysis-step">
        <span class="step-icon">📈</span>
        <p class="step-title">שלב 3: זיהוי קשר לטרנדים</p>
        <div id="step-trends" class="analysis-step-output loading"></div>
      </div>
    </div>

    <div id="ai-feedback-results" style="opacity: 0;">
      <h3>תוצאות ומשוב מהמוח הדיגיטלי:</h3>
      <div id="engagement-score-container">
          <div id="engagement-score-bar-container">
              <div id="engagement-score-bar"><span id="score-text">0%</span></div>
          </div>
          <p>ציון פוטנציאל מעורבות (מתוך 100): <span id="engagement-score-value">0</span></p>
      </div>
      <p id="feedback-text"></p>
    </div>
     <button id="reset-sim">בחירת תוכן חדש לניתוח</button>
  </div>
</div>

<style>
  #social-sim-app {
    font-family: 'Heebo', sans-serif; /* Changed font to Heebo or similar clean font */
    direction: rtl;
    text-align: right;
    background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%); /* Subtle gradient background */
    padding: 30px;
    border-radius: 12px; /* More rounded corners */
    margin-bottom: 40px;
    border: 1px solid #80deea; /* Matching border color */
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Softer shadow */
    overflow: hidden; /* Prevent overflow issues */
  }

  h2 {
    color: #00796b; /* Dark teal */
    text-align: center;
    margin-bottom: 20px;
    font-size: 1.8em;
  }

  p {
    color: #333;
    line-height: 1.7;
    margin-bottom: 15px;
  }

  #content-selection {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px; /* Increased gap */
    margin-bottom: 30px;
  }

  .content-option {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #fff;
    border: 2px solid #e0e0e0;
    border-radius: 10px; /* More rounded */
    padding: 15px; /* Increased padding */
    cursor: pointer;
    transition: all 0.3s ease-in-out; /* Slower, smoother transition */
    width: 160px; /* Slightly wider buttons */
    text-align: center;
    font-size: 1em; /* Standard font size */
    color: #555;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
  }

  .content-option:hover {
    border-color: #00796b; /* Highlight color */
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15); /* More prominent shadow on hover */
    transform: translateY(-5px); /* Slight lift effect */
  }

   .content-option.selected {
      border-color: #00796b;
      background-color: #e0f2f7; /* Light blue background for selected */
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
   }


  .content-option img {
      border-radius: 8px; /* Rounded image corners */
      margin-bottom: 10px; /* More space below image */
      border: 1px solid #eee;
      width: 100%; /* Make image responsive within button */
      height: auto;
  }

   .content-option span {
       max-width: 100%;
       word-wrap: break-word;
       font-weight: bold;
       color: #004d40; /* Darker teal for text */
   }

  #ai-analysis-section {
    margin-top: 20px;
    border-top: 1px solid #b2ebf2; /* Matching border */
    padding-top: 30px; /* Increased padding */
  }

  .analysis-step {
    display: flex;
    align-items: flex-start; /* Align icon and text at top */
    margin-bottom: 20px; /* Space between steps */
    opacity: 0; /* Start hidden for animation */
    transform: translateY(20px); /* Start below final position */
    transition: opacity 0.5s ease-out, transform 0.5s ease-out;
  }

   .analysis-step.visible {
      opacity: 1;
      transform: translateY(0);
   }

  .step-icon {
    font-size: 2em; /* Larger icon */
    margin-left: 15px; /* Space between icon and text */
    color: #00796b; /* Icon color */
  }

  .step-title {
    font-weight: bold;
    margin: 0 0 8px 0; /* Adjust margin */
    color: #004d40; /* Dark teal */
    font-size: 1.1em;
  }

  .analysis-step-output {
    flex-grow: 1; /* Take remaining space */
    min-height: 50px; /* Larger space for content */
    background-color: #f5f5f5; /* Light gray background */
    padding: 15px; /* Increased padding */
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    color: #333;
    font-size: 0.95em;
    line-height: 1.6;
    position: relative; /* Needed for loader */
    overflow: hidden; /* Hide loader overflow */
  }

   .analysis-step-output.loading::after {
        content: '';
        position: absolute;
        bottom: 0;
        right: 0; /* Start from right for RTL */
        width: 100%;
        height: 5px; /* Loader bar height */
        background: linear-gradient(90deg, transparent, #00796b, transparent); /* Loader color */
        animation: loading-bar 1.5s infinite linear;
        transform-origin: right; /* Animate from right */
    }

    @keyframes loading-bar {
        0% { transform: translateX(100%); }
        50% { transform: translateX(0); }
        100% { transform: translateX(-100%); }
    }


  #ai-feedback-results {
    margin-top: 30px;
    padding: 20px;
    background-color: #e0f2f7; /* Light blue background */
    border-radius: 8px;
    border: 1px solid #b2ebf2;
    transition: opacity 1s ease-out; /* Fade in effect */
  }

  #ai-feedback-results h3 {
    color: #004d40; /* Dark teal */
    margin-top: 0;
    margin-bottom: 15px;
    text-align: center;
    font-size: 1.5em;
  }

  #engagement-score-container {
    text-align: center;
    margin-bottom: 20px;
  }

  #engagement-score-bar-container {
    width: 80%; /* Wider container */
    max-width: 400px; /* Max width */
    background-color: #e0e0e0;
    border-radius: 25px; /* Fully rounded */
    overflow: hidden;
    margin: 10px auto; /* Center the bar */
    height: 30px; /* Taller bar */
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.2); /* Inner shadow */
  }

  #engagement-score-bar {
    height: 100%;
    width: 0; /* Initial width */
    background: linear-gradient(90deg, #4caf50, #8bc34a); /* Green gradient */
    text-align: center;
    line-height: 30px; /* Vertically center text */
    color: white;
    font-weight: bold;
    transition: width 1.5s ease-out; /* Smoother animation */
    direction: ltr; /* Ensure bar grows left-to-right visually */
    display: flex; /* Use flex for centering text */
    align-items: center;
    justify-content: center;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.3); /* Text shadow */
  }

   #score-text {
       opacity: 0; /* Hide text initially */
       transition: opacity 0.5s ease 1.5s; /* Fade in after animation */
   }

  #engagement-score-value {
      font-weight: bold;
      color: #00796b; /* Highlight color */
      font-size: 1.2em;
  }

  #feedback-text {
    font-style: italic;
    color: #555;
    margin-top: 15px;
    text-align: center;
    font-size: 1.1em;
  }

   #reset-sim {
       display: block;
       margin: 30px auto 0; /* Centered with more space */
       padding: 12px 25px; /* Larger padding */
       background-color: #00796b; /* Dark teal */
       color: white;
       border: none;
       border-radius: 25px; /* Pill shape */
       cursor: pointer;
       font-size: 1.1em;
       transition: background-color 0.3s ease, transform 0.1s ease;
       box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
   }
    #reset-sim:hover {
        background-color: #004d40; /* Darker teal */
        transform: translateY(-2px);
    }
     #reset-sim:active {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
     }


  #show-explanation {
    display: block;
    margin: 30px auto;
    padding: 12px 25px;
    background-color: #607d8b; /* Blue gray */
    color: white;
    border: none;
    border-radius: 25px; /* Pill shape */
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  #show-explanation:hover {
    background-color: #455a64; /* Darker blue gray */
    transform: translateY(-2px);
  }
   #show-explanation:active {
       transform: translateY(0);
       box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
   }


  #explanation-section {
    margin-top: 40px;
    padding: 30px;
    background-color: #f1faee; /* Light pale green */
    border-radius: 12px;
    border: 1px solid #a8dadc; /* Matching border */
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    opacity: 0; /* Initially hidden for animation */
    transform: translateY(20px);
    transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    display: none; /* Initially hidden */
  }

  #explanation-section.visible {
     display: block; /* Show before animating */
     opacity: 1;
     transform: translateY(0);
  }

  #explanation-section h2 {
     color: #1d3557; /* Dark blue */
     margin-top: 0;
     margin-bottom: 20px;
     text-align: right;
  }

  #explanation-section h3 {
    color: #457b9d; /* Steel blue */
    margin-top: 25px;
    margin-bottom: 10px;
    font-size: 1.3em;
  }

  #explanation-section p {
    line-height: 1.7;
    margin-bottom: 15px;
    color: #333;
  }

  #explanation-section ul {
      margin-bottom: 15px;
      padding-right: 20px; /* Adjust padding for RTL list */
  }

  #explanation-section li {
      margin-bottom: 8px;
      line-height: 1.6;
      color: #333;
  }
   /* Bar color variations */
   #engagement-score-bar.high {
       background: linear-gradient(90deg, #28a745, #218838);
   }
   #engagement-score-bar.medium-high {
       background: linear-gradient(90deg, #ffc107, #e0a800);
   }
   #engagement-score-bar.medium {
       background: linear-gradient(90deg, #fd7e14, #e06200);
   }
    #engagement-score-bar.low {
       background: linear-gradient(90deg, #dc3545, #c82333);
   }


</style>

<button id="show-explanation">פענוח האלגוריתם: הסבר מעמיק</button>

<div id="explanation-section">
  <h2>האלגוריתם במבט מקרוב: מאחורי הקלעים של הפיד</h2>

  <h3>מהו תפקיד ה-AI ברשתות חברתיות?</h3>
  <p>תחשבו על הרשת החברתית כעל עיר ענקית, והתוכן כעל כל הדברים שקורים בה. תפקיד ה-AI הוא כמו "מדריך טיולים" אישי שלכם, שמחליט מה להראות לכם כדי שתיהנו הכי הרבה (ותישארו בעיר). הוא אחראי לדירוג התכנים בפיד, המלצה על חברים, קבוצות, או אפילו מוצרים שתאהבו. אבל לא רק - הוא גם שוטר ופקח תנועה, מזהה תוכן פוגעני, ספאם או חשבונות מזויפים כדי לשמור על הסדר.</p>

  <h3>כיצד ה-AI מבין על מה התוכן בכלל?</h3>
  <p>כדי שה-AI יוכל להחליט מה להראות לכם, הוא חייב קודם "להבין" את התוכן שמישהו פרסם. זה קורה באמצעות טכנולוגיות מתוחכמות:</p>
  <ul>
    <li>**טקסט (פוסטים, תגובות):** ניתוח שפה טבעית (NLP) קורא את המילים, מזהה נושאים, מילות מפתח, ואפילו את "מצב הרוח" של הטקסט (סנטימנט - האם הוא שמח, כועס, רגוע?). הוא יודע לזהות אם מדברים על "בחירות", "חתולים" או "מתכונים".</li>
    <li>**תמונות:** ראייה ממוחשבת (Computer Vision) מאפשרת ל-AI "לראות" מה יש בתמונה. חתולים? אוכל? חוף ים? אנשים? פעילויות? הוא סורק את הפיקסלים ומבין את האובייקטים והסצנה.</li>
    <li>**וידאו:** זה השלב המורכב ביותר! ה-AI משלב ניתוח ויזואלי (תמונה-אחר-תמונה), ניתוח קול (מה נאמר? איזו מוזיקה מתנגנת?) וניתוח תנועה כדי להבין את העלילה או המסר של הסרטון.</li>
  </ul>
  הניתוח הזה מספק ל-AI תובנות עמוקות על "מה באמת קורה" בתוך התוכן.

  <h3>מודלים לחיזוי הצלחה: ממה מורכב "ציון המעורבות"?</h3>
  <p>אחרי שה-AI הבין את התוכן, הוא מנסה לנבא כמה הוא יעניין דווקא *אתכם* (או משתמשים דומים). זהו שלב קריטי בדירוג. המודלים לוקחים בחשבון קוקטייל של גורמים:</p>
  <ul>
    <li>**מאפייני התוכן:** האם זה וידאו קצר וקליט או מאמר ארוך? האם הסנטימנט חיובי ומעורר? אילו נושאים הוא עוסק?</li>
    <li>**היסטוריית האינטראקציות שלכם:** מה אהבתם בעבר? על מה הגבתם? אילו סרטונים ראיתם עד הסוף? עם מי התקשרתם הכי הרבה? ה-AI לומד את טעמכם האישי.</li>
    <li>**מאפייני המפרסם:** האם זה חבר קרוב שלכם? האם זה דף שאתם עוקבים אחריו ומגיבים לו תדיר? האם התוכן של המפרסם הזה זוכה בדרך כלל להצלחה?</li>
    <li>**הצלחת תוכן דומה:** אם מיליון אנשים כמוכם אהבו סרטוני חתולים דומים, יש סיכוי גבוה שגם אתם תאהבו.</li>
    <li>**ביצועים ראשוניים (זמן אמת):** האם הפוסט כבר צובר לייקים ותגובות מהירות מרגע פרסומו? האם אנשים משתפים אותו?</li>
  </ul>
  שילוב כל הגורמים הללו יוצר את "ציון פוטנציאל המעורבות" - הערכה של כמה "שווה" להראות לכם את התוכן הזה.

  <h3>זיהוי טרנדים: תופעות ויראליות ו"באזז" דיגיטלי</h3>
  <p>מעבר לניתוח תוכן ספציפי, ה-AI סורק כל הזמן את "דופק הרשת". הוא מזהה נושאים, מילות מפתח או האשטאגים שמתחילים להופיע בתדירות גבוהה באופן חריג, או כאלו שצוברים מעורבות מהירה מאוד. אלו הם ה"טרנדים". זיהוי טרנדים מאפשר לרשת להבליט תכנים רלוונטיים לנושאים אקטואליים או פופולריים, ולמעשה לעזור להם להתפשט עוד יותר מהר ולהפוך לויראליים. זה גם מבטיח שתמיד תראו בפיד שלכם דברים "חמים" שעליהם כולם מדברים.</p>

  <h3>הלולאה הדיגיטלית: אתם מאמנים את המוח</h3>
  <p>האלגוריתמים הם לא סטטיים. הם מערכות לומדות. כל אינטראקציה שלכם - לייק, שיתוף, תגובה, קליק, צפייה ארוכה בסרטון, או אפילו התעלמות מפוסט מסוים - היא פיסת מידע יקרת ערך עבור ה-AI. המידע הזה נאסף, מנותח, ומשמש כדי לשפר את המודלים לחיזוי. אם לדוגמה תתחילו לגלול מהר כשמופיעים סרטוני חתולים ותצפו עד הסוף בסרטוני בישול, ה-AI יבין את השינוי בהעדפותיכם וישנה בהתאם את סדר התכנים שיוצגו לכם בעתיד. כך, למעשה, ההתנהגות שלכם ברשתות מאמנת את המוח הדיגיטלי לשרת אתכם (ולהציג לכם מודעות) בצורה מדויקת ויעילה יותר - ולרשת להחזיק אתכם כמה שיותר זמן בתוכה.</p>

  <h3>ההשפעה מעבר לפיד: האלגוריתמים מעצבים את המציאות</h3>
  <p>השפעת האלגוריתמים חורגת הרבה מעבר לחוויה האישית שלכם. בכך שהם מחליטים איזה מידע יגיע אליכם ומאיזה תתעלמו, הם משפיעים על האופן שבו אתם תופסים את העולם, על הנושאים שנראים לכם חשובים, ואף על הדעות שאליהן אתם נחשפים. זה יכול להוביל לתופעת "בועות פילטר" או "חדרי הדהוד", בהם אנו נחשפים בעיקר למידע ודעות שתואמים את אלו שכבר יש לנו. הבנת פעולתם חיונית כדי להיות גולשים וצרכני מידע ביקורתיים ומודעים יותר בעולם הדיגיטלי.</p>
</div>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const contentOptionsData = [
      { id: 'cat-video', title: 'סרטון מצחיק של חתולים', type: 'video', keywords: ['חתולים', 'מצחיק', 'וידאו', 'בידור', 'קליל'], sentiment: 'חיובי מאד', potential: 95, isTrendyTopic: true, analysisDetail: 'ה-AI זיהה סרטון קצר וקליל עם נושא פופולרי (חתולים!) וסנטימנט חיובי ומבדר. פוטנציאל ויראליות גבוה.' },
      { id: 'ai-ethics', title: 'מאמר מעמיק על אתיקה ב-AI', type: 'text', keywords: ['AI', 'אתיקה', 'טכנולוגיה', 'חברה', 'דו"ח', 'עתיד'], sentiment: 'ניטרלי/פורמלי', potential: 40, isTrendyTopic: false, analysisDetail: 'ה-AI זיהה מאמר ארוך עם נושא רציני וסנטימנט ניטרלי/פורמלי. פונה לקהל נישתי יותר, פחות פוטנציאל למעורבות רחבה.' },
      { id: 'sunset-photo', title: 'תמונת שקיעה אמנותית', type: 'image', keywords: ['שקיעה', 'טבע', 'יפה', 'צילום', 'אומנות'], sentiment: 'חיובי', potential: 75, isTrendyTopic: true, analysisDetail: 'ה-AI זיהה תמונת נוף אסתטית עם סנטימנט חיובי. נושאים ויזואליים כמו נופים וצילום נוטים לקבל מעורבות טובה, במיוחד אם יפים במיוחד.' },
      { id: 'soup-recipe', title: 'מתכון קל ומהיר למרק עדשים', type: 'text', keywords: ['מתכון', 'אוכל', 'מרק', 'קל', 'בישול', 'ביתי'], sentiment: 'חיובי', potential: 60, isTrendyTopic: false, analysisDetail: 'ה-AI זיהה תוכן פרקטי ושימושי (מתכון) עם סנטימנט חיובי. פוטנציאל טוב לקהל רחב שמתעניין בבישול, אך לרוב לא ויראלי כמו תוכן בידורי.' }
    ];

    const contentSelectionDiv = document.getElementById('content-selection');
    const aiAnalysisSection = document.getElementById('ai-analysis-section');
    const stepAnalysisDiv = document.getElementById('step-analysis');
    const stepPredictionDiv = document.getElementById('step-prediction');
    const stepTrendsDiv = document.getElementById('step-trends');
    const engagementScoreBar = document.getElementById('engagement-score-bar');
    const engagementScoreValue = document.getElementById('engagement-score-value');
    const feedbackText = document.getElementById('feedback-text');
    const showExplanationButton = document.getElementById('show-explanation');
    const explanationSection = document.getElementById('explanation-section');
    const resetButton = document.getElementById('reset-sim');
    const aiFeedbackResults = document.getElementById('ai-feedback-results');
    const scoreTextSpan = document.getElementById('score-text');


    // Add event listeners to content options
    contentSelectionDiv.querySelectorAll('.content-option').forEach(button => {
      button.addEventListener('click', () => {
        // Remove 'selected' class from all buttons
        contentSelectionDiv.querySelectorAll('.content-option').forEach(btn => btn.classList.remove('selected'));

        // Add 'selected' class to the clicked button
        button.classList.add('selected');

        const contentId = button.dataset.contentId;
        const selectedContent = contentOptionsData.find(content => content.id === contentId);
        if (selectedContent) {
          simulateAIAnalysis(selectedContent);
        }
      });
    });

    // Simulate AI analysis process with animations
    function simulateAIAnalysis(content) {
      // Hide selection, show analysis section immediately
      contentSelectionDiv.style.display = 'none';
      aiAnalysisSection.style.display = 'block';
      aiAnalysisSection.classList.add('visible'); // Add class for fade/slide in

      // Reset previous results and animations
      stepAnalysisDiv.innerHTML = '';
      stepPredictionDiv.innerHTML = '';
      stepTrendsDiv.innerHTML = '';
      stepAnalysisDiv.classList.add('loading');
      stepPredictionDiv.classList.add('loading');
      stepTrendsDiv.classList.add('loading');

      document.querySelectorAll('.analysis-step').forEach(step => {
          step.classList.remove('visible'); // Hide steps for re-animation
      });

      engagementScoreBar.style.width = '0';
      engagementScoreValue.textContent = '0';
      scoreTextSpan.textContent = '0%';
      scoreTextSpan.style.opacity = '0'; // Hide score text initially
      feedbackText.textContent = '';
      aiFeedbackResults.style.opacity = '0'; // Hide results section

      // Clear previous bar color classes
      engagementScoreBar.classList.remove('high', 'medium-high', 'medium', 'low');


      // Step 1: Analyze Content
      setTimeout(() => {
        stepAnalysisDiv.innerHTML = `
          זיהוי מילות מפתח: <strong>${content.keywords.join(', ')}</strong><br>
          סנטימנט: <strong>${content.sentiment}</strong><br>
          סוג תוכן: <strong>${content.type}</strong><br>
          ${content.analysisDetail}
        `;
        stepAnalysisDiv.classList.remove('loading');
        document.querySelector('.analysis-step:nth-child(1)').classList.add('visible');
      }, 800); // Simulate delay for step 1

      // Step 2: Predict Engagement
      setTimeout(() => {
        const score = content.potential;
        stepPredictionDiv.innerHTML = `
          חישוב מבוסס היסטוריית משתמשים ותכונות תוכן: <strong>${score}/100</strong>
        `;
         stepPredictionDiv.classList.remove('loading');
         document.querySelector('.analysis-step:nth-child(2)').classList.add('visible');

        // Animate the score bar and value
        const scoreAnimationDuration = 1500; // ms
        let currentScore = 0;
        const scoreInterval = setInterval(() => {
            currentScore += Math.ceil(score / (scoreAnimationDuration / 50)); // Increment based on duration
            if (currentScore >= score) {
                currentScore = score;
                clearInterval(scoreInterval);
                 scoreTextSpan.style.opacity = '1'; // Show text after animation
            }
            engagementScoreValue.textContent = currentScore;
            engagementScoreBar.style.width = currentScore + '%';
             scoreTextSpan.textContent = currentScore + '%';
        }, 50);

        // Set bar color based on score
        if (score >= 80) {
           engagementScoreBar.classList.add('high');
        } else if (score >= 60) {
           engagementScoreBar.classList.add('medium-high');
        } else if (score >= 40) {
            engagementScoreBar.classList.add('medium');
        } else {
           engagementScoreBar.classList.add('low');
        }


      }, 2000); // Simulate delay for step 2

      // Step 3: Identify Trends
       setTimeout(() => {
           stepTrendsDiv.innerHTML = `
               בדיקת קשר לנושאים חמים ומתפתחים ברשת...<br>
               <strong>${content.isTrendyTopic ? '🔥 זיהוי טרנד: קשור לנושאים ויראליים כרגע! 🔥' : '❄️ לא קשור לטרנדים רחבים כרגע.'}</strong>
           `;
           stepTrendsDiv.classList.remove('loading');
           document.querySelector('.analysis-step:nth-child(3)').classList.add('visible');
       }, 3200); // Simulate delay for step 3

      // Final Feedback & Show Results Section
      setTimeout(() => {
        let feedback = 'על פי המוח הדיגיטלי: ';
        if (content.potential >= 80) {
          feedback += 'פוטנציאל ויראליות אדיר! התוכן מבדר/פופולרי, סנטימנט חיובי ביותר וקשור לטרנדים חמים. צפה לחשיפה מקסימלית!';
        } else if (content.potential >= 60) {
          feedback += 'פוטנציאל מעורבות גבוה. תוכן מעניין ורלוונטי. עשוי להגיע לקהל רחב וליצור אינטראקציה משמעותית.';
        } else if (content.potential >= 40) {
          feedback += 'פוטנציאל מעורבות בינוני. התוכן אינפורמטיבי או נישתי. יגיע כנראה לקהל יעד ספציפי יותר.';
        } else {
          feedback += 'פוטנציאל מעורבות נמוך יותר עבור חשיפה רחבה. תוכן מעמיק או נישתי מאוד שפחות נוטה להיות ויראלי ברשת הכללית.';
        }
         feedbackText.textContent = feedback;
         aiFeedbackResults.style.opacity = '1'; // Fade in results section
      }, 4500); // Simulate delay for feedback
    }

    // Toggle explanation section
    showExplanationButton.addEventListener('click', () => {
      const isHidden = explanationSection.style.display === 'none' || explanationSection.style.opacity === '0';
      if(isHidden) {
        explanationSection.style.display = 'block'; // Show first
        setTimeout(() => explanationSection.classList.add('visible'), 10); // Then add class for transition
      } else {
         explanationSection.classList.remove('visible'); // Start transition out
         setTimeout(() => explanationSection.style.display = 'none', 500); // Hide after transition
      }
      showExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'פענוח האלגוריתם: הסבר מעמיק';
    });

    // Reset simulation
     resetButton.addEventListener('click', () => {
        aiAnalysisSection.style.display = 'none';
        aiAnalysisSection.classList.remove('visible'); // Remove class
        contentSelectionDiv.style.display = 'flex'; // Show selection again
         contentSelectionDiv.querySelectorAll('.content-option').forEach(btn => btn.classList.remove('selected')); // Deselect buttons
         // Reset analysis output visually (done when simulateAIAnalysis is called again, but good to clear on reset too)
         stepAnalysisDiv.innerHTML = '';
         stepPredictionDiv.innerHTML = '';
         stepTrendsDiv.innerHTML = '';
         engagementScoreBar.style.width = '0';
         engagementScoreValue.textContent = '0';
         scoreTextSpan.textContent = '0%';
         scoreTextSpan.style.opacity = '0';
         feedbackText.textContent = '';
         aiFeedbackResults.style.opacity = '0';
          document.querySelectorAll('.analysis-step').forEach(step => {
             step.classList.remove('visible');
             step.querySelector('.analysis-step-output').classList.remove('loading'); // Ensure loaders are off
         });
          engagementScoreBar.classList.remove('high', 'medium-high', 'medium', 'low'); // Clear bar color

     });

  });
</script>
---
```