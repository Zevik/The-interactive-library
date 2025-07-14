---
title: "הכסף שלך 'נעלם'? סימולטור חוויתי לשחיקת כוח קנייה"
english_slug: your-money-disappearing-purchasing-power-erosion-simulator
category: "כלכלה"
tags: [אינפלציה, כוח קנייה, ערך הכסף, חסכון, כלכלת המשפחה, השקעות]
---
# הכסף שלך 'נעלם'? חווה את שחיקת כוח הקנייה באינטראקטיביות!
דמיינו שהכסף שחסכתם בעמל רב, פשוט "מתאדה" לאורך זמן. לא פיזית, אלא ביכולת שלו לקנות דברים. למה זה קורה, ואיך תופעה "שקטה" כמו אינפלציה יכולה לכרסם בחיסכון שלכם בלי שתשימו לב? בואו נצלול לחוויה אינטראקטיבית שתמחיש זאת בדיוק.

<div id="simulator-app">
  <h2>כמה שווה הכסף שלך *באמת* אחרי אינפלציה?</h2>
  <div class="input-group">
    <label for="initial-amount">הסכום ההתחלתי בארנק/בבנק (₪):</label>
    <input type="number" id="initial-amount" value="10000" min="100" step="100">
  </div>
  <div class="input-group">
    <label for="number-of-years">כמה שנים קדימה נסתכל? (1-50)</label>
    <input type="number" id="number-of-years" value="10" min="1" max="50" step="1">
  </div>
    <div class="input-group">
    <label for="inflation-rate">קצב האינפלציה השנתי הממוצע שצפוי (%) - **ברירת מחדל: 3%**</label>
    <input type="number" id="inflation-rate" value="3.0" min="0" step="0.1">
  </div>
  <button id="calculate-btn">חשב את "ההתאדות" של הכסף</button>

  <div id="result-area" class="result">
    <h3>המספרים נחשפים:</h3>
    <div class="result-item initial-value">
        <label>התחלת עם:</label>
        <span id="initial-value-display" class="value"></span>
    </div>
    <div class="result-item eroded-value">
        <label>אחרי <span id="years-display"></span> שנים שווה רק:</label>
        <span id="eroded-value-display" class="value eroded"></span>
    </div>
     <div class="result-item erosion-amount">
        <label>סה"כ "נאכל" ע"י האינפלציה:</label>
        <span id="erosion-amount-display" class="value loss"></span>
    </div>
     <div class="result-item erosion-percentage">
        <label>שחיקה באחוזים:</label>
        <span id="erosion-percentage-display" class="value loss"></span>
    </div>
    <div class="result-summary">
        <p>לסיכום: הסכום ההתחלתי שלך של <span id="summary-initial" class="bold"></span> ש"ח, אחרי <span id="summary-years" class="bold"></span> שנים עם אינפלציה שנתית ממוצעת של <span id="summary-inflation" class="bold"></span>%, שווה היום רק <span id="summary-eroded" class="bold"></span> ש"ח במונחי כוח קנייה. **זהו הפסד של <span id="summary-loss-amount" class="bold"></span> ש"ח, שהם <span id="summary-loss-percentage" class="bold"></span>% מכוח הקנייה המקורי!**</p>
    </div>
  </div>
</div>

