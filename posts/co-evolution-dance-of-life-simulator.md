---
title: "אבולוציה משותפת: סימולטור הריקוד האבולוציוני"
english_slug: co-evolution-dance-of-life-simulator
category: "מדעי החיים / ביולוגיה"
tags:
- ביולוגיה
- אבולוציה
- אבולוציה משותפת
- האבקה
- ברירה טבעית
- סימולציה
- אינטראקציה ביולוגית
---
# אבולוציה משותפת: סימולטור הריקוד האבולוציוני

האם נדהמתם פעם מההתאמה המושלמת בין פרח למאביק שלו? איך חדק הפרפר מתאים בדיוק לעומק הצוף של הפרח? זו לא קסם, אלא "ריקוד" אבולוציוני שנמשך מיליוני שנים! בואו להיכנס למעבדת האבולוציה ולגלות בעצמכם כיצד שני מינים יכולים לעצב זה את זה באמצעות ברירה טבעית הדדית.

<div id="coevolution-simulator" class="interactive-module">
    <div class="controls-panel">
        <h2>מעבדת אבולוציה: הגדרות</h2>
        <div class="control-group">
            <label for="initial-plant-trait">מאפיין צמח התחלתי (למשל, עומק צוף):</label>
            <input type="number" id="initial-plant-trait" value="10" step="0.5" min="1">
            <span class="unit">(יחידות התאמה)</span>
        </div>
        <div class="control-group">
            <label for="initial-pollinator-trait">מאפיין מאביק התחלתי (למשל, אורך חדק):</label>
            <input type="number" id="initial-pollinator-trait" value="10" step="0.5" min="1">
             <span class="unit">(יחידות התאמה)</span>
        </div>
         <div class="control-group">
            <label for="population-size">גודל אוכלוסייה (לכל מין):</label>
            <input type="number" id="population-size" value="200" min="50" max="1000">
             <span class="unit">(פרטים)</span>
        </div>
        <div class="control-group">
            <label for="mutation-rate">עוצמת שינוי (מוטציה):</label>
            <input type="number" id="mutation-rate" value="0.8" step="0.1" min="0.1" max="5">
             <span class="unit">(פיזור תכונה)</span>
        </div>
        <div class="control-group">
            <label for="generations">משך הסימולציה (דורות):</label>
            <input type="number" id="generations" value="250" min="50" max="1000">
             <span class="unit">(דורות)</span>
        </div>
        <div class="button-group">
            <button id="start-simulation" class="action-button primary">התחל ריקוד!</button>
            <button id="reset-simulation" class="action-button secondary">התחל מחדש</button>
        </div>
    </div>
    <div class="simulation-results">
        <h2>הריקוד מתפתח: תוצאות</h2>
        <div class="chart-container">
             <canvas id="coevolution-chart"></canvas>
        </div>
        <div id="simulation-status" class="status-area">
            <span id="status-message">הגדר את הפרמטרים והתחל את הסימולציה.</span>
            <div id="current-state" style="display: none;">
                <div>דור נוכחי: <span id="current-generation">0</span></div>
                <div>ממוצע תכונת צמח: <span id="avg-plant-trait">-</span></div>
                <div>ממוצע תכונת מאביק: <span id="avg-pollinator-trait">-</span></div>
            </div>
        </div>
    </div>
</div>

<style>
/* סגנונות כלליים למודול האינטראקטיבי */
.interactive-module {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    flex-wrap: wrap;
    gap: 30px; /* הגדלת רווחים */
    margin: 30px 0; /* רווח מהתוכן שמסביב */
    padding: 25px; /* ריפוד פנימי */
    border: 1px solid #e0e0e0;
    border-radius: 12px; /* פינות מעוגלות יותר */
    background-color: #f8f8f8; /* רקע מעט אפור */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* הוספת צל עדין */
    direction: rtl; /* יישור לימין עבור עברית */
    text-align: right; /* יישור טקסט לימין */
}

/* סגנונות לפאנל הבקרות */
.controls-panel {
    flex: 1;
    min-width: 280px; /* הגדלת רוחב מינימלי */
    max-width: 400px; /* הגבלת רוחב מקסימלי */
    padding: 20px;
    background-color: #ffffff; /* רקע לבן */
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    display: flex;
    flex-direction: column;
    gap: 15px; /* רווח בין קבוצות בקרות */
}

