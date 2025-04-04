function factorial(n) {
    if (n === 0 || n === 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }  

window.onload = function(){ 

  let a = ''
  let b = ''
  let expressionResult = ''
  let selectedOperation = null
  
  // окно вывода результата
  outputElement = document.getElementById("result")
  
  // список объектов кнопок циферблата (id которых начинается с btn_digit_)
  digitButtons = document.querySelectorAll('[id ^= "btn_digit_"]')
  
  function onDigitButtonClicked(digit) {
      if (!selectedOperation) {
          if ((digit != '.') || (digit == '.' && !a.includes(digit))) { 
              a += digit
          }
          outputElement.innerHTML = a
      } else {
          if ((digit != '.') || (digit == '.' && !b.includes(digit))) { 
              b += digit
              outputElement.innerHTML = b        
          }
      }
  }
  
  // устанавка колбек-функций на кнопки циферблата по событию нажатия
  digitButtons.forEach(button => {
      button.onclick = function() {
          const digitValue = button.innerHTML
          onDigitButtonClicked(digitValue)
      }
  });
  
  // установка колбек-функций для кнопок операций
  document.getElementById("btn_op_mult").onclick = function() { 
      if (a === '') return
      selectedOperation = 'x'
  }
  document.getElementById("btn_op_plus").onclick = function() { 
      if (a === '') return
      selectedOperation = '+'
  }
  document.getElementById("btn_op_minus").onclick = function() { 
      if (a === '') return
      selectedOperation = '-'
  }
  document.getElementById("btn_op_div").onclick = function() { 
      if (a === '') return
      selectedOperation = '/'
  }
  document.getElementById("btn_op_factorial").onclick = function() {
    if (a === '') return;
    let result = factorial(parseInt(a));
    if (result.toString().includes('e')) {
      result = result.toPrecision(6); // Используем toPrecision для ограничения числа до 6 значащих цифр
    }
    a = result.toString();
    outputElement.innerHTML = a;
  };  
  document.getElementById("btn_op_percent").onclick = function() {
    if (a !== '') {
        if (!selectedOperation) {
            a = (+a) / 100;
            outputElement.innerHTML = a;
        } else if (b !== '') {
            b = (+b) * (+a) / 100;
            outputElement.innerHTML = b;
        }
    }
}  
  
  // кнопка очищения
  document.getElementById("btn_op_clear").onclick = function() { 
      a = ''
      b = ''
      selectedOperation = ''
      expressionResult = ''
      outputElement.innerHTML = 0
  }
  
  // кнопка расчёта результата
  document.getElementById("btn_op_equal").onclick = function() { 
      if (a === '' || b === '' || !selectedOperation)
          return
          
      switch(selectedOperation) { 
          case 'x':
              expressionResult = (+a) * (+b)
              break;
          case '+':
              expressionResult = (+a) + (+b)
              break;
          case '-':
              expressionResult = (+a) - (+b)
              break;
          case '/':
              expressionResult = (+a) / (+b)
              break;
      }
      
      a = expressionResult.toString()
      b = ''
      selectedOperation = null
  
      outputElement.innerHTML = a
  }
  };