<style>
  /* כללי */
  #simulator-app, #explanation-section {
    direction: rtl;
    font-family: 'Heebo', sans-serif; /* פונט נעים יותר */
    color: #333;
  }

  #simulator-app {
    background: linear-gradient(135deg, #f0f4f8 0%, #d9e2ec 100%); /* רקע עדין ומעוצב */
    padding: 30px;
    border-radius: 12px;
    max-width: 550px; /* רוחב מקסימלי קצת יותר גדול */
    margin: 30px auto;
    box-shadow: 0 8px 16px rgba(0,0,0,0.15); /* צל משופר */
    border: 1px solid #c3dae8;
  }

  #simulator-app h2 {
    text-align: center;
    color: #0056b3; /* כחול עמוק יותר */
    margin-bottom: 25px;
    font-size: 1.8rem;
    font-weight: 700;
    position: relative; /* בשביל אולי להוסיף אלמנט עיצובי */
  }

  /* קבוצות קלט */
  .input-group {
    margin-bottom: 20px; /* רווח גדול יותר בין קבוצות */
    background-color: #ffffff;
    padding: 15px;
    border-radius: 8px;
    border: 1px solid #e0e6ef;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  }

  .input-group label {
    display: block;
    margin-bottom: 8px; /* רווח מתחת לתווית */
    font-weight: 600; /* משקל פונט עבה יותר */
    color: #004085; /* כחול כהה */
    font-size: 1rem;
  }

  .input-group input[type="number"] {
    width: calc(100% - 24px); /* התאמה לריפוד וגבול */
    padding: 12px;
    border: 1px solid #c3dae8;
    border-radius: 6px; /* פינות עגולות יותר */
    font-size: 1.1rem;
    color: #333;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
  }

  .input-group input[type="number"]:focus {
    border-color: #007bff; /* הדגשת הפוקוס */
    box-shadow: 0 0 8px rgba(0,123,255,0.2);
    outline: none;
  }

  /* כפתור חישוב */
  #calculate-btn {
    display: block;
    width: 100%;
    padding: 15px;
    background: linear-gradient(45deg, #007bff 0%, #0056b3 100%); /* מעבר צבעים */
    color: white;
    border: none;
    border-radius: 8px; /* פינות עגולות יותר */
    font-size: 1.2rem;
    font-weight: 700;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease, opacity 0.3s ease; /* הוספת אנימציות */
    box-shadow: 0 4px 8px rgba(0,123,255,0.3);
  }

  #calculate-btn:hover {
    background: linear-gradient(45deg, #0056b3 0%, #004085 100%);
    box-shadow: 0 6px 12px rgba(0,123,255,0.4);
  }

  #calculate-btn:active {
    transform: scale(0.98); /* אנימציית לחיצה */
    box-shadow: 0 2px 4px rgba(0,123,255,0.3);
  }

  #calculate-btn:disabled {
      opacity: 0.6;
      cursor: not-allowed;
      box-shadow: none;
  }

  /* אזור התוצאות */
  .result {
    margin-top: 30px;
    padding: 25px;
    border: 1px solid #c3dae8;
    border-radius: 10px;
    background-color: #e9ecef; /* רקע בהיר לתוצאות */
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    opacity: 0; /* התחלה שקופה לאנימציה */
    transform: translateY(20px); /* התחלה מעט למטה */
    animation: fadeInResult 0.5s ease-out forwards; /* אנימציית כניסה */
    display: none; /* מוסתר בהתחלה ע"י JS */
  }

  @keyframes fadeInResult {
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }


  .result h3 {
    margin-top: 0;
    color: #004085; /* כותרת בולטת */
    border-bottom: 2px solid #c3dae8; /* קו הדגשה */
    padding-bottom: 15px;
    margin-bottom: 20px;
    font-size: 1.5rem;
  }

  .result-item {
      margin-bottom: 15px;
      padding: 10px 0;
      border-bottom: 1px dashed #d0d9e2; /* קו הפרדה עדין */
      display: flex; /* שימוש ב-flexbox לסידור לייבל וערך */
      justify-content: space-between; /* פיזור לייבל וערך לקצוות */
      align-items: center;
  }

   .result-item:last-of-type {
       border-bottom: none; /* הסרת קו הפרדה לאחרון */
       margin-bottom: 0;
   }


  .result-item label {
      font-weight: 600;
      color: #555;
      flex-grow: 1; /* מאפשר ללייבל לגדול */
      margin-inline-end: 15px; /* רווח בין הלייבל לערך */
  }

  .result-item .value {
      font-weight: 700;
      font-size: 1.2rem;
      color: #007bff; /* צבע הדגשה כללי */
  }

  .result-item .value.eroded {
      color: #28a745; /* צבע ירוק לערך הריאלי (מה שנשאר) */
  }

  .result-item .value.loss {
      color: #dc3545; /* צבע אדום להדגשת ההפסד */
      font-size: 1.3rem; /* גודל פונט גדול יותר להפסד */
  }

  .result-summary {
      margin-top: 20px;
      padding-top: 15px;
      border-top: 1px solid #c3dae8;
      font-size: 1.1rem;
      line-height: 1.6;
      color: #333;
  }

  .result-summary .bold {
      font-weight: 700;
      color: #004085;
  }


  /* כפתור הצגת/הסתרת הסבר */
  #toggle-explanation-btn {
    display: block;
    margin: 30px auto;
    padding: 12px 20px;
    background-color: #6c757d;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1.1rem;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
     font-weight: 600;
  }

  #toggle-explanation-btn:hover {
    background-color: #5a6268;
  }
   #toggle-explanation-btn:active {
    transform: scale(0.98);
  }

  /* אזור ההסבר */
  #explanation-section {
    max-width: 800px;
    margin: 30px auto;
    padding: 30px;
    border: 1px solid #c3dae8;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    display: none; /* מוסתר בהתחלה */
    line-height: 1.7; /* מרווח שורות נוח */
  }

  #explanation-section h2 {
    color: #0056b3;
    margin-bottom: 15px;
    font-size: 1.7rem;
    border-bottom: 2px solid #e9ecef;
    padding-bottom: 10px;
  }

  #explanation-section h3 {
    color: #004085;
    margin-top: 25px;
    margin-bottom: 10px;
    font-size: 1.4rem;
  }

  #explanation-section p {
    margin-bottom: 15px;
    color: #555;
  }

  #explanation-section strong {
    color: #000;
    font-weight: 700;
  }

  #explanation-section ul {
      margin-bottom: 15px;
      padding-inline-start: 20px; /* רווח לתבליטים */
  }

   #explanation-section li {
       margin-bottom: 8px;
       color: #555;
   }

   #explanation-section li strong {
       color: #333;
   }

