---
title: "המספר 1: יחידה, בסיס וזהות"
category: "מתמטיקה"
tags: [מתמטיקה, מספרים, המספר 1, חשבון, זהות כפלית]
---

# המספר 1: יותר מסתם ספרה

המספר 1 נראה פשוט, אך הוא אחד המספרים החשובים והבסיסיים ביותר במתמטיקה. הוא משמש כאבן בניין ליצירת כל שאר המספרים הטבעיים, הוא בעל תכונה ייחודית בפעולת הכפל, והוא מייצג את מושג ה"שלם" שממנו נגזרים השברים.

בדף זה נחקור שלוש תכונות מרכזיות של המספר 1 דרך כלים אינטראקטיביים פשוטים.

## 1. אבן הבניין של המספרים

כל מספר טבעי (1, 2, 3, ...) יכול להיווצר על ידי חיבור של המספר 1 לעצמו. 1 הוא המספר הראשון, והוא הבסיס שממנו צומחת כל שרשרת המספרים.

**הדגמה:** לחצו על הכפתור "+1" וראו כיצד אתם בונים את המספרים הבאים בתור, לבנה אחר לבנה.

<div id="number-one-app-container">
    <div class="interactive-section" id="builder-app">
        <h3>בניית מספרים מ-1</h3>
        <div class="builder-controls">
            <button id="add-one-btn" aria-label="הוסף 1">+ 1</button>
            <button id="reset-builder-btn" aria-label="אפס">אפס</button>
        </div>
        <div class="builder-display">
            <div class="current-number-display">
                <span id="number-display">1</span>
            </div>
            <div id="blocks-container">
                <div class="block">1</div>
            </div>
        </div>
    </div>

## 2. הזהות השקטה: 1 בכפל

למספר 1 יש תפקיד מיוחד בכפל: כל מספר שתכפילו ב-1 יישאר ללא שינוי. תכונה זו נקראת "איבר יחידה (או זהות) כפלי". זה אולי נשמע מובן מאליו, אבל זוהי תכונת יסוד באלגברה.

**הדגמה:** הכניסו מספר כלשהו ל"מכונת הכפל" וראו כיצד המספר 1 שומר על זהותו.

    <div class="interactive-section" id="identity-app">
        <h3>מכונת הזהות הכפלית</h3>
        <div class="identity-machine">
            <label for="identity-input">הכנס מספר:</label>
            <input type="number" id="identity-input" value="17" placeholder="הכנס מספר">
            <div class="machine-arrow">× 1 ➔</div>
            <div class="identity-output-container">
                <span>תוצאה:</span>
                <span id="identity-output">17</span>
            </div>
        </div>
    </div>

## 3. האחד השלם: בסיס לשברים

המספר 1 מייצג לא רק כמות, אלא גם רעיון של "שלם" או "יחידה". מעגל שלם, פיצה שלמה, 100% - כולם ייצוגים של 1. כאשר אנו מחלקים את השלם לחלקים שווים, אנחנו יוצרים שברים.

**הדגמה:** בחרו בכמה חלקים לחלק את העיגול השלם כדי לראות כיצד נוצרים שברים מהיחידה.

    <div class="interactive-section" id="unit-app">
        <h3>מהשלם אל החלק</h3>
        <div class="unit-controls">
            <span>חלק את השלם ל:</span>
            <button class="slice-btn" data-slices="2">2</button>
            <button class="slice-btn" data-slices="3">3</button>
            <button class="slice-btn" data-slices="4">4</button>
            <button class="slice-btn" data-slices="5">5</button>
            <button class="slice-btn" data-slices="6">6</button>
            <button class="slice-btn" data-slices="1">1</button>
        </div>
        <div class="unit-display">
            <svg id="pie-chart" viewBox="0 0 100 100"></svg>
        </div>
        <div id="fraction-label">1</div>
    </div>

## בחן את עצמך

