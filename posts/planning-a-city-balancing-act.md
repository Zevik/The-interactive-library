---
title: "מתכננים עיר: האם תצליחו לאזן בין הכל?"
english_slug: planning-a-city-balancing-act
category: "תכנון עירוני"
tags:
  - תכנון עירוני
  - איזון עירוני
  - שימושי קרקע
  - סימולציה
  - קיימות
  - אתגר
---
<h1>מתכננים עיר: האם תצליחו לאזן בין הכל?</h1>

<p>ברוכים הבאים לתפקיד המתכננים הראשיים! קיבלתם שטח ריק ואתם צריכים להחליט מה לבנות עליו. כל החלטה משפיעה על חיי התושבים, על כלכלת העיר ועל הסביבה. האם תתנו עדיפות לשכונות מגורים צפופות, אזורי תעשייה רווחיים או ריאות ירוקות חיוניות? נסו לבנות את העיר האולטימטיבית - אבל היזהרו, קל מאוד להפר את האיזון העדין!</p>

<div id="city-simulation">
  <div class="controls">
    <div class="area-info">
      <h2>שטח זמין: <span id="available-area">100</span></h2>
      <div class="area-bar-container"><div id="used-area-bar" class="area-bar"></div></div>
    </div>
    <p class="prompt">בחרו מה לבנות:</p>
    <div class="button-group">
      <button data-type="residential" class="selected"><i class="icon fas fa-home"></i> מגורים</button>
      <button data-type="industrial"><i class="icon fas fa-factory"></i> תעשייה</button>
      <button data-type="green"><i class="icon fas fa-tree"></i> שטח ירוק</button>
    </div>
    <button data-type="clear" class="clear-button"><i class="icon fas fa-eraser"></i> ניקוי משבצת</button>

    <div class="metrics">
      <h3><i class="icon fas fa-chart-line"></i> מדדים עירוניים:</h3>
      <div class="metric-item">
        <label>פוטנציאל תושבים:</label>
        <span id="metric-residents">0</span>
        <div class="metric-bar-container"><div id="residents-bar" class="metric-bar"></div></div>
      </div>
      <div class="metric-item">
        <label>הכנסות (משוער):</label>
        <span id="metric-income">0</span>
        <div class="metric-bar-container"><div id="income-bar" class="metric-bar"></div></div>
      </div>
      <div class="metric-item">
        <label>רמת זיהום:</label>
        <span id="metric-pollution">0</span>%
         <div class="metric-bar-container pollution"><div id="pollution-bar" class="metric-bar"></div></div>
      </div>
       <div class="metric-item">
        <label>שביעות רצון:</label>
        <span id="metric-satisfaction">50</span>%
        <div class="metric-bar-container satisfaction"><div id="satisfaction-bar" class="metric-bar"></div></div>
      </div>
    </div>

    <div class="legend">
        <h4>מקרא</h4>
        <ul>
            <li><span class="legend-color residential"></span> מגורים</li>
            <li><span class="legend-color industrial"></span> תעשייה</li>
            <li><span class="legend-color green"></span> שטח ירוק</li>
        </ul>
    </div>

  </div>
  <div id="city-grid" class="grid">
    <!-- Grid cells will be generated here by JS -->
  </div>
</div>

