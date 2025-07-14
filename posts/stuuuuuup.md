---
title: "אפקט סטרופ: הריקוד הסבוך של הקשב"
category: "מדעי החברה / פסיכולוגיה"
tags: [פסיכולוגיה, קוגניציה, תפיסה, קשב, סטרופ, ניסוי]
---

# אפקט סטרופ: הקונפליקט המרתק בין מילים לצבעים

ברוכים הבאים לעולם המרתק של אפקט סטרופ – תופעה קוגניטיבית קלאסית שמגלה לנו משהו עמוק על הדרך בה המוח שלנו מעבד מידע. האפקט, שקרוי על שם הפסיכולוג ג'ון ריידלי סטרופ, מדגים בצורה מוחשית את ההפרעה שנוצרת כשאנחנו נתקלים במידע סותר – למשל, כשהמילה "אדום" כתובה בצבע כחול.

הניסוי המפורסם מציג למשתתפים שמות של צבעים המודפסים בדיו בצבעים שונים. המשימה? לזהות במהירות את *צבע הדיו* ולהתעלם ממשמעות המילה הכתובה. נשמע פשוט, נכון? בפועל, רובנו מגלים שהדבר הרבה פחות טריוויאלי מכפי שחשבנו. קריאת המילה, שהיא תהליך אוטומטי ומהיר במיוחד עבור קוראים מיומנים, "קופצת" לנו לתודעה ומפריעה למשימה המודעת והאיטית יותר של זיהוי צבע הדיו. זהו מאבק פנימי יומיומי בין "הטייס האוטומטי" של המוח לבין השליטה המודעת שלנו.

## חוו את הניסוי: טבילה בעולם הקשב

ההדמיה האינטראקטיבית שלפניכם נוצרה כדי לאפשר לכם לצלול אל תוך חוויית אפקט סטרופ בעצמכם. תתבקשו לעבור סדרת ניסויים קצרים ומאתגרים. בכל ניסוי, מילה תופיע על המסך בצבע דיו מסוים. המטרה שלכם היא *ללחוץ כמה שיותר מהר ומדויק* על הכפתור המתאים ל**צבע הדיו** שבו כתובה המילה – *תוך התעלמות מוחלטת מהמילה עצמה*.

שימו לב למה שקורה לכם בזמן הניסוי. האם יש רגעים שבהם המילה "מושכת" את תשומת לבכם? האם אתם מרגישים קונפליקט קטן לפני שאתם מצליחים לבחור את צבע הדיו הנכון? זהו בדיוק אפקט סטרופ בפעולה! בסוף המבחן הקצר, האפליקציה תסכם עבורכם את התוצאות ותיתן לכם הצצה לביצועים שלכם במאבק המרתק הזה בין מילה לצבע.

