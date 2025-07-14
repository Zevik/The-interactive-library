---
title: "ביטול רעשים באוזניות: איך גלים הופכים שקט לקסם פיזיקלי?"
english_slug: noise-cancellation-headphones-destructive-interference
category: "מדעים מדויקים / פיזיקה"
tags:
  - physics
  - waves
  - sound
  - interference
  - noise-cancellation
---
<p>תארו לעצמכם רגע של שקט מוחלט בלב סערת רעש חיצונית – רכבת רועשת, מטוס ממריא, או סתם המולה עירונית. אוזניות מבטלות רעשים מבטיחות בדיוק את זה, אבל לא על ידי חסימה פיזית בלבד. הן משתמשות בפיזיקה גאונית כדי "להעלים" את הרעש באופן פעיל. איך זה קורה? האם אפשר ליצור שקט באמצעות גלי קול אחרים?</p>

<div id="simulation-container">
  <div id="canvases-container">
    <div class="wave-label">🎧 רעש חיצוני (גל מקורי)</div>
    <canvas id="noise-wave-canvas"></canvas>
    <div class="wave-label">💡 אות מהאוזניה (גל 'אנטי-רעש')</div>
    <canvas id="headphone-wave-canvas"></canvas>
    <div class="wave-label">🔇 הגל השקול באוזן (התוצאה!)</div>
    <canvas id="result-wave-canvas"></canvas>
  </div>
  <div id="controls-container">
    <div class="control-group">
      <label for="amplitude-slider">עוצמת ('אמפליטודת') האות מהאוזניה:</label>
      <input type="range" id="amplitude-slider" min="0" max="100" value="100">
      <span id="amplitude-value">100%</span>
    </div>
    <div class="control-group">
      <label for="phase-toggle">היפוך פאזה ('הפוך' את הגל):</label>
      <button id="phase-toggle">0°</button>
    </div>
    <div class="control-tip">נסו להתאים את <strong>העוצמה</strong> ולהפוך את <strong>הפאזה</strong> כך שהגל השקול יהיה קו ישר ככל האפשר – זהו רגע ה"שקט" שנוצר!</div>
     <div id="cancellation-feedback"></div>
  </div>
</div>

<button id="toggle-explanation" aria-expanded="false">הצג/הסתר את הקסם: הסבר פיזיקלי מפורט</button>

