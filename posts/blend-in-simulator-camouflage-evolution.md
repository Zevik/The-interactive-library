---
title: "אמני ההסוואה: סימולטור ברירה טבעית"
english_slug: blend-in-simulator-camouflage-evolution
category: "ביולוגיה"
tags: ["אבולוציה", "ברירה טבעית", "הסוואה", "התאמה", "סימולציה", "משחק לימודי"]
---
<h1>אמני ההסוואה: סימולטור ברירה טבעית</h1>
<p class="intro-paragraph">איך בעלי חיים מסוימים מצליחים להיעלם כמעט לחלוטין בסביבתם? האם זה קסם, או תהליך מדהים שמתפתח במשך דורות? צאו למסע מרתק בזמן והתנסו בעצמכם כיצד כוחות הטבע מעצבים את היכולת המופלאה הזו להשתלב ולהישאר בחיים. צפו באוכלוסייה של יצורים קטנים מתפתחת מול עיניכם והתאימו את עצמכם לסביבה המשתנה!</p>

<div id="simulation-container">
    <div id="environment" class="environment-brown">
        <!-- Creatures will be added here by JavaScript -->
    </div>
    <div id="controls">
        <div class="control-group">
            <label for="environment-select">משנים את העולם:</label>
            <select id="environment-select">
                <option value="brown">אדמה מדברית</option>
                <option value="green">צמחייה טרופית</option>
            </select>
        </div>
        <button id="start-stop-sim" class="action-button">מתחילים במסע!</button>
        <div id="status">
            <p>דור: <span id="generation-count">0</span></p>
            <p>אוכלוסייה: <span id="population-count">0</span></p>
        </div>
    </div>
</div>

