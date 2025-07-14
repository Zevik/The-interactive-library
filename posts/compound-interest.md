---
title: "ריבית דריבית"
category: "מדעי החברה / כלכלה וסוציולוגיה"
tags: [כלכלה, ריבית, חיסכון, השקעות, ריבית דריבית, צמיחה מעריכית]
---

# ריבית דריבית: כוחה של הצמיחה המעריכית

ריבית דריבית מכונה לעיתים "הפלא השמיני של העולם". בניגוד לריבית פשוטה, שמחושבת רק על הקרן (הסכום המקורי), ריבית דריבית מחושבת על הקרן **וגם** על הריבית שהצטברה בתקופות קודמות. התוצאה היא אפקט של "כדור שלג": הכסף שלך מתחיל לעבוד בשבילך וליצור כסף נוסף בקצב הולך וגובר.

## מטרת המחשבון

המחשבון הוויזואלי הזה מדגים את ההבדל העצום בין חיסכון עם ריבית פשוטה לבין חיסכון עם ריבית דריבית לאורך זמן. שנו את הפרמטרים (סכום התחלתי, ריבית שנתית, מספר שנים והפקדה חודשית) וראו כיצד הפער גדל בצורה דרמטית. הגרף והטבלה מתעדכנים בזמן אמת כדי להמחיש את העוצמה של צמיחה מעריכית.

<!-- Compound Interest Calculator App -->
<div id="compoundInterestApp">
  <div class="controls">
    <div class="control-group">
      <label for="initialAmount">סכום התחלתי (₪)</label>
      <input type="number" id="initialAmount" value="10000" min="0">
    </div>
    <div class="control-group">
      <label for="annualRate">ריבית שנתית (%)</label>
      <input type="number" id="annualRate" value="7" min="0" step="0.1">
    </div>
    <div class="control-group">
      <label for="years">מספר שנים</label>
      <input type="number" id="years" value="30" min="1" max="50">
    </div>
    <div class="control-group">
      <label for="monthlyContribution">הפקדה חודשית (₪)</label>
      <input type="number" id="monthlyContribution" value="500" min="0">
    </div>
  </div>
  <div class="outputs">
    <div class="chart-container">
      <canvas id="interestChart"></canvas>
    </div>
    <div class="summary">
      <div class="summary-item simple">
        <h4>סך הכל עם ריבית פשוטה</h4>
        <p id="simpleTotal">₪0</p>
      </div>
      <div class="summary-item compound">
        <h4>סך הכל עם ריבית דריבית</h4>
        <p id="compoundTotal">₪0</p>
      </div>
    </div>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>שנה</th>
            <th>סך הפקדות</th>
            <th>סכום (ריבית דריבית)</th>
          </tr>
        </thead>
        <tbody id="resultsTable">
        </tbody>
      </table>
    </div>
  </div>
</div>

