---
title: "הקסם של הצמנט הרומי: עמיד במים לאלפי שנים"
english_slug: the-magic-of-roman-cement-waterproof-for-thousands-of-years
category: "הנדסת חומרים"
tags: [הנדסה רומית, בטון, צמנט, פוצולן, כימיה של חומרים]
---
<h1>הקסם של הצמנט הרומי: עמיד במים לאלפי שנים</h1>
<p>דמיינו את זה: מבנים מפוארים, נמלים עתיקים, אמות מים אדירות – כולם שרדו אלפי שנים, אפילו תחת גלי הים הפראיים. איך יצרו הרומאים, בלי המפעלים המודרניים שלנו, חומר בנייה כל כך בלתי מנוצח? התכוננו לחשוף את הסוד הכימי העתיק שהפך סיד פשוט לצמנט ימי אגדי. הצטרפו למסע אינטראקטיבי אל לב ההמצאה הרומית ששינתה את העולם!</p>

<div id="roman-cement-app" class="simulation-app">
  <h2>המסע אל הסוד הרומי: סימולציית בנייה ובדיקה</h2>

  <div class="simulation-step active" id="step1-lime">
    <h3>שלב 1: הבסיס - טיח סיד מסורתי</h3>
    <p>הכל מתחיל עם הבסיס של פעם: טיח סיד. זה היה המלט של העולם העתיק. מערבבים סיד, מים ואגרגט (חול ואבנים). הוא מתקשה, כן, אבל רק באוויר הפתוח, ותחת מים... טוב, בואו נראה.</p>
    <button id="make-lime-mortar">הכינו את תערובת הסיד הבסיסית</button>
    <div class="mix-representation" id="lime-mix-viz" style="display: none;">
      <div class="ingredients">
        <div class="ingredient"><img src="https://via.placeholder.com/80x80?text=סיד" alt="סיד"><p>סיד</p></div>
        <div class="ingredient"><img src="https://via.placeholder.com/80x80?text=מים" alt="מים"><p>מים</p></div>
        <div class="ingredient"><img src="https://via.placeholder.com/80x80?text=אגרגט" alt="אגרגט"><p>אגרגט</p></div>
      </div>
      <div class="mixing-process">
         <div class="arrow">← ערבוב ←</div>
         <div class="mixed-bowl lime">טיח סיד מוכן</div>
      </div>
    </div>
  </div>

  <div class="simulation-step" id="step2-roman">
    <h3>שלב 2: התוספת המופלאה - הפוצולן!</h3>
    <p>וכאן נכנס הקסם הרומי! במקום טיח סיד רגיל, הרומאים גילו שתוספת אפר וולקני מיוחד (שכינו 'פוצולן') משנה הכל. החומר הזה, שנראה כמו אבק פשוט, יוצר תגובה כימית חדשה לגמרי! לחצו כדי להוסיף את החומר הסודי ולערבב.</p>
    <button id="add-pozzolan">הוספו פוצולן וערבבו ליצירת צמנט רומי</button>
    <div class="mix-representation" id="roman-mix-viz" style="display: none;">
      <div class="ingredients">
         <div class="ingredient"><img src="https://via.placeholder.com/80x80?text=סיד" alt="סיד"><p>סיד</p></div>
         <div class="ingredient"><img src="https://via.placeholder.com/80x80?text=מים" alt="מים"><p>מים</p></div>
         <div class="ingredient"><img src="https://via.placeholder.com/80x80?text=אגרגט" alt="אגרגט"><p>אגרגט</p></div>
         <div class="ingredient pozzolan-added"><img src="https://via.placeholder.com/80x80?text=פוצולן" alt="פוצולן"><p>פוצולן</p></div>
      </div>
       <div class="mixing-process">
          <div class="arrow">← ערבוב קסום ←</div>
          <div class="mixed-bowl roman">צמנט רומי מופלא מוכן!</div>
       </div>
    </div>
  </div>

  <div class="simulation-step" id="step3-test">
    <h3>שלב 3: המבחן הגדול - עמידות במים</h3>
    <p>עכשיו למבחן האמת! ניקח דוגמאות משתי התערובות שיצרנו - טיח הסיד הרגיל והצמנט הרומי הסודי - ונשקיע אותן במים כדי לראות איך הן מתמודדות לאורך 'זמן'. מי ישרוד ומי ייכנע?</p>
    <button id="start-water-test">צאו לדרך עם מבחן המים!</button>
    <div id="water-tanks-viz" style="display: none;">
      <div class="water-tank">
        <div class="water"></div>
        <div id="sample-lime-in-water" class="sample lime">טיח סיד</div>
        <p class="tank-label">טיח סיד במים</p>
      </div>
      <div class="water-tank">
        <div class="water"></div>
        <div id="sample-roman-in-water" class="sample roman">צמנט רומי</div>
        <p class="tank-label">צמנט רומי במים</p>
      </div>
    </div>
    <div id="test-results" style="display: none;">
      <h4>הזמן עבר... והתוצאות לפניכם!</h4>
      <p id="lime-result" class="result"></p>
      <p id="roman-result" class="result"></p>
    </div>
  </div>