<style>
    /* כללי: שיפור פונטים, רקעים, מרווחים ופינות מעוגלות */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f0f4f8; /* רקע עדין לאתר כולו */
    }

    h1 {
        text-align: center;
        color: #1a237e; /* כותרת בצבע כחול כהה יותר */
        margin-bottom: 10px;
    }

    .intro-paragraph {
        text-align: center;
        max-width: 700px;
        margin: 0 auto 20px auto;
        font-size: 1.1rem;
        color: #555;
    }

    #simulation-container {
        max-width: 800px;
        margin: 20px auto;
        border: none; /* מסגרת מוסרת לטובת צל */
        padding: 20px; /* הגדלת ריפוד */
        background-color: #ffffff; /* רקע לבן למיכל הסימולציה */
        border-radius: 12px; /* פינות מעוגלות יותר */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* הוספת צל עדין */
        overflow: hidden; /* לוודא שהכל בפנים */
    }

    #environment {
        width: 100%;
        height: 450px; /* הגדלת גובה הסביבה */
        position: relative;
        border: none; /* מסגרת מוסרת */
        overflow: hidden;
        background-size: cover;
        background-position: center;
        border-radius: 8px; /* פינות מעוגלות לסביבה עצמה */
        transition: background-image 0.5s ease, background-color 0.5s ease; /* אנימציה לשינוי סביבה */
    }

    /* רקעים משודרגים לסביבות - שימוש בצבעים עשירים יותר או טקסטורות בסיסיות */
    .environment-brown {
        /* צבע חום עשיר יותר */
        background-color: #8b4513; /* SaddleBrown */
        /* אפשר להוסיף גרדיאנט או טקסטורה בסיסית */
        /* background-image: linear-gradient(to bottom right, #a0522d, #8b4513); */
         background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWF... (replace with a better base64 texture if desired, or keep simple color)');
         /* example base64 for noise: */
         background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAHCAYAAACSZHlKAQAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAB9JREFUeNqUlEENACAMA0e09f+HwYQvCxqE+fJ3Y0oAAJ8E/bV2Zg8AAAAASUVORK5CYII=');
         background-repeat: repeat;
         background-size: 7px 7px; /* Adjust size based on texture */

    }

    .environment-green {
         /* צבע ירוק עשיר יותר */
         background-color: #2e8b57; /* SeaGreen */
         /* background-image: linear-gradient(to bottom right, #3cb371, #2e8b57); */
         /* example base64 for noise: */
          background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAHCAYAAACSZHlKAQAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAB9JREFUeNqUlEENACAMA0e09f+HwYQvCxqE+fJ3Y0oAAJ8E/bV2Zg8AAAAASUVORK5CYII=');
          background-repeat: repeat;
          background-size: 7px 7px; /* Adjust size based on texture */
    }

    .creature {
        position: absolute;
        width: 10px; /* הגדלת גודל יצור מעט */
        height: 10px;
        border-radius: 50%;
        box-sizing: border-box;
        opacity: 1; /* התחלה עם אטימות מלאה */
        transition: opacity 0.4s ease-out; /* אנימציה לעמעום */
        /* Add a subtle border for definition against various backgrounds */
        border: 1px solid rgba(0, 0, 0, 0.1);
        /* No transition on background-color to avoid visual lag during updates */
    }

    /* אנימציה ליצורים שמוסרים (נאכלו) */
    .creature.fading-out {
        opacity: 0;
    }

    #controls {
        margin-top: 20px; /* הגדלת מרווח עליון */
        display: flex;
        justify-content: center; /* מרכוז הפקדים */
        align-items: center;
        gap: 25px; /* הגדלת הרווח בין הפקדים */
        flex-wrap: wrap;
        padding: 10px 0;
    }

    .control-group {
         display: flex;
         align-items: center;
         gap: 8px;
    }

    #controls label {
        font-weight: bold;
        color: #333;
        font-size: 1rem;
    }

    #controls select,
    #controls button {
        padding: 10px 15px; /* הגדלת ריפוד כפתורים/סלקט */
        border: 1px solid #c0c0c0; /* מסגרת עדינה יותר */
        border-radius: 6px; /* פינות מעוגלות יותר */
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    #controls select {
        background-color: #f9f9f9;
    }

    .action-button {
        background-color: #4CAF50; /* ירוק - צבע פעולה */
        color: white;
        border-color: #4CAF50;
    }

    .action-button:hover {
        background-color: #45a049;
        border-color: #45a049;
        box-shadow: 0 3px 8px rgba(0,0,0,0.15);
    }

     #start-stop-sim.running {
         background-color: #f44336; /* אדום כשפועל */
         border-color: #f44336;
     }

     #start-stop-sim.running:hover {
         background-color: #d32f2f;
         border-color: #d32f2f;
     }


    #controls select:focus,
    #controls button:focus {
        outline: none;
        border-color: #007bff;
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
    }


    #status {
        display: flex;
        gap: 30px; /* הגדלת רווח */
        font-size: 1.1rem; /* הגדלת גודל פונט */
        margin-right: 0; /* ביטול push ל right כדי לשמור על מרכוז */
        color: #1a237e;
    }

    #status p {
        margin: 0;
        font-weight: bold;
    }

    #status span {
        font-weight: normal; /* להבליט רק את הטקסט 'דור'/'אוכלוסייה' */
        color: #555;
    }


    /* סגנון להסבר */
    #explanation {
        margin-top: 30px; /* הגדלת מרווח עליון */
        padding: 25px; /* הגדלת ריפוד */
        border: none; /* מסגרת מוסרת */
        background-color: #e3f2fd; /* רקע תכלת עדין */
        border-radius: 12px; /* פינות מעוגלות */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08); /* צל עדין */
    }

    #explanation h2 {
        margin-top: 0;
        color: #1a237e;
        border-bottom: 2px solid #bbdefb; /* קו תחתון לכותרת */
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    #explanation h3 {
        color: #333;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    #explanation p, #explanation ul {
        line-height: 1.7;
        color: #555;
        margin-bottom: 15px;
    }

    #explanation ul {
        padding-left: 25px; /* הגדלת הזחה */
    }

    #explanation li {
        margin-bottom: 10px; /* הגדלת מרווח בין פריטים */
    }

    #toggle-explanation {
        display: block;
        margin: 30px auto; /* הגדלת מרווח עליון ותחתון */
        padding: 12px 25px; /* הגדלת ריפוד */
        font-size: 1.1rem;
        cursor: pointer;
        border: none;
        background-color: #007bff; /* כחול */
        color: white;
        border-radius: 6px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
    }

    #toggle-explanation:hover {
        background-color: #0056b3;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    }

    #toggle-explanation:active {
         background-color: #003f7f;
         box-shadow: none;
    }