<style>
  /* Adding FontAwesome for icons - assumes it's available in the environment */
  /* If not, these styles can be removed or replaced with image icons */
  @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');


  #city-simulation {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* More modern font stack */
    display: flex;
    flex-direction: column;
    gap: 30px; /* Increased gap */
    margin: 25px auto; /* Centered block */
    padding: 25px;
    border: none; /* Remove default border */
    border-radius: 12px;
    background: linear-gradient(to bottom right, #eef2f7, #c4d7eb); /* Soft gradient background */
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    max-width: 900px; /* Limit max width */
    align-items: center;
  }

  .controls {
    text-align: center;
    background-color: #ffffff; /* White background for controls */
    padding: 25px;
    border-radius: 10px;
    width: 100%;
    max-width: 600px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
  }

  .area-info {
      margin-bottom: 20px;
      padding-bottom: 15px;
      border-bottom: 1px dashed #ddd;
  }

   .area-info h2 {
       margin: 0 0 10px 0;
       color: #0056b3;
       font-size: 1.5em;
   }

   .area-bar-container {
       width: 100%;
       height: 8px;
       background-color: #e0e0e0;
       border-radius: 4px;
       overflow: hidden; /* Hide overflowing bar */
   }

   #used-area-bar {
       height: 100%;
       width: 0%; /* Will be set by JS */
       background-color: #28a745; /* Green */
       transition: width 0.5s ease-in-out;
   }

  .prompt {
      margin-bottom: 15px;
      font-size: 1.1em;
      color: #333;
  }

  .button-group {
      margin-bottom: 15px;
  }

  .controls button {
    padding: 12px 20px; /* More padding */
    margin: 5px;
    cursor: pointer;
    border: none; /* No default border */
    border-radius: 6px; /* Slightly more rounded */
    font-size: 1em;
    transition: all 0.3s ease; /* Smooth transitions */
    display: inline-flex; /* Align icon and text */
    align-items: center;
    gap: 8px; /* Space between icon and text */
  }

  .controls button .icon {
      font-size: 1.1em;
  }

  .controls button[data-type="residential"] {
    background-color: #ff7f7f; /* Muted red */
    color: #4a0000;
  }
   .controls button[data-type="industrial"] {
    background-color: #7fafff; /* Muted blue */
    color: #002b5a;
  }
   .controls button[data-type="green"] {
    background-color: #7fff7f; /* Muted green */
    color: #004a00;
  }

  .controls button.selected {
    transform: translateY(-2px); /* Lift button */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    filter: brightness(1.1); /* Slightly brighter */
  }

  .controls button:not(.selected):hover:not(:disabled) {
    filter: brightness(0.9); /* Slightly darker on hover */
  }

  .controls button:active:not(:disabled) {
      transform: scale(0.98); /* Press effect */
  }

  .controls button:disabled {
      opacity: 0.6;
      cursor: not-allowed;
  }

  .clear-button {
      background-color: #dc3545 !important; /* Bootstrap danger color */
      color: white !important;
      margin-top: 10px;
  }
   .clear-button:hover:not(:disabled) {
      background-color: #c82333 !important;
   }


  .metrics {
    margin-top: 30px; /* More space */
    padding-top: 20px;
    border-top: 1px solid #eee;
    text-align: right; /* RTL */
    direction: rtl;
    width: 100%;
  }

  .metrics h3 {
      margin-top: 0;
      margin-bottom: 15px;
      text-align: center;
      color: #0056b3;
  }

  .metric-item {
      margin-bottom: 15px;
      font-size: 1em;
      display: flex;
      align-items: center;
      justify-content: space-between; /* Distribute items */
      gap: 10px;
  }

    .metric-item label {
        flex-grow: 1; /* Take available space */
        text-align: left; /* Align labels to the left */
        color: #555;
    }

    .metric-item span {
        font-weight: bold;
        min-width: 40px; /* Ensure space for numbers */
        text-align: right; /* Numbers align right */
    }

    .metric-bar-container {
        width: 150px; /* Fixed width for bars */
        height: 10px;
        background-color: #e0e0e0;
        border-radius: 5px;
        overflow: hidden;
        position: relative; /* For potential inner shadow/border */
        margin-left: 10px; /* Space between number and bar */
    }

     .metric-bar {
        height: 100%;
        width: 0%; /* Will be set by JS */
        background-color: #28a745; /* Default green */
        transition: width 0.5s ease-in-out; /* Animate bar growth */
     }

     .metric-bar-container.pollution .metric-bar { background-color: #dc3545; } /* Red for pollution */
     .metric-bar-container.satisfaction .metric-bar { background-color: #ffc107; } /* Yellow/Orange for satisfaction */
      /* Income/Residents could have their own colors or use default green */
      #income-bar { background-color: #17a2b8; } /* Info blue for income */
       #residents-bar { background-color: #6f42c1; } /* Purple for residents */


    .legend {
        margin-top: 20px;
        padding-top: 15px;
        border-top: 1px dashed #ddd;
        text-align: center;
    }
    .legend h4 {
        margin-top: 0;
        margin-bottom: 10px;
        color: #0056b3;
    }
    .legend ul {
        list-style: none;
        padding: 0;
        margin: 0;
        display: flex;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }
    .legend li {
        display: flex;
        align-items: center;
        gap: 5px;
        font-size: 0.9em;
        color: #555;
    }
    .legend-color {
        display: inline-block;
        width: 15px;
        height: 15px;
        border-radius: 3px;
        border: 1px solid rgba(0,0,0,0.1); /* Small border for definition */
    }
    .legend-color.residential { background-color: #ff7f7f; }
    .legend-color.industrial { background-color: #7fafff; }
    .legend-color.green { background-color: #7fff7f; }


  #city-grid {
    display: grid;
    grid-template-columns: repeat(10, 35px); /* Slightly larger cells */
    grid-template-rows: repeat(10, 35px);
    gap: 2px; /* Slightly larger gap */
    border: 1px solid #999; /* Darker border */
    width: fit-content;
    margin: 0 auto;
    background-color: #ccc; /* Color for the gap */
    border-radius: 5px;
    overflow: hidden; /* Keep cells within rounded border */
  }

  .grid-cell {
    width: 100%; /* Fill grid area */
    height: 100%; /* Fill grid area */
    background-color: #e0e0e0; /* Default empty color */
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transitions */
    position: relative; /* For potential overlay effects */
  }

   .grid-cell:hover {
      transform: scale(1.05); /* Slight zoom on hover */
      z-index: 1; /* Bring hovered cell to front */
      box-shadow: 0 0 5px rgba(0,0,0,0.3);
  }

  /* Animation for cell placement */
  .grid-cell.placed {
      animation: pop-in 0.3s ease;
  }

  @keyframes pop-in {
      0% { transform: scale(0.8); opacity: 0.5; }
      80% { transform: scale(1.05); opacity: 1; }
      100% { transform: scale(1); }
  }


  .grid-cell.residential {
    background-color: #ff7f7f; /* Muted red */
  }

  .grid-cell.industrial {
    background-color: #7fafff; /* Muted blue */
  }

  .grid-cell.green {
    background-color: #7fff7f; /* Muted green */
  }

    /* Responsive adjustments */
  @media (max-width: 768px) {
      #city-grid {
          grid-template-columns: repeat(10, 30px); /* Smaller cells */
          grid-template-rows: repeat(10, 30px);
          gap: 1px;
      }
      .metrics {
          font-size: 0.9em;
      }
       .metric-bar-container {
           width: 100px; /* Smaller bars */
       }
  }

   @media (max-width: 480px) {
      #city-grid {
          grid-template-columns: repeat(10, 25px); /* Even smaller */
          grid-template-rows: repeat(10, 25px);
          gap: 1px;
      }
       .controls button {
           padding: 10px 15px;
           gap: 5px;
       }
       .controls button .icon {
            font-size: 1em;
       }
       .metric-item {
           flex-direction: column; /* Stack metrics vertically */
           align-items: flex-start;
       }
        .metric-item label {
            text-align: right; /* Labels align right in stack */
            width: 100%;
        }
       .metric-bar-container {
           width: 100%; /* Bars take full width */
           margin-left: 0;
            margin-top: 5px;
       }
       .metric-item span {
            width: 100%;
            text-align: left; /* Numbers align left in stack */
       }
   }


  #toggle-explanation {
    display: block;
    width: fit-content;
    margin: 30px auto 20px auto; /* More space above, less below */
    padding: 12px 25px;
    font-size: 1.1em;
    cursor: pointer;
    border: none;
    border-radius: 25px; /* Pill shape */
    background-color: #007bff;
    color: white;
    box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2);
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
  }

  #toggle-explanation:hover {
    background-color: #0056b3;
    box-shadow: 0 6px 12px rgba(0, 123, 255, 0.3);
  }
   #toggle-explanation:active {
       transform: scale(0.98);
   }


  #explanation-content {
    display: none; /* Hidden by default */
    margin-top: 20px;
    padding: 20px;
    border: none;
    border-radius: 10px;
    background-color: #f8f9fa; /* Light background */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    line-height: 1.6; /* Improved readability */
    color: #333;
  }

  #explanation-content h2 {
      margin-top: 0;
      color: #0056b3;
      border-bottom: 1px solid #eee;
      padding-bottom: 10px;
      margin-bottom: 15px;
  }

  #explanation-content p {
      margin-bottom: 15px;
  }

  #explanation-content ul {
      list-style: disc outside; /* Disc bullet points outside the text */
      margin-right: 20px; /* Space for bullets */
      padding-right: 0;
  }

  #explanation-content li {
      margin-bottom: 12px;
      line-height: 1.5;
  }
   #explanation-content li strong {
       color: #0056b3; /* Highlight key terms */
   }


