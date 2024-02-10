<script setup>

    const route = useRoute();
    const{data:favoritReceived} = await useFetch(`http://localhost:8000/favoritos?usuario=${route.params.id}`);
    const{data:categoriasReceived}= await useFetch(`http://localhost:8000/categoria`);

let showForm = false;

const setShowForm = () => {
    showForm = true;
    refreshNuxtData();
}

let FkFilme;
let FkUser;

const sendForm = async () =>{
    console.log("FkFilme",FkFilme);
    console.log("FkUser",FkUser);

    await useFetch('http://localhost:8000/favoritos/',{
        method: 'POST',
        body:[{
            idFilmeFK: FkFilme,
            idUsuarioFK: route.params.id
        }]
    })
};
</script>

<template>
    <div>
        <div v-for="favoritValues in favoritReceived" :key="favoritValues.id">
     
     <h3>Filme : </h3>
     <h3>id: {{ favoritValues.idFilmeFK.id }}</h3>
     <img :src="'http://localhost:8000'+favoritValues.idFilmeFK.banner" alt="">
     <h3>nome: {{ favoritValues.idFilmeFK.nome }}</h3>
     <h3>Categoria: {{categoriasReceived.find(category => category.id === favoritValues.idFilmeFK.idCategoriaFK).nome }}</h3>
     <h3>descricao: {{ favoritValues.idFilmeFK.descricao }}</h3><br>
    </div>
    <button @click="setShowForm">Adicionar Favoritos</button>

    <section v-if="showForm === true"> 
        <div><label for="">Filme</label><input type="number" v-model="FkFilme"></div>
        <button @click="sendForm">Salvar Favoritos</button>
    </section>
    </div>
     
</template>