</style>

<button id="toggle-explanation">הצג לי את הקסם!</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: מסע האבולוציה דרך הסוואה</h2>
    <p>הסימולציה המרתקת הזו מדגימה כיצד כוחה של הברירה הטבעית מניע תהליכי התאמה בסביבה. במקרה שלנו, נראה איך אוכלוסייה של יצורים קטנים "לומדת" להשתלב בסביבתה באמצעות שינויים הדרגתיים בצבע הגוף לאורך דורות.</p>

    <h3>למה הסוואה היא סופר-פאוור הישרדותי?</h3>
    <p>הסוואה היא הרבה יותר מסתם "להיות יפה" בצבע הרקע. זוהי אסטרטגיית הישרדות קריטית! יצור שמצליח להתמזג בסביבתו מקשה מאוד על טורפים למצוא אותו. ככל שיצור מוסווה טוב יותר, כך עולים סיכוייו לחמוק מסכנה, להגיע לבגרות, ולחשוב - הכי חשוב - להעביר את הגנים ה"טובים" שלו הלאה לדור הבא.</p>

    <h3>ברירה טבעית: המנוע של השינוי</h3>
    <p>האבולוציה, התפתחות החיים על פני כדור הארץ, מונעת בעיקר על ידי מנגנון שנקרא "ברירה טבעית". הסימולציה מדגימה את עקרונות הליבה שלו:</p>
    <ul>
        <li><strong>שונות מטריפה (Variation):</strong> אף פעם אין שני יצורים זהים לחלוטין (אפילו באוכלוסייה המדומה שלנו). תמיד יש שונות קלה בתכונות, במקרה זה - בצבע הגוף. השונות הזו היא חומר הגלם של האבולוציה.</li>
        <li><strong>תורשה עוברת מדור לדור (Inheritance):</strong> התכונות הללו, כולל צבע הגוף, עוברות מהורים לצאצאים. אמנם יש "טעויות העתקה" קטנות (מוטציות אקראיות) בכל דור, אבל הבסיס התורשתי נשמר.</li>
        <li><strong>השורדים שמעבירים הלאה (Differential Survival and Reproduction):</strong> וזה לב העניין! בסימולציה שלנו, ה"טורף" (שנעלם מהעין אך עושה את עבודתו!) 'צד' את היצורים הבולטים ביותר, אלו שהכי קל לזהות על רקע הסביבה. היצורים המוסווים טוב יותר שורדים בשיעורים גבוהים יותר, ולכן הם אלו שמתרבים ומעבירים את תכונות הצבע שלהם לילדיהם.</li>
    </ul>
    <p>ככה, לאורך דורות, התכונות שמסייעות להישרדות (הסוואה מעולה!) הופכות להיות יותר ויותר נפוצות באוכלוסייה כולה.</p>

    <h3>איך זה בא לידי ביטוי בסימולציה?</h3>
    <p>בכל "דור" בסימולציה, אנו מדמים אירוע הישרדות. היצורים שצבעם קרוב יותר לצבע הרקע מקבלים "ציון הסוואה" גבוה יותר, ולכן סיכוייהם לשרוד את ה"ציד" הווירטואלי גדולים יותר. רק אלו ששורדים זוכים להעמיד צאצאים. הצאצאים יורשים את צבע הוריהם, בתוספת שינוי אקראי זעיר (המוטציה). התוצאה? דור אחר דור, ממוצע הצבע באוכלוסייה הולך ומתקרב לצבע הסביבה, והאוכלוסייה כולה הופכת להיות מוסווית יותר ויותר!</p>

    <h3>סוגי הסוואה: לא רק צבע!</h3>
    <p>בטבע, הסוואה לובשת צורות רבות ומגוונות מעבר להתאמת צבע פשוטה:</p>
    <ul>
        <li><strong>הסוואה מתמזגת (Cryptic Coloration):</strong> הצבע והדפוסים על הגוף מחקים את הרקע באופן ישיר (נחש חום על אדמה חומה, זחל ירוק על עלה ירוק).</li>
        <li><strong>צביעה מבליטה ( Disruptive Coloration):</strong> פסים או כתמים עזים שדווקא "שוברים" את צורת הגוף ומקשים על הטורף לזהות שמדובר בבעל חיים (דוגמה קלאסית: פסי זברה).</li>
        <li><strong>חיקוי (Mimicry):</strong> בעל חיים מחקה מראה של בעל חיים אחר, לרוב מסוכן או בלתי טעים, כדי להרתיע טורפים (לדוגמה, זבוב לא מזיק שמחקה מראה של צרעה).</li>
        <li><strong>הסוואת תנועה (Motion Camouflage):</strong> שינוי מיקום יחסית לטורף באופן שגורם לו להיראות כאילו הוא לא זז, עד הרגע האחרון.</li>
    </ul>

    <h3>מה קורה כשעוברים דירה? (שינוי סביבה)</h3>
    <p>אחד הניסויים המעניינים ביותר בסימולציה הוא שינוי הסביבה באמצע התהליך! אם תעברו מרקע חום לירוק (או להיפך), תראו שהצבעים שהיו מצוינים להישרדות הופכים לפתע לבולטים ומסוכנים. לחץ הברירה ישתנה באופן דרמטי, ורק היצורים שצבעם במקרה קרוב יותר לרקע החדש, יחד עם הצאצאים הנושאים מוטציות בכיוון הנכון, יתחילו לשגשג. לאורך דורות נוספים, האוכלוסייה תתחיל שוב להתאים את עצמה לסביבה החדשה - זוהי עדות מדהימה לגמישות ולעוצמה של הברירה הטבעית!</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const environmentDiv = document.getElementById('environment');
        const environmentSelect = document.getElementById('environment-select');
        const startStopButton = document.getElementById('start-stop-sim');
        const generationCountSpan = document.getElementById('generation-count');
        const populationCountSpan = document.getElementById('population-count');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');

        let creatures = [];
        const initialPopulationSize = 150;
        const creatureSize = 10; // px (increased from 8)
        const mutationRate = 15; // Max +/- change in camouflage value per generation (increased from 10)
        const survivalRate = 0.65; // Percentage of population that survives each round (slightly adjusted)
        const simulationSpeed = 80; // Milliseconds per generation (faster)

        let simulationInterval = null;
        let isRunning = false;
        let generation = 0;
        let creatureIdCounter = 0; // To assign unique IDs

        // Map environment types to target camouflage values (0-255)
        // 0 is darkest, 255 is lightest (conceptually, mapped to HSL hue later)
        const environmentTargets = {
            'brown': 50, // Target darker creatures for brown environment
            'green': 200 // Target lighter creatures for green environment
        };

        // --- Color Mapping Enhancement ---
        // Map value (0-255) to a color gradient that visually matches the environments.
        // Use HSL color space for better control.
        // Value 0 should map to a brown-like color, 255 to a green-like color.
        function getCreatureColor(value) {
            // Ensure value is clamped
            const clampedValue = Math.max(0, Math.min(255, value));

            // Interpolate between two HSL colors (e.g., a brown and a green)
            const brownHSL = { h: 30, s: 60, l: 20 }; // Example brown HSL (Hue, Saturation, Lightness)
            const greenHSL = { h: 120, s: 50, l: 30 }; // Example green HSL

            // Simple linear interpolation for each component
            const h = brownHSL.h + (clampedValue / 255) * (greenHSL.h - brownHSL.h);
            const s = brownHSL.s + (clampedValue / 255) * (greenHSL.s - brownHSL.s);
            const l = brownHSL.l + (clampedValue / 255) * (greenHSL.l - brownHSL.l);

             // Slight adjustment to lightness based on value for better contrast range?
             // Or just use the linear interpolation result. Let's stick to linear.

            return `hsl(${h}, ${s}%, ${l}%)`;
        }

        // --- Camouflage Score Enhancement ---
        // The scoring logic is already good - closer to target is better.
        function getCamouflageScore(creatureValue, environmentType) {
            const targetValue = environmentTargets[environmentType];
            const difference = Math.abs(creatureValue - targetValue);
            const maxDifference = 255;

            // Use a non-linear scoring function? For now, linear is clear and functional.
            // Score from 1 to 100 (or any arbitrary range)
            const maxScore = 100;
            const minScore = 10; // Ensure minimum survival chance for some diversity
            return maxScore - (difference / maxDifference) * (maxScore - minScore);
        }

        // --- Core Simulation Logic (Refinement) ---

        function initializePopulation() {
            creatures = [];
            environmentDiv.innerHTML = ''; // Clear previous creatures
            generation = 0;
            creatureIdCounter = 0; // Reset ID counter
            generationCountSpan.textContent = generation;

            const envRect = environmentDiv.getBoundingClientRect();
            const maxX = envRect.width - creatureSize;
            const maxY = envRect.height - creatureSize;

            for (let i = 0; i < initialPopulationSize; i++) {
                const creature = {
                    id: creatureIdCounter++,
                    x: Math.random() * maxX,
                    y: Math.random() * maxY,
                    // Start with random camouflage values across the full range
                    camouflageValue: Math.random() * 255
                };
                creatures.push(creature);
                createCreatureElement(creature); // Creates element and adds to DOM
            }
            populationCountSpan.textContent = creatures.length;
            // Initial colors are set by createCreatureElement
        }

        // --- Visuals & DOM Manipulation ---

        function createCreatureElement(creature) {
            const element = document.createElement('div');
            element.classList.add('creature');
            element.style.width = `${creatureSize}px`;
            element.style.height = `${creatureSize}px`;
            element.style.left = `${creature.x}px`;
            element.style.top = `${creature.y}px`;
            element.id = `creature-${creature.id}`;
            element.style.backgroundColor = getCreatureColor(creature.camouflageValue);

            // Optional: Add a slight initial fade-in animation
             element.style.opacity = 0; // Start invisible
             environmentDiv.appendChild(element);
             // Trigger fade-in after adding to DOM
             requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                    element.style.opacity = 1;
                });
             });
        }

        function removeCreatureElement(creature) {
            const element = document.getElementById(`creature-${creature.id}`);
            if (element) {
                // Add a class to trigger fade-out animation
                element.classList.add('fading-out');
                // Remove the element after the animation duration
                // The CSS transition is 0.4s, add a small buffer
                setTimeout(() => {
                    element.remove();
                }, 400); // Match this duration to the CSS transition
            }
        }


        function runGeneration() {
            generation++;
            generationCountSpan.textContent = generation;

            const currentEnvironment = environmentSelect.value;

            // 1. Selection (Hunting)
            const creaturesWithScores = creatures.map(creature => {
                const score = getCamouflageScore(creature.camouflageValue, currentEnvironment);
                return { creature, score };
            });

            // Sort creatures by camouflage score (lowest first) to easily select survivors
            creaturesWithScores.sort((a, b) => a.score - b.score);

            const numToSurvive = Math.round(initialPopulationSize * survivalRate);
            const survivors = creaturesWithScores.slice(creaturesWithScores.length - numToSurvive).map(item => item.creature);

            // Identify who was killed
            const killed = creatures.filter(c => !survivors.includes(c));

            // --- Animation: Trigger fade-out for killed creatures ---
            killed.forEach(creature => {
                 removeCreatureElement(creature);
            });

            // 2. Reproduction
            const newGeneration = [];
            const numToReproduce = initialPopulationSize - survivors.length;

            if (survivors.length > 0) {
                for (let i = 0; i < numToReproduce; i++) {
                    // Select a random survivor to reproduce (with replacement)
                    const parent = survivors[Math.floor(Math.random() * survivors.length)];

                    // Create offspring with inherited trait + mutation
                    const mutation = (Math.random() - 0.5) * 2 * mutationRate; // Mutation between -mutationRate and +mutationRate
                    let offspringValue = parent.camouflageValue + mutation;

                    // Clamp value to 0-255 range
                    offspringValue = Math.max(0, Math.min(255, offspringValue));

                    const envRect = environmentDiv.getBoundingClientRect();
                    const maxX = envRect.width - creatureSize;
                    const maxY = envRect.height - creatureSize;

                    const offspring = {
                         id: creatureIdCounter++, // Assign unique ID
                         x: Math.random() * maxX,
                         y: Math.random() * maxY,
                         camouflageValue: offspringValue
                    };
                    newGeneration.push(offspring);
                    // --- Animation: createCreatureElement now handles fade-in ---
                    createCreatureElement(offspring);
                }
            } else {
                 // This scenario should be rare with survivalRate > 0
                 console.warn("All creatures died. Simulation cannot reproduce.");
                 stopSimulation();
            }

            // Update the main creatures array
            creatures = survivors.concat(newGeneration);
            populationCountSpan.textContent = creatures.length;

            // No need to call updateCreatureColors explicitly per generation
            // as colors are set when elements are created.
        }

        function startSimulation() {
            if (isRunning) return;
            isRunning = true;
            startStopButton.textContent = 'עצור סימולציה';
            startStopButton.classList.add('running'); // Add class for styling

            // Ensure population exists before starting
            if (creatures.length === 0 || parseInt(populationCountSpan.textContent) === 0) {
                initializePopulation();
            } else {
                // If restarting after stopping, clear any lingering fade-out animations
                 document.querySelectorAll('.creature.fading-out').forEach(el => el.remove());
            }

            simulationInterval = setInterval(runGeneration, simulationSpeed);
        }

        function stopSimulation() {
            if (!isRunning) return;
            isRunning = false;
            startStopButton.textContent = 'התחל סימולציה';
            startStopButton.classList.remove('running'); // Remove class for styling
            clearInterval(simulationInterval);
            simulationInterval = null;
        }

        function toggleSimulation() {
            if (isRunning) {
                stopSimulation();
            } else {
                startSimulation();
            }
        }

        function changeEnvironment() {
            const selectedEnvironment = environmentSelect.value;
            // Use requestAnimationFrame to ensure class change applies visually before creature colors update?
            // Or just change the class directly. The CSS transition handles the background visual change.
            // The simulation logic (runGeneration) will automatically use the new target.
            // No need to update creature colors *visually* based on environment change
            // as their color represents their inherited trait, not their current survival chance.
            environmentDiv.className = ''; // Remove previous class
            environmentDiv.classList.add('environment-' + selectedEnvironment);

            // Optional: Immediately apply camouflage scoring visual cue if implemented (not currently)
            // updateCreatureColors(); // Call if creature colors had e.g. a border indicating score
        }

        function toggleExplanation() {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג לי את הקסם!';
        }

        // Event Listeners
        startStopButton.addEventListener('click', toggleSimulation);
        environmentSelect.addEventListener('change', changeEnvironment);
        toggleExplanationButton.addEventListener('click', toggleExplanation);


        // Initial setup
        initializePopulation();
        // Ensure the correct environment class is set initially based on default select value
        changeEnvironment();
    });
</script>
```