</div>

<button id="toggle-explanation" class="explanation-toggle">רוצים לגלות את הסוד הכימי? הצגת/הסתרת ההסבר המפורט</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: הסוד הכימי של הצמנט הרומי</h2>

    <h3>מהו צמנט ומהו בטון?</h3>
    <p>נתחיל בבסיס: <strong>צמנט</strong> (מלט) הוא חומר מקשר קסום, כמו דבק על-חלל לחומרי בנייה. הוא מחבר יחד <strong>אגרגטים</strong> (חול, חצץ, אבנים קטנות) ויוצר תערובת שאנחנו קוראים לה <strong>בטון</strong>. כשהבטון מתקשה, הוא הופך לגוש מוצק וחזק בצורה בלתי רגילה, והצמנט הוא הכוח המניע שמאחורי ההתקשות הזו.</p>

    <h3>ההבדל בין טיח סיד של סבא לצמנט הרומי הגאוני</h3>
    <p><strong>טיח סיד</strong> היה הסטנדרט שנים רבות. מכינים אותו מסיד שרוף וכבוי (סידן הידרוקסידי, Ca(OH)₂). ההתקשות שלו? תהליך איטי שמתרחש באוויר הפתוח בלבד, כשהוא נושם פחמן דו חמצני מהאטמוספרה והופך בחזרה לאבן גיר (סידן פחמתי, CaCO₃). הבעיה? הוא לא אוהב מים. אם הוא נרטב מדי או שוקע במים, הוא נחלש ומתפורר לאורך זמן.</p>
    <p>אבל הרומאים... אה, הרומאים הוסיפו טוויסט גאוני! הם לקחו את בסיס הסיד הזה והוסיפו לו את ה<strong>פוצולן</strong>. התוספת הזו לא רק שיפרה את החוזק, אלא הפכה את החומר לעמיד בצורה פנומנלית למים. זו הייתה המהפכה ההנדסית שלהם!</p>

    <h3>המפתח לקסם: המרכיבים הסודיים של הצמנט הרומי</h3>
    <ul>
        <li><strong>סיד (Lime):</strong> הלב של התערובת. זה אותו סיד כבוי שמשתמשים בו לטיח רגיל.</li>
        <li><strong>אגרגט (Aggregate):</strong> החלק ה"שמנמן" של הבטון - חול, חצץ, אבנים. הרומאים היו יצירתיים והשתמשו לפעמים גם בשברי לבנים או רעפים שרופים.</li>
        <li><strong>פוצולן (Pozzolan):</strong> המרכיב הסודי והקריטי! זה החומר ששינה את כללי המשחק.</li>
    </ul>

    <h3>אז מה זה לעזאזל פוצולן?</h3>
    <p>פוצולן זה שם קצת מוזר לחומר שבמבט ראשון לא נראה מיוחד. זה בדרך כלל אפר וולקני או חומרים אחרים עשירים בסיליקה (SiO₂) ואלומינה (Al₂O₃) במצב שנקרא "אמורפי" (כלומר, לא מסודר כמו גביש). בפני עצמו, הפוצולן לא מתקשה במים. אבל כשהוא פוגש את הסיד הכבוי בנוכחות מים - קורה הקסם!</p>
    <p>הרומאים מצאו את האפר הוולקני המושלם הזה ליד עיירה בשם פוצואולי (Pozzuoli) שליד נאפולי - ומכאן השם שנדבק לחומר. הם גם היו חכמים מספיק להבין שגם שברי לבנים או חרס שרוף היטב יכולים לשמש כ"פוצולנה מלאכותית".</p>

    <h3>הקסם הכימי בפעולה: התגובה הפוצולנית</h3>
    <p>בואו נצלול לרגע למיקרוסקופ הכימי. כשהסיד הכבוי (Ca(OH)₂) והפוצולן (בעיקר SiO₂ ו-Al₂O₃) נפגשים במים, הם לא סתם יושבים יחד. הם מגיבים כימית! הסיד "אוכל" את הסיליקה והאלומינה מהפוצולן בנוכחות המים, ויוצר תרכובות חדשות לגמרי:</p>
    <ul>
        <li>סידן-סיליקט הידרטים (C-S-H)</li>
        <li>סידן-אלומניום הידרטים (C-A-H)</li>
    </ul>
    <p>אל תיתנו לשמות המפוצצים לבלבל אתכם. אלו אותן תרכובות מדהימות שמקנות חוזק ועמידות למים גם לצמנט המודרני שלנו (צמנט פורטלנד). התגובה הזו, בניגוד להתקשות טיח הסיד, מתרחשת *במים* ויכולה להימשך זמן רב, מה שהופך את החומר לחזק יותר ויותר כשהוא חשוף לרטיבות!</p>

    <h3>למה הקסם הזה עובד כל כך טוב במים?</h3>
    <p>זוכרים שטיח סיד התקשה ע"י תגובה עם אוויר (CO₂)? התגובה הפוצולנית מתקיימת עם מים (הידרציה). זה אומר שהיא לא צריכה אוויר, והיא אפילו משגשגת בנוכחות מים. התוצרים החדשים (C-S-H, C-A-H) הם כמו רשת צפופה ובלתי מסיסה כמעט, שממלאת את כל הרווחים הקטנים בחומר. הרשת הזו לא רק מקנה חוזק עצום, אלא גם חוסמת את המים מלהיכנס פנימה ולפגוע בחומר.</p>
    <p>ועוד משהו חשוב: התגובה הזו "בולעת" את הסיד הכבוי החופשי שנשאר מהתגובה הראשונית. הסיד החופשי הזה הוא הנקודה החלשה של טיח הסיד, כי הוא נוטה להישטף או להגיב עם חומרים מזיקים במים (כמו סולפטים). כשהפוצולן צורך אותו, הוא מנטרל את הנקודה החלשה הזו והופך את הצמנט הרומי לחסין במיוחד, בייחוד בסביבות אגרסיביות כמו מי ים מלוחים!</p>

    <h3>עדויות חיות: המבנים שהרומאים השאירו מאחור</h3>
    <p>הטכנולוגיה הזו לא נשארה על הנייר. הרומאים השתמשו בה כדי לבנות אימפריה! הנה כמה דוגמאות עוצרות נשימה:</p>
    <ul>
        <li><strong>נמלים ימיים:</strong> דמיינו את הנמל העתיק של קיסריה בישראל או אוסטיה באיטליה. הם בנו שוברים גלים ומזחים ששקעו במים והתקשו שם, עומדים איתן מול הגלים והמלח במשך אלפי שנים!</li>
        <li><strong>מרחצאות ענק (Thermae):</strong> כמו מרחצאות קרקלה ברומא, עם כיפות ענקיות וצורך בלתי פוסק בעמידות ללחות ואדים.</li>
        <li><strong>אמות מים (Aqueducts):</strong> אותם גשרים מפוארים שהובילו מים לערים, שנבנו בחלקם מבטון רומי עמיד.</li>
        <li><strong>הפנתיאון:</strong> אחד המבנים המרשימים ביותר ששרדו. הכיפה הענקית שלו, הגדולה ביותר בעולם העתיק שלא נתמכה, יכלה להיבנות רק בזכות הקלות היחסית והעמידות של הבטון הרומי לעומת אבן.</li>
    </ul>
    <p>הבנת הסודות של הצמנט הרומי לא רק מלמדת אותנו על גאונות העבר, אלא גם נותנת השראה למחקר עכשווי על חומרי בנייה ירוקים ועמידים יותר לעתיד!</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const appContainer = document.getElementById('roman-cement-app');
    const steps = appContainer.querySelectorAll('.simulation-step');
    const makeLimeMortarBtn = document.getElementById('make-lime-mortar');
    const limeMixViz = document.getElementById('lime-mix-viz');
    const addPozzolanBtn = document.getElementById('add-pozzolan');
    const romanMixViz = document.getElementById('roman-mix-viz');
    const startWaterTestBtn = document.getElementById('start-water-test');
    const waterTanksViz = document.getElementById('water-tanks-viz');
    const sampleLimeInWater = document.getElementById('sample-lime-in-water');
    const sampleRomanInWater = document.getElementById('sample-roman-in-water');
    const testResults = document.getElementById('test-results');
    const limeResultP = document.getElementById('lime-result');
    const romanResultP = document.getElementById('roman-result');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    let currentStep = 0;

    function showStep(stepIndex) {
        steps.forEach((step, index) => {
            step.classList.remove('active');
            step.style.display = 'none';
        });
        steps[stepIndex].style.display = 'block';
        // Use a small delay to allow display:block before adding active class for transitions
        setTimeout(() => {
             steps[stepIndex].classList.add('active');
        }, 50);
        currentStep = stepIndex;
    }

    function animateIngredients(mixVizElement, callback) {
        const ingredients = mixVizElement.querySelectorAll('.ingredient');
        ingredients.forEach((ing, index) => {
            ing.style.opacity = 0;
            ing.style.transform = 'translateY(-20px)';
            setTimeout(() => {
                ing.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
                ing.style.opacity = 1;
                ing.style.transform = 'translateY(0)';
            }, index * 200); // Stagger ingredient appearance
        });

        const mixingProcess = mixVizElement.querySelector('.mixing-process');
         mixingProcess.style.opacity = 0;
         mixingProcess.style.transform = 'scale(0.8)';
         setTimeout(() => {
             mixingProcess.style.transition = 'opacity 0.7s ease-out, transform 0.7s ease-out';
             mixingProcess.style.opacity = 1;
             mixingProcess.style.transform = 'scale(1)';
             if (callback) {
                 setTimeout(callback, 800); // Delay callback slightly after mixing animation
             }
         }, ingredients.length * 200 + 300); // Start mixing animation after ingredients appear
    }


    // Initialize - show the first step
    showStep(0);

    makeLimeMortarBtn.addEventListener('click', () => {
        makeLimeMortarBtn.disabled = true;
        limeMixViz.style.display = 'flex'; // Use flex for layout
        animateIngredients(limeMixViz, () => {
             setTimeout(() => {
                showStep(1);
            }, 1500); // Wait after animation ends
        });
    });

    addPozzolanBtn.addEventListener('click', () => {
        addPozzolanBtn.disabled = true;
        romanMixViz.style.display = 'flex'; // Use flex for layout
         animateIngredients(romanMixViz, () => {
             setTimeout(() => {
                showStep(2);
            }, 1500); // Wait after animation ends
         });
    });

    startWaterTestBtn.addEventListener('click', () => {
        startWaterTestBtn.disabled = true;
        waterTanksViz.style.display = 'flex'; // Show the tanks

        // Animate samples dropping into water
        setTimeout(() => {
            sampleLimeInWater.style.bottom = '20%'; // Position in water
            sampleLimeInWater.style.opacity = 1; // Ensure visible
            sampleRomanInWater.style.bottom = '20%'; // Position in water
            sampleRomanInWater.style.opacity = 1; // Ensure visible
        }, 100); // Short delay after tanks appear

        // Simulate time passing and showing results with animation
        setTimeout(() => {
            // Lime mortar starts to deteriorate
            sampleLimeInWater.classList.add('deteriorating');
            limeResultP.textContent = 'תוצאת טיח סיד: החל להתפורר ולהיעלם במים...';

            // Roman cement remains solid
            sampleRomanInWater.textContent = 'צמנט רומי (סלע!)'; // Update text for emphasis
             romanResultP.textContent = 'תוצאת צמנט רומי: נשאר מוצק, התקשה עוד יותר, עמיד לחלוטין!';
             sampleRomanInWater.style.boxShadow = '0 0 15px rgba(0,255,0,0.5)'; // Subtle glow for success


            // After deterioration animation completes (CSS handles duration)
            sampleLimeInWater.addEventListener('animationend', () => {
                 testResults.style.display = 'block'; // Show the results text after lime deteriorates
            }, { once: true }); // Only trigger once
             // Fallback in case animationend isn't caught or animation is short
             setTimeout(() => {
                 testResults.style.display = 'block';
             }, 2500); // Ensure results show after max deterioration time
        }, 2000); // Start deterioration/hardening visualization after 2 seconds in water
    });

    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג הסבר מפורט';
    });
});
</script>

