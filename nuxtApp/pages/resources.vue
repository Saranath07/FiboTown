<template>
    <div class="resources-container">
      <h1 class="text-center">Select Your Resources</h1>
      <div class="resources-section">
        <h2>Fibonacci Resources</h2>
        <div class="resource-buttons">
          <button v-for="(resource, index) in fibonacciResources" :key="index" @click="selectResource(resource, 'fibonacci')">
            {{ resource }}
          </button>
        </div>
      </div>
      <div class="resources-section">
        <h2>Odd Town Resources</h2>
        <div class="resource-buttons">
          <button v-for="(resource, index) in oddTownResources" :key="index" @click="selectResource(resource, 'oddTown')">
            {{ resource }}
          </button>
        </div>
      </div>
      <div class="calculator-section">
        <h2>Fibonacci Calculator</h2>
        <label for="fibInput">Enter a number:</label>
        <input type="number" id="fibInput" v-model="fibInput" @input="displayFibonacci">
        <div class="latex-space"></div>
        <MDC :value="matrixDisplay" class="latex-display"/>
      </div>
      <div class="text-center">
        <button class="next-button" @click="proceed">Next</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  // import 'katex/dist/katex.min.css'; // Import KaTeX CSS
  // import Katex from 'vue-katex'; // Import vue-katex component
  
  const router = useRouter();
  const fibInput = ref(0);
  const fibonacciResources = ref(generateFibonacciResources());
  const oddTownResources = ref(generateOddTownResources());
  let selectedResources = { fibonacci: null, oddTown: null };
  const matrixDisplay = ref('');
  
  function selectResource(resource, type) {
    selectedResources[type] = resource;
    alert(`Selected ${type} resource: ${resource}`);
  }
  
  function proceed() {
    if (selectedResources.fibonacci && selectedResources.oddTown) {
      router.push('/nextPage');
    } else {
      alert('Please select resources from both sections');
    }
  }
  
  function multiplyMatrices(a, b) {
    return [
      [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
      [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
    ];
  }
  
  function matrixPower(matrix, n) {
    if (n === 0) return [[1, 0], [0, 1]]; 
    if (n === 1) return matrix; 
    if (n % 2 === 0) {
      const halfPower = matrixPower(matrix, n / 2);
      return multiplyMatrices(halfPower, halfPower);
    } else {
      return multiplyMatrices(matrix, matrixPower(matrix, n - 1));
    }
  }
  
  function fibonacci(n) {
    if (n === 0) return 0;
    if (n === 1) return 1;
  
    const M = [[1, 1], [1, 0]];
    const resultMatrix = matrixPower(M, n - 1);
  
    return resultMatrix[0][0];
  }
  
  function displayFibonacci() {
    const n = parseInt(fibInput.value);
    const fibN = fibonacci(n);
  
    const M = '$\\mathbf{M} = \\begin{bmatrix} 1 & 1 \\\\ 1 & 0 \\end{bmatrix}$';
    const resultMatrix = matrixPower([[1, 1], [1, 0]], n - 1);
    const resultLatex = `$\\mathbf{M}^{${n-1}} = \\begin{bmatrix} ${resultMatrix[0][0]} & ${resultMatrix[0][1]} \\\\ ${resultMatrix[1][0]} & ${resultMatrix[1][1]} \\end{bmatrix}$`;
    matrixDisplay.value = `${M} $\\quad \\Rightarrow \\quad$ ${resultLatex}`;
  }
  
  function threeDigitFibonacci() {
    let fibs = [];
    let a = 0, b = 1;
    while (b < 100) {
      if (b >= 10) {
        fibs.push(b);
      }
      [a, b] = [b, a + b];
    }
    return fibs;
  }
  
  function generateFibonacciResources() {
    const fibonacciNumbers = threeDigitFibonacci();
    const selectedFibonacci = fibonacciNumbers.sort(() => 0.5 - Math.random()).slice(0, 3);
    const randomNumbers = Array.from({ length: 4 }, () => Math.floor(Math.random() * (100 - 10 + 1)) + 10);
    const result = selectedFibonacci.concat(randomNumbers).sort(() => 0.5 - Math.random());
    return result;
  }
  
  function generateOddTownResources() {
    return Array.from({ length: 3 }, () => Math.floor(Math.random() * (10 - 4 + 1)) + 4);
  }
  </script>
  
  <style scoped>
  body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    margin: 0;
    padding: 0;
  }
  
  .resources-container {
    max-width: 800px;
    margin: auto;
    padding: 20px;
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .text-center {
    text-align: center;
  }
  
  .resources-section {
    margin: 20px 0;
  }
  
  .resource-buttons {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
  }
  
  .resource-buttons button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 20px;
    margin: 5px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .resource-buttons button:hover {
    background-color: #0056b3;
  }
  
  .calculator-section {
    text-align: center;
    margin: 20px 0;
  }
  
  .latex-space {
    margin-top: 10px;
  }
  
  .latex-display {
    font-size: 1.5em;
    margin-top: 10px;
  }
  
  .next-button {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .next-button:hover {
    background-color: #218838;
  }
  </style>
  