.controls-panel h2 {
    color: #0056b3; /* כחול כהה לכותרת */
    margin-top: 0;
    margin-bottom: 20px;
    font-size: 1.5em;
    border-bottom: 2px solid #007bff; /* קו תחתון דקורטיבי */
    padding-bottom: 10px;
    text-align: center;
}

.control-group {
    margin-bottom: 15px; /* רווח בין פקדים */
}

.controls-panel label {
    display: block;
    margin-bottom: 8px; /* רווח מהאינפוט */
    font-weight: bold;
    color: #333; /* צבע טקסט כהה */
    font-size: 1em;
}

.controls-panel input[type="number"] {
    width: calc(100% - 60px); /* התאמת רוחב עם מקום ליחידה */
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 1em;
    box-sizing: border-box; /* כולל פדינג ובורדר ברוחב */
    transition: border-color 0.3s ease; /* אנימציית מעבר בצבע בורדר */
    display: inline-block;
    vertical-align: middle;
}

.controls-panel input[type="number"]:focus {
    border-color: #007bff; /* צבע בורדר בפוקוס */
    outline: none; /* הסרת האאוטליין המוגדר כברירת מחדל */
}

.control-group .unit {
    font-size: 0.9em;
    color: #555;
    margin-right: 5px; /* רווח מהאינפוט */
    display: inline-block;
    vertical-align: middle;
}


.button-group {
    margin-top: 20px;
    display: flex;
    gap: 15px; /* רווח בין כפתורים */
    justify-content: center; /* מרכז את הכפתורים */
}

.action-button {
    padding: 12px 25px; /* פדינג גדול יותר */
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.1em; /* גופן גדול יותר */
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease; /* אנימציות מעבר */
    text-align: center;
}

.action-button.primary {
    background-color: #28a745; /* ירוק */
    color: white;
}

.action-button.primary:hover {
    background-color: #218838; /* ירוק כהה יותר */
    transform: translateY(-1px); /* אפקט קפיצה קטן */
}

.action-button.primary:active {
     background-color: #1e7e34; /* ירוק כהה עוד יותר */
     transform: translateY(0);
}

.action-button.secondary {
    background-color: #dc3545; /* אדום */
    color: white;
}

.action-button.secondary:hover {
    background-color: #c82333; /* אדום כהה יותר */
     transform: translateY(-1px);
}
.action-button.secondary:active {
     background-color: #bd2130; /* אדום כהה עוד יותר */
     transform: translateY(0);
}

.action-button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    transform: none;
}

/* סגנונות לאזור התוצאות */
.simulation-results {
    flex: 2;
    min-width: 350px; /* רוחב מינימלי גדול יותר לגרף */
    padding: 20px;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px; /* רווח בין כותרת, גרף, וסטטוס */
}

.simulation-results h2 {
    color: #0056b3;
    margin-top: 0;
    margin-bottom: 10px;
    font-size: 1.5em;
    border-bottom: 2px solid #007bff;
    padding-bottom: 5px;
    width: 100%; /* קו תחתון לכל רוחב */
    text-align: center;
}

.chart-container {
    width: 100%;
    max-width: 700px; /* רוחב מקסימלי לגרף */
    height: 350px; /* גובה גדול יותר לגרף */
    position: relative; /* מאפשר מיקום אבסולוטי אם צריך */
}

#coevolution-chart {
    width: 100% !important; /* דורס הגדרות אינליין אם יש */
    height: 100% !important;
}

.status-area {
    margin-top: 15px;
    padding: 10px 15px;
    background-color: #e9ecef; /* רקע בהיר לסטטוס */
    border-radius: 8px;
    font-size: 0.95em;
    color: #343a40; /* צבע טקסט כהה */
    width: 100%;
    text-align: center;
}

#current-state div {
    margin-top: 5px;
    font-weight: bold;
}

#current-state span {
    font-weight: normal;
    color: #007bff; /* צבע כחול לערכים */
}


/* סגנונות לכפתור הצגת/הסתרת הסבר */
#explanation-toggle {
    display: block;
    width: fit-content;
    margin: 30px auto; /* ממיר margin 20px למרווח גדול יותר */
    padding: 12px 25px; /* פדינג גדול יותר */
    background-color: #007bff; /* כחול */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.1em;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease;
}

#explanation-toggle:hover {
    background-color: #0056b3; /* כחול כהה יותר */
     transform: translateY(-1px);
}
#explanation-toggle:active {
     background-color: #004085;
     transform: translateY(0);
}


