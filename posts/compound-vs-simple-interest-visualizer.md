---
title: "הכוח החזותי של ריבית דריבית מול ריבית פשוטה: מחשבון אינטראקטיבי"
english_slug: compound-vs-simple-interest-visualizer
category: "מדעי החברה / כלכלה ופיננסים"
tags:
  - ריבית
  - חיסכון
  - השקעות
  - הדמיה
  - מתמטיקה פיננסית
---
# ראו בעצמכם: כיצד ריבית דריבית משנה את כללי המשחק

האם ידעתם שכסף יכול לגדול לאורך זמן, אבל האופן שבו הוא עושה זאת יכול להשתנות באופן דרמטי? דמיינו את הכסף שלכם כזרע קטן – ריבית פשוטה גורמת לו לגדול באופן קבוע, שנה אחר שנה. אבל ריבית דריבית? היא גורמת לזרע לא רק לגדול, אלא גם להוליד זרעים חדשים שממשיכים לגדול בעצמם!

בואו נצלול פנימה ונראה בדיוק איך הקסם הפיננסי הזה מתרחש. שחקו עם המספרים וגלו את הפוטנציאל העצום שמתחבא בריבית על ריבית.

<div class="interest-calculator-app">
    <div class="controls-panel">
        <div class="input-group">
            <label for="principal">סכום התחלתי:</label>
            <input type="number" id="principal" value="10000" min="100" step="100" aria-label="סכום ההשקעה ההתחלתי">
        </div>
        <div class="input-group">
            <label for="rate">ריבית שנתית (%):</label>
            <input type="number" id="rate" value="5" min="0.1" max="50" step="0.1" aria-label="שיעור הריבית השנתית באחוזים">
        </div>
        <div class="input-group">
            <label for="years">מספר שנים:</label>
            <input type="number" id="years" value="20" min="1" max="70" step="1" aria-label="מספר השנים לחישוב">
        </div>
        <!-- The calculate button is removed to enable live updates on input change -->
    </div>

    <div class="results-panel">
        <div class="result-box compound">
            <h3>ריבית דריבית</h3>
            <p class="result-label">סכום סופי משוער:</p>
            <span id="compound-result" class="result-value">-</span>
        </div>
        <div class="result-box simple">
            <h3>ריבית פשוטה</h3>
            <p class="result-label">סכום סופי משוער:</p>
            <span id="simple-result" class="result-value">-</span>
        </div>
        <div class="result-box difference">
             <h3>הפרש</h3>
             <p class="result-label">יתרון ריבית דריבית:</p>
             <span id="difference-result" class="result-value">-</span>
        </div>
    </div>

    <div class="graph-area">
        <canvas id="interestChart"></canvas>
    </div>
</div>

<button id="toggle-explanation" class="explanation-toggle-button">הבנתם את הכוח? לחצו להסבר מעמיק</button>

<div id="explanation" class="hidden">
    <h2>מאחורי הקסם: ריבית פשוטה מול ריבית דריבית</h2>
    <p>ההבדל היסודי והקריטי בין ריבית פשוטה לריבית דריבית הוא בבסיס החישוב לתקופות עתידיות. הבנה זו היא מהותית לכל מי שחוסך או משקיע לאורך זמן.</p>
    
    <h3>ריבית פשוטה (Simple Interest): הצמיחה הליניארית</h3>
    <p>בריבית פשוטה, הריבית מחושבת תמיד ורק על סכום ההתחלה שהפקדתם (הקרן). סכום הריבית שמתווסף בתקופת זמן נתונה (למשל, שנה) נשאר קבוע, בהנחה ששיעור הריבית קבוע. הנוסחה המתארת את הסכום הכולל (A) לאחר מספר מסוים של שנים (t), עם קרן התחלתית (P) וריבית שנתית (r), היא:</p>
    <p class="formula"><code>A = P * (1 + r * t)</code></p>
    <p>כמו שרואים בגרף, הגידול בסכום הכולל מתבטא בקו ישר ואחיד – צמיחה ליניארית.</p>

    <h3>ריבית דריבית (Compound Interest): הכוח האקספוננציאלי</h3>
    <p>בריבית דריבית, כאן קורה הדבר המרתק! הריבית מחושבת לא רק על הקרן המקורית, אלא גם על כל הריבית שכבר הספיקה להיצבר בתקופות הקודמות. למעשה, הכסף שלכם "מרוויח ריבית על הריבית" שכבר הרוויח. ככל שעובר יותר זמן, כך הריבית המצטברת הופכת לחלק גדול יותר מהסכום הכולל, והצמיחה מתעצמת ומאיצה. הנוסחה לחישוב הסכום הסופי (A) במקרה זה היא:</p>
    <p class="formula"><code>A = P * (1 + r)^t</code></p>
    <p>בגרף, הגידול בריבית דריבית נראה כעקומה שתלולה יותר ויותר עם הזמן – זוהי צמיחה אקספוננציאלית (מעריכית). ההבדל בין העקומה הזו לקו הישר של ריבית פשוטה מדגים את "הפער המצטבר", שהופך למשמעותי ביותר לאורך שנים רבות, במיוחד בריביות גבוהות או בסכומים גדולים יותר.</p>
    <p>אלברט איינשטיין כנראה לא אמר שריבית דריבית היא "הפלא השמיני של העולם", אבל התיאור הזה בהחלט מסביר את כוחה העצום ביצירת עושר לאורך זמן. ככל שמתחילים מוקדם יותר ומפקידים לאורך זמן רב יותר, כך כוח הריבית דריבית מתעצם.</p>