<div id="explanation" class="collapsed" aria-hidden="true">
  <h2>הקסם הפיזיקלי מאחורי ביטול רעשים: התאבכות הורסת</h2>

  <p>כדי לפענח את סוד ביטול הרעשים הפעיל, נצא למסע אל עולם הגלים, ובפרט גלי הקול. אל דאגה, זה פשוט יותר ממה שזה נשמע!</p>

  <h3>מהו גל קול, בעצם?</h3>
  <p>דמיינו טיפת מים שנופלת לאגם – היא יוצרת אדוות שמתפשטות. גל קול דומה, רק שהוא "אדוות" של לחץ אוויר (או תווך אחר) שמתקדמות במרחב. כשאנו מדברים או שומעים מוזיקה, האוויר סביבנו רוטט. הרטיטות האלו מגיעות לאוזן שלנו, מזיזות את עור התוף, והמוח שלנו מפרש אותן כקול. גרפית, אפשר לייצג את גל הקול כעקומה שמתארת את שינויי לחץ האוויר לאורך זמן או מרחב.</p>

  <h3>המבנה הפנימי של גל: אמפליטודה, תדר ופאזה</h3>
  <p>כשמסתכלים על ייצוג גרפי של גל (כמו גל סינוס), מזהים שלושה מאפיינים קריטיים:</p>
  <ul>
    <li><strong>אמפליטודה (Amplitude):</strong> זהו הגובה המקסימלי של הגל מנקודת האפס (קו האמצע). באוזניות, האמפליטודה קשורה ישירות ל<strong>עוצמת הקול</strong> שאנו שומעים. אמפליטודה גדולה = קול חזק יותר.</li>
    <li><strong>תדר (Frequency):</strong> מספר מחזורי הגל שמתרחשים ביחידת זמן (לרוב בשנייה, נמדד בהרץ - Hz). הוא קובע את <strong>גובה הצליל</strong>. תדר גבוה = צליל גבוה (צפצוף), תדר נמוך = צליל נמוך (באס).</li>
    <li><strong>פאזה (Phase):</strong> זהו "מצב" הגל בנקודת זמן או מרחב מסוימת – היכן הוא מתחיל את המחזור שלו ביחס לנקודת ההתחלה. שני גלים יכולים להיות "באותה פאזה" (מסונכרנים, שיא פוגש שיא) או "בפאזה הפוכה" (הפרש של 180 מעלות, שיא פוגש שפל).</li>
  </ul>

  <h3>כשגלים נפגשים: עקרון הסופרפוזיציה</h3>
  <p>מה קורה כששני גלי קול או יותר מגיעים לאותה נקודה במרחב (למשל, בתוך האוזן שלכם) באותו זמן? הפיזיקה נותנת תשובה אלגנטית: ההפרעה הכוללת באותה נקודה היא פשוט **הסכום** של ההפרעות שיוצר כל גל בנפרד. זה נקרא "עקרון הסופרפוזיציה של גלים". הגל השקול שאתם שומעים הוא למעשה התוצאה של חיבור כל הגלים שנפגשים שם.</p>

  <h3>השפעת המפגש: התאבכות בונה והורסת</h3>
  <p>עקרון הסופרפוזיציה מוביל לשני סוגים מרהיבים של אינטראקציה בין גלים, המכונים "התאבכות":</p>
  <ul>
    <li><strong>התאבכות בונה (Constructive Interference):</strong> קורה כשגלים נפגשים כשהם "מסונכרנים" – באותה פאזה. שיא פוגש שיא, ושפל פוגש שפל. הגלים "מתחברים" ומחזקים זה את זה. הגל השקול שנוצר גדול יותר מהגלים המקוריים (אם הם זהים, האמפליטודה מוכפלת). עוצמת הקול עולה משמעותית!</li>
    <li><strong>התאבכות הורסת (Destructive Interference):</strong> זהו לב העניין של ביטול רעשים. קורה כשגלים נפגשים כשהם "לא מסונכרנים" לחלוטין – בפאזה הפוכה (הפרש 180 מעלות). השיא של גל אחד פוגש בדיוק את השפל של הגל השני, ולהיפך. אם לשני הגלים יש גם אותה אמפליטודה בדיוק, הם **מבטלים זה את זה לחלוטין!** הסכום שלהם הוא אפס, והתוצאה היא... שקט מוחלט (קו ישר בגרף). אם האמפליטודות קרובות אך לא זהות, מתרחש ביטול חלקי, והגל השקול קטן יותר.</li>
  </ul>

  <h3>ביטול רעשים פעיל הלכה למעשה: הגל ה"אנטי-רעש"</h3>
  <p>וכאן נכנסות לתמונה האוזניות החכמות. לאוזניות אקטיביות יש מיקרופון קטן שקולט את הרעש החיצוני שמנסה לחדור לאוזן (למשל, רעש מנוע או מזגן). האוזניה לא רק "מקשיבה" לרעש הזה, אלא גם מנתחת אותו בזמן אמת (זה קורה מהר מאוד!).</p>

  <p>מעבד זעיר באוזניה יוצר **בזמן אמת** גל קול חדש, גל "אנטי-רעש". הגל הזה מתוכנן בקפידה:</p>
  <ol>
    <li>הוא בעל <strong>אותה אמפליטודה</strong> כמו גל הרעש הנכנס.</li>
    <li>הוא נמצא <strong>בדיוק בפאזה הפוכה (180°)</strong> לגל הרעש הנכנס.</li>
  </ol>
  <p>לאחר מכן, האוזניה משמיעה את גל ה"אנטי-רעש" הזה, יחד עם המוזיקה או האודיו שאתם מאזינים לו, ישירות אל תוך האוזן שלכם.</p>

  <h3>השקט שנוצר: התאבכות הורסת בתוך האוזן</h3>
  <p>בתוך חלל האוזן (או התעלה הקטנה בתוך האוזניה עצמה), גל הרעש המקורי מהסביבה וגל ה"אנטי-רעש" שיצרה האוזניה נפגשים. מכיוון שהם נוצרו עם אותה אמפליטודה ונמצאים בפאזה הפוכה לחלוטין, הם עוברים **התאבכות הורסת**. התוצאה? הגלים מבטלים זה את זה באופן דרמטי! הרעש המקורי "נעלם" או מוחלש משמעותית עוד לפני שהוא מגיע לעור התוף. כך נוצרת סביבת שמיעה שקטה להפליא, שבה אתם יכולים לשמוע רק את מה שאתם רוצים לשמוע.</p>
  <p>זה לא קסם, זו פיזיקה בפעולה! השילוב המדויק של אמפליטודה ופאזה הפוכה מאפשר לגלים "להתנגש" ולהשמיד זה את זה, וליצור כיס אוויר של שקט בתוך האוזניות שלכם.</p>