</style>

<button id="toggle-explanation-btn">הצג/הסתר את סוד שחיקת כוח הקנייה</button>

<div id="explanation-section">
  <h2>הסבר מורחב: איך ומדוע הכסף שלכם "מתכווץ"?</h2>

  <h3>מהי אינפלציה? (הסבר פשוט)</h3>
  <p>בלי להיכנס לז'רגון כלכלי מסובך, <strong>אינפלציה</strong> היא פשוט תהליך שבו המחירים של רוב המוצרים והשירותים שאנחנו קונים עולים עם הזמן. חשבו על זה ככה: אם פעם יכולתם לקנות עם 10 ש"ח סלסלת עגבניות, ועם השנים אותה סלסלה עולה 12 ש"ח, אז ה-10 ש"ח שלכם שווים היום פחות מבחינת כמה עגבניות הם יכולים לקנות. זוהי שחיקת כוח קנייה, והאינפלציה היא הגורם העיקרי לה.</p>

  <h3>איך מודדים את התופעה? (מדד המחירים לצרכן)</h3>
  <p>כדי לדעת בכמה המחירים עלו, יש לנו כלי שנקרא <strong>מדד המחירים לצרכן</strong>. זהו בעצם סל קניות "ממוצע" של משפחה ישראלית (שכולל הכל מדיור ותחבורה ועד מזון וביגוד). הלשכה המרכזית לסטטיסטיקה (למ"ס) עוקבת אחרי המחירים של הפריטים בסל הזה מדי חודש, והשינוי באחוזים במחיר הכולל של הסל הוא שיעור האינפלציה. המספרים שמתפרסמים הם מדד חשוב לכלכלת המדינה ולכיס שלכם.</p>

  <h3>הקשר הישיר: אינפלציה = פגיעה בכוח הקנייה</h3>
  <p>כשמדד המחירים לצרכן עולה (כלומר, יש אינפלציה), ה-100 ש"ח שיש לכם בכיס או בבנק יכולים לקנות פחות פריטים מאשר בעבר. זה לא שהשטר של 100 ש"ח השתנה, אלא שהמוצרים שמסביב התייקרו. היכולת של הכסף שלכם "לקנות" דברים יורדת – זו בדיוק <strong>שחיקת כוח הקנייה</strong>. אינפלציה גבוהה היא כמו תולעת שנוגסת בערך של הכסף שלכם בקצב מהיר יותר.</p>

  <h3>דוגמה מהחיים (עם מספרים):</h3>
  <p>נניח לפני 10 שנים חסכתם 10,000 ש"ח. אם במהלך העשור הזה האינפלציה הממוצעת הייתה 3% לשנה, זה אומר שהמחירים עלו בסך הכל בכ-34.4% (זה חישוב מורכב של ריבית דריבית על המחירים). כדי לקנות היום את מה שיכולתם לקנות אז ב-10,000 ש"ח, הייתם צריכים היום כ-13,440 ש"ח! 10,000 השקלים ששמורים לכם בצד שווים היום מבחינת כוח קנייה רק כ-7,440 ש"ח (10,000 חלקי 1.344). הפסדתם 2,560 ש"ח מכוח הקנייה המקורי, פשוט כי הכסף ישב ללא תזוזה ריאלית.</p>

  <h3>מי מרגיש את זה הכי הרבה?</h3>
  <p>שחיקת כוח הקנייה פוגעת במיוחד בקבוצות הבאות:</p>
  <ul>
    <li><strong>אנשים שחוסכים "מתחת לבלטות" או בחשבון עו"ש:</strong> כסף שאינו מושקע או צמוד למדד מאבד מערכו הכי מהר.</li>
    <li><strong>בעלי שכר קבוע:</strong> אם המשכורת שלכם לא עולה בקצב לפחות כמו האינפלציה, בפועל כוח הקנייה שלכם יורד ואתם יכולים לקנות פחות עם אותה משכורת.</li>
    <li><strong>פנסיונרים עם קצבאות לא צמודות:</strong> ערך הפנסיה עלול להישחק משמעותית לאורך שנים רבות של פרישה.</li>
    <li><strong>מי שמלווה כסף בריבית קבועה נמוכה מהאינפלציה:</strong> הכסף שמקבלים בחזרה שווה פחות ממה שהושקע.</li>
  </ul>

  <h3>אז מה אפשר לעשות? (כלים להתמודדות)</h3>
  <p>אי אפשר לבטל את האינפלציה, אבל אפשר להתמודד איתה:</p>
  <ul>
    <li>**השקעה:** השקעת הכסף בנכסים כמו מניות, נדל"ן, או קרנות נאמנות, שיש להם פוטנציאל לגדול בקצב גבוה מהאינפלציה.</li>
    <li>**חסכונות צמודים למדד:** קיימים פיקדונות ותוכניות חיסכון בבנקים ובתי השקעות שהתשואה שלהם צמודה למדד המחירים לצרכן, לפעמים בתוספת ריבית קטנה, ושומרים על ערך הכסף.</li>
    <li>**הצמדה בחוזים:** בונוסים, שכר דירה, או חוזים אחרים שכוללים מנגנון הצמדה למדד כדי לשמור על ערכם הריאלי.</li>
  </ul>

  <h3>למה כל זה חשוב לכם?</h3>
  <p>הבנת השפעת האינפלציה היא אבן יסוד לתכנון פיננסי נכון. היא מבהירה מדוע חשוב לא להשאיר סכומים גדולים בעו"ש לאורך זמן, מעודדת לחשוב על השקעות מושכלות או מסלולי חיסכון שמגנים על ערך הכסף, ומאפשרת לכם לשמור על עתיד פיננסי יציב יותר.</p>
</div>

<script>
  document.getElementById('calculate-btn').addEventListener('click', function() {
    const initialAmount = parseFloat(document.getElementById('initial-amount').value);
    const numberOfYears = parseInt(document.getElementById('number-of-years').value);
    const inflationRate = parseFloat(document.getElementById('inflation-rate').value) / 100;
    const resultArea = document.getElementById('result-area');

    // Input validation with improved message
    if (isNaN(initialAmount) || initialAmount <= 0) {
        alert('אנא הכנס סכום כסף התחלתי חוקי וחיובי.');
        return;
    }
     if (isNaN(numberOfYears) || numberOfYears <= 0 || numberOfYears > 50) {
        alert('אנא הכנס מספר שנים חוקי בין 1 ל-50.');
        return;
    }
     if (isNaN(inflationRate) || inflationRate < 0) {
        alert('אנא הכנס שיעור אינפלציה חוקי (0 או יותר).');
        return;
    }


    // Disable button and indicate processing
    const calculateBtn = document.getElementById('calculate-btn');
    calculateBtn.disabled = true;
    calculateBtn.innerText = 'מחשב...';
    resultArea.style.opacity = 0; // Start fade out for previous results

    // Small delay to allow button state change and visual reset before calculation
    setTimeout(() => {
        // Calculate the cumulative inflation factor
        // Formula: (1 + rate)^years
        const cumulativeInflationFactor = Math.pow(1 + inflationRate, numberOfYears);

        // Calculate the real value after inflation
        // Real Value = Initial Amount / Cumulative Inflation Factor
        const erodedValue = initialAmount / cumulativeInflationFactor;

        // Calculate the erosion amount
        const erosionAmount = initialAmount - erodedValue;

        // Calculate the erosion percentage
        // Percentage = (Erosion Amount / Initial Amount) * 100
        const erosionPercentage = (erosionAmount / initialAmount) * 100;

        // --- Display Results ---
        // Show the result area if it was hidden
        resultArea.style.display = 'block';

        // Populate individual result items
        document.getElementById('initial-value-display').innerText = `${initialAmount.toLocaleString('he-IL', { minimumFractionDigits: 0, maximumFractionDigits: 2 })} ₪`;
        document.getElementById('years-display').innerText = numberOfYears;
        document.getElementById('eroded-value-display').innerText = `${erodedValue.toLocaleString('he-IL', { minimumFractionDigits: 0, maximumFractionDigits: 2 })} ₪`;
        document.getElementById('erosion-amount-display').innerText = `${erosionAmount.toLocaleString('he-IL', { minimumFractionDigits: 0, maximumFractionDigits: 2 })} ₪`;
        document.getElementById('erosion-percentage-display').innerText = `${erosionPercentage.toFixed(2)}%`;

        // Populate summary text
        document.getElementById('summary-initial').innerText = initialAmount.toLocaleString('he-IL', { minimumFractionDigits: 0, maximumFractionDigits: 2 });
         document.getElementById('summary-years').innerText = numberOfYears;
         document.getElementById('summary-inflation').innerText = (inflationRate * 100).toFixed(1);
         document.getElementById('summary-eroded').innerText = erodedValue.toLocaleString('he-IL', { minimumFractionDigits: 0, maximumFractionDigits: 2 });
         document.getElementById('summary-loss-amount').innerText = erosionAmount.toLocaleString('he-IL', { minimumFractionDigits: 0, maximumFractionDigits: 2 });
         document.getElementById('summary-loss-percentage').innerText = erosionPercentage.toFixed(2);


        // Trigger fade-in animation
        resultArea.style.opacity = 1;
        resultArea.style.transform = 'translateY(0)';


        // Re-enable button and reset text after results displayed
         calculateBtn.disabled = false;
         calculateBtn.innerText = 'חשב את "ההתאדות" של הכסף';

    }, 100); // Short delay


  });

  // Initially hide the result area
  document.getElementById('result-area').style.display = 'none';


  // Toggle explanation section visibility
  document.getElementById('toggle-explanation-btn').addEventListener('click', function() {
    const explanationSection = document.getElementById('explanation-section');
    const button = this; // Reference to the button itself
    const isHidden = explanationSection.style.display === 'none' || explanationSection.style.display === '';

    if (isHidden) {
      explanationSection.style.display = 'block';
      // Optional: Change button text
      // button.innerText = 'הסתר הסבר על שחיקת כוח קנייה';
    } else {
      explanationSection.style.display = 'none';
       // Optional: Change button text
       // button.innerText = 'הצג הסבר על שחיקת כוח קנייה';
    }
  });

   // Add event listeners for input changes to provide live feedback or clear results?
   // For this simple example, maybe clear results area on any input change.
    const inputs = document.querySelectorAll('#simulator-app input');
    inputs.forEach(input => {
        input.addEventListener('input', () => {
            const resultArea = document.getElementById('result-area');
            // resultArea.style.display = 'none'; // Hide completely
            resultArea.style.opacity = 0; // Just fade out
             resultArea.style.transform = 'translateY(20px)';
        });
    });


</script>
```