/* סגנונות לאזור ההסבר */
#explanation {
    margin-top: 20px;
    padding: 25px;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    background-color: #f8f8f8;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    display: none; /* Initially hidden */
    line-height: 1.7; /* מרווח שורות נוח לקריאה */
    color: #333;
}

#explanation h2 {
    color: #0056b3;
    margin-top: 15px;
    margin-bottom: 15px;
    border-bottom: 2px solid #007bff;
    padding-bottom: 8px;
    font-size: 1.4em;
}

#explanation h3 {
    color: #007bff;
    margin-top: 15px;
    margin-bottom: 10px;
    font-size: 1.2em;
}

#explanation p {
    margin-bottom: 15px;
}

#explanation ul {
    margin-bottom: 15px;
    padding-right: 20px; /* הזחה לרשימה */
}

#explanation li {
    margin-bottom: 8px;
}

/* רספונסיביות בסיסית */
@media (max-width: 768px) {
    .interactive-module {
        flex-direction: column;
        gap: 20px;
        padding: 15px;
    }

    .controls-panel, .simulation-results {
        min-width: 100%;
        max-width: 100%;
    }

    .button-group {
        flex-direction: column;
        gap: 10px;
    }

    .action-button {
        width: 100%;
    }

    .chart-container {
        height: 300px; /* גובה גרף מעט קטן יותר בנייד */
    }
}

</style>

<button id="explanation-toggle">הצג/הסתר את הסבר המודל</button>

<div id="explanation">
    <h2>מהו הריקוד האבולוציוני המשותף?</h2>
    <p>דמיינו שני רקדנים, צמח ומאביק. כל תנועה של רקדן אחד משפיעה על התנועה של הרקדן השני, ולהיפך. לאורך אלפי דורות, "הריקוד" הזה, או ליתר דיוק – האבולוציה המשותפת (Co-evolution), מעצבת אותם באופן הדדי ליצירת התאמות מדהימות ולעיתים קיצוניות.</p>
    <p>אבולוציה משותפת מתרחשת כאשר שני מינים או יותר מקיימים אינטראקציה קרובה, ושינויים אבולוציוניים במין אחד מפעילים לחץ ברירה טבעית על המין השני, שבתורו מגיב בשינויים משלו, וחוזר חלילה.</p>

    <h3>יחסי צמח-מאביק: סיפור אהבה הדדי</h3>
    <p>אחד המודלים הקלאסיים לאבולוציה משותפת הוא מערכת היחסים בין פרחים למאביקים שלהם, כמו דבורים, פרפרים, עשים, ציפורי יונק דבש או עטלפים. זוהי דוגמה למוטואליזם – יחסים שמועילים לשני הצדדים:</p>
    <ul>
        <li>**עבור הצמח:** האבקה יעילה, המובילה לרבייה מוצלחת. הצמח "משקיע" באטרקציות כמו צבעים בולטים, ריחות, צוף מתוק, ואבקה מזינה כדי למשוך את המאביקים הנכונים.</li>
        <li>**עבור המאביק:** מקור מזון חיוני (צוף או אבקה). המאביק "מתמחה" בגישה למשאבים אלו על ידי פיתוח מבנים גופניים כמו חדק ארוך, כושר ראייה מותאם לצבעי הפרח, או יכולת ניווט.</li>
    </ul>
    <p>בסימולטור זה, ה"מאפיין" יכול לייצג, לדוגמה, את עומק צינור הצוף של הפרח ואת אורך החדק של המאביק. ככל שהמאפיינים קרובים יותר, כך ההתאמה טובה יותר, ושני הצדדים מרוויחים יותר (הצמח מואבק ביעילות, והמאביק מקבל מזון).</p>

    <h3>מרוץ חימוש או ריקוד תיאום?</h3>
    <p>לחץ הברירה הטבעית פועל כאן באופן הדדי. נניח שמופיע פרח עם צינור צוף מעט ארוך מהרגיל (מוטציה). פרח זה יואבק רק על ידי מאביקים עם חדק ארוך יותר שיוכלו להגיע לצוף. מאביקים אלה, בתמורה, ייהנו ממקור מזון פחות נגיש למתחרים, מה שיגדיל את סיכויי שרידתם ורבייתם. הדור הבא של המאביקים יכלול יותר פרטים עם חדק ארוך. עכשיו, עבור הצמח, פרחים עם צינור צוף ארוך יותר יקבלו יותר האבקה מהמאביקים המותאמים הללו, מה שיגדיל את סיכויי רבייתם. לאורך דורות, ממוצע עומק הצוף בפרחים וממוצע אורך החדק במאביקים עשויים לעלות באופן מתואם - מעין "מרוץ חימוש" שבו כל צד דוחף את השני להתפתח.</p>
    <p>שיעור המוטציה קובע את מגוון התכונות המופיע בכל דור. מוטציה גבוהה יותר פירושה יותר שינויים פתאומיים ואקראיים בתכונות, בעוד שמוטציה נמוכה יותר מובילה לשינויים הדרגתיים יותר.</p>

    <h3>מעבר למוטואליזם</h3>
    <p>חשוב לזכור שאבולוציה משותפת אינה מוגבלת ליחסים מועילים. היא מתרחשת גם ביחסי טורף-נטרף (הטורף מתפתח להיות צייד טוב יותר, הנטרף מפתח הגנות), טפיל-פונדקאי, ותחרות.</p>
    <p>הסימולטור מאפשר לכם לשחק עם הפרמטרים ולראות כיצד הם משפיעים על ה"ריקוד" לאורך דורות רבים. האם התכונות מתכנסות? מתרחקות? רודפות זו אחר זו? גלו בעצמכם!</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