<style>
  /* General Styles */
  #roman-cement-app {
    border: 1px solid #e0e0e0; /* Softer border */
    padding: 30px; /* More padding */
    border-radius: 12px; /* More rounded corners */
    margin: 30px auto; /* Center block */
    max-width: 800px; /* Max width for better readability */
    background-color: #fefefe; /* Lighter background */
    direction: rtl;
    text-align: right;
    font-family: 'Arial', sans-serif; /* A common, clean font */
    box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Subtle shadow */
  }

  #roman-cement-app h2 {
    color: #2c3e50; /* Darker, professional blue */
    text-align: center;
    margin-bottom: 25px;
    font-size: 2em;
  }

   #roman-cement-app h3 {
    color: #34495e; /* Slightly lighter */
    text-align: center;
    margin-top: 20px;
    margin-bottom: 15px;
    font-size: 1.5em;
  }

  #roman-cement-app p {
      color: #555;
      line-height: 1.7;
      margin-bottom: 15px;
      text-align: center; /* Center text in simulation steps */
  }

  .simulation-step {
    margin-bottom: 40px;
    padding-bottom: 30px;
    border-bottom: 1px dashed #ddd;
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    display: none; /* Initially hidden, JS manages display block */
  }

  .simulation-step.active {
      opacity: 1;
      transform: translateY(0);
  }

  .simulation-step:last-child {
    border-bottom: none;
    margin-bottom: 0;
  }

  button {
    padding: 12px 25px; /* Larger buttons */
    font-size: 1.1em;
    cursor: pointer;
    background: linear-gradient(to bottom, #3498db, #2980b9); /* Gradient blue */
    color: white;
    border: none;
    border-radius: 6px; /* More rounded */
    margin: 20px auto; /* Center block with margin */
    display: block;
    transition: background 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
  }

  button:hover {
    background: linear-gradient(to bottom, #2980b9, #3498db);
    transform: translateY(-1px);
  }

  button:disabled {
      background: #bdc3c7;
      cursor: not-allowed;
      box-shadow: none;
      transform: none;
  }

  /* Mix Representation Styles */
  .mix-representation {
    margin-top: 30px;
    padding: 25px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #ecf0f1; /* Light grey-blue */
    text-align: center;
    display: flex; /* Use flexbox */
    flex-direction: column;
    align-items: center;
    gap: 20px; /* Space between ingredients and mixing */
  }

   .mix-representation .ingredients {
       display: flex;
       justify-content: center;
       gap: 15px; /* Space between ingredients */
   }

  .mix-representation .ingredient {
      text-align: center;
      opacity: 0; /* Start hidden for animation */
      transform: translateY(-20px); /* Start above for animation */
      transition: opacity 0.5s ease, transform 0.5s ease; /* Animation */
  }

  .mix-representation .ingredient img {
      display: block; /* Remove extra space */
      margin: 0 auto 5px;
      border-radius: 4px; /* Slightly rounded images */
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  }

   .mix-representation .ingredient p {
       font-size: 0.9em;
       color: #333;
       margin: 0;
       text-align: center;
   }

   .mixing-process {
       display: flex;
       align-items: center;
       gap: 20px;
       opacity: 0; /* Start hidden for animation */
       transform: scale(0.8); /* Start smaller for animation */
       transition: opacity 0.7s ease, transform 0.7s ease; /* Animation */
   }

  .mixing-process .arrow {
      font-size: 1.5em;
      color: #7f8c8d;
  }


  .mixed-bowl {
    display: inline-block;
    padding: 20px 30px; /* More padding */
    border: 3px solid #34495e; /* Darker border */
    border-radius: 20px; /* More rounded, bowl-like */
    background-color: #bdc3c7; /* Default grey */
    min-width: 180px; /* Wider */
    text-align: center;
    font-weight: bold;
    font-size: 1.1em;
    color: #2c3e50;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* Inner shadow */
    transition: background-color 0.5s ease; /* Smooth color change */
  }

  .mixed-bowl.lime {
     background-color: #e0e0e0; /* Lighter grey for lime */
  }

  .mixed-bowl.roman {
     background-color: #a0522d; /* Earthy brown for roman cement */
     color: white;
     text-shadow: 0 1px 2px rgba(0,0,0,0.3);
  }

  /* Water Test Styles */
  #water-tanks-viz {
    display: flex;
    justify-content: space-around;
    align-items: flex-end; /* Align tanks bottoms */
    margin-top: 30px;
    gap: 30px; /* Space between tanks */
    min-height: 250px; /* Ensure space for samples */
    /* Removed perspective as it's not used */
  }

  .water-tank {
    width: 160px; /* Wider tank */
    height: 220px; /* Taller tank */
    border: 2px solid #3498db; /* Blue border */
    border-top: none; /* No top border */
    border-radius: 0 0 15px 15px; /* More rounded base */
    position: relative;
    overflow: hidden; /* Hide anything outside */
    background-color: #ecf0f1; /* Tank background */
    box-shadow: 0 5px 10px rgba(0,0,0,0.1); /* Soft shadow */
  }

  .water {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 100%; /* Water fills the tank height visually */
    background: linear-gradient(to bottom, rgba(52, 152, 219, 0.3), rgba(52, 152, 219, 0.6)); /* Gradient water */
    z-index: 1; /* Water below sample */
  }

  .tank-label {
      position: absolute;
      top: 10px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 1em;
      font-weight: bold;
      color: #2c3e50;
      text-align: center;
      width: 100%;
      z-index: 3; /* Label above */
  }


  .sample {
    position: absolute;
    width: 70px; /* Larger sample */
    height: 70px;
    background-color: #ccc;
    border: 2px solid #555;
    border-radius: 8px; /* More rounded */
    bottom: 110%; /* Start high, outside the tank, for drop animation */
    left: 50%;
    transform: translateX(-50%);
    text-align: center;
    line-height: 66px; /* Center text vertically */
    font-size: 0.9em;
    font-weight: bold;
    color: #333;
    box-sizing: border-box;
    z-index: 2; /* Sample above water */
    opacity: 0; /* Start hidden */

    /* Initial state for dropping */
    transition: bottom 1.5s ease-in, opacity 0.5s ease; /* Smooth drop */
  }

  .sample.lime {
    background-color: #eee;
  }

  .sample.roman {
    background-color: #a0522d; /* Roman cement color */
    color: white;
  }

  /* Deterioration animation for lime */
  @keyframes crumble {
      0% { transform: translateX(-50%) scale(1); opacity: 1; background-color: #eee; }
      50% { transform: translateX(-50%) scale(1.05); opacity: 0.8; background-color: #f0f0f0; }
      100% { transform: translateX(-50%) scale(0.7); opacity: 0.3; background-color: rgba(238, 238, 238, 0.3); }
  }

  .sample.lime.deteriorating {
    animation: crumble 2s ease-in forwards; /* Apply crumbling animation */
  }


  #test-results {
    margin-top: 40px;
    padding: 25px;
    border: 1px solid #dcdcdc; /* Lighter border */
    border-radius: 8px;
    background-color: #e9f5f9; /* Light blue background */
    text-align: center;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }

   #test-results h4 {
       color: #2c3e50;
       margin-bottom: 20px;
       font-size: 1.3em;
   }

  .result {
      font-size: 1.1em;
      font-weight: bold;
      margin-bottom: 15px;
  }

  #lime-result {
      color: #c0392b; /* Red for failure */
  }

  #roman-result {
      color: #27ae60; /* Green for success */
  }


  /* Explanation Toggle Button */
  .explanation-toggle {
      margin: 30px auto;
      display: block;
      background: linear-gradient(to bottom, #95a5a6, #7f8c8d); /* Grey gradient */
  }
   .explanation-toggle:hover {
      background: linear-gradient(to bottom, #7f8c8d, #95a5a6);
   }


  /* Explanation Section Styles */
  #explanation {
      border: 1px solid #e0e0e0;
      padding: 30px;
      border-radius: 12px;
      background-color: #f9f9f9; /* Slightly different light background */
      direction: rtl;
      text-align: right;
      margin-top: 20px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.08);
  }

  #explanation h2 {
      color: #2c3e50;
      margin-top: 0;
      margin-bottom: 20px;
      text-align: right;
      font-size: 1.8em;
      border-bottom: 1px solid #eee;
      padding-bottom: 10px;
  }

   #explanation h3 {
      color: #34495e;
      margin-top: 25px;
      margin-bottom: 10px;
      text-align: right;
      font-size: 1.4em;
   }

  #explanation p {
      line-height: 1.8; /* More space */
      margin-bottom: 18px;
      color: #444;
      text-align: right; /* Ensure explanation text aligns right */
  }

  #explanation ul {
      margin-bottom: 20px;
      padding-right: 20px; /* Indent list */
      color: #444;
  }

  #explanation li {
      margin-bottom: 8px;
      line-height: 1.6;
  }

   #explanation strong {
       color: #333;
   }
</style>
```