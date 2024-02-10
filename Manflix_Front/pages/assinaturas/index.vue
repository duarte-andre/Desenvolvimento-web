<!--ASSINATURAS-->

<script setup>
    const{data:assinaturasReceived}= await useFetch(`http://127.0.0.1:8000/assinatura/`);
</script>
<template>
    <div>
        <h1>Assinaturas de MangeFlix</h1>

        <div v-for="assinaturaValues in assinaturasReceived" :key="assinaturaValues.id">
            <h3>{{ assinaturaValues.nome }}</h3>
            <h3>{{ assinaturaValues.valor }}</h3><br>   

        </div>
    </div>
    
</template>