</div>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const noiseCanvas = document.getElementById('noise-wave-canvas');
    const headphoneCanvas = document.getElementById('headphone-wave-canvas');
    const resultCanvas = document.getElementById('result-wave-canvas');
    const amplitudeSlider = document.getElementById('amplitude-slider');
    const amplitudeValueSpan = document.getElementById('amplitude-value');
    const phaseToggle = document.getElementById('phase-toggle');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const cancellationFeedback = document.getElementById('cancellation-feedback');

    const ctxNoise = noiseCanvas.getContext('2d');
    const ctxHeadphone = headphoneCanvas.getContext('2d');
    const ctxResult = resultCanvas.getContext('2d');

    let canvasWidth, canvasHeight, centerY;
    let noiseAmplitude;
    const noiseFrequency = 3; // 3 cycles across the canvas width
    const noisePhaseOffset = Math.PI / 4; // Some initial phase offset for visual appeal
    let time = 0; // For animation

    let headphoneAmplitudeMultiplier = amplitudeSlider.value / 100;
    let headphonePhaseOffset = 0; // 0 or Math.PI

    // Function to draw a single animated sine wave
    function drawWave(ctx, amplitude, frequency, phaseOffset, timeOffset, color = 'blue', fill = false) {
      ctx.clearRect(0, 0, canvasWidth, canvasHeight);

      // Draw X axis (center line) - slightly thicker or different color
      ctx.beginPath();
      ctx.strokeStyle = '#bbb'; // Lighter grey
      ctx.lineWidth = 1;
      ctx.moveTo(0, centerY);
      ctx.lineTo(canvasWidth, centerY);
      ctx.stroke();

      // Draw sine wave
      ctx.beginPath();
      ctx.strokeStyle = color;
      ctx.lineWidth = 3; // Thicker lines
      if (fill) {
          ctx.fillStyle = color + '30'; // Semi-transparent fill
          ctx.moveTo(0, centerY); // Start fill path at center line
      }


      for (let x = 0; x < canvasWidth; x++) {
        const angle = (x / canvasWidth) * (2 * Math.PI * frequency) + phaseOffset + timeOffset;
        const y = centerY - amplitude * Math.sin(angle);

        if (x === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }
       if (fill) {
          ctx.lineTo(canvasWidth, centerY); // End fill path at center line
          ctx.closePath();
          ctx.fill();
       } else {
           ctx.stroke();
       }
    }

    // Function to calculate and draw the resulting wave
    function drawResultWave() {
      ctxResult.clearRect(0, 0, canvasWidth, canvasHeight);

       // Draw X axis (center line) - emphasized for the result
      ctxResult.beginPath();
      ctxResult.strokeStyle = '#888'; // Slightly darker grey
      ctxResult.lineWidth = 1;
      ctxResult.moveTo(0, centerY);
      ctxResult.lineTo(canvasWidth, centerY);
      ctxResult.stroke();


      ctxResult.beginPath();
      ctxResult.strokeStyle = '#000'; // Black color for result
      ctxResult.lineWidth = 3; // Thicker line for result

      let totalDeviation = 0; // For feedback calculation

      for (let x = 0; x < canvasWidth; x++) {
        const angle = (x / canvasWidth) * (2 * Math.PI * noiseFrequency);

        // Calculate noise wave value (relative to center line) at current time
        const noiseYValue = noiseAmplitude * Math.sin(angle + noisePhaseOffset + time);

        // Calculate headphone wave value (relative to center line) at current time
        const currentHeadphoneAmplitude = noiseAmplitude * headphoneAmplitudeMultiplier;
        const headphoneYValue = currentHeadphoneAmplitude * Math.sin(angle + headphonePhaseOffset + time);

        // Sum the waves (Superposition)
        const resultYValue = noiseYValue + headphoneYValue;

        // Accumulate deviation for feedback
        totalDeviation += Math.abs(resultYValue);

        // Draw on canvas (remember y=0 is at the top, and we draw relative to centerY)
        const drawY = centerY - resultYValue;

        if (x === 0) {
          ctxResult.moveTo(x, drawY);
        } else {
          ctxResult.lineTo(x, drawY);
        }
      }
      ctxResult.stroke();

      // Calculate average deviation and update feedback
      const averageDeviation = totalDeviation / canvasWidth;
      const maxPossibleDeviation = noiseAmplitude * 2; // If waves added perfectly
      const cancellationPercentage = 100 - (averageDeviation / maxPossibleDeviation) * 100;

      updateFeedback(cancellationPercentage);
    }

    // Update feedback message based on cancellation percentage
    function updateFeedback(cancellationPercentage) {
       let feedbackText = '';
       let feedbackClass = '';

       if (cancellationPercentage > 95) {
           feedbackText = '⭐ שקט כמעט מוחלט! התאבכות הורסת מושלמת!';
           feedbackClass = 'feedback-great';
       } else if (cancellationPercentage > 70) {
            feedbackText = '✅ ביטול רעשים טוב! התאבכות הורסת יעילה.';
            feedbackClass = 'feedback-good';
       } else if (cancellationPercentage > 30) {
            feedbackText = '🤨 יש ביטול חלקי, אבל עדיין שומעים רעש.';
             feedbackClass = 'feedback-partial';
       }
       else {
            feedbackText = '🔊 רעש חזק! נסו לשנות את הגדרות האוזניה.';
            feedbackClass = 'feedback-noisy';
       }

       cancellationFeedback.textContent = feedbackText;
       cancellationFeedback.className = ''; // Clear previous classes
       cancellationFeedback.classList.add(feedbackClass);
    }


    // Animation loop
    function animate() {
      time += 0.05; // Increment time for animation speed
      updateSimulation();
      requestAnimationFrame(animate);
    }

    // Update all drawings
    function updateSimulation() {
      const timeOffset = time; // Pass current time for animation

      // Draw noise wave (fixed)
      drawWave(ctxNoise, noiseAmplitude, noiseFrequency, noisePhaseOffset, timeOffset, '#FF5733', true); // Reddish-orange, filled

      // Draw headphone wave (adjustable)
      const currentHeadphoneAmplitude = noiseAmplitude * headphoneAmplitudeMultiplier;
      drawWave(ctxHeadphone, currentHeadphoneAmplitude, noiseFrequency, headphonePhaseOffset, timeOffset, '#33A0FF', true); // Bluish, filled

      // Draw result wave
      drawResultWave();

      // Update amplitude value display
      amplitudeValueSpan.textContent = `${Math.round(headphoneAmplitudeMultiplier * 100)}%`;
    }

    // Set initial canvas dimensions and properties
    function setupCanvases() {
        // Get actual rendered size, not the CSS specified size directly
        const container = document.getElementById('canvases-container');
        canvasWidth = container.clientWidth; // Use container width
        canvasHeight = 100; // Keep fixed height as per CSS

        centerY = canvasHeight / 2;

        // Set canvas element size (this affects drawing surface)
        noiseCanvas.width = headphoneCanvas.width = resultCanvas.width = canvasWidth;
        noiseCanvas.height = headphoneCanvas.height = resultCanvas.height = canvasHeight;

        // Define noise amplitude relative to the canvas height
        noiseAmplitude = centerY * 0.7; // 70% of half height, allowing some room for peaks beyond view if desired (though not ideal)
    }


    // Event listeners for controls
    amplitudeSlider.addEventListener('input', (event) => {
      headphoneAmplitudeMultiplier = event.target.value / 100;
      // Animation loop will call updateSimulation
    });

    phaseToggle.addEventListener('click', () => {
      if (headphonePhaseOffset === 0) {
        headphonePhaseOffset = Math.PI; // 180 degrees
        phaseToggle.textContent = '180°';
        phaseToggle.classList.add('active');
      } else {
        headphonePhaseOffset = 0; // 0 degrees
        phaseToggle.textContent = '0°';
        phaseToggle.classList.remove('active');
      }
      // Animation loop will call updateSimulation
    });

     // Event listener for explanation button
     toggleExplanationButton.addEventListener('click', () => {
        const isCollapsed = explanationDiv.classList.contains('collapsed');
        if (isCollapsed) {
            explanationDiv.classList.remove('collapsed');
            explanationDiv.classList.add('expanded');
            explanationDiv.setAttribute('aria-hidden', 'false');
             toggleExplanationButton.setAttribute('aria-expanded', 'true');
        } else {
            explanationDiv.classList.remove('expanded');
            explanationDiv.classList.add('collapsed');
            explanationDiv.setAttribute('aria-hidden', 'true');
            toggleExplanationButton.setAttribute('aria-expanded', 'false');
        }
    });


    // Handle window resize (re-draw canvases with correct dimensions)
    window.addEventListener('resize', () => {
       setupCanvases(); // Recalculate dimensions and noiseAmplitude
       // Animation loop will call updateSimulation
    });

    // Initial setup and drawing
    setupCanvases();
    animate(); // Start the animation loop!
  });
