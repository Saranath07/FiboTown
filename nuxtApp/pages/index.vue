<template>
    <div class="game-container">
      <div class="game-header text-center">
        <h1 class="game-title">Welcome to FiboTown</h1>
        <p class="game-rules">
          The Rules of the game are as follows:
          <br>
          There will be 2 sets of resources:
          <br>
          1. Fibonacci resources 
          <br>
          2. Odd Town resources 
          <br><br>
          <strong>Your Goal:</strong>
          <br>
          Choose any number from each of the resources, say m for Fibonacci and n for Odd Town.
          <br>
          Note: m should be a Fibonacci number, and you can use the calculator wisely to check if the number is Fibonacci.
          <br>
          You have to frame an Odd Town, i.e., the number of people in each club is an odd number where there are totally m people.
          <br>
          Every pair intersection of the clubs should have an even number of people.
        </p>
      </div>
      <div class="game-start flex justify-center items-center">
        <button @click="start" class="start-button">Start</button>
      </div>
      <div class="game-status text-center">
        <h1 class="status-message">{{name}}</h1>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  
  const name = ref("");
  const route = useRoute();
  const router = useRouter();
  
  function start() {
    // alert("Starting..");
    name.value = "Game is starting..";
    router.push("/resources");
  }
  </script>
  
  <style scoped>
  body {
    background-color: #f0f8ff;
    font-family: 'Comic Sans MS', 'Comic Sans', cursive;
    color: #333;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .game-container {
    text-align: center;
    background-color: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .game-header {
    margin-bottom: 20px;
  }
  
  .game-title {
    font-size: 2.5em;
    color: #4a90e2;
  }
  
  .game-rules {
    font-size: 1.2em;
    line-height: 1.5;
    color: #555;
  }
  
  .start-button {
    background-color: #ff7f50;
    color: white;
    padding: 15px 30px;
    border: none;
    border-radius: 50px;
    font-size: 1.2em;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .start-button:hover {
    background-color: #ff4500;
  }
  
  .status-message {
    margin-top: 20px;
    font-size: 1.5em;
    color: #333;
  }
  </style>
  