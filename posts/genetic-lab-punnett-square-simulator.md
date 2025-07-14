---
title: "מעבדה גנטית: סימולטור ריבוע פאנט"
english_slug: genetic-lab-punnett-square-simulator
category: "ביולוגיה"
tags:
  - גנטיקה
  - תורשה
  - ריבוע פאנט
  - הכלאה גנטית
  - אללים
  - סימולציה
---
# מעבדה גנטית: ריבוע פאנט בפעולה

צאו למסע מרתק אל תוך עולם התורשה! איך תכונות עוברות מהורים לצאצאים? האם צבע העיניים שלכם או גובה צמח האפונה בגינה שלכם הם תוצאה של מקריות גרידא? ממש לא! הכירו את ריבוע פאנט - כלי ויזואלי פשוט אך עוצמתי שיאפשר לכם לחזות את הסיכויים לקבלת תכונות מסוימות בדור הבא. התנסו בסימולטור שלנו וגלו את חוקי המשחק הגנטי!

<div class="punnett-simulator">
  <h2>הכלאה גנטית: סימולטור אינטראקטיבי</h2>
  <div class="trait-info">
    <h3>מתמקדים בתכונה: צבע פרח בצמח אפונה</h3>
    <p>האללים ששולטים בתכונה:</p>
    <ul>
        <li><span class="allele-dominant">P</span> (<span class="allele-dominant">סגול</span> - אלל דומיננטי)</li>
        <li><span class="allele-recessive">p</span> (<span class="allele-recessive">לבן</span> - אלל רצסיבי)</li>
    </ul>
    <p>האלל הדומיננטי (<span class="allele-dominant">P</span>) יבוא לידי ביטוי בפנוטיפ (הצבע הנראה לעין) גם בנוכחות עותק אחד בלבד. האלל הרצסיבי (<span class="allele-recessive">p</span>) יבוא לידי ביטוי רק אם שני האללים הם רצסיביים.</p>
  </div>

  <div class="parent-selection">
    <div class="parent">
      <h4>הורה 1 <span class="parent-icon">♀️</span></h4>
      <select id="parent1-genotype" class="genotype-select">
        <option value="PP">PP (הומוזיגוט דומיננטי)</option>
        <option value="Pp">Pp (הטרוזיגוט)</option>
        <option value="pp">pp (הומוזיגוט רצסיבי)</option>
      </select>
    </div>
    <div class="parent">
      <h4>הורה 2 <span class="parent-icon">♂️</span></h4>
      <select id="parent2-genotype" class="genotype-select">
        <option value="PP">PP (הומוזיגוט דומיננטי)</option>
        <option value="Pp" selected>Pp (הטרוזיגוט)</option>
        <option value="pp">pp (הומוזיגוט רצסיבי)</option>
      </select>
    </div>
  </div>

  <div class="punnett-square-container">
    <table id="punnett-square-table">
      <thead>
        <tr>
          <th></th>
          <th id="parent2-gamete1" class="gamete-cell"></th>
          <th id="parent2-gamete2" class="gamete-cell"></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th id="parent1-gamete1" class="gamete-cell"></th>
          <td class="offspring-genotype"></td>
          <td class="offspring-genotype"></td>
        </tr>
        <tr>
          <th id="parent1-gamete2" class="gamete-cell"></th>
          <td class="offspring-genotype"></td>
          <td class="offspring-genotype"></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="results">
    <h3>ניתוח הצאצאים הפוטנציאליים:</h3>
    <div class="genotype-ratios">
      <h4>יחסי גנוטיפים:</h4>
      <p id="genotype-PP"><span class="allele-dominant">PP</span>: <span class="ratio"></span> (<span class="percent"></span>%)</p>
      <p id="genotype-Pp"><span class="allele-dominant">P</span><span class="allele-recessive">p</span>: <span class="ratio"></span> (<span class="percent"></span>%)</p>
      <p id="genotype-pp_lower"><span class="allele-recessive">pp</span>: <span class="ratio"></span> (<span class="percent"></span>%)</p>
    </div>
    <div class="phenotype-ratios">
      <h4>יחסי פנוטיפים:</h4>
      <p id="phenotype-dominant"><span class="allele-dominant">פרח סגול</span> (PP, Pp): <span class="ratio"></span> (<span class="percent"></span>%)</p>
      <p id="phenotype-recessive"><span class="allele-recessive">פרח לבן</span> (pp): <span class="ratio"></span> (<span class="percent"></span>%)</p>
    </div>
  </div>