</script>

<style>
  /* General Body/Container styles for better look */
  body {
      font-family: 'Arial', sans-serif;
      line-height: 1.6;
      color: #333;
      background-color: #f4f4f4;
      padding: 0;
      margin: 0;
  }

  p {
      margin-bottom: 1em;
  }

  #simulation-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px auto; /* Center the container */
    max-width: 800px; /* Limit max width */
    background-color: #fff; /* White background for simulation */
    border-radius: 12px; /* Rounded corners */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    overflow: hidden; /* Keep content within bounds */
  }

  #canvases-container {
    width: 100%;
    border-bottom: 1px solid #ddd;
    background-color: #f9f9f9; /* Light background for canvas area */
  }

  canvas {
    width: 100%;
    height: 100px; /* Fixed height for each wave */
    display: block;
    /* border-bottom: 1px dashed #eee; */ /* Removed inner borders, container border is enough */
  }
  canvas:last-child {
    border-bottom: none;
  }

  .wave-label {
    font-weight: bold;
    text-align: center;
    padding: 8px 0; /* More padding */
    background-color: #eef;
    font-size: 1.1em;
    color: #0056b3; /* Blue color for labels */
    border-bottom: 1px solid #ddd;
  }
    .wave-label:last-of-type {
        border-bottom: none;
    }


  #controls-container {
    width: 100%;
    padding: 20px; /* More padding */
    background-color: #e9e9e9; /* Slightly darker background for controls */
    border-radius: 0 0 12px 12px; /* Rounded bottom corners */
  }

  .control-group {
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
  }

  .control-group label {
    margin-right: 15px; /* More space */
    min-width: 220px; /* Give labels more room */
    font-weight: bold;
    color: #555; /* Darker grey */
    flex-shrink: 0; /* Prevent label from shrinking */
    margin-bottom: 5px; /* Space below label if wrapping */
  }

  .control-group input[type="range"] {
    flex-grow: 1;
    margin-right: 15px;
    -webkit-appearance: none; /* Override default styles */
    appearance: none;
    height: 8px;
    background: #ddd;
    border-radius: 5px;
    outline: none;
    opacity: 0.9;
    transition: opacity .2s;
  }

  .control-group input[type="range"]:hover {
    opacity: 1;
  }

  .control-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #fff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
  }

   .control-group input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #fff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
  }


  #amplitude-value {
    min-width: 60px; /* More width */
    text-align: right;
    font-weight: bold;
    color: #0056b3;
  }

  #phase-toggle {
    padding: 8px 15px;
    cursor: pointer;
    border: none; /* Remove border */
    background-color: #007bff;
    color: white;
    border-radius: 5px; /* Slightly more rounded */
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
    font-size: 1em;
    min-width: 80px; /* Consistent width */
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
  }

  #phase-toggle:hover {
      background-color: #0056b3;
  }

  #phase-toggle:active {
      transform: scale(0.98); /* Button press effect */
  }


  #phase-toggle.active {
     background-color: #dc3545; /* Red for 180 degrees */
     box-shadow: 0 2px 4px rgba(220,53,69,0.4);
  }

   #phase-toggle.active:hover {
      background-color: #c82333;
   }


  .control-tip {
      font-style: italic;
      text-align: center;
      margin-top: 15px; /* More space above tip */
      padding-top: 15px;
      border-top: 1px dashed #bbb;
      color: #555;
      font-size: 0.95em;
  }

  #cancellation-feedback {
      text-align: center;
      margin-top: 15px;
      padding: 10px;
      border-radius: 5px;
      font-weight: bold;
      min-height: 1.2em; /* Reserve space */
  }

  .feedback-great {
      background-color: #d4edda;
      color: #155724;
      border: 1px solid #c3e6cb;
  }

  .feedback-good {
      background-color: #ffeeba;
      color: #856404;
      border: 1px solid #ffc107;
  }

  .feedback-partial {
      background-color: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
  }
    .feedback-noisy {
      background-color: #e2e3e5;
      color: #383d41;
      border: 1px solid #d6d8db;
  }


  #toggle-explanation {
    display: block;
    margin: 30px auto; /* More margin */
    padding: 12px 25px; /* More padding */
    font-size: 1.1em; /* Slightly larger font */
    cursor: pointer;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
  }

  #toggle-explanation:hover {
    background-color: #218838;
  }

  #toggle-explanation:active {
      transform: scale(0.98);
  }


  #explanation {
    /* Initially hidden */
    margin: 20px auto;
    max-width: 800px;
    padding: 20px; /* More padding */
    border: 1px solid #eee;
    background-color: #fff; /* White background */
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    overflow: hidden; /* For smooth animation */
    transition: max-height 0.5s ease-in-out, opacity 0.5s ease-in-out;
  }

    #explanation.collapsed {
        max-height: 0;
        opacity: 0;
        padding-top: 0;
        padding-bottom: 0;
        border-color: transparent;
        margin-top: 0;
        margin-bottom: 0;
    }

     #explanation.expanded {
        max-height: 2000px; /* Needs to be larger than max possible content height */
        opacity: 1;
         padding-top: 20px;
        padding-bottom: 20px;
        border-color: #eee;
        margin-top: 20px;
         margin-bottom: 20px;
     }


  #explanation h2 {
    color: #0056b3;
    margin-top: 0; /* Adjust margin */
    margin-bottom: 15px; /* More space below title */
    border-bottom: 2px solid #007bff; /* More prominent border */
    padding-bottom: 8px;
    font-size: 1.6em;
  }
    #explanation h3 {
    color: #007bff;
    margin-top: 20px; /* More space above sub-headings */
    margin-bottom: 10px;
    font-size: 1.3em;
  }

  #explanation ul, #explanation ol {
    margin-left: 25px; /* More indent */
    margin-bottom: 15px;
    padding: 0; /* Remove default padding */
  }

  #explanation li {
    margin-bottom: 10px; /* More space between list items */
    line-height: 1.7; /* Improved readability */
    list-style-type: disc; /* Default bullet */
  }

  #explanation ol li {
      list-style-type: decimal; /* Numbered list */
  }

   #explanation p {
       margin-bottom: 15px; /* More space between paragraphs */
       line-height: 1.7;
       font-size: 1.05em;
   }

    /* Responsive adjustments */
    @media (max-width: 600px) {
        .control-group {
            flex-direction: column;
            align-items: stretch;
        }
        .control-group label {
            min-width: auto;
            margin-right: 0;
            margin-bottom: 8px;
        }
        .control-group input[type="range"] {
            margin-right: 0;
            margin-bottom: 8px;
        }
        #amplitude-value, #phase-toggle {
             align-self: flex-end; /* Align button/value to the right if column layout */
        }
         #amplitude-value {
             text-align: left;
         }
         #controls-container {
             padding: 15px;
         }
         #explanation {
             padding: 15px;
         }
         #explanation h2 {
             font-size: 1.4em;
         }
          #explanation h3 {
             font-size: 1.1em;
         }
          #explanation p, #explanation li {
             font-size: 1em;
          }
           #toggle-explanation {
             font-size: 1em;
             padding: 10px 20px;
           }
    }

</style>
---