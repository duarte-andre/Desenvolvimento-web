<!--FAVORITOS-->

<script setup>
const{data:favoritReceived} = await useFetch(`http://localhost:8000/favoritos`);
const{data:categoriasReceived}= await useFetch(`http://localhost:8000/categoria`);
</script>

<template>
    <div>
        <h1>Os Filmes Favoritos</h1>

        <div v-for="favoritValues in favoritReceived" :key="favoritValues.id">

            <div>
                <h3>Filme : </h3>
                <h3>id: {{ favoritValues.idFilmeFK.id }}</h3>
                <h3>nome: {{ favoritValues.idFilmeFK.nome }}</h3>
                <h3>Categoria: {{categoriasReceived.find(category => category.id === favoritValues.idFilmeFK.idCategoriaFK).nome }}</h3>
                <h3>descricao: {{ favoritValues.idFilmeFK.descricao }}</h3>

            </div>  <br>

            <div>
                <h3>Usuario : </h3>
                <h3>id: {{favoritValues.idUsuarioFK.id}}</h3>
                <h3>nome: {{favoritValues.idUsuarioFK.nome}}</h3>
                <h3>cpf: {{favoritValues.idUsuarioFK.cpf}}</h3>
            </div><br>
        </div>
    </div>
    

</template>