</div>

<style>
    :root {
        --primary-color: #007bff; /* Base Blue */
        --secondary-color: #28a745; /* Compound Green */
        --simple-color: #6610f2; /* Simple Purple/Indigo */
        --difference-color: #ffc107; /* Difference Yellow */
        --background-light: #f8f9fa;
        --background-mid: #e9ecef;
        --background-dark: #dee2e6;
        --text-color-dark: #212529;
        --text-color-light: #495057;
        --border-color: #ced4da;
        --radius-small: 4px;
        --radius-medium: 8px;
        --radius-large: 12px;
        --box-shadow-light: 0 4px 8px rgba(0, 0, 0, 0.08);
        --box-shadow-medium: 0 6px 12px rgba(0, 0, 0, 0.1);
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        background-color: var(--background-light);
        color: var(--text-color-dark);
        direction: rtl; /* Ensure RTL */
        text-align: right; /* Ensure right alignment */
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 1em;
    }
     h1 { font-size: 2em; margin-top: 0.5em; }
     h2 { font-size: 1.7em; margin-top: 1.5em; }
     h3 { font-size: 1.4em; margin-top: 1em; margin-bottom: 0.5em;}


    p {
        margin-bottom: 1em;
        color: var(--text-color-light);
    }

    .interest-calculator-app {
        background-color: #ffffff;
        padding: 30px;
        border-radius: var(--radius-large);
        box-shadow: var(--box-shadow-medium);
        margin-bottom: 30px;
        display: flex;
        flex-direction: column;
        gap: 30px;
    }

    .controls-panel {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
        align-items: flex-end;
        padding-bottom: 20px; /* Space below controls before results */
        border-bottom: 1px solid var(--background-dark);
    }

    .input-group {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    .input-group label {
        font-weight: bold;
        color: var(--text-color-dark);
        font-size: 0.95em;
    }

    .input-group input[type="number"] {
        padding: 12px 15px;
        border: 1px solid var(--border-color);
        border-radius: var(--radius-small);
        font-size: 1.1em;
        width: 100%; /* Make inputs full width */
        box-sizing: border-box; /* Include padding/border in width */
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .input-group input[type="number"]:focus {
        outline: none;
        border-color: var(--primary-color);
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
    }

    /* Hide default number input arrows */
    input[type="number"]::-webkit-inner-spin-button,
    input[type="number"]::-webkit-outer-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
    input[type="number"] {
        -moz-appearance: textfield; /* Firefox */
    }


    .results-panel {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 20px;
        text-align: center;
    }

    .result-box {
        background-color: var(--background-mid);
        padding: 20px;
        border-radius: var(--radius-medium);
        border: 1px solid var(--background-dark);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

     .result-box:hover {
         transform: translateY(-3px);
         box-shadow: var(--box-shadow-light);
     }

    .result-box.compound {
        background-color: rgba(40, 167, 69, 0.1); /* Light green tint */
        border-color: var(--secondary-color);
    }

    .result-box.simple {
        background-color: rgba(102, 16, 242, 0.1); /* Light purple tint */
        border-color: var(--simple-color);
    }
     .result-box.difference {
        background-color: rgba(255, 193, 7, 0.1); /* Light yellow tint */
        border-color: var(--difference-color);
    }


    .result-box h3 {
        margin-top: 0;
        margin-bottom: 0.5em;
        font-size: 1.2em;
    }
     .result-box.compound h3 { color: var(--secondary-color); }
    .result-box.simple h3 { color: var(--simple-color); }
     .result-box.difference h3 { color: var(--difference-color); }

     .result-label {
         font-size: 0.9em;
         color: var(--text-color-light);
         margin-bottom: 0.5em;
     }

    .result-value {
        font-size: 1.8em;
        font-weight: bold;
        color: var(--text-color-dark);
        display: block; /* Ensure it takes full width */
        min-height: 1.5em; /* Prevent layout shifts when value updates */
        transition: color 0.3s ease, transform 0.3s ease; /* Add animation for value changes */
    }

     /* Animation for result update */
     .result-value.pulsing {
         animation: pulse 0.5s ease-in-out;
     }

     @keyframes pulse {
         0% { transform: scale(1); color: var(--text-color-dark); }
         50% { transform: scale(1.05); color: var(--primary-color); } /* Pulse effect with color change */
         100% { transform: scale(1); color: var(--text-color-dark); }
     }


    .graph-area {
        width: 100%;
        max-width: 900px; /* Limit graph width */
        margin: 20px auto 0 auto; /* Center and space graph */
        background-color: #ffffff; /* White background for chart area */
        border-radius: var(--radius-medium);
        padding: 15px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    #interestChart {
         display: block;
         width: 100% !important; /* Override default inline styles */
         height: 450px !important; /* Fixed height for consistency, adjust as needed */
    }

    .explanation-toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: var(--text-color-light); /* Darker gray */
        color: white;
        border: none;
        border-radius: var(--radius-small);
        font-size: 1em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .explanation-toggle-button:hover {
        background-color: #5a6268; /* Slightly darker gray */
        transform: translateY(-1px);
    }

    .explanation-toggle-button:active {
        transform: translateY(0);
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }

    #explanation {
        background-color: var(--background-mid);
        padding: 30px;
        border-radius: var(--radius-large);
        box-shadow: var(--box-shadow-light);
        margin-top: 20px;
        border: 1px solid var(--background-dark);
    }

    #explanation.hidden {
        display: none;
    }

    #explanation h2 {
        margin-top: 0;
        color: var(--primary-color);
        text-align: right; /* Align explanation text right */
    }
     #explanation h3 {
         color: var(--text-color-dark); /* Use dark text for explanation subheadings */
         text-align: right;
     }

    .formula {
        font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
        background-color: var(--background-dark);
        padding: 10px 15px;
        border-radius: var(--radius-small);
        overflow-x: auto; /* Allow horizontal scroll if formula is too long */
        text-align: left; /* Formulas left-aligned for readability */
        direction: ltr;
        margin: 15px 0;
        font-size: 0.95em;
    }

    code {
        font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
    }

    /* Responsiveness */
    @media (max-width: 768px) {
        body {
            padding: 15px;
        }

        .interest-calculator-app {
            padding: 20px;
            gap: 20px;
        }

        .controls-panel, .results-panel {
            grid-template-columns: 1fr; /* Stack elements on small screens */
        }

        .graph-area {
             padding: 10px;
        }

        #interestChart {
            height: 300px !important; /* Reduce chart height on small screens */
        }

        .result-value {
            font-size: 1.5em;
        }
    }

    @media (max-width: 480px) {
         h1 { font-size: 1.7em; }
         h2 { font-size: 1.5em; }
         h3 { font-size: 1.3em; }

        .interest-calculator-app {
             padding: 15px;
        }

        .input-group input[type="number"],
        .explanation-toggle-button {
             font-size: 0.95em;
             padding: 10px 12px;
        }

        .result-box {
             padding: 15px;
        }

         .result-value {
             font-size: 1.3em;
         }

        .graph-area {
             margin-top: 15px;
        }

         #interestChart {
             height: 250px !important;
         }

        #explanation {
             padding: 20px;
        }
    }


