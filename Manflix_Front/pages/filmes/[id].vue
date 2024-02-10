<script setup>
    const route = useRoute();
    const{data:filmesResult} = await useFetch(`http://localhost:8000/filmes/${route.params.id}`);
</script>

<template>
    <div>
        <img :src="'http://localhost:8000/'+filmesResult.banner" alt="">
        <h2>{{ filmesResult.nome }}</h2>
        <br>
        <h3>{{ filmesResult.descricao }}</h3>
        <h3>Categorias: {{ filmesResult.idCategoriaFK.nome }}</h3>
         
    </div>
</template>







