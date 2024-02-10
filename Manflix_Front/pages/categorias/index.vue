<!--CATEGORIAS-->

<script setup>
    const{data:categoriasReceived}= await useFetch(`http://localhost:8000/categoria`);
</script>

<template>
    <div>
        <h1>Categorias de Filmes e Séries</h1>
        <div v-for="CategoryValues in categoriasReceived" :key="CategoryValues.id">
            <h3>{{ CategoryValues.nome }}</h3>
        </div>
    </div>
    
</template>