</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const principalInput = document.getElementById('principal');
        const rateInput = document.getElementById('rate');
        const yearsInput = document.getElementById('years');
        // calculateButton is removed as calculation now happens on input
        const compoundResultSpan = document.getElementById('compound-result');
        const simpleResultSpan = document.getElementById('simple-result');
        const differenceResultSpan = document.getElementById('difference-result');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const ctx = document.getElementById('interestChart').getContext('2d');

        let interestChart = null; // Variable to hold the chart instance

        // Function to calculate values for each year
        function calculateInterestGrowth(principal, annualRate, years) {
            const simpleData = [];
            const compoundData = [];
            const rateDecimal = annualRate / 100;

            // Add year 0 data (initial principal)
             simpleData.push({ x: 0, y: principal });
             compoundData.push({ x: 0, y: principal });

            for (let year = 1; year <= years; year++) {
                // Simple Interest
                const simpleAmount = principal * (1 + rateDecimal * year);
                simpleData.push({ x: year, y: simpleAmount });

                // Compound Interest
                const compoundAmount = principal * Math.pow(1 + rateDecimal, year);
                compoundData.push({ x: year, y: compoundAmount });
            }

            return { simpleData, compoundData };
        }

        // Function to update results display with animation
        function updateResults(simpleTotal, compoundTotal) {
            const difference = compoundTotal - simpleTotal;

            animateResultUpdate(simpleResultSpan, formatCurrency(simpleTotal));
            animateResultUpdate(compoundResultSpan, formatCurrency(compoundTotal));
            animateResultUpdate(differenceResultSpan, formatCurrency(difference));
        }

         // Helper function to animate span update
        function animateResultUpdate(element, newValue) {
            const currentValue = element.textContent;
            if (currentValue !== newValue) {
                element.textContent = newValue;
                element.classList.remove('pulsing'); // Remove class to reset animation
                // Trigger reflow to restart animation
                void element.offsetWidth;
                element.classList.add('pulsing');
            }
        }


        // Function to format currency
        function formatCurrency(amount) {
            // Use minimumFractionDigits and maximumFractionDigits to control decimal places
            // Use minimumFractionDigits for clarity, maybe 0 for whole numbers, 2 for cents?
            // Let's use 0 for simplicity unless amount is less than 1000 or has decimal part
            let fractionDigits = 0;
             if (Math.abs(amount) < 1000 && !Number.isInteger(amount)) {
                fractionDigits = 2; // Show cents for smaller or non-integer amounts
            } else if (Math.abs(amount) < 100) {
                 fractionDigits = 2; // Always show cents for amounts less than 100
             }


            return new Intl.NumberFormat('he-IL', {
                style: 'currency',
                currency: 'ILS',
                minimumFractionDigits: fractionDigits,
                maximumFractionDigits: fractionDigits // Ensure consistent decimal places
            }).format(amount);
        }


        // Function to draw/update the chart
        function drawChart(simpleData, compoundData) {
            const years = compoundData.map(data => data.x); // Use compound data for labels as it's guaranteed to have all years
            const maxY = Math.max(...simpleData.map(d => d.y), ...compoundData.map(d => d.y));
            const suggestedMaxY = maxY > 0 ? Math.ceil(maxY * 1.1 / 1000) * 1000 : 1000; // Add 10% padding, round up, ensure min 1000

             if (interestChart) {
                interestChart.destroy(); // Destroy previous chart instance
            }

            interestChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: years, // X-axis labels (years)
                    datasets: [
                        {
                            label: 'ריבית פשוטה',
                            data: simpleData,
                            borderColor: var(--simple-color), /* Simple Purple */
                            backgroundColor: 'rgba(102, 16, 242, 0.15)',
                            fill: 'origin', // Fill area below the line
                            tension: 0.2, /* Add slight curve */
                            pointRadius: 0, /* Hide points */
                            pointHoverRadius: 6, /* Show points on hover */
                            pointBackgroundColor: var(--simple-color),
                             pointBorderColor: '#fff',
                             pointBorderWidth: 2,
                             borderWidth: 3
                        },
                        {
                            label: 'ריבית דריבית',
                            data: compoundData,
                            borderColor: var(--secondary-color), /* Compound Green */
                            backgroundColor: 'rgba(40, 167, 69, 0.15)',
                            fill: 'origin', // Fill area below the line
                            tension: 0.2, /* Add slight curve */
                            pointRadius: 0, /* Hide points */
                            pointHoverRadius: 6, /* Show points on hover */
                             pointBackgroundColor: var(--secondary-color),
                             pointBorderColor: '#fff',
                             pointBorderWidth: 2,
                            borderWidth: 3
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                     layout: {
                         padding: {
                             left: 5,
                             right: 5,
                             top: 10,
                             bottom: 5
                         }
                     },
                    scales: {
                        x: {
                            type: 'linear',
                            position: 'bottom',
                            title: {
                                display: true,
                                text: 'שנים',
                                font: { weight: 'bold', size: 14 }
                            },
                             min: 0, // Start X axis at 0
                            ticks: {
                                stepSize: years.length > 20 ? Math.max(5, Math.floor(years.length / 10)) : (years.length > 10 ? 2 : 1), // Dynamic step size
                                callback: function(value, index, values) {
                                     if (Number.isInteger(value)) {
                                        return value;
                                    }
                                    return null; // Only show integer years
                                },
                                color: var(--text-color-light)
                            },
                             grid: {
                                display: true, /* Show x-axis grid lines */
                                drawBorder: false,
                                color: var(--background-dark) /* Color for grid lines */
                            }
                        },
                        y: {
                            beginAtZero: true,
                             title: {
                                display: true,
                                text: 'סכום מצטבר (ש"ח)',
                                font: { weight: 'bold', size: 14 }
                            },
                            suggestedMax: suggestedMaxY,
                            ticks: {
                                 callback: function(value, index, values) {
                                    // Format Y-axis ticks (e.g., add K for thousands)
                                    if (value >= 1000000) {
                                        return (value / 1000000).toFixed(value % 1000000 === 0 ? 0 : 1) + 'M';
                                    } else if (value >= 1000) {
                                        return (value / 1000).toFixed(value % 1000 === 0 ? 0 : 1) + 'K';
                                    }
                                    return value;
                                },
                                color: var(--text-color-light)
                            },
                             grid: {
                                display: true, /* Show Y-axis grid lines */
                                drawBorder: false,
                                color: var(--background-dark) /* Color for grid lines */
                            }
                        }
                    },
                    plugins: {
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    let label = context.dataset.label || '';
                                    if (label) {
                                        label += ': ';
                                    }
                                    label += formatCurrency(context.parsed.y);
                                    return label;
                                },
                                title: function(context) {
                                     return `שנה: ${context[0].parsed.x}`;
                                }
                            },
                            rtl: true, /* Enable RTL for tooltips */
                             bodyFont: { size: 14 },
                             titleFont: { size: 14, weight: 'bold' },
                             padding: 10,
                             cornerRadius: var(--radius-small)
                        },
                         legend: {
                            position: 'bottom', /* Move legend to bottom */
                            labels: {
                                usePointStyle: true, /* Use circles instead of squares */
                                boxWidth: 10,
                                padding: 15,
                                font: { size: 13 }
                            },
                             rtl: true, /* Enable RTL for legend */
                             textDirection: 'rtl'
                        },
                         title: {
                             display: false, /* Hide default chart title as we have H1 */
                             // text: 'גידול הכסף לאורך שנים',
                             // font: { size: 16, weight: 'bold' }
                         }
                    },
                     animation: {
                        duration: 1200, /* Slightly longer animation */
                        easing: 'easeInOutQuart' /* Smoother easing */
                    },
                     hover: {
                        mode: 'nearest',
                        intersect: true
                     }
                }
            });
        }

        // Function to perform calculation and updates
        function performCalculationAndUpdate() {
            const principal = parseFloat(principalInput.value) || 0;
            const rate = parseFloat(rateInput.value) || 0;
            const years = parseInt(yearsInput.value, 10) || 0;

            // Basic validation (can be enhanced)
             if (principal < 0 || rate < 0 || years < 0) {
                 // Optional: show a subtle warning instead of alert
                 console.warn('Negative values are not typical for this calculation.');
                 // Use absolute values for calculation or keep last valid calculation?
                 // Let's just proceed with potentially zero values if inputs are invalid, but prevent negative input via min attribute.
             }

            const { simpleData, compoundData } = calculateInterestGrowth(principal, rate, years);

            // Get the final amounts for the result display
            const simpleTotal = simpleData.length > 0 ? simpleData[simpleData.length - 1].y : 0;
            const compoundTotal = compoundData.length > 0 ? compoundData[compoundData.length - 1].y : 0;

            updateResults(simpleTotal, compoundTotal);
            drawChart(simpleData, compoundData);
        }


        // Event listeners for input changes to trigger live update
         principalInput.addEventListener('input', performCalculationAndUpdate);
         rateInput.addEventListener('input', performCalculationAndUpdate);
         yearsInput.addEventListener('input', performCalculationAndUpdate);


        // Event listener for explanation button
        toggleExplanationButton.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
            if (!explanationDiv.classList.contains('hidden')) {
                 // Scroll smoothly to the explanation section after showing it
                 explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start', inline: 'nearest' });
                 toggleExplanationButton.textContent = 'הסתר הסבר'; // Change button text
             } else {
                 // Optional: Scroll back up to the calculator or keep position
                 // Keep position for now, only scroll down when showing
                 toggleExplanationButton.textContent = 'הבנתם את הכוח? לחצו להסבר מעמיק'; // Change button text back
             }
        });

        // Initial calculation on page load with default values
        performCalculationAndUpdate();
    });
</script>