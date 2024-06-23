<template>
    <div class="gameplay-container">
      <h1 class="text-center title">Game Play</h1>
      <div class="boxes">
        <div
          v-for="(box, index) in oddTown"
          :key="index"
          class="box"
        >
          <h2>Town {{ index + 1 }}</h2>
          <div class="sub-boxes">
            <button
              v-for="n in fibonacci"
              :key="n"
              :class="{ selected: selectedSubBoxes[index].includes(n) }"
              @click="toggleSelection(index, n)"
            >
              {{ n }}
            </button>
          </div>
          <!-- <button class="select-all-button" @click="selectAll(index)">Select All</button> -->
        </div>
      </div>
      <div class="button-group text-center">
        <button class="submit-button" @click="evaluateSelections">Submit</button>
        <button class="back-button" @click="goBack">Back</button>
      </div>
      <div v-if="resultMessage" class="result-message">{{ resultMessage }}</div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  const oddTown = ref([]);
  const fibonacci = ref([]);
  const selectedSubBoxes = ref([]);
  const resultMessage = ref('');
  
  onMounted(() => {
    const storedResources = JSON.parse(sessionStorage.getItem('selectedResources'));
    if (storedResources) {
      oddTown.value = Array.from({ length: storedResources.oddTown }, (_, i) => i + 1);
      fibonacci.value = Array.from({ length: storedResources.fibonacci }, (_, i) => i + 1);
      selectedSubBoxes.value = Array.from({ length: storedResources.oddTown }, () => []);
    } else {
      alert('No game data found. Please select resources first.');
      router.push('/');
    }
  });
  
  function toggleSelection(boxIndex, subBoxValue) {
    const selected = selectedSubBoxes.value[boxIndex];
    const index = selected.indexOf(subBoxValue);
    if (index === -1) {
      selected.push(subBoxValue);
    } else {
      selected.splice(index, 1);
    }
  }
  
  function selectAll(boxIndex) {
    selectedSubBoxes.value[boxIndex] = [...fibonacci.value];
  }
  
  function goBack() {
    sessionStorage.clear();
    router.push('/');
  }
  
  function evaluateSelections() {
    let isValid = true;
    const clubSizes = selectedSubBoxes.value.map(club => club.length);
  
    // Check if all club sizes are odd
    isValid = clubSizes.every(size => size % 2 !== 0);
  
    // Check if every pair intersection is even
    if (isValid) {
      for (let i = 0; i < selectedSubBoxes.value.length; i++) {
        for (let j = i + 1; j < selectedSubBoxes.value.length; j++) {
          const intersectionSize = selectedSubBoxes.value[i].filter(x => selectedSubBoxes.value[j].includes(x)).length;
          if (intersectionSize % 2 !== 0) {
            isValid = false;
            break;
          }
        }
        if (!isValid) break;
      }
    }
  
    resultMessage.value = isValid ? 'Valid Odd Town!' : 'Invalid Odd Town. Please try again.';
  }
  </script>
  
  <style scoped>
  body {
    font-family: Arial, sans-serif;
    background-color: #87CEEB;
    margin: 0;
    padding: 0;
  }
  
  .title {
    font-size: 2.5em;
    color: #4a90e2;
  }
  
  .gameplay-container {
    max-width: 800px;
    margin: auto;
    padding: 50px;
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .text-center {
    text-align: center;
  }
  
  .boxes {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
  }
  
  .box {
    background: #f0f8ff;
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: 80px; /* Smaller width */
    text-align: center;
    position: relative;
  }
  
  .sub-boxes {
    display: flex;
    flex-wrap: wrap;
    gap: 3px; /* Smaller gap */
    justify-content: center;
    margin-top: 10px;
  }
  
  .sub-boxes button {
    background-color: red;
    color: white;
    border: none;
    padding: 3px; /* Smaller padding */
    border-radius: 3px;
    cursor: pointer;
    transition: background-color 0.3s;
    width: 20px; /* Smaller width */
    height: 20px; /* Smaller height */
    font-size: 0.7em; /* Smaller font size */
  }
  
  .sub-boxes button.selected {
    background-color: green;
  }
  
  .sub-boxes button:hover {
    opacity: 0.8;
  }
  
  .select-all-button {
    background-color: #ffa500;
    color: white;
    border: none;
    padding: 5px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    font-size: 0.3em;
    margin-top: 10px;
    position: absolute;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
  }
  
  .select-all-button:hover {
    background-color: #ff8c00;
  }
  
  .button-group {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 20px;
  }
  
  .submit-button, .back-button {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .submit-button:hover, .back-button:hover {
    background-color: #218838;
  }
  
  .back-button {
    background-color: #ff5c5c;
  }
  
  .back-button:hover {
    background-color: #ff1a1a;
  }
  
  .result-message {
    margin-top: 20px;
    text-align: center;
    font-size: 1.2em;
    font-weight: bold;
    color: #333;
  }
  </style>
  