</div>

<button id="toggle-explanation" class="toggle-button">רוצים להבין לעומק? לחצו כאן להסבר על ריבוע פאנט</button>

<div id="explanation" class="explanation" style="display: none;">
  <h2>מהו ריבוע פאנט ולשם מה הוא משמש?</h2>
  <p>ריבוע פאנט הוא כלי גרפי פשוט המאפשר לחזות את כל שילובי האללים האפשריים בצאצאים של הכלאה גנטית נתונה, וכפועל יוצא מכך, לחשב את הסיכויים לקבלת גנוטיפים ופנוטיפים מסוימים. הוא נקרא על שם המדען הבריטי רג'ינלד פאנט, והוא למעשה הדמיה של <a href="#mendel-laws">חוק ההפרדה של מנדל</a>.</p>

  <h3>מושגי יסוד בגנטיקה שכדאי להכיר:</h3>
  <ul>
    <li><strong>גן:</strong> יחידת התורשה הבסיסית, מקטע של DNA שנושא מידע ליצירת חלבון או מולקולה תפקודית אחרת, וקובע תכונה מסוימת (למשל, הגן לצבע פרח).</li>
    <li><strong>אללים:</strong> גרסאות שונות לאותו גן. לכל גן יכולים להיות אללים שונים (לדוגמה, אלל לצבע פרח סגול ואלל לצבע פרח לבן). לרוב האורגניזמים הדיפלואידים (כמונו) יש שני עותקים מכל גן, אחד מכל הורה.</li>
    <li><strong>אלל דומיננטי:</strong> אלל שתמיד מבטא את הפנוטיפ (התכונה החיצונית הנראית לעין) שלו, גם כשיש לו רק עותק אחד (כלומר, כשהאורגניזם הטרוזיגוט). מסומן בדרך כלל באות גדולה (כמו P).</li>
    <li><strong>אלל רצסיבי:</strong> אלל שמבטא את הפנוטיפ שלו רק כשיש לו שני עותקים (כלומר, כשהאורגניזם הומוזיגוט רצסיבי). נוכחות של אלל דומיננטי תסתיר את הפנוטיפ הרצסיבי. מסומן באות קטנה (כמו p).</li>
    <li><strong>גנוטיפ:</strong> ההרכב הגנטי המדויק של האורגניזם עבור גן מסוים או קבוצת גנים. זהו זוג האללים שיש לאורגניזם (לדוגמה, PP, Pp, או pp).</li>
    <li><strong>פנוטיפ:</strong> הביטוי החיצוני של התכונה, הנובע מהגנוטיפ ומהשפעות סביבתיות. זה מה שאנחנו רואים בפועל (לדוגמה, פרח סגול או לבן).</li>
    <li><strong>הומוזיגוט:</strong> אורגניזם שיש לו שני עותקים זהים של אותו אלל עבור גן מסוים (PP או pp).</li>
    <li><strong>הטרוזיגוט:</strong> אורגניזם שיש לו שני עותקים שונים של האללים עבור גן מסוים (Pp).</li>
  </ul>

  <h3>כיצד בונים ומנתחים ריבוע פאנט?</h3>
  <p>ניקח שוב את הדוגמה של צבע פרח בצמח אפונה (P=סגול, p=לבן), ונבחן הכלאה בין שני הורים הטרוזיגוטים: Pp x Pp.</p>
  <ol>
    <li><strong>זיהוי גנוטיפי ההורים:</strong> במקרה זה, שני ההורים הם Pp.</li>
    <li><strong>קביעת סוגי הגמטות (תאי מין) האפשריים:</strong> לפי חוק ההפרדה של מנדל, כל הורה תורם רק אלל אחד מתוך הזוג לכל גמטה. הורה בעל גנוטיפ Pp יכול לייצר גמטות הנושאות את האלל P (בסיכוי 50%) וגמטות הנושאות את האלל p (בסיכוי 50%).</li>
    <li><strong>בניית הריבוע:</strong> יוצרים טבלה (2x2 עבור הכלאה של תכונה אחת). בצד העליון רושמים את סוגי הגמטות של הורה אחד, ובצד השמאלי רושמים את סוגי הגמטות של ההורה השני.
      <pre dir="ltr">
          |   P   |   p
        -----------------
        P |       |
        -----------------
        p |       |
      </pre>
    </li>
    <li><strong>מילוי הריבוע:</strong> כל תא בריבוע מייצג שילוב אפשרי של גמטה מהורה אחד וגמטה מההורה השני. ממלאים כל תא על ידי צירוף האללים מהכותרות של השורה והטור המתאימים. כל תא מציג גנוטיפ אפשרי של צאצא.
      <pre dir="ltr">
          |   P   |   p
        -----------------
        P |  PP   |  Pp
        -----------------
        p |  Pp   |  pp
      </pre>
      (שימו לב: Pp ו-pP מייצגים את אותו גנוטיפ הטרוזיגוטי, ולרוב רושמים Pp לפי סדר האלל הדומיננטי תחילה).
    </li>
  </ol>

  <h3>פענוח התוצאות (ניתוח הריבוע):</h3>
  <p>לאחר מילוי הריבוע, קל לחשב את הסיכויים:</p>
  <ul>
    <li><strong>יחסי גנוטיפים:</strong> סופרים את התאים המכילים כל גנוטיפ אפשרי (PP, Pp, pp) מתוך סך התאים (4 במקרה זה). בריבוע זה: 1 PP, 2 Pp, 1 pp. יחס גנוטיפים: 1:2:1. באחוזים: 25% PP, 50% Pp, 25% pp.</li>
    <li><strong>יחסי פנוטיפים:</strong> קובעים את הפנוטיפ של כל גנוטיפ על פי כללי הדומיננטיות.
      <ul>
        <li>PP: סגול (הומוזיגוט דומיננטי)</li>
        <li>Pp: סגול (הטרוזיגוט - האלל P דומיננטי ומכסה על p)</li>
        <li>pp: לבן (הומוזיגוט רצסיבי - רק כך האלל p בא לידי ביטוי)</li>
      </ul>
      סופרים את התאים המובילים לכל פנוטיפ. בדוגמה זו: 3 תאים מובילים לפנוטיפ "סגול" (PP ו-Pp) ותא 1 מוביל לפנוטיפ "לבן" (pp). יחס פנוטיפים: 3 סגול : 1 לבן. באחוזים: 75% סגול, 25% לבן.
    </ul>

  <h3 id="mendel-laws">חיבור לחוקי מנדל:</h3>
  <p>ריבוע פאנט הוא הדמיה יפהפייה של <strong>חוק ההפרדה (חוק המיון)</strong> של גרגור מנדל. חוק זה קובע שזוג האללים עבור כל תכונה נפרד במהלך היווצרות הגמטות (כך שכל גמטה נושאת רק אלל אחד). במהלך ההפריה, הגמטות מהורים שונים מתאחדות באופן אקראי ליצירת הגנוטיפ הדיפלואידי של הצאצא. ריבוע פאנט מציג את כל השילובים האפשריים של הגמטות ומה הסיכויים לכל שילוב כזה.</p>

  <h3>התנסו ולמדו!</h3>
  <p>חזרו לסימולטור למעלה ושנו את הגנוטיפים של הורי צמח האפונה. צפו כיצד סוגי הגמטות, הגנוטיפים בצאצאים, ויחסי הגנוטיפים והפנוטיפים משתנים בהתאם. נסו את כל השילובים האפשריים (PP x PP, PP x Pp, PP x pp, Pp x Pp, Pp x pp, pp x pp) כדי לראות את כל התרחישים האפשריים ולחזק את הבנתכם את עקרונות התורשה הבסיסיים!</p>
