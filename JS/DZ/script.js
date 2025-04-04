function solve(expression, x) {
    const preparedExpression = expression.replace(/x/g, x);
    
    try {
        const result = eval(preparedExpression);
        return result;
    } catch (e) {
        console.error("Invalid expression");
        return null;
    }
}

function displayResult(expression, x) {
    const result = solve(expression, x);
    const resultText = `Expression: "${expression}", x: ${x} => Result: ${result}`;
    
    const p = document.createElement('p');
    p.textContent = resultText;
    
    document.getElementById('results').appendChild(p);
}

displayResult("2 * x + 3", 5); // 13
displayResult("(x + 2) * 3 - x", 4); // 10
displayResult("10 - x * 2", 3); // 4
displayResult("x * (x + 1)", 7); // 56
