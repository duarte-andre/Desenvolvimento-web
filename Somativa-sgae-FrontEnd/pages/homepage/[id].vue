<script setup>
const route = useRoute();

const{data:user} = await useFetch(`http://localhost:8000/usuarios/${route.params.id}`)

const { data: tarefaFound } = await useFetch(`http://localhost:8000/tarefas/${route.params.id}`, {
    key: 'tarefaRequest'
});


</script>

<template>
    <div>
      <h1>Olá {{ user.data.nome }}</h1>
      <br>
      <section>
        
      
    </section>
      
    </div>
  </template>
  