<div id="stroop-app">
  <style>
    /* כללי */
    #stroop-app {
      font-family: 'Arial Hebrew', sans-serif; /* גופן נעים וקריא יותר */
      text-align: center;
      padding: 30px 20px; /* ריווח פנימי גדול יותר */
      border: none; /* מורידים את המסגרת */
      border-radius: 12px; /* פינות מעוגלות יותר */
      max-width: 550px; /* רוחב מקסימלי מעט גדול יותר */
      margin: 30px auto; /* ריווח חיצוני גדול יותר למעלה ולמטה */
      background: linear-gradient(to bottom right, #eef2f7, #e0e9f3); /* רקע עם גרדיאנט עדין */
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* צל עמוק יותר */
      direction: rtl; /* ודא כיווניות RTL */
      overflow: hidden; /* הסתרת גלישה אם יש אנימציה */
    }
    #stroop-app h2 {
        margin-top: 0;
        margin-bottom: 25px; /* ריווח אחרי הכותרת */
        color: #1a3b5d; /* צבע כותרת עמוק יותר */
        font-size: 1.8em; /* גודל כותרת גדול יותר */
        font-weight: bold;
    }

    /* מצב המשחק/סטטוס */
    #status {
        margin-bottom: 25px; /* ריווח תחתון */
        font-size: 1.2em; /* גודל טקסט סטטוס גדול יותר */
        min-height: 1.5em; /* גובה מינימלי כדי למנוע קפיצות */
        color: #5a677a; /* צבע טקסט סטטוס רגוע */
        transition: color 0.3s ease; /* מעבר צבע חלק */
    }
     #status.correct {
        color: #28a745; /* ירוק להצלחה */
        font-weight: bold;
    }
    #status.incorrect {
        color: #dc3545; /* אדום לכישלון */
        font-weight: bold;
    }


    /* מילה בתצוגה */
    #stroop-word {
      font-size: 4em; /* גודל גופן גדול ומודגש */
      font-weight: 900; /* עובי גופן מירבי */
      margin-bottom: 30px; /* ריווח תחתון */
      height: 1.8em; /* גובה קבוע למניעת קפיצות */
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100px; /* גובה מינימלי גדול יותר */
      transition: color 0.1s ease-out, transform 0.1s ease-out; /* מעבר חלק בצבע וקנה מידה */
      text-shadow: 2px 2px 4px rgba(0,0,0,0.2); /* צל קל למילה */
    }
    /* אנימציה קטנה על המילה בעת הופעה */
    #stroop-word.new-word {
        animation: appearScale 0.3s ease-out;
    }
    @keyframes appearScale {
        0% { transform: scale(0.8); opacity: 0.5; }
        100% { transform: scale(1); opacity: 1; }
    }


    /* כפתורי צבעים */
    #color-buttons {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(110px, 1fr)); /* כפתורים גדולים יותר */
      gap: 15px; /* רווח גדול יותר בין כפתורים */
      margin-bottom: 30px; /* ריווח תחתון */
    }
    #color-buttons button {
      padding: 18px 15px; /* ריווח פנימי גדול יותר */
      font-size: 1.2em; /* גודל גופן גדול יותר */
      cursor: pointer;
      border: none;
      border-radius: 8px; /* פינות מעוגלות */
      transition: background-color 0.2s ease, transform 0.1s ease; /* מעבר חלק */
      color: white; /* צבע טקסט לבן */
      font-weight: bold;
      text-shadow: 1px 1px 3px rgba(0,0,0,0.4); /* צל טקסט מודגש יותר */
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* צל קטן לכפתור */
    }
    #color-buttons button:hover:not(:disabled) {
        opacity: 0.95; /* שקיפות קלה בריחוף */
        transform: translateY(-2px); /* אפקט קל של הרמה */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); /* צל גדול יותר בריחוף */
    }
     #color-buttons button:disabled {
        cursor: not-allowed;
        opacity: 0.5; /* שקיפות גבוהה יותר ללא פעיל */
        box-shadow: none;
        transform: none;
    }

    /* צבעי כפתורים ספציפיים */
    #btn-red { background-color: #e74c3c; } /* אדום עז יותר */
    #btn-blue { background-color: #3498db; } /* כחול שמיים */
    #btn-green { background-color: #2ecc71; } /* ירוק עשיר */
    #btn-yellow { background-color: #f1c40f; color: #333; text-shadow: 1px 1px 2px rgba(255,255,255,0.6); } /* צהוב בהיר יותר, טקסט כהה וצל בהיר */

    /* כפתורי שליטה */
    #controls button {
        padding: 12px 20px; /* ריווח פנימי גדול יותר */
        font-size: 1.1em; /* גודל גופן גדול יותר */
        cursor: pointer;
        border: 1px solid #c0d3eb; /* מסגרת עדינה יותר */
        border-radius: 6px; /* פינות מעוגלות */
        background-color: #ffffff; /* רקע לבן */
        margin: 5px;
        transition: background-color 0.2s ease, box-shadow 0.2s ease; /* מעבר חלק */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08); /* צל קטן */
        color: #333; /* צבע טקסט כהה */
    }
    #controls button:hover:not(:disabled) {
        background-color: #eef2f7; /* רקע בהיר יותר בריחוף */
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.12); /* צל גדול יותר בריחוף */
    }
     #controls button:disabled {
        cursor: not-allowed;
        opacity: 0.6;
        box-shadow: none;
    }

     /* תוצאה סופית */
     #stroop-app.finished #stroop-word {
         font-size: 2em; /* גודל קטן יותר לסיכום */
         font-weight: normal;
         color: #1a3b5d !important; /* צבע אחיד לתוצאה */
         text-shadow: none;
         min-height: 50px;
     }
       #stroop-app.finished #status {
         color: #1a3b5d;
         font-weight: bold;
     }

  </style>

  <h2>חוו את אפקט סטרופ בעצמכם!</h2>
  <div id="status">לחצו "התחל" כדי לאתגר את הקשב שלכם</div>
  <div id="stroop-word">-</div>
  <div id="color-buttons">
    <button id="btn-red" data-color="red">אדום</button>
    <button id="btn-blue" data-color="blue">כחול</button>
    <button id="btn-green" data-color="green">ירוק</button>
    <button id="btn-yellow" data-color="yellow">צהוב</button>
  </div>
  <div id="controls">
    <button id="start-btn">התחל</button>
    <button id="reset-btn" style="display: none;">אפס</button>
  </div>

  <script>
    const words = ['אדום', 'כחול', 'ירוק', 'צהוב'];
    const colors = ['red', 'blue', 'green', 'yellow']; // CSS color names mapped to Hebrew words

    const stroopAppEl = document.getElementById('stroop-app');
    const stroopWordEl = document.getElementById('stroop-word');
    const statusEl = document.getElementById('status');
    const startBtn = document.getElementById('start-btn');
    const resetBtn = document.getElementById('reset-btn');
    const colorButtons = document.querySelectorAll('#color-buttons button');

    let gameActive = false;
    let trialsCompleted = 0;
    let correctAnswers = 0;
    const totalTrials = 15; // מספר הניסויים במבחן
    let currentInkColor = ''; // שומר את שם צבע הדיו הנוכחי ב-CSS
    let trialTimeout = null; // מזהה הטיימאאוט לניסוי הבא
    let buttonPressTimestamp = 0; // זמן לחיצת הכפתור
    let trialStartTime = 0; // זמן תחילת הניסוי
    let reactionTimes = []; // רשימת זמני התגובה

    function getRandomInt(min, max) {
      return Math.floor(Math.random() * (max - min)) + min;
    }

    function displayNewTrial() {
      // הסרת קלאסים של פידבק לפני הניסוי החדש
      statusEl.classList.remove('correct', 'incorrect');
      stroopWordEl.classList.remove('new-word');


      if (trialsCompleted >= totalTrials) {
        endGame();
        return;
      }

      // ודא שכפתורים מופעלים לניסוי החדש
      colorButtons.forEach(button => button.disabled = false);

      const wordIndex = getRandomInt(0, words.length);
      let colorIndex = getRandomInt(0, colors.length);

      // ניתן להוסיף כאן לוגיקה להגדלת סיכוי לאי-התאמה
      // (כרגע אקראי לחלוטין - כולל התאמה)

      const wordText = words[wordIndex];
      currentInkColor = colors[colorIndex]; // צבע הדיו הוא הצבע הנכון ללחוץ עליו

      stroopWordEl.textContent = wordText;
      stroopWordEl.style.color = currentInkColor; // צובע את המילה בצבע הדיו
      stroopWordEl.classList.add('new-word'); // הפעלת אנימציה
      statusEl.textContent = `ניסוי ${trialsCompleted + 1} מתוך ${totalTrials}. מהו צבע הדיו?`;

      trialStartTime = performance.now(); // מתחיל למדוד זמן תגובה לניסוי הנוכחי
    }

    function handleButtonClick(event) {
      if (!gameActive || !trialStartTime) return; // התעלם מלחיצות אם המשחק לא פעיל או הניסוי לא התחיל

      const clickTime = performance.now();
      const reactionTime = clickTime - trialStartTime;
      reactionTimes.push(reactionTime); // שומר את זמן התגובה

      // נטרל כפתורים מיד לאחר בחירה כדי למנוע לחיצות כפולות
      colorButtons.forEach(button => button.disabled = true);
      trialStartTime = 0; // מאפס את זמן תחילת הניסוי עד לניסוי הבא

      const selectedColor = event.target.dataset.color; // קבל את שם צבע ה-CSS מהכפתור

      // הסרת קלאסים קודמים של פידבק
      statusEl.classList.remove('correct', 'incorrect');

      if (selectedColor === currentInkColor) {
        correctAnswers++;
        statusEl.textContent = `נכון! 👍`; // פידבק להצלחה
        statusEl.classList.add('correct');
      } else {
        statusEl.textContent = `טעות. ❌ צבע הדיו היה: ${getColorNameHebrew(currentInkColor)}.`; // פידבק לטעות
        statusEl.classList.add('incorrect');
      }

      trialsCompleted++;
      // הוסף עיכוב קצר לפני הניסוי הבא
      trialTimeout = setTimeout(displayNewTrial, 900); // מעט יותר זמן לפידבק
    }

    function getColorNameHebrew(cssColor) {
        switch(cssColor) {
            case 'red': return 'אדום';
            case 'blue': return 'כחול';
            case 'green': return 'ירוק';
            case 'yellow': return 'צהוב';
            default: return cssColor; // חזרה לברירת מחדל
        }
    }


    function startGame() {
      gameActive = true;
      trialsCompleted = 0;
      correctAnswers = 0;
      reactionTimes = []; // איפוס זמני התגובה
      startBtn.style.display = 'none';
      resetBtn.style.display = 'inline-block';
      stroopWordEl.textContent = '-'; // נקה מילה קודמת
      stroopWordEl.style.color = '#333'; // אפס צבע
      stroopAppEl.classList.remove('finished'); // הסרת קלאס סיום
      displayNewTrial(); // התחל ניסוי ראשון
    }

    function endGame() {
      gameActive = false;
      clearTimeout(trialTimeout); // נקה כל טיימאאוט ממתין
      stroopAppEl.classList.add('finished'); // הוספת קלאס סיום לעיצוב מיוחד
      stroopWordEl.textContent = 'המבחן הסתיים!';
      stroopWordEl.style.color = '#1a3b5d'; // צבע אחיד לטקסט סיום
      stroopWordEl.classList.remove('new-word'); // הסרת אנימציה
      const averageReactionTime = reactionTimes.reduce((sum, rt) => sum + rt, 0) / reactionTimes.length;
      statusEl.textContent = `סיימת ${totalTrials} ניסויים. צדקת ב- ${correctAnswers} מתוך ${totalTrials}. זמן תגובה ממוצע: ${averageReactionTime ? averageReactionTime.toFixed(0) + 'ms' : '--'}.`;
      statusEl.classList.remove('correct', 'incorrect'); // ודא שהסטטוס ללא קלאסים קודמים
      resetBtn.style.display = 'inline-block';
      startBtn.style.display = 'inline-block'; // אפשר להתחיל שוב
      colorButtons.forEach(button => button.disabled = true); // נטרל כפתורים בסיום
    }

    function resetGame() {
        gameActive = false;
        clearTimeout(trialTimeout); // נקה כל טיימאאוט ממתין
        trialsCompleted = 0;
        correctAnswers = 0;
        reactionTimes = [];
        stroopWordEl.textContent = '-';
        stroopWordEl.style.color = '#333';
        statusEl.textContent = 'לחצו "התחל" כדי לאתגר את הקשב שלכם';
        statusEl.classList.remove('correct', 'incorrect'); // ודא שהסטטוס ללא קלאסים קודמים
        resetBtn.style.display = 'none';
        startBtn.style.display = 'inline-block';
        colorButtons.forEach(button => button.disabled = true); // נטרל כפתורים בהתחלה
        stroopAppEl.classList.remove('finished'); // הסרת קלאס סיום
         stroopWordEl.classList.remove('new-word'); // הסרת אנימציה
    }


    // הוספת מאזיני אירועים
    startBtn.addEventListener('click', startGame);
    resetBtn.addEventListener('click', resetGame);
    colorButtons.forEach(button => {
      button.addEventListener('click', handleButtonClick);
      // כפתורים מנוטרלים בהתחלה באמצעות פונקציית resetGame שנקראת למטה
    });

    // הגדרת מצב התחלתי כשהסקריפט נטען
    resetGame();

  </script>
</div>