</style>

<button id="toggle-explanation">הצגת אתגרי התכנון (למה זה כל כך מורכב?)</button>

<div id="explanation-content">
  <h2>האתגר האמיתי: למה לתכנן עיר זה מסובך?</h2>
  <p>תכנון עירוני הוא כמו משחק שחמט מורכב שמשפיע על מיליוני אנשים. הוא דורש לא רק ראייה אדריכלית או הנדסית, אלא הבנה עמוקה של צרכים אנושיים, כלכלה, סביבה וחברה. המטרה היא לבנות מרחב עירוני שיהיה גם פונקציונלי, גם נעים למגורים, גם משגשג כלכלית וגם שומר על כדור הארץ לדורות הבאים. האתגר? כל המטרות האלה לרוב מתנגשות...</p>
  <ul>
    <li><strong>מהות התכנון העירוני:</strong><br>בבסיסו, תכנון עירוני הוא אומנות וגם מדע של ארגון המרחב בו אנו חיים ועובדים. זה לא רק איפה נבנה בניין, אלא איך הבניין הזה ישפיע על התנועה ברחוב, על איכות האוויר, על הנגישות לפארק הקרוב, ועל התחושה הכללית של הקהילה. תכנון טוב מאפשר לעיר לצמוח בצורה מסודרת, מונע כאוס ומבטיח שמשאבים מוגבלים כמו קרקע ומים ינוהלו בתבונה.</li>
    <li><strong>שחקנים ראשיים במפת העיר:</strong><br>העיר בנויה מאזורים עם תפקידים שונים:
        <ul>
            <li><strong>מגורים:</strong> הלב של העיר. איפה שאנשים גרים, מגדלים משפחות ויוצרים קהילות. דורש גישה נוחה לשירותים (חינוך, בריאות), שטחים פתוחים ותחבורה ציבורית טובה. צפיפות גבוהה יכולה ליצור עומס, צפיפות נמוכה "מבזבזת" קרקע ותשתיות.</li>
            <li><strong>תעשייה ומסחר:</strong> מנוע הצמיחה הכלכלי. מייצרים מקומות עבודה, הכנסות (ארנונה!) ומספקים שירותים ומוצרים. הפוטנציאל השלילי: זיהום, רעש, תנועת משאיות כבדות ועומסי תנועה בשעות העומס.</li>
            <li><strong>שטחים ירוקים ופתוחים:</strong> הריאות הירוקות, המקום לנשום, לנוח ולהתחבר לטבע גם בלב העיר. פארקים, גינות, שמורות טבע עירוניות. חיוניים לבריאות פיזית ונפשית, משפרים איכות אוויר ומים, תורמים למגוון הביולוגי ופשוט הופכים את העיר ליפה יותר. "החיסרון" מבחינה כלכלית צרה: לא מייצרים הכנסה וגוזלים שטח יקר.</li>
        </ul>
    </li>
    <li><strong>התנגשויות בלתי נמנעות:</strong><br>הדבר המאתגר ביותר הוא ששימושי הקרקע השונים לא תמיד "חברים" טובים. מי רוצה לגור ממש ליד מפעל מזהם או כביש סואן? איך מייצרים מספיק מקומות עבודה בלי לחנוק את העיר בזיהום? ואיך בונים מספיק דירות לכולם בלי "לבלוע" את כל השטחים הירוקים שנשארו? כל החלטה במקום אחד יוצרת גלי הדף במקומות אחרים.</li>
    <li><strong>תכנון אזורים חדשים: הזדמנות ואחריות:</strong><br>כשיש שטח גדול וריק, זו הזדמנות נדירה לעצב את העתיד. אבל זו גם אחריות ענקית. המתכננים חייבים לחשוב על הכל יחד: איך לשלב מגורים, עבודה ופנאי כך שישרתו זה את זה? איך להבטיח תחבורה קיימת? איך לנהל את הפסולת והזיהום? ואיך לדאוג שכל תושבי העיר, מכל הרקעים, יוכלו למצוא בה את מקומם?</li>
    <li><strong>הכוח של פשרות וראייה מערכתית:</strong><br>עיר מושלמת לא קיימת. תכנון טוב הוא כמעט תמיד תוצאה של פשרות חכמות. מתכננים מצליחים הם אלה שמסוגלים לראות את התמונה הגדולה, להבין את הקשרים בין החלקים השונים של המערכת העירונית, ולמצוא את האיזון הטוב ביותר האפשרי עבור כמה שיותר אנשים, תוך מחשבה לטווח ארוך על קיימות וחוסן עירוני. עכשיו, נסו בעצמכם!</li>
  </ul>