<style>
  #compoundInterestApp {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    max-width: 800px;
    margin: 2rem auto;
    padding: 1.5rem;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    direction: rtl;
  }
  .controls {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
  }
  .control-group {
    display: flex;
    flex-direction: column;
  }
  .control-group label {
    font-size: 0.9rem;
    color: #555;
    margin-bottom: 0.4rem;
  }
  .control-group input {
    width: 100%;
    padding: 0.6rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
    box-sizing: border-box;
  }
  .outputs {
    width: 100%;
  }
  .chart-container {
    position: relative;
    height: 300px;
    margin-bottom: 2rem;
  }
  .summary {
    display: flex;
    justify-content: space-around;
    text-align: center;
    margin-bottom: 2rem;
    gap: 1rem;
  }
  .summary-item {
    flex: 1;
    padding: 1rem;
    border-radius: 6px;
  }
  .summary-item.simple {
    background-color: #e0f0ff;
  }
  .summary-item.compound {
    background-color: #d4f7e0;
  }
  .summary h4 {
    margin: 0 0 0.5rem 0;
    font-size: 1rem;
    color: #333;
  }
  .summary p {
    margin: 0;
    font-size: 1.5rem;
    font-weight: bold;
  }
  .summary-item.simple p { color: #005a9e; }
  .summary-item.compound p { color: #0d6a33; }
  .table-container {
    max-height: 300px;
    overflow-y: auto;
    border: 1px solid #ddd;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
  }
  th, td {
    text-align: center;
    padding: 0.75rem 0.5rem;
    border-bottom: 1px solid #eee;
  }
  thead th {
    background-color: #f2f2f2;
    position: sticky;
    top: 0;
  }
  tbody tr:nth-child(even) {
    background-color: #f9f9f9;
  }
  @media (max-width: 600px) {
    #compoundInterestApp {
        padding: 1rem;
    }
    .summary {
        flex-direction: column;
    }
  }
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const initialAmountInput = document.getElementById('initialAmount');
    const annualRateInput = document.getElementById('annualRate');
    const yearsInput = document.getElementById('years');
    const monthlyContributionInput = document.getElementById('monthlyContribution');
    const resultsTableBody = document.getElementById('resultsTable');
    const simpleTotalEl = document.getElementById('simpleTotal');
    const compoundTotalEl = document.getElementById('compoundTotal');

    const canvas = document.getElementById('interestChart');
    const ctx = canvas.getContext('2d');
    let chartInstance = null;

    function calculateAndDisplay() {
        const principal = parseFloat(initialAmountInput.value) || 0;
        const annualRate = parseFloat(annualRateInput.value) / 100 || 0;
        const years = parseInt(yearsInput.value) || 0;
        const monthlyContribution = parseFloat(monthlyContributionInput.value) || 0;

        let compoundFutureValue = principal;
        let simpleInterestTotal = principal;
        let totalContributions = principal;
        
        const compoundData = [];
        const simpleData = [];
        const labels = [];
        const contributionData = [];

        for (let i = 1; i <= years; i++) {
            let yearlyContribution = monthlyContribution * 12;
            let compoundInterestForYear = (compoundFutureValue + yearlyContribution) * annualRate;
            compoundFutureValue += yearlyContribution + compoundInterestForYear;

            simpleInterestTotal += (principal + (i * yearlyContribution)) * annualRate + yearlyContribution;
            totalContributions += yearlyContribution;

            labels.push(`שנה ${i}`);
            compoundData.push(compoundFutureValue);
            simpleData.push(simpleInterestTotal);
            contributionData.push(totalContributions);
        }

        updateTable(years, principal, monthlyContribution, compoundData);
        updateSummary(simpleInterestTotal, compoundFutureValue);
        drawChart(labels, compoundData, simpleData, contributionData);
    }
    
    function updateSummary(simple, compound) {
        const formatCurrency = (val) => `₪${Math.round(val).toLocaleString()}`;
        simpleTotalEl.textContent = formatCurrency(simple);
        compoundTotalEl.textContent = formatCurrency(compound);
    }

    function updateTable(years, principal, monthlyContribution, compoundValues) {
        resultsTableBody.innerHTML = '';
        for (let i = 0; i < years; i++) {
            const year = i + 1;
            const totalDeposits = principal + (monthlyContribution * 12 * year);
            const row = `
                <tr>
                    <td>${year}</td>
                    <td>${Math.round(totalDeposits).toLocaleString()}</td>
                    <td>${Math.round(compoundValues[i]).toLocaleString()}</td>
                </tr>
            `;
            resultsTableBody.innerHTML += row;
        }
    }
    
    function drawChart(labels, compoundData, simpleData, contributionData) {
        const parent = canvas.parentElement;
        canvas.width = parent.clientWidth;
        canvas.height = parent.clientHeight;

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const allValues = [...compoundData, ...simpleData, ...contributionData];
        const maxValue = Math.max(...allValues);
        const padding = 50;
        const chartWidth = canvas.width - padding * 2;
        const chartHeight = canvas.height - padding * 2;
        const xStep = chartWidth / (labels.length - 1 || 1);
        const yStep = chartHeight / maxValue;

        const plot = (data, color) => {
            ctx.beginPath();
            ctx.strokeStyle = color;
            ctx.lineWidth = 3;
            ctx.moveTo(padding, canvas.height - padding - data[0] * yStep);
            data.forEach((point, i) => {
                ctx.lineTo(padding + i * xStep, canvas.height - padding - point * yStep);
            });
            ctx.stroke();
        };

        // Draw Axes
        ctx.beginPath();
        ctx.strokeStyle = '#aaa';
        ctx.lineWidth = 1;
        // Y-Axis
        ctx.moveTo(padding, padding / 2);
        ctx.lineTo(padding, canvas.height - padding);
        // X-Axis
        ctx.lineTo(canvas.width - padding / 2, canvas.height - padding);
        ctx.stroke();

        // Draw data lines
        plot(simpleData, '#3b82f6'); // Blue for simple
        plot(compoundData, '#16a34a'); // Green for compound
        plot(contributionData, '#888'); // Gray for contributions

        // Draw Legend
        const drawLegendItem = (text, color, x, y) => {
             ctx.fillStyle = color;
             ctx.fillRect(x, y - 10, 10, 10);
             ctx.fillStyle = '#333';
             ctx.font = '12px Arial';
             ctx.fillText(text, x + 15, y);
        };
        drawLegendItem('ריבית דריבית', '#16a34a', padding, 20);
        drawLegendItem('ריבית פשוטה', '#3b82f6', padding + 120, 20);
        drawLegendItem('סך הפקדות', '#888', padding + 240, 20);
    }

    [initialAmountInput, annualRateInput, yearsInput, monthlyContributionInput].forEach(input => {
        input.addEventListener('input', calculateAndDisplay);
    });
    
    // Initial calculation on load
    calculateAndDisplay();
});
</script>