<script setup lang="ts">
import { ref } from 'vue'

const text = ref('(ready)')
const textToWrite = ref('')

const readText = () => {
  fetch('http://localhost:12345/text/read')
   .then((res) => res.json())
    .then((data) => {
      text.value = `Text from server: ${data['content']}`
    })
    .catch((err) => {
      text.value = `Error: ${text}`
    })
}

const writeText = () => {
  if (textToWrite.value.length === 0) {
    text.value = 'Error: No text specified'
    return
  }

  fetch('http://localhost:12345/text/write', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ new_content: textToWrite.value })
  })
    .then((res) => res.json())
    .then((data) => {
      text.value = `Wrote: ${data['new_content']}`
    })
    .catch((err) => {
      text.value = `Error: ${text}`
    })
}
</script>


<template>
  <div class="max-w-[1280px] min-w-3xl">
    <h1>My beautiful app</h1>

    <h2 class="pt-8">Current response from server</h2>
    <p data-testid="server-response">{{ text }}</p>

    <h2 class="pt-8">Read text</h2>
    <button
      @click="readText"
      data-testid="read-text-button"
      class="bg-pink-500 text-white px-4 py-2 rounded-full hover:bg-pink-600 transition-colors cursor-pointer">
      Read text from server
    </button>

    <h2 class="pt-8">Write text</h2>
    <input
      v-model="textToWrite"
      data-testid="write-text-input"
      class="block w-full mb-4 border border-gray-300 rounded-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-pink-500" />
    <button
      @click="writeText"
      data-testid="write-text-button"
      class="block bg-pink-500 text-white px-4 py-2 rounded-full hover:bg-pink-600 transition-colors cursor-pointer">
      Write text to server
    </button>
  </div>
</template>
