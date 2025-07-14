---
title: "כוריאוגרפיית ההתנגשות: ריקוד התנע"
english_slug: unexpected-collision-who-moves-where
category: "פיזיקה"
tags: ["פיזיקה", "תנע", "התנגשות", "שימור תנע", "מכניקה", "סימולציה", "אינטראקטיבי"]
---
<h1>כוריאוגרפיית ההתנגשות: ריקוד התנע</h1>

<p>דמיינו מכונית צעצוע עדינה פוגשת קיר בטון איתן, לעומת משאית ענקית שפוגשת באותה מכונית צעצוע. התוצאה, ברור לכולנו, שונה דרמטית! אבל מהו העיקרון הפיזיקלי האלגנטי שמכתיב מי יזוז לאן ובאיזו מהירות אחרי כל התנגשות, בכל מצב, גם כשהמסות והמהירויות משתנות פלאים? בואו נגלה!</p>

<div class="app-container">
    <div class="controls">
        <h2>הגדירו את המפגש הגורלי</h2>
        <div class="control-group">
            <h3>כדור הכחול 🔵</h3>
            <label for="mass1">מסה (ק"ג): <span id="mass1-value">1</span></label>
            <input type="range" id="mass1" min="0.5" max="5" step="0.1" value="1">
            <br>
            <label for="velocity1">מהירות התחלתית (מ"ש): <span id="velocity1-value">2</span></label>
            <input type="range" id="velocity1" min="-5" max="5" step="0.1" value="2">
        </div>
        <div class="control-group">
            <h3>כדור האדום 🔴</h3>
            <label for="mass2">מסה (ק"ג): <span id="mass2-value">1</span></label>
            <input type="range" id="mass2" min="0.5" max="5" step="0.1" value="1">
            <br>
            <label for="velocity2">מהירות התחלתית (מ"ש): <span id="velocity2-value">-2</span></label>
            <input type="range" id="velocity2" min="-5" max="5" step="0.1" value="-2">
        </div>
        <div class="button-group">
             <button id="collide-button" class="action-button primary">הפעל סימולציה!</button>
             <button id="reset-button" class="action-button secondary">איפוס</button>
        </div>
    </div>

    <div class="simulation-area">
        <div class="track">
            <div id="ball1" class="ball ball1"></div>
            <div id="ball2" class="ball ball2"></div>
        </div>
    </div>

    <div class="momentum-display">
        <h2>מאזן התנע של המערכת</h2>
        <div class="momentum-section">
            <h3>לפני המפגש</h3>
            <p>תנע כחול (<span class="ball1-color">p₁</span>): <span id="p1-initial">-</span> ק"ג*מ"ש</p>
            <p>תנע אדום (<span class="ball2-color">p₂</span>): <span id="p2-initial">-</span> ק"ג*מ"ש</p>
            <p class="total">תנע כולל (<span dir="ltr">P<sub>total</sub></span>): <span id="p-total-initial">-</span> ק"ג*מ"ש</p>
        </div>
        <div class="momentum-section">
            <h3>אחרי המפגש</h3>
             <p>תנע כחול (<span class="ball1-color">p₁'</span>): <span id="p1-final">-</span> ק"ג*מ"ש</p>
            <p>תנע אדום (<span class="ball2-color">p₂'</span>): <span id="p2-final">-</span> ק"ג*מ"ש</p>
            <p class="total">תנע כולל (<span dir="ltr">P<sub>total</sub>'</span>): <span id="p-total-final">-</span> ק"ג*מ"ש</p>
        </div>
    </div>
     <div class="conservation-hint" style="display: none;">
         <h3>שימו לב!</h3>
         <p>האם התנע הכולל לפני ההתנגשות שווה לתנע הכולל אחריה? חפשו את החוק הסודי...</p>
     </div>
</div>

<button id="toggle-explanation">רוצים להבין לעומק? לחצו כאן להסבר!</button>

<div id="explanation" class="explanation" style="display: none;">
    <h2>פענוח המפגש: תנע וקסם השימור</h2>
    <p><strong>מה זה בכלל תנע?</strong> דמיינו שאתם מנסים לעצור גוף בתנועה. קל יותר לעצור כדור פינג-פונג שזז לאט מאשר משאית שועטת, נכון? התנע הוא גודל וקטורי שמבטא את "כמות התנועה" של גוף, וכמה "קשה" לשנות את מצב התנועה שלו. הוא מחושב בפשטות: מסה כפול מהירות (<span dir="ltr">p = m * v</span>). שימו לב לכיוון! מהירות ותנע יכולים להיות חיוביים (ימינה) או שליליים (שמאלה).</p>
    <p><strong>התנגשויות: דרמה במיקרו-שנייה</strong> התנגשות היא אירוע קצר ועוצמתי. הגופים מפעילים כוחות עצומים זה על זה, לרוב הרבה יותר גדולים מכוחות חיצוניים כמו חיכוך (במערכת אופקית כמו בסימולציה). הדרמה הגדולה קורית בפנים!</p>
    <p><strong>מערכת סגורה והכוחות הפנימיים</strong> כשאנחנו מתמקדים בקבוצת גופים (במקרה שלנו, שני הכדורים), אנחנו מגדירים "מערכת". כוחות בין הגופים בתוך המערכת הם "פנימיים" (הכוח שכדור כחול מפעיל על אדום, ולהיפך - זוג פעולה-תגובה). כוחות מחוץ למערכת הם "חיצוניים" (למשל, מנוע או כוח גרר משמעותי). בסימולציה הזו, אנו מתעלמים מכוחות חיצוניים בכיוון התנועה, מה שהופך את המערכת ל"כמעט סגורה" בכיוון האופקי.</p>
    <p><strong>החוק הגדול: שימור התנע!</strong> זהו אחד מעמודי התווך של הפיזיקה. במערכת סגורה לחלוטין (או כמעט סגורה, כשכוחות פנימיים דומיננטיים), התנע הכולל של המערכת <strong>נשמר!</strong> כלומר, הסכום הווקטורי של התנעים של כל הגופים לפני ההתנגשות שווה בדיוק לסכום הווקטורי של התנעים שלהם אחרי ההתנגשות:</p>
    <p dir="ltr">p<sub>total_before</sub> = p<sub>total_after</sub></p>
    <p dir="ltr">m<sub>1</sub>v<sub>1_initial</sub> + m<sub>2</sub>v<sub>2_initial</sub> = m<sub>1</sub>v<sub>1_final</sub> + m<sub>2</sub>v<sub>2_final</sub></p>
    <p>כאשר v₁ ו-v₂ עם אינדקס initial מתייחסים למהירויות לפני, ועם אינדקס final למהירויות אחרי. המסות (m) נשארות כמובן קבועות. הסוד הוא שהתנע עובר בין הגופים במהלך ההתנגשות, אבל הסכום הכולל שלו לא "הולך לאיבוד" או נוצר יש מאין.</p>
    <p><strong>הצגה ויזואלית של הקסם:</strong> האפליקציה מציגה לכם את ערכי התנע של כל כדור בנפרד ואת התנע הכולל של המערכת לפני ואחרי ההתנגשות. שחקו עם מסות ומהירויות שונות, וצפו כיצד התנעים האישיים עפים לכל עבר, אבל התנע הכולל של המערכת נשאר יציב להפליא (עם סטייה זעירה עקב דיוקי חישוב). זהו לב חוק שימור התנע בפעולה!</p>
</div>

<style>
    /* Import a modern font */
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    .app-container {
        font-family: 'Heebo', sans-serif;
        direction: rtl; /* For Hebrew text alignment */
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 30px;
        padding: 30px;
        border: none; /* Remove default border */
        border-radius: 12px; /* More rounded corners */
        background-color: #f0f4f8; /* Soft light blue background */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        max-width: 700px; /* Slightly wider container */
        width: 95%; /* Responsive width */
        margin-left: auto;
        margin-right: auto;
    }

    h1, h2, h3 {
        color: #2c3e50; /* Darker blue-gray for headings */
        text-align: center;
        margin-bottom: 15px;
        font-weight: 700;
    }

    p {
         color: #34495e; /* Slightly lighter text color */
         line-height: 1.7;
         margin-bottom: 1em;
    }


    .controls {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 25px; /* Increased gap */
        margin-bottom: 30px;
        width: 100%;
    }

    .control-group {
        background-color: #ffffff; /* White background for control groups */
        padding: 20px; /* More padding */
        border-radius: 8px;
        min-width: 250px; /* Wider control groups */
        flex-grow: 1; /* Allow groups to grow */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* Subtle shadow */
    }

    .control-group h3 {
        margin-top: 0;
        margin-bottom: 15px;
        color: #3498db; /* Blue accent for group titles */
        font-size: 1.1em;
    }

     .control-group label {
        display: block;
        margin-bottom: 8px;
        font-weight: 400; /* Regular weight for labels */
        color: #555;
        font-size: 0.95em;
     }

     .control-group input[type="range"] {
        width: 100%;
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        height: 8px;
        background: #bdc3c7; /* Light gray track */
        outline: none;
        opacity: 0.7;
        transition: opacity .15s ease-in-out;
        border-radius: 5px;
     }

     .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #3498db; /* Blue thumb */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
     }

      .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #3498db;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
     }

     .button-group {
         width: 100%;
         display: flex;
         justify-content: center;
         gap: 15px;
         margin-top: 20px;
     }

    .action-button {
        padding: 12px 25px; /* More padding */
        font-size: 1em; /* Standard size */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 700;
    }

    .primary {
        background-color: #2ecc71; /* Green primary */
        color: white;
    }
     .primary:hover {
         background-color: #27ae60; /* Darker green on hover */
     }
      .primary:active {
         transform: scale(0.98); /* Slight press effect */
      }

    .secondary {
         background-color: #e74c3c; /* Red secondary */
         color: white;
     }
     .secondary:hover {
         background-color: #c0392b; /* Darker red on hover */
     }
     .secondary:active {
         transform: scale(0.98); /* Slight press effect */
     }

     .action-button:disabled {
         background-color: #bdc3c7; /* Gray when disabled */
         cursor: not-allowed;
         opacity: 0.8;
     }


    .simulation-area {
        width: 100%;
        max-width: 650px; /* Slightly wider simulation area */
        height: 120px; /* More height for track visualization */
        position: relative;
        margin-bottom: 30px;
        overflow: hidden; /* Hide balls going off-screen */
        background-color: #ecf0f1; /* Light background for sim area */
        border-radius: 8px;
        box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .track {
        width: calc(100% - 40px); /* Track doesn't touch edges */
        height: 25px; /* Thicker track */
        background: linear-gradient(to right, #bdc3c7, #95a5a6); /* Gradient track */
        position: absolute;
        top: 50%; /* Center vertically */
        left: 20px; /* Offset from left */
        transform: translateY(-50%); /* Perfect vertical centering */
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .ball {
        position: absolute;
        width: 40px; /* Ball size */
        height: 40px;
        border-radius: 50%;
        /* Adjusted top position relative to simulation-area */
        top: 50%;
        transform: translateY(-50%);
        box-sizing: border-box;
        transition: transform 0.1s ease-in-out; /* Smooth scaling/pulse */
    }

    .ball1 {
        background-color: #3498db; /* Blue */
        left: 0; /* Initial position */
        border: 3px solid #2980b9; /* Darker blue border */
        box-shadow: 0 0 10px rgba(52, 152, 219, 0.6); /* Blue glow */
    }

    .ball2 {
        background-color: #e74c3c; /* Red */
        right: 0; /* Initial position */
        border: 3px solid #c0392b; /* Darker red border */
        box-shadow: 0 0 10px rgba(231, 76, 60, 0.6); /* Red glow */
    }

    /* Collision Animation Effect */
     .ball.colliding {
         animation: pulse 0.4s ease-in-out infinite alternate;
         box-shadow: 0 0 20px #f1c40f; /* Yellowish flash effect */
     }

     @keyframes pulse {
         from {
             transform: translateY(-50%) scale(1);
             opacity: 1;
         }
         to {
              transform: translateY(-50%) scale(1.05);
             opacity: 0.9;
         }
     }


    .momentum-display {
        width: 100%;
        max-width: 650px; /* Match sim area width */
        margin-top: 20px;
        border-top: 2px solid #bdc3c7; /* Separator line */
        padding-top: 20px;
        background-color: #ecf0f1; /* Match sim area background */
        border-radius: 8px;
        padding-bottom: 10px;
    }

    .momentum-display h2 {
        text-align: center;
        margin-bottom: 20px;
        color: #2c3e50;
        font-size: 1.2em;
    }

    .momentum-section {
        display: inline-block; /* Display side-by-side */
        width: 48%; /* Roughly half width */
        vertical-align: top;
        padding: 0 10px;
        box-sizing: border-box; /* Include padding in width */
    }
     .momentum-section:last-of-type {
         text-align: right;
     }

    .momentum-display p {
        margin: 8px 0; /* More vertical space */
        font-size: 0.95em;
        color: #34495e;
    }

    .momentum-display .total {
        font-weight: 700; /* Bold total */
        border-top: 1px dashed #95a5a6;
        padding-top: 8px;
        margin-top: 15px;
        color: #2c3e50; /* Darker color for total */
        font-size: 1em;
    }

     .ball1-color {
         color: #3498db;
         font-weight: 700;
     }
      .ball2-color {
         color: #e74c3c;
         font-weight: 700;
     }

    .conservation-hint {
        margin-top: 20px;
        padding: 15px;
        background-color: #f1c40f; /* Yellow background */
        color: #2c3e50;
        border-radius: 6px;
        font-weight: 700;
        text-align: center;
        width: calc(100% - 40px);
        max-width: 610px;
    }
     .conservation-hint h3 {
         margin: 0 0 10px 0;
         color: #2c3e50;
         font-size: 1.1em;
     }
      .conservation-hint p {
         margin: 0;
         font-weight: 400;
         line-height: 1.5;
      }


    #toggle-explanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #3498db; /* Blue button */
        color: white;
        font-weight: 700;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #toggle-explanation:hover {
        background-color: #2980b9; /* Darker blue on hover */
    }
     #toggle-explanation:active {
         transform: scale(0.98); /* Slight press effect */
     }


    .explanation {
        margin-top: 20px;
        padding: 30px;
        border: none;
        border-radius: 12px;
        background-color: #ffffff; /* White background */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        direction: rtl; /* Ensure explanation is RTL */
        text-align: justify;
        max-width: 700px;
        width: 95%;
        margin-left: auto;
        margin-right: auto;
    }

    .explanation h2 {
        text-align: center;
        margin-top: 0;
        color: #2c3e50;
        border-bottom: 2px solid #bdc3c7;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

     .explanation p {
         margin-bottom: 18px; /* More space between paragraphs */
         line-height: 1.7;
         color: #34495e;
         font-weight: 400;
     }

      .explanation span[dir="ltr"] {
          direction: ltr;
          display: inline-block; /* Prevent RTL layout issues with formulas */
          unicode-bidi: embed;
          font-family: 'Consolas', 'Courier New', monospace; /* Monospace for formulas */
          background-color: #ecf0f1; /* Light background for formulas */
          padding: 2px 5px;
          border-radius: 4px;
          font-weight: 700;
          color: #2c3e50;
      }

      .explanation strong {
          color: #3498db; /* Blue for emphasized terms */
          font-weight: 700;
      }

      /* Responsive adjustments */
      @media (max-width: 600px) {
         .controls {
             flex-direction: column;
             align-items: stretch;
         }
         .control-group {
             min-width: unset;
             width: 100%;
         }
         .button-group {
             flex-direction: column;
             gap: 10px;
         }
         .momentum-section {
             width: 100%;
             display: block;
             text-align: right;
             padding: 10px 0;
             border-bottom: 1px dashed #bdc3c7;
         }
          .momentum-section:first-of-type {
             text-align: left;
             padding-bottom: 10px;
             border-bottom: 1px dashed #bdc3c7;
              padding-left: 0;
          }
           .momentum-section:last-of-type {
              text-align: right;
              padding-top: 10px;
              padding-right: 0;
              border-bottom: none;
           }
      }


</style>

<script>
    // Get elements
    const mass1Input = document.getElementById('mass1');
    const mass1ValueSpan = document.getElementById('mass1-value');
    const velocity1Input = document.getElementById('velocity1');
    const velocity1ValueSpan = document.getElementById('velocity1-value');

    const mass2Input = document.getElementById('mass2');
    const mass2ValueSpan = document.getElementById('mass2-value');
    const velocity2Input = document.getElementById('velocity2');
    const velocity2ValueSpan = document.getElementById('velocity2-value');

    const collideButton = document.getElementById('collide-button');
    const resetButton = document.getElementById('reset-button');

    const ball1 = document.getElementById('ball1');
    const ball2 = document.getElementById('ball2');
    const simulationArea = document.querySelector('.simulation-area'); // Use simulation-area for width

    const p1InitialSpan = document.getElementById('p1-initial');
    const p2InitialSpan = document.getElementById('p2-initial');
    const pTotalInitialSpan = document.getElementById('p-total-initial');
    const p1FinalSpan = document.getElementById('p1-final');
    const p2FinalSpan = document.getElementById('p2-final');
    const pTotalFinalSpan = document.getElementById('p-total-final');
    const conservationHintDiv = document.querySelector('.conservation-hint');


    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Simulation parameters
    // Get dynamic width from simulation area
    let simAreaWidth = simulationArea.offsetWidth;
    const ballDiameter = 40; // Matches CSS size
    const scaleFactor = 50; // Pixels per meter (e.g., 1 m/s -> 50 px/s)
    const frameRate = 60; // frames per second
    const timeStep = 1 / frameRate; // Time step per frame in seconds

    let animationFrameId = null;
    let simulationTime = 0;

    // Initial ball positions (in meters relative to track left edge, considering ball center)
    // Ball 1 starts at the very left edge of the track (pixel 0), center is at radius
    let ball1InitialX_meters = ballDiameter / (2 * scaleFactor);
     // Ball 2 starts at the very right edge of the track (simAreaWidth - ballDiameter), center is at simAreaWidth - radius
    let ball2InitialX_meters = (simAreaWidth - ballDiameter / 2) / scaleFactor;


    // Function to set ball positions in pixels based on meters
    function setBallPositions(ball1X_m, ball2X_m) {
        // Convert meter positions (center) to pixel positions (left edge)
        // pixel_left = meter_pos * scale - ballRadius
        const ball1PixelX = ball1X_m * scaleFactor - ballDiameter / 2;
        const ball2PixelX = ball2X_m * scaleFactor - ballDiameter / 2;

        ball1.style.left = ball1PixelX + 'px';
        ball2.style.left = ball2PixelX + 'px';
    }

    // Initial ball positions (relative to simulation area, accounting for track padding)
    // Track width is calc(100% - 40px), left: 20px. So effective track area is 20px from left to width-20px
    // Initial position in pixels: Ball 1 at left: 20px, Ball 2 at left: width - 20px - ballDiameter
    function resetSimulationState() {
         simAreaWidth = simulationArea.offsetWidth; // Update width on reset

         const trackPaddingLeft = 20; // Matches CSS left margin
         const trackWidthPixels = simAreaWidth - (2 * trackPaddingLeft);

         // Ball 1 starts at the very left of the track area (pixel 20)
         const ball1StartPixel = trackPaddingLeft;
         // Ball 2 starts at the very right of the track area (pixel width - 20 - ballDiameter)
         const ball2StartPixel = simAreaWidth - trackPaddingLeft - ballDiameter;


         ball1.style.left = ball1StartPixel + 'px';
         ball2.style.left = ball2StartPixel + 'px';

         // Store initial positions in meters (center of the ball relative to simulation area left=0)
         ball1InitialX_meters = (ball1StartPixel + ballDiameter/2) / scaleFactor;
         ball2InitialX_meters = (ball2StartPixel + ballDiameter/2) / scaleFactor;


         simulationTime = 0; // Reset time

         // Clear momentum display
         p1InitialSpan.textContent = '-';
         p2InitialSpan.textContent = '-';
         pTotalInitialSpan.textContent = '-';
         p1FinalSpan.textContent = '-';
         p2FinalSpan.textContent = '-';
         pTotalFinalSpan.textContent = '-';
         conservationHintDiv.style.display = 'none';


         collideButton.disabled = false; // Enable collide button
         ball1.classList.remove('colliding'); // Remove collision effects
         ball2.classList.remove('colliding');
    }

    // Update displayed values for sliders
    mass1Input.addEventListener('input', () => { mass1ValueSpan.textContent = mass1Input.value; });
    velocity1Input.addEventListener('input', () => { velocity1ValueSpan.textContent = velocity1Input.value; });
    mass2Input.addEventListener('input', () => { mass2ValueSpan.textContent = mass2Input.value; });
    velocity2Input.addEventListener('input', () => { velocity2ValueSpan.textContent = velocity2Input.value; });

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר פיזיקלי';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'רוצים להבין לעומק? לחצו כאן להסבר!';
        }
    });

    // Reset button functionality
     resetButton.addEventListener('click', () => {
         cancelAnimationFrame(animationFrameId);
         resetSimulationState();
     });


    // Collision logic
    collideButton.addEventListener('click', () => {
        cancelAnimationFrame(animationFrameId); // Stop any previous animation

        const m1 = parseFloat(mass1Input.value);
        const v1_i = parseFloat(velocity1Input.value);
        const m2 = parseFloat(mass2Input.value);
        const v2_i = parseFloat(velocity2Input.value);

        // Calculate initial momentum
        const p1_i = m1 * v1_i;
        const p2_i = m2 * v2_i;
        const p_total_i = p1_i + p2_i;

        // Display initial momentum (rounded for readability)
        p1InitialSpan.textContent = p1_i.toFixed(2);
        p2InitialSpan.textContent = p2_i.toFixed(2);
        pTotalInitialSpan.textContent = p_total_i.toFixed(2);
        p1FinalSpan.textContent = '-'; // Clear final values
        p2FinalSpan.textContent = '-';
        pTotalFinalSpan.textContent = '-';
        conservationHintDiv.style.display = 'none';


        // Calculate final velocities using elastic collision formulas
        // v1_f = ((m1 - m2) * v1_i + 2 * m2 * v2_i) / (m1 + m2)
        // v2_f = (2 * m1 * v1_i + (m2 - m1) * v2_i) / (m1 + m2)
        let v1_f, v2_f;

        // Handle the case where masses are extremely close to zero (shouldn't happen with min=0.5, but good practice)
        if (m1 + m2 === 0) {
             v1_f = v1_i;
             v2_f = v2_i;
        } else {
             v1_f = ((m1 - m2) * v1_i + 2 * m2 * v2_i) / (m1 + m2);
             v2_f = (2 * m1 * v1_i + (m2 - m1) * v2_i) / (m1 + m2);
        }


        // Animation state
        // Start simulation from the reset state positions
        let ball1X_m = ball1InitialX_meters;
        let ball2X_m = ball2InitialX_meters;
        let ball1V = v1_i;
        let ball2V = v2_i;
        let collisionDetected = false;
        simulationTime = 0; // Reset time

        // Disable button during animation
        collideButton.disabled = true;

        function animate() {
            // Update positions based on current velocities
            ball1X_m += ball1V * timeStep;
            ball2X_m += ball2V * timeStep;
            simulationTime += timeStep;

            // Convert meters to pixels and set position
            setBallPositions(ball1X_m, ball2X_m);

            // Collision detection
            // Collision occurs when the right edge of ball1 touches/crosses the left edge of ball2
            // Positions are center positions in meters
            const distanceBetweenCenters_m = ball2X_m - ball1X_m;
            const collisionDistance_m = ballDiameter / scaleFactor; // Sum of radii (ballDiameter/2 + ballDiameter/2)

            // Check for collision: centers are closer than collisionDistance, AND they are moving towards each other
            if (!collisionDetected && distanceBetweenCenters_m <= collisionDistance_m && (v1_i > v2_i || v1_f < v2_f) ) {
                // Add a small tolerance for floating point errors
                 if (distanceBetweenCenters_m < collisionDistance_m * 0.95) {
                      // If they somehow significantly overlap already, maybe reset or handle error?
                      // For now, just proceed, but log a warning.
                     console.warn("Significant overlap detected before collision logic.");
                 }

                collisionDetected = true;

                 // Backtrack slightly to the estimated point of collision for smoother transition
                 // Calculate overlap distance in meters
                const overlap_m = collisionDistance_m - distanceBetweenCenters_m;
                 // Calculate time to backtrack using initial relative velocity
                 const relativeVelocityBefore = v1_i - v2_i;
                 if (Math.abs(relativeVelocityBefore) > 1e-9) { // Avoid division by zero
                     const timeToBacktrack = overlap_m / relativeVelocityBefore;

                     ball1X_m -= v1_i * timeToBacktrack;
                     ball2X_m -= v2_i * timeToBacktrack;

                      // Update pixel positions after backtracking
                     setBallPositions(ball1X_m, ball2X_m);
                 } else {
                      // If initial relative velocity is zero or near-zero, balls start touching or moving parallel.
                      // Collision might not happen or is a different type. In this elastic collision model,
                      // if v1_i == v2_i, then v1_f == v1_i and v2_f == v2_i unless masses are different.
                      // If masses are same and velocities same, they just move together. If masses different,
                      // they might swap velocities or bounce differently. The formula handles this, but
                      // the backtracking needs a non-zero relative velocity. If relative velocity is zero,
                      // they don't need backtracking for overlap as they shouldn't overlap further
                      // if velocities remain equal. Let's just apply final velocities from current position.
                 }


                 // Apply final velocities after collision
                 ball1V = v1_f;
                 ball2V = v2_f;


                 // Calculate final momentum (using calculated final velocities)
                 const p1_f = m1 * v1_f;
                 const p2_f = m2 * v2_f;
                 const p_total_f_calculated = p1_f + p2_f; // Calculate and display this value

                 // Display final momentum (rounded for readability)
                 p1FinalSpan.textContent = p1_f.toFixed(2);
                 p2FinalSpan.textContent = p2_f.toFixed(2);
                 // Display the calculated total final momentum, not just copy the initial one
                 pTotalFinalSpan.textContent = p_total_f_calculated.toFixed(2);


                 // Trigger collision visual effect
                 ball1.classList.add('colliding');
                 ball2.classList.add('colliding');
                 // Remove effect after a short delay
                 setTimeout(() => {
                     ball1.classList.remove('colliding');
                     ball2.classList.remove('colliding');
                 }, 500); // Animation duration

                 // Show conservation hint
                 conservationHintDiv.style.display = 'block';

            }

             // Stop condition: Balls moved significantly off screen or specific time limit
             // Check if ball centers are outside the simulation area + a buffer
             const buffer_m = ballDiameter / (2 * scaleFactor); // Half ball diameter buffer
            if (ball1X_m < -buffer_m || ball1X_m > simAreaWidth / scaleFactor + buffer_m ||
                ball2X_m < -buffer_m || ball2X_m > simAreaWidth / scaleFactor + buffer_m ||
                 simulationTime > 15) // Stop after 15 seconds to prevent infinite loop
                 {
                cancelAnimationFrame(animationFrameId);
                collideButton.disabled = false; // Re-enable button
                 // Optional: Reset state immediately or leave balls at final position
                 // resetSimulationState(); // Or leave them where they ended
                return;
            }

            animationFrameId = requestAnimationFrame(animate);
        }

        // Start the animation
        animate();
    });

     // Update simulation area width on window resize
    window.addEventListener('resize', () => {
         simAreaWidth = simulationArea.offsetWidth;
         // Recalculate initial ball positions based on new width
         const trackPaddingLeft = 20;
         const ball1StartPixel = trackPaddingLeft;
         const ball2StartPixel = simAreaWidth - trackPaddingLeft - ballDiameter;
         ball1InitialX_meters = (ball1StartPixel + ballDiameter/2) / scaleFactor;
         ball2InitialX_meters = (ball2StartPixel + ballDiameter/2) / scaleFactor;

         // Reset state to apply new calculated positions
         resetSimulationState();
         // Clear any ongoing animation frame request
         cancelAnimationFrame(animationFrameId);

    });


    // Initial setup
    mass1ValueSpan.textContent = mass1Input.value;
    velocity1ValueSpan.textContent = velocity1Input.value;
    mass2ValueSpan.textContent = mass2Input.value;
    velocity2ValueSpan.textContent = velocity2Input.value;

    // Set initial positions based on calculated meters from current sim area width
     simAreaWidth = simulationArea.offsetWidth; // Get width on load
     const trackPaddingLeft = 20;
     const ball1StartPixel = trackPaddingLeft;
     const ball2StartPixel = simAreaWidth - trackPaddingLeft - ballDiameter;
     ball1InitialX_meters = (ball1StartPixel + ballDiameter/2) / scaleFactor;
     ball2InitialX_meters = (ball2StartPixel + ballDiameter/2) / scaleFactor;
     resetSimulationState(); // Use the reset function for initial setup


</script>
```