document.addEventListener('DOMContentLoaded', () => {
    // Get DOM elements
    const initialPlantTraitInput = document.getElementById('initial-plant-trait');
    const initialPollinatorTraitInput = document.getElementById('initial-pollinator-trait');
    const populationSizeInput = document.getElementById('population-size');
    const mutationRateInput = document.getElementById('mutation-rate');
    const generationsInput = document.getElementById('generations');
    const startButton = document.getElementById('start-simulation');
    const resetButton = document.getElementById('reset-simulation');
    const statusMessageSpan = document.getElementById('status-message');
    const currentStateDiv = document.getElementById('current-state');
    const currentGenerationSpan = document.getElementById('current-generation');
    const avgPlantTraitSpan = document.getElementById('avg-plant-trait');
    const avgPollinatorTraitSpan = document.getElementById('avg-pollinator-trait');
    const explanationToggle = document.getElementById('explanation-toggle');
    const explanationDiv = document.getElementById('explanation');
    const ctx = document.getElementById('coevolution-chart').getContext('2d');

    let chart = null; // Use null to check if chart exists
    let simulationRunning = false;
    let animationFrameId = null; // To store the ID returned by requestAnimationFrame

    // --- Simulation Core Functions (Kept simple as per structure constraint) ---

    function initializePopulations(size, initialPlantTrait, initialPollinatorTrait) {
        // Create populations with initial traits
        const plants = Array(size).fill(0).map(() => ({ trait: initialPlantTrait }));
        const pollinators = Array(size).fill(0).map(() => ({ trait: initialPollinatorTrait }));
        return { plants, pollinators };
    }

    function calculateMatchQuality(traitA, traitB) {
        // Simple fitness function: better match means higher fitness
        // Using a negative exponential of the squared difference
        const difference = Math.abs(traitA - traitB);
        const sensitivity = 0.05; // Lower sensitivity makes broader match acceptable
        return Math.exp(-(difference * difference) * sensitivity);
    }

    function reproduce(population, partnerPopulation, mutationRate, originalPopulationSize) {
        const nextGeneration = [];
        const partnerAvgTrait = getAverageTrait(partnerPopulation);

        // Calculate fitness for each individual based on match with partner population average
        const fitnessScores = population.map(individual => calculateMatchQuality(individual.trait, partnerAvgTrait));

        const totalFitness = fitnessScores.reduce((sum, fitness) => sum + fitness, 0);

        if (totalFitness === 0) {
             // If total fitness is zero (e.g., perfect mismatch and no mutation previously),
             // allow minimal random reproduction with high mutation to potentially escape
             console.warn("Total fitness is zero, adding random drift.");
             return Array(originalPopulationSize).fill(0).map(() => ({ trait: population[0].trait + (Math.random() - 0.5) * mutationRate * 5 }));
        }


        // Select individuals for reproduction using fitness proportional selection (roulette wheel)
        for (let i = 0; i < originalPopulationSize; i++) {
            let runningSum = 0;
            let randomIndex = Math.random() * totalFitness;
            let selectedParent = null;

            for (let j = 0; j < population.length; j++) {
                runningSum += fitnessScores[j];
                if (runningSum >= randomIndex) {
                    selectedParent = population[j];
                    break;
                }
            }

            // Fallback if no parent selected (shouldn't happen with totalFitness > 0, but good practice)
            if (!selectedParent) {
                 selectedParent = population[Math.floor(Math.random() * population.length)];
            }

            // Create offspring with mutation
            // Mutation adds a random value from a normal-like distribution (Box-Muller or summing uniforms)
            // For simplicity, using two uniforms:
            const mutation = (Math.random() + Math.random() - 1) * mutationRate; // Range approx -mutationRate to +mutationRate
            let newTrait = selectedParent.trait + mutation;

             // Optional: Add bounds to traits if needed, though co-evolution often leads to extremes
             // if (newTrait < 1) newTrait = 1; // Example lower bound

            nextGeneration.push({ trait: newTrait });
        }

        return nextGeneration;
    }

    function getAverageTrait(population) {
        if (population.length === 0) return 0;
        const sum = population.reduce((sum, individual) => sum + individual.trait, 0);
        return sum / population.length;
    }

    // --- Chart and UI Update Functions ---

    function createChart(generations, plantTraits, pollinatorTraits) {
         if (chart) {
             chart.destroy(); // Destroy existing chart before creating a new one
         }

        chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: generations,
                datasets: [
                    {
                        label: 'ממוצע תכונת צמח',
                        borderColor: '#28a745', /* ירוק */
                        backgroundColor: 'rgba(40, 167, 69, 0.2)',
                        data: plantTraits,
                        fill: false,
                        tension: 0.1 /* מעט עקמומיות בקו */
                    },
                    {
                        label: 'ממוצע תכונת מאביק',
                        borderColor: '#007bff', /* כחול */
                         backgroundColor: 'rgba(0, 123, 255, 0.2)',
                        data: pollinatorTraits,
                        fill: false,
                        tension: 0.1 /* מעט עקמומיות בקו */
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                 plugins: {
                     title: {
                        display: true,
                        text: 'התפתחות ממוצע התכונות לאורך דורות',
                         font: {
                             size: 16,
                             family: 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif'
                         },
                         color: '#333'
                    },
                     tooltip: {
                         rtl: true,
                         callbacks: {
                             label: function(context) {
                                 let label = context.dataset.label || '';
                                 if (label) {
                                     label += ': ';
                                 }
                                 if (context.parsed.y !== null) {
                                     label += context.parsed.y.toFixed(2); // הצג 2 ספרות אחרי הנקודה
                                 }
                                 return label;
                             }
                         }
                     }
                 },
                 hover: {
                     mode: 'nearest',
                     intersect: true
                 },
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'דור',
                             font: {
                                 size: 14,
                                  family: 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif'
                             },
                             color: '#555'
                        },
                         ticks: {
                             autoSkip: true,
                             maxTicksLimit: 20
                         }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'ערך תכונה ממוצע',
                             font: {
                                 size: 14,
                                 family: 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif'
                             },
                            color: '#555'
                        }
                    }
                }
            }
        });
    }

    function updateChart(generations, plantTraits, pollinatorTraits) {
        if (chart) {
            chart.data.labels = generations;
            chart.data.datasets[0].data = plantTraits;
            chart.data.datasets[1].data = pollinatorTraits;
            chart.update();
        }
    }

    function updateStatus(message, generation, plantTrait, pollinatorTrait, isRunning) {
        statusMessageSpan.textContent = message;
        if (isRunning) {
            currentStateDiv.style.display = 'block';
            currentGenerationSpan.textContent = generation;
            avgPlantTraitSpan.textContent = plantTrait.toFixed(2); // Format to 2 decimal places
            avgPollinatorTraitSpan.textContent = pollinatorTrait.toFixed(2); // Format to 2 decimal places
        } else {
             currentStateDiv.style.display = 'none';
        }
    }


    // --- Simulation Control Flow ---

    function runSimulation() {
        const initialPlantTrait = parseFloat(initialPlantTraitInput.value);
        const initialPollinatorTrait = parseFloat(initialPollinatorTraitInput.value);
        const populationSize = parseInt(populationSizeInput.value);
        const mutationRate = parseFloat(mutationRateInput.value);
        const totalGenerations = parseInt(generationsInput.value);

        // Basic validation
        if (isNaN(initialPlantTrait) || isNaN(initialPollinatorTrait) || isNaN(populationSize) || isNaN(mutationRate) || isNaN(totalGenerations) || populationSize < 10 || totalGenerations < 10 || mutationRate < 0) {
            updateStatus('אנא הכנס ערכים חוקיים.', 0, 0, 0, false);
            return;
        }
         if (initialPlantTrait <= 0 || initialPollinatorTrait <= 0) {
              updateStatus('מאפייני התחלה חייבים להיות חיוביים.', 0, 0, 0, false);
             return;
         }


        resetSimulation(); // Ensure clean state
        simulationRunning = true;
        startButton.disabled = true;
        resetButton.disabled = false;

        let { plants, pollinators } = initializePopulations(populationSize, initialPlantTrait, initialPollinatorTrait);

        const plantTraitsHistory = [getAverageTrait(plants)];
        const pollinatorTraitsHistory = [getAverageTrait(pollinators)];
        const generationsHistory = [0];

        createChart(generationsHistory, plantTraitsHistory, pollinatorTraitsHistory);
        updateStatus('מתחילים סימולציה...', 0, plantTraitsHistory[0], pollinatorTraitsHistory[0], true);


        const simulationLoop = (generation) => {
            if (!simulationRunning || generation >= totalGenerations) {
                simulationRunning = false; // Ensure flag is false on finish
                startButton.disabled = false;
                resetButton.disabled = false; // Allow reset after finishing
                 updateStatus(`הסימולציה הסתיימה לאחר ${generation} דורות.`, generation, plantTraitsHistory[plantTraitsHistory.length - 1], pollinatorTraitsHistory[pollinatorTraitsHistory.length - 1], false);

                 // Ensure the last state is shown if it was running
                 currentGenerationSpan.textContent = generation;
                 avgPlantTraitSpan.textContent = plantTraitsHistory[plantTraitsHistory.length - 1].toFixed(2);
                 avgPollinatorTraitSpan.textContent = pollinatorTraitsHistory[pollinatorTraitsHistory.length - 1].toFixed(2);
                 currentStateDiv.style.display = 'block';


                return;
            }

            // Simulate reproduction
            const nextPlants = reproduce(plants, pollinators, mutationRate, populationSize);
            const nextPollinators = reproduce(pollinators, plants, mutationRate, populationSize);

            plants = nextPlants;
            pollinators = nextPollinators;

            generationsHistory.push(generation + 1);
            plantTraitsHistory.push(getAverageTrait(plants));
            pollinatorTraitsHistory.push(getAverageTrait(pollinators));

            updateChart(generationsHistory, plantTraitsHistory, pollinatorTraitsHistory);
            updateStatus(`דור ${generation + 1}/${totalGenerations} בעיצומו...`, generation + 1, plantTraitsHistory[plantTraitsHistory.length - 1], pollinatorTraitsHistory[pollinatorTraitsHistory.length - 1], true);

            // Continue loop
             animationFrameId = requestAnimationFrame(() => simulationLoop(generation + 1));
        };

        // Start the loop
        simulationLoop(0);
    }

    function resetSimulation() {
         if (animationFrameId) {
            cancelAnimationFrame(animationFrameId); // Stop the animation loop
            animationFrameId = null;
         }
         simulationRunning = false; // Set flag to false

         // Clear the chart
         if (chart) {
             chart.destroy();
             chart = null;
         }
         // Ensure canvas is clear - destroy *should* handle this, but being explicit doesn't hurt
          const canvas = document.getElementById('coevolution-chart');
          if (canvas) {
              const context = canvas.getContext('2d');
              context.clearRect(0, 0, canvas.width, canvas.height);
              // Optional: Re-add initial empty state drawing if desired
          }


         updateStatus('הסימולציה מאופסת. הגדר פרמטרים חדשים.', 0, 0, 0, false);
         startButton.disabled = false;
         resetButton.disabled = true; // Disable reset until simulation starts again

         // Clear displayed current state values
         currentGenerationSpan.textContent = '0';
         avgPlantTraitSpan.textContent = '-';
         avgPollinatorTraitSpan.textContent = '-';
         currentStateDiv.style.display = 'none';
    }


    // --- Event Listeners ---

    startButton.addEventListener('click', runSimulation);
    resetButton.addEventListener('click', resetSimulation);

    explanationToggle.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationToggle.textContent = isHidden ? 'הסתר את הסבר המודל' : 'הצג את הסבר המודל';
    });

    // --- Initialization ---
    resetButton.disabled = true; // Disable reset initially
    explanationDiv.style.display = 'none'; // Hide explanation by default
    explanationToggle.textContent = 'הצג את הסבר המודל'; // Set initial button text
     currentStateDiv.style.display = 'none'; // Hide current state display initially
});
</script>