עכשיו, אחרי שחקרנו את תכונותיו של המספר 1, בואו נבדוק מה למדנו במבחן קצר.

    <div class="interactive-section" id="quiz-app">
        <h3>מבחן קצר על המספר 1</h3>
        <div id="quiz-container">
            <div id="quiz-question"></div>
            <div id="quiz-options"></div>
            <div id="quiz-feedback"></div>
            <button id="quiz-next-btn" style="display: none;">השאלה הבאה</button>
        </div>
        <div id="quiz-results" style="display: none;"></div>
    </div>
</div>

<style>
    :root {
        --primary-bg: #f7f9fc;
        --secondary-bg: #ffffff;
        --text-color: #333;
        --primary-accent: #007bff;
        --secondary-accent: #ff9800;
        --success-color: #28a745;
        --danger-color: #dc3545;
        --border-color: #e0e0e0;
        --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    #number-one-app-container {
        font-family: var(--font-family);
        color: var(--text-color);
        direction: rtl;
        text-align: right;
    }

    .interactive-section {
        background-color: var(--secondary-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        overflow: hidden;
    }

    .interactive-section h3 {
        margin-top: 0;
        color: var(--primary-accent);
        border-bottom: 2px solid var(--secondary-accent);
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
    
    button {
        font-family: inherit;
        font-size: 1rem;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
        background-color: var(--primary-accent);
        color: white;
    }

    button:hover {
        opacity: 0.85;
        transform: translateY(-2px);
    }
    
    button:disabled {
        background-color: #ccc;
        cursor: not-allowed;
        transform: none;
    }

    /* Builder App */
    .builder-controls {
        display: flex;
        gap: 0.75rem;
        margin-bottom: 1.5rem;
    }

    #reset-builder-btn {
        background-color: #6c757d;
    }

    .builder-display {
        display: flex;
        align-items: center;
        gap: 1.5rem;
        flex-wrap: wrap;
    }

    .current-number-display {
        font-size: 3rem;
        font-weight: bold;
        color: var(--secondary-accent);
    }
    
    #blocks-container {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        flex: 1;
        background: var(--primary-bg);
        padding: 10px;
        border-radius: 8px;
        min-height: 50px;
    }

    .block {
        width: 30px;
        height: 30px;
        background-color: var(--primary-accent);
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 4px;
        font-size: 0.8rem;
        animation: popIn 0.3s ease;
    }
    
    @keyframes popIn {
        from { transform: scale(0.5); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }


    /* Identity App */
    .identity-machine {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 1rem;
    }

    #identity-input {
        padding: 0.6rem;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        font-size: 1.2rem;
        width: 100px;
        text-align: center;
    }

    .machine-arrow {
        font-size: 1.5rem;
        font-weight: bold;
        color: var(--primary-accent);
    }

    .identity-output-container {
        display: flex;
        align-items: baseline;
        gap: 0.5rem;
        font-size: 1.2rem;
    }

    #identity-output {
        font-size: 1.8rem;
        font-weight: bold;
        color: var(--secondary-accent);
        min-width: 50px;
        text-align: center;
    }

    /* Unit App */
    .unit-controls {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
    }

    .unit-controls .slice-btn {
        background-color: #6c757d;
        min-width: 40px;
    }
    
    .unit-controls .slice-btn.active {
        background-color: var(--secondary-accent);
        box-shadow: 0 0 0 3px rgba(255, 152, 0, 0.4);
    }

    .unit-display {
        width: 100%;
        max-width: 200px;
        margin: 0 auto;
    }

    #pie-chart path {
        transition: all 0.5s ease-in-out;
        stroke: white;
        stroke-width: 2px;
    }

    #fraction-label {
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        margin-top: 1rem;
        color: var(--primary-accent);
    }
    
    /* Quiz App */
    #quiz-question {
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 1.5rem;
    }
    #quiz-options {
        display: grid;
        grid-template-columns: 1fr;
        gap: 0.75rem;
    }
    .quiz-option {
        width: 100%;
        text-align: right;
        background-color: white;
        color: var(--primary-accent);
        border: 2px solid var(--primary-accent);
    }
    .quiz-option:not(:disabled):hover {
        background-color: #e6f2ff;
    }
    .quiz-option.correct {
        background-color: var(--success-color);
        border-color: var(--success-color);
        color: white;
    }
    .quiz-option.incorrect {
        background-color: var(--danger-color);
        border-color: var(--danger-color);
        color: white;
    }
    #quiz-feedback {
        margin-top: 1rem;
        font-weight: bold;
        min-height: 24px;
    }
    #quiz-next-btn {
        margin-top: 1rem;
        background-color: var(--secondary-accent);
    }
    #quiz-results {
        text-align: center;
        font-size: 1.5rem;
    }

    @media (min-width: 768px) {
        #quiz-options {
            grid-template-columns: 1fr 1fr;
        }
    }
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {

    // --- App 1: Builder ---
    const addOneBtn = document.getElementById('add-one-btn');
    const resetBuilderBtn = document.getElementById('reset-builder-btn');
    const numberDisplay = document.getElementById('number-display');
    const blocksContainer = document.getElementById('blocks-container');

    let currentNumber = 1;

    const resetBuilder = () => {
        currentNumber = 1;
        numberDisplay.textContent = currentNumber;
        blocksContainer.innerHTML = '<div class="block">1</div>';
    };

    addOneBtn.addEventListener('click', () => {
        currentNumber++;
        numberDisplay.textContent = currentNumber;
        const newBlock = document.createElement('div');
        newBlock.classList.add('block');
        newBlock.textContent = '1';
        blocksContainer.appendChild(newBlock);
    });

    resetBuilderBtn.addEventListener('click', resetBuilder);

    // --- App 2: Identity Machine ---
    const identityInput = document.getElementById('identity-input');
    const identityOutput = document.getElementById('identity-output');

    identityInput.addEventListener('input', () => {
        const num = identityInput.value;
        identityOutput.textContent = num;
    });

    // --- App 3: Unit App (Pie Chart) ---
    const pieChart = document.getElementById('pie-chart');
    const unitControls = document.querySelector('.unit-controls');
    const fractionLabel = document.getElementById('fraction-label');
    const sliceButtons = document.querySelectorAll('.slice-btn');
    const colors = ['#007bff', '#ff9800', '#28a745', '#dc3545', '#6f42c1', '#20c997'];

    function createPieSlice(cx, cy, r, startAngle, endAngle, color) {
        const start = polarToCartesian(cx, cy, r, endAngle);
        const end = polarToCartesian(cx, cy, r, startAngle);
        
        const largeArcFlag = endAngle - startAngle <= 180 ? "0" : "1";

        const d = [
            "M", cx, cy, 
            "L", start.x, start.y, 
            "A", r, r, 0, largeArcFlag, 0, end.x, end.y,
            "Z"
        ].join(" ");

        const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        path.setAttribute("d", d);
        path.setAttribute("fill", color);
        return path;
    }

    function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
        const angleInRadians = (angleInDegrees-90) * Math.PI / 180.0;
        return {
            x: centerX + (radius * Math.cos(angleInRadians)),
            y: centerY + (radius * Math.sin(angleInRadians))
        };
    }

    function drawPie(slices) {
        pieChart.innerHTML = '';
        if (slices === 1) {
            const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            circle.setAttribute("cx", 50);
            circle.setAttribute("cy", 50);
            circle.setAttribute("r", 48); // a bit smaller to show stroke
            circle.setAttribute("fill", colors[0]);
            pieChart.appendChild(circle);
            fractionLabel.textContent = '1';
            return;
        }

        const sliceAngle = 360 / slices;
        let currentAngle = 0;
        
        for (let i = 0; i < slices; i++) {
            const slice = createPieSlice(50, 50, 50, currentAngle, currentAngle + sliceAngle, colors[i % colors.length]);
            pieChart.appendChild(slice);
            currentAngle += sliceAngle;
        }
        fractionLabel.innerHTML = `<sup>1</sup>&frasl;<sub>${slices}</sub>`;
    }

    unitControls.addEventListener('click', (e) => {
        if (e.target.classList.contains('slice-btn')) {
            const numSlices = parseInt(e.target.dataset.slices, 10);
            drawPie(numSlices);
            
            sliceButtons.forEach(btn => btn.classList.remove('active'));
            e.target.classList.add('active');
        }
    });
    
    // Initial draw
    drawPie(1);
    document.querySelector('.slice-btn[data-slices="1"]').classList.add('active');


    // --- App 4: Quiz ---
    const quizData = [
        {
            question: "בפעולת הכפל, מה התפקיד של המספר 1?",
            options: ["הוא מכפיל כל מספר פי 2", "הוא משאיר כל מספר ללא שינוי", "הוא הופך כל מספר ל-0", "אין לו תפקיד מיוחד"],
            correctAnswer: "הוא משאיר כל מספר ללא שינוי"
        },
        {
            question: "איך נוצר המספר 4 בעזרת המספר 1?",
            options: ["1 + 3", "1 × 4", "1 + 1 + 1 + 1", "2 + 2"],
            correctAnswer: "1 + 1 + 1 + 1"
        },
        {
            question: "המספר 1 מייצג רעיון של...",
            options: ["חצי", "אינסוף", "שלם או יחידה", "כלום"],
            correctAnswer: "שלם או יחידה"
        },
        {
            question: "אם נכפיל 987 ב-1, מה תהיה התוצאה?",
            options: ["1", "988", "0", "987"],
            correctAnswer: "987"
        }
    ];

    const quizContainer = document.getElementById('quiz-container');
    const quizQuestionEl = document.getElementById('quiz-question');
    const quizOptionsEl = document.getElementById('quiz-options');
    const quizFeedbackEl = document.getElementById('quiz-feedback');
    const quizNextBtn = document.getElementById('quiz-next-btn');
    const quizResultsEl = document.getElementById('quiz-results');

    let currentQuestionIndex = 0;
    let score = 0;

    function loadQuiz() {
        if (currentQuestionIndex < quizData.length) {
            const currentQuestion = quizData[currentQuestionIndex];
            quizQuestionEl.textContent = currentQuestion.question;
            quizOptionsEl.innerHTML = '';
            
            currentQuestion.options.forEach(optionText => {
                const button = document.createElement('button');
                button.textContent = optionText;
                button.classList.add('quiz-option');
                quizOptionsEl.appendChild(button);
            });

            quizFeedbackEl.textContent = '';
            quizNextBtn.style.display = 'none';
        } else {
            showResults();
        }
    }

    function showResults() {
        quizContainer.style.display = 'none';
        quizResultsEl.style.display = 'block';
        quizResultsEl.innerHTML = `סיימת את המבחן!<br>הצלחת ב-${score} מתוך ${quizData.length} שאלות.`;
    }

    quizOptionsEl.addEventListener('click', e => {
        if (e.target.tagName === 'BUTTON') {
            const selectedAnswer = e.target.textContent;
            const correctAnswer = quizData[currentQuestionIndex].correctAnswer;

            const optionButtons = quizOptionsEl.querySelectorAll('.quiz-option');
            optionButtons.forEach(btn => {
                btn.disabled = true;
                if (btn.textContent === correctAnswer) {
                    btn.classList.add('correct');
                } else if (btn.textContent === selectedAnswer) {
                    btn.classList.add('incorrect');
                }
            });

            if (selectedAnswer === correctAnswer) {
                score++;
                quizFeedbackEl.textContent = "נכון!";
                quizFeedbackEl.style.color = 'var(--success-color)';
            } else {
                quizFeedbackEl.textContent = `טעות. התשובה הנכונה היא: ${correctAnswer}`;
                quizFeedbackEl.style.color = 'var(--danger-color)';
            }

            quizNextBtn.style.display = 'block';
        }
    });

    quizNextBtn.addEventListener('click', () => {
        currentQuestionIndex++;
        loadQuiz();
    });

    loadQuiz();
});
</script>