</div>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const gridElement = document.getElementById('city-grid');
    const availableAreaElement = document.getElementById('available-area');
    const usedAreaBar = document.getElementById('used-area-bar');
    const metrics = {
      residents: { value: 0, element: document.getElementById('metric-residents'), bar: document.getElementById('residents-bar') },
      income: { value: 0, element: document.getElementById('metric-income'), bar: document.getElementById('income-bar') },
      pollution: { value: 0, element: document.getElementById('metric-pollution'), bar: document.getElementById('pollution-bar') },
      satisfaction: { value: 50, element: document.getElementById('metric-satisfaction'), bar: document.getElementById('satisfaction-bar') }
    };
    const typeButtons = document.querySelectorAll('.controls button[data-type]:not(.clear-button)'); // Exclude clear button
    const clearButton = document.querySelector('.controls button.clear-button');
    const explanationButton = document.getElementById('toggle-explanation');
    const explanationContent = document.getElementById('explanation-content');

    const GRID_SIZE = 10; // 10x10 grid
    const TOTAL_AREA = GRID_SIZE * GRID_SIZE;
    let availableArea = TOTAL_AREA;
    let gridState = Array(TOTAL_AREA).fill('empty'); // 'empty', 'residential', 'industrial', 'green'
    let selectedType = 'residential'; // Default selected type

    // Define effects per cell type - Adjusted values for more noticeable impact
    const effects = {
      empty: { residents: 0, income: 0, pollution: 0, greenScore: 0 },
      residential: { residents: 8, income: -3, pollution: 1, greenScore: 0 }, // Costs income for services, slight pollution from living
      industrial: { residents: -5, income: 18, pollution: 7, greenScore: -2 }, // Negative residents due to noise/smell, high pollution, slightly reduces green score nearby
      green: { residents: 1, income: -1, pollution: -4, greenScore: 5 } // Attracts residents (slight), costs income (maintenance), reduces pollution, adds high green score
    };

    function renderGrid() {
      gridElement.innerHTML = ''; // Clear existing grid
      for (let i = 0; i < TOTAL_AREA; i++) {
        const cell = document.createElement('div');
        cell.classList.add('grid-cell');
        cell.classList.add(gridState[i]);
        cell.dataset.index = i;
        cell.addEventListener('click', handleCellClick);
        gridElement.appendChild(cell);
      }
      updateMetrics();
      updateAvailableAreaDisplay();
    }

    function updateAvailableAreaDisplay() {
        const usedArea = gridState.filter(type => type !== 'empty').length;
        availableArea = TOTAL_AREA - usedArea;
        availableAreaElement.textContent = availableArea;

        const usedPercentage = (usedArea / TOTAL_AREA) * 100;
        usedAreaBar.style.width = `${usedPercentage}%`;

         // Disable placement buttons if no area, unless clearing
        typeButtons.forEach(button => {
            if (availableArea === 0) {
                button.disabled = true;
            } else {
                button.disabled = false;
            }
        });
         // Clear button is always enabled if anything is placed
         clearButton.disabled = usedArea === 0;
    }


    function updateMetrics() {
      let totalResidentsEffect = 0;
      let totalIncomeEffect = 0;
      let totalPollutionEffect = 0;
      let totalGreenScore = 0;

      let placedCellsCount = 0;
      let residentialCount = 0;

      gridState.forEach(type => {
        if (type !== 'empty') {
            placedCellsCount++;
            totalResidentsEffect += effects[type].residents;
            totalIncomeEffect += effects[type].income;
            totalPollutionEffect += effects[type].pollution;
            totalGreenScore += effects[type].greenScore;

            if (type === 'residential') residentialCount++;
        }
      });

      // --- Calculate Overall Metrics ---
      // Residents: Base on effect sum, scale it (e.g., 0 to 1000 potential residents)
      const maxPossibleResidents = TOTAL_AREA * effects.residential.residents; // Max if all residential
      const minPossibleResidents = TOTAL_AREA * effects.industrial.residents; // Max negative if all industrial
      // Map totalResidentsEffect to a more meaningful range (e.g., 0 to 1000)
      let potentialResidents = Math.max(0, Math.round((totalResidentsEffect - minPossibleResidents) / (maxPossibleResidents - minPossibleResidents) * 1000));

      // Income: Base on effect sum, scale it (e.g., -500 to 1000 potential income units)
       const maxPossibleIncome = TOTAL_AREA * effects.industrial.income;
       const minPossibleIncome = TOTAL_AREA * effects.residential.income; // Assuming residential costs most
       let potentialIncome = Math.round((totalIncomeEffect - minPossibleIncome) / (maxPossibleIncome - minPossibleIncome) * 1000 - 500); // Shift range


      // Pollution: Base on effect sum, clamped and scaled (0-100%)
      const maxPotentialPollution = TOTAL_AREA * Math.max(effects.industrial.pollution, effects.residential.pollution, effects.green.pollution > 0 ? effects.green.pollution : 0); // Max possible positive pollution
      const minPotentialPollution = TOTAL_AREA * Math.min(effects.industrial.pollution < 0 ? effects.industrial.pollution : 0, effects.residential.pollution < 0 ? effects.residential.pollution : 0, effects.green.pollution); // Max possible negative pollution
      let pollutionLevel = Math.round(((totalPollutionEffect - minPotentialPollution) / (maxPotentialPollution - minPotentialPollution)) * 100); // Scale to 0-100 range
      pollutionLevel = Math.max(0, Math.min(100, pollutionLevel));


      // Satisfaction: More complex formula
      const maxGreenScore = TOTAL_AREA * effects.green.greenScore;
      const minGreenScore = TOTAL_AREA * Math.min(effects.industrial.greenScore, effects.residential.greenScore); // Max negative green effect

      const greenFactor = Math.max(0, Math.min(1, (totalGreenScore - minGreenScore) / (maxGreenScore - minGreenScore))); // Scale green score to 0-1
      const pollutionFactor = Math.max(0, Math.min(1, (pollutionLevel / 100))); // Pollution as 0-1

      // Density factor: higher density relative to total cells decreases satisfaction
      const densityFactor = placedCellsCount > 0 ? (residentialCount / placedCellsCount) : 0;

      // Simple combined formula: Base + Green Boost - Pollution Penalty - Density Penalty
      let totalSatisfaction = 70 + (greenFactor * 40) - (pollutionFactor * 50) - (densityFactor * 20); // Adjusted weights

      // Add penalty for extreme income (e.g., very negative income is bad)
      const incomePenalty = potentialIncome < 0 ? Math.abs(potentialIncome / 20) : 0; // Penalty if income is negative
      totalSatisfaction -= incomePenalty;


      totalSatisfaction = Math.max(0, Math.min(100, Math.round(totalSatisfaction))); // Clamp between 0-100

      // --- Update Display ---
      metrics.residents.element.textContent = potentialResidents;
      metrics.income.element.textContent = potentialIncome;
      metrics.pollution.element.textContent = pollutionLevel;
      metrics.satisfaction.element.textContent = totalSatisfaction;

      // Update bars - Scale values for bars (0-100 range needed for bar width)
      // Residents & Income need mapping as they can be >100 or <0
       const residentsBarValue = Math.max(0, Math.min(100, Math.round(potentialResidents / 10))); // Assuming max 1000 maps to 100%
       const incomeBarValue = Math.max(0, Math.min(100, Math.round((potentialIncome + 500) / 15))); // Assuming range -500 to 1000 maps to 0-100%
       const pollutionBarValue = pollutionLevel; // Already 0-100
       const satisfactionBarValue = totalSatisfaction; // Already 0-100


      metrics.residents.bar.style.width = `${residentsBarValue}%`;
      metrics.income.bar.style.width = `${incomeBarValue}%`;
      metrics.pollution.bar.style.width = `${pollutionBarValue}%`;
      metrics.satisfaction.bar.style.width = `${satisfactionBarValue}%`;

       // Optional: Change pollution bar color based on level
       if (pollutionLevel > 70) metrics.pollution.bar.style.backgroundColor = '#dc3545'; // Red
       else if (pollutionLevel > 40) metrics.pollution.bar.style.backgroundColor = '#ffc107'; // Orange
       else metrics.pollution.bar.style.backgroundColor = '#28a745'; // Green

        // Optional: Change satisfaction bar color based on level
       if (totalSatisfaction < 30) metrics.satisfaction.bar.style.backgroundColor = '#dc3545'; // Red
       else if (totalSatisfaction < 60) metrics.satisfaction.bar.style.backgroundColor = '#ffc107'; // Orange
       else metrics.satisfaction.bar.style.backgroundColor = '#28a745'; // Green
    }

    function handleCellClick(event) {
      const index = parseInt(event.target.dataset.index);
      const currentType = gridState[index];
      const cellElement = event.target;

      let typeToPlace = selectedType;

      if (selectedType === 'clear') {
          if (currentType !== 'empty') {
              gridState[index] = 'empty';
              // Animate removal? Or just update. Let's just update.
              cellElement.classList.remove(currentType);
               cellElement.classList.add('empty');
          } else {
              return; // Don't do anything if clearing an empty cell
          }
      } else {
          if (currentType !== typeToPlace) {
               // Only place if there's enough area or replacing
              if (currentType === 'empty') {
                  // Check if there's available area
                  if (availableArea > 0) {
                      gridState[index] = typeToPlace;
                      cellElement.classList.remove('empty');
                       cellElement.classList.add(typeToPlace);
                       // Add placement animation class
                       cellElement.classList.add('placed');
                       setTimeout(() => cellElement.classList.remove('placed'), 300); // Remove class after anim
                  } else {
                      // Visual cue instead of alert
                      // Maybe shake the grid or flash a message area
                       console.log('נגמר השטח הפנוי!'); // For debugging, could replace with UI feedback
                       // Add a temporary class to grid for visual feedback?
                       gridElement.classList.add('no-area-feedback');
                       setTimeout(() => gridElement.classList.remove('no-area-feedback'), 500);
                      return; // Don't update if no area
                  }
              } else {
                 // Replace existing type
                 const previousType = currentType;
                 gridState[index] = typeToPlace;
                 cellElement.classList.remove(previousType);
                 cellElement.classList.add(typeToPlace);
                  cellElement.classList.add('placed');
                  setTimeout(() => cellElement.classList.remove('placed'), 300);
              }
          } else {
             // Clicked the same type again - do nothing or use clear button
             return;
          }
      }

      updateMetrics(); // Update metrics after successful placement/clearing
      updateAvailableAreaDisplay(); // Update area display
    }

    function handleTypeButtonClick(event) {
      const type = event.target.dataset.type;
      selectedType = type;

      // Update button styles
      document.querySelectorAll('.controls button[data-type]').forEach(button => { // Select all buttons including clear
        if (button.dataset.type === type) {
          button.classList.add('selected');
        } else {
          button.classList.remove('selected');
        }
      });
    }

    function toggleExplanation() {
        const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר אתגרי התכנון' : 'הצגת אתגרי התכנון (למה זה כל כך מורכב?)';
    }


    // --- Initialization ---
    renderGrid(); // Initial render
    document.querySelectorAll('.controls button[data-type]').forEach(button => {
      button.addEventListener('click', handleTypeButtonClick);
    });
    explanationButton.addEventListener('click', toggleExplanation);

     // Set initial button state
    typeButtons.forEach(button => {
        if(button.dataset.type === selectedType) {
            button.classList.add('selected');
        }
    });

  });
</script>
```