</div>

<style>
  /* General styling for the simulator container */
  .punnett-simulator {
    font-family: 'Arial', sans-serif;
    direction: rtl;
    text-align: right;
    background-color: #e8f5e9; /* Light green background */
    border: 1px solid #c8e6c9; /* Matching border color */
    border-radius: 12px; /* More rounded corners */
    padding: 25px;
    margin-bottom: 30px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
  }

  .punnett-simulator h2 {
      color: #2e7d32; /* Dark green */
      text-align: center;
      margin-bottom: 20px;
      font-size: 1.8rem;
      border-bottom: 2px solid #a5d6a7;
      padding-bottom: 10px;
  }

  .punnett-simulator h3 {
    color: #388e3c; /* Medium green */
    margin-top: 15px;
    margin-bottom: 12px;
    font-size: 1.4rem;
  }

   .punnett-simulator h4 {
    color: #4caf50; /* Green */
    margin-bottom: 8px;
    font-size: 1.1rem;
  }

  .trait-info {
    margin-bottom: 25px;
    padding-bottom: 20px;
    border-bottom: 1px solid #c8e6c9;
  }

  .trait-info p, .trait-info ul {
      margin-bottom: 10px;
      line-height: 1.5;
  }
   .trait-info ul {
       list-style: none;
       padding: 0;
   }
   .trait-info li {
       margin-bottom: 5px;
       padding-right: 15px;
       position: relative;
   }
   .trait-info li::before {
       content: '🌱'; /* Pea plant icon */
       position: absolute;
       right: 0;
       color: #4caf50;
   }


  /* Allele coloring and styling */
  .allele-dominant {
    font-weight: bold;
    color: #9c27b0; /* Purple, matching pea flower */
  }

  .allele-recessive {
    font-weight: bold;
    color: #5c6bc0; /* Indigo/Blue, distinct from dominant */
  }

  /* Parent Selection */
  .parent-selection {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-bottom: 30px;
    flex-wrap: wrap;
  }

  .parent {
    text-align: center;
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 15px 20px;
    margin: 10px;
    flex: 1; /* Allow parents to grow/shrink */
    min-width: 200px; /* Minimum width */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
  }

  .parent-icon {
      font-size: 1.5rem;
      vertical-align: middle;
      margin-left: 5px;
  }

  .genotype-select {
    padding: 10px 15px;
    font-size: 1.1rem;
    border-radius: 6px;
    border: 1px solid #ccc;
    cursor: pointer;
    outline: none;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
  }

  .genotype-select:focus {
      border-color: #4caf50;
      box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
  }

  /* Punnett Square */
  .punnett-square-container {
    display: flex;
    justify-content: center;
    margin-bottom: 30px;
  }

  #punnett-square-table {
    border-collapse: collapse;
    width: 250px; /* Larger size for better visibility */
    height: 250px;
    font-size: 1.3rem;
    text-align: center;
    table-layout: fixed;
    background-color: #ffffff;
    border: 2px solid #4caf50; /* Stronger border */
  }

  #punnett-square-table th, #punnett-square-table td {
    border: 1px solid #a5d6a7; /* Lighter border inside */
    padding: 10px;
    width: 25%;
    height: 25%;
  }

  #punnett-square-table th {
    background-color: #e0f2f7; /* Light blue-green for headers */
    font-weight: bold;
    color: #0277bd; /* Dark blue for header text */
  }

  .gamete-cell {
      font-size: 1.5rem;
      /* Initial state for animation */
      opacity: 0;
      transform: translateY(-10px); /* Start slightly up */
  }

   .gamete-cell.animate-in {
       animation: fadeInSlideDown 0.5s ease-out forwards;
   }

   @keyframes fadeInSlideDown {
       from { opacity: 0; transform: translateY(-10px); }
       to { opacity: 1; transform: translateY(0); }
   }


  .offspring-genotype {
    font-weight: bold;
    color: #3f51b5; /* Indigo color for offspring */
    font-size: 1.4rem;
    /* Initial state for animation */
    opacity: 0;
    transform: scale(0.8);
  }

  .offspring-genotype.animate-in {
      animation: fadeInScale 0.5s ease-out forwards;
  }

  @keyframes fadeInScale {
      from { opacity: 0; transform: scale(0.8); }
      to { opacity: 1; transform: scale(1); }
  }


  /* Results Section */
  .results {
    margin-top: 25px;
    padding-top: 20px;
    border-top: 1px solid #c8e6c9;
    display: flex;
    flex-wrap: wrap;
    gap: 20px; /* Space between genotype and phenotype blocks */
    justify-content: center;
  }

  .genotype-ratios, .phenotype-ratios {
      background-color: #ffffff;
      border: 1px solid #e0e0e0;
      border-radius: 8px;
      padding: 15px;
      flex: 1; /* Allow to grow/shrink */
      min-width: 250px; /* Minimum width */
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
  }

  .results h4 {
    margin-bottom: 10px;
    color: #555;
    border-bottom: 1px dotted #ccc;
    padding-bottom: 5px;
  }

  .genotype-ratios p, .phenotype-ratios p {
    margin-bottom: 8px;
    font-size: 1.1rem;
  }

  .ratio, .percent {
    font-weight: bold;
    color: #0d47a1; /* Dark blue for numbers */
    font-size: 1.2rem; /* Larger numbers */
     /* Initial state for animation */
    opacity: 0;
    transform: translateY(5px);
  }

  .ratio.animate-in, .percent.animate-in {
      animation: fadeInSlideUp 0.5s ease-out forwards;
  }

    @keyframes fadeInSlideUp {
       from { opacity: 0; transform: translateY(5px); }
       to { opacity: 1; transform: translateY(0); }
   }


  /* Explanation Section */
  .toggle-button {
    display: block;
    width: fit-content;
    margin: 20px auto;
    padding: 12px 25px;
    font-size: 1.1rem;
    cursor: pointer;
    background-color: #0288d1; /* Light blue */
    color: white;
    border: none;
    border-radius: 6px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  }

  .toggle-button:hover {
    background-color: #0277bd; /* Darker blue on hover */
    transform: translateY(-1px); /* Slight lift effect */
  }

    .toggle-button:active {
    background-color: #01579b; /* Even darker on click */
     transform: translateY(0);
  }


  .explanation {
    background-color: #e3f2fd; /* Lighter blue */
    border: 1px solid #bbdefb; /* Matching border */
    border-radius: 12px;
    padding: 25px;
    margin-top: 30px;
    line-height: 1.7;
    direction: rtl;
    text-align: right;
    color: #333;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .explanation h2 {
      color: #0d47a1; /* Dark blue */
      margin-bottom: 20px;
      border-bottom: 2px solid #90caf9;
      padding-bottom: 10px;
       font-size: 1.6rem;
  }
   .explanation h3 {
      color: #1565c0; /* Medium blue */
      margin-bottom: 15px;
      margin-top: 25px;
       font-size: 1.3rem;
  }

  .explanation ul, .explanation ol {
    margin-bottom: 20px;
    padding-right: 25px; /* Adjusted padding */
  }

  .explanation li {
      margin-bottom: 10px;
      line-height: 1.6;
  }

  .explanation li strong {
      color: #0d47a1; /* Match heading color */
  }

  .explanation a {
      color: #0277bd;
      text-decoration: none;
      border-bottom: 1px dotted #0277bd;
      transition: color 0.3s ease, border-bottom-color 0.3s ease;
  }

  .explanation a:hover {
      color: #01579b;
      border-bottom-color: #01579b;
  }

  .explanation pre {
      background-color: #e1f5fe; /* Very light blue */
      border: 1px solid #b3e5fc;
      border-radius: 6px;
      padding: 15px;
      overflow-x: auto;
      margin: 20px 0;
      direction: ltr; /* Code direction */
      text-align: left; /* Code direction */
      font-family: 'Courier New', Courier, monospace;
      font-size: 0.95rem;
      line-height: 1.4;
      color: #333;
  }


  /* Responsive adjustments */
  @media (max-width: 768px) {
      .punnett-simulator {
          padding: 20px;
      }
      .punnett-simulator h2 {
          font-size: 1.5rem;
      }
       .punnett-simulator h3 {
           font-size: 1.2rem;
       }
       .punnett-simulator h4 {
           font-size: 1rem;
       }
      .parent-selection {
          flex-direction: column;
          align-items: stretch; /* Stretch parents to fill width */
      }
       .parent {
           margin: 8px 0; /* Adjust margin for column layout */
           min-width: unset; /* Remove min-width */
       }

      #punnett-square-table {
          width: 200px; /* Smaller size for smaller screens */
          height: 200px;
          font-size: 1rem;
      }

      #punnett-square-table th, #punnett-square-table td {
          padding: 8px;
      }

      .gamete-cell {
          font-size: 1.2rem;
      }
       .offspring-genotype {
           font-size: 1.1rem;
       }

      .results {
          flex-direction: column; /* Stack results vertically */
          gap: 15px;
      }

       .genotype-ratios, .phenotype-ratios {
           min-width: unset; /* Remove min-width */
       }

      .toggle-button {
        font-size: 1rem;
        padding: 10px 20px;
      }
      .explanation {
          padding: 20px;
      }
      .explanation h2 {
           font-size: 1.4rem;
      }
      .explanation h3 {
           font-size: 1.1rem;
      }
      .explanation pre {
          font-size: 0.9rem;
          padding: 10px;
      }
  }
   @media (max-width: 480px) {
       #punnett-square-table {
           width: 160px;
           height: 160px;
            font-size: 0.9rem;
       }
        .gamete-cell {
          font-size: 1rem;
      }
       .offspring-genotype {
           font-size: 1rem;
       }
       .results p {
           font-size: 1rem;
       }
       .ratio, .percent {
           font-size: 1.1rem;
       }
   }
</style>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const parent1Select = document.getElementById('parent1-genotype');
    const parent2Select = document.getElementById('parent2-genotype');
    const punnettTable = document.getElementById('punnett-square-table');

    const gameteCells = punnettTable.querySelectorAll('.gamete-cell');
    const offspringCells = punnettTable.querySelectorAll('.offspring-genotype');

    const genotypeRatiosDiv = document.querySelector('.genotype-ratios');
    const phenotypeRatiosDiv = document.querySelector('.phenotype-ratios');
    const ratioElements = document.querySelectorAll('.results .ratio, .results .percent');


    const toggleButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Define traits and their alleles/phenotypes
    const traitData = {
      'flower-color': {
        alleles: { dominant: 'P', recessive: 'p' },
        phenotypes: {
          'PP': 'סגול',
          'Pp': 'סגול',
          'pp': 'לבן'
        }
      }
    };

    // Currently using only one trait
    const currentTrait = 'flower-color';
    const alleles = traitData[currentTrait].alleles;
    const phenotypes = traitData[currentTrait].phenotypes;
    const dominantAllele = alleles.dominant;
    const recessiveAllele = alleles.recessive;

    // Map genotype strings to gamete arrays
    function getGametes(genotype) {
      if (genotype === dominantAllele + dominantAllele) {
        return [dominantAllele, dominantAllele];
      } else if (genotype === recessiveAllele + recessiveAllele) {
        return [recessiveAllele, recessiveAllele];
      } else { // Assumes heterozygous is dominant + recessive
        return [dominantAllele, recessiveAllele];
      }
    }

    function resetAnimations() {
        // Remove animation classes from previous run
        gameteCells.forEach(cell => cell.classList.remove('animate-in'));
        offspringCells.forEach(cell => cell.classList.remove('animate-in'));
        ratioElements.forEach(el => el.classList.remove('animate-in'));

         // Clear previous content
        gameteCells.forEach(cell => cell.textContent = '');
        offspringCells.forEach(cell => cell.textContent = '');
         ratioElements.forEach(el => el.textContent = '');
    }

    function calculateAndAnimatePunnettSquare() {
      resetAnimations(); // Start clean

      const parent1Genotype = parent1Select.value;
      const parent2Genotype = parent2Select.value;

      const parent1Gametes = getGametes(parent1Genotype);
      const parent2Gametes = getGametes(parent2Genotype);

      // Gamete Animation Sequence
      const parent1Gamete1Cell = document.getElementById('parent1-gamete1');
      const parent1Gamete2Cell = document.getElementById('parent1-gamete2');
      const parent2Gamete1Cell = document.getElementById('parent2-gamete1');
      const parent2Gamete2Cell = document.getElementById('parent2-gamete2');

      // Animate parent 1 gametes
      setTimeout(() => { parent1Gamete1Cell.textContent = parent1Gametes[0]; parent1Gamete1Cell.classList.add('animate-in'); }, 200);
      setTimeout(() => { parent1Gamete2Cell.textContent = parent1Gametes[1]; parent1Gamete2Cell.classList.add('animate-in'); }, 300);

      // Animate parent 2 gametes
      setTimeout(() => { parent2Gamete1Cell.textContent = parent2Gametes[0]; parent2Gamete1Cell.classList.add('animate-in'); }, 400);
      setTimeout(() => { parent2Gamete2Cell.textContent = parent2Gametes[1]; parent2Gamete2Cell.classList.add('animate-in'); }, 500);


      // Calculate offspring genotypes (needed before animating)
      const offspring = [
        parent1Gametes[0] + parent2Gametes[0],
        parent1Gametes[0] + parent2Gametes[1],
        parent1Gametes[1] + parent2Gametes[0],
        parent1Gametes[1] + parent2Gametes[1]
      ];

      // Normalize genotypes (e.g., pP -> Pp) - keeps Pp format consistent
      const normalizedOffspring = offspring.map(genotype => {
          // Handle pP -> Pp, but keep PP and pp as is
          if (genotype.length === 2 && genotype[0] === recessiveAllele && genotype[1] === dominantAllele) {
              return dominantAllele + recessiveAllele;
          }
           // Ensure homozygous recessive is always lowercase (pp)
           if (genotype.length === 2 && genotype[0] === dominantAllele && genotype[1] === recessiveAllele) {
               return dominantAllele + recessiveAllele; // Keep Pp
           }
            if (genotype.length === 2 && genotype[0] === recessiveAllele && genotype[1] === recessiveAllele) {
               return recessiveAllele + recessiveAllele; // Keep pp
           }
            if (genotype.length === 2 && genotype[0] === dominantAllele && genotype[1] === dominantAllele) {
               return dominantAllele + dominantAllele; // Keep PP
           }
          return genotype; // Should not happen for 2-allele traits
      });

      // Offspring Cell Animation Sequence
      const cellAnimationDelay = 150; // delay between each offspring cell
      const offspringAnimationStartTime = 800; // Start after gametes appear

      offspringCells.forEach((cell, index) => {
          setTimeout(() => {
              cell.textContent = normalizedOffspring[index];
              cell.classList.add('animate-in');
          }, offspringAnimationStartTime + index * cellAnimationDelay);
      });

      // Calculate and Animate Ratios after offspring animation finishes
      const totalOffspringAnimationTime = offspringAnimationStartTime + offspringCells.length * cellAnimationDelay;
      setTimeout(() => {
          calculateRatios(normalizedOffspring); // Calculate and update text content
          ratioElements.forEach(el => el.classList.add('animate-in')); // Animate the numbers
      }, totalOffspringAnimationTime + 300); // Small delay before ratio animation starts

    }

    function calculateRatios(offspringGenotypes) {
        const totalOffspring = offspringGenotypes.length;
        const genotypeCounts = {
            [dominantAllele + dominantAllele]: 0,
            [dominantAllele + recessiveAllele]: 0, // Ensure heterozygous is ordered correctly
            [recessiveAllele + recessiveAllele]: 0
        };

        offspringGenotypes.forEach(genotype => {
            genotypeCounts[genotype]++;
        });

        // Update text content *before* adding animation class in the timeout function
        genotypeRatiosDiv.querySelector(`#genotype-PP .ratio`).textContent = `${genotypeCounts[dominantAllele + dominantAllele]}/${totalOffspring}`;
        genotypeRatiosDiv.querySelector(`#genotype-PP .percent`).textContent = ((genotypeCounts[dominantAllele + dominantAllele] / totalOffspring) * 100).toFixed(0);

        genotypeRatiosDiv.querySelector(`#genotype-Pp .ratio`).textContent = `${genotypeCounts[dominantAllele + recessiveAllele]}/${totalOffspring}`;
        genotypeRatiosDiv.querySelector(`#genotype-Pp .percent`).textContent = ((genotypeCounts[dominantAllele + recessiveAllele] / totalOffspring) * 100).toFixed(0);

        genotypeRatiosDiv.querySelector(`#genotype-pp_lower .ratio`).textContent = `${genotypeCounts[recessiveAllele + recessiveAllele]}/${totalOffspring}`;
        genotypeRatiosDiv.querySelector(`#genotype-pp_lower .percent`).textContent = ((genotypeCounts[recessiveAllele + recessiveAllele] / totalOffspring) * 100).toFixed(0);


        // Phenotype Ratios
        const dominantPhenotypeCount = genotypeCounts[dominantAllele + dominantAllele] + genotypeCounts[dominantAllele + recessiveAllele];
        const recessivePhenotypeCount = genotypeCounts[recessiveAllele + recessiveAllele];

        phenotypeRatiosDiv.querySelector(`#phenotype-dominant .ratio`).textContent = `${dominantPhenotypeCount}/${totalOffspring}`;
        phenotypeRatiosDiv.querySelector(`#phenotype-dominant .percent`).textContent = ((dominantPhenotypeCount / totalOffspring) * 100).toFixed(0);

        phenotypeRatiosDiv.querySelector(`#phenotype-recessive .ratio`).textContent = `${recessivePhenotypeCount}/${totalOffspring}`;
        phenotypeRatiosDiv.querySelector(`#phenotype-recessive .percent`).textContent = ((recessivePhenotypeCount / totalOffspring) * 100).toFixed(0);
    }


    // Event listeners for genotype selection change
    parent1Select.addEventListener('change', calculateAndAnimatePunnettSquare);
    parent2Select.addEventListener('change', calculateAndAnimatePunnettSquare);

    // Initial calculation and animation on page load
    calculateAndAnimatePunnettSquare();

    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
      const isHidden = explanationDiv.style.display === 'none';
      explanationDiv.style.display = isHidden ? 'block' : 'none';
      toggleButton.textContent = isHidden ? 'הסתרת ההסבר' : 'רוצים להבין לעומק? לחצו כאן להסבר על ריבוע פאנט';
       // Optional: Scroll to the explanation if it's shown
       if (isHidden) {
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
       }
    });
  });
</script>
```